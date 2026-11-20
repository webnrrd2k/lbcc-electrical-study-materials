#!/usr/bin/env python3
"""Build the PRELIMINARY Lab 3 (Forward/Reverse) wiring diagrams and wire-label sheets.

Everything is generated from the SEGMENTS list below (one entry per physical
conductor). Edit a segment, re-run `python3 build_diagrams.py`, and every
output (diagram, wire list, labels) updates together.

Outputs (same folder as this script):
  wiring-diagrams.html          Figure 1 physical layout, Figure 2 ladder, wire list, notes
  wire-labels.html              printable sheet of wire-number labels (one per wire end)
  wire-labels.csv               same labels as CSV, for label-maker software
"""
import csv
import html
import os

OUT = os.path.dirname(os.path.abspath(__file__))

FILL = {'red': '#d0262b', 'white': '#fbfbfb', 'black': '#151515', 'green': '#1d8a3c'}
EDGE = {'red': '#d0262b', 'white': '#7a7a7a', 'black': '#151515', 'green': '#1d8a3c'}
CROSS_FILL = '#ffe680'   # tag fill for wires that cross the door (the "9 wires")

# ---------------------------------------------------------------------------
# Terminals for Figure 1.  id -> x, y, exit ('top' | 'bot' | 'door'), short label,
# long name used in the wire list, optional 'via' (x of a side channel the wire
# steps into before running to the duct).
# ---------------------------------------------------------------------------
T = {}


def term(tid, x, y, exit_, label, name, via=None, lpos=None, tagd=26):
    T[tid] = dict(x=x, y=y, exit=exit_, label=label, name=name, via=via, tagd=tagd,
                  lpos=lpos or ('above' if exit_ in ('door', 'bot') else 'below'))


DOOR_Y = 215
# Door devices, seen from the INSIDE of the door (mirror image of the front).
DOOR = [
    # id,     x,    title,     sub,                    kind,   terminals
    ('ACIN',  100, 'AC IN',   'cord grip',             'gland', []),
    ('REVON', 230, 'REVON',   'red pilot, 24 V',       'pilot', ['X1', 'X2']),
    ('FWDON', 350, 'FWDON',   'red pilot, 24 V',       'pilot', ['X1', 'X2']),
    ('RLS',   490, 'RLS',     'limit sw · NC 21–22',   'limit', ['21', '22']),
    ('FLS',   620, 'FLS',     'limit sw · NC 21–22',   'limit', ['21', '22']),
    ('SEL',   760, 'selector', 'not used',             'sel',   []),
    ('REV',   900, 'REV',     'green · NO 3–4',        'pbg',   ['3', '4']),
    ('STOP2', 1040, 'STOP2',  'red · NC 1–2',          'pbr',   ['1', '2']),
    ('FWD',   1180, 'FWD',    'green · NO 3–4',        'pbg',   ['3', '4']),
    ('STOP1', 1320, 'STOP1',  'red · NC 1–2',          'pbr',   ['1', '2']),
]
for did, x, title, sub, kind, terms in DOOR:
    for i, t in enumerate(terms):
        term(f'{did}.{t}', x - 15 + 30 * i, DOOR_Y, 'door', t, f'{title} {t} (door)')
for i, c in enumerate(['H', 'N', 'G']):
    term(f'ACIN.{c}', 85 + 15 * i, 200, 'door', '', 'cord')

# Backplate
TOP, BOT = 600, 900
for i, t in enumerate(['H1', 'H3', 'H2', 'H4']):
    term(f'T1.{t}', 80 + 40 * i, TOP, 'top', t, f'Transformer {t}')
for i, t in enumerate(['X4', 'X2', 'X3', 'X1']):
    term(f'T1.{t}', 80 + 40 * i, BOT, 'bot', t, f'Transformer {t}')
term('CB1.1', 300, TOP, 'top', '1', 'CB1-1 (top)')
term('CB1.2', 300, 880, 'bot', '2', 'CB1-2 (bottom)')
term('CB2.1', 740, TOP, 'top', '1', 'CB2-1 (top)')
term('CB2.2', 740, 880, 'bot', '2', 'CB2-2 (bottom)')
TBX = {'TBG1': 370, 'TBG2': 392, 'TBG3': 414, 'TB1': 450, 'TB2': 472, 'TB3': 494,
       'TB4': 540, 'TB5': 562, 'TB6': 584, 'TB7': 630, 'TB8': 652, 'TB9': 674,
       'TB-T1': 1400, 'TB-T2': 1422, 'TB-T3': 1444}
for k, (tb, x) in enumerate(TBX.items()):
    term(f'{tb}.top', x, 650, 'top', '', f'{tb} (top)', tagd=26 + 18 * (k % 3))
    term(f'{tb}.bot', x, 840, 'bot', '', f'{tb} (bottom)', tagd=26 + 18 * (k % 3))
for i, (t, ln) in enumerate([('24', 'L1'), ('21', 'L2'), ('14', 'L3')]):
    term(f'SOCK.{t}', 815 + 30 * i, TOP, 'top', t, f'3PHIN socket {t} ({ln})')

CONT = {'FW': 930, 'RV': 1160}       # left edge of each contactor + overload stack
OLN = {'FW': 'OLF', 'RV': 'OLR'}
for c, x0 in CONT.items():
    for k, (t, dx) in enumerate([('1L1', 15), ('3L2', 42), ('5L3', 69), ('7L4', 96), ('A1', 123)]):
        term(f'{c}.{t}', x0 + dx, 680, 'top', t, f'{c} {t}', tagd=26 + 22 * (k % 2))
    for k, (t, dx) in enumerate([('23', 148), ('24', 168), ('31', 188), ('32', 208)]):
        term(f'{c}.{t}', x0 + dx, 595, 'top', t, f'{c} aux {t}', tagd=22 + 20 * (k % 2))
    # Overload face, laid out like the WEG RW17-1D on the panel: 14/22 and A2 in the top corners,
    # the control row 96-98-97-95 across the middle (95 on the right, under A2), and the
    # load terminals 2T1/4T2/6T3 along the bottom edge.
    term(f'{c}.1422', x0 + 15, 820, 'bot', '14/22', f'{OLN[c]} 14/22 (= {c} 8T4)', via=x0 - 12, lpos='below', tagd=62)
    term(f'{c}.A2', x0 + 205, 820, 'bot', 'A2', f'{OLN[c]} A2 (= {c} coil A2)', lpos='left')
    for t, dx in [('96', 15), ('98', 78), ('97', 141), ('95', 205)]:
        term(f'{c}.{t}', x0 + dx, 900, 'bot', t, f'{OLN[c]} {t}', lpos='left' if t == '95' else None)
    for k, (t, dx) in enumerate([('2T1', 45), ('4T2', 110), ('6T3', 175)]):
        term(f'{c}.{t}', x0 + dx, 940, 'bot', t, f'{OLN[c]} {t}', tagd=26 + 20 * (k % 2))

# ---------------------------------------------------------------------------
# Physical conductors, in a sensible wiring order.
# route: cord | chan | top | bot | door | cross | local
# ---------------------------------------------------------------------------
S = []


def seg(num, color, a, b, route, note='', chan=None, pts=None, group=''):
    S.append(dict(num=num, color=color, a=a, b=b, route=route, note=note, chan=chan,
                  pts=pts, group=group))


G = '120 V supply'
seg('H', 'black', 'ACIN.H', 'CB1.1', 'cord', 'Cord hot (smooth conductor if a flat cord)', group=G)
seg('N', 'white', 'ACIN.N', 'TB1.top', 'cord', 'Cord neutral (may be ribbed black on a flat cord)', group=G)
seg('G', 'green', 'ACIN.G', 'TBG1.top', 'cord', 'Cord ground', group=G)
seg('H1', 'black', 'CB1.2', 'T1.H1', 'chan', '', chan=244, group=G)
seg('N2', 'white', 'TB1.bot', 'T1.H4', 'chan', 'Ladder calls this N2 at TB1 and N1 at the transformer. See note 4', chan=251, group=G)
G = '24 V secondary'
seg('G', 'green', 'TBG1.bot', 'T1.X4', 'bot', 'Bonds X4 to ground, landed ON the transformer X4 screw', group=G)
seg('X4', 'white', 'T1.X4', 'TB4.bot', 'bot', 'Starts the X4N bus (TB4–TB6 comb jumper)', group=G)
seg('X1', 'red', 'T1.X1', 'CB2.1', 'chan', '', chan=258, group=G)
seg('24', 'red', 'CB2.2', 'TB7.bot', 'bot', 'Starts the 24 V bus (TB7–TB9 comb jumper)', group=G)
G = 'Rungs 5–6: FORWARD'
seg('1', 'red', 'STOP1.1', 'TB7.top', 'cross', '', group=G)
seg('2', 'red', 'STOP1.2', 'STOP2.1', 'door', 'Door jumper', group=G)
seg('3', 'red', 'STOP2.2', 'FWD.3', 'door', 'Door jumper', group=G)
seg('3', 'red', 'FWD.3', 'REV.3', 'door', 'Door jumper', group=G)
seg('3', 'red', 'REV.3', 'FW.7L4', 'cross', 'FW holding contact, line side (13 on some contactors)', group=G)
seg('3', 'red', 'FW.7L4', 'RV.7L4', 'top', 'Panel jumper to RV holding contact', group=G)
seg('4', 'red', 'FWD.4', 'FLS.21', 'door', 'Door jumper', group=G)
seg('4', 'red', 'FLS.21', 'FW.1422', 'cross', 'FW holding contact, load side (14 on some contactors)', group=G)
seg('5', 'red', 'FLS.22', 'RV.31', 'cross', 'Into the RV interlock (NC)', group=G)
seg('6', 'red', 'RV.32', 'FW.A1', 'top', '', group=G)
seg('7', 'red', 'FW.A2', 'FW.95', 'local', 'Short loop on OLF face. Field wire, NOT internal: see note 10. Color: see note 3', group=G)
seg('8', 'white', 'FW.96', 'TB5.bot', 'bot', '', group=G)
G = 'Rungs 7–8: REVERSE'
seg('9', 'red', 'REV.4', 'RLS.21', 'door', 'Door jumper', group=G)
seg('9', 'red', 'RLS.21', 'RV.1422', 'cross', 'RV holding contact, load side', group=G)
seg('10', 'red', 'RLS.22', 'FW.31', 'cross', 'Into the FW interlock (NC)', group=G)
seg('11', 'red', 'FW.32', 'RV.A1', 'top', '', group=G)
seg('12', 'red', 'RV.A2', 'RV.95', 'local', 'Short loop on OLR face. Field wire, NOT internal: see note 10. Color: see note 3', group=G)
seg('8', 'white', 'RV.96', 'FW.96', 'bot', 'OLR 96 joins OLF 96', group=G)
G = 'Rungs 9–10: pilot lights'
seg('13', 'red', 'TB8.top', 'FW.23', 'top', '', group=G)
seg('14', 'red', 'FW.24', 'FWDON.X1', 'cross', '', group=G)
seg('16', 'red', 'TB9.top', 'RV.23', 'top', '', group=G)
seg('17', 'red', 'RV.24', 'REVON.X1', 'cross', '', group=G)
seg('15', 'white', 'REVON.X2', 'FWDON.X2', 'door', 'Door jumper', group=G)
seg('15', 'white', 'FWDON.X2', 'TB6.bot', 'cross', '', group=G)
G = 'Power circuit (simulated 3-phase)'
for ln, st, fw, rv in [('L1', '24', '1L1', '5L3'), ('L2', '21', '3L2', '3L2'), ('L3', '14', '5L3', '1L1')]:
    seg(ln, 'black', f'SOCK.{st}', f'FW.{fw}', 'top', '', group=G)
    seg(ln, 'black', f'FW.{fw}', f'RV.{rv}', 'top', 'RV swaps L1 and L3' if ln != 'L2' else '', group=G)
for tn, o, tb in [('T1', '2T1', 'TB-T1'), ('T2', '4T2', 'TB-T2'), ('T3', '6T3', 'TB-T3')]:
    # TB-T terminals take only one wire, so OLF jumpers to OLR and OLR feeds TB-T (see note 7)
    seg(tn, 'black', f'FW.{o}', f'RV.{o}', 'bot', 'Jumper OLF to OLR', group=G)
    seg(tn, 'black', f'RV.{o}', f'{tb}.bot', 'bot', 'One wire per TB-T terminal', group=G)

CROSS_NUMS = sorted({s['num'] for s in S if s['route'] == 'cross'}, key=lambda n: int(n))
assert len([s for s in S if s['route'] == 'cross']) == 9, 'door channel must carry exactly 9 wires'
USED = {s['a'] for s in S} | {s['b'] for s in S}

# ---------------------------------------------------------------------------
# Figure 1 routing
# ---------------------------------------------------------------------------
DUCT = {'door': (258, 378), 'top': (433, 552), 'bot': (978, 1090)}
LEFT_LANES = {'H': 38, 'N': 46, 'G': 54}
RIGHT_X0 = 1482


def side_x(t):
    return t['via'] if t['via'] is not None else t['x']


def plan_intervals():
    iv = []        # (duct, seg index, lo, hi)
    right = []     # crossing segments, ordered for the right duct
    for i, s in enumerate(S):
        a, b = T[s['a']], T[s['b']]
        r = s['route']
        if r == 'cord':
            xl = LEFT_LANES[s['num']]
            iv.append(('door', i, xl, a['x']))
            iv.append(('top', i, xl, b['x']))
        elif r == 'chan':
            iv.append(('bot', i, *sorted((s['chan'], a['x']))))
            iv.append(('top', i, *sorted((s['chan'], b['x']))))
        elif r in ('top', 'bot', 'door'):
            iv.append((r, i, *sorted((side_x(a), side_x(b)))))
        elif r == 'cross':
            right.append(i)
    # wires that continue to the bottom duct get the outer (right-most) lanes
    right.sort(key=lambda i: (T[door_panel(S[i])[1]]['exit'] == 'bot', -T[door_panel(S[i])[0]]['x']))
    rx = {i: RIGHT_X0 + 9 * k for k, i in enumerate(right)}
    for i in right:
        d, p = door_panel(S[i])
        iv.append(('door', i, T[d]['x'], rx[i]))
        iv.append((T[p]['exit'], i, side_x(T[p]), rx[i]))
    return iv, rx


def door_panel(s):
    return (s['a'], s['b']) if T[s['a']]['exit'] == 'door' else (s['b'], s['a'])


def allocate(iv):
    lane_of, n_lanes = {}, {}
    for duct in DUCT:
        items = sorted([v for v in iv if v[0] == duct], key=lambda v: -(v[3] - v[2]))
        lanes = []
        for _, i, lo, hi in items:
            for k, occ in enumerate(lanes):
                if all(hi + 14 < a or lo - 14 > b for a, b in occ):
                    occ.append((lo, hi))
                    lane_of[(duct, i)] = k
                    break
            else:
                lanes.append([(lo, hi)])
                lane_of[(duct, i)] = len(lanes) - 1
        n_lanes[duct] = len(lanes)
    ys = {}
    for (duct, i), k in lane_of.items():
        y0, y1 = DUCT[duct]
        n = n_lanes[duct]
        step = min(10, (y1 - y0) / max(n - 1, 1))
        ys[(duct, i)] = y0 + k * step
    return ys


def term_offsets():
    count, seen, off = {}, {}, {}
    for s in S:
        for e in (s['a'], s['b']):
            count[e] = count.get(e, 0) + 1
    for i, s in enumerate(S):
        for e in (s['a'], s['b']):
            k = seen.get(e, 0)
            seen[e] = k + 1
            off[(i, e)] = (k - (count[e] - 1) / 2) * 5
    return off


def build_paths():
    iv, rx = plan_intervals()
    ys = allocate(iv)
    off = term_offsets()
    paths = []
    for i, s in enumerate(S):
        r = s['route']
        a, b = T[s['a']], T[s['b']]

        def stub(tid, t):
            return (t['x'] + off[(i, tid)], t['y'])

        def via_pts(tid, t, lane_y):
            """points from the terminal out to (side_x, lane_y)."""
            p0 = stub(tid, t)
            if t['via'] is not None:
                return [p0, (t['via'], p0[1]), (t['via'], lane_y)]
            return [p0, (p0[0], lane_y)]

        if r == 'cord':
            xl = LEFT_LANES[s['num']]
            yd, yt = ys[('door', i)], ys[('top', i)]
            pts = [(a['x'], a['y']), (a['x'], yd), (xl, yd), (xl, yt), (b['x'] + off[(i, s['b'])], yt),
                   stub(s['b'], b)]
        elif r == 'chan':
            yb, yt = ys[('bot', i)], ys[('top', i)]
            pts = [stub(s['a'], a), (stub(s['a'], a)[0], yb), (s['chan'], yb), (s['chan'], yt),
                   (stub(s['b'], b)[0], yt), stub(s['b'], b)]
        elif r in ('top', 'bot', 'door'):
            y = ys[(r, i)]
            pa = via_pts(s['a'], a, y)
            pb = via_pts(s['b'], b, y)
            pts = pa + pb[::-1]
        elif r == 'cross':
            d, p = door_panel(s)
            td, tp = T[d], T[p]
            yd, yp = ys[('door', i)], ys[(tp['exit'], i)]
            pd = via_pts(d, td, yd)
            pp = via_pts(p, tp, yp)
            pts = pd + [(rx[i], yd), (rx[i], yp)] + pp[::-1]
            if s['a'] != d:
                pts = pts[::-1]
        elif r == 'local':
            p0, p1 = stub(s['a'], a), stub(s['b'], b)
            pts = [p0, (p0[0], 850), (p1[0], 850), p1]
        paths.append(pts)
    return paths


def along(pts, dist):
    """point `dist` px along a polyline."""
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        L = abs(x1 - x0) + abs(y1 - y0)
        if L >= dist and L > 0:
            f = dist / L
            return x0 + (x1 - x0) * f, y0 + (y1 - y0) * f
        dist -= L
    return pts[-1]


def tag(x, y, text, color, cross=False):
    w = 10 + 6.6 * len(text)
    fill = CROSS_FILL if cross else '#fff'
    return (f'<rect x="{x - w / 2:.1f}" y="{y - 8:.1f}" width="{w:.1f}" height="16" rx="8" fill="{fill}" '
            f'stroke="{EDGE[color]}" stroke-width="1.6"/>'
            f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="middle" class="wt">{html.escape(text)}</text>')


def polyline(pts, color, width=3):
    d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    if color == 'white':
        return (f'<path d="{d}" fill="none" stroke="#7a7a7a" stroke-width="{width + 1.4}" stroke-linejoin="round"/>'
                f'<path d="{d}" fill="none" stroke="#fbfbfb" stroke-width="{width - 0.6}" stroke-linejoin="round"/>')
    return f'<path d="{d}" fill="none" stroke="{FILL[color]}" stroke-width="{width}" stroke-linejoin="round"/>'


def circle(x, y, used=True, r=5):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{"#c9c9c9" if used else "#eee"}" '
            f'stroke="#555" stroke-width="1.2"/>')


def text(x, y, s, cls, anchor='middle', extra='', halo=False):
    if halo:
        cls += ' halo'
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}"{extra}>{html.escape(s)}</text>'


def figure1():
    o = ['<svg viewBox="0 0 1600 1130" role="img" aria-label="Preliminary physical wiring diagram: door devices '
         'seen from inside on top, backplate below, every conductor drawn in its color with its wire number.">']
    # door
    o.append('<rect x="20" y="30" width="1455" height="365" rx="10" fill="#e6e8ea" stroke="#999" stroke-width="1.5"/>')
    o.append(text(35, 55, 'DOOR (front panel), seen from the INSIDE. Left/right is mirrored vs. the front.', 'h', 'start'))
    o.append(f'<rect x="30" y="250" width="1440" height="136" fill="#d3d6d9" stroke="#b5b8bb"/>')
    o.append(text(1460, 380, 'door wire duct', 'dl', 'end'))
    for did, x, title, sub, kind, terms in DOOR:
        if kind in ('pbg', 'pbr'):
            col = '#1d8a3c' if kind == 'pbg' else '#d97a6a'
            o.append(f'<rect x="{x - 30}" y="95" width="60" height="50" rx="4" fill="#2b2b2b"/>'
                     f'<rect x="{x - 18}" y="110" width="36" height="78" rx="3" fill="{col}"/>')
        elif kind == 'pilot':
            o.append(f'<circle cx="{x}" cy="140" r="34" fill="#2b2b2b"/><circle cx="{x}" cy="140" r="20" fill="#e33" opacity=".85"/>')
        elif kind == 'limit':
            o.append(f'<rect x="{x - 24}" y="100" width="48" height="88" rx="4" fill="#c4c8cc" stroke="#777"/>'
                     f'<circle cx="{x}" cy="112" r="9" fill="#888"/>')
        elif kind == 'sel':
            o.append(f'<circle cx="{x}" cy="130" r="32" fill="#2b2b2b"/><rect x="{x - 6}" y="104" width="12" height="52" rx="3" fill="#ddd"/>')
        elif kind == 'gland':
            o.append(f'<circle cx="{x}" cy="140" r="30" fill="#777"/><circle cx="{x}" cy="140" r="12" fill="#222"/>')
        o.append(text(x, 74, title, 'dn'))
        o.append(text(x, 88, sub, 'ds'))
    # backplate
    o.append('<rect x="20" y="405" width="1565" height="712" rx="10" fill="#eef0f1" stroke="#999" stroke-width="1.5"/>')
    o.append('<rect x="60" y="425" width="1405" height="135" fill="#d3d6d9" stroke="#b5b8bb"/>')
    o.append(text(68, 420, 'BACKPLATE', 'h', 'start'))
    o.append(text(1455, 556, 'top wire duct', 'dl', 'end'))
    o.append('<rect x="60" y="970" width="1405" height="128" fill="#d3d6d9" stroke="#b5b8bb"/>')
    o.append(text(1455, 1112, 'bottom wire duct', 'dl', 'end'))
    o.append('<rect x="30" y="250" width="30" height="310" fill="#cfd2d5" stroke="#b5b8bb"/>')
    o.append(text(45, 330, 'LEFT tray: cord only', 'dl', 'middle', ' transform="rotate(-90 45 330)"'))
    o.append('<rect x="1470" y="250" width="100" height="848" fill="#f3e6b5" stroke="#b9a35a"/>')
    o.append(text(1555, 700, 'RIGHT tray = DOOR CHANNEL: exactly 9 wires', 'dn', 'middle', ' transform="rotate(90 1555 700)"'))
    # transformer
    o.append('<rect x="66" y="585" width="166" height="330" rx="6" fill="#2b2b2b"/>'
             '<rect x="74" y="680" width="150" height="130" rx="3" fill="#f2f2f2"/>')
    for i, s in enumerate(['T1 control transformer', '120 V primary (top)', '24 V secondary (bottom)',
                           'links: H1–H3, H2–H4, X2–X3', '(same as Lab 2)']):
        o.append(text(149, 702 + 18 * i, s, 'dn' if i == 0 else 'ds'))
    o.append('<rect x="80" y="606" width="40" height="5" fill="#c9a43a"/><rect x="160" y="606" width="40" height="5" fill="#c9a43a"/>'
             '<rect x="120" y="889" width="40" height="5" fill="#c9a43a"/>')
    # breakers
    for cb, x, sub in [('CB1', 300, '120 V primary'), ('CB2', 740, '24 V secondary')]:
        o.append(f'<rect x="{x - 30}" y="585" width="60" height="310" rx="5" fill="#f7f7f7" stroke="#888"/>'
                 f'<rect x="{x - 18}" y="690" width="36" height="60" rx="3" fill="#222"/>')
        o.append(text(x, 780, cb, 'dn'))
        o.append(text(x, 796, sub, 'ds'))
        o.append(text(x, 812, '1 wire/terminal', 'ds'))
    # terminal blocks
    groups = [('GND', ['TBG1', 'TBG2', 'TBG3'], '#b9e06a', ''),
              ('120V-N', ['TB1', 'TB2', 'TB3'], '#a9adb1', ''),
              ('24V-N', ['TB4', 'TB5', 'TB6'], '#a9adb1', 'X4N bus'),
              ('24V-H', ['TB7', 'TB8', 'TB9'], '#a9adb1', '24 V bus'),
              ('3PH POWER', ['TB-T1', 'TB-T2', 'TB-T3'], '#a9adb1', '')]
    for gname, tbs, col, bus in groups:
        for tb in tbs:
            x = TBX[tb]
            o.append(f'<rect x="{x - 10}" y="632" width="20" height="226" fill="{col}" stroke="#777"/>')
            o.append(text(x, 805, tb, 'tls', 'middle', f' transform="rotate(-90 {x} 805)" dy="4"'))
        xm = sum(TBX[t] for t in tbs) / 3
        o.append(text(xm, 740, gname, 'dn', halo=True))
        if bus:
            o.append(f'<rect x="{TBX[tbs[0]] - 6}" y="690" width="56" height="9" rx="3" fill="#e07800"/>')
            o.append(text(xm, 754, bus, 'ds', halo=True))
    # 3PHIN socket
    o.append('<rect x="790" y="585" width="110" height="275" rx="5" fill="#8a8a8a" stroke="#555"/>'
             '<circle cx="845" cy="720" r="34" fill="#ccc" stroke="#555"/>')
    o.append(text(845, 790, '3PHIN', 'tlw'))
    o.append(text(845, 806, 'CR socket', 'tlw'))
    o.append(text(845, 822, 'simulates 3φ in', 'tlw'))
    # contactors + overloads
    for c, x0 in CONT.items():
        o.append(f'<rect x="{x0 + 135}" y="578" width="85" height="80" rx="4" fill="#dde3ea" stroke="#666"/>')
        o.append(text(x0 + 177, 640, 'aux block', 'ds'))
        o.append(f'<rect x="{x0}" y="665" width="220" height="130" rx="5" fill="#c9cfd8" stroke="#666"/>')
        o.append(text(x0 + 110, 740, f'{c} contactor', 'dn'))
        o.append(text(x0 + 110, 756, '"FR" on the layout' if c == 'FW' else 'reversing', 'ds'))
        o.append(f'<rect x="{x0}" y="805" width="220" height="150" rx="5" fill="#c9cfd8" stroke="#666"/>')
        o.append(text(x0 + 100, 850, f'{OLN[c]} overload', 'dn'))
        o.append(text(x0 + 100, 866, 'wire A2 → 95 yourself', 'ds'))
    # wires
    paths = build_paths()
    for s, pts in zip(S, paths):
        o.append(polyline(pts, s['color']))
    # terminals (drawn on top of wire ends)
    for tid, t in T.items():
        if tid.startswith('ACIN'):
            continue
        used = tid in USED
        o.append(circle(t['x'], t['y'], used))
        if t['label']:
            if tid.startswith('T1.'):
                o.append(text(t['x'], t['y'] + (19 if t['exit'] == 'top' else -11), t['label'], 'tlw'))
            elif t['exit'] == 'door':
                o.append(text(t['x'], t['y'] - 9, t['label'], 'tl'))
            elif t['lpos'] == 'left':
                o.append(text(t['x'] - 9, t['y'] + 4, t['label'], 'tl', 'end'))
            elif t['lpos'] == 'below':
                o.append(text(t['x'], t['y'] + 17, t['label'], 'tl'))
            else:
                o.append(text(t['x'], t['y'] - 9, t['label'], 'tl'))
    # tags at both ends
    drawn = set()
    for s, pts in zip(S, paths):
        cross = s['num'] in CROSS_NUMS
        ends = [(s['b'], pts[::-1])] if s['route'] == 'cord' else [(s['a'], pts), (s['b'], pts[::-1])]
        for tid, p in ends:
            if (tid, s['num']) in drawn:
                continue
            drawn.add((tid, s['num']))
            x, y = along(p, T[tid]['tagd'] if s['route'] != 'local' else 14)
            o.append(tag(x, y, s['num'], s['color'], cross))
    o.append('</svg>')
    return '\n'.join(o)


# ---------------------------------------------------------------------------
# Figure 2: ladder diagram, relabeled
# ---------------------------------------------------------------------------
def wl(pts, color, num=None, at=None, cross=False):
    o = [polyline(pts, color, 2.6)]
    if num:
        if at is None:
            (x0, y0), (x1, y1) = pts[0], pts[1]
            at = ((x0 + x1) / 2, (y0 + y1) / 2)
        o.append(tag(at[0], at[1], num, color, cross))
    return ''.join(o)


def bg(x, y, w, h):
    return f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" fill="#fff"/>'


def sym_no(x, y, nc=False):
    s = bg(x, y, 30, 28) + (f'<line x1="{x - 6}" y1="{y - 12}" x2="{x - 6}" y2="{y + 12}" stroke="#222" stroke-width="2.2"/>'
                            f'<line x1="{x + 6}" y1="{y - 12}" x2="{x + 6}" y2="{y + 12}" stroke="#222" stroke-width="2.2"/>'
                            f'<line x1="{x - 20}" y1="{y}" x2="{x - 6}" y2="{y}" stroke="#222" stroke-width="2"/>'
                            f'<line x1="{x + 6}" y1="{y}" x2="{x + 20}" y2="{y}" stroke="#222" stroke-width="2"/>')
    if nc:
        s += f'<line x1="{x - 12}" y1="{y + 12}" x2="{x + 12}" y2="{y - 12}" stroke="#222" stroke-width="2"/>'
    return s


def sym_pb(x, y, nc):
    yb = y + 8 if nc else y - 8
    return (bg(x, y, 44, 40) +
            f'<circle cx="{x - 14}" cy="{y}" r="3" fill="#fff" stroke="#222" stroke-width="1.5"/>'
            f'<circle cx="{x + 14}" cy="{y}" r="3" fill="#fff" stroke="#222" stroke-width="1.5"/>'
            f'<line x1="{x - 20}" y1="{y}" x2="{x - 17}" y2="{y}" stroke="#222" stroke-width="2"/>'
            f'<line x1="{x + 17}" y1="{y}" x2="{x + 20}" y2="{y}" stroke="#222" stroke-width="2"/>'
            f'<line x1="{x - 16}" y1="{yb}" x2="{x + 16}" y2="{yb}" stroke="#222" stroke-width="2"/>'
            f'<line x1="{x}" y1="{yb}" x2="{x}" y2="{y - 18}" stroke="#222" stroke-width="2"/>')


def sym_ls(x, y):
    return (bg(x, y, 44, 34) +
            f'<circle cx="{x - 14}" cy="{y}" r="3" fill="#fff" stroke="#222" stroke-width="1.5"/>'
            f'<circle cx="{x + 14}" cy="{y}" r="3" fill="#fff" stroke="#222" stroke-width="1.5"/>'
            f'<line x1="{x - 20}" y1="{y}" x2="{x - 17}" y2="{y}" stroke="#222" stroke-width="2"/>'
            f'<line x1="{x + 17}" y1="{y}" x2="{x + 20}" y2="{y}" stroke="#222" stroke-width="2"/>'
            f'<path d="M{x - 12},{y + 3} L{x + 15},{y + 6} L{x + 9},{y + 12}" fill="none" stroke="#222" stroke-width="2"/>')


def sym_coil(x, y, lamp=False):
    s = bg(x, y, 40, 34) + (f'<circle cx="{x}" cy="{y}" r="14" fill="#fff" stroke="#222" stroke-width="2"/>'
                            f'<line x1="{x - 20}" y1="{y}" x2="{x - 14}" y2="{y}" stroke="#222" stroke-width="2"/>'
                            f'<line x1="{x + 14}" y1="{y}" x2="{x + 20}" y2="{y}" stroke="#222" stroke-width="2"/>')
    if lamp:
        s += (f'<line x1="{x - 10}" y1="{y - 10}" x2="{x + 10}" y2="{y + 10}" stroke="#222" stroke-width="1.3"/>'
              f'<line x1="{x - 10}" y1="{y + 10}" x2="{x + 10}" y2="{y - 10}" stroke="#222" stroke-width="1.3"/>'
              f'<text x="{x}" y="{y + 4}" text-anchor="middle" class="wt" style="font-size:11px">R</text>')
    return s


def sym_tb(x, y):
    return (f'<circle cx="{x}" cy="{y}" r="7" fill="#fff" stroke="#222" stroke-width="1.6"/>'
            f'<line x1="{x - 4}" y1="{y + 4}" x2="{x + 4}" y2="{y - 4}" stroke="#222" stroke-width="1.3"/>')


def labels(x, y, name, sub, tl='', tr='', dy=26):
    o = text(x, y - dy, name, 'dn')
    if sub:
        o += text(x, y + dy + 6, sub, 'ds')
    if tl:
        o += text(x - 20, y - 8, tl, 'tl', 'end')
    if tr:
        o += text(x + 20, y - 8, tr, 'tl', 'start')
    return o


def figure2():
    X = lambda n: n in CROSS_NUMS  # noqa: E731
    o = ['<svg viewBox="0 0 1600 1150" role="img" aria-label="The lab ladder diagram redrawn with device '
         'locations, wire colors and wire numbers.">']
    LR, RR = 120, 1040
    # --- supply ---
    o.append(text(LR, 44, 'Cord HOT', 'ds'))
    o.append(text(600, 44, 'Cord NEUTRAL', 'ds'))
    o.append(text(760, 44, 'Cord GROUND', 'ds'))
    o.append(wl([(LR, 50), (LR, 98)], 'black', 'H', (LR, 72)))
    o.append(f'<path d="M{LR},98 q14,12 0,24" fill="none" stroke="#222" stroke-width="2.2"/>')
    o.append(text(LR + 18, 110, 'CB1', 'dn', 'start') + text(LR + 18, 124, 'panel, 1st breaker', 'ds', 'start'))
    o.append(wl([(LR, 122), (LR, 200), (250, 200), (250, 238)], 'black', 'H1', (185, 200)))
    o.append(wl([(600, 50), (600, 113)], 'white', 'N', (600, 80)))
    o.append(sym_tb(600, 120) + text(612, 116, 'TB1', 'dn', 'start'))
    o.append(wl([(600, 127), (600, 200), (490, 200), (490, 238)], 'white', 'N2', (545, 200)))
    o.append(wl([(760, 50), (760, 113)], 'green', 'G', (760, 80)))
    o.append(sym_tb(760, 120) + text(772, 116, 'TBG1', 'dn', 'start'))
    o.append(wl([(760, 127), (760, 330), (490, 330)], 'green', 'G', (760, 230)))
    o.append(f'<g stroke="#222" stroke-width="2"><line x1="760" y1="160" x2="800" y2="160"/>'
             f'<line x1="788" y1="160" x2="788" y2="170"/><line x1="778" y1="170" x2="798" y2="170"/>'
             f'<line x1="782" y1="175" x2="794" y2="175"/><line x1="786" y1="180" x2="790" y2="180"/></g>')
    o.append(text(806, 156, 'bonded to DIN rail / plate', 'ds', 'start'))
    o.append(text(640, 322, 'green lands ON the X4 screw', 'ds', 'middle', halo=True))
    # transformer
    coil = 'M250,250 ' + ' '.join('q10,-14 20,0' for _ in range(12))
    coil2 = 'M250,292 ' + ' '.join('q10,14 20,0' for _ in range(12))
    o.append(f'<path d="{coil}" fill="none" stroke="#222" stroke-width="2"/><path d="{coil2}" fill="none" stroke="#222" stroke-width="2"/>'
             f'<line x1="250" y1="266" x2="490" y2="266" stroke="#222" stroke-width="2"/>'
             f'<line x1="250" y1="276" x2="490" y2="276" stroke="#222" stroke-width="2"/>'
             f'<line x1="250" y1="238" x2="250" y2="250" stroke="#222" stroke-width="2"/>'
             f'<line x1="490" y1="238" x2="490" y2="250" stroke="#222" stroke-width="2"/>')
    o.append(text(370, 230, 'T1 · 120 V → 24 V', 'dn'))
    o.append(text(240, 252, 'H1', 'tl', 'end') + text(500, 252, 'H4', 'tl', 'start'))
    o.append(text(240, 300, 'X1', 'tl', 'end') + text(500, 300, 'X4', 'tl', 'start'))
    o.append(wl([(250, 292), (250, 340), (LR, 340), (LR, 360)], 'red', 'X1', (185, 340)))
    o.append(f'<path d="M{LR},360 q14,12 0,24" fill="none" stroke="#222" stroke-width="2.2"/>')
    o.append(text(LR + 18, 372, 'CB2', 'dn', 'start') + text(LR + 18, 386, 'panel, 2nd breaker', 'ds', 'start'))
    o.append(wl([(490, 292), (490, 330)], 'white'))
    o.append(wl([(490, 330), (490, 390), (RR, 390), (RR, 413)], 'white', 'X4', (765, 390)))
    o.append(sym_tb(RR, 420) + text(RR + 12, 416, 'TB4', 'dn', 'start'))
    # rails
    o.append(wl([(LR, 384), (LR, 980)], 'red', '24', (LR, 420)))
    o.append(text(LR, 1010, '24 V bus', 'ds') + text(LR, 1024, 'TB7–TB9 comb jumper', 'ds'))
    o.append(wl([(RR, 427), (RR, 880)], 'white', 'X4N', (RR, 455)))
    o.append(text(RR, 1010, 'X4N bus', 'ds') + text(RR, 1024, 'TB4–TB6 comb jumper', 'ds'))
    # rung numbers (match the lab sheet)
    R = {5: 500, 6: 580, 7: 680, 8: 760, 9: 880, 10: 960}
    for n, y in R.items():
        o.append(text(60, y + 4, str(n), 'dn'))
    y5, y6, y7, y8, y9, y10 = (R[k] for k in (5, 6, 7, 8, 9, 10))
    xs = dict(TB=170, S1=250, S2=340, n3=400, FB=450, n4=505, LS=560, IL=660, CO=760, OL=860, n8=915, TBr=970)
    # rung 5 wires
    o.append(wl([(LR, y5), (xs['TB'] - 7, y5)], 'red'))
    o.append(wl([(xs['TB'] + 7, y5), (xs['S1'] - 20, y5)], 'red', '1', None, X('1')))
    o.append(wl([(xs['S1'] + 20, y5), (xs['S2'] - 20, y5)], 'red', '2', None, X('2')))
    o.append(wl([(xs['S2'] + 20, y5), (xs['FB'] - 20, y5)], 'red', '3', (370, y5), X('3')))
    o.append(wl([(xs['FB'] + 20, y5), (xs['LS'] - 20, y5)], 'red', '4', (522, y5), X('4')))
    o.append(wl([(xs['LS'] + 20, y5), (xs['IL'] - 20, y5)], 'red', '5', None, X('5')))
    o.append(wl([(xs['IL'] + 20, y5), (xs['CO'] - 20, y5)], 'red', '6', None))
    o.append(wl([(xs['CO'] + 20, y5), (xs['OL'] - 20, y5)], 'red', '7', None))
    o.append(wl([(xs['OL'] + 20, y5), (xs['TBr'] - 7, y5)], 'white', '8', (940, y5)))
    o.append(wl([(xs['TBr'] + 7, y5), (RR, y5)], 'white'))
    # rung 6 (FW seal-in) and the node-3 riser
    o.append(wl([(xs['n3'], y5), (xs['n3'], y8), (xs['FB'] - 20, y8)], 'red'))
    o.append(wl([(xs['n3'], y6), (xs['FB'] - 20, y6)], 'red'))
    o.append(wl([(xs['n3'], y7), (xs['FB'] - 20, y7)], 'red'))
    o.append(tag(xs['n3'], (y5 + y6) / 2, '3', 'red', X('3')))
    o.append(tag(xs['n3'], (y7 + y8) / 2 + 10, '3', 'red', X('3')))
    o.append(wl([(xs['FB'] + 20, y6), (xs['n4'], y6), (xs['n4'], y5)], 'red', '4', (xs['n4'], (y5 + y6) / 2), X('4')))
    # rung 7
    o.append(wl([(xs['FB'] + 20, y7), (xs['LS'] - 20, y7)], 'red', '9', (522, y7), X('9')))
    o.append(wl([(xs['LS'] + 20, y7), (xs['IL'] - 20, y7)], 'red', '10', None, X('10')))
    o.append(wl([(xs['IL'] + 20, y7), (xs['CO'] - 20, y7)], 'red', '11', None))
    o.append(wl([(xs['CO'] + 20, y7), (xs['OL'] - 20, y7)], 'red', '12', None))
    o.append(wl([(xs['OL'] + 20, y7), (xs['n8'], y7), (xs['n8'], y5)], 'white', '8', (xs['n8'], (y5 + y7) / 2)))
    # rung 8 (RV seal-in)
    o.append(wl([(xs['FB'] + 20, y8), (xs['n4'], y8), (xs['n4'], y7)], 'red', '9', (xs['n4'], (y7 + y8) / 2), X('9')))
    # rungs 9, 10
    for y, tb, cont, num_a, num_b, lamp in [(y9, 'TB8', 'FW', '13', '14', 'FWDON'), (y10, 'TB9', 'RV', '16', '17', 'REVON')]:
        o.append(wl([(LR, y), (xs['TB'] - 7, y)], 'red'))
        o.append(wl([(xs['TB'] + 7, y), (xs['FB'] - 20, y)], 'red', num_a, (300, y), X(num_a)))
        o.append(wl([(xs['FB'] + 20, y), (xs['CO'] - 20, y)], 'red', num_b, (605, y), X(num_b)))
    o.append(wl([(xs['CO'] + 20, y9), (xs['TBr'] - 7, y9)], 'white', '15', (840, y9), X('15')))
    o.append(wl([(xs['CO'] + 20, y10), (xs['n8'], y10), (xs['n8'], y9)], 'white', '15', (840, y10), X('15')))
    o.append(wl([(xs['TBr'] + 7, y9), (RR, y9)], 'white'))
    # symbols + labels
    for y, tb in [(y5, 'TB7'), (y9, 'TB8'), (y10, 'TB9')]:
        o.append(sym_tb(xs['TB'], y) + text(xs['TB'], y - 14, tb, 'dn'))
    for y, tb in [(y5, 'TB5'), (y9, 'TB6')]:
        o.append(sym_tb(xs['TBr'], y) + text(xs['TBr'], y - 14, tb, 'dn'))
    o.append(sym_pb(xs['S1'], y5, True) + labels(xs['S1'], y5, 'STOP1', 'door', '1', '2'))
    o.append(sym_pb(xs['S2'], y5, True) + labels(xs['S2'], y5, 'STOP2', 'door', '1', '2'))
    o.append(sym_pb(xs['FB'], y5, False) + labels(xs['FB'], y5, 'FWD', 'door', '3', '4'))
    o.append(sym_pb(xs['FB'], y7, False) + labels(xs['FB'], y7, 'REV', 'door', '3', '4'))
    o.append(sym_ls(xs['LS'], y5) + labels(xs['LS'], y5, 'FLS', 'door', '21', '22'))
    o.append(sym_ls(xs['LS'], y7) + labels(xs['LS'], y7, 'RLS', 'door', '21', '22'))
    o.append(sym_no(xs['FB'], y6) + labels(xs['FB'], y6, 'FW', 'seal-in', '7L4', '14/22', 18))
    o.append(sym_no(xs['FB'], y8) + labels(xs['FB'], y8, 'RV', 'seal-in', '7L4', '14/22', 18))
    o.append(sym_no(xs['IL'], y5, True) + labels(xs['IL'], y5, 'RV', 'aux · interlock', '31', '32'))
    o.append(sym_no(xs['IL'], y7, True) + labels(xs['IL'], y7, 'FW', 'aux · interlock', '31', '32'))
    o.append(sym_coil(xs['CO'], y5) + labels(xs['CO'], y5, 'FW coil', 'panel', 'A1', 'A2'))
    o.append(sym_coil(xs['CO'], y7) + labels(xs['CO'], y7, 'RV coil', 'panel', 'A1', 'A2'))
    o.append(sym_no(xs['OL'], y5, True) + labels(xs['OL'], y5, 'OLF', 'overload', '95', '96'))
    o.append(sym_no(xs['OL'], y7, True) + labels(xs['OL'], y7, 'OLR', 'overload', '95', '96'))
    o.append(sym_no(xs['FB'], y9) + labels(xs['FB'], y9, 'FW', 'aux', '23', '24', 20))
    o.append(sym_no(xs['FB'], y10) + labels(xs['FB'], y10, 'RV', 'aux', '23', '24', 20))
    o.append(sym_coil(xs['CO'], y9, True) + labels(xs['CO'], y9, 'FWDON', 'door', 'X1', 'X2'))
    o.append(sym_coil(xs['CO'], y10, True) + labels(xs['CO'], y10, 'REVON', 'door', 'X1', 'X2'))
    o.append(text(560, 1070, 'Shaded tag = this wire number crosses the door (right tray). '
                  'Door jumpers keep it to one crossing per number.', 'ds'))

    # --- power section ---
    L = {'L1': 1190, 'L2': 1260, 'L3': 1330}
    RVX = {'1L1': 1420, '3L2': 1490, '5L3': 1560}
    o.append(text(1260, 44, 'SW1 + fuses: not on your panel', 'ds'))
    for ln, x in L.items():
        o.append(f'<line x1="{x}" y1="54" x2="{x}" y2="190" stroke="#888" stroke-width="2" stroke-dasharray="7 5"/>')
        o.append(text(x, 70, ln, 'dn'))
    o.append(text(1260, 210, '3PHIN socket simulates the 3-phase supply', 'ds'))
    for (ln, x), st in zip(L.items(), ['24', '21', '14']):
        o.append(sym_tb(x, 240) + text(x + 10, 232, st, 'tl', 'start'))
    o.append(wl([(L['L1'], 247), (L['L1'], 640)], 'black', 'L1', (L['L1'], 290)))
    o.append(wl([(L['L2'], 247), (L['L2'], 640)], 'black', 'L2', (L['L2'], 290)))
    o.append(wl([(L['L3'], 247), (L['L3'], 640)], 'black', 'L3', (L['L3'], 290)))
    o.append(wl([(L['L1'], 360), (RVX['5L3'], 360), (RVX['5L3'], 640)], 'black', 'L1', (1530, 360)))
    o.append(wl([(L['L2'], 390), (RVX['3L2'], 390), (RVX['3L2'], 640)], 'black', 'L2', (1460, 390)))
    o.append(wl([(L['L3'], 420), (RVX['1L1'], 420), (RVX['1L1'], 640)], 'black', 'L3', (1390, 420)))
    for x in (L['L1'], L['L2'], L['L3']):
        o.append(f'<circle cx="{x}" cy="{ {L["L1"]: 360, L["L2"]: 390, L["L3"]: 420}[x] }" r="4" fill="#222"/>')
    o.append(text(1440, 315, 'RV gets L3 / L2 / L1: L1 and L3 swapped', 'ds', halo=True))
    o.append(text(1440, 329, '→ motor runs backwards', 'ds', halo=True))

    def pole(x, y, lab):
        return (bg(x, y, 30, 22) +
                f'<line x1="{x - 12}" y1="{y - 6}" x2="{x + 12}" y2="{y - 6}" stroke="#222" stroke-width="2.2"/>'
                f'<line x1="{x - 12}" y1="{y + 6}" x2="{x + 12}" y2="{y + 6}" stroke="#222" stroke-width="2.2"/>'
                + text(x + 16, y - 10, lab, 'tl', 'start'))

    def heater(x, y):
        return (bg(x, y, 20, 30) + f'<path d="M{x},{y - 14} q8,7 0,14 q-8,7 0,14" fill="none" stroke="#222" stroke-width="2"/>')

    for (ln, x), t in zip(L.items(), ['1L1', '3L2', '5L3']):
        o.append(wl([(x, 640), (x, 900)], 'black'))
        o.append(pole(x, 660, t) + heater(x, 780))
    for t, x in RVX.items():
        o.append(wl([(x, 640), (x, 900)], 'black'))
        o.append(pole(x, 660, t) + heater(x, 780))
    o.append(text(1260, 700, 'FW main poles', 'dn', halo=True) + text(1490, 700, 'RV main poles', 'dn', halo=True))
    o.append(text(1260, 820, 'OLF heaters', 'dn', halo=True) + text(1490, 820, 'OLR heaters', 'dn', halo=True))
    o.append(text(1260, 836, 'OLF 2T1 / 4T2 / 6T3', 'ds', halo=True) + text(1490, 836, 'OLR 2T1 / 4T2 / 6T3', 'ds', halo=True))
    # load side joins
    joins = [('T1', L['L1'], RVX['1L1'], 900), ('T2', L['L2'], RVX['3L2'], 925), ('T3', L['L3'], RVX['5L3'], 950)]
    for tn, xf, xr, yj in joins:
        o.append(wl([(xr, 900), (xr, yj), (xf, yj)], 'black', tn, (xr - 40, yj)))
        o.append(wl([(xf, 900), (xf, 993)], 'black', tn, (xf, 975)))
        o.append(f'<circle cx="{xf}" cy="{yj}" r="4" fill="#222"/>')
        o.append(sym_tb(xf, 1000) + text(xf + 10, 1018, f'TB-{tn}', 'tl', 'start'))
        o.append(f'<line x1="{xf}" y1="1007" x2="{xf}" y2="1060" stroke="#888" stroke-width="2" stroke-dasharray="7 5"/>')
    o.append('<circle cx="1260" cy="1085" r="26" fill="#fff" stroke="#888" stroke-width="2" stroke-dasharray="5 4"/>')
    o.append(text(1260, 1082, 'MOTOR', 'tl') + text(1260, 1096, '½ HP', 'tl'))
    o.append(f'<line x1="{L["L1"]}" y1="1060" x2="1245" y2="1064" stroke="#888" stroke-width="2" stroke-dasharray="7 5"/>'
             f'<line x1="{L["L3"]}" y1="1060" x2="1275" y2="1064" stroke="#888" stroke-width="2" stroke-dasharray="7 5"/>')
    o.append(text(1430, 1090, 'dashed = simulated, not wired', 'ds'))
    o.append('</svg>')
    return '\n'.join(o)


# ---------------------------------------------------------------------------
# Wire list + labels
# ---------------------------------------------------------------------------
ROUTE_TXT = {'cord': 'cord → left tray → top duct', 'chan': 'bottom duct → side channel → top duct',
             'top': 'top duct', 'bot': 'bottom duct', 'door': 'door (jumper)', 'local': 'on the overload face',
             'cross': 'DOOR CHANNEL (right tray)'}


def name(tid):
    return T[tid]['name']


def label_ends():
    ends = []
    for k, s in enumerate(S, 1):
        for e in ([s['b']] if s['route'] == 'cord' else [s['a'], s['b']]):
            ends.append(dict(num=s['num'], at=name(e), seg=k, color=s['color']))
    return ends


def num_key(n):
    return (0, int(n)) if n.isdigit() else (1, n)


NOTES = [
    ('PRELIMINARY: check your own parts before you wire.',
     'This page was drawn from the lab sheet (LAB3-F20b), the component-layout and front-panel drawings, and the '
     'Additional Specifications. It was <b>not</b> drawn from photos of a built panel. The wire numbers and from/to '
     'terminals come from the ladder and should be right. Where each terminal physically sits on your contactors, '
     'aux blocks and the CR socket is a <b>guess</b>. Read the numbers stamped on your parts and go by those. '
     'Once the panel is wired, send photos and this page can be redrawn to match, the same as Lab 2.', False),
    ('Exactly 9 wires through the door channel, and the door jumpers are why.',
     'Wire numbers 1, 3, 4, 5, 9, 10, 14, 15 and 17 each cross the door <b>once</b> (the yellow tags). To keep it at '
     'one crossing per number, make these jumpers on the door itself: 2 (STOP1→STOP2), 3 (STOP2→FWD→REV), '
     '4 (FWD→FLS), 9 (REV→RLS) and 15 (REVON X2→FWDON X2). Run all 9 in the <b>right</b> tray. The left tray is '
     'for the cord only. A control wire in the left tray, or a neutral (15) running by itself, loses selloff points.', False),
    ('Wires 7 and 12 are not neutrals, so what color?',
     'They run from the coil A2 to the overload 95, which is <i>upstream</i> of the OL contact. When an overload '
     'trips, 7 or 12 is at 24 V. The spec only says "24VAC Neutral: White", so they are drawn red here. In Lab 2 '
     'the same wire (wire 4) was white. Ask which color the instructor wants before you cut them. '
     'Wires 8 and 15 land straight on the X4N bus, so white is right for those.', False),
    ('The lab sheet names the neutral jumper two ways.',
     'The wire from TB1 (bottom) to the transformer is marked <b>N2</b> at TB1 and <b>N1</b> at the transformer. '
     'It is one conductor, so it gets one number. These labels use N2, as printed at the terminal block. '
     'Change it in the script if your instructor uses N1.', True),
    ('Two kinds of contactor, same terminals.',
     'The note on the lab sheet says some contactors use 13/14 for the holding contact and others use 7L4/14-22. '
     '13 = 7L4 and 14 = 14/22. On the 7L4 type with the overload attached, the load side of that contact '
     '(8T4) is reached through the overload\'s <b>14/22</b> pass-through. The coil\'s A2 is reached through the '
     'overload\'s <b>A2</b> pass-through. Both work the same as in Lab 2. The interlocks (31-32, NC) and the '
     'pilot contacts (23-24, NO) are on the front aux block. Check that your aux block really has '
     '23-24 NO and 31-32 NC.', True),
    ('Transformer grounding: green goes to the X4 screw.',
     'Per <i>Proper Grounding of the Motor Control Transformer</i>, the green bond lands directly on the '
     'transformer\'s X4 terminal, next to the white X4. Landing it at TB4 instead would be a code violation, even though '
     'Constructor draws it that way. Procedure photo 4 has to show it clearly.', True),
    ('The power circuit: RV swaps L1 and L3.',
     'FW gets L1/L2/L3 on 1L1/3L2/5L3. RV gets L3/L2/L1. The diagram makes the line-side jumpers contactor to contactor '
     '(FW 1L1→RV 5L3, FW 3L2→RV 3L2, FW 5L3→RV 1L1), so each socket terminal has only one wire. On the '
     'load side, the TB-T terminals are too small for two wires, so each OLF output (2T1/4T2/6T3) jumpers '
     'to the same OLR terminal, and one wire runs from OLR to the bottom of TB-T1..T3. That puts two wires '
     'under each OLR load-side screw, which the overload\'s box clamp is made for. '
     'Nothing goes on the top of TB-T (the motor is simulated) or upstream of the socket. Before power-on, '
     'an ohmmeter check catches a swap. FW 1L1 to RV 5L3 should be ~0 Ω, and FW 1L1 to RV 1L1 should be OL.', True),
    ('Interlocking is electrical only.',
     'FWD and REV are plain NO buttons with no button interlock. The only thing keeping FW and RV from both '
     'pulling in is each one\'s NC 31-32 in the other\'s rung. If your reversing pair has a mechanical interlock '
     'between them, install it too. Operation tests 7 and 8 film exactly this.', True),
    ('Not used in this lab (leave empty).',
     'TB2, TB3, TBG2, TBG3, the selector switch, the limit switches\' NO 13-14, OLF/OLR 97-98, the other CR '
     'socket terminals, and the tops of TB-T1..T3. The spec says "No wiring to extra terminals".', True),
    ('A2 to 95 is a wire YOU install. It is not internal.',
     'Wires 7 (FW A2 → OLF 95) and 12 (RV A2 → OLR 95) are easy to skip, because the overload plugs right onto '
     'the contactor and looks like one unit. But the overload\'s 95-96 is a <b>separate, isolated contact</b>. '
     'Nothing inside connects it to the coil, because the maker can\'t know where you want it in your circuit '
     '(common side, hot side, several starters, a PLC input). Leave 7 or 12 off and that coil has no return path, '
     'so nothing happens when you press FWD or REV, even though every switch tests fine. '
     '<br><br><b>Connections the parts make for you (don\'t wire these):</b> the two terminals of one contact '
     '(1L1-2T1, 7L4-8T4, 31-32, 23-24, a pushbutton\'s pair), connected only when that contact is closed; '
     'the overload\'s <b>A2</b> and <b>14/22</b> pass-throughs, which are the contactor\'s A2 and 8T4 '
     '(note 5; the pin only connects if the contactor\'s screw is tightened on it); the overload\'s line side, which '
     'plugs into the contactor\'s T terminals; and the top and bottom screws of one feed-through TB. '
     '<br><b>Connections you must make:</b> everything else, including A2 → 95 (7, 12), 96 → common (8), '
     'the transformer links (H1-H3, H2-H4, X2-X3) and the comb jumpers (TB4-TB6, TB7-TB9). '
     '<br><b>Rule of thumb:</b> separate contacts on one device are never connected inside it. '
     '<br><b>Check before power-on:</b> with the cord unplugged, ohm from each coil\'s A2 to OLF 96. It should read '
     '~0 Ω through wire 7 or 12 and the closed OL contact. If it reads OL (open), that return is missing. '
     'Powered, the symptom is 24 V (hot to OL 95) but 0 V (hot to coil A2).', False),
]

# ---------------------------------------------------------------------------
# Build order, with quick checks after each stage. Each step:
# (title, what to do, [(where the meter goes, what you do, what it should read), ...])
# ---------------------------------------------------------------------------
BUILD_INTRO = (
    'Wire one section at a time and check it before you move on. A wrong contact block or a loose pin '
    'takes seconds to find on the bench and an afternoon to find in a finished panel. '
    '<b>Rules for every ohm/continuity check:</b> cord unplugged, 3PHIN feed unplugged, and <b>CB2 OFF</b>. '
    'The transformer secondary connects the 24 V bus to common through a few ohms, so with CB2 on, '
    'almost every control check reads "continuous" and tells you nothing. Clip leads help when you need '
    'one hand on a button. "Open" means the meter reads OL.')

BUILD = [
    ('Bench-check the door devices (before wiring them)',
     'Ohm across each contact by itself. This proves the contact blocks are the right type and on the right terminals.',
     [('STOP1 1–2, STOP2 1–2', 'at rest', 'continuous (NC)'),
      ('STOP1 1–2, STOP2 1–2', 'button pressed', 'open'),
      ('FWD 3–4, REV 3–4', 'at rest', 'open (NO)'),
      ('FWD 3–4, REV 3–4', 'button pressed', 'continuous'),
      ('FLS 21–22, RLS 21–22', 'at rest', 'continuous (NC)'),
      ('FLS 21–22, RLS 21–22', 'lever actuated', 'open. In the circuit, FLS opens wire 4 → 5 and drops FW only; '
                                                  'RLS opens wire 9 → 10 and drops RV only'),
      ('FLS 13–14, RLS 13–14', 'at rest / actuated', 'open / continuous (NO, not used in this lab)')]),
    ('Bench-check each contactor and its aux block',
     'With the aux block snapped on the front, push the contactor armature in by hand (unpowered) to operate '
     'every contact. Do this for FW and RV.',
     [('A1–A2', 'at rest', 'a definite resistance (the coil): not 0, not open'),
      ('1L1–2T1, 3L2–4T2, 5L3–6T3, 7L4–8T4', 'at rest', 'open'),
      ('1L1–2T1, 3L2–4T2, 5L3–6T3, 7L4–8T4', 'armature pushed in', 'continuous'),
      ('aux 23–24', 'at rest / pushed in', 'open / continuous (NO, pilot light)'),
      ('aux 31–32', 'at rest / pushed in', 'continuous / open (NC, interlock)')]),
    ('Bench-check each overload and set it up',
     'Set the FLA dial and the AUTO/HAND reset selector where your instructor wants them (HAND: you press R '
     'after a trip; AUTO: it resets itself).',
     [('95–96', 'normal', 'continuous (NC)'),
      ('97–98', 'normal', 'open (NO, not used)'),
      ('95–96 and 97–98', 'trip it with the test button, if your model has one', '95–96 open, 97–98 continuous. Press R to reset, then recheck 95–96')]),
    ('Join each overload to its contactor, then check the pass-throughs right away',
     'Plug the overload onto the contactor and <b>tighten the contactor\'s A2 and 2T1/4T2/6T3 screws</b> onto the '
     'overload\'s pins. Then install the short wire from overload A2 to overload 95 (wire 7 on FW, 12 on RV; see note 10).',
     [('overload A2 to contactor A1', 'at rest', 'coil resistance. Open = the A2 pin isn\'t clamped'),
      ('overload 14/22 to contactor 7L4', 'at rest / armature pushed in', 'open / continuous. Proves the 14/22 pass-through'),
      ('contactor 1L1 to overload 2T1 (same for L2, L3)', 'armature pushed in', 'continuous (through the heater)'),
      ('contactor A1 to overload 96', 'after wire 7 or 12 is on', 'coil resistance. This one check proves the coil, the A2 pin, '
                                                                     'wire 7/12 and the OL contact all at once')]),
    ('Wire the 120 V supply and the transformer (cord, CB1, TB1, TBG1, T1, CB2, TB buses)',
     'Install the primary links H1–H3 and H2–H4, the secondary link X2–X3, and the TB4–TB6 and TB7–TB9 comb jumpers.',
     [('cord plug H to N', 'CB1 on / off', 'low resistance (transformer primary) / open'),
      ('cord plug H and N to G', 'CB1 on', 'open'),
      ('TBG1 to transformer X4', '—', 'continuous (X4 is bonded to ground)'),
      ('TB7 to TB9, TB4 to TB6', '—', 'continuous (comb jumpers seated)'),
      ('<b>Powered</b> (cord in, 3PHIN still unplugged): TB7 to TB4', 'CB2 on / off', '≈24 V AC / 0 V. Then unplug before you go on')]),
    ('Wire the door (jumpers 2, 3, 4, 9, 15)',
     'Check at the door ends of the wires before they go into the duct.',
     [('wire 1 (STOP1 1) to wire 3 (STOP2 2)', 'at rest / either STOP pressed', 'continuous / open'),
      ('wire 3 to wire 4 (FWD 4)', 'at rest / FWD pressed', 'open / continuous'),
      ('wire 3 to wire 9 (REV 4)', 'at rest / REV pressed', 'open / continuous'),
      ('wire 4 to wire 5 (FLS 22)', 'at rest / FLS actuated', 'continuous / open'),
      ('wire 9 to wire 10 (RLS 22)', 'at rest / RLS actuated', 'continuous / open'),
      ('FWDON X2 to REVON X2', '—', 'continuous (wire 15 jumper)')]),
    ('Wire the forward and reverse rungs (wires 1–12)',
     'CB2 OFF for all of these. TB7 is the 24 V bus, TB4 is common.',
     [('TB7 to FW A1', 'nothing pressed', 'open'),
      ('TB7 to FW A1', 'hold FWD', 'continuous'),
      ('TB7 to FW A1', 'hold FWD and actuate FLS', 'open (limit switch)'),
      ('TB7 to FW A1', 'hold FWD and press STOP1 or STOP2', 'open'),
      ('TB7 to FW A1', 'no buttons, push FW\'s armature in', 'continuous (seal-in through 7L4 → 14/22)'),
      ('RV 31 (wire 5) to RV 32 (wire 6)', 'at rest / RV armature pushed in', 'continuous / open. The interlock in the forward rung. '
       '(Check it here, not from TB7: with an armature pushed in, a back path through both coils can fool the meter)'),
      ('FW A2 to TB4', '—', 'continuous (wire 7, OLF 95–96, wire 8)'),
      ('TB7 to TB4', 'nothing pressed / hold FWD', 'open / FW coil resistance. The whole forward rung in one check'),
      ('Repeat for reverse: TB7 to RV A1', 'hold REV, then add RLS or a STOP', 'continuous, then open'),
      ('FW 31 (wire 10) to FW 32 (wire 11)', 'at rest / FW armature pushed in', 'continuous / open (interlock in the reverse rung)'),
      ('TB7 to RV A1', 'no buttons, push RV\'s armature in', 'continuous (seal-in)'),
      ('RV A2 to TB4', '—', 'continuous (wire 12, OLR 95–96, wire 8)'),
      ('TB7 to TB4', 'hold REV', 'RV coil resistance')]),
    ('Wire the pilot lights (wires 13–17)',
     'CB2 OFF.',
     [('TB8 to FWDON X1', 'at rest / FW armature pushed in', 'open / continuous'),
      ('TB9 to REVON X1', 'at rest / RV armature pushed in', 'open / continuous'),
      ('FWDON X2 and REVON X2 to TB4', '—', 'continuous (wire 15)')]),
    ('Wire the power circuit (L1–L3, T1–T3)',
     '3PHIN feed unplugged. Watch for a phase swap: the one place the reversal can go wrong.',
     [('FW 1L1 to RV 5L3, FW 5L3 to RV 1L1, FW 3L2 to RV 3L2', '—', '≈0 Ω'),
      ('FW 1L1 to RV 1L1', '—', 'open (if it\'s continuous, L1/L3 aren\'t swapped)'),
      ('socket 24 (L1) to TB-T1, TB-T2, TB-T3', 'nothing pushed', 'all open'),
      ('socket 24 (L1) to TB-T1', 'FW armature pushed in', 'continuous'),
      ('socket 24 (L1) to TB-T3', 'RV armature pushed in', 'continuous (RV swaps L1 and L3)'),
      ('any L to any other L, any L to ground', '—', 'open')]),
    ('First power-up: control circuit only',
     'Cord in, 3PHIN still unplugged, CB2 on. If something doesn\'t work, put the black lead on TB4 and walk the red lead '
     'down the rung (TB7, wire 2, wire 3, then hold FWD: wire 4, wire 5, A1). The fault is between the last point '
     'with 24 V and the first with 0 V. If A1 has 24 V and the coil won\'t pull in, check A2: 24 V there means the '
     'return (wire 7 / OL 95–96 / wire 8) is open.',
     [('Press FWD', '—', 'FW pulls in, stays in after release, FWDON lights'),
      ('Press REV while FW is running', '—', 'nothing happens (interlock)'),
      ('Press STOP1, then STOP2 (restart in between)', '—', 'FW drops out each time'),
      ('Actuate FLS while FW is running', '—', 'FW drops out; RV still starts with REV'),
      ('Repeat all of the above for REV, REVON and RLS', '—', 'same, mirrored'),
      ('Then, with the instructor: plug in 3PHIN', '—', 'run the operation tests on the lab sheet')]),
]


def build_html():
    out = [f'<p>{BUILD_INTRO}</p>']
    for i, (title, do, checks) in enumerate(BUILD, 1):
        rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in checks)
        out.append(f'<div class="step"><h3><span class="snum">{i}</span>{title}</h3><p>{do}</p>'
                   f'<table><thead><tr><th style="width:34%">Meter on</th><th style="width:24%">Condition</th>'
                   f'<th>Should read</th></tr></thead><tbody>{rows}</tbody></table></div>')
    return '\n'.join(out)


def html_page(fig1, fig2):
    legend = (
        '<div class="legend">'
        '<span><span class="ln" style="background:#d0262b"></span>red: 24 V control (hot side)</span>'
        '<span><span class="ln" style="background:#fff;outline:1.5px solid #888"></span>white: 24 V common (X4N) / 120 V neutral</span>'
        '<span><span class="ln" style="background:#151515"></span>black: 120 V hot and 3-phase</span>'
        '<span><span class="ln" style="background:#1d8a3c"></span>green: ground</span>'
        '<span><span class="sw" style="background:#fff;border-radius:8px"></span>wire number</span>'
        f'<span><span class="sw" style="background:{CROSS_FILL};border-radius:8px"></span>wire number that crosses the door (one of the 9)</span>'
        '</div>')
    rows, last = [], None
    for k, s in enumerate(S, 1):
        if s['group'] != last:
            rows.append(f'<tr class="grp"><td colspan="7">{html.escape(s["group"])}</td></tr>')
            last = s['group']
        a = '<i>cord</i>' if s['route'] == 'cord' else html.escape(name(s['a']))
        cross = s['route'] == 'cross'
        rows.append(
            f'<tr><td>{k}</td><td><b>{html.escape(s["num"])}</b></td>'
            f'<td><span class="sw" style="background:{FILL[s["color"]]}"></span>{s["color"]}</td>'
            f'<td>{a}</td><td>{html.escape(name(s["b"]))}</td>'
            f'<td>{"<b>" if cross else ""}{ROUTE_TXT[s["route"]]}{"</b>" if cross else ""}</td>'
            f'<td>{html.escape(s["note"])}</td></tr>')
    notes = []
    for i, (title, body, minor) in enumerate(NOTES, 1):
        notes.append(f'<div class="issue{" minor" if minor else ""}"><span class="num">{i}</span><b>{title}</b> {body}</div>')
    ends = label_ends()
    nlab = len(ends)
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lab 3 Motor Control: Forward/Reverse Wiring Diagrams (PRELIMINARY)</title>
<style>
:root{{color-scheme:light}}
body{{margin:0;background:#f6f6f4;color:#1c1c1c;font:15px/1.5 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
main{{max-width:1180px;margin:0 auto;padding:28px 20px 60px}}
h1{{font-size:26px;margin:0 0 4px}} h2{{font-size:20px;margin:38px 0 8px}}
.lede{{color:#555;margin:0 0 18px}}
.prelim{{background:#fff4e0;border:2px solid #e07800;border-radius:8px;padding:10px 14px;margin:12px 0}}
figure{{margin:14px 0;background:#fff;border:1px solid #ddd;border-radius:10px;padding:10px}}
figure svg{{width:100%;height:auto;display:block}}
figcaption{{font-size:13.5px;color:#555;padding:8px 6px 2px}}
.legend{{display:flex;flex-wrap:wrap;gap:14px;font-size:13px;margin:6px 4px}}
.legend span{{display:inline-flex;align-items:center;gap:6px}}
.ln{{display:inline-block;width:28px;height:4px;border-radius:2px}}
.sw{{display:inline-block;width:12px;height:12px;border-radius:3px;border:1px solid #888;margin-right:6px;vertical-align:-1px}}
table{{border-collapse:collapse;width:100%;font-size:13.5px;background:#fff}}
th,td{{border-bottom:1px solid #e3e3e3;padding:5px 8px;text-align:left;vertical-align:top}}
th{{background:#f0f0ee}} tr.grp td{{background:#f7f3ea;font-weight:700}}
.issue{{background:#fff;border:1px solid #ddd;border-left:5px solid #e07800;border-radius:8px;padding:10px 14px;margin:10px 0}}
.issue.minor{{border-left-color:#999}}
.num{{display:inline-block;background:#e07800;color:#fff;border-radius:50%;width:22px;height:22px;text-align:center;font-weight:700;font-size:13px;line-height:22px;margin-right:6px}}
.minor .num{{background:#888}}
.step{{background:#fff;border:1px solid #ddd;border-left:5px solid #2f6db5;border-radius:8px;padding:8px 14px 12px;margin:12px 0}}
.step h3{{font-size:16px;margin:4px 0 4px}} .step p{{margin:4px 0 8px}}
.snum{{display:inline-block;background:#2f6db5;color:#fff;border-radius:50%;width:22px;height:22px;text-align:center;font-weight:700;font-size:13px;line-height:22px;margin-right:8px}}
@media print{{.step{{break-inside:avoid}}}}
svg .h{{font-size:15px;font-weight:700;fill:#333}}
svg .dn{{font-size:12.5px;font-weight:700;fill:#222}}
svg .ds{{font-size:11px;fill:#555}}
svg .dl{{font-size:11px;fill:#777;font-style:italic}}
svg .tl{{font-size:11px;fill:#222}}
svg .tlw{{font-size:11px;fill:#fff;font-weight:700}}
svg .tls{{font-size:10px;fill:#111}}
svg text.halo{{paint-order:stroke;stroke:#fff;stroke-width:5px;stroke-linejoin:round}}
svg .wt{{font-size:10.5px;font-weight:700;fill:#111}}
@media print{{body{{background:#fff}} figure{{break-inside:avoid}} .issue{{break-inside:avoid}}}}
</style></head><body><main>
<h1>Lab 3 Motor Control: Forward / Reverse Wiring Diagrams</h1>
<div class="prelim"><b>PRELIMINARY.</b> Drawn from the lab sheet and the layout drawings, before the panel was built.
The wire numbers and from/to terminals follow LAB3-F20b. The physical position of terminals on your parts may
differ (see note 1). Every wire number has a tag at <b>both ends</b>, so you can label as you go. Printable labels:
<a href="wire-labels.html">wire-labels.html</a> ({nlab} labels).</div>
<div class="prelim"><b>Commonly missed: wires 7 and 12 (coil A2 → overload 95).</b> They are not internal connections.
Without them the coils have no return path and nothing pulls in. See note 10 for what the parts connect inside and
what you have to wire.</div>
<p class="lede">Figure 1 puts each part where it sits on the door and backplate, in the layout from
<i>Additional Specifications for Lab 3</i>. Figure 2 is the same ladder as LAB3-F20b with the same rung numbers, tags,
terminal numbers and wire numbers, plus wire colors and which wires cross the door. An orange
<span class="num">1</span> is something to settle before wiring; a grey one is background.</p>
{legend}

<h2>Figure 1: Physical wiring diagram</h2>
<figure>{fig1}
<figcaption>The door is shown from the inside, so it is the mirror image of the front. From the front the order is
STOP1, FWD, STOP2, REV, selector, FLS, RLS, FWDON, REVON, AC IN. Duct routes are simplified. What matters is the
terminal each wire lands on and that the 9 door wires use the right-hand tray. Grey terminal circles are used; pale
ones stay empty.</figcaption></figure>

<h2>Figure 2: The lab ladder, with wire numbers, colors and locations</h2>
<figure>{fig2}
<figcaption>Same rungs, contacts and wire numbers as LAB3-F20b. The FW and RV contactors interlock electrically: each
one's NC 31-32 is in the other's rung. The seal-in contacts (7L4 to 14/22) sit across the FWD and REV buttons. The
limit switches drop out their own direction only.</figcaption></figure>

<h2>Build order, with quick checks along the way</h2>
{build_html()}

<h2>Wire list (one row per physical conductor, in a sensible wiring order)</h2>
<table><thead><tr><th>#</th><th>Wire</th><th>Color</th><th>From</th><th>To</th><th>Route</th><th>Note</th></tr></thead><tbody>
{chr(10).join(rows)}
</tbody></table>
<p style="font-size:13px;color:#666">{len(S)} conductors, {nlab} labeled ends (the cord conductors are labeled at the
panel end only). Each TB terminal is a feed-through, so its top and bottom screws are the same point. All wire is
16 AWG stranded. Max 2 wires per terminal, 1 per circuit-breaker terminal.</p>

<h2>Things to check</h2>
{chr(10).join(notes)}
</main></body></html>
'''


def labels_page():
    ends = sorted(label_ends(), key=lambda e: (num_key(e['num']), e['seg']))
    counts = {}
    for e in ends:
        counts[e['num']] = counts.get(e['num'], 0) + 1
    summary = ' · '.join(f'<b>{n}</b>×{c}' for n, c in sorted(counts.items(), key=lambda kv: num_key(kv[0])))
    cells = []
    for e in ends:
        cross = e['num'] in CROSS_NUMS
        cells.append(f'<div class="lab{" x" if cross else ""}"><div class="n">{html.escape(e["num"])}</div>'
                     f'<div class="w">{html.escape(e["at"])}</div></div>')
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>Lab 3 wire labels (PRELIMINARY)</title>
<style>
body{{font:13px/1.4 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:16px;color:#111}}
h1{{font-size:18px;margin:0 0 4px}} p{{margin:4px 0 10px;color:#444}}
.grid{{display:flex;flex-wrap:wrap;gap:0}}
.lab{{width:1.25in;height:0.5in;box-sizing:border-box;border:1px dashed #999;padding:2px 4px;
      display:flex;flex-direction:column;justify-content:center;align-items:center;overflow:hidden}}
.lab .n{{font-size:20px;font-weight:800;line-height:1}}
.lab .w{{font-size:7.5px;color:#444;white-space:nowrap;line-height:1.2}}
.lab.x{{background:#ffe680}}
@media print{{body{{margin:0.3in}} .noprint{{display:none}} .lab.x{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}}}
</style></head><body>
<div class="noprint">
<h1>Lab 3 Forward/Reverse: wire-number labels (PRELIMINARY)</h1>
<p>One label per wire end ({len(ends)} total), sorted by wire number. The big number goes on the wire. The small
text is the terminal that end lands on, so you can find it while wiring. Yellow = one of the 9 door-channel wires.
Print at 100% scale and cut on the dashed lines. With a label maker, import <code>wire-labels.csv</code> instead.</p>
<p>Count per wire: {summary}</p>
</div>
<div class="grid">{''.join(cells)}</div>
</body></html>
'''


def main():
    with open(os.path.join(OUT, 'wiring-diagrams.html'), 'w') as f:
        f.write(html_page(figure1(), figure2()))
    with open(os.path.join(OUT, 'wire-labels.html'), 'w') as f:
        f.write(labels_page())
    with open(os.path.join(OUT, 'wire-labels.csv'), 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['label', 'lands_on', 'color', 'door_channel'])
        for e in sorted(label_ends(), key=lambda e: (num_key(e['num']), e['seg'])):
            w.writerow([e['num'], e['at'], e['color'], 'yes' if e['num'] in CROSS_NUMS else ''])
    print(f'{len(S)} conductors, {len(label_ends())} labels, door wires: {CROSS_NUMS}')


if __name__ == '__main__':
    main()
