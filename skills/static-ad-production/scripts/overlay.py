"""Put Hebrew ad text on a generated image and export a 1080x1350 (4:5) PNG.

The image model draws the photo without text. This script lays the Hebrew
headline on top through headless Chrome, so the RTL text and the font are
always correct. Colors are brand-neutral by default; pass your brand colors
with --fg / --fg2 / --accent / --shade.

Usage:
  python overlay.py --image in.png --out out.png --headline "..." [--sub "..."]
                    [--badge "..."] [--theme light|dark] [--size 1080x1350]
                    [--fg "#111111"] [--fg2 "#333333"] [--accent "#D3192B"]
                    [--shade "rgba(247,242,232,.92)"] [--font Heebo]
"""
import argparse
import base64
import html
import mimetypes
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/usr/bin/google-chrome", "/opt/pw-browsers/chromium",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

THEMES = {
    # fg = headline, fg2 = sub line, shade = gradient behind the text, tshadow = text shadow
    "light": dict(fg="#111111", fg2="#333333", shade="rgba(247,242,232,.92)", tshadow="none"),
    "dark": dict(fg="#FFFFFF", fg2="#E6E6E6", shade="rgba(15,15,20,.85)",
                 tshadow="0 2px 12px rgba(0,0,0,.35)"),
}

TEMPLATE = """<!doctype html>
<html lang="he" dir="rtl"><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family={font_q}:wght@500;800;900&display=block" rel="stylesheet">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html, body {{ width:{w}px; height:{h}px; overflow:hidden; }}
  body {{ font-family:'{font}', Arial, sans-serif; position:relative; background:#000; }}
  .bg {{ position:absolute; inset:0; background:url('{img}') center/cover no-repeat; }}
  .shade {{ position:absolute; left:0; right:0; top:0; height:48%;
           background:linear-gradient(to bottom, {shade} 0%, {shade} 35%, transparent 100%); }}
  .txt {{ position:absolute; top:{pad}px; right:{pad}px; left:{pad}px; text-align:center; }}
  h1 {{ font-weight:900; font-size:{hs}px; line-height:1.08; color:{fg}; letter-spacing:-1px;
        text-shadow:{tshadow}; }}
  p {{ margin-top:22px; font-weight:500; font-size:{ss}px; line-height:1.3; color:{fg2};
       text-shadow:{tshadow}; }}
  .badge {{ position:absolute; bottom:{pad}px; right:50%; transform:translateX(50%);
            background:{accent}; color:#fff; font-weight:800; font-size:{bs}px;
            padding:18px 44px; border-radius:999px; white-space:nowrap;
            box-shadow:0 6px 20px rgba(0,0,0,.25); }}
</style></head><body>
<div class="bg"></div><div class="shade"></div>
<div class="txt"><h1>{headline}</h1>{sub}</div>
{badge}
</body></html>"""


def find_chrome():
    for p in CHROME_PATHS:
        if os.path.exists(p):
            return p
    for name in ("google-chrome", "chromium", "chromium-browser", "msedge"):
        found = shutil.which(name)
        if found:
            return found
    sys.exit("Chrome or Edge not found. Install one or set CHROME_PATHS in this script.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--image", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--headline", required=True)
    ap.add_argument("--sub", default="")
    ap.add_argument("--badge", default="")
    ap.add_argument("--theme", choices=sorted(THEMES), default="light")
    ap.add_argument("--size", default="1080x1350", help="WIDTHxHEIGHT, default 1080x1350 (4:5)")
    ap.add_argument("--fg", help="headline color, overrides the theme")
    ap.add_argument("--fg2", help="sub line color, overrides the theme")
    ap.add_argument("--accent", default="#D3192B", help="badge background color")
    ap.add_argument("--shade", help="gradient color behind the text, overrides the theme")
    ap.add_argument("--font", default="Heebo", help="Google font family name")
    a = ap.parse_args()

    w, h = (int(x) for x in a.size.lower().split("x"))
    mime = mimetypes.guess_type(a.image)[0] or "image/png"
    img = f"data:{mime};base64," + base64.b64encode(Path(a.image).read_bytes()).decode()

    t = dict(THEMES[a.theme])
    if a.fg:
        t["fg"] = a.fg
    if a.fg2:
        t["fg2"] = a.fg2
    if a.shade:
        t["shade"] = a.shade

    esc = lambda s: html.escape(s).replace("\\n", "<br>").replace("\n", "<br>")
    page = TEMPLATE.format(
        w=w, h=h, img=img, accent=a.accent, font=a.font, font_q=a.font.replace(" ", "+"),
        pad=round(w * 0.07), hs=round(w * 0.085), ss=round(w * 0.04), bs=round(w * 0.036),
        headline=esc(a.headline),
        sub=f"<p>{esc(a.sub)}</p>" if a.sub else "",
        badge=f'<div class="badge">{esc(a.badge)}</div>' if a.badge else "",
        **t,
    )

    with tempfile.TemporaryDirectory() as td:
        page_path = Path(td) / "ad.html"
        page_path.write_text(page, encoding="utf-8")
        out = str(Path(a.out).resolve())
        subprocess.run([
            find_chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-sandbox",
            f"--window-size={w},{h}", "--virtual-time-budget=6000",
            f"--screenshot={out}", page_path.as_uri(),
        ], check=True, capture_output=True)
    print(out)


if __name__ == "__main__":
    main()
