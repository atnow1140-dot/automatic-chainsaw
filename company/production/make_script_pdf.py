"""台本（Markdown）をPDFにする

使い方:
  python3 company/production/make_script_pdf.py scripts/ep01_xxx.md [出力.pdf]

出力を省略すると、台本と同じ場所に同じ名前の .pdf を作る。
台本の書き方（ep01 と同じ形）:
  **画**：…      → 映像の指示（グレーの枠）
  **ナレ**       → 次の行からシンのナレーション
  **テロップ**：… → 黒帯のテロップ。**太字**は黄、（「〇〇」を赤）と書いた語は赤
"""
import html
import os
import re
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
ASSETS = os.path.join(ROOT, "company", "design", "assets")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@font-face{font-family:NB;src:url('file://%(a)s/NotoSansCJKjp-Bold.otf')}
@font-face{font-family:NK;src:url('file://%(a)s/NotoSansCJKjp-Black.otf')}
@font-face{font-family:IPA;src:url('file:///usr/share/fonts/opentype/ipafont-gothic/ipag.ttf')}
@page{size:A4;margin:16mm 16mm 18mm}
*{box-sizing:border-box}
body{font-family:IPA,sans-serif;color:#2b211a;font-size:10.5pt;line-height:1.75;margin:0}
h1{font-family:NK;font-size:22pt;line-height:1.35;margin:0 0 6mm;color:#1c140e}
h2{font-family:NB;font-size:14pt;margin:9mm 0 3mm;padding:2mm 0 2mm 4mm;border-left:6px solid #2e7d32;background:#f3efe6;break-after:avoid}
h2 .t{font-family:NB;font-size:9.5pt;color:#fff;background:#2b211a;border-radius:3mm;padding:.5mm 2.5mm;margin-left:3mm;vertical-align:middle}
h3{font-family:NB;font-size:12pt;margin:5mm 0 2mm;color:#2e7d32;break-after:avoid}
.cover{text-align:left}
.cover img{width:100%%;border-radius:3mm;margin:2mm 0 5mm;box-shadow:0 1mm 3mm rgba(0,0,0,.25)}
.theme{font-family:NB;color:#2e7d32;font-size:11pt;margin-bottom:2mm}
ul.info{list-style:none;padding:0;margin:0 0 4mm}
ul.info li{padding:1mm 0;border-bottom:1px dashed #d8cfbf}
ul.info b{font-family:NB;display:inline-block;width:26mm;color:#6b5a48}
table{border-collapse:collapse;width:100%%;font-size:9.5pt;margin:2mm 0 4mm}
th{font-family:NB;background:#2b211a;color:#fff;padding:1.5mm 2mm;text-align:left}
td{padding:1.5mm 2mm;border-bottom:1px solid #e3dccf}
tr:nth-child(even) td{background:#faf7f1}
.legend{font-size:9pt;color:#6b5a48;background:#faf7f1;padding:2mm 3mm;border-radius:2mm}
.legend span{display:inline-block;margin-right:4mm}
.blk{break-inside:avoid;margin:2.5mm 0}
.ga{background:#eeeeee;border-radius:2mm;padding:2mm 3mm;color:#444;font-size:9.5pt}
.ga:before{content:'画';font-family:NB;background:#777;color:#fff;border-radius:1mm;padding:0 1.5mm;margin-right:2mm}
.na{border-left:3px solid #c9a86a;padding:.5mm 0 .5mm 4mm}
.na .lb{font-family:NB;font-size:8.5pt;color:#b08a45;display:block;margin-bottom:.5mm}
.te{background:#111;color:#fff;font-family:NB;font-size:12pt;padding:2.5mm 4mm;border-radius:2mm}
.te:before{content:'テロップ';font-size:7.5pt;color:#111;background:#fff;border-radius:1mm;padding:0 1.5mm;margin-right:3mm;vertical-align:middle}
.y{color:#FFD400}.r{color:#EB2323}
.te .note{font-family:IPA;font-size:8pt;color:#999;margin-left:2mm}
.memo{background:#f3efe6;border-radius:2mm;padding:2mm 4mm;font-size:9.5pt}
code{font-size:8.5pt;color:#6b5a48}
hr{border:none;border-top:1px solid #d8cfbf;margin:6mm 0}
.page-break{break-before:page}
"""


def inline(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return s


def telop(text):
    reds = re.findall(r"（「([^」]+)」を赤）", text)
    text = re.sub(r"（「[^」]+」を(赤|黄)）", "", text).strip()
    out = html.escape(text)

    def rep(m):
        w = m.group(1)
        return f'<span class="{"r" if w in reds else "y"}">{w}</span>'

    return re.sub(r"\*\*([^*]+)\*\*", rep, out)


def convert(md, thumb):
    lines = md.splitlines()
    h, i = [], 0
    in_info = False
    while i < len(lines):
        l = lines[i]
        if l.startswith("# "):
            h.append('<div class="cover"><div class="theme">あなたの人生に、小さな気づきの芽を。</div>')
            h.append(f"<h1>{inline(l[2:])}</h1>")
            if thumb:
                h.append(f'<img src="file://{thumb}">')
            h.append("</div>")
        elif l.startswith("## "):
            t = l[3:]
            m = re.match(r"(.*)（(\d+:\d+–\d+:\d+)）$", t)
            if m:
                h.append(f'<h2>{inline(m.group(1))}<span class="t">{m.group(2)}</span></h2>')
            else:
                if t == "全体の流れ":
                    h.append('<div class="page-break"></div>')
                h.append(f"<h2>{inline(t)}</h2>")
            in_info = t == "基本情報"
        elif l.startswith("### "):
            h.append(f"<h3>{inline(l[4:])}</h3>")
        elif l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.match(r"^\|[-| ]+\|$", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip("|").split("|")])
                i += 1
            h.append("<table><tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr>")
            for r in rows[1:]:
                h.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
            h.append("</table>")
            continue
        elif l.startswith("凡例"):
            h.append('<div class="legend"><span><b>画</b>＝映像</span><span><b>ナレ</b>＝シンのナレーション</span>'
                     '<span><b>テロップ</b>＝画面の文字（<span style="color:#b89600">黄＝強調</span>、'
                     '<span style="color:#EB2323">赤＝ひっくり返し</span>）</span></div>')
        elif l.startswith("**画**："):
            h.append(f'<div class="blk ga">{inline(l[len("**画**："):])}</div>')
        elif l.startswith("**テロップ**："):
            h.append(f'<div class="blk te">{telop(l[len("**テロップ**："):])}</div>')
        elif l.strip() == "**ナレ**":
            i += 1
            paras, cur = [], []
            while i < len(lines) and not lines[i].startswith(("**", "#", "---")):
                if lines[i].strip() == "":
                    if cur:
                        paras.append(cur)
                        cur = []
                else:
                    cur.append(lines[i])
                i += 1
            if cur:
                paras.append(cur)
            body = ""
            for p in paras:
                if all(x.startswith("- ") for x in p):
                    body += "<ul>" + "".join(f"<li>{inline(x[2:])}</li>" for x in p) + "</ul>"
                else:
                    body += "<p style='margin:0 0 2mm'>" + "<br>".join(inline(x) for x in p) + "</p>"
            h.append(f'<div class="blk na"><span class="lb">ナレ（シン）</span>{body}</div>')
            continue
        elif l.startswith("- "):
            items = []
            while i < len(lines) and lines[i].startswith("- "):
                items.append(lines[i][2:])
                i += 1
            if in_info:
                lis = []
                for it in items:
                    m = re.match(r"\*\*([^*]+)\*\*：(.*)", it)
                    lis.append(f"<li><b>{html.escape(m.group(1))}</b>{inline(m.group(2))}</li>" if m else f"<li>{inline(it)}</li>")
                h.append('<ul class="info">' + "".join(lis) + "</ul>")
            else:
                h.append('<ul class="memo">' + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        elif l.strip() == "---":
            h.append("<hr>")
        elif l.strip():
            h.append(f"<p>{inline(l)}</p>")
        i += 1
    return "\n".join(h)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    src = os.path.abspath(sys.argv[1])
    out = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".pdf"
    md = open(src, encoding="utf-8").read()
    m = re.search(r"\*\*サムネ\*\*：`([^`]+)`", md)
    thumb = os.path.join(ROOT, m.group(1)) if m else None
    body = convert(md, thumb if thumb and os.path.exists(thumb) else None)
    doc = f"<!doctype html><html lang='ja'><head><meta charset='utf-8'><style>{CSS % {'a': ASSETS}}</style></head><body>{body}</body></html>"
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(doc)
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files",
                    "--no-pdf-header-footer", f"--print-to-pdf={out}", f"file://{f.name}"],
                   check=True, capture_output=True)
    print(out)


if __name__ == "__main__":
    main()
