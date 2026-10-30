"""Builds assets/banner.svg — the animated terminal banner at the top of the profile README.

Needs assets/_photo360.jpg (a 360×360 copy of the profile photo); it gets embedded as base64.
"""
import base64
from html import escape

W, H = 1000, 360
PANEL, LINE = "#0c1016", "#1a212b"
CW = 8.45
G, B, Y, D, F, WH, HOT = "#3ddc97", "#5fb3ff", "#ffb454", "#6b7684", "#c9d1d9", "#ffffff", "#ff8a3d"

PX, PY, PW, PH = 28, 62, 252, 270          # photo frame
X0, Y0, LH = PX + PW + 36, 80, 22         # terminal text column

script = [
    ("cmd", "whoami"),
    ("out", [("Mohammad Karimi", WH, True), ("  ·  ", D, False), ("Staff AI Engineer @ Proofpoint", G, False), ("  ·  Toronto", D, False)]),
    ("gap",),
    ("cmd", "cat now.txt"),
    ("out", [("› ", G, False), ("a ", F, False), ("sub-second speech-to-speech", WH, True), (" multi-agent system", F, False)]),
    ("out", [("› ", G, False), ("LLM inference on Kubernetes at ", F, False), ("20M+ messages/day", WH, True)]),
    ("gap",),
    ("cmd", "./bench --prod"),
    ("out", [("latency ", D, False), ("<1s   ", G, True), ("cost ", D, False), ("10–122×↓   ", G, True), ("recall@5 ", D, False), ("94%   ", G, True), ("false+ ", D, False), ("−45%", G, True)]),
    ("gap",),
    ("cmd", "ls ~/systems"),
    ("out", [("voice-investigator  automate-inference  hybrid-rag", B, False)]),
    ("out", [("agentic-decisioning  distilled-compliance-llm  redaction-api", B, False)]),
    ("gap",),
    ("cmd", "open mmdpy.github.io"),
]

PROMPT = f'<tspan fill="{G}" font-weight="700">mmdpy</tspan><tspan fill="{B}">&#160;~</tspan><tspan fill="{G}">&#160;❯&#160;</tspan>'
PLEN = len("mmdpy ~ ❯ ")

defs, body = [], []
t, y = 1.1, Y0
last = None
for i, step in enumerate(script):
    kind = step[0]
    if kind == "gap":
        y += 8
        continue
    if kind == "cmd":
        cmd = step[1]
        cx = X0 + PLEN * CW
        start = t + 0.15
        dur = max(0.35, len(cmd) * 0.055)
        widths = ";".join(f"{k * CW:.1f}" for k in range(len(cmd) + 1))
        defs.append(f'<clipPath id="c{i}"><rect x="{cx:.1f}" y="{y - 16}" height="22" width="0">'
                    f'<animate attributeName="width" begin="{start:.2f}s" dur="{dur:.2f}s" fill="freeze" calcMode="discrete" values="{widths}"/></rect></clipPath>')
        body.append(f'<g class="o" style="animation-delay:{t:.2f}s">'
                    f'<text x="{X0}" y="{y}">{PROMPT}</text>'
                    f'<text x="{cx:.1f}" y="{y}" fill="{WH}" font-weight="700" clip-path="url(#c{i})">{escape(cmd)}</text></g>')
        last = (cx + len(cmd) * CW + 3, y, start + dur)
        t = start + dur + 0.25
        y += LH
    else:
        spans = "".join(f'<tspan fill="{c}"{" font-weight=\"700\"" if b else ""}>{escape(s).replace(" ", "&#160;")}</tspan>' for s, c, b in step[1])
        body.append(f'<text class="o" style="animation-delay:{t:.2f}s" x="{X0}" y="{y}">{spans}</text>')
        t += 0.18
        y += LH

cx, cy, ct = last
body.append(f'<g class="o" style="animation-delay:{ct:.2f}s"><rect class="cur" x="{cx:.1f}" y="{cy - 14}" width="8" height="17" fill="{G}"/></g>')

# --- photo: LED-matrix look via a dot-grid mask, with a vignette and a scan-in reveal ---
photo_b64 = base64.b64encode(open("assets/_photo360.jpg", "rb").read()).decode()
crop_x, crop_y, crop_w = 38.0, 6.0, 284.0          # face crop inside the 360px image
scale = PW / crop_w
img_size = 360 * scale
img_x, img_y = PX - crop_x * scale, PY - crop_y * scale
CELL = 6
photo = f'''
  <pattern id="led" x="{PX}" y="{PY}" width="{CELL}" height="{CELL}" patternUnits="userSpaceOnUse">
    <rect x=".6" y=".6" width="{CELL - 1.2}" height="{CELL - 1.2}" rx="1.3" fill="#fff"/>
  </pattern>
  <radialGradient id="vig" cx="50%" cy="48%" r="58%">
    <stop offset=".72" stop-color="#fff"/><stop offset="1" stop-color="#000"/>
  </radialGradient>
  <mask id="ledmask" maskUnits="userSpaceOnUse" x="{PX}" y="{PY}" width="{PW}" height="{PH}">
    <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="url(#vig)"/>
  </mask>
  <mask id="dots" maskUnits="userSpaceOnUse" x="{PX}" y="{PY}" width="{PW}" height="{PH}">
    <rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="url(#led)"/>
  </mask>
  <clipPath id="scanin"><rect x="{PX}" y="{PY}" width="{PW}" height="0">
    <animate attributeName="height" begin="0.15s" dur="0.9s" fill="freeze" values="0;{PH}" calcMode="spline" keySplines=".2 .8 .2 1"/>
  </rect></clipPath>'''
defs.append(photo)

photo_layer = f'''
<g clip-path="url(#scanin)">
  <g mask="url(#ledmask)">
    <g mask="url(#dots)">
      <image href="data:image/jpeg;base64,{photo_b64}" x="{img_x:.1f}" y="{img_y:.1f}" width="{img_size:.1f}" height="{img_size:.1f}" style="filter:saturate(1.15) contrast(1.05)"/>
    </g>
  </g>
</g>
<rect x="{PX}" y="{PY}" width="{PW}" height="2" fill="{G}" opacity="0">
  <animate attributeName="y" begin="0.15s" dur="0.9s" values="{PY};{PY + PH}" calcMode="spline" keySplines=".2 .8 .2 1" fill="freeze"/>
  <animate attributeName="opacity" begin="0.15s" dur="0.9s" values="0;.9;.9;0" fill="freeze"/>
</rect>'''

css = """
text { font-family: ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace; font-size: 14px; }
.o { opacity: 0; animation: show .01s linear forwards; }
@keyframes show { to { opacity: 1; } }
.cur { animation: blink 1s steps(1) infinite; }
@keyframes blink { 50% { opacity: 0; } }
"""

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="mmdpy terminal: Mohammad Karimi, Staff AI Engineer at Proofpoint. Sub-second speech-to-speech agent, 20M+ messages per day, 10 to 122 times cheaper inference.">
<style>{css}</style>
<defs>
  <radialGradient id="glow" cx="90%" cy="0%" r="70%"><stop offset="0" stop-color="{G}" stop-opacity=".12"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></radialGradient>
  <radialGradient id="glow2" cx="0%" cy="100%" r="60%"><stop offset="0" stop-color="{HOT}" stop-opacity=".10"/><stop offset="1" stop-color="{HOT}" stop-opacity="0"/></radialGradient>
  <linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{G}" stop-opacity=".55"/><stop offset=".5" stop-color="{LINE}"/><stop offset="1" stop-color="{B}" stop-opacity=".55"/></linearGradient>
  <pattern id="scan" width="4" height="3" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" fill-opacity=".02"/></pattern>
  {"".join(defs)}
</defs>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{PANEL}"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="url(#glow)"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="url(#glow2)"/>
<path d="M14.5 .5 H{W - 14.5} A14 14 0 0 1 {W - .5} 14.5 V40 H.5 V14.5 A14 14 0 0 1 14.5 .5Z" fill="#10151c"/>
<line x1="0" y1="40.5" x2="{W}" y2="40.5" stroke="{LINE}"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="url(#edge)"/>
<circle cx="24" cy="20.5" r="6" fill="#ff5f57"/><circle cx="44" cy="20.5" r="6" fill="#febc2e"/><circle cx="64" cy="20.5" r="6" fill="#28c840"/>
<text x="{W / 2}" y="25" fill="{D}" text-anchor="middle" style="font-size:12px">mmdpy — zsh — ~/portfolio</text>
<circle cx="{W - 78}" cy="20.5" r="3.5" fill="{G}"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="{W - 68}" y="25" fill="{D}" style="font-size:12px">online</text>
{photo_layer}
{"".join(body)}
<rect x=".5" y="41" width="{W - 1}" height="{H - 42}" rx="14" fill="url(#scan)" pointer-events="none"/>
</svg>'''

with open("assets/banner.svg", "w") as f:
    f.write(svg)
print(f"wrote assets/banner.svg · {len(svg) // 1024} KB · animation {t:.1f}s · last text y={y - LH}")
