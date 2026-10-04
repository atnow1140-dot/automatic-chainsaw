# 文字起こしツール

録音・動画ファイルを日本語で文字起こしする。Whisper small をローカルで動かすので、外部APIは使わない。

## 準備（セッションごとに1回・1〜2分）
```
cd tools/transcribe && npm install
```
- 必要なもの: Node.js、ffmpeg
- モデルは npm パッケージ `sts-whisper-small` から入る（Hugging Face が使えない環境でも動く）

## 使い方
```
node tools/transcribe/transcribe.mjs <ファイル> [-o 出力.txt]
```
- 対応: m4a / mp3 / wav / mp4 など ffmpeg で読めるもの
- 出力は `[開始秒-終了秒] テキスト` の形式

## 注意
- 人名・作品名などの固有名詞はよく間違える（例: キアヌ → キアの）。台本にする前に文脈で直す
- YouTubeのURLは直接読めない。画面録画や録音ファイルにしてから使う
