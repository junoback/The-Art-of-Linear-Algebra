# 圖片描述與章節 Schema

> **目的：** 為「《The Art of Linear Algebra》→ 互動式 Python 視覺化教材」專案定義 md 寫作格式。
> 統一格式讓後續 S02-S08 各章可獨立撰寫，並讓 S10+ 做視覺化時能直接從 md 抓參數。

---

## 1. 章節 md 檔案結構（每章一檔）

每個章節 md 的標頭與段落順序：

```markdown
# 章節編號. 章節中文標題（English Title）

> **原書頁碼：** p.X–p.Y
> **對應 .tex 段落：** `<檔案>` 第 N–M 行
> **本章圖數：** N
> **狀態：** [ ] 撰寫中 / [x] 已完成 / [ ] 校對中

---

## 章節摘要（200–400 字）

（用繁體中文總結本章要傳達的核心觀念。術語第一次出現時括號標英文。）

---

## 數學要點

> 公式直接保留 LaTeX（用 `$$ ... $$` 包），方便後續 Python 程式碼直接複製或轉 SymPy。

$$
A = \begin{bmatrix} \cdots \end{bmatrix}
$$

---

## 圖片區（逐張）

（每張圖一個 `### Figure X.Y` 子區塊，格式見第 2 節）

---

## 章末延伸

- **後續章節連結：** [→ chXX-foo.md](chXX-foo.md)
- **未來互動視覺化建議：** （供 S10+ 開發時挑題目）

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line A–B / `The-Art-of-Linear-Algebra.pdf` p.X
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line A–B
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0
```

---

## 2. 單張圖描述格式（四欄位 schema）

每張圖固定四個欄位，順序不變。後三欄位對應未來 Python 視覺化的三個層次。

```markdown
### Figure X.Y: 圖中文標題（English Caption from book）

**圖檔：** `docs/book/figs-png/<name>.png`（原始 EPS：`figs/<name>.eps`）
**原書頁碼：** p.X
**所屬章節：** §X.Y

#### 視覺結構 (Visual Structure)

文字描述這張圖的構圖：
- 整體布局（左右 / 上下 / 流程箭頭方向）
- 主要圖形元素（方塊、向量、箭頭、座標軸）
- 顏色 / 線型 / 標記符號的意義
- 視覺上要讀者「先看哪裡、再看哪裡」的引導

字數約 100–250 字，目標：盲讀者（看不到圖）也能在腦中重建畫面。

#### 數學內容 (Mathematical Content)

- 圖中出現的所有變數 → 對應的數學物件
- 圖中演示的運算或變換 → LaTeX 公式
- 維度標註（$m \times n$、向量在 $\mathbb{R}^n$ 等）

範例：
$$
\mathbf{a}_1 \in \mathbb{R}^m, \quad \mathbf{a}_2 \in \mathbb{R}^m, \quad
A = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 \end{bmatrix} \in \mathbb{R}^{m \times 2}
$$

#### 直覺解讀 (Intuition)

200–400 字的解說：
- 此圖想讓讀者「悟到」什麼概念
- 與前後章節觀念的連結
- 容易誤解的點 / 常見初學陷阱
- 必要時對比「另一種看法」（呼應原書「N Ways」風格）

#### 互動化提示 (Interactivity Hints)

供 S10+ 開發 Python 互動視覺化時參考。三類提示：

- **可調參數 (Sliders):** 列出建議讓使用者拖拉的變數（含合理範圍與步進）
  - 範例：矩陣維度 $m \in [2,6]$、$n \in [2,6]$；數值 $a_{ij} \in [-5,5]$ 步進 $0.5$
- **動畫敘事 (Animation):** 若該圖能拆解為時間步驟（例如逐欄計算內積），描述每步該突顯什麼
- **替代視角 (Alternative Views):** 此圖能與哪些其他圖切換對照
```

---

## 3. 風格與用語規範

### 3.1 語言與術語

- **主要語言：** 繁體中文
- **第一次出現的線代術語：** 中文 + 括號英文，例如「行空間 (column space)」
- **第二次起：** 可只用中文或只用英文，依該段語境
- **核心術語對照（永久保留中英並列）：**
  - matrix 矩陣
  - vector 向量
  - row 列 / column 行（**注意：中文「行」「列」與英文 row/column 翻譯習慣相反，本專案採台灣慣用：column = 行（直的）、row = 列（橫的）**）
  - rank 秩
  - subspace 子空間
  - basis 基底
  - linear combination 線性組合
  - dot product 點積 / 內積 (inner product)
  - factorization 分解
  - eigenvalue 特徵值、eigenvector 特徵向量
  - singular value 奇異值

### 3.2 公式

- 行內公式：`$a + b$`
- 區塊公式：`$$ ... $$`
- 矩陣優先用 `\begin{bmatrix}`
- 向量加粗：`\mathbf{a}`（不用 `\bm`，跨平台相容性較好）

### 3.3 圖片連結

- 一律用相對路徑指向 `figs-png/`：`![caption](figs-png/<name>.png)`
- 不直接嵌 .eps（瀏覽器顯示不了）

### 3.4 引述原書

- 若需引用原書文字，限制在「短句、必要、有引號」三條件
- 大段落改寫為自己的中文敘述 + 數學內容（事實性數學陳述不受著作權限制）
- 圖片描述全用自己的分析語言，不逐字翻譯原書圖說

---

## 4. 檔名規範

| 檔案類型 | 命名格式 | 範例 |
|---|---|---|
| 章節 md | `ch<NN>-<slug>.md` | `ch01-viewing-matrix.md` |
| 子章 md（5 大分解） | `ch06<a-f>-<slug>.md` | `ch06b-CR.md` |
| 附錄 | `appendix-<slug>.md` | `appendix-map-eigenvalues.md` |
| 機械轉換結果 | `from-{tex,pdf}/{en,zh}.{md,txt}` | `from-tex/en.md` |
| 合併版 | `BOOK.md`（S09 產出） | — |

---

## 5. 撰寫流程（每個章節 session 適用）

每個章節 session（S02–S08）的工作步驟：

1. 從 `from-tex/en.md` 抓本章的 LaTeX 原始結構（標題、公式、圖片清單）
2. 對照 `from-pdf/en.txt` 確認 PDF 上的純文字（補 pandoc 漏掉的東西）
3. 對照 `from-tex/zh.md` 看簡中版用詞做翻譯參考
4. 看 `figs-png/` 中對應的 PNG 圖檔，逐張寫四欄位描述
5. 寫章節摘要與數學要點段
6. 在 `_merged.md` 對應章節區塊勾選完成
7. 更新 HANDOFF.md 與 CURRENT_SESSION.log

---

## 6. 版本

| 版本 | 日期 | 變更 |
|---|---|---|
| 0.1 | 2026-05-12 | 初版（S01 定版）|
