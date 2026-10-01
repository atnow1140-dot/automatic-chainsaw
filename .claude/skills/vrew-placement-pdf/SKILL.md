---
name: vrew-placement-pdf
description: 真面目の芽（YouTube）の動画用に、台本（ナレーション原稿）をもとに「どの画像を、Vrewのどの文のクリップに置くか」をまとめた配置リストPDFを作る。後から差し替えた画像（文字画面・END）や上に重ねる画像（テロップ・シンのアイコン）も全部含め、サムネイル付きで1つにまとめる。フウガが「配置リスト」「どの画像をどこに入れるか」「挿絵の配置」「差し替え込みのリスト」を求めたとき、または挿絵がそろってVrewで組む前に使う。
---

# Vrew 挿絵の配置リストPDF（動画制作の標準フォーマット）

フウガ決定（2026-10-01）：動画を作るときは、この形式のPDFで渡す。第2話以降もすべてこの形。

## 見本（第1話・フウガOKの最終版）
- `examples/ep01/ep01_vrew-placement_final.pdf` … 完成形。見た目・行の並べ方・メモの書き方はこれに合わせる
- `examples/ep01/ep01_placement.csv` … そのCSV。新しい回はこれをコピーして書き換えるのが早い
- 第1話の時間の目安は概要欄の目次に合わせて手入力した（自動計算は少し短めに出る）

## 中身
- タイトル＋サブ行（ナレーション原稿のファイル名、時間の目安の出し方）
- **置き方**：Vrewでの置き方のルール（差替＝赤、重ね＝緑の意味も）
- **配置リスト**の表：画像／目安／切り替える文（このクリップから）／絵の内容／メモ
  - 後から差し替えた画像は【差替】（赤）、上に重ねる透過PNGは【重ね】（緑）のバッジ＋サムネイル
  - 重ねる画像は、重ねる先の画像の行のすぐ下に置く（シンのアイコンは一番上）

## 手順
1. **材料を集める**：ナレーション原稿（Vrew用txt）、挿絵の一覧（番号と絵の内容）、差し替え・重ね用の画像
2. **素材フォルダ**：`company/production/epXX_parts/` にナレーション原稿・差し替え画像・重ね画像を置く
3. **CSVを書く**：`epXX_parts/epXX_placement.csv`（列は `image,kind,time,line,content,memo,thumb`）
   - `line` はナレーション原稿の文の書き出しをそのままコピー（Vrewのクリップを探しやすいように）
   - `kind`：空／差替／重ね。`thumb`：表示したい画像のファイル名（CSVと同じフォルダ）
   - `time`：空なら1分300字で自動計算。概要欄の目次と合わせたいときは手で入れる
   - 「文字」画面を画像で作っていないときは `image` に `文字` と書く（灰色の行になる）
4. **PDFにする**：
   ```
   python3 .claude/skills/vrew-placement-pdf/scripts/make_placement.py \
     company/production/epXX_parts/epXX_placement.csv \
     --narration company/production/epXX_parts/narration_vrew.txt \
     --title "真面目の芽｜第X話「タイトル」Vrew 挿絵の配置リスト" \
     --out company/production/epXX_parts/epXX_vrew-placement.pdf
   ```
   置き方に足したいルールは `--rule "…"` で追加できる
5. **自分で確認**：PDFをReadで開いて、サムネイルが出ているか、文がナレーション原稿と一致しているか（警告が出ていないか）を見る
6. **渡す**：SendUserFile（display: render）で送り、todoにパスを書く。コミットしてpushする
7. **差し替えが出たら**：CSVの行を直して（kind=差替、thumbを追加）作り直す。PDFは常に最新版1つにまとめる
