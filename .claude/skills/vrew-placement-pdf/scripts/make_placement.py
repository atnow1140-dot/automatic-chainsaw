#!/usr/bin/env python3
"""Vrew 挿絵の配置リストPDFを作る。

使い方:
  python3 make_placement.py placement.csv --narration narration.txt \
      --title "真面目の芽｜第◯話 Vrew 挿絵の配置リスト" --out epXX_vrew-placement.pdf

placement.csv の列（1行目は見出し）:
  image   : 01.png など。文字だけの画面は「文字」
  line    : 切り替える文（ナレーション原稿の文の書き出しをそのままコピー）
  content : 絵の内容
  memo    : メモ（空でOK）
  time    : 目安（空なら、ナレーション原稿から 1分300字 で自動計算）
  thumb   : 差し替え・追加画像のパス（CSVからの相対パス。あれば小さく画像を表示）
  kind    : 空=通常／差替=後から差し替えた画像／重ね=上に重ねる画像（透過PNG）
"""
import argparse
import csv
import html
import os
import re
import subprocess
import sys

CHARS_PER_MIN = 300
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RULES = [
    "Vrewはナレーションが文ごとにクリップに分かれる。表の「切り替える文」のクリップに画像を置き、次の画像の手前まで伸ばす",
    "画像ファイル名は、ChatGPTで作ったときの番号（01.png〜）",
    "「文字」画面（引用文）は画像で用意してある（quote_XXXX.png）。普通の挿絵と同じように置く",
    "赤の【差替】＝後から差し替えた画像。古いファイルは _old をつけてよけてから置く",
    "緑の【重ね】＝上に重ねる透過PNG。Vrewで「重ねる画像」として入れ、全画面に広げる（位置合わせ不要）",
    "切り替えはディゾルブ（ふわっと切り替え）、静止画にはゆっくりズームイン／パンを付ける",
    "シンのアイコンは動画の最初〜ENDの直前まで表示。エンドカードからは外す",
]


def squash(s):
    return re.sub(r"\s", "", s)


def estimate(narration, line):
    body = squash(narration)
    key = squash(line)
    for n in (len(key), 20, 12, 8):
        pos = body.find(key[:n])
        if pos >= 0:
            sec = round(pos * 60 / CHARS_PER_MIN)
            return f"{sec // 60}:{sec % 60:02d}"
    print(f"警告: ナレーションに見つからない文 → {line}", file=sys.stderr)
    return "?"


def build_html(title, sub, rules, rows):
    e = html.escape
    trs = []
    for r in rows:
        kind = (r.get("kind") or "").strip()
        cls = {"差替": "sasi", "重ね": "kasa"}.get(kind, "moji" if r["image"].strip() == "文字" else "")
        badge = f"<span class='b {cls}'>{e(kind)}</span>" if kind else ""
        thumb = r.get("thumb") or ""
        img = f"<img src='{e(thumb)}'>" if thumb else ""
        trs.append(
            f"<tr class='{cls}'><td class='m'>{e(r['image'])}{badge}</td><td class='m'>{e(r['time'])}</td>"
            f"<td>{e(r['line'])}</td><td>{img}{e(r['content'])}</td><td>{e(r.get('memo') or '')}</td></tr>"
        )
    lis = "".join(f"<li>{e(x)}</li>" for x in rules)
    css = open(os.path.join(HERE, "..", "assets", "style.css"), encoding="utf-8").read()
    return f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>{e(title)}</title>
<style>{css}</style></head><body>
<h1>{e(title)}</h1><div class="sub">{e(sub)}</div>
<h2>置き方</h2><ul>{lis}</ul>
<h2>配置リスト</h2>
<table><thead><tr><th style="width:9%">画像</th><th style="width:6%">目安</th>
<th style="width:37%">切り替える文（このクリップから）</th><th style="width:39%">絵の内容</th><th style="width:9%">メモ</th></tr></thead>
<tbody>{''.join(trs)}</tbody></table></body></html>"""


def to_pdf(html_path, pdf_path):
    chrome = os.environ.get("CHROME", "/opt/pw-browsers/chromium")
    subprocess.run(
        [chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", "file://" + os.path.abspath(html_path)],
        check=True, stderr=subprocess.DEVNULL,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--narration", help="ナレーション原稿（目安時間の自動計算用）")
    ap.add_argument("--title", default="真面目の芽｜Vrew 挿絵の配置リスト")
    ap.add_argument("--rule", action="append", help="置き方に足す行（何度でも）")
    ap.add_argument("--out", required=True, help="出力PDF")
    a = ap.parse_args()

    with open(a.csv, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    narration = open(a.narration, encoding="utf-8").read() if a.narration else ""
    for r in rows:
        if not (r.get("time") or "").strip():
            r["time"] = estimate(narration, r["line"]) if narration else ""

    src = os.path.basename(a.narration) if a.narration else "（ナレーション原稿）"
    sub = f"ナレーション原稿：{src}／時間はナレーション1分{CHARS_PER_MIN}字で読んだ場合の目安"
    html_path = os.path.splitext(a.out)[0] + ".html"
    # 画像の相対パスをCSV基準にするため、HTMLはCSVと同じフォルダに書く
    html_path = os.path.join(os.path.dirname(os.path.abspath(a.csv)), os.path.basename(html_path))
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(build_html(a.title, sub, DEFAULT_RULES + (a.rule or []), rows))
    to_pdf(html_path, os.path.abspath(a.out))
    print(a.out)


if __name__ == "__main__":
    main()
