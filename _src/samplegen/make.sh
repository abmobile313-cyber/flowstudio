#!/usr/bin/env bash
# usage: _src/samplegen/make.sh data.json   (run from the repo root)
# builds one 5 s 1080x720 UI film + poster per item, adds the Flow Studio watermark, copies into samples/
set -e
D=$(cd "$(dirname "$0")" && pwd); W=$(mktemp -d)
python3 "$D/engine.py" "$1" "$W/html"
(cd /tmp && node "$D/render.js" "$W/html" "$W/vid" 25 5)
mkdir -p "$W/out"
for f in "$W"/vid/*.raw.mp4; do id=$(basename "$f" .raw.mp4)
  ffmpeg -nostdin -v error -y -i "$f" -i "$D/wm.png" -filter_complex "[1]scale=1080:720[w];[0][w]overlay=0:0,format=yuv420p" -c:v libx264 -preset veryfast -crf 23 -movflags +faststart -an "$W/out/$id.mp4"
  ffmpeg -nostdin -v error -y -ss 4.6 -i "$W/out/$id.mp4" -frames:v 1 -q:v 3 "$W/out/$id.jpg"
done
cp "$W"/out/* samples/; echo "made $(ls "$W"/out/*.mp4 | wc -l) samples (posters in samples/)"
