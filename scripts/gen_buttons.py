from html import escape

CW = 7.8
BTNS = {
    "website": ("❯", "mmdpy.github.io"),
    "resume": ("↓", "resume.pdf"),
    "linkedin": ("in", "linkedin"),
    "email": ("@", "email"),
    "paper": ("§", "paper · IJAIED 2025"),
}

for name, (icon, label) in BTNS.items():
    w = round(30 + len(label) * CW + 18)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="32" viewBox="0 0 {w} 32" role="img" aria-label="{escape(label)}">
<style>text {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 13px; }}</style>
<rect x=".5" y=".5" width="{w - 1}" height="31" rx="7" fill="#0c1016" stroke="#1a212b"/>
<text x="14" y="20.5" fill="#3ddc97" font-weight="700">{escape(icon)}</text>
<text x="34" y="20.5" fill="#c9d1d9">{escape(label)}</text>
</svg>'''
    with open(f"assets/btn-{name}.svg", "w") as f:
        f.write(svg)
    print(f"assets/btn-{name}.svg  {w}px")
