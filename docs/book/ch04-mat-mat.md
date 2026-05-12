# 第 4 章. 矩陣乘以矩陣 — 四種視角（Matrix × Matrix — 4 Ways）

> **原書頁碼：** p.4
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 114–125 行
> **本章圖數：** 1（Figure 4.1，含 MM1 / MM2 / MM3 / MM4 四子圖 2×2 排版）
> **本章 VizMark 數：** 4（⭐⭐⭐ × 2 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成 / [ ] 校對中

---

## 章節摘要

矩陣乘以矩陣 $AB = C$ 是「矩陣乘以向量」的自然延伸。同一個結果 $C$ 可以從**四個視角**讀出：**(MM1) 點積方式** — $C$ 的每個元素 $c_{ij}$ 各自是「$A$ 第 $i$ 橫躺行 · $B$ 第 $j$ 直立列」的 dot product；**(MM2) 列線性組合方式** — $C$ 的每一直立列 $\mathbf{c}_j$ 是「$A$ 的直立列以 $B$ 第 $j$ 列為係數的線性組合」；**(MM3) 行線性組合方式** — $C$ 的每一橫躺行 $\mathbf{c}^*_i$ 是「$B$ 的橫躺行以 $A$ 第 $i$ 行為係數的線性組合」；**(MM4) 外積之和方式** — $AB$ 直接拆成 $k$ 個秩 1 矩陣相加（$\mathbf{a}_p$ 列 × $\mathbf{b}^*_p$ 行）。

四種視角對應 §2（向量 × 向量）與 §3（矩陣 × 向量）的不同延伸：**(MM1) ↔ (Mv1) ↔ (v1) 點積家族**；**(MM2) ↔ (Mv2) 列線組家族（從右切看 B）**；**(MM3) ↔ (vM2) 行線組家族（從左切看 A）**；**(MM4) ↔ (v2) 外積家族 — 這條線是 §6 SVD 與 CR 分解的真正鑰匙**。

> ⚠ **本章是 §6 五大分解的「視覺前置」。** §6 所有矩陣分解 ($A = CR$、$A = LU$、$A = QR$、$S = Q\Lambda Q^{\mathrm{T}}$、$A = U\Sigma V^{\mathrm{T}}$) 都會把右側拆成「兩個 / 三個矩陣相乘」並用 (MM4) 或 (MM2)（取決於分解類型）來重新詮釋成秩 1 累加或列空間重塑。**MM4 視角不熟，後面 SVD 永遠卡住。**

> ⚠ **術語提醒（沿用 §1–§3 全書慣例 — A 派）：** column = 列（直立、綠色）、row = 行（橫躺、粉紅色）。$A$ 的「第 $j$ 直立列」記作 $\mathbf{a}_j \in \mathbb{R}^m$、「第 $i$ 橫躺行」記作 $\mathbf{a}^*_i \in \mathbb{R}^{1 \times k}$。$B$ 同理。$AB = C$ 的形狀運算 $(m \times k)(k \times n) = (m \times n)$，**中間維度 $k$ 必須對齊**。

---

## 數學要點

設 $A \in \mathbb{R}^{m \times k}$（$m$ 行 $k$ 列）、$B \in \mathbb{R}^{k \times n}$（$k$ 行 $n$ 列）、$C = AB \in \mathbb{R}^{m \times n}$。

矩陣切片符號（沿用 §3）：
- $\mathbf{a}_p \in \mathbb{R}^m$ = $A$ 的第 $p$ 直立列 ($p = 1, \ldots, k$)。
- $\mathbf{a}^*_i \in \mathbb{R}^{1 \times k}$ = $A$ 的第 $i$ 橫躺行 ($i = 1, \ldots, m$)。
- $\mathbf{b}_j \in \mathbb{R}^k$ = $B$ 的第 $j$ 直立列 ($j = 1, \ldots, n$)。
- $\mathbf{b}^*_p \in \mathbb{R}^{1 \times n}$ = $B$ 的第 $p$ 橫躺行 ($p = 1, \ldots, k$)。
- $\mathbf{c}_j$、$\mathbf{c}^*_i$ 同理。

### (MM1) 點積方式（Element-wise Dot Product Way）

把 $A$ 拆成 $m$ 個橫躺行、$B$ 拆成 $n$ 個直立列，則 $C$ 的每個元素是「行 · 列」點積：

$$
c_{ij}
\;=\;
\mathbf{a}^*_i \cdot \mathbf{b}_j
\;=\;
\sum_{p=1}^{k} a_{ip} \, b_{pj}
\qquad (i = 1, \ldots, m;\ j = 1, \ldots, n)
$$

寫成矩陣方塊形式：

$$
\underbrace{
\begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix}
}_{A}
\;
\underbrace{
\begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_n \end{bmatrix}
}_{B}
\;=\;
\begin{bmatrix}
\mathbf{a}^*_1 \cdot \mathbf{b}_1 & \mathbf{a}^*_1 \cdot \mathbf{b}_2 & \cdots & \mathbf{a}^*_1 \cdot \mathbf{b}_n \\
\mathbf{a}^*_2 \cdot \mathbf{b}_1 & \mathbf{a}^*_2 \cdot \mathbf{b}_2 & \cdots & \mathbf{a}^*_2 \cdot \mathbf{b}_n \\
\vdots & \vdots & \ddots & \vdots \\
\mathbf{a}^*_m \cdot \mathbf{b}_1 & \mathbf{a}^*_m \cdot \mathbf{b}_2 & \cdots & \mathbf{a}^*_m \cdot \mathbf{b}_n
\end{bmatrix}
$$

- **總點積次數：** $m \cdot n$ 個（每個元素 1 次點積，每次點積 $k$ 次乘法 + $(k{-}1)$ 次加法）。
- **直覺：** 「每元素一個點積」 — 這是教科書最熟悉的視角，與 (Mv1) 的「每分量一個點積」一脈相承。
- **原書 (MM1) 範例（$m=3, k=2, n=2$）：**

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix}
\;=\;
\begin{bmatrix}
(x_1 + 2 x_2) & (y_1 + 2 y_2) \\
(3 x_1 + 4 x_2) & (3 y_1 + 4 y_2) \\
(5 x_1 + 6 x_2) & (5 y_1 + 6 y_2)
\end{bmatrix}
$$

### (MM2) 列線性組合方式（Column Linear Combination Way）

把 $B$ 拆成 $n$ 個直立列 $\mathbf{b}_1, \ldots, \mathbf{b}_n$，則 $C$ 的每一直立列各自是「$A$ 對 $\mathbf{b}_j$ 的線性組合」（即 (Mv2) 重複 $n$ 次）：

$$
AB \;=\; A \begin{bmatrix} \mathbf{b}_1 & \mathbf{b}_2 & \cdots & \mathbf{b}_n \end{bmatrix} \;=\; \begin{bmatrix} A\mathbf{b}_1 & A\mathbf{b}_2 & \cdots & A\mathbf{b}_n \end{bmatrix}
$$

逐列展開：

$$
\mathbf{c}_j \;=\; A \mathbf{b}_j \;=\; b_{1j} \mathbf{a}_1 + b_{2j} \mathbf{a}_2 + \cdots + b_{kj} \mathbf{a}_k
\qquad (j = 1, \ldots, n)
$$

- **直覺：** $B$ 的每一直立列 $\mathbf{b}_j$ 是一份「配方」，告訴你**把 $A$ 的直立列用什麼比例混合**，得到 $C$ 的第 $j$ 直立列。$C$ 的所有直立列因此都落在 $\mathbf{C}(A)$（$A$ 的列空間）裡。
- **原書 (MM2) 範例：**

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix}
\;=\;
A
\begin{bmatrix} \mathbf{x} & \mathbf{y} \end{bmatrix}
\;=\;
\begin{bmatrix} A\mathbf{x} & A\mathbf{y} \end{bmatrix}
$$

其中 $A\mathbf{x} = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 = x_1 (1,3,5)^{\mathrm{T}} + x_2 (2,4,6)^{\mathrm{T}}$。

- **關鍵推論（後續章節依賴）：** $\mathbf{C}(AB) \subseteq \mathbf{C}(A)$ — 乘上任何 $B$ 從右邊，列空間只會「等於或縮小」，永遠不會超出 $A$ 的列空間。

### (MM3) 行線性組合方式（Row Linear Combination Way）

把 $A$ 拆成 $m$ 個橫躺行 $\mathbf{a}^*_1, \ldots, \mathbf{a}^*_m$，則 $C$ 的每一橫躺行各自是「$\mathbf{a}^*_i$ 對 $B$ 的線性組合」（即 (vM2) 重複 $m$ 次）：

$$
AB \;=\; \begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix} B \;=\; \begin{bmatrix} \mathbf{a}^*_1 B \\ \mathbf{a}^*_2 B \\ \vdots \\ \mathbf{a}^*_m B \end{bmatrix}
$$

逐行展開：

$$
\mathbf{c}^*_i \;=\; \mathbf{a}^*_i B \;=\; a_{i1} \mathbf{b}^*_1 + a_{i2} \mathbf{b}^*_2 + \cdots + a_{ik} \mathbf{b}^*_k
\qquad (i = 1, \ldots, m)
$$

- **直覺：** $A$ 的每一橫躺行 $\mathbf{a}^*_i$ 是一份「配方」，告訴你**把 $B$ 的橫躺行用什麼比例混合**，得到 $C$ 的第 $i$ 橫躺行。$C$ 的所有橫躺行因此都落在 $\mathbf{C}(B^{\mathrm{T}})$（$B$ 的行空間）裡。
- **原書 (MM3) 範例：**

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix}
\;=\;
\begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \mathbf{a}^*_3 \end{bmatrix} B
\;=\;
\begin{bmatrix} \mathbf{a}^*_1 B \\ \mathbf{a}^*_2 B \\ \mathbf{a}^*_3 B \end{bmatrix}
$$

其中 $\mathbf{a}^*_1 B = \begin{bmatrix} 1 & 2 \end{bmatrix} B = 1 \cdot (x_1, y_1) + 2 \cdot (x_2, y_2) = (x_1 + 2x_2, \, y_1 + 2y_2)$。

- **關鍵推論：** $\mathbf{C}((AB)^{\mathrm{T}}) \subseteq \mathbf{C}(B^{\mathrm{T}})$ — 行空間只會「等於或縮小」。

### (MM4) 外積之和方式（Sum of Outer Products / Rank-1 Decomposition Way）— **本章核心**

把 $A$ 拆成 $k$ 個直立列、$B$ 拆成 $k$ 個橫躺行（**注意：拆數 $k$ 是「內維度」，不是 $m$ 或 $n$**），則 $AB$ 等於 $k$ 個外積（秩 1 矩陣）的和：

$$
AB
\;=\;
\begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_k \end{bmatrix}
\begin{bmatrix} \mathbf{b}^*_1 \\ \mathbf{b}^*_2 \\ \vdots \\ \mathbf{b}^*_k \end{bmatrix}
\;=\;
\sum_{p=1}^{k} \mathbf{a}_p \mathbf{b}^*_p
\;=\;
\mathbf{a}_1 \mathbf{b}^*_1 + \mathbf{a}_2 \mathbf{b}^*_2 + \cdots + \mathbf{a}_k \mathbf{b}^*_k
$$

每一項 $\mathbf{a}_p \mathbf{b}^*_p$ 都是一個**秩 1 矩陣**（$m \times n$），是 §2 (v2) 外積 → rank 1 結構的**直接重複 $k$ 次**。

- **形狀檢核：** $\mathbf{a}_p \in \mathbb{R}^{m \times 1}$、$\mathbf{b}^*_p \in \mathbb{R}^{1 \times n}$、$\mathbf{a}_p \mathbf{b}^*_p \in \mathbb{R}^{m \times n}$。$k$ 個 $m \times n$ 矩陣相加仍是 $m \times n$。
- **直覺：** 把 $AB$ 看成「**$k$ 個秩 1 圖層疊加**」。當 $k$ 很大時（如 SVD），疊加越多項越接近原矩陣；截斷前幾項即低秩近似。
- **原書 (MM4) 範例（$k = 2$）：**

$$
\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
\begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}
\;=\;
\begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \end{bmatrix}
\,+\,
\begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} \begin{bmatrix} b_{21} & b_{22} \end{bmatrix}
$$

展開為兩個秩 1 矩陣：

$$
=\;
\begin{bmatrix} b_{11} & b_{12} \\ 3 b_{11} & 3 b_{12} \\ 5 b_{11} & 5 b_{12} \end{bmatrix}
\,+\,
\begin{bmatrix} 2 b_{21} & 2 b_{22} \\ 4 b_{21} & 4 b_{22} \\ 6 b_{21} & 6 b_{22} \end{bmatrix}
\;=\;
\begin{bmatrix} b_{11} + 2 b_{21} & b_{12} + 2 b_{22} \\ 3 b_{11} + 4 b_{21} & 3 b_{12} + 4 b_{22} \\ 5 b_{11} + 6 b_{21} & 5 b_{12} + 6 b_{22} \end{bmatrix}
$$

- **與 §6 五大分解的銜接：**
  - **$A = CR$（行列消去）：** $A$ 寫成「獨立列 × 行操作」的乘積，秩 = 獨立列數 = MM4 的有效項數。
  - **$A = LU$（消去法）：** $LU$ 即 (MM4)（$L$ 的直立列 × $U$ 的橫躺行）的有限項相加。
  - **$A = QR$（正交化）：** 同上 (MM4) 結構，但 $Q$ 的直立列彼此正交。
  - **$S = Q \Lambda Q^{\mathrm{T}}$（譜分解）：** 對稱矩陣的特殊 (MM4)，$S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$。
  - **$A = U \Sigma V^{\mathrm{T}}$（SVD）：** 最一般的 (MM4)，$A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，按 $\sigma_p$ 大小排序，取前 $r$ 項即最佳低秩近似（Eckart–Young 定理）。

**(MM4) 不誇張地說，是這本書（也是線性代數應用版圖）的 \*核心\*。**

### 四個視角總表

| 視角 | 拆法 | 主角 | 一句話 | 結果空間關係 |
|---|---|---|---|---|
| **(MM1)** | $A$ 攤橫躺行 + $B$ 攤直立列 | 每個元素 1 個點積 | 「行 · 列 = $c_{ij}$」 | — |
| **(MM2)** | $B$ 攤直立列 | $C$ 的每一直立列 = $A$ 列的線組 | 「$\mathbf{c}_j = A \mathbf{b}_j$」 | $\mathbf{C}(C) \subseteq \mathbf{C}(A)$ |
| **(MM3)** | $A$ 攤橫躺行 | $C$ 的每一橫躺行 = $B$ 行的線組 | 「$\mathbf{c}^*_i = \mathbf{a}^*_i B$」 | $\mathbf{C}(C^{\mathrm{T}}) \subseteq \mathbf{C}(B^{\mathrm{T}})$ |
| **(MM4)** | $A$ 攤直立列 + $B$ 攤橫躺行 | $AB$ = $k$ 個秩 1 矩陣相加 | 「$AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$」 | $\operatorname{rank}(AB) \le k$；§6 分解皆基於此 |

### 與 §2 §3 的對偶傳承

| §2 / §3 視角 | §4 推廣 | 關係 |
|---|---|---|
| (v1) 點積 $\mathbf{v} \cdot \mathbf{w}$ | (MM1) 點積每元素 | 「dot product 升級到陣列規模」 |
| (v2) 外積 $\mathbf{v} \mathbf{w}^*$ → 秩 1 矩陣 | (MM4) 外積之和 | 「外積家族真正的家」 |
| (Mv1) $A\mathbf{x}$ 點積 | (MM1) | — |
| (Mv2) $A\mathbf{x}$ 列線組 | (MM2) | 「Mv2 重複 $n$ 次」 |
| (vM1) $\mathbf{y}A$ 點積 | (MM1) | — |
| (vM2) $\mathbf{y}A$ 行線組 | (MM3) | 「vM2 重複 $m$ 次」 |

**記憶口訣：** 「**MM1 像 dot 連環、MM2 是 Mv2 重播、MM3 是 vM2 重播、MM4 是 v2 升級。**」

### 維度檢核（中間維度對齊）

$(m \times k)(k \times n) = (m \times n)$。**內維度 $k$（A 的列數 = B 的行數）必須相等**才能做乘法。常見錯誤：

- **shape mismatch：** $A$ 是 $3 \times 4$、$B$ 是 $5 \times 2$ → $k$ 不對齊，無法乘。
- **方陣不一定可乘自身：** $A$ 是 $3 \times 4$ → $A \cdot A$ 不合法（要算 $A^{\mathrm{T}} A$ 或 $A A^{\mathrm{T}}$）。
- **MM4 拆數恰是 $k$：** 因為這是內維度，不是 $m$ 也不是 $n$。SVD 把 $A$ ($m \times n$) 拆成 $\sum_{p=1}^{r} \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，這裡 $r \le \min(m, n)$ 是秩，比 $k$（如果 $A$ 不是分解形式）更精確。

### 矩陣乘法不滿足交換律

一般而言 $AB \ne BA$，且兩者形狀可能不同：

- $A$ 是 $m \times k$、$B$ 是 $k \times n$ → $AB$ 是 $m \times n$、$BA$ 形狀需 $n = m$ 才合法且為 $k \times k$。
- **方陣可換的條件：** 兩個方陣同階 + 共享一組特徵向量（如同時對角化）。
- **(MM4) 視角的直覺：** $AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$ 是「左列 × 右行」、$BA = \sum_q \mathbf{b}_q \mathbf{a}^*_q$ 是「左列 × 右行」但拆的對象互換，幾何上完全不同。

---

## 圖片詳細描述（Figure Descriptions）

### Figure 4.1: 矩陣乘以矩陣的四種視角（Matrix × Matrix — (MM1), (MM2), (MM3), (MM4)）

**圖檔：** `docs/book/figs-png/MatrixTimesMatrix.png`（原始 EPS：`figs/MatrixTimesMatrix.eps`）
**原書頁碼：** p.4（書封底也呈現此圖）
**所屬章節：** §4

#### 視覺結構 (Visual Structure)

此圖採「**2 × 2 並列四子圖**」結構，是本書最大資訊密度的單頁圖之一。每個子圖左上角有灰色小圈圈標 `MM1`、`MM2`、`MM3`、`MM4` 編號。範例矩陣設定為 $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \in \mathbb{R}^{3 \times 2}$、$B = \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} \in \mathbb{R}^{2 \times 2}$（部份子圖 $B$ 寫作 $\begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}$ — 兩種記法等價）。

- **左上 (MM1) 點積方式：**
  - 抽象示意：**$A$（3 條粉紅橫躺行）× $B$（2 條綠直立列）= $C$（3×2 棋盤格，每 cell 內畫一條粉紅橫條 + 一條綠直條交叉**「混色」**）**。
  - 右側文字：**"Every element becomes a dot product of row vector and column vector."**
  - 具體範例（下方）：
    $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} = \begin{bmatrix} (x_1 + 2 x_2) & (y_1 + 2 y_2) \\ (3x_1 + 4x_2) & (3 y_1 + 4 y_2) \\ (5x_1 + 6x_2) & (5 y_1 + 6 y_2) \end{bmatrix}$$
- **右上 (MM2) 列線性組合方式：**
  - 抽象示意：**$A$（灰色實心方塊）× $B$（2 條綠直立列在大方框）= $A B$（同樣 2 條綠直立列在大方框，但每條稍透明帶漸層）= 進一步寫成 `[Ax  Ay]` 兩條結果直立列**。
  - 右側文字：**"$A\mathbf{x}$ and $A\mathbf{y}$ are linear combinations of columns of $A$."**
  - 具體範例（下方）：
    $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} = A \begin{bmatrix} \mathbf{x} & \mathbf{y} \end{bmatrix} = \begin{bmatrix} A\mathbf{x} & A\mathbf{y} \end{bmatrix}$$
- **左下 (MM3) 行線性組合方式：**
  - 抽象示意：**$A$（3 條粉紅橫躺行）× $B$（灰色實心方塊）= $C$（3 條粉紅橫躺行 + 灰色背景，每條稍透明帶漸層）= 進一步寫成「$\mathbf{a}^*_1 X$ / $\mathbf{a}^*_2 X$ / $\mathbf{a}^*_3 X$」三條結果橫躺行**。
  - 右側文字：**"The produced rows are linear combinations of rows."**
  - 具體範例（下方，原書記 $B$ 為 $X$）：
    $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} = \begin{bmatrix} \mathbf{a}^*_1 \\ \mathbf{a}^*_2 \\ \mathbf{a}^*_3 \end{bmatrix} X = \begin{bmatrix} \mathbf{a}^*_1 X \\ \mathbf{a}^*_2 X \\ \mathbf{a}^*_3 X \end{bmatrix}$$
- **右下 (MM4) 外積之和方式：**
  - 抽象示意：**$A$（2 條綠直立列）× $B$（2 條粉紅橫躺行）= 兩個「綠直立 × 粉紅橫躺」秩 1 矩陣（$m \times n$ 大小，內含上方一橫條粉紅 + 左側一直條綠的「+」字交叉染色）相加**。
  - 右側文字：**"Multiplication $AB$ is broken down to a sum of rank 1 matrices."**
  - 具體範例（下方）：
    $$\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 \end{bmatrix} \begin{bmatrix} \mathbf{b}^*_1 \\ \mathbf{b}^*_2 \end{bmatrix} = \mathbf{a}_1 \mathbf{b}^*_1 + \mathbf{a}_2 \mathbf{b}^*_2$$
    展開：
    $$= \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \end{bmatrix} + \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix} \begin{bmatrix} b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} b_{11} & b_{12} \\ 3 b_{11} & 3 b_{12} \\ 5 b_{11} & 5 b_{12} \end{bmatrix} + \begin{bmatrix} 2 b_{21} & 2 b_{22} \\ 4 b_{21} & 4 b_{22} \\ 6 b_{21} & 6 b_{22} \end{bmatrix}$$
- **配色語意（全章一致，沿用 §1–§3）：**
  - **粉紅色橫條** = 橫躺行（row）。
  - **綠色直條** = 直立列（column）。
  - **灰色實心方塊** = 矩陣整體（不分行 / 列），表示「不關心內部切法、只看為一個 transformation」。
  - **漸層 / 半透明效果** = 「該軸方向被線性組合稀釋 / 投影」。
  - **棋盤交叉（MM1 結果）** = 「每元素同時受到 row + column 兩條方向影響」。
- **四子圖排版方向意義：**
  - **左欄 (MM1, MM3)：** 「逐行 / 逐元素」思維 — 結果用「橫躺行家族」描述。
  - **右欄 (MM2, MM4)：** 「逐列 / 整體疊加」思維 — 結果用「直立列家族」或「秩 1 矩陣相加」描述。
  - **上排 (MM1, MM2)：** 結果是「具體元素填上的最終矩陣」。
  - **下排 (MM3, MM4)：** 結果是「結構性分解（橫躺行家族或秩 1 之和）」 — 更接近 §6 分解視角。

讀者的視覺動線：左上 (MM1) 是熟悉起點 → 順時針到右上 (MM2) 把每元素點積擴展到「整列被線組」→ 跳到右下 (MM4) 把整個運算改寫成「兩個秩 1 之和」 → 最後左下 (MM3) 收尾，與 (MM2) 形成左右乘對稱。**讀完 (MM4) 後再回頭看 (MM1) 會發現「點積方式只是把 (MM4) 中所有秩 1 矩陣的 $(i, j)$ 元素加起來」 — 四視角是同一件事的四種讀法。**

#### 數學內容 (Mathematical Content)

**設定（沿用原書）：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \in \mathbb{R}^{3 \times 2}$、$B = \begin{bmatrix} x_1 & y_1 \\ x_2 & y_2 \end{bmatrix} \in \mathbb{R}^{2 \times 2}$、$C = AB \in \mathbb{R}^{3 \times 2}$。

**四種視角驗證恆等（左上角元素 $c_{11}$）：**

- **(MM1)：** $c_{11} = \mathbf{a}^*_1 \cdot \mathbf{b}_1 = 1 \cdot x_1 + 2 \cdot x_2 = x_1 + 2 x_2$。
- **(MM2)：** $\mathbf{c}_1 = A \mathbf{b}_1 = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 = x_1 (1,3,5)^{\mathrm{T}} + x_2 (2,4,6)^{\mathrm{T}}$；$\mathbf{c}_1$ 的第 1 分量 = $x_1 + 2 x_2$。✓
- **(MM3)：** $\mathbf{c}^*_1 = \mathbf{a}^*_1 B = 1 \cdot (x_1, y_1) + 2 \cdot (x_2, y_2) = (x_1 + 2x_2, y_1 + 2y_2)$；$\mathbf{c}^*_1$ 的第 1 分量 = $x_1 + 2x_2$。✓
- **(MM4)：** $AB = \mathbf{a}_1 \mathbf{b}^*_1 + \mathbf{a}_2 \mathbf{b}^*_2$；左上角 = $1 \cdot x_1 + 2 \cdot x_2 = x_1 + 2 x_2$。✓

四種視角數值完全等價，差別在「**閱讀順序 / 心智模型 / 連結後續概念的方向**」。

**運算量檢核：** 四種視角總 FLOP 數相同（$2 \cdot m \cdot k \cdot n$ — 含 $mkn$ 個乘法 + $m(k-1)n$ 個加法），但**記憶體存取模式不同**：

| 視角 | 主要 loop 順序 | 記憶體優勢 |
|---|---|---|
| (MM1) | `for i for j for p: c[i,j] += a[i,p]*b[p,j]` | 直觀但 cache miss 高（B column-major 不利 row-major 存取） |
| (MM2) | `for j: c[:,j] = A @ b[:,j]` | 適合直立列為主的儲存（Fortran / MATLAB） |
| (MM3) | `for i: c[i,:] = a[i,:] @ B` | 適合橫躺行為主的儲存（C / NumPy 預設 row-major） |
| (MM4) | `for p: C += a[:,p:p+1] @ b[p:p+1,:]` | 適合 streaming / out-of-core（隨來隨累加，無需一次載入完整 A, B） |

**形狀運算（四視角共通）：** $(3 \times 2)(2 \times 2) = (3 \times 2)$。內維度 $k = 2$。

**(MM4) 秩 1 之和的視覺意義：**

$$\mathbf{a}_1 \mathbf{b}^*_1 = \begin{bmatrix} 1 \\ 3 \\ 5 \end{bmatrix} \begin{bmatrix} b_{11} & b_{12} \end{bmatrix} = \begin{bmatrix} b_{11} & b_{12} \\ 3b_{11} & 3b_{12} \\ 5b_{11} & 5b_{12} \end{bmatrix}$$

注意這個矩陣的每一直立列都是 $\mathbf{a}_1 = (1,3,5)^{\mathrm{T}}$ 的倍數，每一橫躺行都是 $\mathbf{b}^*_1 = (b_{11}, b_{12})$ 的倍數 — 這就是「**秩 1 矩陣**」的定義（所有直立列共線、所有橫躺行也共線）。

**$AB$ 的秩界限：** $\operatorname{rank}(AB) \le \min(\operatorname{rank} A, \operatorname{rank} B) \le \min(m, k, n)$。從 (MM4) 看：$AB$ 是 $k$ 個秩 1 矩陣相加，秩最多 $k$。若 $A$ 的列空間或 $B$ 的行空間維度更小，秩進一步受限。

#### 直覺解讀 (Intuition)

**1. 四個視角是同一座山的四個觀景台。** 不是「四種不同算法」 — 是同一個 $AB$ 的四種「拆解方式」。教科書通常先教 (MM1)（因為「點積」最具體），但 (MM2) (MM3) 是矩陣論大量結論的源頭，(MM4) 則是 §6 五大分解的鑰匙。**真正讀通的人腦中四個視角能隨意切換 — 看見一個 $AB$ 表達式，會自動同時看到 4 個結構。**

**2. 為什麼 (MM4) 是「最重要」的視角？** 因為：
- **§6 所有分解都是 (MM4) 的特例：** 把 $A$ 寫成兩 / 三個矩陣相乘，再用 (MM4) 把右側展開成「秩 1 之和」。SVD 的 $A = U \Sigma V^{\mathrm{T}}$ 展開即 $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，是「按重要性排序的 (MM4) 之和」。
- **低秩近似的數學依據：** 取 (MM4) 前 $k$ 項即「秩 $k$ 截斷」近似，Eckart–Young 定理保證 SVD 的截斷是 Frobenius 範數下最佳。**這在影像壓縮、推薦系統（矩陣分解）、PCA 都是核心**。
- **Streaming 運算的視角：** $AB$ 不需一次計算完。每次處理一對 $(\mathbf{a}_p, \mathbf{b}^*_p)$ 就累加一個秩 1 圖層 — 適合分散式 / 線上學習。

**3. (MM2) vs (MM3) 的對偶。** 兩者完美對稱：
- (MM2)：「把 $B$ 視為『右側操作』」 — $B$ 的每一直立列指揮如何混合 $A$ 的列。$C$ 的列空間繼承自 $A$ 的列空間。
- (MM3)：「把 $A$ 視為『左側操作』」 — $A$ 的每一橫躺行指揮如何混合 $B$ 的行。$C$ 的行空間繼承自 $B$ 的行空間。
**口訣：** 「**從右邊乘 = 從右側看 = 看 $B$ 怎麼切 = 列線組；從左邊乘 = 從左側看 = 看 $A$ 怎麼切 = 行線組。**」

**4. (MM1) 是「Bad Default」嗎？** 不是。(MM1) 在四方面仍然不可或缺：
- **教學起點：** 對中學程度讀者最容易理解。
- **單一元素查詢：** 只要算 $c_{ij}$ 一個值，(MM1) 是最直接的方式（不需展開整個 $A$ 或 $B$）。
- **稀疏矩陣最佳化：** 若 $A$ 的某 row 多 0 / $B$ 的某 column 多 0，(MM1) 視角下可早終止點積。
- **數學證明便利：** 推導 $c_{ij}$ 的代數性質時 (MM1) 視角最方便（如 trace、Frobenius inner product）。
但 (MM1) 缺乏「子空間 / 秩 / 分解」的視角延伸性 — 這是它的限制。

**5. 何時選哪個視角思考？**

| 你的目標 | 推薦視角 |
|---|---|
| 算單一元素 $c_{ij}$ | (MM1) |
| 理解 $AB$ 的列空間 / 解 $Ax = b$ | (MM2) |
| 理解 $AB$ 的行空間 / 列消去法 | (MM3) |
| 矩陣分解 / SVD / 低秩近似 / streaming | **(MM4)** |
| 證明 trace / 矩陣範數性質 | (MM1) |
| 推導 chain rule（神經網路反向傳播） | (MM2) 或 (MM3)（看 $A$ 還是 $B$ 是參數） |

**常見誤解警示：**
- **「(MM4) 的秩 1 矩陣可以隨便排序」** — 數值上可以（加法可換），但 SVD 的關鍵是「**按 $\sigma_p$ 大小排序後截斷才是最佳近似**」。隨便排序則截斷品質沒保證。
- **「(MM2) 和 (Mv2) 只是寫法不同」** — (Mv2) 是「一個 $\mathbf{x}$ 對 $A$ 列做線組」、(MM2) 是「$n$ 個 $\mathbf{b}_j$ 各自對 $A$ 列做線組」。(MM2) = (Mv2) 重複 $n$ 次，但這個「重複」本身就是 (MM2) 的核心。
- **「四種視角適合不同類型的矩陣」** — 否，四種視角對任何矩陣都成立。差別在你想看出什麼性質。
- **「(MM4) 對非方陣不適用」** — 完全適用。$A$ 是 $m \times k$、$B$ 是 $k \times n$，$AB$ 是 $\sum_{p=1}^{k} \mathbf{a}_p \mathbf{b}^*_p$ — 每項是 $m \times n$ 矩陣，與 $A, B$ 是否方陣無關。

**為什麼這張圖該做成互動視覺化？** 因為四個視角的「**等價性**」是動態概念 — 看著同一個 $AB$ 的計算流程從 (MM1) 模式切換到 (MM4) 模式，會即時看到「點積堆 → 列線組 → 行線組 → 秩 1 圖層疊加」的轉換動畫，這是靜態圖完全傳達不了的（見 VizMark-01）。並且 (MM4) 秩 1 圖層的「動態疊加 + rank-$k$ 截斷」是 SVD 教學最缺的鋪陳（見 VizMark-02），把這個畫面做好，§6 SVD 的學習曲線可以下降一半。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [切換視角] ⭐⭐⭐
> **位置：** Figure 4.1 / §4 / (MM1) ↔ (MM2) ↔ (MM3) ↔ (MM4) 四視角切換
> **核心概念：** $AB$ 的四種「拆解 / 閱讀」視角等價（同結果、不同心智模型）
> **互動梗概：** 四個 tab 切換，每次切換觸發 800ms 動畫，把 $A, B, C$ 的色塊（行 / 列 / 灰塊）按目標視角重排，公式逐項同步重排
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [拉桿調參 + 動態累加] ⭐⭐⭐
> **位置：** Figure 4.1 / §4 / (MM4) 子圖 + §6 SVD 預備
> **核心概念：** $AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$ 的秩 1 圖層**逐項累加 / 截斷**動畫，建立「低秩近似」直覺（為 §6 SVD 鋪陳）
> **互動梗概：** 拉「累加項數」slider 從 0 → $k$，看每加一個秩 1 圖層 $C$ 如何越來越接近目標；切換到「彩色圖像」demo 看 SVD 截斷的視覺效果
> **詳見劇本：** VizScript-02（章末）

> 🎬 **VizMark-03** [維度檢核 + 對齊] ⭐⭐
> **位置：** Figure 4.1 / §4 / 整體
> **核心概念：** $(m \times k)(k \times n) = (m \times n)$ 的「內維度對齊」是矩陣乘法合法性的唯一條件
> **互動梗概：** 拉 $A$ 與 $B$ 的尺寸 slider，動態顯示「$k$ 對齊 / 不對齊」的視覺紅綠提示 + 形狀 prediction
> **詳見劇本：** VizScript-03（章末，精簡版）

> 🎬 **VizMark-04** [數值步進] ⭐
> **位置：** Figure 4.1 / §4 / (MM1) 子圖
> **核心概念：** 逐 cell walk through (MM1) 點積計算過程，連結到中學算盤式思維
> **互動梗概：** 按播放鍵，從 $c_{11}$ 開始依序高亮對應的 $\mathbf{a}^*_i$ 與 $\mathbf{b}_j$、播放點積結果填入 cell 的動畫
> **詳見劇本：** VizScript-04（章末，輕量版）

---

## 視覺化劇本（VizScripts）

### VizScript-01: 矩陣乘以矩陣的四種視角切換（4-Way Toggle Animation）

#### A. 一句話定位
單一畫面同時可切換 (MM1) / (MM2) / (MM3) / (MM4) 四種視角，每次切換以 800ms 動畫把 $A, B, C$ 的色塊（橫躺粉紅、直立綠、灰塊、秩 1 圖層）按目標視角重排並重新染色，下方公式逐項同步展開。

#### B. 學習目標（Learning Outcome）
- 使用者能切換四個視角並指出每個視角下 $A, B, C$ 的「主角形狀」（橫躺 / 直立 / 整塊 / 秩 1 圖層）。
- 使用者能寫出每個視角下 $c_{ij}$、$\mathbf{c}_j$、$\mathbf{c}^*_i$、$\mathbf{a}_p \mathbf{b}^*_p$ 的精確公式。
- 使用者能說出「(MM4) 把 $AB$ 解讀成『秩 1 之和』，為 §6 SVD 鋪陳」。
- 使用者能根據手上的任務（算單一元素 / 找列空間 / 找行空間 / 做分解）選用對應視角。
- 使用者能在「拉 $\mathbf{x}$ slider」時觀察到 (MM2) 模式下「$A$ 不動、$B$ 的某直立列權重變化、結果直立列同步變化」的列線組行為。

#### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$C = AB \in \mathbb{R}^{m \times n}$、4 個切片家族（$\mathbf{a}^*_i, \mathbf{a}_p, \mathbf{b}^*_p, \mathbf{b}_j$）、$k$ 個秩 1 矩陣 $\mathbf{a}_p \mathbf{b}^*_p$。
- **預設值：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$（$m=3, k=2$）、$B = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$（$k=2, n=2$，使 $C$ 各分量均為「對應 $A$ row sum 倍率」便於觀察）。
- **維度範圍：** $m, n \in [2, 6]$，$k \in [2, 5]$（限 $k \le 5$ 以避免 MM4 秩 1 圖層過多視覺擁擠）。
- **數值範圍：** $a_{ij}, b_{ij} \in [-9, 9]$ 步進 1。
- **退化情形：**
  - $B = I$（$k = n$）：$AB = A$，四視角都顯示「結果完全等於 $A$」的特殊情況。
  - $B = 0$：$AB = 0$，所有色塊變灰、(MM4) 秩 1 圖層全 0。
  - $\operatorname{rank}(A) = 1$ 且 $\operatorname{rank}(B) = 1$：$AB$ 也是秩 1，(MM4) 只剩 1 個非 0 圖層。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 70% 視角區（依模式顯示對應子圖）+ 中 10% 公式區 + 下 20% 控制列。
- **視角區共用畫布：** 1200×480 px 白底；色塊主舞台位於畫布中央 1000×360 px。
- **(MM1) 模式：** 左 $A$（3 條粉紅橫條 stack，60px 高 × 240px 寬）+ 中 `=` + 右 $B$（2 條綠直條 stack，240px 高 × 60px 寬）+ 「箭頭 →」+ $C$（3×2 棋盤格 cell，每 cell 內畫一條粉紅橫條 + 一條綠直條交叉）。
- **(MM2) 模式：** 左 $A$（灰色實心方塊 240×240 px，內以淡粉紅 / 淡綠十字格線提示但不主導）+ `×` + $B$（2 條綠直立列）+ `=` + $C$（2 條綠直立列，每條漸層稀釋表示「線組混合」）。
- **(MM3) 模式：** 左 $A$（3 條粉紅橫躺行）+ `×` + $B$（灰色實心方塊）+ `=` + $C$（3 條粉紅橫躺行，漸層稀釋）。
- **(MM4) 模式：** 左 $A$（2 條綠直立列）+ `×` + $B$（2 條粉紅橫躺行）+ `=` + 2 個「秩 1 矩陣」並排（每個 $m \times n$ 方塊，上方一條粉紅橫 + 左側一條綠直「+」字交叉染色）+ 「$+$」+ ... + 「$=$」+ 最終 $C$。
- **配色（全章一致）：** 綠 `#2ca02c`、粉紅 `#d62728`、藍點 `#1f77b4`、灰填充 `#eeeeee` / 框 `#333333`、漸層 alpha 0.3。
- **公式區：** 等寬字 14pt，LaTeX 渲染（即時切換）。
- **控制列：** 模式 tab（4 個）+ $A$ slider grid + $B$ slider grid + $m, k, n$ slider + 重設 button。
- **字型 / 字級：** 視角標題 18pt sans bold、$A, B, C$ 標籤 14pt italic、cell 內數字 12pt mono、控制列 12pt。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 mode | tab × 4 | MM1 / MM2 / MM3 / MM4 | MM1 | 即時 + 動畫 |
| $m$ | slider | [2, 6] | 3 | 即時 |
| $k$ | slider | [2, 5] | 2 | 即時 |
| $n$ | slider | [2, 6] | 2 | 即時 |
| $a_{ij}$ ($i\!=\!1..m, p\!=\!1..k$) | slider grid | [-9, 9] step 1 | $1, 2, ..., mk$ | 即時 |
| $b_{pj}$ ($p\!=\!1..k, j\!=\!1..n$) | slider grid | [-9, 9] step 1 | 1 (all 1) | 即時 |
| 公式逐項高亮 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click → 還原預設 |

#### F. 輸出畫面細節（Outputs）
- **(MM1) 模式輸出：**
  - $C$ 棋盤格每 cell 中段顯示「$\sum_p a_{ip} b_{pj}$」具體數字（如「$1 \cdot 1 + 2 \cdot 1 = 3$」），公式區同步展開。
  - hover cell $c_{ij}$ → 對應 $\mathbf{a}^*_i$（粉紅整橫條）+ $\mathbf{b}_j$（綠整直條）highlight 加粗外框。
- **(MM2) 模式輸出：**
  - $C$ 的每一直立列中段顯示「$A \mathbf{b}_j$」與展開 `$b_{1j} \mathbf{a}_1 + b_{2j} \mathbf{a}_2 + \ldots$」。
  - hover 結果某直立列 → 對應 $B$ 的該直立列 + 所有 $A$ 直立列同時 highlight（縮放係數對應 $b_{pj}$）。
- **(MM3) 模式輸出：**
  - $C$ 的每一橫躺行中段顯示「$\mathbf{a}^*_i B$」與展開 `$a_{i1} \mathbf{b}^*_1 + a_{i2} \mathbf{b}^*_2 + \ldots$」。
  - hover 結果某橫躺行 → 對應 $A$ 的該橫躺行 + 所有 $B$ 橫躺行同時 highlight。
- **(MM4) 模式輸出：**
  - $k$ 個秩 1 矩陣並排，每個顯示「$\mathbf{a}_p \mathbf{b}^*_p$」與具體元素網格（每個 cell 數字 = $a_{ip} \cdot b_{pj}$）。
  - 最右側「$=$ $C$」顯示累加結果。
  - hover 第 $p$ 個秩 1 矩陣 → 對應 $\mathbf{a}_p$（綠直條）+ $\mathbf{b}^*_p$（粉紅橫條）highlight。
- **公式區：** 即時 LaTeX，$AB = \cdots$（依模式顯示對應展開）。
- **左下角狀態列：** `mode: MM2 | shape: (3×2)(2×2) = (3×2) | rank ≤ 2`。

#### G. 互動行為（Interactions）
- **切換 mode tab：** 觸發轉視角動畫（見 §H）；公式區同步切換 LaTeX。
- **拉動 $a_{ij}$ slider：** 立即重算結果。當前模式對應的色塊內元素數值即時變化；(MM1) 模式下對應第 $i$ 橫躺行內第 $p$ 個元素亮一下；(MM4) 模式下對應第 $p$ 個秩 1 矩陣的「綠直立列」亮一下。
- **拉動 $b_{pj}$ slider：** 對稱行為。
- **拉動 $m, k, n$ slider：** 調整矩陣尺寸 — 色塊重繪 + slider grid 重建。**注意 $k$ 必須在 $A$ 列數與 $B$ 行數同步**（拉 $k$ 同時改兩邊形狀，視覺強化「中間維度對齊」概念）。
- **hover cell / 直立列 / 橫躺行 / 秩 1 圖層：** 見 §F。
- **快捷鍵：** `1` → MM1、`2` → MM2、`3` → MM3、`4` → MM4、`Space` → 依序循環、`R` → reset、`H` → 公式逐項高亮 toggle。

#### H. 動畫腳本（視角切換）
- **從 MM1 → MM2：**
  - **t=0：** MM1 穩態（$A$ 粉紅橫條堆 + $B$ 綠直條 + $C$ 棋盤交叉格）。
  - **t=0–200ms：** $C$ 棋盤格內粉紅橫條 fade out（opacity 1 → 0）；$A$ 的粉紅橫條合併成灰色實心方塊（每條從外向中心收攏 + 染色變灰）。
  - **t=200–500ms：** $C$ 棋盤格散開成 $n$ 個獨立直立綠條（每條從棋盤中抽出 + 對齊到 $B$ 直立列下方）。
  - **t=500–800ms：** $C$ 直立列各自加上漸層稀釋效果（提示「線組混合」）。
- **從 MM2 → MM3：**
  - **t=0–300ms：** $A$ 灰塊散開成 $m$ 條粉紅橫躺行；$B$ 從直立列合併成灰塊。
  - **t=300–600ms：** $C$ 從直立列轉為橫躺行（每條直立列旋轉 90° + 換色 → 粉紅橫躺）。
  - **t=600–800ms：** $C$ 橫躺行各自加上漸層稀釋。
- **從 MM3 → MM4：**
  - **t=0–200ms：** $A$ 粉紅橫躺行翻轉成綠直立列（每條旋轉 90° + 換色）；$B$ 灰塊散開成 $k$ 條粉紅橫躺行。
  - **t=200–500ms：** $C$ 橫躺行 fade out；同時在原本 $C$ 區域畫出 $k$ 個秩 1 矩陣（每個從中心放大到正常大小，stagger 60ms）。
  - **t=500–800ms：** 「$+$」號淡入於秩 1 矩陣之間，「$=$」與最終 $C$ 在最右側淡入。
- **從 MM4 → MM1（循環）：** 對應反向動畫。
- **總長度：** 800ms。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。
- **暫停 / 倒轉：** 是（動畫進行中切換立即 reverse）。

#### I. 邊界與錯誤處理
- **$k$ 不對齊（理論上 UI 不允許，但測試模式可手動觸發）：** 紅色閃爍提示「$A$ 列數 ≠ $B$ 行數」+ 計算被擋下。
- **$m, n, k$ 大尺寸（>5）：** cell 自動縮為 36×36 px；slider grid 改為可摺疊 panel。
- **動畫進行中再切換：** debounce 100ms 或佇列。
- **$A = 0$ 或 $B = 0$：** $C$ 全 0 + 灰色 + 提示「乘 0 矩陣」。
- **拖動 slider 過快：** debounce 30ms。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - MM1 tab：「每元素 = 一條橫躺行 · 一條直立列」
  - MM2 tab：「$C$ 的每一直立列 = $A$ 直立列的線性組合（係數來自 $B$ 對應直立列）」
  - MM3 tab：「$C$ 的每一橫躺行 = $B$ 橫躺行的線性組合（係數來自 $A$ 對應橫躺行）」
  - MM4 tab：「$AB$ = $k$ 個秩 1 矩陣相加 — §6 SVD 與低秩近似的鑰匙」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在是 MM1：$C$ 的每個元素是『$A$ 橫躺行 · $B$ 直立列』」
  - Step 2：「按 `2` 切到 MM2：$A$ 變灰塊、$B$ 仍是直立列、結果直立列是『$A\mathbf{b}_j$』」
  - Step 3：「按 `3` 切到 MM3：對稱於 MM2，這次 $B$ 變灰塊」
  - Step 4：「按 `4` 切到 MM4：$AB$ 變成 $k$ 個秩 1 矩陣之和 — 這是 SVD 的鑰匙！」
  - Step 5：「拉 $b_{pj}$ slider 看每個視角下變化的位置不同 — 但結果完全相同」
- **常見誤解警示：**
  - 「四個視角不是不同算法 — 是同一個 $AB$ 的四種讀法」
  - 「MM4 的 $k$ 是『內維度』，不是 $m$ 或 $n$」
- **延伸閱讀：** 原書 p.4、`ch04-mat-mat.md` 數學要點、Strang LAFE Sec. 1.4。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo（反應式 notebook）+ matplotlib + `matplotlib.animation.FuncAnimation`（控制視角切換動畫）+ marimo.ui。
- **替代方案：** Streamlit + Plotly + custom JS（如需高品質瀏覽器分享）。
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫粉紅橫條 / 綠直條 / 灰塊。
  - `matplotlib.transforms.Affine2D().rotate_deg_around()` 做橫 ↔ 直旋轉。
  - `matplotlib.collections.PatchCollection` 高效繪製大量秩 1 矩陣 cell。
  - `marimo.ui.tabs`（4 個視角切換）、`marimo.ui.slider`、`marimo.ui.array`（slider grid）。
  - `numpy.einsum('ip,pj->ij', A, B)` 計算結果。
- **檔案結構：**
  ```
  viz/
    ch04_matrix_matrix.py        # 主入口（含 VizScript-01 / 02 / 03 / 04 共用畫面 tab）
    _common/
      palette.py                 # 沿用 §1–§3 配色
      matrix_canvas.py           # §3 已建（橫條 / 直條 / 灰塊原語），§4 直接 import + 新增「秩 1 圖層」原語
      rank1_layer.py             # 新增：(MM4) 秩 1 矩陣繪製（綠直 + 粉紅橫「+」字交叉）
  ```
- **效能：** 動畫期間預先計算所有 frame 的色塊座標 / 顏色，存 list；動畫結束後切回 reactive。$k > 3$ 時 (MM4) 模式秩 1 圖層橫向排版改為兩排（避免畫布過寬）。
- **測試：** 動畫關鍵 frame（t=0 / 300 / 600 / 800）各 1 張 snapshot；4 個模式各 1 張靜態 snapshot；退化（$B = I$ / $B = 0$）各 1 張。

#### L. 驗收標準（Acceptance Criteria）
- [ ] 視角 tab 切換動畫總長 ≤ 800ms，60fps 無 frame drop。
- [ ] 拉 $a_{ij}$ / $b_{pj}$ slider 即時更新 $C$，並在當前模式對應位置高亮 200ms。
- [ ] hover $C$ 元素 / 直立列 / 橫躺行 / 秩 1 圖層 → 對應 $A, B$ 部分正確高亮。
- [ ] 公式區 LaTeX 渲染 < 50ms 完成。
- [ ] $k$ 改變時 $A$ 列數與 $B$ 行數同步更新（不允許不對齊）。
- [ ] $B = I$ 時 $C$ 與 $A$ 完全等價（視覺上可確認）。
- [ ] Walkthrough 5 步驟首次開啟自動觸發。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純並列四子圖靜態，無動畫切換。
- **Tier 3 擴充：** + 加 3D 視窗即時顯示 $A$ 列空間與 $B^{\mathrm{T}}$ 行空間的「列空間映射 = $C$ 列空間」幾何（與 §3 4-Subspaces 互動連接）。
- **估時：** 1.5 session（含測試與 walkthrough）

---

### VizScript-02: MM4 外積之和的逐項累加與秩截斷（Rank-1 Layer Accumulation + Rank-$k$ Truncation）— SVD 鋪陳

#### A. 一句話定位
拉「累加項數 $r$」slider 從 0 走到 $k$，看 $C$ 從全 0 逐項加上 $\mathbf{a}_p \mathbf{b}^*_p$ 秩 1 圖層、最終疊加成完整 $AB$；切換到「彩色圖像」demo 模式時，使用實際 64×64 像素影像（內建 4 張：Mona Lisa / 條紋 / 漸層 / 隨機）做 SVD 截斷，視覺展示「**前幾個秩 1 圖層保留主要結構、後面的只加細節**」。

#### B. 學習目標（Learning Outcome）
- 使用者能直觀感受「$AB$ = $k$ 個秩 1 矩陣相加」的視覺意義。
- 使用者能說出「每個 $\mathbf{a}_p \mathbf{b}^*_p$ 是一個秩 1 矩陣，所有直立列共線、所有橫躺行共線」。
- 使用者能解釋「秩 $r$ 截斷」概念：取前 $r$ 個秩 1 圖層 = 用 $r$ 個秩 1 矩陣近似原矩陣。
- 使用者能在「彩色圖像 demo」中觀察到「前 5–10 個 SVD 秩 1 圖層保留人臉 / 主要結構，後面的只在加紋理細節」。
- 使用者能在「秩 1 圖層重排序」交互中觀察到「按 $\sigma_p$ 大小排序的截斷品質遠好於隨機排序」 — 鋪陳 §6.5 Eckart–Young 定理。
- 使用者能說出「(MM4) 是 SVD 的鑰匙、是 PCA / 推薦系統 / 影像壓縮的核心」。

#### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$k$ 個秩 1 矩陣 $\mathbf{a}_p \mathbf{b}^*_p$、累加中間結果 $C_r = \sum_{p=1}^{r} \mathbf{a}_p \mathbf{b}^*_p$、目標 $C = AB$、誤差 $\|C - C_r\|_F$。
- **預設值（兩種模式）：**
  - **模式 1（小矩陣 demo）：** $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}$、$B = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$（$B = I_2$，使 $AB = A$，便於對比）；$k = 2$。
  - **模式 2（彩色圖像）：** $A, B$ 從 SVD 分解出（內建 64×64 灰階圖像 → $A = U \Sigma^{1/2}$、$B = \Sigma^{1/2} V^{\mathrm{T}}$），$k = 64$（full rank）。
- **維度範圍：**
  - 模式 1：$m \in [2, 6]$、$k \in [2, 5]$、$n \in [2, 6]$。
  - 模式 2：固定 $64 \times 64$，$k = 64$。
- **退化情形：**
  - $r = 0$：$C_r = 0$（全黑 / 全 0），誤差 $\|C\|_F$。
  - $r = k$：$C_r = C$（完美還原），誤差 0。
  - $\mathbf{a}_p = 0$ 或 $\mathbf{b}^*_p = 0$：該秩 1 圖層為 0，跳過不變化。
  - 兩個秩 1 圖層相同（共線）：累加時視為「方向重疊」用淡色提示。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 55% 主舞台 + 中 15% 秩 1 圖層 strip + 下 30% 控制列 + 圖表。
- **主舞台（左中右三區）：**
  - **左 30%：** $A$ + $B$ 原始矩陣顯示（$A$ 綠直立列 stack、$B$ 粉紅橫躺行 stack）。
  - **中 35%：** 「+」號 + $r$ 個秩 1 圖層相加結構 + 「$=$」+ 累加結果 $C_r$（cell 值即時更新，每個 cell 內字級隨數字長度自適應）。
  - **右 35%：** 目標 $C$ 與當前 $C_r$ 對比（兩個矩陣並列，差異用熱色 colormap 顯示 $|C - C_r|$）。模式 2 時改為「彩色圖像對比」：原圖 / 累加圖 / 誤差熱圖三張 64×64 像素影像。
- **秩 1 圖層 strip（中 15%）：** 橫向排列 $k$ 個秩 1 矩陣縮圖（每個 60×60 px），按「當前是否已被累加」分為亮色 / 灰色兩組；hover 縮圖顯示「$\mathbf{a}_p \mathbf{b}^*_p$」公式與其能量貢獻 $\|\mathbf{a}_p\| \cdot \|\mathbf{b}^*_p\|$（模式 2 顯示對應的 $\sigma_p$）。
- **下 30% 控制列：**
  - 上排：「累加項數 $r$」slider [0, $k$] + play / pause button + 「自動播放」speed slider。
  - 中排：模式切換 radio（小矩陣 / Mona Lisa / 條紋 / 漸層 / 隨機）+ 「重排序」radio（按 $\sigma_p$ 排序 / 按 $\|\mathbf{a}_p\|$ 排序 / 隨機排序 / 自訂順序）。
  - 下排：誤差曲線圖（橫軸 $r$、縱軸 $\|C - C_r\|_F$ / $\|C\|_F$，當前 $r$ 標紅點）。
- **配色：** $\mathbf{a}_p$ 綠 `#2ca02c`、$\mathbf{b}^*_p$ 粉紅 `#d62728`、秩 1 圖層 cell 用「藍 → 白 → 紅」連續 colormap（依數值正負）、累加結果 $C_r$ 用同 colormap。模式 2 用 gray colormap。
- **字型 / 字級：** 矩陣標題 18pt、cell 數字 12pt、圖層 strip 標籤 10pt、誤差曲線 12pt。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 累加項數 $r$ | slider | [0, $k$] | 0 | 即時 + 動畫 |
| play / pause | button | — | pause | click |
| 自動播放速度 | slider | 200ms – 2s / 項 | 700ms | 即時 |
| 模式 | radio | 小矩陣 / Mona Lisa / 條紋 / 漸層 / 隨機 | 小矩陣 | 切換重建 |
| 重排序 | radio | $\sigma_p$ 排序 / $\|\mathbf{a}_p\|$ 排序 / 隨機 / 自訂 | $\sigma_p$ | 即時重算 |
| $a_{ip}, b_{pj}$（小矩陣模式） | slider grid | [-9, 9] step 1 | 預設值 | 即時 |
| 顯示誤差熱圖 | checkbox | on / off | on | 即時 |
| 顯示能量貢獻 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click |

#### F. 輸出畫面細節（Outputs）
- **主舞台累加結果 $C_r$：**
  - 小矩陣模式：每 cell 顯示具體數字，數字字級隨整體尺寸自適應。
  - 圖像模式：64×64 灰階熱圖即時更新。
- **秩 1 圖層 strip：**
  - 已累加的圖層（$p \le r$）顯示飽和色 + 邊框深色；未累加（$p > r$）顯示淡灰色 + 邊框虛線。
  - 每個縮圖右下角標 `p`，下方標 $\sigma_p$（模式 2）或 $\|\mathbf{a}_p\| \|\mathbf{b}^*_p\|$（模式 1）。
- **目標 / 對比區：**
  - 上方：「目標 $C$」（不變）+ 「累加 $C_r$」（即時）。
  - 下方：「誤差 $|C - C_r|$」熱圖，紅色越深表示誤差越大。
  - 模式 2：三張 64×64 影像並列（原圖 / 重建圖 / 誤差圖）+ 「相對誤差 $\|C - C_r\|_F / \|C\|_F = 23.4\%$」即時數字。
- **誤差曲線圖：**
  - 橫軸 $r$，縱軸 $\|C - C_r\|_F / \|C\|_F$，曲線呈遞減（按 $\sigma_p$ 排序時下降最快）。
  - 當前 $r$ 用紅點 + 垂直虛線標記。
  - 不同重排序方式用不同顏色曲線（按 $\sigma_p$ 排序：粗藍實線；隨機排序：淡灰虛線；對比效果一目了然）。
- **公式區：** 即時 LaTeX `$C_r = \sum_{p=1}^{r} \mathbf{a}_p \mathbf{b}^*_p$`，並列出當前 $r$ 對應的具體展開項。

#### G. 互動行為（Interactions）
- **拉「$r$」slider 從 0 到 $k$：** 主舞台累加結果即時更新（每加 1 項，新秩 1 圖層從 strip 飛到主舞台中央 + 與當前累加結果做加法動畫 400ms）；strip 中對應圖層從灰變亮；誤差曲線紅點同步移動。
- **拉「$r$」slider 從 $k$ 到 0（倒退）：** 反向動畫，秩 1 圖層從累加結果中「飛回」strip + 變灰。
- **play 自動播放：** 依速度設定自動推進 $r$，從 0 走到 $k$ + 暫停 1 秒 + 從 $k$ 走回 0 循環。
- **切換模式：** 整個畫面重建（小矩陣 → 圖像模式時，所有 cell 變成像素網格）。
- **切換重排序：** 秩 1 圖層 strip 順序重排（300ms 動畫）+ 誤差曲線重繪（同色曲線淡化、新色曲線淡入）+ 提示「按 $\sigma_p$ 排序時前 5 項已覆蓋 87% 能量」之類的數字提示。
- **hover 秩 1 圖層 strip 某項：** 該項放大 1.2 倍 + 顯示詳細 tooltip（$\mathbf{a}_p$ / $\mathbf{b}^*_p$ 數值、能量、累積占比）；主舞台對應位置高亮。
- **快捷鍵：** `Space` play / pause、`→` $r$ += 1、`←` $r$ -= 1、`R` reset、`0` reset $r$ to 0、`Shift+End` $r$ to $k$、`M` 切換模式（依序循環）。

#### H. 動畫腳本（秩 1 圖層飛入累加）
- **新增第 $p$ 項（$r$ 從 $r$ 到 $r+1$）：**
  - **t=0：** strip 第 $p$ 項從灰色開始放大。
  - **t=0–150ms：** 該項放大 1.3 倍 + 從 strip 位置「彈出」朝主舞台中央飛入（位置插值 + 透明度 0.7 → 1）。
  - **t=150–350ms：** 該項抵達主舞台「+」號右側 + 縮回正常大小 + 顯示「$+ \mathbf{a}_p \mathbf{b}^*_p$」標籤。
  - **t=350–650ms：** 該項與當前累加結果合併 — 像素級疊加動畫（每個 cell 數值從舊值 lerp 到新值 + 顏色 colormap 同步插值，stagger 從左上到右下 5ms 一個 cell）。
  - **t=650–800ms：** 「+」號 / 「=」號 / 結果 $C_r$ 同步更新數字 + 誤差數字字級閃一下提示降低。
  - **strip 第 $p$ 項：** 從灰色轉為飽和色（150ms fade）。
- **總長度：** 800ms / 項。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。
- **倒退（$r$ 從 $r$ 到 $r-1$）：** 反向重播，秩 1 圖層從主舞台「飛回」strip。
- **自動播放：** 連續執行新增動畫，stagger 200ms（速度依 slider）。

#### I. 邊界與錯誤處理
- **$r = 0$：** 主舞台累加結果全 0 + 灰底；誤差曲線紅點在最左、誤差最大（= 100%）。
- **$r = k$：** 累加結果與目標 $C$ 完全相同（cell 值逐項對比可驗證）；誤差為 0；秩 1 圖層 strip 全亮。
- **拉 slider 過快：** debounce 50ms，動畫跳過中間幀直接到目標 $r$ 對應狀態（避免播放堆疊）。
- **圖像模式切換中：** 顯示 loading spinner 500ms；SVD 計算在 worker 執行，主執行緒不卡。
- **$\mathbf{a}_p = 0$ 或 $\mathbf{b}^*_p = 0$：** strip 該項標「dead layer」灰色標籤；累加時無變化。
- **重排序為「自訂」：** 顯示 drag handle 讓使用者拖曳 strip 改順序。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - 秩 1 圖層縮圖：「第 $p$ 個秩 1 矩陣 $\mathbf{a}_p \mathbf{b}^*_p$，能量 $\|\mathbf{a}_p\|\|\mathbf{b}^*_p\| = 17.3$」
  - $r$ slider：「累加前 $r$ 個秩 1 圖層 — 拉到 $k$ 即完整 $AB$」
  - 重排序選項：「按 $\sigma_p$ 排序的截斷是 Frobenius 範數下最佳近似（Eckart–Young 定理，§6.5）」
  - 誤差曲線：「累積保留能量比例 — 注意按 $\sigma_p$ 排序時前 5 項已覆蓋大部分能量」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在 $r = 0$，$C_r = 0$（全 0 矩陣 / 全黑影像）」
  - Step 2：「按 → 鍵或拉 slider 到 $r = 1$，看第 1 個秩 1 圖層飛入累加」
  - Step 3：「注意第 1 個秩 1 矩陣的『所有直立列共線、所有橫躺行共線』 — 這就是『秩 1』的定義」
  - Step 4：「繼續加到 $r = k$，看 $C_r$ 完全還原 $AB$」
  - Step 5：「切到『Mona Lisa』模式，看前 5–10 個秩 1 圖層已能還原人臉輪廓 — 這就是 SVD 壓縮的精髓」
  - Step 6：「切『隨機排序』看誤差曲線變差 — 說明『按 $\sigma_p$ 排序』才能最佳壓縮（§6.5 SVD 會證明）」
- **常見誤解警示：**
  - 「秩 1 矩陣不是『1 個元素的矩陣』 — 是『所有列共線』的矩陣」
  - 「(MM4) 對任何矩陣都可拆，不限 SVD — SVD 是『最佳化的 (MM4) 拆法』」
  - 「截斷 $r < k$ 不是『近似誤差』 — 是『有意丟掉小能量項』，是壓縮策略」
- **延伸閱讀：** 原書 p.4、§6.5 ($A = U \Sigma V^{\mathrm{T}}$)、Strang LAFE Sec. 1.4 + Sec. 7.4 Eckart–Young、`ch04-mat-mat.md` 數學要點 (MM4) 段。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib + matplotlib.animation + marimo.ui（小矩陣模式）；圖像模式建議 Plotly + Dash（heatmap 渲染更快、影像對比更專業）。
- **替代方案：** Streamlit（純 Python、部署簡單） + Plotly。
- **關鍵 API：**
  - `numpy.linalg.svd(image, full_matrices=False)` 計算 SVD（圖像模式）。
  - `numpy.einsum('p,ip,pj->ij', sigma[:r], U[:,:r], Vt[:r,:])` 計算秩 $r$ 重建。
  - `numpy.outer(a_p, b_p)` 計算秩 1 矩陣。
  - `matplotlib.image.imshow` / `plotly.express.imshow` 繪製熱圖。
  - `matplotlib.animation.FuncAnimation` 累加動畫（每 frame 更新 cell 數值）。
- **檔案結構：**
  ```
  viz/
    ch04_matrix_matrix.py
    _common/
      rank1_layer.py             # 共用秩 1 圖層繪製
      svd_demo.py                # 圖像 SVD 預先計算 + cache
    assets/
      mona_lisa_64.npy           # 64×64 灰階 numpy array
      stripes_64.npy
      gradient_64.npy
      random_64.npy
  ```
- **效能：** 圖像 SVD 預先計算並 cache 到 `assets/`；播放時只做切片運算（$O(64 \times 64 \times r)$）。
- **測試：** $r = 0, 1, k/2, k$ 各 1 張 snapshot；4 種圖像各 1 張（$r = 5, 10, 20, 64$）；誤差曲線 1 張。

#### L. 驗收標準（Acceptance Criteria）
- [ ] 拉 $r$ slider 從 0 走到 $k$，每加 1 項動畫 ≤ 800ms。
- [ ] 切換 4 種圖像模式無延遲（< 200ms 載入）。
- [ ] Mona Lisa 模式 $r = 10$ 時可清楚辨識人臉。
- [ ] 重排序「$\sigma_p$」與「隨機」對比下，前者誤差曲線明顯較陡。
- [ ] 累加動畫 60fps 無 frame drop（64×64 cell × 60fps × 64 frame = 245760 cell updates / sec OK）。
- [ ] hover 秩 1 圖層 strip 即時顯示能量數值。
- [ ] Walkthrough 6 步驟首次開啟自動觸發。
- [ ] $r$ 倒退時動畫反向，無視覺殘留。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 3
- **Tier 1 對應：** 純並列「目標 / 累加 / 誤差」三張靜態圖，無動畫。
- **Tier 2 對應：** 加 $r$ slider 控制累加項數 + 即時更新（無秩 1 圖層 strip）。
- **Tier 3 擴充（本版本）：** + 圖像 demo 4 張 + 重排序對比 + 誤差曲線 + 飛入動畫。
- **Tier 4 擴充（S12+ 可選）：** + 多影像並排對比（同一 $r$ 看不同影像的壓縮品質差異）+ 對應 SVD 「Mode 1 / Mode 2 / Mode 3」分解模式互動。
- **估時：** 2.5 session（含 4 張圖像準備、SVD 預計算、累加動畫、誤差曲線、Walkthrough 等；圖像模式是難點，Plotly Dash 整合需 0.5 session）

---

### VizScript-03: 維度檢核與內維對齊（Shape Validator）

#### A. 一句話定位
拉 $A, B$ 的尺寸 slider 即時看「$k$ 對齊 / 不對齊」綠紅燈號 + $(m \times k)(k \times n) = (m \times n)$ 形狀預測，並用色塊「能不能拼起來」的視覺暗示讓使用者體會「中間維度必須匹配」。

#### B. 學習目標（Learning Outcome）
- 使用者能在拉 slider 時即時判定 $AB$ 是否合法。
- 使用者能說出「$A$ 列數 = $B$ 行數」是矩陣乘法的唯一形狀條件。
- 使用者能根據 $A, B$ 形狀推測 $AB$ 形狀（拼起來 = 外維度組合）。

#### C. 待視覺化的數學物件
- $A \in \mathbb{R}^{m \times k_A}$、$B \in \mathbb{R}^{k_B \times n}$、合法條件 $k_A = k_B$。
- **預設值：** $m=3, k_A=k_B=2, n=2$（合法）。
- **維度範圍：** 各維度 $\in [1, 8]$。

#### D. 視覺布局
- 上 60% 視覺區：$A$ 灰塊（寬 $m$ cm × 高 $k_A$ cm 比例）+ $B$ 灰塊（寬 $k_B$ × 高 $n$）+ 「拼接示意」中間區（綠 / 紅圈圈）+ $AB$ 預測形狀（虛框）。
- 下 40% 控制列：$m, k_A, k_B, n$ 各一個 slider [1–8]，外加「強制 $k_A = k_B$」toggle。

#### E. 輸入控制
$m, k_A, k_B, n$ slider × 4 + `k 同步` toggle。

#### F. 輸出畫面細節
- $A, B$ 灰塊根據 slider 即時調整 aspect ratio。
- 中間「對齊圈」：$k_A = k_B$ 時顯示綠勾，否則紅叉 + 提示「$k_A = $ X ≠ Y = $k_B$」。
- $AB$ 預測形狀：合法時顯示綠虛框 $(m \times n)$ + 灰填充、不合法時顯示「— illegal —」與紅虛框。
- 公式區：合法時 LaTeX `$(m \times k)(k \times n) = (m \times n)$`；不合法時整段刪除線 + 紅字提示。

#### G. 互動行為
- 拉 slider 即時重繪 + 對齊圈狀態更新。
- toggle `k 同步` 為 on 時，拉 $k_A$ 自動同步 $k_B$（避免不合法）。
- hover $A$ 或 $B$ 灰塊：顯示「行 / 列數」標籤。

#### H. 動畫腳本
- 不合法 → 合法：紅叉淡出 + 綠勾淡入 200ms + $AB$ 虛框從紅變綠 + 灰填充淡入 300ms。
- 合法 → 不合法：反向。

#### I. 邊界與錯誤處理
- 維度 1：cell 變極小（4 px），改用文字標 "1"。
- 維度 8：cell 縮為 18 px。

#### J. 教學支援
- Tooltip：對齊圈 — 「中間維度匹配是矩陣乘法唯一形狀條件 — 若有疑問就拼一下『$A$ 列數』 vs 『$B$ 行數』」。

#### K. 技術實作建議
- Marimo + matplotlib (`Rectangle` + `Text`)，無動畫密集，純 reactive。

#### L. 驗收標準
- [ ] slider 即時響應 < 50ms。
- [ ] $k_A \ne k_B$ 時紅叉與紅虛框正確顯示。
- [ ] toggle `k 同步` 行為正確。

#### M. 互動深度 Tier + 估時
- **Tier 1**；估時 0.5 session。

---

### VizScript-04: MM1 點積 walkthrough（Per-Element Dot Product Tour）

#### A. 一句話定位
按播放鍵，從 $c_{11}$ 開始依序遍歷 $C$ 的每個元素，每個元素高亮對應 $\mathbf{a}^*_i$ 與 $\mathbf{b}_j$、播放點積計算過程（$a_{i1} \cdot b_{1j} + a_{i2} \cdot b_{2j} + \ldots$）、填入結果到對應 cell。

#### B. 學習目標
- 使用者能完整重現 (MM1) 點積計算流程。
- 使用者能將 (MM1) 公式與視覺色塊一一對應。

#### C. 待視覺化的數學物件
- $A, B, C$、每個元素 $c_{ij}$ 對應的 $\mathbf{a}^*_i$ 與 $\mathbf{b}_j$、點積中間值。
- **預設：** 原書範例（$m=3, k=2, n=2$）。

#### D. 視覺布局
- 與 VizScript-01 (MM1) 模式畫面共用。
- 增加一個底部 walkthrough panel（顯示當前算到的 $c_{ij}$ + 點積展開式）。

#### E. 輸入控制
- play / pause、speed slider、jump-to-cell (i, j)。

#### F. 輸出畫面細節
- 當前 $c_{ij}$ cell 內顯示展開式「$a_{i1} b_{1j} + a_{i2} b_{2j}$」+ 數字代入 + `=` + 最終值。
- 對應 $\mathbf{a}^*_i$ 與 $\mathbf{b}_j$ 加粗外框 + 亮色填充。
- 其他 cell 半透明 0.5。

#### G. 互動行為
- 自動播放：依序遍歷 $i = 1..m, j = 1..n$，每個 cell 暫停 1.5 秒。
- click 任意 cell 跳轉到該位置。

#### H. 動畫腳本
- 移到下個 cell：點積中間值「$a_{i1} \cdot b_{1j}$」浮現 → 「+ $a_{i2} \cdot b_{2j}$」浮現 → 「= $c_{ij}$」浮現 → 該 cell 填入結果。

#### I. 邊界與錯誤處理
- 大矩陣（$mn > 20$）：自動加速到 0.5 秒 / cell。

#### J. 教學支援
- Tooltip：點積中間值 — 「$a_{i1} b_{1j}$ 是 $\mathbf{a}^*_i$ 第 1 元素 × $\mathbf{b}_j$ 第 1 元素」。

#### K. 技術實作建議
- 與 VizScript-01 共用 ch04 主入口，新增 `walkthrough_mm1.py` 模組。

#### L. 驗收標準
- [ ] 自動播放遍歷所有 $c_{ij}$。
- [ ] click 任意 cell 跳轉正確。

#### M. 互動深度 Tier + 估時
- **Tier 1**；估時 0.5 session。

---

## 章末延伸與來源對照

### 與原書其他章節的連結
- **§1 (Viewing a Matrix - 4 Ways)：** 提供「橫躺行 / 直立列 / 元素 / 秩 1 之和」四種看 $A$ 的方式 → 直接套用到本章 $C = AB$ 的四種讀法。(MM1) ↔ 「個別元素」、(MM2) ↔ 「直立列家族」、(MM3) ↔ 「橫躺行家族」、(MM4) ↔ 「秩 1 之和」。
- **§2 (Vector × Vector - 2 Ways)：** (v2) 外積 → 秩 1 矩陣 = (MM4) 中每一項 $\mathbf{a}_p \mathbf{b}^*_p$ 的單獨型態。「§2 v2 是 §4 MM4 的單項。」
- **§3 (Matrix × Vector - 2 Ways + 4-Subspaces)：** (Mv2) = (MM2) 取 $B$ 為單一直立列 $\mathbf{b} \in \mathbb{R}^k$；(vM2) = (MM3) 取 $A$ 為單一橫躺行 $\mathbf{a}^* \in \mathbb{R}^{1 \times k}$。本章把 §3 的「兩個視角」推廣到「兩個矩陣的乘積」，從而出現第 4 個全新視角 (MM4)。
- **§5 (Practical Patterns)：** Pattern 1 / 2 / 1′ / 2′ / 3 都是 (MM2) 或 (MM3) 或 (MM4) 的特殊配置 — Pattern 1 = (MM2) 加 (Mv2)、Pattern 2 = (MM3) 加 (vM2)。本章是 §5 的數學基石。
- **§6 (Five Factorizations)：** 全部都是 (MM4) 的展開：
  - $A = CR$：$A = C R$ 是 (MM2) + (MM4)（$C$ 是 $A$ 獨立直立列、$R$ 是行操作；展開 $CR$ 即 $\sum_p \mathbf{c}_p \mathbf{r}^*_p$）。
  - $A = LU$：$LU$ 同 (MM4) 結構（$L$ 直立列 × $U$ 橫躺行），秩 1 之和的有限項。
  - $A = QR$：同 $LU$ 結構，但 $Q$ 的直立列正交。
  - $S = Q \Lambda Q^{\mathrm{T}}$：$S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$，對稱矩陣的 (MM4) 譜分解。
  - $A = U \Sigma V^{\mathrm{T}}$：$A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，最一般的 (MM4)，按 $\sigma_p$ 大小排序即最佳低秩近似（Eckart–Young）。

### 與工程實作的銜接
- **NumPy / PyTorch：** `A @ B` 預設以 (MM3) 模式實作（row-major 友善）；`numpy.einsum('ip,pj->ij', A, B)` 可指定其他模式。
- **BLAS：** Level 3 BLAS（GEMM）內部以 (MM4) 風格 + cache blocking 實現，把大矩陣拆成小區塊外積之和以利用 CPU cache。
- **GPU 矩陣乘法：** Tensor core 直接以 (MM1) + (MM4) 混合（4×4 點積 + 累加），與 NVIDIA Tensor Core 設計直接對應。
- **影像壓縮 / 推薦系統：** SVD 截斷即 (MM4) 取前 $r$ 項（如 Netflix Prize 用 $r \approx 50$ 個 latent factors 即可達到良好預測精度）。
- **神經網路反向傳播：** 鏈式法則 $\frac{\partial L}{\partial A} = \frac{\partial L}{\partial C} B^{\mathrm{T}}$ 是 (MM2) / (MM3) 應用 — 整個 PyTorch autograd 由 (MM1)–(MM4) 視角組合而成。

### 來源對照
- **`docs/book/from-tex/en.md`** 第 114–125 行（英文版 § Matrix times Matrix - 4 Ways）。
- **`docs/book/from-tex/zh.md`** 第 109–120 行（簡中版 § 矩阵乘以矩阵 - 4 个视角）。
- **`docs/book/from-pdf/en.txt`** Figure 6 對應段落（line 215–262）— 含 4 子圖具體展開。
- **`docs/book/figs-png/MatrixTimesMatrix.png`** 主圖（2×2 並列四子圖）。
- **Strang《Linear Algebra for Everyone》Sec. 1.4** (p.35) "Four Ways to Multiply $AB = C$" — 與本章順序完全一致。
- **書封底圖** — 原書封底重印此圖，是全書最具識別性的視覺標誌。

---

## 章節結束自檢清單

- [x] 摘要段點明四視角名稱 + 各自核心 + (MM4) 是 SVD 鑰匙
- [x] 數學要點覆蓋四個視角 + 對偶總表 + 與 §2 §3 傳承表 + 維度檢核 + 非交換律
- [x] (MM4) 段強調與 §6 五大分解的銜接
- [x] Figure 4.1 完整四欄描述（含四子圖獨立段落）
- [x] 4 個 VizMark + VizScript：⭐⭐⭐ × 2 完整 13 段 / ⭐⭐ × 1 精簡 13 段 / ⭐ × 1 輪廓
- [x] 章末延伸銜接 §1–§3 來源 + §5 §6 後續
- [x] 來源對照行數精確
- [x] 沿用 A 派術語（列 = column 直立、行 = row 橫躺）
- [x] 沿用全書視覺一致性錨點（配色 hex、cell 尺寸、動畫時間）
