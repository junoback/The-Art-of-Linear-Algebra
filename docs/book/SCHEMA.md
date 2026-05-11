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
> **本章 VizMark 數：** N（⭐⭐⭐ × n_a / ⭐⭐ × n_b / ⭐ × n_c）
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

（每章 N 張圖，每張一個 `### Figure X.Y` 子區塊，格式見 §2；圖描述後若該圖有對應 VizMark，緊跟著嵌一個 `VizMark` 引用 block）

---

## 視覺化劇本（VizScripts）

> 本章的所有 VizScript 集中於此，每個對應上方某個 VizMark。
> 格式規範見 `VIZ_SCHEMA.md` §2。

### VizScript-01: ...
（13 段細緻劇本，可直接餵 LLM 生 Python 程式）

### VizScript-02: ...
...

---

## 章末延伸

- **後續章節連結：** [→ chXX-foo.md](chXX-foo.md)
- **延伸閱讀 / 相關概念：** （非互動的純文字延伸）

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

#### 視覺化機會（VizMark 引用）

> 此欄位**取代**舊版的「互動化提示」。如果此圖值得做互動視覺化，插一個 VizMark 引用 block，並在章末「## 視覺化劇本」段寫對應 VizScript。
> 格式規範見 `VIZ_SCHEMA.md`。

範例：

```markdown
> 🎬 **VizMark-01** [切換視角] ⭐⭐⭐
> **位置：** 本圖 / §1.2 ViewingMatrix-4Ways
> **核心概念：** 同一矩陣的 4 種等價觀看視角
> **互動梗概：** 按 4 個視角鈕，主圖即時切換並動畫過渡
> **詳見劇本：** VizScript-01（章末）
```

如該圖無視覺化價值（純示意 / 表格 / 流程圖等），此小節寫「（無 VizMark — 純說明圖）」即可，不必勉強加。
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
  - row 行 / column 列（**注意：中文「行」「列」與英文 row/column 翻譯方向不唯一。本專案採華文主流慣用（含中國大陸、日本、多數 Python / 線代中文文件）：column = 列（直立）、row = 行（橫躺）。台灣本土數學教科書傳統採相反方向（column = 行、row = 列），讀者若來自此背景請花一兩分鐘調整。**）
  - column vector 列向量（直立）/ row vector 行向量（橫躺）
  - column space 列空間 $\mathbf{C}(A)$ / row space 行空間 $\mathbf{C}(A^{\mathrm{T}})$
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

每個章節 session（S02–S10）的工作步驟（**方案 A 整合版**）：

1. 從 `from-tex/en.md` 抓本章的 LaTeX 原始結構（標題、公式、圖片清單）
2. 對照 `from-pdf/en.txt` 確認 PDF 上的純文字（補 pandoc 漏掉的東西）
3. 對照 `from-tex/zh.md` 看簡中版用詞做翻譯參考
4. **看 `figs-png/` 中對應的 PNG 圖檔，逐張寫四欄位描述**
5. **同步掃描視覺化機會：每張圖看完描述後，判斷是否插 VizMark**
   - 命中 §1.3 五種類型之一 → 插 VizMark（章內就近放）
   - 判定優先級 ⭐ / ⭐⭐ / ⭐⭐⭐
6. **章末寫 VizScript：每個 VizMark 對應一個 800 字劇本**
   - 格式遵 `VIZ_SCHEMA.md` §2（13 段）
   - 配色、數字、邊界、驗收標準都明確列
7. 寫章節摘要與數學要點段（最後寫，因為描述完才能精煉摘要）
8. 在 `_merged.md` 對應章節區塊勾選完成 + 填 VizMark 計數
9. 更新 HANDOFF.md 與 CURRENT_SESSION.log

**順序提示：** 第 4-6 步是同一個「閱讀 → 描述 → 標記 → 寫劇本」的連續心智動作，**不要切開**，否則理解會斷層。

---

## 6. 版本

| 版本 | 日期 | 變更 |
|---|---|---|
| 0.1 | 2026-05-12 | 初版（S01 定版）|
