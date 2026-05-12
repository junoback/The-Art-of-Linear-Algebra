# 第 3 章. 矩陣乘以向量 — 兩種視角 + 四個基本子空間（Matrix × Vector — 2 Ways + The Four Subspaces）

> **原書頁碼：** p.3
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 69–112 行
> **本章圖數：** 3（Figure 3.1 / 3.2 / 3.3）
> **本章 VizMark 數：** 4（⭐⭐⭐ × 2 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成 / [ ] 校對中

---

## 章節摘要

矩陣乘以向量 $A\mathbf{x}$ 有兩種視角：**(Mv1) 點積方式** — 把 $A$ 的每一橫躺行當成一個向量，與 $\mathbf{x}$ 做點積，得到一條由「行數個點積」堆出來的列向量；**(Mv2) 線性組合方式** — 把 $A$ 的每一直立列當成一個向量，用 $\mathbf{x}$ 的分量當係數做線性組合，得到的依然是同一條列向量。**初學會先學 (Mv1)，但 (Mv2) 才是後續所有章節（特別是子空間與分解）的鑰匙。**

對偶側：**行向量** $\mathbf{y}$ 從左邊乘以 $A$ 也有完全平行的兩種視角 — **(vM1)** 點積方式（$\mathbf{y}$ 對 $A$ 每一直立列做點積）、**(vM2)** 線性組合方式（$A$ 每一橫躺行用 $\mathbf{y}$ 分量做線性組合）。

把這兩組視角合起來，會自然冒出**四個基本子空間 (Four Fundamental Subspaces)**：
- 在 $\mathbb{R}^n$ 中：**行空間 (row space)** $\mathbf{C}(A^{\mathrm{T}})$（所有可能的 $\mathbf{y}A$）與 **零空間 (nullspace)** $\mathbf{N}(A)$（所有滿足 $A\mathbf{x} = \mathbf{0}$ 的 $\mathbf{x}$），兩者**正交互補**；
- 在 $\mathbb{R}^m$ 中：**列空間 (column space)** $\mathbf{C}(A)$（所有可能的 $A\mathbf{x}$）與 **左零空間 (left nullspace)** $\mathbf{N}(A^{\mathrm{T}})$（所有滿足 $\mathbf{y}A = 0$ 的 $\mathbf{y}$），兩者**正交互補**。

> ⚠ **本章是全書最濃縮的一章。** §1 鋪設視角、§2 是「外積 = 秩 1」基本骨架，本章一次端上**「兩個運算 × 兩個視角 × 兩個方向」=「八種乘法畫面」+ 四個子空間的幾何圖**。讀通後，§6 的所有分解都會變成自然推論。

> ⚠ **術語提醒（沿用 §1 / §2 全書慣例 — A 派）：** column = 列（直立、綠色）、row = 行（橫躺、粉紅色）。$\mathbf{C}(A) = $ 列空間（columns of $A$ 張成）、$\mathbf{C}(A^{\mathrm{T}}) = $ 行空間（rows of $A$ 張成）、$\mathbf{N}(A) = $ 零空間、$\mathbf{N}(A^{\mathrm{T}}) = $ 左零空間。

> ### 💡 背後觀念：$A\mathbf{x}$ 兩種讀法與四子空間是怎麼自然冒出的？
>
> 本章涵蓋線性代數最濃縮的 **3 個基本動機問題**：
>
> - **[Q06：$A\mathbf{x}$ 為什麼這樣定義？](appendix-D-why.md#q06)** — $A\mathbf{x}$ 不是事後設計的，是從「想把 $m$ 個方程濃縮為單一矩陣方程 $A\mathbf{x} = \mathbf{b}$」這個需求**自然浮現**的。完整的 4 步驟設計過程（拆 $A,\mathbf{x},\mathbf{b}$ → 要求結果 → 觀察規律 → 兩讀法等價）顯示「行點積」與「列線性組合」兩讀法是**同一個展開的兩種重排**。
> - **[Q07：為什麼要有 2 個視角（點積 + 線性組合）？](appendix-D-why.md#q07)** — **(Mv1) 是「算」、(Mv2) 是「看」**。判斷「$A\mathbf{x} = \mathbf{b}$ 有沒有解？」用 (Mv1) 要跑完高斯消去法、用 (Mv2) **一秒看出**（$\mathbf{b}$ 在 $\mathbf{C}(A)$ 嗎？）。Strang 強調「**列視角是線代的鑰匙**」 — 整本 §4–§6 五大分解都用列視角為主導。
> - **[Q08：四個基本子空間為什麼會自然冒出？](appendix-D-why.md#q08)** — 4 子空間是「**2 方向（右乘 $A$ vs 左乘 $A^{\mathrm{T}}$）× 2 概念（像 vs 核）= 4**」的**組合必然產物**，不可能多、不可能少。它們兩兩正交、列秩 = 行秩、維度互補 — 這些「優美」結果不是巧合，而是「$A$ 把 $\mathbb{R}^n$ 分成（行空間 + 零空間），$A^{\mathrm{T}}$ 把 $\mathbb{R}^m$ 分成（列空間 + 左零空間）」這個雙向分解的必然產物。Strang 稱之為「**線性代數的地理**」。

---

## 數學要點

設 $A \in \mathbb{R}^{m \times n}$（$m$ 行 $n$ 列）、$\mathbf{x} \in \mathbb{R}^n$、$\mathbf{y} \in \mathbb{R}^{1 \times m}$（行向量）。

### (Mv1) 點積方式（Dot Product Way）

把 $A$ 拆成 $m$ 個橫躺行 $\mathbf{a}^*_1, \mathbf{a}^*_2, \ldots, \mathbf{a}^*_m \in \mathbb{R}^{1 \times n}$（每個是行向量），則：

$$
A\mathbf{x}
\;=\;
\begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix}
\mathbf{x}
\;=\;
\begin{bmatrix} \mathbf{a}^*_1 \cdot \mathbf{x} \\ \mathbf{a}^*_2 \cdot \mathbf{x} \\ \vdots \\ \mathbf{a}^*_m \cdot \mathbf{x} \end{bmatrix}
\;\in\; \mathbb{R}^m
$$

- **形狀運算：** $(m \times n)(n \times 1) = (m \times 1)$。
- **逐分量計算：** 第 $i$ 個輸出分量 $= \sum_{k=1}^{n} a_{ik} x_k$。
- **原書 (Mv1) 範例：**

$$
A\mathbf{x}
\;=\;
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
\;=\;
\begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \\ 5x_1 + 6x_2 \end{bmatrix}
$$

### (Mv2) 線性組合方式（Linear Combination Way）

把 $A$ 拆成 $n$ 個直立列 $\mathbf{a}_1, \mathbf{a}_2, \ldots, \mathbf{a}_n \in \mathbb{R}^m$（每個是列向量），則：

$$
A\mathbf{x}
\;=\;
\begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}
\;=\;
x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \cdots + x_n \mathbf{a}_n
\;\in\; \mathbb{R}^m
$$

- **形狀運算：** 同 (Mv1)，$(m \times n)(n \times 1) = (m \times 1)$。
- **直覺：** $\mathbf{x}$ 的每一個分量都是一個「混合比例」，告訴你要把 $A$ 的某一直立列**放大幾倍**，再把所有放大後的列**疊加**起來。
- **原書 (Mv2) 範例：**

$$
A\mathbf{x}
\;=\;
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \end{bmatrix}
\;=\;
x_1 \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} + x_2 \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}
$$

### 對偶關係（Mv1 ↔ Mv2）

兩種視角**計算結果完全一致**，差別在「讀法」：
- (Mv1) 是「**逐個橫躺行單獨吃進整個 $\mathbf{x}$**」 — 每一橫躺行各自做完一個 dot product，把 $m$ 個結果堆出來。
- (Mv2) 是「**逐個直立列同時被 $\mathbf{x}$ 的某分量縮放**」 — $\mathbf{x}$ 一次決定所有列的縮放比例，再把它們向量相加。

兩者也對應「**外向看**」與「**內向看**」：(Mv1) 把 $A$ 攤平成橫躺行；(Mv2) 把 $A$ 拼立成直立列。

### (vM1) 行向量點積方式（Row Dot Product Way）

把 $A$ 拆成 $n$ 個直立列 $\mathbf{a}_1, \ldots, \mathbf{a}_n$，行向量 $\mathbf{y} \in \mathbb{R}^{1 \times m}$ 從左乘以 $A$：

$$
\mathbf{y} A
\;=\;
\mathbf{y}
\begin{bmatrix} \mathbf{a}_1 & \cdots & \mathbf{a}_n \end{bmatrix}
\;=\;
\begin{bmatrix} \mathbf{y} \cdot \mathbf{a}_1 & \mathbf{y} \cdot \mathbf{a}_2 & \cdots & \mathbf{y} \cdot \mathbf{a}_n \end{bmatrix}
\;\in\; \mathbb{R}^{1 \times n}
$$

- **形狀運算：** $(1 \times m)(m \times n) = (1 \times n)$，結果是一個行向量。
- **逐分量計算：** 第 $j$ 個輸出分量 $= \mathbf{y} \cdot \mathbf{a}_j = \sum_{i=1}^{m} y_i a_{ij}$。
- **原書 (vM1) 範例：**

$$
\mathbf{y} A
\;=\;
\begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix}
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\;=\;
\begin{bmatrix} y_1 + 3y_2 + 5y_3 & 2y_1 + 4y_2 + 6y_3 \end{bmatrix}
$$

### (vM2) 行向量線性組合方式（Row Linear Combination Way）

把 $A$ 拆成 $m$ 個橫躺行 $\mathbf{a}^*_1, \ldots, \mathbf{a}^*_m$，則：

$$
\mathbf{y} A
\;=\;
\begin{bmatrix} y_1 & y_2 & \cdots & y_m \end{bmatrix}
\begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix}
\;=\;
y_1 \mathbf{a}^*_1 + y_2 \mathbf{a}^*_2 + \cdots + y_m \mathbf{a}^*_m
\;\in\; \mathbb{R}^{1 \times n}
$$

- **直覺：** $\mathbf{y}$ 的每一分量是「混合比例」，把 $A$ 的某一橫躺行放大幾倍，再把所有橫躺行疊加成一條新行向量。
- **原書 (vM2) 範例：**

$$
\mathbf{y} A
\;=\;
\begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix}
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\;=\;
y_1 \begin{bmatrix} 1 & 2 \end{bmatrix} + y_2 \begin{bmatrix} 3 & 4 \end{bmatrix} + y_3 \begin{bmatrix} 5 & 6 \end{bmatrix}
$$

### Mv ↔ vM 對偶（左乘 vs 右乘的鏡像對稱）

| | 點積方式（1） | 線性組合方式（2） | 結果型 |
|---|---|---|---|
| **右乘** $A\mathbf{x}$ | (Mv1) 每**橫躺行** · $\mathbf{x}$ | (Mv2) $\mathbf{x}$ 對 $A$ 的**直立列**做線性組合 | 列向量 $\in \mathbb{R}^m$ |
| **左乘** $\mathbf{y}A$ | (vM1) $\mathbf{y}$ · 每**直立列** | (vM2) $\mathbf{y}$ 對 $A$ 的**橫躺行**做線性組合 | 行向量 $\in \mathbb{R}^{1 \times n}$ |

**記憶口訣：**「**點積看對立方向、線性組合看同方向**」— Mv1 行（橫躺） · 列（直立）方向互垂直；Mv2 列向量被列向量縮放（同直立）。vM 也一樣：vM1 行 · 列 垂直、vM2 行向量被行向量縮放（同橫躺）。

### 四個基本子空間（The Four Fundamental Subspaces）

把上面兩個運算所有可能的輸出蒐集起來，就會在 $\mathbb{R}^n$ 與 $\mathbb{R}^m$ 中各得到兩個子空間，共**四個**：

| 子空間 | 定義 | 所在空間 | 維度 | 物理意義 |
|---|---|---|---|---|
| **列空間** $\mathbf{C}(A)$ | $\{A\mathbf{x} : \mathbf{x} \in \mathbb{R}^n\}$ = $A$ 所有直立列的線性組合 | $\mathbb{R}^m$ | $r$（秩） | "What $A$ can output as $A\mathbf{x}$" — 所有 (Mv2) 結果的集合 |
| **零空間** $\mathbf{N}(A)$ | $\{\mathbf{x} \in \mathbb{R}^n : A\mathbf{x} = \mathbf{0}\}$ | $\mathbb{R}^n$ | $n - r$ | "What $A$ sends to zero" — 滿足 (Mv1) 全為 0 的 $\mathbf{x}$ |
| **行空間** $\mathbf{C}(A^{\mathrm{T}})$ | $\{\mathbf{y}A : \mathbf{y} \in \mathbb{R}^{1 \times m}\}$ = $A$ 所有橫躺行的線性組合 | $\mathbb{R}^n$ | $r$（與列空間同維） | 所有 (vM2) 結果的集合 |
| **左零空間** $\mathbf{N}(A^{\mathrm{T}})$ | $\{\mathbf{y} \in \mathbb{R}^{1 \times m} : \mathbf{y}A = 0\}$ | $\mathbb{R}^m$ | $m - r$ | 滿足 (vM1) 全為 0 的 $\mathbf{y}$ |

**兩對正交分解（perpendicular decomposition）：**

$$
\mathbb{R}^n \;=\; \mathbf{C}(A^{\mathrm{T}}) \oplus \mathbf{N}(A),
\qquad
\mathbf{C}(A^{\mathrm{T}}) \perp \mathbf{N}(A)
$$

$$
\mathbb{R}^m \;=\; \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}}),
\qquad
\mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}})
$$

**正交性的直接證明（一行）：** 設 $\mathbf{v} \in \mathbf{N}(A)$，則 $A\mathbf{v} = \mathbf{0}$，亦即 $A$ 的每一橫躺行 $\cdot \mathbf{v} = 0$。所以 $\mathbf{v}$ 與每一橫躺行都垂直 → $\mathbf{v} \perp \mathbf{C}(A^{\mathrm{T}})$。

**為何說「自然冒出」？** (Mv1) 與 (vM1) 都是「以橫躺 / 直立向量做點積」 — 點積等於零正是「垂直」的定義；而 (Mv2) 與 (vM2) 都是「以列 / 行做線性組合」 — 線性組合的張成正是「子空間」的定義。**四個子空間就是「兩個運算 × 兩個視角」自然交叉的產物**。

### 對應原書章節（Strang《Linear Algebra for Everyone》）

- Sec. 1.1 (p.3) Linear combinations — 對應 (Mv2)
- Sec. 1.3 (p.21) Matrices and Column Spaces — 對應 $\mathbf{C}(A)$
- Sec. 3.5 (p.124) Dimensions of the Four Subspaces — 對應四子空間維度定理
- 補充：Sec 6.1 $A = CR$ 給出秩 $r$ 的具體分解（將在 §6.1 詳細處理）

---

## 圖片區

本章共 3 張圖：Figure 3.1（Mv1, Mv2）、Figure 3.2（vM1, vM2）、Figure 3.3（Four Subspaces）。

---

### Figure 3.1: 矩陣乘以向量的兩種視角（Matrix × Vector — (Mv1), (Mv2)）

**圖檔：** `docs/book/figs-png/MatrixTimesVector.png`（原始 EPS：`figs/MatrixTimesVector.eps`）
**原書頁碼：** p.3
**所屬章節：** §3

#### 視覺結構 (Visual Structure)

此圖採「左右並列兩區」結構，**左半 (Mv1) 點積方式**、**右半 (Mv2) 線性組合方式**，每區「**抽象色塊示意（上）+ 文字描述（中）+ 具體數字範例（下）**」三層。

- **左半：(Mv1) 點積方式**
  - 左上角小灰圈內標 `Mv1`，標示視角編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **粉紅色橫條 × 3 條** 堆疊在大方框內 —— 表示 $A$ 的 3 個橫躺行（rows）。
    2. **綠色直條** —— 表示列向量 $\mathbf{x}$（直立）。
    3. **粉紅色橫條 × 3 條**，每條中段被綠色色塊覆蓋 —— 表示產出的列向量 $A\mathbf{x}$，每個分量是「該橫躺行 · $\mathbf{x}$」的 dot product 結果（粉紅 + 綠交疊代表 dot 過程）。
  - 中段文字：**"The row vectors of $A$ are multiplied by a vector $\mathbf{x}$ and become the three dot-product elements of $A\mathbf{x}$."**
  - 具體範例（最下方）：
    $$A\mathbf{x} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \\ 5x_1 + 6x_2 \end{bmatrix}$$
- **右半：(Mv2) 線性組合方式**
  - 左上角小灰圈內標 `Mv2`，標示視角編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **綠色直條 × 2 條** 並列在大方框內 —— 表示 $A$ 的 2 個直立列（columns）。
    2. **2 個藍色實心圓點**直立排列在小方框內 —— 表示 $\mathbf{x}$ 的兩個分量（$x_1, x_2$）。
    3. 在 `=` 右側出現 **2 個項相加**的結構：「藍點 × 綠直條 + 藍點 × 綠直條」 —— 表示 $\mathbf{x}$ 的每個分量分別縮放 $A$ 的每一直立列，再相加。
  - 中段文字：**"The product $A\mathbf{x}$ is a linear combination of the column vectors of $A$."**
  - 具體範例（最下方）：
    $$A\mathbf{x} = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = x_1 \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} + x_2 \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}$$
- **配色語意（沿用 §1 §2）：** 綠 = 列向量 / 直立、粉紅 = 行向量 / 橫躺、藍點 = 標量 / $\mathbf{x}$ 分量、灰 = 結構填充。
- **左右兩區的「視角互補」對比：**
  - (Mv1) 主角是**橫躺粉紅** — $A$ 被攤平成 3 個橫躺行，每行各自吃進整個 $\mathbf{x}$。
  - (Mv2) 主角是**直立綠** — $A$ 被拼立成 2 個直立列，$\mathbf{x}$ 從上方一次分配權重給所有列。
  - 兩種視角的「動詞」不同：(Mv1) 是「**逐行 dot**」、(Mv2) 是「**整體 weight**」。

讀者的視覺動線：先看左半 (Mv1) 確認熟悉的「逐行點積運算」 → 跳到右半 (Mv2) 看到「同樣的結果可從『列向量加權和』算出」 → 對比下方兩個具體範例（同一個 $A$ 和 $\mathbf{x}$，左邊是分量展開、右邊是列向量乘係數展開）→ 領悟「(Mv2) 把 $A\mathbf{x}$ 重新詮釋成 column space 中的一個向量」這個關鍵翻轉。

#### 數學內容 (Mathematical Content)

兩種視角共享同一個結果 $A\mathbf{x} \in \mathbb{R}^m$，但展開方式不同。

**設定：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \in \mathbb{R}^{3 \times 2}$，$\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \in \mathbb{R}^2$。

**(Mv1) 點積展開：**

$$
A\mathbf{x} \;=\; \begin{bmatrix} \mathbf{a}^*_1 \cdot \mathbf{x} \\ \mathbf{a}^*_2 \cdot \mathbf{x} \\ \mathbf{a}^*_3 \cdot \mathbf{x} \end{bmatrix} \;=\; \begin{bmatrix} (1, 2) \cdot (x_1, x_2) \\ (3, 4) \cdot (x_1, x_2) \\ (5, 6) \cdot (x_1, x_2) \end{bmatrix} \;=\; \begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \\ 5x_1 + 6x_2 \end{bmatrix}
$$

**(Mv2) 線性組合展開：**

$$
A\mathbf{x} \;=\; x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 \;=\; x_1 \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} + x_2 \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} \;=\; \begin{bmatrix} x_1 + 2x_2 \\ 3x_1 + 4x_2 \\ 5x_1 + 6x_2 \end{bmatrix}
$$

**驗證恆等：** 兩種展開的每一分量逐項相同（$x_1 + 2x_2 = 1 \cdot x_1 + 2 \cdot x_2$，依此類推）。

**形狀運算（兩種視角共通）：** $(3 \times 2)(2 \times 1) = (3 \times 1)$。中間維度 2 必須相等才能做乘法。

**列空間的具體呈現：** 任何 $A\mathbf{x}$ 都可寫成 $x_1 (1,3,5)^{\mathrm{T}} + x_2 (2,4,6)^{\mathrm{T}}$，即 $\mathbf{C}(A) = \operatorname{span}\{(1,3,5)^{\mathrm{T}}, (2,4,6)^{\mathrm{T}}\} \subset \mathbb{R}^3$。由於這兩個列向量線性獨立（不成比例），$\dim \mathbf{C}(A) = r = 2$，是 $\mathbb{R}^3$ 中的一個平面。

#### 直覺解讀 (Intuition)

**1. 同一個運算的兩種「閱讀方向」。** 矩陣乘向量 $A\mathbf{x}$ 不是兩個算式 — 是同一個算式被「**橫切**」（Mv1：一行一行做點積）或「**縱切**」（Mv2：一列一列做縮放再相加）的兩個視角。剛入門時 (Mv1) 直觀（套用點積公式），但 (Mv2) 才是矩陣論的核心 — 因為它把 $A\mathbf{x}$ 解讀成「$A$ 列空間裡的某個向量」，直接連接到子空間 / 秩 / 解的存在性。

**2. 為什麼 (Mv2) 是後續一切的鑰匙？**

- **「$A\mathbf{x} = \mathbf{b}$ 有解 ⟺ $\mathbf{b} \in \mathbf{C}(A)$」** — 這個基本定理直接從 (Mv2) 視角看到：因為 $A\mathbf{x}$ 就是 $A$ 直立列的線性組合，所以 $\mathbf{b}$ 必須是這些列的某個組合才有解。從 (Mv1) 視角看則需要繞一圈點積與聯立方程。
- **「秩 = 線性無關直立列的最大個數」** — 從 (Mv2) 視角看，秩就是「$\mathbf{C}(A)$ 的維度」，是 $A$「能輸出多少不同方向」的衡量。
- **「特徵向量 / 奇異向量都是『被 $A$ 直立列線性組合』後恰好指向特定方向的 $\mathbf{x}$」** — §6 的所有矩陣分解都建立在 (Mv2) 視角上。

**3. 兩個視角對應兩種解方程策略。** 解 $A\mathbf{x} = \mathbf{b}$：
- **從 (Mv1) 出發** → 高斯消去法（Gaussian elimination）— 對橫躺行做加減消元。
- **從 (Mv2) 出發** → 投影 / 最小二乘 / SVD — 找 $\mathbf{C}(A)$ 中最接近 $\mathbf{b}$ 的點。
高中學的解聯立屬 (Mv1) 思路；機器學習與信號處理大量使用 (Mv2) 思路。

**4. 矩陣的本質是「函數」，$\mathbf{x}$ 是「指令」。** 從 (Mv2) 看，$A$ 把「$\mathbf{x}$ 的每個分量」翻譯成「對應直立列要放大幾倍」。$\mathbf{x}$ 是一份「混合配方」、$A$ 的直立列是「材料庫」、$A\mathbf{x}$ 是「成品」。

**常見誤解警示：**
- **「(Mv1) 和 (Mv2) 是不同算法」** — 否，**完全相同的計算結果**，只是「視角 / 解讀順序」不同。差別在心智模型而非數值。
- **「線性組合 (Mv2) 的係數從哪來？」** — $\mathbf{x}$ 的分量本身就是係數，不需另外求。$\mathbf{x}$ 的角色從「被矩陣作用的向量」翻轉成「指揮列向量怎麼組合的係數」。
- **「直立列必須線性獨立」** — 否，$A$ 的直立列可以線性相依（此時 $r < n$），但 $A\mathbf{x}$ 永遠落在 $\mathbf{C}(A)$ 內。

**為什麼這張圖該做成互動視覺化？** 「拉 $\mathbf{x}$ 的分量看 (Mv2) 兩個列同步縮放再疊加」是動態概念 — 靜態圖無法傳達「縮放動畫」與「向量加法尾接頭視覺」。並且 (Mv1) → (Mv2) 的「視角切換」本身就是本書最重要的認知翻轉（見 VizMark-01）。另外輸入 $\mathbf{x}$ 看 $A\mathbf{x}$ 在 3D 平面上掃過 $\mathbf{C}(A)$ 也是建立子空間直覺的關鍵（見 VizMark-04）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [切換視角] ⭐⭐⭐
> **位置：** Figure 3.1 / §3 / (Mv1) ↔ (Mv2) 對偶
> **核心概念：** $A\mathbf{x}$ 同時是「橫躺行的點積堆疊」與「直立列的線性組合」 — 兩種視角同結果
> **互動梗概：** toggle (Mv1) / (Mv2)，畫面動畫切換「行橫躺被綠覆蓋 → 列直立被藍點縮放並疊加」，下方公式同步重排
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-04** [拉桿調參 + 空間幾何] ⭐
> **位置：** Figure 3.1 / §3 / (Mv2) 結果端
> **核心概念：** $A\mathbf{x}$ 永遠落在 $\mathbf{C}(A)$ 中（$\mathbb{R}^m$ 內的子空間）
> **互動梗概：** 一邊拉 $\mathbf{x}$ 各分量、一邊在 3D 視窗即時顯示 $A\mathbf{x}$ 端點 + 已掃過的軌跡（漸層淡化），顯示「軌跡完全落在某個平面內」
> **詳見劇本：** VizScript-04（章末，輕量版）

---

### Figure 3.2: 向量乘以矩陣的兩種視角（Vector × Matrix — (vM1), (vM2)）

**圖檔：** `docs/book/figs-png/VectorTimesMatrix.png`（原始 EPS：`figs/VectorTimesMatrix.eps`）
**原書頁碼：** p.3
**所屬章節：** §3

#### 視覺結構 (Visual Structure)

此圖採「**上下並列兩區**」結構（與 Figure 3.1 的左右並列形成轉置對應），**上半 (vM1) 行向量點積**、**下半 (vM2) 行向量線性組合**。

- **上半：(vM1) 行向量點積方式**
  - 左上角小灰圈內標 `vM1`，標示視角編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **粉紅色橫條** —— 行向量 $\mathbf{y}$（橫躺）。
    2. **綠色直條 × 2 條** 並列在大方框內 —— 表示 $A$ 的 2 個直立列。
    3. **粉紅色橫條** 中含 2 個被綠覆蓋的小區段 —— 表示產出的行向量 $\mathbf{y}A$，2 個分量各是「$\mathbf{y}$ · 該直立列」的 dot product。
  - 右側文字：**"A row vector $\mathbf{y}$ is multiplied by the two column vectors of $A$ and become the two dot-product elements of $\mathbf{y}A$."**
  - 具體範例（下方）：
    $$\mathbf{y}A = \begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} = \begin{bmatrix} (y_1 + 3y_2 + 5y_3) & (2y_1 + 4y_2 + 6y_3) \end{bmatrix}$$
- **下半：(vM2) 行向量線性組合方式**
  - 左上角小灰圈內標 `vM2`。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **3 個藍色實心圓點** 橫排在小方框內 —— 表示 $\mathbf{y}$ 的三個分量（$y_1, y_2, y_3$）。
    2. **粉紅色橫條 × 3 條** 堆疊在大方框內 —— 表示 $A$ 的 3 個橫躺行。
    3. 在 `=` 右側出現 **3 個項相加**的結構：「藍點 × 粉紅橫條 + 藍點 × 粉紅橫條 + 藍點 × 粉紅橫條」 —— 表示 $\mathbf{y}$ 的每個分量分別縮放 $A$ 的每一橫躺行，再相加。
  - 右側文字：**"The product $\mathbf{y}A$ is a linear combination of the row vectors of $A$."**
  - 具體範例（下方）：
    $$\mathbf{y}A = \begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix} \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} = y_1 \begin{bmatrix} 1 & 2 \end{bmatrix} + y_2 \begin{bmatrix} 3 & 4 \end{bmatrix} + y_3 \begin{bmatrix} 5 & 6 \end{bmatrix}$$
- **配色語意（沿用）：** 綠 / 粉紅 / 藍點 / 灰，**配色與 Figure 3.1 完全一致**（讀者跨圖認知不需重學）。
- **與 Figure 3.1 的對偶結構：**
  - 上下兩區的「主角形狀」與 Figure 3.1 完全鏡像：(vM1) 主角是**直立綠**（$A$ 攤成 2 個直立列）、(vM2) 主角是**橫躺粉紅**（$A$ 攤成 3 個橫躺行）。
  - 兩張圖合看會發現：**右乘 (Mv*)** 把焦點放在「結果落在 $\mathbb{R}^m$」、**左乘 (vM*)** 把焦點放在「結果落在 $\mathbb{R}^{1 \times n}$」。

讀者的視覺動線：因為已經看過 Figure 3.1，這張圖可以快讀 — 重點不是學新內容，而是**確認對偶結構** + **建立「左乘 ↔ 右乘 = 行 / 列鏡像」直覺**。

#### 數學內容 (Mathematical Content)

**設定：** $\mathbf{y} = \begin{bmatrix} y_1 & y_2 & y_3 \end{bmatrix} \in \mathbb{R}^{1 \times 3}$，$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（與 Figure 3.1 同矩陣）。

**(vM1) 點積展開：**

$$
\mathbf{y}A \;=\; \begin{bmatrix} \mathbf{y} \cdot \mathbf{a}_1 & \mathbf{y} \cdot \mathbf{a}_2 \end{bmatrix} \;=\; \begin{bmatrix} y_1 + 3y_2 + 5y_3 & 2y_1 + 4y_2 + 6y_3 \end{bmatrix}
$$

**(vM2) 線性組合展開：**

$$
\mathbf{y}A \;=\; y_1 \mathbf{a}^*_1 + y_2 \mathbf{a}^*_2 + y_3 \mathbf{a}^*_3 \;=\; y_1 \begin{bmatrix} 1 & 2 \end{bmatrix} + y_2 \begin{bmatrix} 3 & 4 \end{bmatrix} + y_3 \begin{bmatrix} 5 & 6 \end{bmatrix}
$$

**形狀運算：** $(1 \times 3)(3 \times 2) = (1 \times 2)$。

**行空間具體呈現：** 任何 $\mathbf{y}A$ 都可寫成 3 個橫躺行 $(1,2), (3,4), (5,6)$ 的線性組合，即 $\mathbf{C}(A^{\mathrm{T}}) = \operatorname{span}\{(1,2), (3,4), (5,6)\} \subset \mathbb{R}^2$（注意這 3 個橫躺行所在空間是 $\mathbb{R}^2$）。但 3 個 2 維向量必線性相依（最多 2 個獨立），可驗證 $(3,4) = 2(1,2) + (1,0) \cdot \cdots$（不太對；正確的關係見下）。實際上 $\dim \mathbf{C}(A^{\mathrm{T}}) = r = 2$（與列空間同維） — $\mathbf{C}(A^{\mathrm{T}}) = \mathbb{R}^2$ 整個平面。

#### 直覺解讀 (Intuition)

**1. 結構完全平行於 Figure 3.1。** 把 Figure 3.1 整張圖「**轉置一下**」（行 ↔ 列、左右並列 → 上下並列），就得到 Figure 3.2。所有概念（點積方式 / 線性組合方式 / 結果空間 / 等等）一對一對應。**讀通 Figure 3.1 後，Figure 3.2 約 30 秒就能 internalize。**

**2. 為何要區分左乘 / 右乘？** 在抽象代數裡，矩陣乘法不滿足交換律（$A\mathbf{x} \ne \mathbf{x}A$ 一般而言形狀都不同），所以「從哪邊乘」決定了：
- **產物形狀：** $A\mathbf{x}$ 是列向量、$\mathbf{y}A$ 是行向量。
- **所連接的子空間：** $A\mathbf{x}$ 連到 $\mathbf{C}(A)$（列空間）、$\mathbf{y}A$ 連到 $\mathbf{C}(A^{\mathrm{T}})$（行空間）。

**3. 工程實作為何需要兩個視角？** Python / NumPy 預設用列向量，PyTorch 卻習慣把 batch 維度放最前，**矩陣等價於從左乘**。傳統線性代數教科書多用右乘（$A\mathbf{x} = \mathbf{b}$），深度學習論文常用左乘（$\mathbf{y} = \mathbf{x}W$）。本章兩種視角都要熟練，才能無痛切換不同教材 / 框架。

**4. 對偶證明的便利。** 「列空間維度 = 行空間維度」（即「row rank = column rank」）這個經典定理，從 (Mv2) + (vM2) 對偶就有自然證明：(Mv2) 告訴你 $\dim \mathbf{C}(A) = r$ 個獨立直立列 ⟺ (vM2) 告訴你經過某種行操作後也是 $r$ 個獨立橫躺行（細節見 Strang §3.4）。

**常見誤解警示：**
- **「左乘和右乘的『點積方式』看似都是 dot，但 dot 的對象不同」** — (Mv1) 是 $A$ 的橫躺行 · $\mathbf{x}$，(vM1) 是 $\mathbf{y}$ · $A$ 的直立列。對象從「行 vs 列」換到「行 vs 列」（看似一樣但角色互換）。
- **「行向量 $\mathbf{y}$ 與列向量 $\mathbf{y}^{\mathrm{T}}$ 可以互換」** — 數值資料同，但乘法位置不同：$\mathbf{y}A$ 需要橫躺、$A\mathbf{y}^{\mathrm{T}}$ 需要直立。**記得在程式裡管好 shape（`y.reshape(1,-1)` vs `y.reshape(-1,1)`）。**

**為什麼這張圖該做成互動視覺化？** 因為它與 Figure 3.1 的對偶結構是「**值得用一個動畫一次演完**」的點 — 看著 (Mv*) 和 (vM*) 同步切換，建立「左 / 右乘 = 行 / 列鏡像」直覺。但獨立 Figure 3.2 視覺化的價值次於 Figure 3.1，所以本書設計上把它合進 VizMark-01（與 Mv 共用畫面）或單獨做個輕量 VizMark（見 VizMark-03）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-03** [切換視角] ⭐⭐
> **位置：** Figure 3.2 / §3 / (vM1) ↔ (vM2) 對偶（與 Mv 鏡像）
> **核心概念：** 左乘 $\mathbf{y}A$ 的兩種視角結構完全對偶於右乘 $A\mathbf{x}$，行 / 列角色互換
> **互動梗概：** 與 VizMark-01 共畫面但 toggle 切到「左乘模式」 — 整個畫面從「向量在右上」翻轉到「向量在左下」，所有色塊（行 / 列）旋轉 90°
> **詳見劇本：** VizScript-03（章末）

---

### Figure 3.3: 四個基本子空間（The Four Subspaces）

**圖檔：** `docs/book/figs-png/4-Subspaces.png`（原始 EPS：`figs/4-Subspaces.eps`）
**原書頁碼：** p.3（圖以 8cm 寬呈現）
**所屬章節：** §3 結尾

#### 視覺結構 (Visual Structure)

此圖採「**左右兩塊大空間 + 中央上方箭頭**」結構，是本章（也是全書）視覺上最具標誌性的一張圖，俗稱「**Strang 兩塊大餅圖**」。

- **整體佈局：**
  - **中央上方：** 箭頭從左指向右，箭頭上方文字 $A \in \mathbb{R}^{m \times n}$，箭頭兩端分別標 $\mathbb{R}^n$（左）、$\mathbb{R}^m$（右）。
  - **左方塊：** 在 $\mathbb{R}^n$ 中的兩個子空間。
  - **右方塊：** 在 $\mathbb{R}^m$ 中的兩個子空間。
- **左方塊（$\mathbb{R}^n$）：**
  - **上半大區（傾斜長方形）：行空間 $\mathbf{C}(A^{\mathrm{T}})$**
    - 標籤：**$\mathbf{C}(A^{\mathrm{T}})$**、$\dim = r$
    - 內含文字 "row space"、"all $\mathbf{y}A$"
    - 區內畫**3 條粉紅色橫條**（對應 $A$ 的 3 個橫躺行作為行空間的生成元）。
  - **下半小區（傾斜小方形）：零空間 $\mathbf{N}(A)$**
    - 標籤：**$\mathbf{N}(A)$**、$\dim = n - r$
    - 內含文字 "nullspace"、"$A\mathbf{x} = \mathbf{0}$"
    - 區內無色塊填充（強調這是「會被 $A$ 抹平」的方向）。
  - **兩區交接處：** 直角符號 + 文字 "perpendicular"（**正交**）。
- **右方塊（$\mathbb{R}^m$）：**
  - **上半大區（傾斜長方形）：列空間 $\mathbf{C}(A)$**
    - 標籤：**$\mathbf{C}(A)$**、$\dim = r$
    - 內含文字 "column space"、"all $A\mathbf{x}$"
    - 區內畫**2 條綠色直條**（對應 $A$ 的 2 個直立列作為列空間的生成元）。
  - **下半小區（傾斜小方形）：左零空間 $\mathbf{N}(A^{\mathrm{T}})$**
    - 標籤：**$\mathbf{N}(A^{\mathrm{T}})$**、$\dim = m - r$
    - 內含文字 "left nullspace"、"$\mathbf{y}A = 0$"
    - 區內無色塊填充。
  - **兩區交接處：** 直角符號 + 文字 "perpendicular"。
- **底部正交分解公式：**
  - 左下：**$\mathbb{R}^n = \mathbf{N}(A) + \mathbf{C}(A^{\mathrm{T}})$**、**$\mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}})$**
  - 右下：**$\mathbb{R}^m = \mathbf{C}(A) + \mathbf{N}(A^{\mathrm{T}})$**、**$\mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}})$**
- **配色語意：**
  - **粉紅色橫條（$\mathbf{C}(A^{\mathrm{T}})$ 內）** = 橫躺行的家。
  - **綠色直條（$\mathbf{C}(A)$ 內）** = 直立列的家。
  - **兩個零空間區無色** = 「被擠到角落、會被抹平」的方向。
  - **方塊傾斜畫法** = 提示這些子空間不必對齊座標軸，是一般子空間。

讀者的視覺動線：先看中央上方的「$\mathbb{R}^n \xrightarrow{A} \mathbb{R}^m$」確認 $A$ 是函數 → 看左方塊知道「在 $\mathbb{R}^n$ 中，$\mathbf{x}$ 可分解成行空間部分 + 零空間部分」→ 看右方塊知道「在 $\mathbb{R}^m$ 中，輸出 $A\mathbf{x}$ 必落在列空間，左零空間是右側『額外』的維度」→ 對比兩塊的「大區 = 列空間 / 行空間」配色（綠 / 粉紅）強化「直立 vs 橫躺」記憶 → 底部公式收尾。

#### 數學內容 (Mathematical Content)

**四個子空間的精確定義與維度：**

| 子空間 | 符號 | 在哪個 $\mathbb{R}$ 裡 | 維度 | 生成元 |
|---|---|---|---|---|
| 列空間 (column space) | $\mathbf{C}(A)$ | $\mathbb{R}^m$ | $r$ | $A$ 的直立列（取最大線性獨立子集） |
| 零空間 (nullspace) | $\mathbf{N}(A)$ | $\mathbb{R}^n$ | $n - r$ | $A\mathbf{x} = \mathbf{0}$ 的所有解 |
| 行空間 (row space) | $\mathbf{C}(A^{\mathrm{T}})$ | $\mathbb{R}^n$ | $r$ | $A$ 的橫躺行（取最大線性獨立子集） |
| 左零空間 (left nullspace) | $\mathbf{N}(A^{\mathrm{T}})$ | $\mathbb{R}^m$ | $m - r$ | $\mathbf{y}A = \mathbf{0}$ 的所有解 |

**正交互補（基本定理 / Fundamental Theorem of Linear Algebra Part 2）：**

$$
\mathbf{C}(A^{\mathrm{T}}) \;=\; \mathbf{N}(A)^\perp, \qquad \mathbf{C}(A) \;=\; \mathbf{N}(A^{\mathrm{T}})^\perp
$$

且兩個方向皆有**直和分解 (orthogonal direct sum decomposition)**：

$$
\mathbb{R}^n \;=\; \mathbf{C}(A^{\mathrm{T}}) \oplus \mathbf{N}(A), \qquad \mathbb{R}^m \;=\; \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}})
$$

**正交性的兩行證明：**
- 設 $\mathbf{v} \in \mathbf{N}(A)$ 則 $A\mathbf{v} = \mathbf{0}$。把這個式子展開（用 Mv1 視角）：$A$ 每一橫躺行 $\mathbf{a}^*_i$ 與 $\mathbf{v}$ 的點積為 0，所以 $\mathbf{v} \perp$ 任一橫躺行。因為行空間由橫躺行張成，$\mathbf{v} \perp \mathbf{C}(A^{\mathrm{T}})$。 ✓
- 對偶：$\mathbf{y} \in \mathbf{N}(A^{\mathrm{T}})$ → $\mathbf{y}A = 0$ → $\mathbf{y}$ 與 $A$ 每一直立列點積為 0 → $\mathbf{y} \perp \mathbf{C}(A)$。 ✓

**維度關係（Rank-Nullity Theorem）：**

$$
\dim \mathbf{C}(A) + \dim \mathbf{N}(A) \;=\; n \quad (\text{由秩 } r + (n-r) = n)
$$

$$
\dim \mathbf{C}(A^{\mathrm{T}}) + \dim \mathbf{N}(A^{\mathrm{T}}) \;=\; m \quad (\text{由秩 } r + (m-r) = m)
$$

**關鍵奇蹟（row rank = column rank）：** $\dim \mathbf{C}(A) = \dim \mathbf{C}(A^{\mathrm{T}}) = r$ — 雖然這兩個子空間住在不同維度的空間（$\mathbb{R}^m$ 與 $\mathbb{R}^n$），但**維度恰好相同**。這個事實是線性代數最深刻的對稱之一，是 SVD 的存在性背後的核心（§6.5）。

#### 直覺解讀 (Intuition)

**1. $A$ 是 $\mathbb{R}^n \to \mathbb{R}^m$ 的映射，但它只「看見」一個 $r$ 維的方向。** $\mathbf{x}$ 的「行空間部分」$\mathbf{x}_r \in \mathbf{C}(A^{\mathrm{T}})$ 是 $A$ 真正「處理」的部分（會被映射到 $\mathbf{C}(A)$ 中的某個向量）；$\mathbf{x}$ 的「零空間部分」$\mathbf{x}_n \in \mathbf{N}(A)$ 則被 $A$ **完全抹平**（映射到 $\mathbf{0}$）。

$$
\mathbf{x} \;=\; \underbrace{\mathbf{x}_r}_{\in \mathbf{C}(A^{\mathrm{T}})} + \underbrace{\mathbf{x}_n}_{\in \mathbf{N}(A)}, \qquad A\mathbf{x} \;=\; A\mathbf{x}_r + \underbrace{A\mathbf{x}_n}_{= \mathbf{0}} \;=\; A\mathbf{x}_r
$$

**2. 為什麼右邊 $\mathbf{C}(A)$ 是大區，$\mathbf{N}(A^{\mathrm{T}})$ 是小區？** 因為 $A$ 的「**輸出能力**」就是 $\mathbf{C}(A)$ — 這個子空間維度為 $r$。$\mathbf{N}(A^{\mathrm{T}})$ 是右邊「**$A$ 摸不到的方向**」 — 若 $\mathbf{b} \in \mathbf{N}(A^{\mathrm{T}})$，則任何 $A\mathbf{x}$ 都不等於 $\mathbf{b}$（除非 $\mathbf{b} = \mathbf{0}$），因為它與每一直立列都垂直。$\mathbf{N}(A^{\mathrm{T}})$ 是「**$A\mathbf{x} = \mathbf{b}$ 無解的方向**」。

**3. $A\mathbf{x} = \mathbf{b}$ 的解的結構，全在這張圖裡。**
- **存在性：** $\mathbf{b} \in \mathbf{C}(A)$ ⟺ 有解。等價於 $\mathbf{b}$ 在右方塊上半大區內。
- **唯一性：** 解唯一 ⟺ $\mathbf{N}(A) = \{\mathbf{0}\}$ ⟺ 左方塊下半小區只有原點 ⟺ $r = n$（直立列線性獨立）。
- **若有解但不唯一：** 通解為「一個特解 $\mathbf{x}_p$」+「零空間 $\mathbf{N}(A)$ 中任意向量 $\mathbf{x}_n$」 — 即解集是 $\mathbb{R}^n$ 中與 $\mathbf{N}(A)$ 平行的一個 affine 子空間。

**4. 投影 / 最小二乘 / SVD 都是這張圖的延伸。**
- **投影：** 若 $\mathbf{b} \notin \mathbf{C}(A)$（無解），找 $\mathbf{C}(A)$ 中最接近 $\mathbf{b}$ 的點 $\hat{\mathbf{b}}$ — 等價於把 $\mathbf{b}$ 沿 $\mathbf{N}(A^{\mathrm{T}})$ 方向投到 $\mathbf{C}(A)$。
- **最小二乘解：** $\hat{\mathbf{x}} = (A^{\mathrm{T}}A)^{-1} A^{\mathrm{T}} \mathbf{b}$，本質是把 $\mathbf{b}$ 投影到 $\mathbf{C}(A)$ 後再「逆映射」到 $\mathbf{C}(A^{\mathrm{T}})$。
- **SVD：** $A = U\Sigma V^{\mathrm{T}}$ 直接把這張圖的「兩對正交分解」對齊 — $V$ 的前 $r$ 列構成 $\mathbf{C}(A^{\mathrm{T}})$ 的標準正交基底、$U$ 的前 $r$ 列構成 $\mathbf{C}(A)$ 的標準正交基底（§6.5 詳述）。

**5. 為何稱「**Strang 的兩塊大餅**」？** Gilbert Strang 在 *Linear Algebra and Its Applications* 與 *Linear Algebra for Everyone* 中反覆畫這張圖（不同版本略有差異），把它稱為「**Linear Algebra in a Picture**」 — 因為大多數線性代數核心定理（rank-nullity / fundamental theorem / least squares / SVD）都可以從這張圖直接讀出。在本書 Hiranabe 的版本配色更鮮明，視覺辨識度更高。

**常見誤解警示：**
- **「四個子空間都在 $\mathbb{R}^n$ 或都在 $\mathbb{R}^m$」** — 否，$\mathbb{R}^n$ 中只有 $\mathbf{C}(A^{\mathrm{T}})$ 與 $\mathbf{N}(A)$，$\mathbb{R}^m$ 中只有 $\mathbf{C}(A)$ 與 $\mathbf{N}(A^{\mathrm{T}})$。「列空間」住在「列向量所在的空間」（$\mathbb{R}^m$）才合理。
- **「$\mathbf{C}(A^{\mathrm{T}}) = \mathbf{C}(A)$」** — 否，兩者一個在 $\mathbb{R}^n$ 一個在 $\mathbb{R}^m$，**只有維度相同（都是 $r$）**，子空間本身不同。
- **「零空間是『$A$ 沒有意義的方向』」** — 不嚴謹，正確說法是「$A$ 把它抹平到 $\mathbf{0}$ 的方向」。在最小二乘 / 投影應用中，零空間對應「**不影響輸出的自由度**」（如冗餘參數）。

**為什麼這張圖該做成互動視覺化？** 因為「**拉動 $A$ 的某個元素看四個子空間維度即時變化（並隨秩降低看 $\mathbf{N}(A)$ 從點長成線、列空間從平面塌成線）**」是動態的，遠比靜態圖直觀。另外把 $\mathbf{x}$ 在 $\mathbb{R}^n$ 中拉動、看 $\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$ 即時分解、再看 $A\mathbf{x}$ 在右方塊跑到哪 — 這個「**雙向跨空間流動動畫**」是線性代數教學最有價值的視覺化之一（見 VizMark-02，本書 ⭐⭐⭐ 第一名）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-02** [3D 空間幾何 + 拉桿調參] ⭐⭐⭐
> **位置：** Figure 3.3 / §3 / 四個基本子空間
> **核心概念：** $\mathbb{R}^n = \mathbf{C}(A^{\mathrm{T}}) \oplus \mathbf{N}(A)$、$\mathbb{R}^m = \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}})$，兩對正交分解；$\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$ 後 $A\mathbf{x} = A\mathbf{x}_r$
> **互動梗概：** 左右兩個 3D 視窗（$\mathbb{R}^3$ as $\mathbb{R}^n$ / $\mathbb{R}^3$ as $\mathbb{R}^m$），中央拉動 $A$ 的元素 slider。左視窗顯示 $\mathbf{C}(A^{\mathrm{T}})$（平面或直線）+ $\mathbf{N}(A)$（補的直線或點）+ 用戶可拖曳的 $\mathbf{x}$ 箭頭即時分解成 $\mathbf{x}_r + \mathbf{x}_n$；右視窗顯示 $\mathbf{C}(A)$ + $\mathbf{N}(A^{\mathrm{T}})$ + $A\mathbf{x}$ 軌跡。秩變化時兩邊子空間維度動畫平滑過渡。
> **詳見劇本：** VizScript-02（章末，⭐⭐⭐ 最詳細版本）

---

## 視覺化劇本（VizScripts）

> 本章 4 個 VizMark 對應 4 個 VizScript。格式遵 `VIZ_SCHEMA.md` §2（A–M 共 13 段）。
> ⭐⭐⭐ 兩支（VizScript-01 / 02）寫到完整 13 段詳細劇本；⭐⭐ 一支（VizScript-03）寫到中等詳度；⭐ 一支（VizScript-04）寫到輕量輪廓即可。
> 4 支劇本可合成單一視覺化頁面（共用控制列與畫布切換 tab），不必拆 4 支獨立程式。

### VizScript-01: Mv1 ↔ Mv2 視角切換（Dot Way vs Linear Combination Way）

#### A. 一句話定位
讓使用者 toggle 切換 (Mv1) / (Mv2)，看同一個 $A\mathbf{x}$ 同時被「逐橫躺行做點積堆疊」與「直立列加權線性組合」兩種視角呈現。

#### B. 學習目標（Learning Outcome）
- 使用者能說出 (Mv1) $A\mathbf{x}$ 的第 $i$ 個分量是 $A$ 第 $i$ 橫躺行 · $\mathbf{x}$。
- 使用者能說出 (Mv2) $A\mathbf{x} = x_1 \mathbf{a}_1 + \cdots + x_n \mathbf{a}_n$ 是直立列的線性組合。
- 使用者能驗證兩種視角計算的結果完全一致（逐分量比對動畫）。
- 使用者能解釋「(Mv2) 視角告訴我們 $A\mathbf{x}$ 必落在 $\mathbf{C}(A)$」。
- 使用者能在拉 $\mathbf{x}$ 分量時即時觀察「(Mv1) 點積值如何變」與「(Mv2) 列縮放動畫」。

#### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$、列向量 $\mathbf{x} \in \mathbb{R}^n$、結果 $\mathbf{b} = A\mathbf{x} \in \mathbb{R}^m$。
- **預設值：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（與原書 Figure 3 一致）、$\mathbf{x} = (1, 1)^{\mathrm{T}}$、$m = 3$、$n = 2$。
- **維度範圍：** $m \in [2, 6]$、$n \in [2, 6]$。
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1、$x_j \in [-9, 9]$ 步進 1（沿用 §1 §2）。
- **退化情形：**
  - **$\mathbf{x} = \mathbf{0}$：** 結果全 0，兩種視角都示範「點積全 0」與「線性組合係數全 0」。
  - **某 $x_j = 0$：** (Mv2) 對應的直立列「縮放係數 0」灰掉。
  - **$A$ 某直立列為零：** 該列不參與 (Mv2) 加總；視角切換時該列灰底。
  - **$A$ 秩 < $n$：** 在資訊區提示 "rank deficient: 列空間維度 = ?"。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 70% 主畫面、下 30% 控制列 + 公式區。
- **主畫面尺寸：** 900×480 px，白底；分割成「左 35%（$A$ 與 $\mathbf{x}$）+ 中 10%（`=`）+ 右 35%（結果 $\mathbf{b}$）+ 右側 20%（資訊框）」。
- **(Mv1) 模式排列：**
  - 左 35%：$A$ 顯示為 $m$ 條粉紅色橫條堆疊（每條 240×40 px、間隔 8px），右側緊鄰綠色直條 $\mathbf{x}$（80×$m\cdot 48$ px）。
  - 中 10%：大號 `=` 等號。
  - 右 35%：結果列向量 $\mathbf{b}$，畫成 $m$ 條粉紅色橫條，每條中段（綠色覆蓋部分）顯示計算數值。
- **(Mv2) 模式排列：**
  - 左 35%：$A$ 顯示為 $n$ 條綠色直條並列（每條 48×240 px、間隔 8px），上方緊鄰 $n$ 個藍色實心圓點橫排 $\mathbf{x}$。
  - 中 10%：大號 `=` 等號。
  - 右 35%：拆成「藍點 × 綠直條 + 藍點 × 綠直條 + ...」共 $n$ 項，每兩項間用大 `+` 號連接；最右側出現「= 結果列向量」的綠直條 + 數值。
- **資訊框（右側 20%）：**
  - 上半：當前模式 badge（"Mv1: Dot Product Way" / "Mv2: Linear Combination Way"），底色綠 / 藍切換。
  - 中半：當前算式逐分量展開（用 MathJax 即時渲染）。
  - 下半：「列空間提示」`A·x always lies in C(A) ⊂ R^m`（綠字，僅 (Mv2) 模式顯示）。
- **配色：** 沿用全書錨點 — 綠 `#2ca02c`（列 / 直立）、粉紅 `#d62728`（行 / 橫躺）、藍點 `#1f77b4`（$\mathbf{x}$ 分量）、灰 `#eeeeee`（背景填充）、文字 `#000`。
- **字型 / 字級：** 公式區 16pt MathJax、cell 內數字 14pt monospace、模式 badge 18pt sans bold、提示 12pt sans。
- **邊距：** 上下 20px、左右 24px、cell 間距 4px。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 | toggle | Mv1 / Mv2 | Mv1 | 即時（含 600ms 動畫過渡） |
| $m$ | slider | [2, 6] step 1 | 3 | 即時 |
| $n$ | slider | [2, 6] step 1 | 2 | 即時 |
| $a_{ij}$ ($i\!=\!1..m$, $j\!=\!1..n$) | slider grid ($m \times n$) | [-9, 9] step 1 | 原書值 | 即時 |
| $x_j$ ($j\!=\!1..n$) | slider 橫排 | [-9, 9] step 1 | $(1, 1, \ldots)$ | 即時 |
| 公式逐項高亮 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click → 還原預設 |

#### F. 輸出畫面細節（Outputs）
- **(Mv1) 模式輸出：**
  - 結果區每一橫躺行中段顯示「$\sum_{k=1}^{n} a_{ik} x_k$」具體數字（如「$1 \cdot 1 + 2 \cdot 1 = 3$」），公式區同步逐項展開。
  - hover 結果某行 → 對應 $A$ 該橫躺行 + $\mathbf{x}$ 整條 highlight 加粗外框，視覺連結「這個分量來自哪個 dot product」。
- **(Mv2) 模式輸出：**
  - 中段 `=` 右側依序顯示 `$x_1$ × [$\mathbf{a}_1$] + $x_2$ × [$\mathbf{a}_2$] + ...`，每項中綠直條長度按 $|x_j|$ 等比例縮放、$x_j < 0$ 時直條翻轉並底色變淺；最後一項後面接「`=`」與結果綠直條。
  - hover 某項 $x_j \mathbf{a}_j$ → 該項加粗、其他項半透明 0.3；右側結果區也同步以該項顏色「箭頭尾接頭」動畫畫一段。
- **公式區：** 即時 LaTeX，$A\mathbf{x} = \cdots$（依模式顯示 Mv1 或 Mv2 展開）。

#### G. 互動行為（Interactions）
- **toggle Mv1 ↔ Mv2：** 觸發轉視角動畫（見 §H）；公式區同步切換。
- **拉動 $a_{ij}$ slider：** 立即重算結果。(Mv1) 模式下對應第 $i$ 橫躺行內第 $j$ 個元素亮一下；(Mv2) 模式下對應第 $j$ 直立列內第 $i$ 元素亮一下。
- **拉動 $x_j$ slider：**
  - (Mv1) 模式：所有橫躺行的點積結果同時重算，結果分量用淡黃色閃 200ms。
  - (Mv2) 模式：第 $j$ 直立列的「縮放動畫」即時放大 / 縮小（高度按 $|x_j| / 9 \cdot 240$ px 縮放），最終結果直條同步重畫。
- **hover cell / hover 結果分量：** 見 §F。
- **快捷鍵：** `1` → Mv1、`2` → Mv2、`Space` → toggle、`R` → reset、`H` → 公式逐項高亮 toggle。

#### H. 動畫腳本（Mv1 ↔ Mv2 視角切換）
- **從 Mv1 → Mv2：**
  - **t=0：** Mv1 穩態（$A$ 顯為粉紅橫條堆、$\mathbf{x}$ 為綠直條）。
  - **t=0–200ms：** 結果區所有粉紅橫條 fade out（opacity 1 → 0）。
  - **t=200–500ms：** 左區的 $A$ 從「橫躺行堆疊」翻轉成「直立列並列」 — 動畫實作上是把每一橫躺行的色塊**旋轉 90° + 換色（粉紅 → 綠）**，同時 $\mathbf{x}$ 從右側「直立綠」**旋轉 90° + 換色（綠 → 藍點橫排）**移到 $A$ 上方。
  - **t=500–800ms：** 右區依次淡入 $n$ 個 `$x_j$ × 綠直條` 項（每項 stagger 60ms 從中心放大到正常大小），各項之間 `+` 號淡入。
  - **t=800ms 後：** Mv2 穩態。
- **從 Mv2 → Mv1：** 反向重播。
- **總長度：** 800ms。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。
- **暫停 / 倒轉：** 是（動畫進行中按 toggle 立即 reverse；按 Esc 凍結在當前 frame）。

#### I. 邊界與錯誤處理
- **$m = n = 6$ 大尺寸：** 直條 / 橫條尺寸自動縮為 36×120 px；slider grid 改為可摺疊 panel 避免擠版。
- **動畫進行中再切換：** debounce 100ms 或佇列；防止狀態錯亂。
- **$\mathbf{x} = \mathbf{0}$：** 結果區所有元素顯示 `0`，背景轉淡灰；(Mv2) 模式下所有藍點變灰、所有直條變淺。
- **$A$ 某直立列全 0：** (Mv2) 該列灰掉並顯示「dead column → 不貢獻列空間」；(Mv1) 該列下的所有 $a_{ij}$ slider 標 `0` 灰底。
- **拖動 slider 過快：** debounce 30ms 避免重畫風暴；動畫 throttle 至 60fps。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - Mv1 toggle：「每一橫躺行各自做 dot product，堆成結果」
  - Mv2 toggle：「$\mathbf{x}$ 的每個分量縮放對應直立列，疊加成結果 — 這就是『$A\mathbf{x}$ 在 $\mathbf{C}(A)$ 內』的證明」
  - 公式逐項高亮 checkbox：「滑鼠移到某項，自動 highlight 對應的色塊與分量」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在是 Mv1：每條粉紅橫躺行是 $A$ 的一行，與綠色直立 $\mathbf{x}$ 做 dot product」
  - Step 2：「右邊結果的每個粉紅橫條中段顯示 dot product 數值 — 共 $m$ 個分量」
  - Step 3：「按右下 toggle 切到 Mv2」
  - Step 4：「現在 $A$ 攤成 $n$ 個直立列，$\mathbf{x}$ 的每個分量決定『該列要放大幾倍』」
  - Step 5：「右邊把 $n$ 個放大後的列『箭頭尾接頭』加起來 — 永遠落在 $A$ 的列空間 $\mathbf{C}(A)$」
  - Step 6：「拉 $x_1$ slider 看看第 1 個直立列同步縮放，感受『線性組合』的動態」
- **常見誤解警示：**
  - 「Mv1 和 Mv2 不是不同的『算法』，是同一個運算的兩種讀法」
  - 「Mv2 的『線性組合係數』就是 $\mathbf{x}$ 本身，不需另外算」
- **延伸閱讀：** 原書 p.3、`ch03-mat-vec.md` 數學要點、Strang LAFE Sec. 1.1 + 1.3。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo（反應式 notebook）+ matplotlib + `matplotlib.animation.FuncAnimation`（控制視角切換動畫）+ marimo.ui。
- **替代方案：** Streamlit + Plotly + custom JS（如需高品質瀏覽器分享，旋轉換色用 CSS transform + filter）。
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫粉紅橫條 / 綠直條
  - `matplotlib.transforms.Affine2D().rotate_deg_around()` 做橫 ↔ 直旋轉
  - `marimo.ui.slider`、`marimo.ui.switch`（toggle）、`marimo.ui.array`（slider grid）
  - `numpy.dot(A, x)` 計算結果
- **檔案結構：**
  ```
  viz/
    ch03_matrix_vector.py        # 主入口（含 VizScript-01 / 02 / 03 / 04 共用畫面 tab 切換）
    _common/
      palette.py                 # 沿用 §1 §2 配色
      vector_canvas.py           # §2 已建，§3 直接 import
      subspace_3d.py             # 新增：3D 子空間繪製（給 VizScript-02 用）
  ```
- **效能：** 動畫期間預先計算所有 frame 的色塊座標 / 顏色，存 list；動畫結束後切回 reactive。Slider 拖動以 30ms debounce。
- **測試：** 動畫關鍵 frame（t=0 / 200 / 500 / 800）各 1 張 snapshot；預設值 Mv1 / Mv2 各 1 張靜態 snapshot；退化（$\mathbf{x} = \mathbf{0}$）1 張。

#### L. 驗收標準（Acceptance Criteria）
- [ ] Mv1 ↔ Mv2 toggle 動畫總長 ≤ 800ms，60fps 無 frame drop。
- [ ] 拉 $x_j$ slider 在 (Mv2) 模式下，第 $j$ 直立列縮放動畫 200ms 平滑完成。
- [ ] hover 結果分量 → 對應 $A$ 行 / 列正確高亮（Mv1 高亮整橫躺行、Mv2 高亮整直立列）。
- [ ] 公式區 LaTeX 渲染 < 50ms 完成。
- [ ] $\mathbf{x} = \mathbf{0}$ 或 $A$ 某直立列為 0 時顯示對應退化提示。
- [ ] Walkthrough 6 步驟首次開啟自動觸發，可關閉並有「再看一次」按鈕。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純並列兩種視角靜態圖，無動畫。
- **Tier 3 擴充：** + 加 3D 視窗即時畫 $A\mathbf{x}$ 在 $\mathbf{C}(A)$ 平面上的位置（與 VizScript-04 部分合併）。
- **估時：** 1.5 session（含測試與 walkthrough）

---

### VizScript-02: 四個基本子空間互動式（Four Subspaces Interactive — Strang's Big Picture）

#### A. 一句話定位
左右兩個 3D 視窗分別展示 $\mathbb{R}^n$ 與 $\mathbb{R}^m$ 中的「行空間 ⊕ 零空間」與「列空間 ⊕ 左零空間」，使用者拖曳 $\mathbf{x}$ 看 $\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$ 即時分解、$A\mathbf{x}$ 在右視窗即時定位，並可拉 $A$ 元素看子空間維度隨秩變化。

#### B. 學習目標（Learning Outcome）
- 使用者能指認 $\mathbb{R}^n$ 中「行空間 $\mathbf{C}(A^{\mathrm{T}})$」與「零空間 $\mathbf{N}(A)$」兩個正交互補子空間。
- 使用者能指認 $\mathbb{R}^m$ 中「列空間 $\mathbf{C}(A)$」與「左零空間 $\mathbf{N}(A^{\mathrm{T}})$」兩個正交互補子空間。
- 使用者能驗證 $\dim \mathbf{C}(A) = \dim \mathbf{C}(A^{\mathrm{T}}) = r$（即使所在空間不同）。
- 使用者能在拖曳 $\mathbf{x}$ 時看出 $\mathbf{x}_r \in \mathbf{C}(A^{\mathrm{T}})$、$\mathbf{x}_n \in \mathbf{N}(A)$，並 $A\mathbf{x} = A\mathbf{x}_r$（零空間部分被抹平）。
- 使用者能在拉 $A$ 元素降秩時看出列空間從平面塌成直線、零空間從點 / 線長成線 / 面（維度補償）。
- 使用者能說出「為什麼右方塊上半（$\mathbf{C}(A)$）這麼重要 — 因為它是『$A\mathbf{x} = \mathbf{b}$ 有解 ⟺ $\mathbf{b}$ 在這裡』的關鍵」。

#### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$（限 $m, n \in \{2, 3\}$ 以便 3D 視覺化），$\mathbf{x} \in \mathbb{R}^n$，$\mathbf{x}_r \in \mathbf{C}(A^{\mathrm{T}})$，$\mathbf{x}_n \in \mathbf{N}(A)$，$A\mathbf{x} \in \mathbf{C}(A)$，4 個子空間（每個是 $\mathbb{R}^n$ / $\mathbb{R}^m$ 中的直線 / 平面 / 點）。
- **預設值：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（$m=3, n=2$，秩 = 2），$\mathbf{x} = (1, 1)^{\mathrm{T}}$。預設秩 = 2 讓零空間是 $\{\mathbf{0}\}$、$\mathbf{C}(A^{\mathrm{T}}) = \mathbb{R}^2$（整個左視窗平面）、$\mathbf{C}(A)$ 是 $\mathbb{R}^3$ 中的某個平面。
- **維度範圍：** $m \in \{2, 3\}$、$n \in \{2, 3\}$。
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1。
- **退化情形：**
  - **$A = 0$：** 全部子空間退化（$\mathbf{C}(A) = \{0\}$、$\mathbf{N}(A) = \mathbb{R}^n$ 整個），動畫平滑塌縮。
  - **$r = 1$：** $\mathbf{C}(A)$ 是直線、$\mathbf{N}(A)$ 維度增為 $n-1$。
  - **$\mathbf{x} \in \mathbf{N}(A)$：** $A\mathbf{x} = \mathbf{0}$，右視窗 $A\mathbf{x}$ 標籤標 "annihilated"。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 75%（左 45% 左視窗 + 中 10% 連接動畫 + 右 45% 右視窗）+ 下 25% 控制列。
- **左視窗（$\mathbb{R}^n$，3D matplotlib axes）：** 600×480 px，背景白；座標軸標 $e_1, e_2, e_3$（若 $n=3$）；行空間 $\mathbf{C}(A^{\mathrm{T}})$ 以**粉紅色半透明平面 / 直線**繪製、零空間 $\mathbf{N}(A)$ 以**灰色虛線直線 / 點**繪製；用戶拖曳的 $\mathbf{x}$ 為**藍色箭頭**從原點出發、分解後的 $\mathbf{x}_r$（粉紅實心箭頭）與 $\mathbf{x}_n$（灰色虛線箭頭）平行四邊形連接。
- **右視窗（$\mathbb{R}^m$，3D matplotlib axes）：** 600×480 px，同樣設定；列空間 $\mathbf{C}(A)$ 以**綠色半透明平面 / 直線**繪製、左零空間 $\mathbf{N}(A^{\mathrm{T}})$ 以**灰色虛線**繪製；結果 $A\mathbf{x}$ 為**藍色箭頭**從原點出發、其端點與 $\mathbf{x}_r$ 經 $A$ 映射的位置一致。
- **中央連接（10%）：** 上方文字 $A$ 與箭頭 $\to$；中段顯示「$\mathbf{x} \mapsto A\mathbf{x}$」與「$\mathbf{x}_n \mapsto \mathbf{0}$」兩條動畫光線（拖曳時 $\mathbf{x}$ 沿光線從左飛到右）。
- **控制列（下 25%）：**
  - 左：$A$ 元素 slider grid（$m \times n$ 個）+ $m, n$ slider。
  - 中：模式 radio（"All Subspaces" / "Only $\mathbf{C}(A^{\mathrm{T}}) \oplus \mathbf{N}(A)$" / "Only $\mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}})$"）。
  - 右：「$\mathbf{x}$ 自動掃描」button（讓 $\mathbf{x}$ 自動轉一圈 360° 看 $A\mathbf{x}$ 在 $\mathbf{C}(A)$ 上的軌跡）+ 「reset」。
- **配色：** $\mathbf{C}(A^{\mathrm{T}})$ 粉紅 `#d62728` alpha 0.3、$\mathbf{C}(A)$ 綠 `#2ca02c` alpha 0.3、$\mathbf{N}(A)$ 與 $\mathbf{N}(A^{\mathrm{T}})$ 灰 `#888888` 虛線、$\mathbf{x}$ 藍 `#1f77b4`、$A\mathbf{x}$ 藍 `#1f77b4`、$\mathbf{x}_r$ 粉紅實心、$\mathbf{x}_n$ 灰虛線、座標軸黑。
- **字型 / 字級：** 子空間標籤 14pt bold sans、座標軸 10pt、控制列 12pt。
- **邊距：** 視窗間距 12px、整體 padding 20px。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| $m$ | radio | 2 / 3 | 3 | 即時 |
| $n$ | radio | 2 / 3 | 2 | 即時 |
| $a_{ij}$ | slider grid | [-9, 9] step 1 | 原書值 | 即時 |
| $\mathbf{x}$（拖曳） | 3D drag | $\mathbb{R}^n$ 中任意 | $(1, 1, 0)$ | 即時 |
| 模式 | radio | All / Left only / Right only | All | 即時 |
| 顯示分解 | checkbox | $\mathbf{x}_r + \mathbf{x}_n$ 平行四邊形 | on | 即時 |
| 自動掃 $\mathbf{x}$ | button | — | — | click → 4 秒 360° 旋轉 |
| 顯示秩 | toggle | on / off | on | 即時 |
| reset | button | — | — | — |

#### F. 輸出畫面細節（Outputs）
- **左視窗：**
  - 行空間平面 / 直線（粉紅）半透明填充。
  - 零空間 / 點 / 直線（灰虛線）。
  - 拖曳的 $\mathbf{x}$ 藍色實心箭頭。
  - $\mathbf{x}_r$ 粉紅實心、$\mathbf{x}_n$ 灰虛線（兩者尾接 $\mathbf{x}$ 端點，組成平行四邊形）。
  - 上方文字 `R^n: dim C(A^T) = r = ?, dim N(A) = n-r = ?`。
- **右視窗：**
  - 列空間平面 / 直線（綠）。
  - 左零空間（灰虛線）。
  - $A\mathbf{x}$ 藍色實心箭頭（端點落在綠色面 / 線內）。
  - 上方文字 `R^m: dim C(A) = r = ?, dim N(A^T) = m-r = ?`。
- **資訊區（中央底部）：** 即時 LaTeX
  - $\mathbf{x} = \mathbf{x}_r + \mathbf{x}_n$（顯示具體數值）
  - $A\mathbf{x} = A\mathbf{x}_r$（驗證零空間被抹平）
  - $\operatorname{rank}(A) = r$
- **驗證提示：** 動畫顯示「$\mathbf{x}_r \perp \mathbf{x}_n$」「$A\mathbf{x} \perp \mathbf{N}(A^{\mathrm{T}})$」兩個垂直記號。

#### G. 互動行為（Interactions）
- **拖曳 $\mathbf{x}$（左視窗）：**
  - 即時計算 $\mathbf{x}_r = \mathrm{proj}_{\mathbf{C}(A^{\mathrm{T}})}(\mathbf{x})$、$\mathbf{x}_n = \mathbf{x} - \mathbf{x}_r$。
  - 平行四邊形即時重畫。
  - 右視窗 $A\mathbf{x}$ 箭頭即時更新（從 $A\mathbf{x}_r$ 計算 — 因為 $A\mathbf{x}_n = 0$，數值上等同 $A\mathbf{x}$ 但概念上強調「只有 $\mathbf{x}_r$ 部分貢獻」）。
  - 飛行動畫：拖曳暫停 500ms 後，自動播放一個「$\mathbf{x}$ 從左視窗『沿映射光線』飛到右視窗變成 $A\mathbf{x}$」的軌跡動畫（700ms）。
- **拉 $a_{ij}$ slider：** 即時重算秩、所有子空間（粉紅 / 綠平面 / 直線重畫，並用「平面 → 直線」平滑動畫 600ms 表現維度變化）；左 / 右視窗的子空間自動更新標籤。
- **點「自動掃 $\mathbf{x}$」：** $\mathbf{x}$ 在左視窗的 $\mathbf{C}(A^{\mathrm{T}})$ 平面上以單位圓沿著平面繞 360°（4 秒）；右視窗 $A\mathbf{x}$ 同步在 $\mathbf{C}(A)$ 內畫出對應軌跡（橢圓 / 直線）；軌跡淡化保留 2 秒讓使用者看到全貌。
- **模式切換：** 隱藏 / 顯示對應視窗的子空間平面，但保留箭頭。
- **快捷鍵：** `A` 切到「All」、`L` 左視窗 only、`R` 右視窗 only、`Space` 自動掃 $\mathbf{x}$、`0` reset。

#### H. 動畫腳本（秩變化的子空間維度過渡）
- **拉 $a_{ij}$ 導致秩從 $r$ 降到 $r-1$：**
  - **t=0：** $\mathbf{C}(A)$ 是平面（$r=2$ 在 $\mathbb{R}^3$ 中）。
  - **t=0–300ms：** 平面**朝其中一個方向縮窄**（沿 $\mathbf{C}(A)$ 中即將被抹去的方向），最終塌成直線（$r=1$）。實作上：取秩 $r-1$ 的最大線性獨立子集對應的方向作為「保留方向」，朝其他方向縮窄。
  - **t=300–600ms：** 同時左視窗 $\mathbf{N}(A)$ 從點長成直線、右視窗 $\mathbf{N}(A^{\mathrm{T}})$ 從點長成直線（維度補償）。動畫從原點向外擴展。
- **總長度：** 600ms。
- **緩動：** ease-in-out。
- **暫停 / 倒轉：** 是（slider 回拉立即反向動畫）。

#### I. 邊界與錯誤處理
- **$m = n = 3$ 且 $A$ 滿秩：** $\mathbf{C}(A)$ 是整個 $\mathbb{R}^3$（畫成淡綠 alpha 0.15 充滿視窗）、$\mathbf{N}(A^{\mathrm{T}}) = \{\mathbf{0}\}$ 只顯示原點記號。
- **$A = \mathbf{0}$：** 警示文字 "$A$ 為零矩陣 — 所有 $\mathbf{x}$ 都在 $\mathbf{N}(A)$" 出現 3 秒。
- **3D 視窗旋轉 / 縮放：** 拖曳視窗背景（不是箭頭）做相機旋轉；滾輪縮放。預設視角 elevation = 25°、azimuth = -60°。
- **$\mathbf{x}$ 拖出視窗範圍：** 限制 $\|\mathbf{x}\|_\infty \le 9$；超過時箭頭縮回邊界。
- **計算密集（拖動 + 自動掃同時）：** 取消上一個自動掃任務。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - $\mathbf{C}(A^{\mathrm{T}})$ 標籤：「行空間 — 所有 $A$ 橫躺行的線性組合所成的子空間」
  - $\mathbf{N}(A)$ 標籤：「零空間 — 所有滿足 $A\mathbf{x} = \mathbf{0}$ 的 $\mathbf{x}$」
  - $\mathbf{x}_r$ 箭頭：「$\mathbf{x}$ 在行空間中的分量 — 這部分被 $A$ 真正『映射』」
  - $\mathbf{x}_n$ 箭頭：「$\mathbf{x}$ 在零空間中的分量 — 這部分被 $A$ 抹平」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「左邊是 $\mathbb{R}^n$，所有可能的 $\mathbf{x}$ 都住在這裡」
  - Step 2：「粉紅色平面是『行空間 $\mathbf{C}(A^{\mathrm{T}})$』— $A$ 真正『處理』的方向」
  - Step 3：「灰色直線是『零空間 $\mathbf{N}(A)$』— $A$ 把它抹平」
  - Step 4：「拖曳藍色 $\mathbf{x}$ 看它分解成粉紅 $\mathbf{x}_r$ + 灰 $\mathbf{x}_n$」
  - Step 5：「右邊是 $\mathbb{R}^m$，結果 $A\mathbf{x}$ 永遠落在綠色『列空間 $\mathbf{C}(A)$』內」
  - Step 6：「拉 $A$ 的某個元素讓秩降低，看子空間維度動畫切換」
  - Step 7：「按『自動掃 $\mathbf{x}$』，看 $\mathbf{x}$ 繞行空間一圈，$A\mathbf{x}$ 同步在列空間裡跑」
- **常見誤解警示：**
  - 「行空間和列空間不是同一個子空間 — 它們住在不同維度的空間（$\mathbb{R}^n$ vs $\mathbb{R}^m$），但**維度恰好相等**」
  - 「秩 = 行 / 列獨立向量個數 = $\mathbf{C}(A^{\mathrm{T}})$ 維度 = $\mathbf{C}(A)$ 維度」
  - 「零空間和左零空間不對稱 — 一個在 $\mathbb{R}^n$、一個在 $\mathbb{R}^m$」
- **延伸閱讀：** Strang LAFE Sec. 3.5 (p.124) 四子空間維度定理；原書 p.3 Figure 5；本書 §6.5 SVD 把這張圖完整對齊。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib 3D（`mpl_toolkits.mplot3d`）+ marimo.ui + custom drag handler（用 `matplotlib` 的 `mpl_connect('button_press_event', ...)`）。
- **替代方案：** Plotly 3D scatter + surface（互動效能較好；拖曳用 Plotly 的 dash callbacks）。或 Three.js（最高品質但跳脫 Python 生態）。
- **關鍵 API：**
  - `numpy.linalg.matrix_rank(A)` 求秩
  - `numpy.linalg.svd(A)` 取 $U, \Sigma, V^{\mathrm{T}}$ → $V$ 前 $r$ 列為 $\mathbf{C}(A^{\mathrm{T}})$ 標準正交基底、$U$ 前 $r$ 列為 $\mathbf{C}(A)$ 基底、$V$ 後 $n-r$ 列為 $\mathbf{N}(A)$ 基底、$U$ 後 $m-r$ 列為 $\mathbf{N}(A^{\mathrm{T}})$ 基底（**用 SVD 求四子空間基底是最穩定的方法**）
  - `mpl_toolkits.mplot3d.art3d.Poly3DCollection` 畫半透明平面
  - `matplotlib.patches.FancyArrowPatch` 配 `mpl_toolkits.mplot3d.proj3d.proj_transform` 畫 3D 箭頭
  - `scipy.linalg.null_space(A)` 直接求 $\mathbf{N}(A)$ 基底（替代 SVD）
- **檔案結構：** 與 VizScript-01 共用 `viz/ch03_matrix_vector.py`；3D 繪圖工具放 `viz/_common/subspace_3d.py`。
- **效能：**
  - 預先用 SVD 算好基底並 cache；只在 $A$ 變動時重算。
  - 拖曳 $\mathbf{x}$ 時只重畫箭頭，不重畫平面（用 `set_data_3d` 不要 `clear`）。
  - 「自動掃 $\mathbf{x}$」用 `FuncAnimation` 預先計算 60 frames，避免每 frame 算 SVD。
- **測試：**
  - 秩 = 2 / 1 / 0 各畫 1 張 3D snapshot。
  - $\mathbf{x}$ 從預設位置拖到原點過程中 3 個關鍵 frame snapshot（含分解平行四邊形）。
  - 拉 $a_{11}$ 從 1 → 0（不降秩）與 1 → -3（可能降秩）各 1 張動畫關鍵 frame。

#### L. 驗收標準（Acceptance Criteria）
- [ ] 左右視窗 3D 顯示正確：行空間粉紅平面、列空間綠平面、零空間 / 左零空間灰虛線，正交關係視覺正確。
- [ ] 拖曳 $\mathbf{x}$ 時 $\mathbf{x}_r + \mathbf{x}_n$ 分解平行四邊形即時更新 < 50ms。
- [ ] 「飛行動畫」$\mathbf{x} \to A\mathbf{x}$ 軌跡 700ms 平滑無 frame drop。
- [ ] 拉 $a_{ij}$ 降秩時平面塌成直線 / 零空間擴維動畫 600ms 完成且維度數字正確同步。
- [ ] 「自動掃 $\mathbf{x}$」軌跡完全落在綠色列空間內（驗證 $A\mathbf{x} \in \mathbf{C}(A)$）。
- [ ] 維度顯示文字 `dim C(A) = r`、`dim N(A) = n-r` 等四項與實際運算一致。
- [ ] 退化情形（$A = 0$、$r = 0$）正確顯示警示文字並平滑塌縮。
- [ ] Walkthrough 7 步驟首次開啟自動觸發。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 3
- **Tier 1 對應：** 純靜態圖（原書 Figure 5 重現）+ rank 計算結果文字顯示。
- **Tier 2 對應：** Tier 1 + 拖曳 $\mathbf{x}$ 看分解（無 3D 旋轉、無秩動畫）。
- **Tier 3 擴充內容（本劇本目標）：** 完整 3D 雙視窗 + 拖曳 $\mathbf{x}$ + 飛行動畫 + 秩變化平面塌縮 + 自動掃 $\mathbf{x}$ 軌跡。
- **Tier 4 進階擴充：** + 投影 / 最小二乘可視化（拖 $\mathbf{b}$ 不在 $\mathbf{C}(A)$ 內時，顯示沿 $\mathbf{N}(A^{\mathrm{T}})$ 投影到 $\hat{\mathbf{b}}$）— 留給 §6.5 SVD 章節做。
- **估時：** 3 session（含 3D 互動 debug、SVD 基底計算測試、動畫調校）

---

### VizScript-03: vM1 ↔ vM2 行向量視角切換（Left Multiplication Duality）

#### A. 一句話定位
與 VizScript-01 共畫面但以「左乘 $\mathbf{y}A$」角度呈現，讓使用者在 toggle 「右乘 / 左乘」時看整張畫面行 / 列鏡像翻轉，建立兩種方向的對偶直覺。

#### B. 學習目標
- 使用者能說出 (vM1) 是 $\mathbf{y}$ 與 $A$ 各直立列的點積。
- 使用者能說出 (vM2) 是 $A$ 各橫躺行被 $\mathbf{y}$ 分量縮放後線性組合。
- 使用者能解釋為何 $\mathbf{y}A$ 落在 $\mathbf{C}(A^{\mathrm{T}})$（行空間）。
- 使用者能在 toggle 「右乘 ↔ 左乘」時看出整張畫面行 / 列、上下 / 左右**鏡像翻轉**。

#### C. 待視覺化的數學物件
- 矩陣 $A$（同 VizScript-01）、行向量 $\mathbf{y} \in \mathbb{R}^{1 \times m}$、結果 $\mathbf{z} = \mathbf{y}A \in \mathbb{R}^{1 \times n}$。
- 預設值：$A$ 同 VizScript-01、$\mathbf{y} = (1, 1, 1)$。
- 退化情形：$\mathbf{y} = \mathbf{0}$ → 結果全 0；$\mathbf{y} \in \mathbf{N}(A^{\mathrm{T}})$ → 結果為 0 並標 "annihilated by A^T"。

#### D. 視覺布局
- 與 VizScript-01 共用同一畫面，多加一個頂部 toggle「右乘 $A\mathbf{x}$ / 左乘 $\mathbf{y}A$」。
- (vM1) 模式：$\mathbf{y}$ 橫躺粉紅條在左、$A$ 直立列在右；結果是橫躺粉紅條右端含 $n$ 個 dot product 結果。
- (vM2) 模式：$\mathbf{y}$ 藍點橫排在上、$A$ 橫躺行堆疊在下；結果是 $m$ 項「藍點 × 粉紅橫條」相加 + 結果粉紅橫條。
- 配色完全沿用 VizScript-01。

#### E. 輸入控制
- toggle「右乘 / 左乘」(新增) + (vM1) / (vM2) toggle + $A$ slider grid + $\mathbf{y}$ slider 橫排 + 重設。

#### F. 輸出畫面細節
- (vM1) 結果：橫躺粉紅條，內含 $n$ 個 dot product 數值。
- (vM2) 結果：$m$ 項相加結構，最右側結果橫躺粉紅條。
- 公式區即時顯示 $\mathbf{y}A = ?$。

#### G. 互動行為
- 拉 $\mathbf{y}$ 分量 → 即時重算；(vM2) 模式下對應橫躺行縮放動畫。
- toggle vM1 ↔ vM2 動畫類似 VizScript-01 但軸換 90°（畫面從「上下分」變「左右分」）。

#### H. 動畫腳本
- 與 VizScript-01 共用引擎；vM 模式整體畫面**鏡像翻轉**（上下對換、行 / 列換色），動畫時長 800ms，緩動 ease-in-out。

#### I. 邊界與錯誤處理
- 同 VizScript-01。$\mathbf{y} \in \mathbf{N}(A^{\mathrm{T}})$ 時資訊區紅字提示 "y ∈ left nullspace → yA = 0"。

#### J. 教學支援
- Tooltip：vM1「點積 $\mathbf{y}$ · 直立列」、vM2「行向量縮放加總」。
- Walkthrough 4 步驟：「現在是左乘 vM1 → 切到 vM2 → 拉 $y_1$ 看第 1 橫躺行縮放 → 注意結果落在 $\mathbf{C}(A^{\mathrm{T}})$（與 VizScript-02 左視窗呼應）」。

#### K. 技術實作建議
- 共用 `viz/ch03_matrix_vector.py`；vM 模式只是把 `numpy.dot(A, x)` 換成 `numpy.dot(y, A)` 並把繪圖佈局做 transpose。
- API 同 VizScript-01。

#### L. 驗收標準
- toggle 右乘 ↔ 左乘畫面 800ms 完成翻轉、無布局錯亂。
- 拉 $\mathbf{y}$ slider 結果即時更新 < 50ms。
- $\mathbf{y} = \mathbf{0}$ 顯示退化提示。

#### M. 互動深度 Tier + 估時
- 目標 Tier 2。Tier 1 = 靜態並列 vM1 / vM2。Tier 3 = 與 VizScript-02 左視窗連動，$\mathbf{y}A$ 端點在 $\mathbf{C}(A^{\mathrm{T}})$ 視覺定位。估時 0.5 session（共用 VizScript-01 引擎，只加 transpose 邏輯）。

---

### VizScript-04: 列空間軌跡掃描（Column Space Trace — Lite）

#### A. 一句話定位
拉 $\mathbf{x}$ 各分量看 $A\mathbf{x}$ 在 3D 空間中的端點即時移動 + 留下漸層淡化軌跡，視覺驗證「軌跡完全落在 $\mathbf{C}(A)$ 平面內」。

#### B. 學習目標
- 使用者能視覺驗證 $A\mathbf{x} \in \mathbf{C}(A)$。
- 使用者能直觀理解 $\mathbf{C}(A)$ 的「2 維 = 平面」「1 維 = 直線」對應 $A$ 不同秩。

#### C. 待視覺化的數學物件
- 同 VizScript-02 右視窗，但簡化版（無左視窗、無分解、無秩變化動畫）。

#### D. 視覺布局
- 單 3D 視窗 600×480 px，顯示 $\mathbb{R}^m$ 中的 $\mathbf{C}(A)$ 半透明綠平面 + $A\mathbf{x}$ 藍色箭頭 + 漸層淡化的歷史軌跡（最近 100 frames）。
- 下方控制列：$\mathbf{x}$ 各分量 slider。

#### E. 輸入控制
- $\mathbf{x}$ slider ($n$ 個)、清除軌跡 button、reset。

#### F. 輸出畫面細節
- $A\mathbf{x}$ 當前位置箭頭（不透明）+ 過往位置（透明度按時間衰減）。
- 軌跡的所有點落在綠平面內（視覺驗證）。

#### G. 互動行為
- 拉 $\mathbf{x}$ → 端點移動 + 留新軌跡點；軌跡 deque(maxlen=100)。
- 清除軌跡 button → 重置軌跡。

#### H. 動畫腳本
- 端點移動有 100ms 平滑插值（避免跳動）。

#### I-M. 簡化版
- 邊界 / 教學 / 實作 / 驗收：類似 VizScript-02 但範圍限縮。
- **目標 Tier：** Tier 1。
- **估時：** 0.5 session（建立在 VizScript-02 子集上）。

---

## 章末延伸

- **後續章節連結：** [→ ch04-mat-mat.md](ch04-mat-mat.md) — §4 矩陣乘以矩陣 (Matrix × Matrix) 有 **4 種視角** (MM1, MM2, MM3, MM4)，正是把本章 (Mv1)(Mv2)(vM1)(vM2) 推廣到矩陣 × 矩陣。本章對偶 + 線性組合直覺是 §4 的直接前置。

- **跨章節結構連結：**
  - **§5 Practical Patterns** 大量使用 (Mv2) 與 (vM2) 線性組合視角（投影 / 排列矩陣 / 旋轉矩陣等）。
  - **§6 五大分解** 每一個都基於「四子空間」結構：CR 把 $A$ 寫成 $\mathbf{C}(A^{\mathrm{T}})$ 與 $\mathbf{C}(A)$ 的對偶連接、QR 是行空間的標準正交化、SVD 把四子空間一次對齊到兩組標準正交基底。

- **延伸閱讀 / 相關概念：**
  - Strang《Linear Algebra for Everyone》Sec. 1.1（線性組合）、Sec. 1.3（矩陣與列空間）、Sec. 3.5（四子空間維度）— 原書直接對應段落。
  - Strang 在 *Linear Algebra and Its Applications* 5th ed. 也有相似 4-Subspaces 圖（俗稱 Strang's Big Picture），版本配色略不同但結構相同。
  - **跨領域類比：**
    - 機器學習：線性回歸 $A\mathbf{x} = \mathbf{b}$ 中，當 $\mathbf{b} \notin \mathbf{C}(A)$（資料不在模型可表達空間）時，最小二乘 $\hat{\mathbf{x}}$ 把 $\mathbf{b}$ 投影到 $\mathbf{C}(A)$，殘差 $\mathbf{b} - A\hat{\mathbf{x}} \in \mathbf{N}(A^{\mathrm{T}})$（與列空間正交）。
    - 信號處理：頻譜濾波本質是把訊號分解到不同子空間（傅立葉基底張成的子空間）。
    - 資料壓縮：主成分分析 (PCA) 把資料投影到 $\mathbf{C}(A)$ 維度最低的方向組合（與 SVD 直接相關）。

- **本章學完後讀者應該能回答：**
  - 一個 $3 \times 2$ 矩陣的列空間 / 行空間 / 零空間 / 左零空間各住在哪個 $\mathbb{R}^?$？維度可能是多少？
  - 為什麼 $A\mathbf{x} = \mathbf{b}$ 「有解」這件事可以直接從子空間角度判斷？
  - (Mv2) 視角與 (Mv1) 視角的計算結果為何相同？兩者各自適合什麼樣的數學推導？

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 69–112 / `The-Art-of-Linear-Algebra.pdf` p.3
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 68–107
- **圖檔：**
  - `figs/MatrixTimesVector.eps` → `docs/book/figs-png/MatrixTimesVector.png`
  - `figs/VectorTimesMatrix.eps` → `docs/book/figs-png/VectorTimesMatrix.png`
  - `figs/4-Subspaces.eps` → `docs/book/figs-png/4-Subspaces.png`
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0
