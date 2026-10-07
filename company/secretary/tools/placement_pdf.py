"""真面目の芽：画像配置表（A4・1枚PDF）を作る。全動画共通の最終フォーマット。

使い方:
    python3 company/secretary/tools/placement_pdf.py company/secretary/ideas/specs/<動画>-placement.json

spec(JSON)の rows は [台本の区切り, 画像, 種類("GPT"|"ADD"|"REUSE"), 見せ方, {"y": [黄色の語], "r": [赤の語]}]
字幕の色ルールは company/secretary/ideas/majime-no-me-style-guide.md
"""
import json
import os
import sys
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
pdfmetrics.registerFont(TTFont("JP", "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"))

INK, MUTED, ACC = colors.HexColor("#2b2620"), colors.HexColor("#6b6258"), colors.HexColor("#5a7a4a")
ADD_BG, HEAD_BG, GRID = colors.HexColor("#e6efdc"), colors.HexColor("#efe9df"), colors.HexColor("#d8d0c4")
YELLOW, RED = "#F5C828", "#BE1E1E"


def style(name, **kw):
    return ParagraphStyle(name, **{"fontName": "JP", "textColor": INK, **kw})


H1 = style("h1", fontSize=14, leading=19)
SUB = style("sub", fontSize=7.8, leading=11, textColor=MUTED, spaceAfter=4)
H2 = style("h2", fontSize=9.5, leading=13, textColor=ACC, spaceBefore=5, spaceAfter=2)
C = style("c", fontSize=7.3, leading=9.6)
CB = style("cb", fontSize=7.5, leading=10)


def yellow(word):
    return f'<font backColor="{YELLOW}"> {escape(word)} </font>'


def red(word):
    return f'<font color="{RED}"><b>{escape(word)}</b></font>'


def subtitle_cell(colors_):
    parts = [red(w) for w in colors_.get("r", [])] + [yellow(w) for w in colors_.get("y", [])]
    return "　".join(parts) if parts else '<font color="#9a9087">（白のみ）</font>'


def build(spec_path):
    spec = json.load(open(spec_path, encoding="utf-8"))
    out = os.path.join(ROOT, spec["output"])

    hdr = ["順", "台本（この文から切り替える）", "画像", "種類", "見せ方", "字幕の色"]
    data = [[Paragraph(h, CB) for h in hdr]]
    ts = [("BACKGROUND", (0, 0), (-1, 0), HEAD_BG), ("GRID", (0, 0), (-1, -1), 0.3, GRID),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (0, -1), "CENTER"),
          ("ALIGN", (2, 0), (3, -1), "CENTER"),
          ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.2),
          ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3)]
    red_count = 0
    for i, (text, img, kind, how, cols) in enumerate(spec["rows"], 1):
        red_count += len(cols.get("r", []))
        is_add = kind in ("ADD", "REUSE")
        img_label = f'<font color="#3f6b2a">{escape(img)}.png</font>' if is_add else f"{escape(img)}.png"
        kind_label = {"ADD": '<font color="#3f6b2a">追加生成</font>',
                      "REUSE": '<font color="#3f6b2a">使い回し</font>'}.get(kind, "ChatGPT")
        data.append([Paragraph(str(i), C), Paragraph(escape(text), C), Paragraph(img_label, C),
                     Paragraph(kind_label, C), Paragraph(escape(how), C), Paragraph(subtitle_cell(cols), C)])
        if is_add:
            ts.append(("BACKGROUND", (0, i), (-1, i), ADD_BG))
    if red_count > 3:
        print(f"注意: 赤の字幕が{red_count}回あります（ルールは1本につき2〜3回まで）")

    table = Table(data, colWidths=[6 * mm, 60 * mm, 13 * mm, 13 * mm, 47 * mm, 43 * mm], repeatRows=1)
    table.setStyle(TableStyle(ts))

    story = [Paragraph(escape(spec["title"]), H1), Paragraph(escape(spec["subtitle"]), SUB), table]
    if spec.get("extra"):
        story.append(Paragraph(escape(spec.get("extra_title", "追加で生成する画像")), H2))
        et = Table([[Paragraph(escape(a), C), Paragraph(escape(b), C)] for a, b in spec["extra"]],
                   colWidths=[13 * mm, 169 * mm])
        et.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), ADD_BG), ("GRID", (0, 0), (-1, -1), 0.3, GRID),
                                ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]))
        story.append(et)
    story.append(Paragraph("メモ", H2))
    story += [Paragraph("・" + escape(n), C) for n in spec.get("notes", [])]

    SimpleDocTemplate(out, pagesize=A4, leftMargin=14 * mm, rightMargin=14 * mm, topMargin=12 * mm,
                      bottomMargin=10 * mm, title=spec["title"]).build(story)
    print(out)


if __name__ == "__main__":
    build(sys.argv[1])
