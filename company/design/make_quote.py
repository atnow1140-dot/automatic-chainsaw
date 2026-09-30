"""「文字」画面（引用を1枚で見せる画面）生成（ルールは thumbnail-rules.md）

使い方:
  python3 make_quote.py 出力.png "1行目" ["2行目" ...] [--by "出典"]

例:
  python3 make_quote.py quote.png "{y:人生}は短いのではない。" "その多くを{r:浪費}しているのだ。" --by "セネカ『人生の短さについて』"

`{y:...}` で黄、`{r:...}` で赤、それ以外は白。強調は1行に1か所まで。
出力は1920x1080のPNG（黒背景・全画面）。Vrewで挿絵と同じように置く。
"""
import os
import re
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
FB = os.path.join(D, "assets", "NotoSansCJKjp-Bold.otf")
W, H = 1920, 1080
BG = (12, 12, 12)
WHITE = (255, 255, 255)
YELLOW = (255, 212, 0)
RED = (235, 35, 35)
GRAY = (170, 170, 170)
COLORS = {"y": YELLOW, "r": RED}


def parse(line):
    """「{y:人生}は」→ [("人生", 黄), ("は", 白)]"""
    parts, pos = [], 0
    for m in re.finditer(r"\{([yr]):(.+?)\}", line):
        if m.start() > pos:
            parts.append((line[pos:m.start()], WHITE))
        parts.append((m.group(2), COLORS[m.group(1)]))
        pos = m.end()
    if pos < len(line):
        parts.append((line[pos:], WHITE))
    return parts


def background():
    # 真ん中がほんの少し明るい黒（周辺減光）
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    lift = np.clip(1 - r, 0, 1) * 18
    arr = np.clip(np.array(BG, np.float32)[None, None, :] + lift[..., None], 0, 255)
    return Image.fromarray(arr.astype(np.uint8)).convert("RGBA")


def make(lines, by=None):
    im = background()
    f = ImageFont.truetype(FB, 80)
    fs = ImageFont.truetype(FB, 40)
    d = ImageDraw.Draw(im)
    lh = 130
    block = lh * len(lines) + (110 if by else 0)
    y = (H - block) / 2

    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    rows = []
    for line in lines:
        parts = parse(line)
        w = sum(d.textlength(t, font=f) for t, _ in parts)
        rows.append((parts, (W - w) / 2, y))
        x = (W - w) / 2
        for t, _ in parts:
            sd.text((x + 3, y + 4), t, font=f, fill=(0, 0, 0, 220))
            x += d.textlength(t, font=f)
        y += lh
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(4)))
    d = ImageDraw.Draw(im)
    for parts, x, ry in rows:
        for t, c in parts:
            d.text((x, ry), t, font=f, fill=c)
            x += d.textlength(t, font=f)

    if by:
        t = "― " + by
        w = d.textlength(t, font=fs)
        y += 40
        d.text(((W - w) / 2, y), t, font=fs, fill=GRAY)
    return im.convert("RGB")


def main():
    args = sys.argv[1:]
    by = None
    if "--by" in args:
        i = args.index("--by")
        by = args[i + 1]
        args = args[:i] + args[i + 2:]
    if len(args) < 2:
        sys.exit(__doc__)
    make(args[1:], by).save(args[0])


if __name__ == "__main__":
    main()
