"""左下のシンのアイコン（動画中ずっと出す）生成

使い方:
  python3 make_icon.py 出力.png

出力は透過PNG（1920x1080）。左下にシンの顔の丸アイコン（水色の発光フチ）。
全画面サイズなので、動画編集ソフトで位置合わせせずにそのまま重ねるだけでOK。
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw

D = os.path.dirname(os.path.abspath(__file__))
W, H = 1920, 1080
CYAN = (60, 220, 255)
SIZE = 200  # アイコンの直径
MARGIN = 44


def make():
    shin = Image.open(os.path.join(D, "assets", "shin.webp")).convert("RGBA")
    # 顔まわりを正方形で切り出す
    cx, cy, r = 590, 470, 390
    face = shin.crop((cx - r, cy - r, cx + r, cy + r))
    bg = Image.new("RGBA", face.size, (245, 240, 230, 255))
    bg.alpha_composite(face)
    face = bg.resize((SIZE, SIZE), Image.LANCZOS)
    mask = Image.new("L", (SIZE * 4, SIZE * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, SIZE * 4 - 1, SIZE * 4 - 1), fill=255)
    mask = mask.resize((SIZE, SIZE), Image.LANCZOS)
    face.putalpha(mask)

    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    x, y = MARGIN, H - MARGIN - SIZE
    # 水色の発光フチ
    ring = np.zeros((H, W), np.float32)
    c = (x + SIZE // 2, y + SIZE // 2)
    cv2.circle(ring, c, SIZE // 2 + 3, 255, 6, cv2.LINE_AA)
    glow = cv2.GaussianBlur(ring, (0, 0), 10) * 1.6 + ring
    g = Image.new("RGBA", (W, H), CYAN + (255,))
    g.putalpha(Image.fromarray(np.clip(glow, 0, 255).astype(np.uint8)))
    im.alpha_composite(g)
    im.alpha_composite(face, (x, y))
    return im


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    make().save(sys.argv[1])


if __name__ == "__main__":
    main()
