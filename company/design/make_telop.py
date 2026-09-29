"""冒頭テロップ（チャンネルのテーマ）生成（ルールは thumbnail-rules.md）

使い方:
  python3 make_telop.py 出力.png [プレビュー用の背景画像]

出力は透過PNG（1920x1080）。動画編集ソフトで冒頭の映像に重ねる。
背景画像を渡すと、重ねた見本（出力名_preview.png）も作る。
"""
import os
import sys

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

D = os.path.dirname(os.path.abspath(__file__))
FB = os.path.join(D, "assets", "NotoSansCJKjp-Bold.otf")
W, H = 1920, 1080
WHITE = (255, 255, 255)
YELLOW = (255, 212, 0)
GLOW = (255, 205, 40)

# テーマ（「気づきの芽」を黄色で強調）
PARTS = [("あなたの人生に、小さな", WHITE), ("気づきの芽", YELLOW), ("を。", WHITE)]


def sprout_icon(h):
    """芽の鉢から葉っぱ部分だけ切り出して、黄色の発光を付ける"""
    pl = Image.open(os.path.join(D, "assets", "me_plant.png"))
    pl = pl.crop(pl.getbbox())
    leaf = pl.crop((0, 0, pl.width, int(pl.height * 0.44)))  # 葉っぱと茎だけ
    arr = np.array(leaf)
    y0 = int(arr.shape[0] * 0.7)  # 下のほうは緑っぽいところ（茎）だけ残して土を消す
    low = arr[y0:]
    low[..., 3] = np.where(low[..., 1] > low[..., 0], low[..., 3], 0)
    leaf = Image.fromarray(arr)
    leaf = leaf.crop(leaf.getbbox())
    leaf = leaf.resize((round(leaf.width * h / leaf.height), h), Image.LANCZOS)
    p = 40
    big = Image.new("RGBA", (leaf.width + 2 * p, leaf.height + 2 * p), (0, 0, 0, 0))
    big.paste(leaf, (p, p), leaf)
    a = (np.array(big.split()[3]) > 128).astype(np.float32) * 255
    ell = lambda n: cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (n, n))
    g = cv2.GaussianBlur(cv2.dilate(a, ell(9)), (0, 0), 12) * 1.3
    out = Image.new("RGBA", big.size, GLOW + (255,))
    out.putalpha(Image.fromarray(np.clip(g, 0, 255).astype(np.uint8)))
    out.alpha_composite(big)
    return out


def make():
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # 読みやすさ用の帯（上下がふわっと消える黒）
    yy = np.arange(H, dtype=np.float32)
    band = np.exp(-(((yy - 600) / 150) ** 2)) * 185
    alpha = np.repeat(band[:, None], W, axis=1).astype(np.uint8)
    b = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    b.putalpha(Image.fromarray(alpha))
    im.alpha_composite(b)

    icon = sprout_icon(150)
    im.alpha_composite(icon, ((W - icon.width) // 2, 545 - icon.height + 40))

    f = ImageFont.truetype(FB, 64)
    d = ImageDraw.Draw(im)
    w = sum(d.textlength(t, font=f) for t, _ in PARTS)
    x, y = (W - w) / 2, 560
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sx = x
    for t, _ in PARTS:
        sd.text((sx + 3, y + 4), t, font=f, fill=(0, 0, 0, 200))
        sx += d.textlength(t, font=f)
    im.alpha_composite(sh.filter(ImageFilter.GaussianBlur(4)))
    d = ImageDraw.Draw(im)
    for t, c in PARTS:
        d.text((x, y), t, font=f, fill=c)
        x += d.textlength(t, font=f)
    # 下の細い線
    d.line(((W - w) / 2 + 40, y + 100, (W + w) / 2 - 40, y + 100), fill=(255, 230, 150, 200), width=2)
    return im


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    im = make()
    im.save(out)
    if len(sys.argv) > 2:
        bg = Image.open(sys.argv[2]).convert("RGBA").resize((W, H), Image.LANCZOS)
        bg.alpha_composite(im)
        bg.convert("RGB").save(os.path.splitext(out)[0] + "_preview.png")


if __name__ == "__main__":
    main()
