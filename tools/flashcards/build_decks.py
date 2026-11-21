#!/usr/bin/env python3
"""Build every flashcard deck in the repo.

A deck is any JSON file (outside tools/ and .git/) with "schema_version": "2.0" and a "cards" list,
following tools/flashcards/deck.schema.json. Each deck lives in its own folder. For each deck this writes,
next to the JSON file:

    README.md            clickable cards, readable on GitHub and on the website
    <name>.apkg          Anki package (needs genanki)
    <name>_quizlet.txt   Quizlet import file (tab-separated, no images)
    <name>.org           Emacs org-drill file

and it writes flashcards/index.json, which the web study page (flashcards/index.html) reads.

Usage:
    python3 tools/flashcards/build_decks.py            # build everything
    python3 tools/flashcards/build_decks.py --check    # validate only, write nothing

Install the optional dependencies with:  pip install -r tools/flashcards/requirements.txt
Without genanki the .apkg files are skipped; without jsonschema only the basic checks run.
"""
import argparse
import hashlib
import html
import json
import os
import re
import shutil
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCHEMA = os.path.join(ROOT, "tools", "flashcards", "deck.schema.json")
SITE = "https://webnrrd2k.github.io/lbcc-electrical-study-materials"
CLOZE = re.compile(r"\{\{c\d+::(.+?)(?:::(.*?))?\}\}")


# ---------------------------------------------------------------- discovery and validation

def find_decks():
    decks = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        rel = os.path.relpath(dirpath, ROOT)
        if rel.split(os.sep)[0] in (".git", "tools", "flashcards", "_site"):
            dirnames[:] = []
            continue
        for fn in filenames:
            if not fn.endswith(".json"):
                continue
            path = os.path.join(dirpath, fn)
            try:
                with open(path, encoding="utf-8") as fh:
                    data = json.load(fh)
            except (ValueError, UnicodeDecodeError):
                continue
            if isinstance(data, dict) and data.get("schema_version") == "2.0" and "cards" in data:
                decks.append((path, data))
    return sorted(decks, key=lambda d: d[0])


def validate(path, deck, all_ids):
    errors = []
    try:
        import jsonschema
        with open(SCHEMA, encoding="utf-8") as fh:
            schema = json.load(fh)
        for err in jsonschema.Draft202012Validator(schema).iter_errors(deck):
            errors.append(f"schema: {'/'.join(map(str, err.path))}: {err.message}")
    except ImportError:
        pass
    base = os.path.dirname(path)
    prefix = deck.get("deck_id", "") + "-"
    retired = set(deck.get("retired_ids", []))
    for c in deck.get("cards", []):
        cid = c.get("id", "?")
        if not cid.startswith(prefix):
            errors.append(f"{cid}: id must start with '{prefix}'")
        if cid in all_ids:
            errors.append(f"{cid}: duplicate id (also in {all_ids[cid]})")
        if cid in retired:
            errors.append(f"{cid}: id is listed in retired_ids")
        all_ids[cid] = os.path.relpath(path, ROOT)
        if c.get("image") and not os.path.exists(os.path.join(base, c["image"])):
            errors.append(f"{cid}: image not found: {c['image']}")
        if c.get("type") == "mcq" and not (0 <= c.get("answer", -1) < len(c.get("choices", []))):
            errors.append(f"{cid}: mcq answer index out of range")
        if c.get("type") == "cloze" and not CLOZE.search(c.get("front", "")):
            errors.append(f"{cid}: cloze card has no {{{{c1::...}}}} marker")
        text = " ".join(str(c.get(k, "")) for k in ("front", "back", "note"))
        if "{%" in text:
            errors.append(f"{cid}: '{{%' would break the website (Jekyll/Liquid)")
        if c.get("type") != "cloze" and "{{" in text:
            errors.append(f"{cid}: '{{{{' would break the website (Jekyll/Liquid)")
        if deck.get("format") == "text" and text.count("$") >= 2:
            errors.append(f"{cid}: two or more '$' signs would be read as math on the website")
    return errors


# ---------------------------------------------------------------- rendering (mirrored in flashcards/index.html)

def _txt(deck, s):
    s = s or ""
    if deck.get("format") == "html":
        return s
    return html.escape(s).replace("\n", "<br>")


def _img(c, base_url=""):
    if not c.get("image"):
        return ""
    alt = html.escape(c.get("image_alt", ""))
    return f'<img src="{base_url}{c["image"]}" alt="{alt}">'


def question_html(deck, c, base_url=""):
    if c["type"] == "cloze":
        q = _txt(deck, CLOZE.sub(lambda m: "[" + (m.group(2) or "...") + "]", c["front"]))
    else:
        q = _txt(deck, c["front"])
    if c["type"] == "mcq":
        q += "<br>" + "<br>".join(f"<b>{'ABCDE'[i]}.</b> {_txt(deck, ch)}" for i, ch in enumerate(c["choices"]))
    if c.get("image_on_front"):
        q += "<br>" + _img(c, base_url)
    return q


def answer_html(deck, c, base_url=""):
    if c["type"] == "cloze":
        parts, last = [], 0
        for m in CLOZE.finditer(c["front"]):
            parts.append(_txt(deck, c["front"][last:m.start()]))
            parts.append("<b>" + _txt(deck, m.group(1)) + "</b>")
            last = m.end()
        parts.append(_txt(deck, c["front"][last:]))
        a = "".join(parts)
        if c.get("back"):
            a += "<br>" + _txt(deck, c["back"])
    elif c["type"] == "mcq":
        i = c["answer"]
        a = f"<b>{'ABCDE'[i]}. {_txt(deck, c['choices'][i])}</b>"
        if c.get("back"):
            a += "<br>" + _txt(deck, c["back"])
    else:
        a = _txt(deck, c["back"])
    if c.get("image") and not c.get("image_on_front"):
        a += "<br>" + _img(c, base_url)
    extras = []
    if c.get("note"):
        extras.append(_txt(deck, c["note"]))
    if c.get("nec_ref"):
        extras.append("NEC " + html.escape(c["nec_ref"]))
    if extras:
        a += "<br><br><sub>" + " · ".join(extras) + "</sub>"
    return a


def sections(deck):
    order, groups = [], {}
    for c in deck["cards"]:
        s = c.get("section") or ""
        if s not in groups:
            order.append(s)
            groups[s] = []
        groups[s].append(c)
    return [(s, groups[s]) for s in order]


def slug(text):
    s = re.sub(r"[^\w\- ]", "", text.lower()).strip()
    return re.sub(r"\s", "-", s)


def write_readme(path, deck, stem):
    base = os.path.dirname(path)
    n = len(deck["cards"])
    lines = [f"# Flashcards — {deck['class']}: {deck['deck']}", ""]
    lines.append(f"{n} cards. Read the question, answer it in your head, then click it to check.")
    lines.append("")
    if deck.get("study_guide"):
        lines.append(f"Study guide for these cards: [{os.path.basename(deck['study_guide'])}]({deck['study_guide']}).")
        lines.append("")
    lines.append(f"- **Study online:** [flashcard page]({SITE}/flashcards/?deck={deck['deck_id']}): "
                 "shuffle, flip, and mark the cards you know.")
    lines.append(f"- **Download:** [Anki]({stem}.apkg) · [Quizlet import file]({stem}_quizlet.txt) (paste into Quizlet's "
                 f"Import box; images are not included) · [Emacs org-drill]({stem}.org) · [raw card data]({stem}.json)")
    lines.append("")
    groups = sections(deck)
    named = [g for g in groups if g[0]]
    if len(named) > 1:
        lines.append("## Contents")
        lines.append("")
        for s, cards in named:
            lines.append(f"- [{s}](#{slug(s)}) ({len(cards)})")
        lines.append("")
    lines.append("---")
    lines.append("")
    num = 0
    for s, cards in groups:
        if s and len(named) > 1:
            lines.append(f"## {s}")
            lines.append("")
        for c in cards:
            num += 1
            q = question_html(deck, c)
            a = answer_html(deck, c)
            lines.append(f"<details><summary><b>{num}.</b> {q}</summary><br>{a}<br><br></details>")
            lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Generated by `tools/flashcards/build_decks.py` from the JSON file. Edit the JSON, not this page.*")
    out = "\n".join(lines) + "\n"
    if "{{" in out or "{%" in out:
        raise SystemExit(f"{path}: rendered README contains '{{{{' or '{{%', which breaks the website")
    with open(os.path.join(base, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(out)


# ---------------------------------------------------------------- Quizlet

def _flat(s):
    s = re.sub(r"<br\s*/?>", " ", s or "")
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s.replace("\t", " ")).strip()


def write_quizlet(path, deck, stem):
    out = []
    for c in deck["cards"]:
        if c.get("image_on_front"):
            continue  # the question is the picture, and Quizlet's text import has no pictures
        if c["type"] == "cloze":
            term = CLOZE.sub("_____", c["front"])
            definition = "; ".join(m.group(1) for m in CLOZE.finditer(c["front"]))
            if c.get("back"):
                definition += " - " + c["back"]
        elif c["type"] == "mcq":
            term = c["front"] + " " + " ".join(f"({'ABCDE'[i]}) {ch}" for i, ch in enumerate(c["choices"]))
            definition = f"{'ABCDE'[c['answer']]}. {c['choices'][c['answer']]}" + (" - " + c["back"] if c.get("back") else "")
        else:
            term, definition = c["front"], c["back"]
        if c.get("note"):
            definition += " (" + c["note"] + ")"
        if c.get("nec_ref"):
            definition += f" [NEC {c['nec_ref']}]"
        out.append(f"{_flat(term)}\t{_flat(definition)}")
    with open(os.path.join(os.path.dirname(path), f"{stem}_quizlet.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")


# ---------------------------------------------------------------- Emacs org-drill

def write_org(path, deck, stem):
    out = [f"#+TITLE: {deck['class']} — {deck['deck']}", "#+FILETAGS: :drill:", "#+STARTUP: overview", "",
           "# Generated by tools/flashcards/build_decks.py. Study with M-x org-drill.", ""]
    for s, cards in sections(deck):
        level = "*"
        if s:
            out += [f"* {s}", ""]
            level = "**"
        for c in cards:
            full_q = _flat(question_html(deck, {**c, "image_on_front": False}))
            title = full_q if len(full_q) <= 90 else full_q[:87].rsplit(" ", 1)[0] + "..."
            title = title.replace("[", "(").replace("]", ")")
            out.append(f"{level} {title}")
            out.append(f"   :PROPERTIES:\n   :ID: {c['id']}\n   :END:")
            if c["type"] == "cloze":
                q = CLOZE.sub(lambda m: "[" + m.group(1) + "]", c["front"])  # org-drill cloze syntax
                out.append(_flat(q))
            elif title != full_q.replace("[", "(").replace("]", ")"):
                out.append(full_q)
            if c.get("image") and c.get("image_on_front"):
                out.append(f"[[file:{c['image']}]]")
            out.append(f"{level}* Answer")
            ans = answer_html(deck, {**c, "image_on_front": True})
            out.append(_flat(ans))
            if c.get("image") and not c.get("image_on_front"):
                out.append(f"[[file:{c['image']}]]")
            for src in re.findall(r'<img src="([^"]+)"', ans if deck.get("format") == "html" else ""):
                out.append(f"[[file:{src}]]")
            out.append("")
    with open(os.path.join(os.path.dirname(path), f"{stem}.org"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")


# ---------------------------------------------------------------- Anki

# Fixed ids: never change them, or students who re-import will get duplicate notes.
MODEL_IDS = {"basic": 1840212801, "reverse": 1840212802, "cloze": 1840212803, "mcq": 1840212804}
CSS = """
.card { font-family: -apple-system, Segoe UI, Roboto, sans-serif; font-size: 20px; text-align: left;
        color: #1a1a1a; background: #ffffff; line-height: 1.4; }
.meta { margin-top: 10px; font-size: 13px; color: #777777; }
img { max-width: 100%; height: auto; margin-top: 10px; }
.nightMode .card { color: #eeeeee; background: #1e1e1e; }
"""


def _stable_int(text, lo=1 << 30, hi=1 << 31):
    return lo + int(hashlib.sha1(text.encode()).hexdigest(), 16) % (hi - lo)


def write_anki(path, deck, stem):
    try:
        import genanki
    except ImportError:
        return False
    fields = [{"name": n} for n in ("Front", "Back", "Source", "Id")]
    tmpl = lambda q, a: {"qfmt": q, "afmt": "{{FrontSide}}<hr id=answer>" + a + "<div class=meta>{{Source}}</div>"}
    basic = genanki.Model(MODEL_IDS["basic"], "LBCC Electrical Basic", fields=fields, css=CSS,
                          templates=[{"name": "Card 1", **tmpl("{{Front}}", "{{Back}}")}])
    rev = genanki.Model(MODEL_IDS["reverse"], "LBCC Electrical Basic+Reverse", fields=fields, css=CSS,
                        templates=[{"name": "Forward", **tmpl("{{Front}}", "{{Back}}")},
                                   {"name": "Reverse", **tmpl("{{Back}}", "{{Front}}")}])
    mcq = genanki.Model(MODEL_IDS["mcq"], "LBCC Electrical Multiple Choice", fields=fields, css=CSS,
                        templates=[{"name": "Card 1", **tmpl("{{Front}}", "{{Back}}")}])
    cloze = genanki.Model(MODEL_IDS["cloze"], "LBCC Electrical Cloze", model_type=genanki.Model.CLOZE, css=CSS,
                          fields=[{"name": n} for n in ("Text", "Extra", "Source", "Id")],
                          templates=[{"name": "Cloze", "qfmt": "{{cloze:Text}}",
                                      "afmt": "{{cloze:Text}}<br>{{Extra}}<div class=meta>{{Source}}</div>"}])
    name = f"LBCC Electrical::{deck['class']}::{deck['deck']}"
    adeck = genanki.Deck(_stable_int("lbcc::" + deck["deck_id"]), name)
    base = os.path.dirname(path)
    stage = tempfile.mkdtemp(prefix="flashcards_anki_")
    media = []
    for c in deck["cards"]:
        cc = dict(c)
        if c.get("image"):
            media_name = f"{deck['deck_id']}_{os.path.basename(c['image'])}"
            staged = os.path.join(stage, media_name)
            if staged not in media:
                shutil.copyfile(os.path.join(base, c["image"]), staged)
                media.append(staged)
            cc["image"] = media_name
        # images referenced inline in html decks
        q, a = question_html(deck, cc), answer_html(deck, cc)
        if deck.get("format") == "html":
            for src in set(re.findall(r'src="([^"]+)"', q + a)):
                if src.startswith(("http", deck["deck_id"] + "_")) or not os.path.exists(os.path.join(base, src)):
                    continue
                media_name = f"{deck['deck_id']}_{os.path.basename(src)}"
                staged = os.path.join(stage, media_name)
                if staged not in media:
                    shutil.copyfile(os.path.join(base, src), staged)
                    media.append(staged)
                q, a = q.replace(f'src="{src}"', f'src="{media_name}"'), a.replace(f'src="{src}"', f'src="{media_name}"')
        source = html.escape(f"{deck['class']} · {deck['deck']} · {c['id']}")
        tags = [f"{deck['deck_id']}::{t}" for t in c["tags"]]
        guid = genanki.guid_for(c["id"])
        if c["type"] == "cloze":
            text = _txt(deck, c["front"]) if deck.get("format") == "html" else \
                "".join(p if CLOZE.fullmatch(p) else _txt(deck, p) for p in re.split(r"(\{\{c\d+::.*?\}\})", c["front"]))
            extra = a.split("<br>", 1)[1] if "<br>" in a else ""
            note = genanki.Note(model=cloze, fields=[text, extra, source, c["id"]], tags=tags, guid=guid)
        else:
            model = mcq if c["type"] == "mcq" else (rev if c.get("reverse") else basic)
            note = genanki.Note(model=model, fields=[q, a, source, c["id"]], tags=tags, guid=guid)
        adeck.add_note(note)
    pkg = genanki.Package(adeck)
    pkg.media_files = media
    pkg.write_to_file(os.path.join(base, f"{stem}.apkg"))
    shutil.rmtree(stage, ignore_errors=True)
    return True


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate only")
    args = ap.parse_args()
    decks = find_decks()
    all_ids, problems, dirs = {}, 0, {}
    for path, deck in decks:
        d = os.path.dirname(path)
        if d in dirs:
            print(f"ERROR {os.path.relpath(path, ROOT)}: second deck in {os.path.relpath(d, ROOT)} (one deck per folder)")
            problems += 1
        dirs[d] = path
        for e in validate(path, deck, all_ids):
            print(f"ERROR {os.path.relpath(path, ROOT)}: {e}")
            problems += 1
    if problems:
        sys.exit(f"{problems} problem(s); nothing written.")
    if args.check:
        print(f"OK: {len(decks)} decks, {len(all_ids)} cards.")
        return
    index, apkg = [], 0
    for path, deck in decks:
        stem = os.path.splitext(os.path.basename(path))[0]
        write_readme(path, deck, stem)
        write_quizlet(path, deck, stem)
        write_org(path, deck, stem)
        apkg += write_anki(path, deck, stem)
        index.append({
            "class": deck["class"], "deck": deck["deck"], "deck_id": deck["deck_id"],
            "order": deck.get("order", 0), "format": deck["format"],
            "path": os.path.relpath(path, ROOT).replace(os.sep, "/"),
            "cards": len(deck["cards"]),
            "sections": [s for s, _ in sections(deck) if s],
        })
    index.sort(key=lambda d: (d["class"], d["order"], d["deck"]))
    os.makedirs(os.path.join(ROOT, "flashcards"), exist_ok=True)
    with open(os.path.join(ROOT, "flashcards", "index.json"), "w", encoding="utf-8") as fh:
        json.dump({"decks": index}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    total = sum(d["cards"] for d in index)
    print(f"Built {len(index)} decks, {total} cards; {apkg} Anki packages"
          + ("" if apkg == len(index) else " (install genanki for the rest)") + ".")


if __name__ == "__main__":
    main()
