"""47都市ぶんのフリー素材（写真・動画）を Pexels / Pixabay から集めて保存する。

使い方:
    export PEXELS_API_KEY=...     # https://www.pexels.com/api/ で無料取得
    export PIXABAY_API_KEY=...    # https://pixabay.com/api/docs/ で無料取得（どちらか片方でも可）
    python3 tools/fetch_media.py                 # 47都市すべて
    python3 tools/fetch_media.py --only 13,26    # 東京と京都だけ
    python3 tools/fetch_media.py --photos 6 --videos 3

保存先: media/<no>_<prefecture>_<city>/photos, videos
クレジット: media/<...>/credits.csv（出典・作者・元URL・ライセンス）
既にあるファイルはスキップするので、何度実行しても大丈夫。
"""
import argparse
import csv
import json
import os
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CITIES = os.path.join(ROOT, "cities.csv")
MEDIA = os.path.join(ROOT, "media")
UA = {"User-Agent": "japan-cities-shorts/1.0"}


def get_json(url, headers=None):
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def download(url, path):
    if os.path.exists(path):
        return False
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r, open(path + ".part", "wb") as f:
        while chunk := r.read(1 << 16):
            f.write(chunk)
    os.replace(path + ".part", path)
    return True


def pexels_photos(q, n, key):
    url = "https://api.pexels.com/v1/search?" + urllib.parse.urlencode(
        {"query": q, "per_page": n, "orientation": "portrait"})
    for p in get_json(url, {"Authorization": key}).get("photos", []):
        yield {"source": "pexels", "id": p["id"], "author": p["photographer"],
               "page": p["url"], "file": p["src"]["large2x"], "ext": "jpg",
               "license": "Pexels License (free, no attribution required)"}


def pexels_videos(q, n, key):
    url = "https://api.pexels.com/videos/search?" + urllib.parse.urlencode(
        {"query": q, "per_page": n, "orientation": "portrait"})
    for v in get_json(url, {"Authorization": key}).get("videos", []):
        files = [f for f in v["video_files"] if f.get("height") and f["height"] <= 1920]
        if not files:
            continue
        best = max(files, key=lambda f: f["height"])
        yield {"source": "pexels", "id": v["id"], "author": v["user"]["name"],
               "page": v["url"], "file": best["link"], "ext": "mp4",
               "license": "Pexels License (free, no attribution required)"}


def pixabay_photos(q, n, key):
    url = "https://pixabay.com/api/?" + urllib.parse.urlencode(
        {"key": key, "q": q, "image_type": "photo", "orientation": "vertical",
         "per_page": max(3, n), "safesearch": "true"})
    for h in get_json(url).get("hits", [])[:n]:
        yield {"source": "pixabay", "id": h["id"], "author": h["user"],
               "page": h["pageURL"], "file": h["largeImageURL"], "ext": "jpg",
               "license": "Pixabay Content License (free, no attribution required)"}


def pixabay_videos(q, n, key):
    url = "https://pixabay.com/api/videos/?" + urllib.parse.urlencode(
        {"key": key, "q": q, "per_page": max(3, n), "safesearch": "true"})
    for h in get_json(url).get("hits", [])[:n]:
        vids = h["videos"]
        best = vids.get("large") or vids.get("medium")
        if not best or not best.get("url"):
            continue
        yield {"source": "pixabay", "id": h["id"], "author": h["user"],
               "page": h["pageURL"], "file": best["url"], "ext": "mp4",
               "license": "Pixabay Content License (free, no attribution required)"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="都市番号をカンマ区切りで（例: 13,26）")
    ap.add_argument("--photos", type=int, default=3, help="キーワード1つあたりの写真枚数")
    ap.add_argument("--videos", type=int, default=2, help="キーワード1つあたりの動画本数")
    args = ap.parse_args()

    pexels, pixabay = os.environ.get("PEXELS_API_KEY"), os.environ.get("PIXABAY_API_KEY")
    if not (pexels or pixabay):
        sys.exit("PEXELS_API_KEY か PIXABAY_API_KEY を設定してください")
    only = set(args.only.split(",")) if args.only else None

    with open(CITIES, encoding="utf-8") as f:
        cities = list(csv.DictReader(f))

    for c in cities:
        if only and c["no"] not in only:
            continue
        folder = os.path.join(MEDIA, f'{c["no"]}_{c["prefecture_en"]}_{c["city_en"]}'.replace(" ", ""))
        os.makedirs(os.path.join(folder, "photos"), exist_ok=True)
        os.makedirs(os.path.join(folder, "videos"), exist_ok=True)
        credits_path = os.path.join(folder, "credits.csv")
        seen = set()
        if os.path.exists(credits_path):
            with open(credits_path, encoding="utf-8") as f:
                seen = {(r["source"], r["id"]) for r in csv.DictReader(f)}
        new_rows = []
        print(f'■ {c["no"]} {c["prefecture_ja"]}／{c["city_ja"]}')

        for kw in c["keywords"].split(";"):
            q = f"{kw} Japan" if "Japan" not in kw else kw
            fetchers = []
            if pexels:
                fetchers += [(pexels_photos, args.photos, pexels, "photos"),
                             (pexels_videos, args.videos, pexels, "videos")]
            if pixabay:
                fetchers += [(pixabay_photos, args.photos, pixabay, "photos"),
                             (pixabay_videos, args.videos, pixabay, "videos")]
            for fn, n, key, sub in fetchers:
                if n <= 0:
                    continue
                try:
                    items = list(fn(q, n, key))
                except Exception as e:
                    print(f"  ! {fn.__name__} '{q}': {e}")
                    continue
                for it in items:
                    if (it["source"], str(it["id"])) in seen:
                        continue
                    name = f'{it["source"]}_{it["id"]}.{it["ext"]}'
                    try:
                        download(it["file"], os.path.join(folder, sub, name))
                    except Exception as e:
                        print(f"  ! download {name}: {e}")
                        continue
                    seen.add((it["source"], str(it["id"])))
                    new_rows.append({"file": f"{sub}/{name}", "keyword": q, **{k: it[k] for k in
                                     ("source", "id", "author", "page", "license")}})
                    print(f"  + {sub}/{name}")
                time.sleep(0.5)

        if new_rows:
            write_header = not os.path.exists(credits_path)
            with open(credits_path, "a", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["file", "keyword", "source", "id", "author", "page", "license"])
                if write_header:
                    w.writeheader()
                w.writerows(new_rows)


if __name__ == "__main__":
    main()
