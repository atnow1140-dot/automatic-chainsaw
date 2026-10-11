# 人物シリーズ 第4話｜大谷翔平　画像プロンプト（13枚・縦9:16）

作成日: 2026-10-11
使い方: Vrewで音声から動画を作ったあと、下の表の「切り替える文」のクリップに画像を差し替える
画像はChatGPTで作る（人物シリーズのルール）。そのまま貼れる版: `chatgpt-prompts.txt`
画風: 第3話・第7話と同じ「鉛筆スケッチ（太い線と細い線のミックス）＋色鉛筆の薄塗り・白い紙を多く残す」

## 守ること（実在の人物・球団の扱い）
- **本人の顔は描かない**。背の高い高校生・無地の白い練習着という「記号」と、後ろ姿・手元・シルエットで表す
- **球団・高校のロゴ、校名、背番号、MLBのユニフォームは描かない**（商標）。メジャーの場面も無地のグレーのユニフォーム
- 目標のシート（マンダラチャート）は「9×9のマス目＋読めない走り書き」にする。文字は画像に入れない（テロップはVrewで乗せる）
- No.11・12の会社員は第3話・第7話と同じ人物
- 各プロンプトの頭に「NEW SCENE」を付けた（第3話でNo.7とNo.8が同じ絵になった対策）

---

## 最初に送る文（新しいチャットで1回）
お手本画像として、第3話（本田宗一郎と藤澤武夫）でできた画像を1枚添付して送る。
```
これから、YouTubeショート用に、同じ画風で縦長（9:16）の挿絵を13枚作ります。添付した画像の絵柄（鉛筆の太い線と細い線のミックス・色鉛筆の薄塗り・白い紙を多く残す）にそろえてください。以下のルールを、このチャットのすべての画像に適用してください。

【画風】
bold expressive pencil sketch illustration on white textured drawing paper, very sharp and crisp, dynamic line weight: strong thick dark graphite contour lines on the main subject mixed with very thin delicate pencil lines for details, confident decisive strokes, fine hatching only in the deepest shadows, light and sparse colored pencil wash with lots of white paper showing through, pale muted sepia, olive and dusty blue-gray tints with a small warm amber accent, high contrast, graphic and striking, NOT realistic, NOT photographic, no text, 9:16 vertical

【入れないもの】
photorealistic, photograph, 3d render, soft blur, heavy coloring, watercolor bleed, smudged charcoal, airbrush, glossy digital painting, flat vector art, motion blur, depth of field, bokeh, text, letters, logos, brand names, team logos, uniform numbers, school names, advertisements, bright saturated colors, anime, cute chibi

【舞台】
No.1〜9は2010年ごろの日本の地方の高校（野球のグラウンド・寮）、No.10はアメリカの大きな野球場、No.11〜13は現代の日本のオフィス・街・机です。毎回ちがう場面なので、前の画像の構図をくり返さないでください。

【人物】
実在の人物の顔は描かないでください。主人公は「背の高い、短い黒髪の高校生（無地の白い練習着）」として、後ろ姿・手元・シルエットだけで表現してください。チームのロゴ・校名・背番号・球団名・広告は描かないでください。

理解したら「OK」とだけ返してください。
```

---

## 一覧（どの文から切り替えるか）
| No | 切り替える文（台本） | 場面 | 役割 |
|---|---|---|---|
| 1 | 高校1年の大谷翔平が | 夕方のグラウンドで、背の高い高校生がゴミを拾う後ろ姿。お尻のポケットからマス目の紙がのぞく | **冒頭フック・サムネ候補** |
| 2 | 岩手の 花巻東高校 | 雪の残る山を背にした、地方の高校の野球グラウンド | 舞台 |
| 3 | 1年生の彼は | 寮の机で、マス目の紙に向かって書く高校生の後ろ姿 | 目標を書く |
| 4 | 真ん中のマスには | 9×9のマス目の紙のアップ。真ん中のマスだけ金色に光る | 夢 |
| 5 | そのまわりに | 夕暮れのマウンドで投げる高校生のシルエット | 努力 |
| 6 | そして | マス目の紙のアップ。ひとつのマスだけ空白で、鉛筆がその上で止まっている | 運のマス |
| 7 | あいさつ | グラウンドの入口で、帽子を取って深く礼をする高校生の後ろ姿 | あいさつ |
| 8 | 部屋そうじ | 寮の部屋をほうきで掃除する高校生の後ろ姿 | 部屋そうじ |
| 9 | ゴミ拾いは 運拾い | 土のグラウンドで、紙くずを拾い上げる手のアップ | 運拾い |
| 10 | メジャーリーガーになった 今も | 巨大なスタジアムの芝の上で、何かを拾う選手の小さな後ろ姿 | 今も |
| 11 | 夢が 大きすぎて | 夜のオフィスで、壁いっぱいの付せんを前に立ち尽くす会社員（第3話と同じ人物） | 視聴者に寄り添う |
| 12 | そんな日は | 朝の通勤路で、同じ会社員が道の紙くずをひとつ拾う | 今日のひとつ |
| 13 | 今日 あなたが | 朝の机に、マス目の紙と野球ボール。小さな鉢から芽が出ている | ラスト・余韻 |

※ 約120秒÷13枚で、1枚あたり8〜9秒。間延びしたらVrewのズームで動きを付ける

---

## 1枚ずつ貼るプロンプト

**No.1｜冒頭フック（サムネ候補）**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a tall slim Japanese high school boy with short black hair in a plain white baseball practice uniform with no logos, no letters and no numbers, seen from behind, bending down to pick up a small piece of crumpled paper litter from the dirt of an empty high school baseball field at dusk, a folded sheet of paper with a square grid pattern sticks out of his back pocket, long shadows, warm amber evening light, quiet and humble mood. No face, no text, no logos.
```

**No.2｜岩手の 花巻東高校**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a rural Japanese high school baseball field in early spring, a simple backstop net and a small wooden dugout, snow still on the mountains of northern Japan in the distance, empty and quiet morning. No people, no text, no signs, no logos.
```

**No.3｜1枚の紙に目標を書く**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a tall slim Japanese high school boy with short black hair in a plain white baseball practice uniform with no logos, no letters and no numbers, seen from behind sitting at a simple desk in a small school dormitory room at night, writing with a pencil on a large sheet of paper divided into a 9 by 9 grid of small squares, a desk lamp, a baseball glove on the shelf. No face, the writing on the paper is illegible tiny scribbles, no readable text, no logos.
```

**No.4｜真ん中のマス（ドラ1 8球団）**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. close-up from above of a sheet of paper divided into a 9 by 9 grid of small squares, every square filled with tiny illegible pencil scribbles, only the single center square glows with warm golden amber light, a pencil lying beside the sheet. No readable text, no letters, no numbers.
```

**No.5｜体づくり・コントロール・スピード**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a tall slim Japanese high school boy with short black hair in a plain white baseball practice uniform with no logos, no letters and no numbers, seen from the side as a strong silhouette in mid pitching motion on a dirt pitcher's mound at sunset, his face in shadow with no detailed features, dust lifting from his foot, dramatic warm sky. No text, no logos.
```

**No.6｜そして 運**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. close-up of a sheet of paper with a square grid pattern, most squares are filled with tiny illegible scribbles, but one square is still empty and white, a teenager's hand holds a pencil hovering just above that empty square, hesitant pause, soft desk lamp light. No readable text, no letters, no numbers.
```

**No.7｜あいさつ・審判さんへの態度**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a tall slim Japanese high school boy with short black hair in a plain white baseball practice uniform with no logos, no letters and no numbers, seen from behind at the entrance of a dirt baseball field, holding his plain cap in one hand and bowing deeply toward the field, early morning light, respectful and calm mood. No face, no text, no logos.
```

**No.8｜部屋そうじ**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a tall slim Japanese high school boy with short black hair in a plain white baseball practice uniform with no logos, no letters and no numbers, seen from behind sweeping the floor of a small tidy school dormitory room with a broom, a neatly made futon and a baseball bat leaning in the corner, morning sunlight through the window. No face, no text, no logos.
```

**No.9｜ゴミ拾いは 運拾い**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. close-up of a young man's hand picking up a small crumpled piece of paper litter from the dirt of a baseball infield, the white chalk line of the field nearby, warm amber light, the moment of picking up feels important. No face, no text, no logos.
```

**No.10｜メジャーでも拾う**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a huge modern baseball stadium seen from high in the stands, packed seats and tall lights, and far below on the bright green grass a single tall player in a plain gray uniform with no logos, letters or numbers is bending down to pick up a small piece of litter, he looks tiny in the vast stadium. No readable text, no logos, no team names, no advertisements.
```

**No.11｜夢が大きすぎて（視聴者）**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a Japanese office worker in his thirties with short black hair, wearing a navy suit jacket, a white shirt and a loosened gray tie, carrying a black business backpack (keep this exact same character in the next image), standing alone in a modern office at night in front of a huge wall covered with dozens of sticky notes, seen from behind, overwhelmed and not knowing where to start, city lights through the window. No readable text on the notes, no logos.
```

**No.12｜今日 拾える ひとつ**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. the same office worker as the previous image (a Japanese office worker in his thirties with short black hair, wearing a navy suit jacket, a white shirt and a loosened gray tie, carrying a black business backpack), on a quiet city sidewalk in the early morning on his way to work, bending down to pick up a single small piece of paper litter, seen from the side with his face in soft shadow so it has no detailed features, fresh morning light, a small calm decision. No readable text, no logos.
```

**No.13｜ラスト（小さな芽を 選べる道に）**
```
NEW SCENE, do not repeat the previous composition. Bold sharp pencil sketch, thick and thin mixed lines, light colored pencil wash on white paper, NOT realistic, same style as before, 9:16 vertical. a clean light-colored wooden desk at dawn by a large window, a sheet of paper with a square grid pattern and a plain white baseball with red stitches lying on it, and next to them a small simple pot from which a single fresh green sprout is growing, the green sprout is the only vivid color in the image, quiet hopeful mood. No readable text, no logos.
```
