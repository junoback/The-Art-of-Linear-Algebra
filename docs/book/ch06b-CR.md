# 6.1 矩陣分解 1：$A = CR$（Column–Row Factorization）

> **原書頁碼：** p.8–p.9
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.1 $A=CR$（en.md line 256–305 / zh.md line 248–293）
> **本章圖數：** 2（`CR1.png`、`CR2.png`，**原書圖中明標 using P1 / using P2**，與 §5 直接連結）
> **本章 VizMark 數：** 3（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成（S07）

---

## 章節摘要

$A = CR$ 是 §6 五大分解的**第一個**，也是教學上**最直觀**的一個。它的核心定理是：**任何**矩陣的「列秩 = 行秩」（column rank = row rank）— 這個事實本身令人意外（列空間 $\mathbf{C}(A)$ 在 $\mathbb{R}^m$、行空間 $\mathbf{C}(A^{\mathrm{T}})$ 在 $\mathbb{R}^n$，兩個維度不同的空間怎麼會有相同的維度數？），而 $A = CR$ 是把這個定理「**裝進一個矩陣等式裡**」的最簡潔說法。

具體流程：

1. **掃** $A$ 的列（column）從左到右，把**獨立列**留下放進 $C$，**依賴列**捨去；
2. 剩下的 $C$ 是 $m \times r$ 矩陣（$r$ = $A$ 的秩 / rank）；
3. 為了重建 $A$，右乘一個 $r \times n$ 的 **row reduced echelon form** $R$；
4. $A = C R$ 同時揭示：$C$ 有 $r$ 個獨立**列** → 列秩 = $r$；$R$ 有 $r$ 個獨立**行** → 行秩 = $r$；因為等式相同，列秩 = 行秩。

本章另一個關鍵點是**與 §5 Pattern 的視覺直接連結**：原書 CR1 圖在右下角畫 `using P1`、CR2 圖在右下角畫 `using P2`。這代表 $A = CR$ 的「列拆解」就是 §5 (P1) Pattern 1（「從右乘任意矩陣 → 列線性組合」）的特例；「行拆解」就是 §5 (P2) Pattern 2 的特例。本章 VizScript 因此採取**雙 pointer 策略**：(MM4) 累加 demo pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)；(P1)/(P2) 列縮放動畫 pointer 到 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)；本章只寫**獨立列高亮 + RREF 過程 + rank 視覺化**等 CR 特有的內容。

數值範例（本章貫穿）：

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 3 & 5 \end{bmatrix}
\;=\;
\underbrace{\begin{bmatrix} 1 & 2 \\ 2 & 3 \end{bmatrix}}_{C}
\underbrace{\begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{bmatrix}}_{R}
$$

讀者掃 $A$ 的列：列 1 $= (1, 2)^{\mathrm{T}}$、列 2 $= (2, 3)^{\mathrm{T}}$、列 3 $= (3, 5)^{\mathrm{T}} = $ 列 1 $+$ 列 2（依賴列）。捨去列 3，保留列 1、列 2 形成 $C$。$R$ 自動由「如何用 $C$ 的列拼回 $A$ 的列」推導：列 1 = $1 \cdot \mathbf{c}_1 + 0 \cdot \mathbf{c}_2$、列 2 = $0 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$、列 3 = $1 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$ → $R = \bigl[\begin{smallmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{smallmatrix}\bigr]$。

> ### 💡 背後觀念：A=CR 為什麼是「最樸素的分解」？「列秩 = 行秩」怎麼自然冒出？
>
> $A = CR$ 看起來不起眼 — 沒有正交化、沒有對角化、沒有三角結構，似乎只是把矩陣「拆成獨立列 × 組合係數」。為什麼 Strang 把它放在 §6 五大分解的**開門第一個**？背後其實藏著兩百年來未被代數封裝的「**rank 視覺化**」設計。2 條設計動機問題：
>
> - **[Q15：A=CR 為什麼成立？「列秩 = 行秩」怎麼自然冒出？](appendix-D-why.md#q15)** — Sylvester 1851 引入「rank」概念、Frobenius 1879 用子行列式給出「列秩 = 行秩」的系統證明 — 但這個流程繞了很大一圈技術細節。Strang 2020《LAFE》**首次把這個流程封裝為「分解 $A = CR$」** — 列秩 = 行秩變成**一行矩陣等式的兩個讀法**，不需任何技術證明。CR 是「**rank 的視覺載體**」+「**矩陣可以拆**」這個最低門檻概念的最直觀展示。
> - **[Q14：為什麼要把矩陣「分解」？](appendix-D-why.md#q14)** — CR 是 §6「**結構理解**」動機的典範。它告訴讀者：分解不只是為了算得更快、解方程更省事 — 分解也可以是為了**讓肉眼直接看見矩陣的結構**（rank、列空間維度 = 行空間維度）。後續 LU / QR / EVD / SVD 都是 CR 的「**結構增加版**」 — 在 CR 的基礎上多加對稱性、正交性、對角性。

---

## 數學要點

### 1. 定義與形狀

$$
A_{m \times n} = C_{m \times r} \, R_{r \times n}, \qquad r = \operatorname{rank}(A)
$$

- **$C$（Column matrix）：** $r$ 個**獨立列**，由 $A$ 從左到右掃描得到（不是任意 basis，是「按出現順序保留」的 basis）；
- **$R$（Row reduced echelon form）：** 把 $A$ 做 row reduction 直到變成 RREF 後，**去掉所有零行**得到的 $r \times n$ 矩陣；
- **$r$ 的視覺含義：** 在中間是「窄腰」，$C$ 矩陣寬 $r$、$R$ 矩陣高 $r$ — 視覺上 $A = CR$ 的「腰部」就是 rank。

### 2. 與 (MM4) 視角的連結 — 秩 1 之和

把 $A = CR$ 套用 §4 (MM4) 「列 × 行外積之和」視角：

$$
A = CR = \sum_{p=1}^{r} \mathbf{c}_p \, \mathbf{r}^{*}_p
$$

- $\mathbf{c}_p$ = $C$ 的第 $p$ 列（綠色直立）；
- $\mathbf{r}^{*}_p$ = $R$ 的第 $p$ 行（粉紅橫躺）；
- $\mathbf{c}_p \mathbf{r}^{*}_p$ 是一個秩 1 矩陣，視覺上是「綠色直立列 × 粉紅橫躺行」的網格；
- $A$ 是 $r$ 個秩 1 矩陣的**精確和**（不是近似 — 因為 $\operatorname{rank}(A) = r$，所以 $r$ 項剛好就能精確還原）。

**範例展開（$r = 2$）：**

$$
A = \mathbf{c}_1 \mathbf{r}^{*}_1 + \mathbf{c}_2 \mathbf{r}^{*}_2
= \begin{bmatrix}1\\2\end{bmatrix}\begin{bmatrix}1 & 0 & 1\end{bmatrix}
+ \begin{bmatrix}2\\3\end{bmatrix}\begin{bmatrix}0 & 1 & 1\end{bmatrix}
$$

逐項計算驗證：

$$
\begin{bmatrix}1 & 0 & 1\\ 2 & 0 & 2\end{bmatrix}
+ \begin{bmatrix}0 & 2 & 2\\ 0 & 3 & 3\end{bmatrix}
= \begin{bmatrix}1 & 2 & 3\\ 2 & 3 & 5\end{bmatrix} = A \;\checkmark
$$

### 3. 與 §5 (P1)/(P2) 的視覺連結 — using P1 / using P2 標記

原書 CR1 / CR2 兩張圖的**右下角**分別標 `using P1` 和 `using P2`，直接點明：

#### CR1 = (P1) 列觀點

$$
\underbrace{A = C R}_{\text{把 } A \text{ 的列用 } C \text{ 的列線組}} \quad\Leftrightarrow\quad \mathbf{a}_j = \sum_{p=1}^{r} R_{pj} \cdot \mathbf{c}_p
$$

**對照 §5 (P1)：** $A = \text{(diag) X (col)} \to$ 在 (P1) 中是「從右乘任意矩陣 → 結果矩陣的列 = 原矩陣列的線性組合」。在 CR 中，$A$ 的第 $j$ 列 $\mathbf{a}_j$ 由 $C$ 的兩個獨立列 $\mathbf{c}_1, \mathbf{c}_2$ 加權組成，權重就是 $R$ 的第 $j$ 行 $\mathbf{r}^{*}_j$ 的元素。**這是 (P1) 在「rank $r$ 的窄腰中」的特例**。

#### CR2 = (P2) 行觀點

$$
\underbrace{A = C R}_{\text{把 } A \text{ 的行用 } R \text{ 的行線組}} \quad\Leftrightarrow\quad \mathbf{a}^{*}_i = \sum_{p=1}^{r} C_{ip} \cdot \mathbf{r}^{*}_p
$$

**對照 §5 (P2)：** $A = \text{(row) X (diag)} \to$ 在 (P2) 中是「從左乘任意矩陣 → 結果矩陣的行 = 原矩陣行的線性組合」。在 CR 中，$A$ 的第 $i$ 行 $\mathbf{a}^{*}_i$ 由 $R$ 的兩個獨立行 $\mathbf{r}^{*}_1, \mathbf{r}^{*}_2$ 加權組成，權重就是 $C$ 的第 $i$ 行的元素。**這是 (P2) 在「rank $r$ 的窄腰中」的特例**。

**關鍵領悟（S07 PNG 重核重大發現）：** 原書 $A = CR$ 不是把 §5 Pattern 重新發明，而是**直接套用 §5 (P1)(P2) 來教證列秩 = 行秩**。這代表：

- **(P1) 視角看：** $A$ 的列空間 $\mathbf{C}(A) = \mathbf{C}(C)$（被 $C$ 的 $r$ 個列張成），維度 = $r$；
- **(P2) 視角看：** $A$ 的行空間 $\mathbf{C}(A^{\mathrm{T}}) = \mathbf{C}(R^{\mathrm{T}})$（被 $R$ 的 $r$ 個行張成），維度 = $r$；
- **兩者相等：** 同一個 $r$ 出現在兩邊 → **列秩 = 行秩**。

### 4. 列秩 = 行秩 — 為什麼這個定理「不顯然」

兩個空間的維度本來就**很容易不同**：

- $\mathbf{C}(A) \subseteq \mathbb{R}^m$ — 列空間住在 $m$ 維；
- $\mathbf{C}(A^{\mathrm{T}}) \subseteq \mathbb{R}^n$ — 行空間住在 $n$ 維。

$m \ne n$ 的長方矩陣（rectangular）兩個空間**整個**住在不同維度的環境裡。然而它們的**維度數**（也就是 basis 大小）卻必相等。例：$3 \times 5$ 矩陣，列空間最多 3 維、行空間最多 5 維 — 直覺上「行空間能容納更多獨立」，但實際上若 $A$ 的列秩 = 2，行秩**一定也是** 2，**不會是 3 或更高**。$A = CR$ 把這個「相等」**強迫到**同一個 $r$ 上：$C$ 的列數 = $R$ 的行數 = $r$。

**證明速覽：** 假設列秩 = $r$，從 $A$ 取出 $r$ 個獨立列形成 $C$，剩下的列都是 $C$ 列的線性組合。把這些「組合係數」整理成 $R$，自然 $A = CR$。觀察 $R$ 的行：$R$ 是「精簡」過的 RREF（除去零行），$r$ 個行**必獨立**（RREF 的非零行永遠獨立）→ 行秩 ≤ $r$。對稱地，從 $A^{\mathrm{T}}$ 起跑也能得行秩 = $r'$ 且必有 $A^{\mathrm{T}} = R'^{\mathrm{T}} C'^{\mathrm{T}}$，列秩 ≤ $r'$。兩個不等式合起來：列秩 = 行秩 = $r$。

### 5. 對 $A = CR$ 的 Procedure（從左到右掃描）

| 步驟 | 動作 | 矩陣狀態 |
|---|---|---|
| 1 | 取 $A$ 的列 1：非零，**保留**到 $C$ | $C \leftarrow [\mathbf{a}_1]$ |
| 2 | 取 $A$ 的列 2：檢查能否表為列 1 的線組（即是否為 $\alpha \mathbf{a}_1$ 形式）；若不能，**保留**到 $C$ | $C \leftarrow [\mathbf{a}_1, \mathbf{a}_2]$（若獨立） |
| 3 | 取 $A$ 的列 3：檢查能否表為列 1、列 2 的線組（$\beta_1 \mathbf{a}_1 + \beta_2 \mathbf{a}_2$）；若能，**捨去**（記下係數 $\beta_1, \beta_2$） | $C$ 不變；記 $\beta$ |
| ... | 重複至所有列掃完 | $C \in \mathbb{R}^{m \times r}$ |
| 末 | 把每列的「線組係數」整理成 $R$ 的對應行 | $R \in \mathbb{R}^{r \times n}$ |

**範例（$A = \bigl[\begin{smallmatrix}1 & 2 & 3 \\ 2 & 3 & 5\end{smallmatrix}\bigr]$）：**

- 列 1 = $(1, 2)^{\mathrm{T}}$：保留 → $\mathbf{c}_1$；
- 列 2 = $(2, 3)^{\mathrm{T}}$：$2 \neq \alpha \cdot 1$ 且 $3 \neq \alpha \cdot 2$ 對任何 $\alpha$，獨立，保留 → $\mathbf{c}_2$；
- 列 3 = $(3, 5)^{\mathrm{T}}$：嘗試 $\beta_1 (1, 2)^{\mathrm{T}} + \beta_2 (2, 3)^{\mathrm{T}} = (3, 5)^{\mathrm{T}}$ → $\beta_1 + 2\beta_2 = 3$、$2\beta_1 + 3\beta_2 = 5$ → $\beta_1 = 1, \beta_2 = 1$ → **依賴**，捨去；
- 整理係數：列 1 對應 $(1, 0)^{\mathrm{T}}$、列 2 對應 $(0, 1)^{\mathrm{T}}$、列 3 對應 $(1, 1)^{\mathrm{T}}$ → $R$ = 把這三個豎著拼成 $r \times n$ 矩陣 = $\bigl[\begin{smallmatrix}1 & 0 & 1 \\ 0 & 1 & 1\end{smallmatrix}\bigr]$；
- 驗證：$CR = \bigl[\begin{smallmatrix}1 & 2 \\ 2 & 3\end{smallmatrix}\bigr]\bigl[\begin{smallmatrix}1 & 0 & 1 \\ 0 & 1 & 1\end{smallmatrix}\bigr] = \bigl[\begin{smallmatrix}1 & 2 & 3 \\ 2 & 3 & 5\end{smallmatrix}\bigr] = A \checkmark$。

### 6. $A = CR$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **CR ↔ LU** | LU 是 CR 的「方陣 + 三角」特例。但 LU 對 $L, U$ 加了三角結構，CR 對 $C, R$ 只加「獨立」與「RREF」結構 |
| **CR ↔ QR** | QR 是「把 $C$ 正交化」的版本 — Gram–Schmidt 把 $C$ 變成 $Q$（正交列），把對應係數變成 $R$（上三角）。**從 CR 到 QR = 套一層 GS** |
| **CR ↔ SVD** | SVD 是「最對稱、最平衡」的 CR — 把 $C$ 變正交 $U$、把 $R$ 變正交 $V^{\mathrm{T}}$、中間插一個對角 $\Sigma$ 容納「縮放因子」。**從 CR 到 SVD = 兩端都正交化** |
| **CR ↔ QΛQᵀ** | QΛQᵀ 限對稱 $S$，且 $C$ 和 $R$ 不獨立（$C = Q$、$R = \Lambda Q^{\mathrm{T}}$） |

**結論：** $A = CR$ 是「**最少要求**」的分解（只要矩陣是矩陣就有），其他四個都是 CR 加各種「結構性」要求的特化。**從教學順序看：先教 CR 建立「分解 = 找出秩 + 拆兩塊」直覺，再教 LU/QR/QΛQᵀ/SVD 加各種結構**，是原書的設計邏輯。

### 7. 數學要點總結（一張表）

| 性質 | $A = CR$ 的對應 |
|---|---|
| 適用矩陣 | 任意 $m \times n$（含長方、退化） |
| $C$ 的列來源 | $A$ 從左到右掃描，獨立列保留 |
| $R$ 的本質 | 把每列表為「$C$ 列的線組」的係數矩陣（恰好是 RREF 去零行） |
| 「腰」的大小 | $r = \operatorname{rank}(A)$ |
| 列秩 = 行秩 證明 | $C$ 的 $r$ 獨立列 = 列秩；$R$ 的 $r$ 獨立行 = 行秩；同一個 $r$ |
| §4 (MM4) 對應 | $A = \sum_{p=1}^{r} \mathbf{c}_p \mathbf{r}^{*}_p$（秩 1 之和，$r$ 項） |
| §5 (P1) 對應 | CR1 圖明標：列觀點的 (P1)（$\mathbf{a}_j = \sum R_{pj} \mathbf{c}_p$） |
| §5 (P2) 對應 | CR2 圖明標：行觀點的 (P2)（$\mathbf{a}^{*}_i = \sum C_{ip} \mathbf{r}^{*}_p$） |
| 計算效率 | $O(mn^2)$（高斯消去），但教學上是「概念分解」，不是「算分解」 |

---

## 圖片詳細描述（Figure Descriptions）

### Figure 6.1: $CR$ 中的列秩（Column Rank in $CR$）— 標 using P1

**圖檔：** `docs/book/figs-png/CR1.png`（原始 EPS：`figs/CR1.eps`）
**原書頁碼：** p.8 圖 11
**所屬章節：** §6.1 $A=CR$（列觀點）

#### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，共 5 段，從左到右：

1. **第 1 段：** 矩陣 $A$ 的方框（灰色填充），框內畫出 **3 條等寬直立的灰色矩形**代表 $A$ 的 3 列；上方有大字 `A`；
2. **第 2 段：** 等號 `=` 大字；
3. **第 3 段：** 矩陣 $C$（方框框住 **2 條綠色直立列**），上方有大字 `C`，每條綠列下方有編號 `1`、`2`；
4. **第 4 段：** 矩陣 $R$（方框框住 **3 列藍/橙/紫色實心圓點對**，每列 2 個點上下排列），上方有大字 `R`；藍/橙/紫**色標對應 $A$ 的 3 列來源**（藍 = 列 1、橙 = 列 2、紫 = 列 3）；
5. **第 5 段：** 等號 `=` 大字；
6. **第 6 段：** 拆解結果，3 個直立列方框並排：
   - 第 1 列：藍·綠1 + （0·綠2 隱去）→ 顯示「藍1 + 綠 1」標記（即 $\mathbf{a}_1 = 1 \cdot \mathbf{c}_1$）；
   - 第 2 列：（0·綠1 隱去）+ 橙·綠2 → 顯示「橙 + 綠 2」標記（即 $\mathbf{a}_2 = 1 \cdot \mathbf{c}_2$）；
   - 第 3 列：紫·綠1 + 紫·綠2 → 顯示「紫 1 + 紫 2」標記（即 $\mathbf{a}_3 = 1 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$）；
7. **右下角圖示：** 圓圈內標 `P1`，文字 `using` — **直接標明「本圖用 §5 Pattern 1 視角」**。

**閱讀順序：** 由左到右讀整個等式鏈 `A = C R = （三列拆解）`。重點掃右側的 3 個拆解列，**藍 / 橙 / 紫色標**讓讀者立刻看出「每列從 $C$ 的兩列各取多少權重」。

#### 數學內容 (Mathematical Content)

對應數學表示：

$$
A = C R = \begin{bmatrix} | & | & | \\ \mathbf{a}_1 & \mathbf{a}_2 & \mathbf{a}_3 \\ | & | & | \end{bmatrix}
= \begin{bmatrix} | & | \\ \mathbf{c}_1 & \mathbf{c}_2 \\ | & | \end{bmatrix} \begin{bmatrix} R_{11} & R_{12} & R_{13} \\ R_{21} & R_{22} & R_{23} \end{bmatrix}
$$

第 $j$ 列展開（**(P1) Pattern 1**）：

$$
\mathbf{a}_j = R_{1j} \cdot \mathbf{c}_1 + R_{2j} \cdot \mathbf{c}_2
$$

對應 $A = \bigl[\begin{smallmatrix}1 & 2 & 3 \\ 2 & 3 & 5\end{smallmatrix}\bigr]$ 範例：

- $\mathbf{a}_1 = 1 \cdot \mathbf{c}_1 + 0 \cdot \mathbf{c}_2$（藍列 = 1·綠1，圖中只標藍 + 綠 1）；
- $\mathbf{a}_2 = 0 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$（橙列 = 1·綠2，圖中只標橙 + 綠 2）；
- $\mathbf{a}_3 = 1 \cdot \mathbf{c}_1 + 1 \cdot \mathbf{c}_2$（紫列 = 1·綠1 + 1·綠2，圖中標紫 1 + 紫 2）。

**顏色編碼的意義（藍 / 橙 / 紫）：** 用顏色代替數字權重，避免在小圖中塞滿小數字。藍 → $R$ 的第 1 行（對應 $A$ 的列 1）、橙 → $R$ 的第 2 行（對應 $A$ 的列 2）、紫 → $R$ 的第 3 行（對應 $A$ 的列 3 即依賴列）。

#### 直覺解讀 (Intuition)

CR1 是「**$A$ 的每一列都用 $C$ 的 2 個獨立列線組出來**」的視覺證明。讀者看右側 3 個拆解列，會立刻領悟：

- **獨立列（列 1、列 2）** 各只用了「自己對應的」$C$ 列一次（藍對綠 1、橙對綠 2），所以拆解圖只有單一綠塊；
- **依賴列（列 3）** 用了 $C$ 的兩列各一次（紫 + 綠 1、紫 + 綠 2），所以拆解圖有兩個綠塊；
- 「**列空間 $\mathbf{C}(A)$ 完全等於 $\mathbf{C}(C)$**」這個事實，從圖上「每列都是 $C$ 列的線組」直觀可見。

**「using P1」標籤的重要性（S07 PNG 重核發現）：** 原書作者**刻意**把這張圖標 `using P1`，等於明說「本圖就是 §5 Pattern 1 的應用」。視覺上看：

- §5 (P1) 圖是 `[列 1 ... 列 n] × diag(d_1, ..., d_n)` → 結果是「每列被 $d_p$ 縮放」；
- CR1 圖是 `[列 1, 列 2] × R` → 結果是「每列被 $R$ 的對應行線組」；
- (P1) 是 **「對角矩陣 R」** 的特例，CR1 是 **「任意 R」** 的一般版。

這個連結讓讀者把 §5 練的 (P1) 直覺**直接搬到** §6.1 — 無需重新建立心智模型，視覺化也可以**直接重用 ch05 VizScript-01 的對角矩陣互動**（只是把對角矩陣換成一般矩陣 $R$）。

**為什麼這張圖該做成互動視覺化？** 因為「獨立列 vs 依賴列」的判斷需要動態檢視 — 用戶調 $A$ 的元素，自動 highlight 哪些列被保留進 $C$、哪些被捨去；同時看到 $R$ 對應位置如何自動填出。靜態圖只能展示一個固定 $A$，互動 demo 可以讓用戶嘗試多種矩陣（含退化、含 rank 1 / 2 / 3）並即時看到 $C, R$ 的形狀變化。這是「列秩 = 行秩」定理感覺最深刻的時刻（見 VizMark-01）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [CR 拆解 + 獨立列高亮 + RREF 過程] ⭐⭐⭐
> 「拉桿調 $A$ 的元素 → 自動掃描獨立列 / 依賴列 → 動態組 $C$ / $R$ → 三色標記列來源（藍 / 橙 / 紫）」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [rank 與獨立列數對應] ⭐⭐
> 「用戶改 $A$ 的列讓 rank 變化（3 → 2 → 1 → 0），看 $C$ 的綠列數量同步變化 + $R$ 的形狀同步」
> **詳見劇本：** VizScript-02（章末，精簡版）

> 🎬 **VizMark-03** [2×3 範例 walkthrough] ⭐
> 「用書中範例 $\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$ 一步一步演示掃描過程，每步顯示『該列獨立還是依賴』」
> **詳見劇本：** VizScript-03（章末，輕量版）

---

### Figure 6.2: $CR$ 中的行秩（Row Rank in $CR$）— 標 using P2

**圖檔：** `docs/book/figs-png/CR2.png`（原始 EPS：`figs/CR2.eps`）
**原書頁碼：** p.8 圖 12
**所屬章節：** §6.1 $A=CR$（行觀點）

#### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**（與 CR1 同款式，但內容互換為行視角），共 5 段：

1. **第 1 段：** 矩陣 $A$ 的方框（灰色填充），框內畫出 **2 條等高橫躺的灰色矩形**代表 $A$ 的 2 行；上方有大字 `A`；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 矩陣 $C$（方框框住 **2 列 × 2 個藍/紫色實心圓點**），上方有大字 `C`；**藍點對應 $A$ 的行 1、紫點對應 $A$ 的行 2**；
4. **第 4 段：** 矩陣 $R$（方框框住 **2 條粉紅橫躺行**），上方有大字 `R`，每條粉紅行右側有編號 `1`、`2`；
5. **第 5 段：** 等號 `=`；
6. **第 6 段：** 拆解結果，2 個橫躺行方框並排（上下排列）：
   - 上行：藍·粉紅1 + 藍·粉紅2 → 顯示「藍 1 + 藍 2」（即 $\mathbf{a}^{*}_1 = $ 藍·$\mathbf{r}^{*}_1$ + 藍·$\mathbf{r}^{*}_2$）；
   - 下行：紫·粉紅1 + 紫·粉紅2 → 顯示「紫 1 + 紫 2」（即 $\mathbf{a}^{*}_2 = $ 紫·$\mathbf{r}^{*}_1$ + 紫·$\mathbf{r}^{*}_2$）；
7. **右下角圖示：** 圓圈內標 `P2`，文字 `using` — **直接標明「本圖用 §5 Pattern 2 視角」**。

**閱讀順序：** 由左到右讀整個等式鏈 `A = C R = （兩行拆解）`。重點掃右側的 2 個拆解行，**藍 / 紫色標**讓讀者立刻看出「每行從 $R$ 的兩行各取多少權重」。

**與 CR1 的對偶關係（重要）：**

| | CR1 | CR2 |
|---|---|---|
| 視角 | 列 (column) | 行 (row) |
| $A$ 的呈現 | 3 條直立灰列 | 2 條橫躺灰行 |
| $C$ 的呈現 | 2 條綠**直立列** | 2 列 × 2 個**藍紫點**（每行對應 $A$ 的一行） |
| $R$ 的呈現 | 3 列 × 2 個**藍橙紫點** | 2 條粉紅**橫躺行** |
| 拆解 | 3 個直立列 = $C$ 列的線組 | 2 個橫躺行 = $R$ 行的線組 |
| 標籤 | `using P1` | `using P2` |
| 直觀傳達 | 「$A$ 的列空間 = $C$ 的列空間」 | 「$A$ 的行空間 = $R$ 的行空間」 |
| 維度結論 | 列秩 = $r$（= $C$ 列數） | 行秩 = $r$（= $R$ 行數） |

**這對「對偶圖」是教學設計的傑作 —** 同一個 $A = CR$ 等式，從兩個視角（列 / 行）各畫一張，**兩張並排**讓讀者一秒領悟「列秩 = 行秩 = $r$」。

#### 數學內容 (Mathematical Content)

對應數學表示（**(P2) Pattern 2** 行視角）：

$$
A = C R, \qquad \mathbf{a}^{*}_i = \sum_{p=1}^{r} C_{ip} \cdot \mathbf{r}^{*}_p
$$

對應 $A = \bigl[\begin{smallmatrix}1 & 2 & 3 \\ 2 & 3 & 5\end{smallmatrix}\bigr]$ 範例：

- 行 1（$\mathbf{a}^{*}_1 = (1, 2, 3)$）= $1 \cdot \mathbf{r}^{*}_1 + 2 \cdot \mathbf{r}^{*}_2 = 1 \cdot (1,0,1) + 2 \cdot (0,1,1) = (1, 2, 3)$ ✓；
- 行 2（$\mathbf{a}^{*}_2 = (2, 3, 5)$）= $2 \cdot \mathbf{r}^{*}_1 + 3 \cdot \mathbf{r}^{*}_2 = 2 \cdot (1,0,1) + 3 \cdot (0,1,1) = (2, 3, 5)$ ✓；
- 圖中藍 / 紫色標代表 $C$ 的第 1 行（藍 = $(1, 2)$）和第 2 行（紫 = $(2, 3)$）。

#### 直覺解讀 (Intuition)

CR2 是「**$A$ 的每一行都用 $R$ 的 2 個獨立行線組出來**」的視覺證明。讀者看右側 2 個拆解行：

- $A$ 的行 1 用了 $R$ 的兩行（藍·$\mathbf{r}^{*}_1$ + 藍·$\mathbf{r}^{*}_2$），權重 = 藍 = $(1, 2)$；
- $A$ 的行 2 用了 $R$ 的兩行（紫·$\mathbf{r}^{*}_1$ + 紫·$\mathbf{r}^{*}_2$），權重 = 紫 = $(2, 3)$；
- 「**行空間 $\mathbf{C}(A^{\mathrm{T}})$ 完全等於 $\mathbf{C}(R^{\mathrm{T}})$**」這個事實，從圖上「每行都是 $R$ 行的線組」直觀可見。

**綜合 CR1 + CR2 的結論：**

- CR1：列空間維度 = $C$ 的列數 = $r$；
- CR2：行空間維度 = $R$ 的行數 = $r$；
- 同一個 $r$ → **列秩 = 行秩**。

**「using P2」標籤的重要性：** 與 CR1 同理，原書明標本圖是 §5 (P2) 的特例。視覺化可直接重用 ch05 VizScript-01 的對角矩陣互動，只是把 $C$ 的對角矩陣換成一般 $m \times r$ 矩陣。

**對 (P1)/(P2) 對偶的全書一致性：** §5 把 (P1)↔(P2) 寫成對偶總表，§6.1 把 CR1↔CR2 寫成對偶圖。**這個「對偶兩張圖」的視覺模式會在 §6.2 LU、§6.3 QR、§6.4 QΛQᵀ、§6.5 SVD 中重複出現**（每個分解都可以從列觀點和行觀點各畫一張）。S07 在寫 ch06b 時建議全書統一這個對偶圖模式，提升閱讀一致性。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [CR 拆解 + 行視角同步] ⭐⭐⭐
> 「同 CR1 的 VizMark-01，但加 toggle 切換『列視角 (CR1) / 行視角 (CR2) / 同時看兩者』三模式」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [rank 與獨立行數對應] ⭐⭐
> 「用戶改 $A$ 的行讓 rank 變化，看 $R$ 的粉紅行數量同步 + $C$ 的形狀同步」（VizScript-02 共用）

---

## 視覺化劇本（VizScripts）

### VizScript-01: CR 拆解 + 三色獨立列高亮 + RREF 動態過程（CR Toggle Animation）

**Tier：** ⭐⭐⭐ Tier 2（含對偶 CR1/CR2 切換 + RREF 計算動畫；秩 1 累加 demo pointer 到 ch04，(P1)/(P2) 列縮放動畫 pointer 到 ch05）
**對應 VizMark：** Figure 6.1 VizMark-01、Figure 6.2 VizMark-01
**預估實作工作量：** S12+ 約 2 session（畫面框架 1 session + 互動邏輯與 RREF 計算 1 session）

#### A. 一句話定位

「給一個 $A$，動態掃描獨立列、組出 $C$ 和 $R$，並切換列視角 (CR1) / 行視角 (CR2) / 同時看兩者，視覺驗證列秩 = 行秩。」

#### B. 學習目標（Learning Outcome）

- **獨立 / 依賴列辨識：** 看到一個矩陣，能一眼判斷哪些列獨立、哪些列是先前列的線組；
- **列秩 = 行秩 直覺：** 透過 CR1 和 CR2 兩張對偶圖**同時動態變化**，建立「$r$ 在兩邊都是 $r$」的視覺反射弧；
- **RREF 結構直覺：** 看到 $R$ 自動形成 RREF（識別矩陣 $I_r$ 嵌在「保留列」對應的欄、依賴列的係數填在其他欄）；
- **跨章連結：** 點 (P1)(P2) 按鈕跳 ch05 VizScript-01 看對角矩陣特例、點 (MM4) 按鈕跳 ch04 VizScript-02 看秩 1 累加。

#### C. 互動參數（UI Inputs）

- **矩陣輸入 $A$：** $m \times n$ 格子網格，$m \in [2, 5]$、$n \in [2, 6]$，每格 $a_{ij} \in [-9, 9]$ 步進 1；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$（書中範例，$r = 2$）；
  - 範例 2：$\bigl[\begin{smallmatrix}1&2&3\\2&4&6\end{smallmatrix}\bigr]$（$r = 1$，所有列共線）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&0&0\\0&1&0\\0&0&1\end{smallmatrix}\bigr]$（單位矩陣，$r = 3$，所有列獨立）；
  - 範例 4：$\bigl[\begin{smallmatrix}1&2&3&4\\2&4&6&8\\3&6&9&12\end{smallmatrix}\bigr]$（$r = 1$，三維列空間退化到一維）；
  - 範例 5：$\bigl[\begin{smallmatrix}1&1&0\\0&1&1\\1&0&1\end{smallmatrix}\bigr]$（**陷阱題**：看起來像獨立，實際 $r = 2$，列 3 = 列 1 + 列 2 − 列 2 ... 留給用戶探索）；
- **視角切換 (radio)：** `列視角 (CR1)` / `行視角 (CR2)` / `同時看兩者（並排）`；
- **掃描速度滑桿：** 自動掃描動畫的速度（0.5×–4×）；
- **跳轉按鈕：**
  - 「→ (P1)(P2) 對角矩陣特例」按鈕（跳 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)，自動把當前 $R$ 換成對角矩陣 $D$）；
  - 「→ (MM4) 秩 1 累加」按鈕（跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)，自動載入 $(\mathbf{c}_p, \mathbf{r}^{*}_p)$ 序列）。

#### D. 視覺布局（Layout）

**主畫面三區（並排視角時）：**

| 區 | 內容 |
|---|---|
| 左區（輸入） | $A$ 的格子輸入網格 + 預設範例選擇器 + 滑桿 |
| 中區（CR1 列視角） | $A$（灰列）= $C$（綠列）$R$（藍橙紫點陣）= 三列拆解（綠塊 + 三色標記）；底部 `using P1` 圖示 |
| 右區（CR2 行視角） | $A$（灰行）= $C$（藍紫點陣）$R$（粉紅行）= 兩行拆解（粉紅塊 + 兩色標記）；底部 `using P2` 圖示 |

**底部資訊條：**

- $r$ = 當前 rank（大字顯示）；
- $C$ 和 $R$ 的形狀（$m \times r$、$r \times n$）；
- 兩個跳轉按鈕。

#### E. 動畫流程（Animation Sequence）

**自動掃描模式（用戶按播放鈕）：**

1. **(0s) 初始：** $A$ 灰色顯示，$C$、$R$ 區域空白；
2. **(1s) 掃列 1：** $A$ 的列 1 變藍 → 「獨立」標記出現 → 列 1 飛入 $C$ 變綠 → $R$ 的第 1 行第 1 列填 1；
3. **(2s) 掃列 2：** $A$ 的列 2 變橙 → 嘗試用 $C$ 的當前列線組 → 不能 → 「獨立」標記出現 → 列 2 飛入 $C$ 變綠 → $R$ 的第 2 行第 2 列填 1；
4. **(3s) 掃列 3：** $A$ 的列 3 變紫 → 嘗試用 $C$ 的當前列線組 → **能**（$\beta_1 = 1, \beta_2 = 1$）→ 「依賴，捨去」標記出現 → 紫色係數填入 $R$ 的第 3 行；
5. **(4s) 結束：** $C$ 和 $R$ 完成，$A$ 整體高亮 + 顯示 `A = CR` 等式；
6. **(5s) 自動切到 CR2 視角：** 重新掃描，但這次以**行**為單位（藍 → 紫順序），展示行視角的線組；
7. **(6s) 並排顯示：** CR1 + CR2 同時顯示，兩邊都標 $r = 2$，**動態箭頭連線**強調「同一個 $r$」。

**手動互動模式：**

- 用戶改 $A$ 的某個元素，**整個畫面 600ms 重排動畫**：rank 重算 / $C$ 列數可能變化 / $R$ 重生 / 拆解列重組；
- 拉桿改 $a_{ij}$ 為連續值（即時更新），讓用戶看到「微擾不改變 rank」vs 「特定值跳變導致 rank 改變」的對比。

#### F. 預設 demo 序列（教學節奏）

1. **範例 1（書中範例 $\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$，$r = 2$）：** 預設啟動，自動掃描一次，建立基線理解；
2. **範例 4（退化 $r = 1$）：** 三列全部依賴，$C$ 只有 1 列、$R$ 只有 1 行，凸顯「退化矩陣的窄腰」；
3. **範例 3（單位矩陣 $I_3$，$r = 3$）：** 所有列獨立，$C = I$、$R = I$，凸顯「滿秩 = CR 退化為 $A = AI$」；
4. **範例 5（陷阱題）：** 用戶手動掃描，發現列 3 是依賴的（雖然第一眼看不出來），訓練「不要靠視覺判斷獨立性，要用線組驗證」的習慣。

#### G. 色彩與樣式

- 綠 `#2ca02c`（$C$ 的列、CR1 的拆解列、$Q^{\mathrm{T}}$ 同色）；
- 粉紅 `#d62728`（$R$ 的行、CR2 的拆解行）；
- 藍 `#1f77b4`（CR1 範例的列 1 標記、CR2 範例的行 1 標記）；
- 橙 `#ff7f0e`（CR1 範例的列 2 標記）；
- 紫 `#9467bd`（CR1 範例的列 3 標記、CR2 範例的行 2 標記，對應 §5 動態系統紫色）；
- 灰 `#cccccc`（$A$ 的占位 / 「依賴列被捨去」的剪頭線）。

**色彩設計原則：** 跟原書 CR1 / CR2 圖完全一致的「藍 / 橙 / 紫」色標，並與 §5 的對應色彩語義對接（紫色 = 「特殊」或「動態演化」的色）。

#### H. 公式同步區（Equation Sync Panel）

底部固定一個 LaTeX 公式區，依當前掃描狀態動態更新：

```
(初始)         A = ?
(掃完列1)      A = [c_1 ...] [1 ...] = ...
(掃完列2)      A = [c_1, c_2] [1 0; 0 1; ...] = ...
(掃完列3，列3依賴)  A = CR = [c_1, c_2] [1 0 1; 0 1 1]   ✓ rank = 2
```

**hover $C$ 的某列 → 高亮 $A$ 中對應的所有「使用該列的列」**（藍橙紫色重疊）；hover $R$ 的某行 → 高亮 $A$ 中對應的「以該行為基的行」。

#### I. 邊界條件與防呆

- **零矩陣：** $A = 0$ 時 $r = 0$、$C$ 和 $R$ 都是空矩陣，顯示「rank = 0，列空間 = 行空間 = {0}」；
- **單列矩陣：** $n = 1$ 時 $C = \mathbf{a}_1$、$R = [1]$（若 $\mathbf{a}_1 \neq 0$）；
- **rank 重算的數值穩定性：** 用「列向量是否與 $C$ 已有列的線組差 < $\epsilon$ = 1e-10」判定，不用嚴格 = 0；
- **退化視覺：** rank 變化時，被捨去的列顯示「→ 0」淡出動畫，不是直接消失（教學上要看到「被捨去」這個動作）。

#### J. 教學節奏建議

- **第 1 階段（0–2 分鐘）：** 預設範例 1 自動播放，建立「掃描 + 獨立 / 依賴 + 三色標記」的基線；
- **第 2 階段（2–5 分鐘）：** 切換 CR1 ↔ CR2 視角，看「列空間 / 行空間」的對偶；
- **第 3 階段（5–10 分鐘）：** 切到並排視角，**動態箭頭強調「同一個 $r$」**，建立列秩 = 行秩反射弧；
- **第 4 階段（10–15 分鐘）：** 嘗試不同預設範例，特別是退化（範例 4）和陷阱題（範例 5）；
- **第 5 階段（15+ 分鐘）：** 點跳轉按鈕，到 ch04/ch05 看 (MM4) 累加和 (P1)/(P2) 對角特例；回流時保持當前 $A$ 的設定。

#### K. 變化版本（Variation）

- **「教師模式」：** 加教師控制台，可逐步播放（一步一停）並用解說條解釋每步動作；
- **「測驗模式」：** 隨機生成矩陣，讓用戶手動標記獨立 / 依賴列，自動評分；
- **「歷史回放」：** 用戶調過的 $A$ 序列存在側邊欄，可回看歷次 $r$ 變化（建立「rank 是 robust 的」直覺）。

#### L. 跨章 pointer 細節

**Pointer 1：「→ (MM4) 秩 1 累加」（跳 ch04 VizScript-02）**

- 帶參數：$(\mathbf{c}_1, \mathbf{r}^{*}_1)$、$(\mathbf{c}_2, \mathbf{r}^{*}_2)$、...、$(\mathbf{c}_r, \mathbf{r}^{*}_r)$；
- ch04 VizScript-02 接收後自動載入 $r$ 個秩 1 層；
- 用戶在 ch04 看完累加動畫後，「返回 CR」按鈕跳回 ch06b 並保留當前 $A$。

**Pointer 2：「→ (P1)(P2) 對角矩陣特例」（跳 ch05 VizScript-01）**

- 帶參數：把 $R$ 強制改為對角矩陣 $D = \operatorname{diag}(R_{11}, R_{22}, ..., R_{rr})$；
- ch05 VizScript-01 演示 $CD$ 的列縮放（即 (P1) 特例）；
- 教學含義：「如果 $R$ 是對角，CR 就退化為 (P1) 列縮放；CR 是 (P1) 的一般化」。

#### M. 驗收條件（Acceptance Criteria）

- 用戶修改 $A$ 的任一元素，整個畫面 < 800ms 完成重排（含 rank 重算、$C$/$R$ 重組、三色重標）；
- CR1 ↔ CR2 視角切換動畫流暢（800ms ease-in-out，色塊重排不跳變）；
- 並排視角下，兩個 $r$ 標記**完全同步**變化（測試列秩 = 行秩的視覺一致性）；
- 範例 1 自動掃描完整跑完 ≤ 6 秒，每步驟（列 1 / 列 2 / 列 3）有明確的「獨立 / 依賴」標記出現；
- 兩個跳轉按鈕能正確帶參數跳到 ch04 / ch05 的對應 VizScript，且能正確返回；
- 退化矩陣（rank = 0、1）和滿秩矩陣的視覺呈現均正確（不出現「綠列 0 個」或「粉紅行 0 個」的崩潰）；
- 數值穩定性：用戶調 $a_{ij}$ 為「接近依賴」（如 $\epsilon$ 偏離整數），rank 不抖動。

---

### VizScript-02: rank 與獨立列 / 行數的對應動畫（Rank–Independence Tracker）

**Tier：** ⭐⭐ Tier 1（精簡 13 段，重點演示「改 $A$ 看 $r$ 變化」，不涉及 CR1/CR2 兩視角切換）
**對應 VizMark：** Figure 6.1 VizMark-02、Figure 6.2 VizMark-02
**預估實作工作量：** S12+ 約 0.5 session（重用 VizScript-01 的 rank 計算邏輯，畫面簡化）

#### A–C 簡述

- **定位：** 「用戶改 $A$ 的某一列為其他列的線組，看 $r$ 從 3 跳到 2，$C$ 的綠列數從 3 個降到 2 個、$R$ 的粉紅行數同步從 3 個降到 2 個」；
- **學習目標：** rank 是 $A$ 的「內在維度」，獨立於畫面表現；視覺看到 $r$ 和 $C/R$ 形狀的一致變化；
- **互動參數：** 預設 $3 \times 3$ 矩陣 + 滑桿可拉某列為其他列的線組（$\alpha, \beta$ 雙滑桿）。

#### D–F 簡述

- **布局：** 左區 $A$ 輸入 + $r$ 大字顯示、右區 $C$ / $R$ 並排（綠列 + 粉紅行）；
- **動畫：** 用戶拉滑桿讓 $\mathbf{a}_3 \to \alpha \mathbf{a}_1 + \beta \mathbf{a}_2$，rank 從 3 → 2 的瞬間 $C$ 的第 3 列「淡出 + 飛向 $R$ 的第 3 行作為線組係數」；
- **demo 序列：** rank 3 → rank 2（第 3 列被吸收） → rank 1（第 2 列也被吸收）→ rank 0（全零）。

#### G–M 簡述

- **色彩 / 公式：** 同 VizScript-01；
- **驗收：** rank 跳變的動畫流暢、$C/R$ 形狀變化與 rank 同步、退化情況不崩潰；
- **教學節奏：** 5 分鐘內讓用戶建立「rank 是 $A$ 的本質、$C/R$ 形狀是 rank 的視覺化」直覺。

---

### VizScript-03: 2×3 範例逐步 walkthrough（Step-by-step CR Demo）

**Tier：** ⭐ Tier 1（輕量版，僅針對書中範例 $\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$ 一步一步動畫）
**對應 VizMark：** Figure 6.1 VizMark-03
**預估實作工作量：** S12+ 約 0.3 session（硬編碼書中範例的步驟）

#### 簡述

- **定位：** 「用書中 $\bigl[\begin{smallmatrix}1&2&3\\2&3&5\end{smallmatrix}\bigr]$ 一步一步示範 CR 掃描，每步顯示『該列獨立還是依賴』+ 數值計算」；
- **互動：** 「下一步」按鈕逐步前進、「自動播放」按鈕、「重置」按鈕；
- **每步畫面：**
  - 步 1：「掃列 1，獨立，加入 $C$ 作為 $\mathbf{c}_1 = (1, 2)^{\mathrm{T}}$」；
  - 步 2：「掃列 2，嘗試 $\alpha \mathbf{c}_1$ 不能匹配 $(2, 3)$，獨立，加入 $C$ 作為 $\mathbf{c}_2 = (2, 3)^{\mathrm{T}}$」；
  - 步 3：「掃列 3，嘗試 $\beta_1 \mathbf{c}_1 + \beta_2 \mathbf{c}_2 = (3, 5)$ → $\beta_1 = 1, \beta_2 = 1$，依賴，捨去」；
  - 步 4：「完成 $A = CR$」+ 顯示完整公式 + 驗證乘法結果；
- **特色：** 適合初次學 CR 的讀者，可印刷成靜態 PDF 教材；
- **跨章 pointer：** 結束時顯示按鈕「→ 看其他範例（VizScript-01）」、「→ (P1)(P2) 對角特例（ch05）」、「→ (MM4) 秩 1 累加（ch04）」。

---

## 章末延伸

- **後續章節連結：**
  - [→ ch06c-LU.md](ch06c-LU.md)（§6.2 $A=LU$ — Gaussian 消去法的 CR 三角化升級）
  - [→ ch06d-QR.md](ch06d-QR.md)（§6.3 $A=QR$ — CR 的正交化升級，$C$ 變正交 $Q$）

- **前置章節傳承：**
  - [← ch04-mat-mat.md](ch04-mat-mat.md) §4 (MM4)：$A = \sum \mathbf{c}_p \mathbf{r}^{*}_p$ 母模板；
  - [← ch05-patterns.md](ch05-patterns.md) §5 (P1)/(P2)：CR1 = (P1) 列觀點、CR2 = (P2) 行觀點 — **原書直接標 `using P1` / `using P2`**；
  - [← ch06a-five.md](ch06a-five.md) §6 總覽：CR 是 5 大分解的「最少要求」起點。

- **延伸閱讀：**
  - Gilbert Strang《Linear Algebra for Everyone》§1.4「Matrix Multiplication and $A = CR$」p.29 — 本章原始來源；
  - Strang《Linear Algebra for Everyone》§3.2「Independent Columns and the Column Space」— RREF 計算細節；
  - 附錄 `World_of_Matrices.png` — CR 在矩陣世界地圖中是「最一般」的起點。

- **對 RREF 計算的補充：** 本章只演示「依結果說明 $R$」，沒詳述「如何由 $A$ 計算 RREF」— Gaussian 消去法的細節留給 §6.2 LU 章。讀者若需要對應的數值算法，可看：
  - Trefethen & Bau《Numerical Linear Algebra》Lecture 20 (Gaussian elimination with partial pivoting)；
  - SciPy `scipy.linalg.lu` / NumPy `numpy.linalg.matrix_rank` 等工程實作。

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` §6.1 $A=CR$（en.md line 256–305）/ `The-Art-of-Linear-Algebra.pdf` p.8–p.9（含圖 11、12）
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` §6.1 $A=CR$（zh.md line 248–293）
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0

---

> **撰寫者註（S07）：** 本章是 §6 五大分解的「第一章詳細版」。**S07 重大發現：** 原書 CR1/CR2 圖明標 `using P1` / `using P2`，**直接連結到 §5 (P1)(P2) Pattern**。這意味著 §6.1–§6.5 都會把 §5 Pattern 標籤套到對應的分解視角圖上（後續章節需逐章核對 PNG 是否有 `using PX` 標記，可能影響 VizScript 跨章 pointer 設計）。本章 VizScript-01 因此採取**雙 pointer 策略**：(MM4) 累加 → ch04 VizScript-02；(P1)(P2) 對角特例 → ch05 VizScript-01。本策略首次驗證「同一 VizScript 雙向 pointer」可行性，後續 §6.2–§6.5 可複用。
