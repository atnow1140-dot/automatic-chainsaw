#!/usr/bin/env bash
# 作業工程HTMLをA4のPDFにする
# 使い方: render.sh <input.html> [output.pdf]
# 画像はHTMLからの相対パスで読むので、HTMLは素材と同じフォルダに置くこと
set -euo pipefail
in="$(realpath "$1")"
out="$(realpath -m "${2:-${in%.html}.pdf}")"
chrome="${CHROME:-/opt/pw-browsers/chromium}"
[ -x "$chrome" ] || chrome="$(command -v chromium || command -v google-chrome)"
"$chrome" --headless --no-sandbox --disable-gpu --allow-file-access-from-files \
  --no-pdf-header-footer --print-to-pdf="$out" "file://$in" 2>/dev/null
echo "$out"
