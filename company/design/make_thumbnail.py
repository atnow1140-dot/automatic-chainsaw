"""サムネ生成スクリプト（ルールは thumbnail-rules.md）

使い方:
  python3 make_thumbnail.py 背景.png 出力.png "{y:人生}は、" "短く{r:ない}。" "2000年前の哲学者の答え"

  {y:...} → 黄色 / {r:...} → 赤 / それ以外 → 白
  3つ目（サブタイトル）は省略可。

必要: pip install pillow numpy opencv-python-headless
フォント（Noto Sans CJK JP Black）は初回に自動ダウンロード。
"""
import os
import re
import sys
import urllib.request

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "assets", "NotoSansCJKjp-Black.otf")
FONT_URL = "https://raw.githubusercontent.com/notofonts/noto-cjk/main/Sans/OTF/Japanese/NotoSansCJKjp-Black.otf"
SHIN = os.path.join(HERE, "assets", "shin.webp")

# 固定カラー（変えない）
WHITE = (255, 255, 255)
RED = (235, 35, 35)
YELLOW = (255, 212, 0)
BAND = (12, 12, 12)
SHIN_GLOW = (60, 220, 255)
COLORS = {"y": YELLOW, "r": RED}

W, H = 1280, 720


def parse(text):
    """'{y:人生}は、' → [('人生', YELLOW), ('は、', WHITE)]"""
    parts = []
    for m in re.finditer(r"\{([yr]):([^}]*)\}|([^{]+)", text):
        if m.group(3):
            parts.append((m.group(3), WHITE))
        else:
            parts.append((m.group(2), COLORS[m.group(1)]))
    return parts


def band(d, parts, font, box, padl):
    d.rectangle(box, fill=BAND)
    x0, t, _, b = box
    g = font.getbbox("短")
    y = t + ((b - t) - (g[3] - g[1])) / 2 - g[1]
    x = x0 + padl
    for s, c in parts:
        d.text((x, y), s, font=font, fill=c)
        x += d.textlength(s, font=font)


def shin_glow(h):
    ch = Image.open(SHIN).convert("RGBA")
    ch = ch.crop(ch.getbbox())
    ch = ch.resize((round(ch.width * h / ch.height), h), Image.LANCZOS)
    pad = 50
    big = Image.new("RGBA", (ch.width + pad * 2, ch.height + pad * 2), (0, 0, 0, 0))
    big.paste(ch, (pad, pad), ch)
    a = (np.array(big.split()[3]) > 128).astype(np.float32) * 255
    ell = lambda n: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (n, n))
    inner = cv2.GaussianBlur(cv2.dilate(a, ell(7)), (0, 0), 3)
    outer = cv2.GaussianBlur(cv2.dilate(a, ell(15)), (0, 0), 14)
    glow = np.clip(inner + outer * 1.3, 0, 255).astype(np.uint8)
    out = Image.new("RGBA", big.size, SHIN_GLOW + (255,))
    out.putalpha(Image.fromarray(glow))
    out.alpha_composite(big)
    return out, pad


def main():
    if len(sys.argv) < 5:
        sys.exit(__doc__)
    bg, dst, l1, l2 = sys.argv[1:5]
    sub = sys.argv[5] if len(sys.argv) > 5 else None
    if not os.path.exists(FONT):
        urllib.request.urlretrieve(FONT_URL, FONT)

    im = Image.open(bg).convert("RGBA").resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    f1 = ImageFont.truetype(FONT, 104)
    f2 = ImageFont.truetype(FONT, 112)
    f3 = ImageFont.truetype(FONT, 32)
    band(d, parse(l1), f1, (640, 30, W, 160), 34)
    band(d, parse(l2), f2, (620, 168, W, 306), 30)
    if sub:
        w = d.textlength(sub, font=f3)
        band(d, parse(sub), f3, (640, 314, round(640 + w + 50), 370), 22)

    s, p = shin_glow(400)
    im.alpha_composite(s, (W - s.width + p, H - s.height + p + 4))
    im.convert("RGB").save(dst)


if __name__ == "__main__":
    main()
