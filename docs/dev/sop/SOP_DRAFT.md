# SOP 草稿：AI 協同開發流程 — 互動式線性代數教材

> **目的：** 記錄 Claude Code 協同把《The Art of Linear Algebra》轉成互動式 Python 教材的完整流程，供日後其他「書 → 互動教材」專案複用。

---

## 第零章：概述

### 適用範圍
- 將既有教科書 / 圖解筆記轉為互動式視覺化教材
- 數學 / 物理 / 工程類書籍（本專案聚焦線性代數）

### 工具鏈
| 工具 | 用途 |
|------|------|
| Claude Code (CLI) | 程式碼修改、實作、重構 |
| claude.ai Chat | 概念討論、視覺化設計 |
| Python 視覺化庫 | （S01 後決定）matplotlib / Plotly / Manim / ipywidgets |

### 限制條件
- 不修改原 repo 的 LaTeX / PPT 檔案（保留原書成品）
- 互動式版本作為「新增層」存在，可選擇放在子目錄如 `interactive/`
- 跨 session 工作，每次需從 HANDOFF.md 恢復 context

---

## 第一章：專案初始化

### 1.1 Repo 取得 — S00 完成
- [x] Clone junoback/The-Art-of-Linear-Algebra
- [x] 確認原書內容範圍（5 大分解、特徵值地圖、Matrix World）

### 1.2 跨 Session 銜接機制 — S00 完成
- [x] 建立 docs/dev/ 結構

### 1.3 技術藍圖 — S01 待辦
- [ ] 與使用者確認技術棧
- [ ] 與使用者確認章節範圍與優先順序
- [ ] 與使用者確認部署形式

---

## 第二章：機械轉換工具鏈（S01 確立）

### 2.1 工具鏈選用與替代方案

| 任務 | 主用 | 替代 / 備援 | 備註 |
|---|---|---|---|
| `.tex` → `.md` | `pandoc -f latex -t markdown --wrap=preserve` | 無 | 公式以 `$$..$$` 保留 LaTeX |
| `.pdf` → 純文字 | `pdftotext -layout` (poppler) | `gs -sDEVICE=txtwrite` | poppler 品質高；gs 適合 poppler 沒裝時 |
| `.eps` → `.png` | `gs -sDEVICE=png16m -r150 -dEPSCrop` | `epstopdf` + `pdftocairo -png` | gs 不依賴 ImageMagick |
| `.eps` 預覽 | macOS Preview | `epstopdf` | EPS 不能直接內嵌 md |

**關鍵教訓：** macOS 預設不裝 ImageMagick / poppler；如要避免 brew 安裝拖時間，**ghostscript 一個工具就能涵蓋 EPS→PNG + PDF→TXT 兩個任務**，作為首發選擇最穩。後續 brew 裝完 poppler 再升級 PDF 文字品質。

### 2.2 章節對映流程
1. `grep -E "^\\\\(section|subsection)" <主檔>.tex` 抓章節
2. `grep "includegraphics" <主檔>.tex` 抓圖片清單
3. 對映表寫入 `docs/book/_merged.md` 的「章節↔圖檔對映」段
4. 章節 md 命名：`ch<NN>-<slug>.md`，子章節 `ch<NN><a-f>-<slug>.md`

### 2.3 圖片描述 Schema（四欄位）
1. **視覺結構 (Visual Structure)** — 構圖、顏色、布局；目標：盲讀者可重建畫面
2. **數學內容 (Mathematical Content)** — 變數對映、LaTeX 公式、維度
3. **直覺解讀 (Intuition)** — 此圖傳達的核心觀念、常見誤解
4. **互動化提示 (Interactivity Hints)** — Sliders / Animation / Alternative Views

理由：後三欄位剛好對應未來 Python 視覺化的計算層 / 動畫層 / widget 層，寫一次 md 後 S10+ 可直接抓參數。

### 2.4 雙語版本處理
- 主敘述用繁中（術語第一次出現括號標英文）
- 簡中 .tex 作為翻譯用詞參考（不直接照抄）
- 中文「行 / 列」採台灣慣用：column = 行（直）、row = 列（橫）— 與簡中譯名相反，需在 SCHEMA §3.1 明示

### 2.5 不修改原 repo
- `docs/book/` 是新增層，原 `figs/` `*.tex` `*.pdf` 一律不動
- 原 repo `origin` 仍指向上游（junoback），收工 commit 留本地，不可 push 到上游
- 建議使用者下個 session 改 remote（自己 fork 或建獨立 repo），或將 `docs/` 抽到獨立 git repo

---

## 附錄

### A. 版本記錄
| 版本 | 日期 | 變更 |
|------|------|------|
| 0.1 | 2026-05-11 | 初版（S00 初始化）|
