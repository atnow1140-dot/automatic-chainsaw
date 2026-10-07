# 真面目の芽｜つなぎ画像ストック（Pollo.ai用・15枚）

作成日: 2026-10-07
目的: どの動画でも使い回せる「つなぎ」の絵を先に作っておき、毎回の生成枚数を減らす
選び方: これまでの台本（時間・働き方・お金・学び・感謝・選択）で何度も出てくる場面を優先

## 作り方
1. ChatGPT に下の「プロンプト作成用の指示」を送り、Pollo.ai 用の英語プロンプトを整えてもらう（下の英語プロンプトをそのまま使ってもOK）
2. Pollo.ai で生成。**縦 9:16** を基本に、長尺用に 16:9 版も作っておくと便利
3. ファイル名を `stock-01.png` 〜 `stock-15.png` に統一して `company/assets/majime-no-me/stock/` で管理
4. 画風がばらついたら、秘書にまとめて送る → セピア＋ノイズで色をそろえる
- 人物は顔を描かない（後ろ姿・手元・シルエット）→ どの話にも当てはめやすい
- 余裕があれば Pollo.ai の画像→動画で「ゆっくり動く」版も作る（湯気・光・砂が落ちる程度の小さな動き）

## ChatGPTに送る「プロンプト作成用の指示」
```
YouTubeチャンネル「真面目の芽」（大人のための静かな学び）で、どの動画でも使い回せる“つなぎ”の挿絵をPollo.aiで作ります。
次の場面を、Pollo.aiの画像生成用の英語プロンプトにしてください。

【共通の画風】flat 2D hand-drawn illustration, NOT realistic, satirical graphic novel style, clear ink outlines, flat muted colors, muted palette of sepia, umber, olive and dusty gray, warm dim light, quiet contemplative mood, subtle paper grain, no text, no logos
【人物】顔は描かない（後ろ姿・手元・シルエットのみ）
【サイズ】9:16 vertical
【場面】（ここに日本語で場面を書く）

1つの場面につき、プロンプトを1つだけ、80語以内で出してください。
```

## ストック15枚
| No | 場面 | よく使うナレーション（例） | タグ |
|---|---|---|---|
| 01 | 朝の光が差し込む窓辺 | 「ここから始まる」「ある日、気づいた」 | 始まり・転機 |
| 02 | 夜の机とランプ、閉じたノート | 「一人で考えた」「振り返ってみると」 | 内省 |
| 03 | 砂が落ちていく砂時計 | 「時間は限られている」「気づけば何年も」 | 時間 |
| 04 | 木のテーブルに積まれたコイン | 「お金の話」「収入・報酬」 | お金 |
| 05 | 開いた財布と家計簿 | 「毎月の支出」「やりくり」「貯金」 | お金・暮らし |
| 06 | 朝の通勤の雑踏（シルエット） | 「毎日の仕事」「忙しさに追われて」 | 働き方 |
| 07 | 机で頭を抱える人の後ろ姿 | 「うまくいかない日」「迷い」 | 悩み |
| 08 | 森の中の分かれ道 | 「選ぶ」「どちらを選ぶか」 | 選択 |
| 09 | 長い階段を一段ずつ登る後ろ姿 | 「積み重ね」「少しずつ」 | 努力 |
| 10 | 差し出す手と受け取る手 | 「ありがとう」「支え合い」 | 感謝 |
| 11 | ランプの下で本を開く手 | 「学ぶ」「知ることで変わる」 | 学び |
| 12 | 雨上がりの道、水たまりに映る空 | 「それでも」「もう一度」 | 立ち直り |
| 13 | 土から顔を出す小さな芽（緑は芽だけ） | 締め・「小さな芽を…」 | 成長・ブランド |
| 14 | 湯気の立つ質素な食卓 | 「日常の幸せ」「大切な人と」 | 日常・家族 |
| 15 | 夕暮れのベンチで休む人の後ろ姿 | 「止まっていい」「余白」 | 休息 |

## そのまま使える英語プロンプト
共通の書き出し: `Flat 2D hand-drawn illustration, NOT realistic, satirical graphic novel style, clear ink outlines, flat muted sepia, umber, olive and dusty gray palette, subtle paper grain, 9:16 vertical, no text, no logos.`（以下、各場面の後ろにこの一文を付ける）

- **01** `Morning sunlight pouring through an old window into a quiet room, dust floating in the light beam, a cup on the windowsill, hopeful beginning.`
- **02** `A wooden desk at night under a single warm lamp, a closed notebook and a pen, the rest of the room in deep shadow, quiet reflection.`
- **03** `A large old hourglass on a table, golden sand steadily falling, soft side light, the feeling of time passing.`
- **04** `A small neat stack of old gold coins on a worn wooden table in warm lamplight, calm and honest mood.`
- **05** `An open leather wallet beside a household account book and a pencil on a kitchen table at night, a few coins and receipts, modest everyday life.`
- **06** `A crowded morning commute, many people seen from behind as hurried silhouettes walking toward a train station, long shadows, busy but quiet tone.`
- **07** `A person seen from behind sitting at an office desk at night, head in hands, papers piled up, a single desk lamp glowing.`
- **08** `A quiet forest path splitting into two directions, soft light falling on both paths, no people, a moment of choice.`
- **09** `A person seen from behind slowly climbing a long stone staircase toward soft light at the top, one step at a time.`
- **10** `One pair of hands gently offering a small object to another pair of hands, warm light between them, kindness and gratitude. No faces.`
- **11** `Hands opening an old book under a warm desk lamp, pages glowing softly, a quiet moment of learning.`
- **12** `A wet street just after the rain, a puddle reflecting a clearing sky with soft light breaking through the clouds, quiet hope.`
- **13** `A single small green sprout breaking through dark soil in soft morning light, the green sprout is the only vivid color.`
- **14** `A simple home-cooked meal on a small wooden table with steam rising from bowls, two chairs, warm evening light, ordinary happiness.`
- **15** `A person seen from behind resting on a park bench at dusk, shoulders relaxed, long shadows on the path, peaceful pause.`
