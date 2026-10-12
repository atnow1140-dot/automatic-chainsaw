# 人物シリーズ 第4話｜大谷翔平　画像の流れ（v2・2026-10-12 作り直し）

フウガが作ったNo.1（夕暮れのグラウンドで紙くずを拾う後ろ姿）を**お手本**にして、No.1から順に組み直した。
- 画風・人物はNo.1にそろえる（細かい鉛筆＋セピアとアンバーの薄塗り／汚れた白いユニフォーム・黒いソックス）
- 目標シートはフウガ作の古紙版 `goal-sheet-aged.png` を使う。ChatGPTが真ん中を「ドライ 8球団」にしていたので「ドラ1」に直した
- ChatGPTで作るのは11枚（No.2・3・5・7〜14）。そのまま貼れる版は `chatgpt-prompts.txt`
- 守ること: 顔は描かない／ロゴ・校名・背番号・MLBのデザインは入れない／文字は画像に入れない
- 旧版（v1）の一覧は git の履歴に残っている

## 最初に送る文（新しいチャットで1回。No.1の画像 `no01-chatgpt.png` を添付）
```
これから、YouTubeショート用の縦長（9:16）の挿絵を何枚か作ります。添付した画像（夕暮れのグラウンドで紙くずを拾う高校生の後ろ姿）がお手本です。このチャットのすべての画像を、次のルールで作ってください。

【画風】
添付画像と同じ：クリーム色の紙に描いた、細かい鉛筆スケッチ。色はセピアとやわらかいアンバー（夕焼けのオレンジ）を色鉛筆で薄く。写真風・3D・アニメ風にはしない。

【人物】
主人公は添付画像の高校生と同じ人物（短い黒髪・背が高くて細身・汚れた無地の白い野球のユニフォーム・黒いソックス・黒いスパイク）。顔は描かず、後ろ姿・横からのシルエット・手元だけで表現してください。

【入れないもの】
文字・ロゴ・校名・背番号・球団名・広告・実在のユニフォームのデザイン。

【その他】
毎回ちがう場面です。前の画像の構図をくり返さないでください。

理解したら「OK」とだけ返してください。
```

## 一覧（どの文から切り替えるか）
| No | 切り替える文（台本） | 場面 | 作り方 |
|---|---|---|---|
| 1 | 高校1年の大谷翔平が | 夕暮れのグラウンドで紙くずを拾う後ろ姿 | ✅ 完成（`no01-chatgpt.png`） |
| 2 | 岩手の 花巻東高校 | No.1と同じグラウンドを、朝の光で広く見せる | ChatGPT |
| 3 | 1年生の彼は | 寮の机で、マス目の紙に鉛筆で書く後ろ姿 | ChatGPT |
| 4 | 真ん中のマスには | 目標シート全体。Vrewでゆっくり真ん中の「ドラ1 8球団」に寄る | ✅ `goal-sheet-aged.png`（フウガ作の古紙版。「ドライ」を「ドラ1」に直したもの） |
| 5 | そのまわりに | 夕暮れのマウンドで投げるシルエット | ChatGPT |
| 6 | そして | 同じ目標シートで、Vrewのズームで「運」のブロックに寄る（新しく作らなくていい） | ✅ `goal-sheet-aged.png` をズーム |
| 7 | あいさつ | グラウンドの入口で、帽子を取って深く礼をする後ろ姿 | ChatGPT |
| 8 | 部屋そうじ | 寮の部屋をほうきで掃除する後ろ姿 | ChatGPT |
| 9 | ゴミ拾いは 運拾い | No.1の手元のアップ。紙くずをつまむ指 | ChatGPT |
| 10 | メジャーリーガーになった 今も | 巨大なスタジアムの芝で、紙くずを拾う小さな後ろ姿 | ChatGPT |
| 11 | 大きな夢と | 手前に芝の上の紙くず、奥にスタジアムの大きな照明 | ChatGPT |
| 12 | 夢が 大きすぎて | 夜のオフィスで、壁いっぱいの付せんの前に立ち尽くす会社員（第3話と同じ人物） | ChatGPT |
| 13 | そんな日は | 朝の通勤路で、同じ会社員が道の紙くずをひとつ拾う（No.1と同じポーズ） | ChatGPT |
| 14 | 今日 あなたが | 朝の机に、マス目の紙と野球ボール。小さな鉢から芽 | ChatGPT |

※ 約120秒÷14枚で1枚8〜9秒。No.4〜6は同じシートをVrewのズームでつなぐと流れが自然

---

## 1枚ずつ貼るプロンプト

**No.1｜冒頭フック（サムネ候補）** … ✅ 完成（`no01-chatgpt.png`）

**No.2｜岩手の 花巻東高校**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. The same rural high school baseball field as the reference image, but in early morning light, seen wide from behind home plate: the chain-link backstop, a small dugout with a bench, a dirt infield, power poles, and the mountains of northern Japan in the distance with a little snow on the peaks, empty and quiet. No people, no text, no signs, no logos.
```

**No.3｜1枚の紙に目標を書く**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. the same high school boy as the attached reference image (short black hair, tall and slim, a dirt-stained plain white baseball uniform with no logos, letters or numbers, black socks, black cleats), now in a plain gray T-shirt, seen from behind sitting at a simple wooden desk in a small school dormitory room at night, writing with a pencil on a large sheet of paper divided into a 9 by 9 grid of small squares, a desk lamp with a warm amber glow, a baseball glove on the shelf. The writing on the paper is tiny illegible scribbles. No face shown, no text, no logos, no numbers.
```

**No.4｜目標シート（全体）** … ✅ `goal-sheet-aged.png`（フウガ作の古紙版。「ドライ」を「ドラ1」に直したもの）

**No.5｜体づくり・コントロール・スピード**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. the same high school boy as the attached reference image (short black hair, tall and slim, a dirt-stained plain white baseball uniform with no logos, letters or numbers, black socks, black cleats), seen from the side as a strong silhouette in mid pitching motion on the dirt pitcher's mound of the same field at sunset, the orange sun low behind the mountains, dust lifting from his front foot, his face in shadow with no detailed features. No face shown, no text, no logos, no numbers.
```

**No.6｜運のマス** … ✅ `goal-sheet-aged.png` をズーム

**No.7｜あいさつ・審判さんへの態度**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. the same high school boy as the attached reference image (short black hair, tall and slim, a dirt-stained plain white baseball uniform with no logos, letters or numbers, black socks, black cleats), holding a plain white cap with no logo in one hand, seen from behind at the entrance gate of the same dirt baseball field, bowing deeply toward the field in the early morning, long soft shadows, respectful and calm mood. No face shown, no text, no logos, no numbers.
```

**No.8｜部屋そうじ**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. the same high school boy as the attached reference image (short black hair, tall and slim, a dirt-stained plain white baseball uniform with no logos, letters or numbers, black socks, black cleats), now in a plain gray T-shirt and the white uniform pants, seen from behind sweeping the wooden floor of a small tidy dormitory room with a broom, a neatly folded futon and a bat leaning in the corner, morning sunlight through the window. No face shown, no text, no logos, no numbers.
```

**No.9｜ゴミ拾いは 運拾い**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. Close-up of the same boy's right hand from the reference image picking up the small crumpled white paper from the dirt of the baseball field at sunset, the dirt-stained white sleeve at the edge of the frame, warm amber light, the small moment feels important. No face, no text, no logos.
```

**No.10｜メジャーでも拾う**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. A huge modern baseball stadium at dusk seen from high in the stands, packed seats and tall bright lights, and far below on the green grass a single tall player in a plain gray uniform with no logos, letters or numbers is bending down to pick up a small piece of white paper litter, the same pose as the reference image, he looks tiny in the vast stadium. No readable text, no logos, no team names, no advertisements.
```

**No.11｜大きな夢と 足もとのゴミ**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. Low angle at ground level: a single small crumpled white paper on green stadium grass in the foreground, sharp and detailed, and in the background the enormous lights and stands of a baseball stadium glowing against the evening sky, contrast between the tiny paper and the huge stadium. No people, no readable text, no logos.
```

**No.12｜夢が大きすぎて（視聴者）**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. A Japanese office worker in his thirties with short black hair, wearing a navy suit jacket, a white shirt and a loosened gray tie, carrying a black business backpack (keep this exact same character in the next image), standing alone in a modern office at night in front of a huge wall covered with dozens of sticky notes, seen from behind, overwhelmed and not knowing where to start, city lights through the window. No readable text on the notes, no logos.
```

**No.13｜今日 拾える ひとつ**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. The same office worker as the previous image, on a quiet city sidewalk in the early morning on his way to work, bending down to pick up a single small crumpled white paper, the same pose as the boy in the reference image, seen from behind and slightly to the side so his face has no detailed features, warm morning light. No readable text, no logos.
```

**No.14｜ラスト（小さな芽を 選べる道に）**
```
NEW SCENE, do not repeat the previous composition. Same drawing style as the attached reference image: detailed pencil sketch on cream paper with warm sepia and soft amber colored pencil wash, 9:16 vertical. A light-colored wooden desk at dawn by a window, a sheet of paper with a square grid pattern and a plain white baseball with red stitches lying on it, next to them a small simple pot from which a single fresh green sprout is growing, the green sprout is the only vivid color in the image, quiet hopeful mood. No readable text, no logos.
```

---

## 目標シートの画像について（v1から引き継ぎ）
- ネットで見かける実物のシート画像は、撮影・掲載した側に権利があるので加工しても使わない
- 代わりに、出典で確認できた中身だけを手書き風の文字で描き起こした（2026-10-11）
  - `goal-sheet-center.png` … 真ん中「ドラ1 8球団」＋まわり8つ（体づくり・コントロール・キレ・メンタル・スピード160km/h・人間性・運・変化球）。出典: ライフハッカー
  - `goal-sheet-un.png` … 「運」のマス8つ（あいさつ・ゴミ拾い・部屋そうじ・道具を大切に使う・審判さんへの態度・プラス思考・応援される人間になる・本を読む）。「ゴミ拾い」は赤、「運」は黄色の薄塗り。中身と並びはフウガが送ってくれた実物シートの画像（2026-10-11）で確認。ライフハッカー、プレジデントオンラインとも一致
  - `goal-sheet-full.png` / `.pdf` / `-9x16.png` … 81マス全部を描き起こした版（フウガ希望・2026-10-11）。「ゴミ拾い」に赤丸。9:16版は動画にそのまま置ける。全体→ズームで「運」のブロック→赤丸、の順に見せると効く
- 実物シートの画像そのもの（新聞・書籍に載ったもの）は動画に使わない。中身を確かめる資料としてだけ使う
- v2（2026-10-12）では、No.4・No.6ともフウガ作の古紙版 `goal-sheet-aged.png`（81マス版をもとにChatGPTで加工）を使う

