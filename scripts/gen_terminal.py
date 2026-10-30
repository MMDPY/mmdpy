from html import escape

W, H = 880, 338
PANEL, LINE = "#0c1016", "#1a212b"
CW = 8.45
X0, Y0, LH = 28, 78, 22
G, B, Y, D, F, WH = "#3ddc97", "#5fb3ff", "#ffb454", "#6b7684", "#c9d1d9", "#ffffff"

script = [
    ("cmd", "whoami"),
    ("out", [("Mohammad Karimi", WH, True), ("  ·  ", D, False), ("Staff AI Engineer @ Proofpoint", G, False), ("  ·  Toronto", D, False)]),
    ("gap",),
    ("cmd", "cat now.txt"),
    ("out", [("› ", G, False), ("shipping a ", F, False), ("sub-second speech-to-speech", WH, True), (" compliance agent", F, False)]),
    ("out", [("› ", G, False), ("agents + subagents + tools, over ", F, False), ("20M+ messages/day", WH, True)]),
    ("gap",),
    ("cmd", "./bench --prod"),
    ("out", [("latency  ", D, False), ("< 1s    ", G, True), ("cost  ", D, False), ("10–122× ↓    ", G, True), ("recall@5  ", D, False), ("94%    ", G, True), ("search  ", D, False), ("−65%", G, True)]),
    ("gap",),
    ("cmd", "ls ~/systems"),
    ("out", [("voice-investigator  agentic-decisioning  archive-rag  llm-serving  redaction-api", B, False)]),
    ("gap",),
    ("cmd", "open mmdpy.github.io"),
]

PROMPT = (f'<tspan fill="{G}">mohammad</tspan><tspan fill="{D}">@</tspan><tspan fill="{B}">toronto</tspan>'
          f'<tspan fill="{Y}">&#160;~</tspan><tspan fill="{G}">&#160;❯&#160;</tspan>')
PLEN = len("mohammad@toronto ~ ❯ ")

defs, body = [], []
t, y = 0.4, Y0
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

css = """
text { font-family: ui-monospace, SFMono-Regular, 'JetBrains Mono', Menlo, Consolas, monospace; font-size: 14px; }
.o { opacity: 0; animation: show .01s linear forwards; }
@keyframes show { to { opacity: 1; } }
.cur { animation: blink 1s steps(1) infinite; }
@keyframes blink { 50% { opacity: 0; } }
"""

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Terminal: Mohammad Karimi, Staff AI Engineer at Proofpoint. Sub-second speech-to-speech agent, 20M+ messages per day, 10 to 122 times cheaper inference.">
<style>{css}</style>
<defs>
  <radialGradient id="glow" cx="85%" cy="0%" r="70%"><stop offset="0" stop-color="{G}" stop-opacity=".10"/><stop offset="1" stop-color="{G}" stop-opacity="0"/></radialGradient>
  <pattern id="scan" width="4" height="3" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#fff" fill-opacity=".02"/></pattern>
  {"".join(defs)}
</defs>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="12" fill="{PANEL}" stroke="{LINE}"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="12" fill="url(#glow)"/>
<path d="M12.5 .5 H{W - 12.5} A12 12 0 0 1 {W - .5} 12.5 V40 H.5 V12.5 A12 12 0 0 1 12.5 .5Z" fill="#10151c"/>
<line x1="0" y1="40.5" x2="{W}" y2="40.5" stroke="{LINE}"/>
<circle cx="24" cy="20.5" r="6" fill="#ff5f57"/><circle cx="44" cy="20.5" r="6" fill="#febc2e"/><circle cx="64" cy="20.5" r="6" fill="#28c840"/>
<text x="{W / 2}" y="25" fill="{D}" text-anchor="middle" style="font-size:12px">mohammad@toronto: ~ — zsh</text>
<circle cx="{W - 78}" cy="20.5" r="3.5" fill="{G}"><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="{W - 68}" y="25" fill="{D}" style="font-size:12px">online</text>
{"".join(body)}
<rect x=".5" y="41" width="{W - 1}" height="{H - 42}" rx="12" fill="url(#scan)" pointer-events="none"/>
</svg>'''

with open("assets/terminal.svg", "w") as f:
    f.write(svg)
print(f"wrote assets/terminal.svg · animation {t:.1f}s · last line y={y - LH}")
