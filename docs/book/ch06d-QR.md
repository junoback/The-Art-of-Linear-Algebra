# 6.3 矩陣分解 3：$A = QR$（Orthogonal × Upper Triangular Factorization）

> **原書頁碼：** p.10–p.11
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.3 $A=QR$（en.md line 379–429 / zh.md line 367–415）
> **本章圖數：** 1（`QR.png`，原書圖中明標 **using P1**）
> **本章 VizMark 數：** 3（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成（S08）

---

## 章節摘要

$A = QR$ 是 §6 五大分解的**第三個**，是把 LU 的「下三角 $L$」**升級為正交 $Q$** 的版本。它的核心過程是**格拉姆–施密特正交化**（Gram–Schmidt orthogonalization）：把 $A$ 的**列**（columns）一個一個處理，每一列都「**減去前面已產生的正交列方向**」再單位化，得到正交基底 $\mathbf{q}_1, \mathbf{q}_2, \ldots, \mathbf{q}_n$。

具體流程：

1. **$\mathbf{q}_1$：** 直接把 $\mathbf{a}_1$ 單位化：$\mathbf{q}_1 = \mathbf{a}_1 / \|\mathbf{a}_1\|$；
2. **$\mathbf{q}_2$：** 把 $\mathbf{a}_2$ **減去** $\mathbf{q}_1$ 方向的投影，再單位化：$\mathbf{q}_2 = (\mathbf{a}_2 - (\mathbf{q}_1^{\mathrm{T}} \mathbf{a}_2) \mathbf{q}_1) / \|\cdots\|$；
3. **$\mathbf{q}_3$：** 把 $\mathbf{a}_3$ **減去** $\mathbf{q}_1, \mathbf{q}_2$ 兩個方向的投影，再單位化；
4. ⋯ 重複至所有列處理完。

**反推 $R$：** 上面流程**留下的乘數**（投影係數 $r_{ij} = \mathbf{q}_i^{\mathrm{T}} \mathbf{a}_j$）和「單位化的縮放因子」（$r_{ii} = \|\cdots\|$）整理成**上三角矩陣** $R$，自然滿足 $A = QR$。

**核心不變量：** $Q$ 的列空間 = $A$ 的列空間（$\mathbf{C}(Q) = \mathbf{C}(A)$）— Gram–Schmidt **不改變 $A$ 撐起的空間**，只**重新挑一組正交的基底**來描述同一個空間。這是 QR 與 LU 的關鍵差異：

| 性質 | $A = LU$ | $A = QR$ |
|---|---|---|
| $Q$ 或 $L$ 的特性 | 下三角 | **正交**（$Q^{\mathrm{T}} Q = I$）|
| 另一側 $U$ 或 $R$ | 上三角 + 主元 | 上三角 + Gram–Schmidt 縮放因子 |
| 與 $A$ 的關係 | $L$ 記錄消去步驟 | $Q$ 是 $A$ 的正交化結果 |
| 空間不變量 | 無直接結構 | $\mathbf{C}(A) = \mathbf{C}(Q)$ |
| 主要用途 | 解 $A\mathbf{x} = \mathbf{b}$ | 最小平方法（least squares）/ 求正交基底 |
| `using` 標記 | LU2 標 (MM4)，LU1 無標 | QR 標 **(P1)** |

**`using P1` 標記的意義（S08 PNG 重核發現）：** 原書 `QR.png` 右下角圓圈標 `P1`，明示「QR 圖的視覺視角是 §5 Pattern 1」— **「從右乘上三角矩陣 $R$，等於把 $Q$ 的列做線性組合」**。這跟 §6.1 CR1 的 `using P1` 是同一個 Pattern，**但 QR 多了「Q 列正交」的特殊性質**。

**本章 VizScript 策略：** ⭐⭐⭐ VizScript-01 採**單 pointer 策略** — (P1) 列線性組合動畫 pointer 到 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)；本章獨立寫的是 **Gram–Schmidt 正交化過程動畫 + 3D 投影視覺 + $\mathbf{C}(A) = \mathbf{C}(Q)$ 不變量演示** 等 QR 特有的內容。

數值範例（本章貫穿）：

$$
A = \begin{bmatrix} 1 & 2 \\ 1 & 0 \end{bmatrix}
\;=\;
\underbrace{\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}}_{Q}
\underbrace{\sqrt{2}\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}}_{R}
$$

驗證：

1. $\mathbf{a}_1 = (1, 1)^{\mathrm{T}}$，$\|\mathbf{a}_1\| = \sqrt{2}$，$\mathbf{q}_1 = (1, 1)^{\mathrm{T}}/\sqrt{2}$；$r_{11} = \sqrt{2}$；
2. $r_{12} = \mathbf{q}_1^{\mathrm{T}} \mathbf{a}_2 = (2 + 0)/\sqrt{2} = \sqrt{2}$；
3. $\mathbf{w}_2 = \mathbf{a}_2 - r_{12} \mathbf{q}_1 = (2, 0)^{\mathrm{T}} - \sqrt{2} \cdot (1, 1)^{\mathrm{T}}/\sqrt{2} = (2, 0)^{\mathrm{T}} - (1, 1)^{\mathrm{T}} = (1, -1)^{\mathrm{T}}$；
4. $\|\mathbf{w}_2\| = \sqrt{2}$，$r_{22} = \sqrt{2}$，$\mathbf{q}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$；
5. 驗證 $Q^{\mathrm{T}} Q = I_2$（兩列正交、單位）+ $QR = A$ ✓。

> ### 💡 背後觀念：A=QR 為什麼需要正交化？Gram-Schmidt 從哪冒出來？
>
> $A$ 本身已經是個明確的矩陣 — 為什麼要費力把它「正交化」？Gram-Schmidt 看起來像個技巧（投影 → 扣減 → 標準化逐步重複），為什麼它能成為**線代基石**？最小平方法為什麼一定要用 QR 而不是「正規方程」 $A^{\mathrm{T}}A\mathbf{x} = A^{\mathrm{T}}\mathbf{b}$？1 條設計動機問題：
>
> - **[Q17：A=QR 為什麼需要正交化？Gram-Schmidt 從哪冒出來？](appendix-D-why.md#q17)** — QR 的歷史是 200 年「**從最小平方法到 Hilbert 空間**」的演化：**Gauss 1801** 用最小平方法算 Ceres 軌道（最小平方法首次重大應用）→ Legendre 1805 獨立發表 → Gauss 1809 系統化正規方程 → **Gram 1883 與 Schmidt 1907** 在最小平方法與 Hilbert 空間框架下系統化正交化 → **Householder 1958** 數值穩定演算法。Gram-Schmidt 的核心動作是「**逐步扣除耦合**」 — 每一步把當前向量中**已被前面 $\mathbf{q}_i$ 覆蓋的成分**減掉，剩下的就是「真正新增的方向」。**「正交基底 = 無耦合的最佳座標」** 是 QR 的核心哲學：對正交基底任意向量的座標 $c_k = \mathbf{q}^{\mathrm{T}}_k \mathbf{v}$ 可逐個獨立計算，不需解任何方程組。最小平方法為什麼用 QR：**$Q$ 正交保長度，不放大條件數**（傳統正規方程會把條件數平方化導致數值失準）。QR 也是 EVD / SVD 的數值前置工具 —「**分解化是把演算法封裝為代數物件的標準路徑**」這個思想貫穿全 §6。

---

## 數學要點

### 1. 定義與形狀

$$
A_{m \times n} = Q_{m \times n} \, R_{n \times n}, \qquad Q^{\mathrm{T}} Q = I_n
$$

- **$Q$（Orthogonal columns）：** $m \times n$ 矩陣，**列兩兩正交且單位長**（orthonormal columns）：$\mathbf{q}_i^{\mathrm{T}} \mathbf{q}_j = \delta_{ij}$（$i = j$ 時為 1，否則為 0）。若 $m = n$（方陣），$Q$ 是「正交矩陣」（orthogonal matrix），$Q^{-1} = Q^{\mathrm{T}}$；
- **$R$（Upper triangular）：** $n \times n$ 上三角矩陣，**對角線元素是 Gram–Schmidt 的「縮放因子」** $r_{ii} = \|\mathbf{w}_i\|$（向量單位化前的長度），對角線上方填 $r_{ij} = \mathbf{q}_i^{\mathrm{T}} \mathbf{a}_j$（投影係數）；
- **形狀（thin QR）：** $A$ 是 $m \times n$（通常 $m \geq n$），$Q$ 也是 $m \times n$（與 $A$ 同形）、$R$ 是 $n \times n$；
- **可分解條件：** $A$ 的列必須線性獨立（rank $= n$），否則 Gram–Schmidt 過程中會出現 $\mathbf{w}_p = \mathbf{0}$。

### 2. Gram–Schmidt 正交化過程（核心 ⭐）

**遞迴公式（正向，從 $\mathbf{a}_p$ 求 $\mathbf{q}_p$）：**

$$
\mathbf{w}_p = \mathbf{a}_p - \sum_{k=1}^{p-1} (\mathbf{q}_k^{\mathrm{T}} \mathbf{a}_p) \mathbf{q}_k, \qquad
\mathbf{q}_p = \frac{\mathbf{w}_p}{\|\mathbf{w}_p\|}
$$

**逐步分解：**

1. **減投影：** $\mathbf{w}_p$ 是 $\mathbf{a}_p$ **減去**它在前 $p-1$ 個 $\mathbf{q}_k$ 方向的投影 — 結果 $\mathbf{w}_p$ 與所有 $\mathbf{q}_1, \ldots, \mathbf{q}_{p-1}$ **正交**；
2. **單位化：** $\mathbf{q}_p = \mathbf{w}_p / \|\mathbf{w}_p\|$ 把 $\mathbf{w}_p$ 縮成單位長度；
3. **記錄縮放：** $r_{pp} = \|\mathbf{w}_p\|$（縮放因子，存入 $R$ 對角線）；
4. **記錄投影係數：** $r_{kp} = \mathbf{q}_k^{\mathrm{T}} \mathbf{a}_p$（$k < p$，存入 $R$ 對角線上方）。

**範例（本章 2×2 範例展開）：**

第 1 列 $\mathbf{a}_1 = (1, 1)^{\mathrm{T}}$：
- $\mathbf{w}_1 = \mathbf{a}_1 = (1, 1)^{\mathrm{T}}$（無投影要減）；
- $r_{11} = \|\mathbf{w}_1\| = \sqrt{2}$；
- $\mathbf{q}_1 = \mathbf{w}_1 / \sqrt{2} = (1, 1)^{\mathrm{T}} / \sqrt{2}$。

第 2 列 $\mathbf{a}_2 = (2, 0)^{\mathrm{T}}$：
- $r_{12} = \mathbf{q}_1^{\mathrm{T}} \mathbf{a}_2 = (1 \cdot 2 + 1 \cdot 0)/\sqrt{2} = 2/\sqrt{2} = \sqrt{2}$；
- $\mathbf{w}_2 = \mathbf{a}_2 - r_{12} \mathbf{q}_1 = (2, 0)^{\mathrm{T}} - \sqrt{2} \cdot (1, 1)^{\mathrm{T}}/\sqrt{2} = (2, 0)^{\mathrm{T}} - (1, 1)^{\mathrm{T}} = (1, -1)^{\mathrm{T}}$；
- $r_{22} = \|\mathbf{w}_2\| = \sqrt{1 + 1} = \sqrt{2}$；
- $\mathbf{q}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$。

**驗證正交性：**

- $\mathbf{q}_1^{\mathrm{T}} \mathbf{q}_2 = (1 \cdot 1 + 1 \cdot (-1))/2 = 0$ ✓；
- $\|\mathbf{q}_1\| = 1, \|\mathbf{q}_2\| = 1$ ✓。

### 3. 與 (P1) 視角的連結 — 反向公式：$\mathbf{a}_p = \sum r_{kp} \mathbf{q}_k$（核心 ⭐）

把第 2 節的「正向」流程**反過來**寫，得到 **(P1) 視角的核心公式**：

$$
\mathbf{a}_p = r_{pp} \mathbf{q}_p + \sum_{k=1}^{p-1} r_{kp} \mathbf{q}_k = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k
$$

**展開（本章 2×2 範例）：**

- $\mathbf{a}_1 = r_{11} \mathbf{q}_1 = \sqrt{2} \cdot (1, 1)^{\mathrm{T}}/\sqrt{2} = (1, 1)^{\mathrm{T}}$ ✓；
- $\mathbf{a}_2 = r_{12} \mathbf{q}_1 + r_{22} \mathbf{q}_2 = \sqrt{2} \cdot (1, 1)^{\mathrm{T}}/\sqrt{2} + \sqrt{2} \cdot (1, -1)^{\mathrm{T}}/\sqrt{2} = (1, 1)^{\mathrm{T}} + (1, -1)^{\mathrm{T}} = (2, 0)^{\mathrm{T}}$ ✓。

**整理成矩陣等式：**

$$
A = \begin{bmatrix} | & | & & | \\ \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \\ | & | & & | \end{bmatrix}
= \begin{bmatrix} | & | & & | \\ \mathbf{q}_1 & \mathbf{q}_2 & \cdots & \mathbf{q}_n \\ | & | & & | \end{bmatrix}
\begin{bmatrix} r_{11} & r_{12} & \cdots & r_{1n} \\ & r_{22} & \cdots & r_{2n} \\ & & \ddots & \vdots \\ & & & r_{nn} \end{bmatrix} = QR
$$

**對照 §5 (P1)：** 「**右乘任意矩陣 = 左矩陣的列做線性組合**」。

- §5 (P1) 一般形式：$AB$ 的第 $j$ 列 = $A$ 的列的線性組合（係數 = $B$ 的第 $j$ 行）；
- QR 特化：$A$ 的第 $p$ 列 = $Q$ 的列的線性組合（係數 = $R$ 的第 $p$ 行，**只有上面 $p$ 個非零**因為 $R$ 上三角）。

**「using P1」標籤的意涵：** 原書 `QR.png` 標 `using P1`，直接點明「QR 圖就是 (P1) 在『$R$ 上三角』情形下的應用」。**這比 CR 的 (P1) 標記更精細** — CR 的 $R$ 是「RREF 不一定上三角」，QR 的 $R$ **強制上三角**，使得「$\mathbf{a}_p$ 只用 $\mathbf{q}_1, \ldots, \mathbf{q}_p$（前 $p$ 個）來組成」這個視覺特徵更強烈。

### 4. 不變量：$\mathbf{C}(A) = \mathbf{C}(Q)$（列空間相等）

**核心定理：** Gram–Schmidt 過程**不改變 $A$ 的列空間**，只重新選一組正交基底：

$$
\mathbf{C}(A) = \operatorname{span}\{\mathbf{a}_1, \ldots, \mathbf{a}_n\}
= \operatorname{span}\{\mathbf{q}_1, \ldots, \mathbf{q}_n\} = \mathbf{C}(Q)
$$

**證明（雙向包含）：**

- **$\mathbf{C}(Q) \subseteq \mathbf{C}(A)$：** 從 Gram–Schmidt 流程看，$\mathbf{q}_p$ 是 $\mathbf{a}_1, \ldots, \mathbf{a}_p$ 的線性組合（減投影 + 縮放），所以每個 $\mathbf{q}_p$ 都在 $\mathbf{C}(A)$ 中；
- **$\mathbf{C}(A) \subseteq \mathbf{C}(Q)$：** 從反向公式 $\mathbf{a}_p = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k$ 看，每個 $\mathbf{a}_p$ 都在 $\mathbf{C}(Q)$ 中。

**結論：** 兩集合**互相包含 → 相等**。**這個不變量是 QR 在「最小平方法」中發揮作用的關鍵** — 因為「最小平方法 = 投影到 $\mathbf{C}(A)$」，而 $\mathbf{C}(A) = \mathbf{C}(Q)$，所以可以用「投影到正交基底 $Q$ 的列」來替代複雜的「投影到一般列 $A$」。

### 5. QR 在「最小平方法（Least Squares）」中的應用

**問題：** 解 $A\mathbf{x} = \mathbf{b}$，但 $A$ 是「**長方** $m \times n, m > n$」（方程個數 > 未知數個數，通常無解），求**最佳近似** $\hat{\mathbf{x}}$ 使 $\|A\mathbf{x} - \mathbf{b}\|^2$ 最小。

**經典解法（正規方程）：** $A^{\mathrm{T}} A \hat{\mathbf{x}} = A^{\mathrm{T}} \mathbf{b}$，**但** $A^{\mathrm{T}} A$ 可能病態（ill-conditioned）。

**QR 解法：** 用 $A = QR$ 代入：

$$
A^{\mathrm{T}} A \hat{\mathbf{x}} = A^{\mathrm{T}} \mathbf{b}
\;\Longleftrightarrow\; R^{\mathrm{T}} Q^{\mathrm{T}} Q R \hat{\mathbf{x}} = R^{\mathrm{T}} Q^{\mathrm{T}} \mathbf{b}
\;\Longleftrightarrow\; R^{\mathrm{T}} R \hat{\mathbf{x}} = R^{\mathrm{T}} Q^{\mathrm{T}} \mathbf{b}
\;\Longleftrightarrow\; R \hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}
$$

（利用 $Q^{\mathrm{T}} Q = I$，並消去 $R^{\mathrm{T}}$ 後得「$R$ 上三角方程」。）

**結果：** 解 $R \hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}$ — **單一三角方程**（後代法 $O(n^2)$），且**數值穩定**（避開了 $A^{\mathrm{T}} A$ 的病態）。

**這是 QR 在工程實務（迴歸分析、訊號處理、機器學習）中最常見的應用情境。**

### 6. $A = QR$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **QR ↔ CR** | QR 是「**正交化過的 CR**」— 把 $C$ 變正交 $Q$（Gram–Schmidt），把 $R$ 從 RREF 換成上三角 |
| **QR ↔ LU** | QR 把 LU 的「下三角 $L$」**升級為正交 $Q$**（保留上三角 $R$）。**從 LU 到 QR = 把 $L$ 正交化** |
| **QR ↔ QΛQᵀ** | QΛQᵀ 限對稱 $S$，$Q$ 是「特徵向量正交基底」；QR 是「列正交基底」（一般矩陣可用）|
| **QR ↔ SVD** | SVD 是「**雙側正交化**」— 把 QR 的左側 $Q$ 保留為 $U$，把右側 $R$ 也正交化得 $V^{\mathrm{T}}$，中間插一個對角 $\Sigma$。**從 QR 到 SVD = 把 $R$ 也正交化** |

**結論：** $A = QR$ 是「**單側正交化**」分解 — 左側 $Q$ 強制正交，右側 $R$ 保留上三角。沿著「正交化逐步加強」的階梯看：

$$
\underbrace{CR}_{\text{0 側正交}} \;\to\; \underbrace{LU}_{\text{0 側正交 + 三角結構}} \;\to\; \underbrace{QR}_{\text{1 側正交 + 三角結構}} \;\to\; \underbrace{U\Sigma V^{\mathrm{T}}}_{\text{2 側正交 + 對角結構}}
$$

**這是原書「五大分解升級鏈」的核心軸 — QR 在中間扮演「**從三角到正交**」的橋梁角色**。

### 7. 數學要點總結（一張表）

| 性質 | $A = QR$ 的對應 |
|---|---|
| 適用矩陣 | $A_{m \times n}$，列線性獨立（rank $= n$）；通常 $m \geq n$ |
| $Q$ 的結構 | $m \times n$，列兩兩正交 + 單位長（$Q^{\mathrm{T}} Q = I_n$）|
| $R$ 的結構 | $n \times n$ 上三角，對角線 = Gram–Schmidt 縮放因子，上方 = 投影係數 |
| 項數 | $n$（與 $A$ 的列數同）|
| 構造方法 | Gram–Schmidt（正向）或 Householder/Givens（更穩定的數值版本）|
| §4 (MM4) 對應 | $A = \sum_p r_{pp} \mathbf{q}_p \mathbf{e}^{\mathrm{T}}_p + (\text{投影修正項})$ 不直接是 (MM4) 形式 |
| §5 Pattern 對應 | **`QR.png` 標 `using P1`**：(P1) 列線性組合的「$R$ 上三角」特化 |
| 列空間不變量 | $\mathbf{C}(A) = \mathbf{C}(Q)$（Gram–Schmidt 不改變列空間，只換正交基底）|
| 求最小平方法 | $R \hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}$（單一三角方程，數值穩定）|
| 計算量 | Gram–Schmidt $O(mn^2)$；Householder 略快且更穩定 |

---

## 圖片詳細描述（Figure Descriptions）

### Figure 6.5: $A = QR$ — 標 using P1

**圖檔：** `docs/book/figs-png/QR.png`（原始 EPS：`figs/QR.eps`）
**原書頁碼：** p.10 圖 15
**所屬章節：** §6.3 $A = QR$（**唯一一張**，無對偶圖）
**圖中標記：** **`using P1`**（圓圈標，右下角）

#### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，共 9 段（與 §6.1 CR 不同，QR 只有一張圖整合所有資訊）：

1. **第 1 段：** 矩陣 $A$ 的方框（內含 **3 條等寬灰色直立列**）— 上方有大字 `A`；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 矩陣 $Q$（方框內 **3 條等寬綠色直立列，每列頂部標 `1`/`2`/`3`**）— 上方有大字 `Q`；綠色色塊代表「**正交且單位長**」的視覺信號；
4. **第 4 段：** 矩陣 $R$（方框內 **6 個藍色圓點以「上三角」形狀排列**：上排 3 點、中排 2 點、下排 1 點）— 上方有大字 `R`；**藍點明示「$R$ 是上三角，左下三角區域全為零」**；
5. **第 5 段：** 等號 `=`；
6. **第 6–8 段：** 拆解結果，3 個直立列方框並排，**從左到右逐漸變寬（容納更多綠列疊加）**：
   - 第 6 段（$\mathbf{a}_1$ 拆解）：**1 條綠色直立列** + 上方藍點 `1`（代表 $r_{11}$）+ 內側標 `1` → $\mathbf{a}_1 = r_{11} \mathbf{q}_1$；
   - 第 7 段（$\mathbf{a}_2$ 拆解）：**2 條綠色直立列**（綠1 + 綠2）+ 上方兩個藍點 `1`、`2`（代表 $r_{12}$、$r_{22}$）+ 加號 `+` → $\mathbf{a}_2 = r_{12} \mathbf{q}_1 + r_{22} \mathbf{q}_2$；
   - 第 8 段（$\mathbf{a}_3$ 拆解）：**3 條綠色直立列**（綠1 + 綠2 + 綠3）+ 上方三個藍點 `1`、`2`、`3`（代表 $r_{13}$、$r_{23}$、$r_{33}$）+ 兩個加號 → $\mathbf{a}_3 = r_{13} \mathbf{q}_1 + r_{23} \mathbf{q}_2 + r_{33} \mathbf{q}_3$；
9. **右下角圖示：** 圓圈內標 `P1`，文字 `using` — **直接標明「本圖用 §5 Pattern 1 視角」**。

**「逐漸變寬」的視覺意義：** 每一列 $\mathbf{a}_p$ 用「前 $p$ 個」$\mathbf{q}_k$ 來組成，**$p$ 增加 → 用到的 $\mathbf{q}$ 越多 → 列拆解越寬**。這直接對應「$R$ 是上三角，第 $p$ 行的非零元素只到第 $p$ 個位置」的數學結構。

**閱讀順序：** 由左到右讀整個等式鏈 `A = Q R = (三個列拆解，逐漸變寬)`。重點掃右側的 3 個拆解列，注意「**綠列數量遞增 + 藍點位置呈上三角分布**」。

#### 數學內容 (Mathematical Content)

對應數學表示（**(P1) Pattern 1** 列視角，$R$ 上三角特化版）：

$$
A = QR = \begin{bmatrix} | & | & | \\ \mathbf{q}_1 & \mathbf{q}_2 & \mathbf{q}_3 \\ | & | & | \end{bmatrix}
\begin{bmatrix} r_{11} & r_{12} & r_{13} \\ & r_{22} & r_{23} \\ & & r_{33} \end{bmatrix}
$$

第 $p$ 列展開（**(P1) Pattern 1 的上三角特化**）：

$$
\mathbf{a}_p = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k
$$

具體：

- $\mathbf{a}_1 = r_{11} \mathbf{q}_1$（只用 $\mathbf{q}_1$，1 項）；
- $\mathbf{a}_2 = r_{12} \mathbf{q}_1 + r_{22} \mathbf{q}_2$（用 $\mathbf{q}_1, \mathbf{q}_2$，2 項）；
- $\mathbf{a}_3 = r_{13} \mathbf{q}_1 + r_{23} \mathbf{q}_2 + r_{33} \mathbf{q}_3$（用 $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$，3 項）。

**正交性副產品：** 因為 $\mathbf{q}_k$ 正交，**從 $A$ 提取係數 $r_{kp}$ 變得非常簡單**：

$$
r_{kp} = \mathbf{q}_k^{\mathrm{T}} \mathbf{a}_p
$$

（投影到 $\mathbf{q}_k$ 方向就是內積。）這與 CR / LU 不同 — CR 的 $R$ 要解 RREF、LU 的 $L$ 要消去 — 但 QR 的 $R$ **直接內積即可**，這是「正交基底」帶來的計算簡化。

#### 直覺解讀 (Intuition)

QR 圖傳達三層核心訊息：

1. **正交基底的「綠色直立列」隱喻：** $Q$ 的 3 條綠色直立列**等寬且等高**，視覺上強調「**長度都是 1 + 兩兩垂直**」。這跟 LU 的 $L$（綠列從高到低，視覺上「降階」）形成對比 — QR 的 $Q$ 是「**整齊的正交基底**」，LU 的 $L$ 是「**有序的三角結構**」；

2. **上三角 $R$ 的「藍點階梯」：** $R$ 的 6 個藍點呈上三角分布（上排 3 點、中排 2 點、下排 1 點），**視覺上明示「對角線 + 上三角區域才有值，左下三角全為零」**。這個視覺信號讓讀者立刻看出 $R$ 的稀疏結構；

3. **「列拆解逐漸變寬」的本質：** 第 $p$ 個拆解列用 $p$ 個綠列疊加，**直觀對應「Gram–Schmidt 過程中第 $p$ 步用到前 $p$ 個 $\mathbf{q}_k$」**。這個視覺序列是 QR 「**逐步擴充正交基底**」過程的最精煉表達。

**「using P1」標籤的重要性（S08 PNG 重核確認）：** 原書作者刻意把這張圖標 `using P1`，與 §6.1 CR1 同款 — 等於明說「**QR 圖跟 CR1 圖是同一種視角（(P1) 列線性組合），只是 $R$ 換成上三角**」。視覺化可以**直接重用 ch05 VizScript-01 的對角矩陣互動**（把對角換成上三角），或重用 ch06b VizScript-01 的 CR 互動（把 $R$ 限定為上三角）。

**為什麼這張圖該做成互動視覺化？** 因為 QR 的核心過程「**Gram–Schmidt 正交化**」是「**動態的逐步過程**」 — 用戶調 $A$ 看每一列如何「**減投影 → 單位化**」變成 $\mathbf{q}_p$，在 3D 空間中可以**清楚看到向量「重新指向正交方向」**的幾何意義。靜態圖只能展示最終結果，**互動 demo 可以展示中間每一步**，這是 QR 教學的關鍵突破點（見 VizMark-01）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [Gram–Schmidt 正交化動畫 + P1 列拆解] ⭐⭐⭐
> 「拉桿調 $A$ 的元素 → 逐步動畫 Gram–Schmidt 三步驟（減投影 → 單位化 → 記錄到 $R$）→ 3D 視窗看 $\mathbf{q}_p$ 如何指向正交方向 → 同步顯示 $Q, R$ 結構」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [3D 投影視覺] ⭐⭐
> 「3D 視窗中展示 $\mathbf{a}_p$ 投影到子空間 $\operatorname{span}\{\mathbf{q}_1, \ldots, \mathbf{q}_{p-1}\}$ + 減投影得 $\mathbf{w}_p$ + 單位化得 $\mathbf{q}_p$」
> **詳見劇本：** VizScript-02（章末，精簡版）

> 🎬 **VizMark-03** [QR 數值範例] ⭐
> 「用 2×2 範例 $A = \bigl[\begin{smallmatrix}1&2\\1&0\end{smallmatrix}\bigr]$ 一步一步動畫展示計算過程，每步顯示具體數字 + $r_{ij}$ 填入 $R$」
> **詳見劇本：** VizScript-03（章末，輕量版）

---

## 視覺化劇本（VizScripts）

### VizScript-01: Gram–Schmidt 正交化 + P1 列拆解動畫（QR Gram–Schmidt Animation）

**Tier：** ⭐⭐⭐ Tier 2（含 Gram–Schmidt 逐步動畫 + 3D 投影視覺 + P1 列拆解；單 pointer 指 ch05 VizScript-01）
**對應 VizMark：** Figure 6.5 VizMark-01
**預估實作工作量：** S12+ 約 2 session（畫面框架 + Gram–Schmidt 1 session + 3D 投影 1 session）

#### A. 一句話定位

「給一個 $A$（$m \times n$，$n \leq m$），動態展示 Gram–Schmidt 正交化過程 — 每一列減投影 / 單位化 / 記錄到 $R$ — 並用 3D 視窗看 $\mathbf{q}_p$ 如何指向正交方向，視覺驗證 $A = QR$ 且 $\mathbf{C}(A) = \mathbf{C}(Q)$。」

#### B. 學習目標（Learning Outcome）

- **Gram–Schmidt 流程直覺：** 看到一個矩陣，能在腦中跑「減投影 → 單位化」三步驟，**手算 Gram–Schmidt**；
- **正交性的幾何意義：** 透過 3D 視窗看到 $\mathbf{q}_p$ 與前 $\mathbf{q}_k$ 都**垂直**，建立「正交 = 各自獨立 = 投影為零」的直覺；
- **列空間不變量：** 動態切換「$A$ 的列」和「$Q$ 的列」，看到它們**撐起的子空間相同**（同一個 3D 平面 / 直線）；
- **(P1) 上三角特化：** 從反向公式看 $\mathbf{a}_p = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k$，理解「$R$ 上三角 → $\mathbf{a}_p$ 只用前 $p$ 個 $\mathbf{q}$」；
- **跨章連結：** 點 (P1) 按鈕跳 ch05 VizScript-01 看對角矩陣特例（理解 QR 是 (P1) 的「上三角版」）。

#### C. 互動參數（UI Inputs）

- **矩陣輸入 $A$：** $m \times n$ 格子網格，$m \in [2, 4]$、$n \in [2, m]$，每格 $a_{ij} \in [-9, 9]$ 步進 1；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}1&2\\1&0\end{smallmatrix}\bigr]$（書中 2×2 範例，正方形）；
  - 範例 2：$\bigl[\begin{smallmatrix}1&1&0\\0&1&1\\1&0&1\end{smallmatrix}\bigr]$（3×3 含正交化的中等難度）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&0&0\\0&1&0\\0&0&1\end{smallmatrix}\bigr]$（單位矩陣，$Q = I, R = I$ 不變特例）；
  - 範例 4：$\bigl[\begin{smallmatrix}1&2&3\\0&4&5\\0&0&6\end{smallmatrix}\bigr]$（**已是上三角**，$Q = I, R = A$ 特例）；
  - 範例 5：$\bigl[\begin{smallmatrix}1&2&3\\1&2&3\\1&2&3\end{smallmatrix}\bigr]$（**退化** rank = 1，第 2、3 列正交化會得 $\mathbf{w}_p = \mathbf{0}$，顯示失敗警示）；
- **動畫模式切換 (radio)：** `分步動畫（手動下一步）` / `自動播放` / `對比 $A$ vs $Q$ 兩個基底`；
- **3D 視窗開關 (checkbox)：** 開啟後右側額外顯示 3D 視窗（僅當 $m \leq 3$ 可用）；
- **跳轉按鈕：**
  - 「→ (P1) 對角矩陣特例」按鈕（跳 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)，自動把 $R$ 換成對角矩陣）；
  - 「→ 最小平方法 demo」按鈕（跳到附加流程，用 $R\hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}$ 解最小平方）。

#### D. 視覺布局（Layout）

**主畫面三區（標準模式）：**

| 區 | 內容 |
|---|---|
| 左區（輸入） | $A$ 的格子輸入網格 + 預設範例選擇器 + radio + 滑桿 |
| 中區（Gram–Schmidt 動畫） | $A, Q, R$ 三矩陣並排 + 當前正在處理的列高亮（金色框）+ 投影 / 減 / 單位化 / 記錄 4 步驟說明文字 |
| 右區（3D 視窗，可選） | 3D 座標系中顯示 $\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3$ (灰色 + 灰平面) 和 $\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3$ (綠色 + 綠平面) 並排，標出投影向量（虛線）|

**底部資訊條：**

- 當前正在處理的 $p$（大字顯示）；
- 當前的 $\mathbf{w}_p, r_{kp}, \mathbf{q}_p$ 數值（小字顯示）；
- 「**$\mathbf{C}(A) = \mathbf{C}(Q)$ 驗證**」（綠色 ✓ 顯示，hover 顯示計算過程）。

#### E. 動畫腳本（Storyboard）

**Step 1（0–500ms）：** $A$ 的格子網格從左區滑入中區，列 1 高亮金色框。

**Step 2（500–1500ms，第 $p = 1$ 步）：**
- 高亮 $\mathbf{a}_1$（綠色淡背景）；
- 公式區顯示 `r_{11} = ||a_1|| = ...`；
- 計算 $r_{11}$（顯示具體數字），$\mathbf{q}_1 = \mathbf{a}_1 / r_{11}$；
- $\mathbf{q}_1$ 移動到 $Q$ 的第 1 列位置（綠色立柱）；
- $r_{11}$ 填入 $R$ 的 $(1, 1)$ 位置（藍點）；
- 3D 視窗：$\mathbf{a}_1$（灰箭頭）淡入 → 縮放到單位長度成 $\mathbf{q}_1$（綠箭頭）。

**Step 3（1500–3000ms，第 $p = 2$ 步）：**
- 高亮 $\mathbf{a}_2$（黃色淡背景）；
- 公式區顯示 `r_{12} = q_1^T a_2 = ...` → 計算投影係數；
- 計算 $\mathbf{w}_2 = \mathbf{a}_2 - r_{12} \mathbf{q}_1$（顯示具體向量減法）；
- 3D 視窗：$\mathbf{a}_2$（灰箭頭）淡入 → 從 $\mathbf{a}_2$ 拉一條虛線到 $\mathbf{q}_1$ 的投影點（紅色投影箭頭）→ 投影向量「飛走」（從 $\mathbf{a}_2$ 移動到原點）→ 留下 $\mathbf{w}_2$（黃色箭頭，與 $\mathbf{q}_1$ 垂直）；
- 公式區顯示 `r_{22} = ||w_2|| = ...`；
- $\mathbf{q}_2 = \mathbf{w}_2 / r_{22}$，$\mathbf{q}_2$ 移動到 $Q$ 的第 2 列；
- $r_{12}, r_{22}$ 填入 $R$ 的 $(1, 2), (2, 2)$ 位置。

**Step 4（3000–5000ms，第 $p = 3$ 步，若 $n \geq 3$）：**
- 類似 Step 3，但減 2 個投影（$r_{13} \mathbf{q}_1 + r_{23} \mathbf{q}_2$）；
- 3D 視窗：$\mathbf{a}_3$ → 從 $\mathbf{q}_1, \mathbf{q}_2$ 撐起的平面投影 → 減去 → $\mathbf{w}_3$ 與平面垂直 → 單位化得 $\mathbf{q}_3$。

**Step 5（完成，5000–6000ms）：** $Q, R$ 全部填完，顯示 `A = QR` 等式驗證 ✓；
- 3D 視窗：$\{\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3\}$ 三個綠箭頭兩兩垂直 + $A$ 的 $\{\mathbf{a}_1, \mathbf{a}_2, \mathbf{a}_3\}$ 三個灰箭頭撐起同一個 3D 子空間（$\mathbf{C}(A) = \mathbf{C}(Q)$ 視覺證明）。

**Step 6（按「對比」radio）：** 顯示「兩個基底並排」：
- 左半 3D：$A$ 的三個列（灰）撐起的 3D 空間 + 任意紅色測試向量 $\mathbf{v}$ 顯示「用 $A$ 列線組」需要的係數（從正規方程算）；
- 右半 3D：$Q$ 的三個列（綠）撐起同樣的 3D 空間 + 同一個紅色測試向量 $\mathbf{v}$ 顯示「用 $Q$ 列線組」需要的係數（**只是內積，超簡單**）；
- **對比直覺：「同樣的空間，不同的座標系；$Q$ 的座標系正交，計算容易」**。

#### F. 配色（依全書視覺一致性錨點）

- **綠 `#2ca02c`：** $\mathbf{q}_p$ / $Q$ 的列 / 3D 視窗中的正交向量；
- **灰 `#cccccc`：** $\mathbf{a}_p$ / $A$ 的列 / 3D 視窗中的原始向量；
- **黃 `#FFD700`：** 當前正在處理的列 / $\mathbf{w}_p$（減投影後的中間結果）；
- **紅 `#d62728`：** 投影向量 $r_{kp} \mathbf{q}_k$（要從 $\mathbf{a}_p$ 減去的部分）；
- **藍 `#1f77b4`：** $R$ 的元素（藍點）/ 3D 視窗座標軸；
- **紫 `#9467bd`：** 失敗 / 退化警示（範例 5 rank 不足）。

#### G. 計算邏輯（Numerical Backend）

```python
def gram_schmidt(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, list[dict]]:
    """Return Q, R, and step-by-step history for animation."""
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))
    history = []
    for p in range(n):
        a_p = A[:, p].copy()
        w_p = a_p.copy()
        proj_components = []
        for k in range(p):
            r_kp = Q[:, k] @ a_p
            R[k, p] = r_kp
            proj = r_kp * Q[:, k]
            w_p = w_p - proj
            proj_components.append({"k": k, "r_kp": r_kp, "proj_vector": proj})
        r_pp = np.linalg.norm(w_p)
        if r_pp < 1e-12:
            raise ValueError(f"Column {p} is linearly dependent")
        R[p, p] = r_pp
        Q[:, p] = w_p / r_pp
        history.append({
            "p": p,
            "a_p": a_p, "w_p": w_p, "q_p": Q[:, p].copy(),
            "r_pp": r_pp, "projections": proj_components
        })
    return Q, R, history
```

**驗證：** $Q^{\mathrm{T}} Q = I$ ✓、$QR = A$ ✓、$\mathbf{C}(Q) = \mathbf{C}(A)$（透過 SVD 比對奇異值非零數）。

#### H. 跨章 pointer 邏輯

- **「→ (P1) 對角矩陣特例」按鈕：**
  - 點擊 → 跳 [ch05 VizScript-01](ch05-patterns.md#vizscript-01)；
  - 自動把當前 $Q$ 載入為 ch05 的「左矩陣」，把 $R$ 的對角元素 $r_{ii}$ 載入為對角矩陣 $D$ 的對角元素（**忽略 $R$ 的上三角部分**）；
  - ch05 動畫展示「$Q D$ 是 $Q$ 列被 $r_{ii}$ 縮放的純粹 (P1) 特例」；
  - 對比理解：「QR 是 (P1) 的『上三角加強版』 — 多了『列之間的相互線性組合』」。

- **「→ 最小平方法 demo」按鈕：**
  - 進入附加流程：輸入 $\mathbf{b}$ 列向量 → 動畫展示 $\mathbf{c} = Q^{\mathrm{T}} \mathbf{b}$ → 後代解 $R \hat{\mathbf{x}} = \mathbf{c}$；
  - 顯示「殘差 $\mathbf{r} = \mathbf{b} - A\hat{\mathbf{x}}$」垂直於 $\mathbf{C}(A)$（**正交投影的幾何意義**）。

#### I. UI 元件清單（Component Inventory）

| 元件 | 類型 | 預期實作 |
|---|---|---|
| 矩陣格子網格 | grid input | $m \times n$ 個 `<input type="number">` |
| 預設範例下拉 | select | 5 個範例 |
| 動畫模式 radio | radio group | 3 選項 |
| 3D 視窗開關 | checkbox | 預設關閉（避免初次認知負荷）|
| 動畫速度滑桿 | range | 0.5–4.0 |
| 「下一步」按鈕 | button | 分步動畫模式專用 |
| 跳轉按鈕 | button | 2 個（→ ch05、→ 最小平方）|
| 3D 視窗 | matplotlib 3D / plotly 3D | 600×480 px |
| 公式 LaTeX 區 | MathJax / KaTeX | 即時更新計算公式 |

#### J. 教學文案（Voiceover / Caption Script）

- **開場：** 「$A = QR$ 把矩陣的列『重新指向正交方向』。**怎麼做**？答案是『**Gram–Schmidt 正交化**』 — 一個一個處理列，每列都減去前面已產生方向的投影，再單位化。」
- **第 1 步：** 「第 1 列 $\mathbf{a}_1$ 直接單位化得 $\mathbf{q}_1$ — 沒有前面的列要減投影。長度 $\|\mathbf{a}_1\|$ 記到 $R$ 的對角線。」
- **第 2 步：** 「第 2 列 $\mathbf{a}_2$ 先**投影到 $\mathbf{q}_1$ 方向**，這個投影量 $r_{12} = \mathbf{q}_1^{\mathrm{T}} \mathbf{a}_2$ 記到 $R$ 的 $(1, 2)$ 位置。$\mathbf{a}_2$ 減去這個投影 → 剩下的 $\mathbf{w}_2$ 與 $\mathbf{q}_1$ 垂直 → 單位化得 $\mathbf{q}_2$。」
- **第 3 步（若 $n \geq 3$）：** 「第 3 列同理，但要減**兩個方向**的投影（$\mathbf{q}_1$ 和 $\mathbf{q}_2$）。結果 $\mathbf{q}_3$ 與前兩個 $\mathbf{q}$ 都垂直。」
- **完成：** 「現在 $Q$ 的三列兩兩正交，$R$ 是上三角，且 $A = QR$。**注意 3D 視窗 — $Q$ 和 $A$ 撐起的是同一個 3D 空間**，只是用不同的基底描述。」
- **(P1) 連結：** 「圖右下角的 `using P1` 標籤點明：$\mathbf{a}_p = \sum_{k=1}^{p} r_{kp} \mathbf{q}_k$ 就是 §5 (P1)『列線性組合』的特例，**只是 $R$ 限定為上三角**。」

#### K. 退化案例 + 邊界處理（Edge Cases）

- **列線性依賴：** 若 $\mathbf{a}_p$ 是前 $\mathbf{a}_1, \ldots, \mathbf{a}_{p-1}$ 的線性組合，$\mathbf{w}_p = \mathbf{0}$，Gram–Schmidt 失敗。顯示橙色警示「rank < n，需用 Modified Gram–Schmidt 或 Householder」+ 範例 5 觸發；
- **接近依賴（病態）：** 若 $\|\mathbf{w}_p\| < 10^{-6}$，數值不穩，顯示紅色警示；
- **正方形 $A$：** $m = n$，$Q$ 是正交矩陣（$Q^{-1} = Q^{\mathrm{T}}$），不變動畫流程；
- **$A$ 已是正交：** $A^{\mathrm{T}} A = I$，則 $Q = A, R = I$，動畫顯示「跳過所有減投影步驟」；
- **$A$ 已是上三角：** $Q = I, R = A$，動畫顯示「跳過所有單位化步驟」。

#### L. 學習評量提示（Assessment Hooks）

互動結束時提供「**理解檢核**」：

1. **概念題：** 「為什麼第 $p$ 步要減**前 $p-1$ 個** $\mathbf{q}_k$ 方向的投影，不能跳過某幾個？」（答：跳過會導致 $\mathbf{w}_p$ 不與所有前 $\mathbf{q}$ 都垂直，破壞正交性）；
2. **計算題：** 「給 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$，動手算 $\mathbf{q}_1, \mathbf{q}_2, R$。」（答：$\mathbf{q}_1 = (3/5, 4/5)^{\mathrm{T}}$，$r_{11} = 5$，$r_{12} = 4$，$\mathbf{w}_2 = (-12/5, 9/5)^{\mathrm{T}}$，$r_{22} = 3$，$\mathbf{q}_2 = (-4/5, 3/5)^{\mathrm{T}}$）；
3. **空間題：** 「驗證 $\mathbf{C}(A) = \mathbf{C}(Q)$：取一個任意 $\mathbf{v} \in \mathbf{C}(A)$，找出用 $A$ 列的線組係數和用 $Q$ 列的線組係數。」（答：兩組係數透過 $R$ 線性關聯）；
4. **跨章連結題：** 「點 → (P1) 對角特例按鈕，看 ch05 動畫。**如果 QR 的 $R$ 強制為對角矩陣，QR 退化成什麼？**」（答：$A$ 本來就是「正交列乘上對角縮放」即 $A = QD$，這只是 QR 在「列已正交」時的退化版）。

#### M. 實作里程碑（Milestones for S12+）

1. **M1（第 1 session）：** 畫面框架（左/中/右三區 + 5 個預設範例 + radio）；
2. **M2：** Gram–Schmidt 分步動畫（中區）— 三步驟逐步演示；
3. **M3：** $Q, R$ 同步填充動畫；
4. **M4（第 2 session）：** 3D 視窗（投影 + 減 + 單位化的幾何動畫）；
5. **M5：** 「對比 $A$ vs $Q$ 兩個基底」模式；
6. **M6：** 跨章 pointer 整合（→ ch05、→ 最小平方法）；
7. **M7：** 邊界處理（退化情形 + 接近依賴警示）；
8. **M8：** 教學文案 + 評量檢核 + 5 個範例驗證。

---

### VizScript-02: 3D 投影視覺（精簡）

**Tier：** ⭐⭐ Tier 1 精簡（單純 3D 投影動畫，無互動參數調整）
**對應 VizMark：** Figure 6.5 VizMark-02
**預估實作工作量：** S12+ 約 1 session

#### A. 一句話定位

「3D 視窗中展示 Gram–Schmidt 的核心動作 — 把 $\mathbf{a}_p$ 投影到子空間 $\operatorname{span}\{\mathbf{q}_1, \ldots, \mathbf{q}_{p-1}\}$，減去投影得垂直向量 $\mathbf{w}_p$，再單位化。」

#### B–E. 互動 + 布局

- **輸入：** 固定 3 個預設 3D 範例（無自由調整）；
- **布局：** 整個畫面 3D 視窗占大半（800 × 600），底部顯示對應公式；
- **動畫腳本：** 3 個範例各 8 秒，總長 24 秒：
  - 範例 A：3 個正交但未單位化的向量 → 純單位化（無投影需要）；
  - 範例 B：3 個一般向量 → 經典 Gram–Schmidt 三步驟；
  - 範例 C：第 3 個向量幾乎在前兩個張成的平面內 → 投影後 $\mathbf{w}_3$ 接近零，展示病態情形。

#### F–G. 配色 + 計算邏輯

配色同 VizScript-01；計算邏輯複用 `gram_schmidt` 函式。

#### H–M. 其餘段落

精簡版主要是純動畫展示，無教學文案以外的互動。預估文字 ~500 字。

---

### VizScript-03: 2×2 QR 數值範例 walkthrough（輕量）

**Tier：** ⭐ Tier 1 輕量（單一範例逐步數字動畫）
**對應 VizMark：** Figure 6.5 VizMark-03
**預估實作工作量：** S12+ 約 0.5 session

#### A. 一句話定位

「對範例 $A = \bigl[\begin{smallmatrix}1&2\\1&0\end{smallmatrix}\bigr]$ 逐步動畫展示 Gram–Schmidt 兩步驟，每步顯示具體數字（含 $\sqrt{2}$ 表示）。」

#### B–E. 簡述

- **輸入：** 無（固定範例）；
- **動畫腳本：** 2 段（求 $\mathbf{q}_1, r_{11}$ → 求 $\mathbf{q}_2, r_{12}, r_{22}$），每段約 5 秒，總長 10 秒；
- **目標：** 入門用，學生第一次看 QR 時用此 demo 建立直覺，看完後再點 VizScript-01 自由探索。

#### F–M. 其餘段落

配色同 VizScript-01；無互動，純線性動畫；無評量。預估文字 ~250 字。

---

## 小結

- **§6.3 A=QR** 是 §6 五大分解的第三個，是「**單側正交化**」分解（左側 $Q$ 正交、右側 $R$ 上三角）；
- **與 (P1) 的連結直接顯式：** QR 圖標 `using P1`，是 S08 PNG 重核發現的「跨章 pointer 官方鐵證」第三例；
- **與 LU 的階梯關係：** QR = LU 把「下三角 $L$」**升級為正交 $Q$**；下一步 SVD = QR 把「上三角 $R$」也正交化；
- **三個 VizScript：** ⭐⭐⭐ Gram–Schmidt 動畫 + 3D 投影 + (P1) 列拆解 + ⭐⭐ 3D 純投影 + ⭐ 2×2 數字 walkthrough；
- **核心應用：** 最小平方法 $R\hat{\mathbf{x}} = Q^{\mathrm{T}} \mathbf{b}$，避開正規方程 $A^{\mathrm{T}} A$ 的病態；
- **下兩章 §6.4 $S = Q\Lambda Q^{\mathrm{T}}$ + §6.5 $A = U\Sigma V^{\mathrm{T}}$（S09 處理）：** 把「單側正交」升級為「**雙側正交 + 中間對角**」，迎來 SVD 這個「分解之王」。
