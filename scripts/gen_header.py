"""Builds assets/header.svg, the top of the profile README. Same palette and font as mmdpy.github.io.

Fonts are embedded because GitHub serves README images through a proxy that can't load web fonts.
"""
import base64
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
font_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "/tmp")
f400 = base64.b64encode((font_dir / "plex400.woff2").read_bytes()).decode()
f600 = base64.b64encode((font_dir / "plex600.woff2").read_bytes()).decode()

W, H = 1200, 436
BG, FG, HI, DIM, RULE, INK = "#0e0e0d", "#d9d5ca", "#f4f1e8", "#7d796f", "#2a2926", "#ff6a3d"
X0, X1 = 48, W - 48

stats = [
    ("20M+", "messages a day"),
    ("< 1 s", "speech-to-speech"),
    ("10\u2013122x", "cheaper than AWS"),
    ("94%", "recall@5, email archive"),
]
col = (X1 - X0) / len(stats)

tabs = ["0:man", "1:work", "2:systems", "3:oss", "4:skills", "5:paper", "6:contact"]

svg = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Mohammad Karimi, Staff AI Engineer at Proofpoint">
<style>
@font-face {{ font-family: P; font-weight: 400; src: url(data:font/woff2;base64,{f400}) format("woff2"); }}
@font-face {{ font-family: P; font-weight: 600; src: url(data:font/woff2;base64,{f600}) format("woff2"); }}
text {{ font-family: P, ui-monospace, Menlo, Consolas, monospace; }}
.cur {{ animation: b 1.1s steps(1) infinite; }}
@keyframes b {{ 50% {{ opacity: 0; }} }}
</style>
<rect width="{W}" height="{H}" fill="{BG}"/>
<text y="52" font-size="18" fill="{DIM}"><tspan x="{X0}">MMDPY(1)</tspan><tspan x="{W/2}" text-anchor="middle">General Commands Manual</tspan><tspan x="{X1}" text-anchor="end">MMDPY(1)</tspan></text>
<text x="{X0}" y="138" font-size="56" font-weight="600" fill="{HI}" letter-spacing="-1">Mohammad Karimi</text>
<text x="{X0}" y="184" font-size="24" fill="{FG}">Staff AI Engineer at Proofpoint<tspan fill="{DIM}">, Toronto</tspan></text>
<text font-size="19" fill="{DIM}"><tspan x="{X1}" y="100" text-anchor="end">currently:</tspan></text>
<text font-size="19" fill="{FG}" text-anchor="end"><tspan x="{X1}" y="128">a voice agent that answers</tspan><tspan x="{X1}" y="155">compliance investigators</tspan><tspan x="{X1}" y="182">in under a second.</tspan></text>
<line x1="{X0}" x2="{X1}" y1="226" y2="226" stroke="{RULE}"/>
''']

for i, (n, label) in enumerate(stats):
    x = X0 + i * col
    svg.append(f'<text x="{x:.0f}" y="292" font-size="44" font-weight="600" fill="{INK}">{n.replace("<", "&lt;")}</text>')
    svg.append(f'<text x="{x:.0f}" y="324" font-size="18" fill="{DIM}">{label}</text>')

svg.append(f'<text x="{X0}" y="374" font-size="20"><tspan fill="{INK}">mmdpy</tspan><tspan fill="{FG}">:~$ </tspan></text>')
svg.append(f'<rect class="cur" x="{X0 + 9 * 12:.0f}" y="357" width="12" height="22" fill="{FG}"/>')

bar_y = H - 34
svg.append(f'<rect x="0" y="{bar_y}" width="{W}" height="34" fill="{FG}"/>')
x = X0
cw = 9.6
parts = [("[mmdpy]", True, False)] + [(t, False, i == 0) for i, t in enumerate(tabs)]
for label, bold, on in parts:
    w = (len(label) + 2) * cw
    if on:
        svg.append(f'<rect x="{x - cw:.1f}" y="{bar_y}" width="{w:.1f}" height="34" fill="{BG}"/>')
    weight = ' font-weight="600"' if bold else ""
    svg.append(f'<text x="{x:.1f}" y="{bar_y + 23}" font-size="16"{weight} fill="{FG if on else BG}">{label}</text>')
    x += w
svg.append(f'<text x="{X1}" y="{bar_y + 23}" font-size="16" fill="{BG}" text-anchor="end">mmdpy.github.io</text>')
svg.append("</svg>")

out = HERE / "assets" / "header.svg"
out.parent.mkdir(exist_ok=True)
out.write_text("\n".join(svg))
print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
