# 6.4 矩陣分解 4：$S = Q \Lambda Q^{\mathrm{T}}$（Spectral Decomposition / Eigenvalue Decomposition）

> **原書頁碼：** p.11–p.12
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.4 $S = Q\Lambda Q^{\mathrm{T}}$（en.md line 430–505 / zh.md line 418–492）
> **本章圖數：** 1（`EVD.png`，原書圖中明標 **using P4**）
> **本章 VizMark 數：** 3（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成（S09）

---

## 章節摘要

$S = Q \Lambda Q^{\mathrm{T}}$ 是 §6 五大分解的**第四個**，也是**整本書第一個「對矩陣本身有結構限制」的分解** — **僅限對稱矩陣** $S = S^{\mathrm{T}}$。它有兩個常用名字：

- **EVD（Eigenvalue Decomposition，特徵值分解）：** 強調「找特徵值 $\lambda_p$ 與特徵向量 $\mathbf{q}_p$」這條對角化路徑；
- **譜分解（Spectral Decomposition）：** 強調最終把 $S$ 寫成「投影矩陣的線性組合」$S = \sum_p \lambda_p P_p$，每個 $\lambda_p$ 配一個秩 1 投影到 $\mathbf{q}_p$ 方向 — 這是「**譜定理**（Spectral Theorem）」的內容。

兩個名字描述的是**同一個分解**，差別在於「強調特徵值/向量這個組件」還是「強調最終的『**對稱結構** = 投影矩陣加權和**』」。本章把兩個視角都鋪開。

**對稱矩陣的兩個鐵律（譜定理保證）：**

1. **所有特徵值 $\lambda_p$ 都是實數**（不會出現複數）；
2. **不同特徵值對應的特徵向量 $\mathbf{q}_p$ 互相正交**（不需手動正交化），可選為單位長 → $Q$ 是**正交矩陣**（$Q^{\mathrm{T}} Q = Q Q^{\mathrm{T}} = I$）。

**這兩個性質是對稱矩陣獨有的「禮物」** — 一般方陣的 $A = X \Lambda X^{-1}$（特徵分解）需要算 $X^{-1}$（昂貴且可能病態），但對稱矩陣 $S = Q \Lambda Q^{\mathrm{T}}$ 直接用 $Q^{\mathrm{T}}$ 就行（轉置 = 反矩陣）。**這是對稱矩陣在工程實務中無所不在的根本原因**：協方差矩陣、Gram 矩陣 $A^{\mathrm{T}} A$、Hessian 矩陣、二次型、PCA、量子力學的可觀測量算符 — 都對稱、都用 EVD 解。

**`using P4` 標記的意義（S09 PNG 重核發現）：** 原書 `EVD.png` 右下角圓圈標 `P4`（**S09 重大發現**），明示「EVD 圖的視覺視角是 §5 Pattern 4」— **「兩個正交矩陣夾一個對角矩陣」三明治結構**。這跟 §6.5 SVD 標的也是 `using P4`（S09 同步發現），等於原書作者把「對稱情境的 EVD」與「一般情境的 SVD」**用同一個視覺語言（P4 三明治）統一表達**。本章 VizScript 採**單 pointer 策略**（PNG 標什麼就指什麼）pointer 到 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)（P4 三明治）。

**本章 VizScript 策略：** ⭐⭐⭐ VizScript-01 採**單 pointer 策略** — (P4) 三明治結構 pointer 到 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)；本章獨立寫的是 **譜分解的「投影矩陣加權和」動畫 + 3D 視窗看橢球主軸對齊（譜定理的幾何直覺）+ $P_p$ 三性質（完備 / 正交 / 冪等）視覺驗證** 等 EVD 特有的內容。

**對比 LU/QR：**

| 性質 | $A = LU$ | $A = QR$ | $S = Q\Lambda Q^{\mathrm{T}}$ |
|---|---|---|---|
| 矩陣限制 | 可 LU 分解 | 列線性獨立 | **必須對稱** $S = S^{\mathrm{T}}$ |
| 左側結構 | 下三角 $L$ | 正交 $Q$ | **正交** $Q$ |
| 中間/右側 | 上三角 $U$ | 上三角 $R$ | **對角** $\Lambda$ + 正交 $Q^{\mathrm{T}}$ |
| 「雙側」性質 | 無 | 單側正交 | **雙側正交（且兩側互為轉置）** |
| `using` 標記 | LU2 標 (MM4) | QR 標 (P1) | **EVD 標 (P4)** |
| 對應 §5 Pattern | (MM4) 秩 1 累加 | (P1) 列線組 | **(P4) 三明治** |
| 求解 $A^{-1}$ | 兩步反代 | $R^{-1} Q^{\mathrm{T}}$ | $Q \Lambda^{-1} Q^{\mathrm{T}}$ |

**核心升級點：** 從 QR 升級到 EVD = **把右側 $R$ 的「上三角」也升級為「對角」+ 把右側換成左側 $Q$ 的轉置 $Q^{\mathrm{T}}$**。這是「**雙側正交且對稱的對角化**」 — 對稱矩陣才有這個特權。

數值範例（本章貫穿，2×2 對稱矩陣）：

$$
S = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}
\;=\;
\underbrace{\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}}_{Q}
\underbrace{\begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}}_{\Lambda}
\underbrace{\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}}_{Q^{\mathrm{T}}}
$$

驗證：

1. 特徵值：$\det(S - \lambda I) = (3-\lambda)^2 - 1 = 0 \Rightarrow \lambda = 4$ 或 $\lambda = 2$；
2. $\lambda_1 = 4$：$(S - 4I) \mathbf{q}_1 = \mathbf{0} \Rightarrow \mathbf{q}_1 = (1, 1)^{\mathrm{T}}/\sqrt{2}$；
3. $\lambda_2 = 2$：$(S - 2I) \mathbf{q}_2 = \mathbf{0} \Rightarrow \mathbf{q}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$；
4. 驗證 $\mathbf{q}_1^{\mathrm{T}} \mathbf{q}_2 = (1 \cdot 1 + 1 \cdot (-1))/2 = 0$ ✓（自動正交，譜定理鐵律）；
5. $Q \Lambda Q^{\mathrm{T}} = \frac{1}{2} \begin{bmatrix}1&1\\1&-1\end{bmatrix} \begin{bmatrix}4&0\\0&2\end{bmatrix} \begin{bmatrix}1&1\\1&-1\end{bmatrix} = \frac{1}{2} \begin{bmatrix}4&2\\4&-2\end{bmatrix} \begin{bmatrix}1&1\\1&-1\end{bmatrix} = \frac{1}{2} \begin{bmatrix}6&2\\2&6\end{bmatrix} = \begin{bmatrix}3&1\\1&3\end{bmatrix} = S$ ✓。

**譜分解形式（本章核心 ⭐）：**

$$
S = \lambda_1 \mathbf{q}_1 \mathbf{q}_1^{\mathrm{T}} + \lambda_2 \mathbf{q}_2 \mathbf{q}_2^{\mathrm{T}}
= 4 \cdot \dfrac{1}{2} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} + 2 \cdot \dfrac{1}{2} \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}
= \begin{bmatrix} 2 & 2 \\ 2 & 2 \end{bmatrix} + \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}
= \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix} = S \checkmark
$$

> ### 💡 背後觀念：對稱矩陣為什麼擁有「完美三明治」？正交性從哪冒出來？
>
> 對稱矩陣 $S = S^{\mathrm{T}}$ 的特徵向量**自動正交**、特徵值**自動實**、$Q^{\mathrm{T}} = Q^{-1}$ — 這三個性質聽起來太巧合。為什麼隨便一個 $n \times n$ 對稱矩陣居然能保證有 $n$ 個互相正交的特徵向量？這個「正交」不是 Gram-Schmidt 強加的，而是**對稱性自動賦予的禮物**。背後其實是「**物理對稱性 = 數學正交性**」的深刻對應。3 條設計動機問題：
>
> - **[Q18：$S = Q\Lambda Q^{\mathrm{T}}$ 為什麼對稱矩陣特徵向量自動正交？](appendix-D-why.md#q18)** — 譜定理從 **Cauchy 1829** 主軸定理（天體力學）→ Sylvester 1852 慣性定律 → Jacobi 1846 旋轉演算法 → Schur 1909 → **量子力學 1920s Hermitian** 整整 100 多年發展。雙證明：① 不同特徵值 $\Rightarrow (\lambda_1 - \lambda_2)\mathbf{q}_2^{\mathrm{T}}\mathbf{q}_1 = 0$（核心步驟用 $S^{\mathrm{T}} = S$）+ ② $\lambda = \bar\lambda$ 實特徵值（複向量共軛轉置）+ 5 條「**物理對稱 ↔ 數學物件**」對應表（能量守恆 / 時間反演 / 空間旋轉 / 馬可夫可逆 / 二次型）。**物理量必須是可觀測量 → 對應算符必須對稱 / 厄米 → 觀測值必須是實數** — 這條鏈是譜定理的深層動機。
> - **[Q11：對角矩陣 $D$ 為什麼這麼特別？](appendix-D-why.md#q11)** — EVD 三明治中間的 $\Lambda$（特徵值對角）擁有「**矩陣世界中的標量**」四超能力，這些超能力**全部繼承到 $S$**：$S^k = Q\Lambda^k Q^{\mathrm{T}}$、$f(S) = Q f(\Lambda) Q^{\mathrm{T}}$ — 所有矩陣函數降為對角元素逐個套用。
> - **[Q13：(P4) 三明治為什麼是線代核心？](appendix-D-why.md#q13)** — EVD 是 (P4) 三明治的「**完美形式**」（兩基底合一為同一個 $Q$）。SVD（§6.5）是把這個完美形式廣義化到「任意矩陣」的版本 —「**對稱矩陣是最容易看清的矩陣**」是 EVD 章的核心昇華：對稱矩陣的「最簡視角」是同一個，輸入與輸出基底兼任。

---

## 數學要點

### 1. 定義與形狀

$$
S_{n \times n} = Q_{n \times n} \, \Lambda_{n \times n} \, Q^{\mathrm{T}}_{n \times n}, \qquad S = S^{\mathrm{T}}, \quad Q^{\mathrm{T}} Q = Q Q^{\mathrm{T}} = I_n
$$

- **$S$（Symmetric）：** $n \times n$ **對稱矩陣**，$s_{ij} = s_{ji}$。**這是本章唯一的限制條件** — 若 $S$ 不對稱，本分解形式失效，需用更一般的 $A = X \Lambda X^{-1}$（特徵分解，$X$ 一般不正交，$X^{-1}$ 不等於 $X^{\mathrm{T}}$）；
- **$Q$（Orthogonal）：** $n \times n$ **正交矩陣**，列為單位長且兩兩正交的特徵向量 $\mathbf{q}_1, \ldots, \mathbf{q}_n$。**$Q^{-1} = Q^{\mathrm{T}}$**（這是「正交矩陣」的定義性質，使 EVD 計算容易）；
- **$\Lambda$（Diagonal）：** $n \times n$ **對角矩陣**，對角元素為實特徵值 $\lambda_1, \lambda_2, \ldots, \lambda_n$（**通常按大小排序**：$\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$，可正可負可零）；
- **形狀：** 全為 $n \times n$ **方陣**（與 LU、QR 可長方不同）；
- **可分解條件：** **任意對稱矩陣**（包含對稱半正定 / 對稱不定）都可分解，無例外（譜定理保證）。**這比 LU（需主元不為零）和 QR（需列線性獨立）寬鬆** — 對稱性自帶「全勤證書」。

### 2. 譜定理（核心 ⭐）

**譜定理（Spectral Theorem）：** 任意實對稱矩陣 $S$ 可表示為

$$
S = Q \Lambda Q^{\mathrm{T}} = \sum_{p=1}^{n} \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}} = \sum_{p=1}^{n} \lambda_p P_p
$$

其中 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 是「**投影到 $\mathbf{q}_p$ 方向的秩 1 投影矩陣**」。

**展開（本章 2×2 範例）：**

$$
S = \begin{bmatrix} 3 & 1 \\ 1 & 3 \end{bmatrix}
= \underbrace{4 \cdot \dfrac{1}{2}\begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}}_{\lambda_1 P_1}
+ \underbrace{2 \cdot \dfrac{1}{2}\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}}_{\lambda_2 P_2}
$$

**譜定理三條保證（對任意實對稱 $S$）：**

1. **實特徵值：** 所有 $\lambda_p \in \mathbb{R}$（不會出現 $a + bi$ 複數）；
2. **正交特徵向量：** 不同特徵值對應的 $\mathbf{q}_p, \mathbf{q}_q$ 自動正交（$\mathbf{q}_p^{\mathrm{T}} \mathbf{q}_q = 0$，$p \neq q$）；
3. **完備正交基底：** 即使有重根特徵值（multiplicity $> 1$），也能在該特徵子空間內選一組正交基底（不會像一般矩陣那樣「特徵向量不夠」造成 Jordan 標準形）。

**證明草稿（保證 1 + 2）：**

- **保證 1（實特徵值）：** 設 $S \mathbf{q} = \lambda \mathbf{q}$（$\mathbf{q} \neq \mathbf{0}$）。取共軛轉置 $\mathbf{q}^* S^* = \bar{\lambda} \mathbf{q}^*$，因 $S$ 實對稱所以 $S^* = S$，得 $\mathbf{q}^* S = \bar{\lambda} \mathbf{q}^*$。右乘 $\mathbf{q}$：$\mathbf{q}^* S \mathbf{q} = \bar{\lambda} \mathbf{q}^* \mathbf{q}$。但 $\mathbf{q}^* S \mathbf{q} = \mathbf{q}^* (\lambda \mathbf{q}) = \lambda \mathbf{q}^* \mathbf{q}$。兩邊比較：$\lambda = \bar{\lambda}$ → $\lambda$ 實數 ✓；
- **保證 2（正交特徵向量）：** 設 $S \mathbf{q}_p = \lambda_p \mathbf{q}_p$，$S \mathbf{q}_q = \lambda_q \mathbf{q}_q$，$\lambda_p \neq \lambda_q$。則 $\mathbf{q}_q^{\mathrm{T}} S \mathbf{q}_p = \lambda_p \mathbf{q}_q^{\mathrm{T}} \mathbf{q}_p$。又 $\mathbf{q}_q^{\mathrm{T}} S \mathbf{q}_p = \mathbf{q}_q^{\mathrm{T}} S^{\mathrm{T}} \mathbf{q}_p = (S \mathbf{q}_q)^{\mathrm{T}} \mathbf{q}_p = \lambda_q \mathbf{q}_q^{\mathrm{T}} \mathbf{q}_p$。兩邊比較：$(\lambda_p - \lambda_q) \mathbf{q}_q^{\mathrm{T}} \mathbf{q}_p = 0$。因 $\lambda_p \neq \lambda_q$，所以 $\mathbf{q}_q^{\mathrm{T}} \mathbf{q}_p = 0$ ✓。

**這兩個證明只用了 $S = S^{\mathrm{T}}$ 一個性質** — 對稱性是「實 + 正交」的唯一來源。

### 3. 投影矩陣 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 的三性質（核心 ⭐）

譜分解的另一個視角：把 $S$ 看成 $n$ 個秩 1 投影矩陣的線性組合，每個 $P_p$ 配一個權重 $\lambda_p$。

每個 $P_p$ 是「**投影到 $\mathbf{q}_p$ 撐起的 1 維子空間**」的投影算子，有三條結構性質：

#### 3.1 完備性（Completeness）

$$
\sum_{p=1}^{n} P_p = P_1 + P_2 + \cdots + P_n = Q Q^{\mathrm{T}} = I_n
$$

**意義：** $n$ 個 1 維投影**覆蓋整個 $\mathbb{R}^n$ 空間**，沒有缺漏。對任意向量 $\mathbf{v}$：

$$
\mathbf{v} = I \mathbf{v} = \sum_{p=1}^{n} P_p \mathbf{v} = \sum_{p=1}^{n} (\mathbf{q}_p^{\mathrm{T}} \mathbf{v}) \mathbf{q}_p
$$

— 這就是「用正交基底展開向量」的標準公式。**完備性 = 正交基底的「無漏」性質。**

#### 3.2 正交性（Mutual Orthogonality）

$$
P_p P_q = O \quad (p \neq q)
$$

**驗證（本章範例）：**

$$
P_1 P_2 = \dfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix} \cdot \dfrac{1}{2}\begin{bmatrix}1&-1\\-1&1\end{bmatrix}
= \dfrac{1}{4}\begin{bmatrix}0&0\\0&0\end{bmatrix} = O \checkmark
$$

**意義：** 投影到 $\mathbf{q}_p$ 後再投影到 $\mathbf{q}_q$（$p \neq q$）= 0。**因為 $\mathbf{q}_q$ 與 $\mathbf{q}_p$ 正交，$\mathbf{q}_p$ 方向上的分量在 $\mathbf{q}_q$ 上沒有任何投影**。

**幾何直覺：** 想像 $\mathbb{R}^3$ 中 $x, y, z$ 三軸（互相垂直），投影到 $x$ 軸再投影到 $y$ 軸 = 0（兩個投影方向不重疊）。$P_p P_q = O$ 是「**互補方向**」的代數寫法。

#### 3.3 冪等性（Idempotence）

$$
P_p^2 = P_p, \quad P_p^{\mathrm{T}} = P_p
$$

**驗證（本章範例）：**

$$
P_1^2 = \dfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix} \cdot \dfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix}
= \dfrac{1}{4}\begin{bmatrix}2&2\\2&2\end{bmatrix} = \dfrac{1}{2}\begin{bmatrix}1&1\\1&1\end{bmatrix} = P_1 \checkmark
$$

**意義：** 投影到 $\mathbf{q}_p$ 後**再投影一次仍是同一個結果** — 因為向量已經在 $\mathbf{q}_p$ 方向上了，再投影一次不會再縮小或改變方向。

**幾何直覺：** 想像把一個 3D 物體投影到 $xy$ 平面上得到陰影；對這個陰影**再投影一次到同一個 $xy$ 平面**還是同樣的陰影（陰影本身已在 $xy$ 平面上）。

**對稱性 $P_p^{\mathrm{T}} = P_p$：** 由 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 直接看出 — 轉置後仍是 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$。**這是「正交投影」的識別標誌**：對稱 + 冪等 = 正交投影矩陣。

#### 三性質統一視圖

| 性質 | 公式 | 幾何意義 |
|---|---|---|
| 完備性 | $\sum P_p = I$ | $n$ 個 1 維投影覆蓋整個 $\mathbb{R}^n$ |
| 正交性 | $P_p P_q = O$（$p \neq q$）| 不同方向的投影互不干擾 |
| 冪等性 | $P_p^2 = P_p$，$P_p^{\mathrm{T}} = P_p$ | 重複投影不變、轉置即自身 |

**這三條性質讓「譜分解 = 投影分解」 — 把 $S$ 看成「在每個正交方向上做不同強度的縮放」**。

### 4. 與 (P4) 視角的連結 — 三明治結構（核心 ⭐）

**(P4) Pattern（§5）：** 「兩個矩陣夾一個對角矩陣 = 秩 1 之和（用對角元素加權）」

$$
\underbrace{U}_{\text{左側}} \underbrace{D}_{\text{對角}} \underbrace{V^{\mathrm{T}}}_{\text{右側}} = \sum_p d_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

**EVD 是 (P4) 的「特殊情境」** — **左側 $U = Q$，右側 $V^{\mathrm{T}} = Q^{\mathrm{T}}$（兩側相同！），對角 $D = \Lambda$：**

$$
S = \underbrace{Q}_{\text{左 = 正交}} \underbrace{\Lambda}_{\text{對角 = 特徵值}} \underbrace{Q^{\mathrm{T}}}_{\text{右 = 左的轉置}}
= \sum_p \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}
$$

**「兩側相同」是對稱矩陣的視覺指紋** — 在 (P4) 三明治結構中，左側和右側「**鏡像對稱**」，這直接對應 $S = S^{\mathrm{T}}$。

**對照表：**

| 元素 | (P4) 一般形式 | EVD 特化 |
|---|---|---|
| 左側 | $U$（任意） | $Q$（正交，特徵向量） |
| 對角 | $D$（任意對角） | $\Lambda$（特徵值） |
| 右側 | $V^{\mathrm{T}}$（任意） | $Q^{\mathrm{T}}$（**左側的轉置**） |
| 秩 1 形式 | $\sum d_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ | $\sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ |
| 秩 1 結構 | 一般「外積」（$\mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$） | **「自外積」$\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}} = P_p$ 投影矩陣** |
| 對稱性 | 一般 $UDV^{\mathrm{T}}$ 不對稱 | $S = (Q\Lambda Q^{\mathrm{T}})^{\mathrm{T}} = Q \Lambda^{\mathrm{T}} Q^{\mathrm{T}} = Q \Lambda Q^{\mathrm{T}} = S$ ✓ |

**「using P4」標籤的意涵：** 原書 `EVD.png` 標 `using P4`，直接點明「EVD 圖就是 (P4) 在『左 = 右轉置 + 對角是特徵值』情形下的特化」。**這是非常精細的標記** — 同樣標 `P4` 的 `SVD.png`（§6.5）情形是「左右兩個正交矩陣**不同** + 對角是奇異值」，EVD 是「左右兩個正交矩陣**相同（互為轉置）** + 對角是特徵值」。**EVD = SVD 的「對稱矩陣對偶版」**。

**連結 (MM4)：** 把譜分解寫成 (MM4) 形式：

$$
S = \sum_{p=1}^{n} \underbrace{\lambda_p \mathbf{q}_p}_{\text{係數 × 列}} \cdot \underbrace{\mathbf{q}_p^{\mathrm{T}}}_{\text{行}} = \sum_{p=1}^{n} \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}
$$

這正好是 (MM4) 「外積之和」的形式，**只是兩個外積向量是同一個 $\mathbf{q}_p$**（而非一般 (MM4) 的 $\mathbf{c}_p$ 和 $\mathbf{r}_p$）。雖然 PNG 沒標 `using MM4`（只標 `using P4`），但 EVD 仍然**繼承 (MM4) 的所有性質**（秩 1 累加、低秩近似、漸進收斂等），可重用 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) 的累加動畫概念。

### 5. 對稱矩陣的特殊性 — 為什麼 EVD 不需 $X^{-1}$

**一般方陣的特徵分解：**

$$
A = X \Lambda X^{-1}
$$

其中 $X$ 是「特徵向量列矩陣」**不一定正交**，所以需要算 $X^{-1}$。算 $X^{-1}$ 有兩個問題：

1. **計算昂貴：** 反矩陣 $O(n^3)$，與 LU 分解相當；
2. **數值不穩：** 若 $X$ 接近奇異（特徵向量幾乎共線），$X^{-1}$ 元素會爆炸大 → 數值誤差放大。

**對稱矩陣的譜分解：**

$$
S = Q \Lambda Q^{\mathrm{T}}
$$

因 $Q$ 正交，$Q^{-1} = Q^{\mathrm{T}}$（**轉置 = 反矩陣**）。**轉置只需 $O(1)$（指標重排）**，且**完美數值穩定**（$\|Q\| = 1$，無放大）。

**這是對稱矩陣比一般矩陣「便宜 N 倍」的關鍵原因。** 在工程實務中：

- **協方差矩陣** $C = \frac{1}{n} X^{\mathrm{T}} X$ — 對稱 → PCA 用 EVD（不用普通特徵分解）；
- **Hessian 矩陣** $H_{ij} = \partial^2 f / \partial x_i \partial x_j$ — 對稱（混合偏導交換）→ 牛頓法 / 二次型優化用 EVD；
- **Gram 矩陣** $G = A^{\mathrm{T}} A$ — 對稱 → 核方法 / SVD 預備步驟用 EVD；
- **量子力學的可觀測量** — 算符自伴（埃爾米特）→ 譜分解 = 物理可測量。

### 6. $S = Q\Lambda Q^{\mathrm{T}}$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **EVD ↔ CR** | EVD 限對稱、$Q$ 正交、$\Lambda$ 對角；CR 一般矩陣、$C$ 是獨立列、$R$ 是 RREF。**EVD 把對稱矩陣的「秩」直接寫成「非零特徵值的個數」**，而 CR 是「獨立列的個數」 — 兩者數值相等（$\operatorname{rank}(S) = $ 非零特徵值個數，對稱情境下這是定理）|
| **EVD ↔ LU** | LU 解 $S\mathbf{x} = \mathbf{b}$ 用兩步反代；EVD 解 $S\mathbf{x} = \mathbf{b}$ 用 $\mathbf{x} = Q \Lambda^{-1} Q^{\mathrm{T}} \mathbf{b}$（**$\Lambda^{-1}$ 只是對角元素取倒數**）。**EVD 在「重複解多個 $\mathbf{b}$」時更快**（共用 $Q, \Lambda^{-1}$） |
| **EVD ↔ QR** | QR 是「列正交化」（一般矩陣可用，$\mathbf{C}(A) = \mathbf{C}(Q)$）；EVD 是「對稱矩陣的雙側正交化」。**從 QR 到 EVD = 把 $R$ 也正交化（變對角 $\Lambda$）+ 強制左右對稱**。實務上**對稱矩陣的 EVD 計算常用 QR 演算法迭代**（QR 演算法 $\neq$ QR 分解，但每步用 QR 分解）|
| **EVD ↔ SVD** | **SVD 是 EVD 的「一般化」** — EVD 限對稱、雙側 $Q$ 相同；SVD 任意矩陣、雙側 $U \neq V$。對任意 $A$：$A^{\mathrm{T}} A$ 對稱半正定 → EVD 給出 $\Sigma^2$ 和 $V$；$A A^{\mathrm{T}}$ 對稱半正定 → EVD 給出 $\Sigma^2$ 和 $U$。**SVD = 兩個 EVD 的整合**（詳見 §6.5） |

**結論：** $S = Q\Lambda Q^{\mathrm{T}}$ 是「**對稱矩陣的雙側正交對角化**」。沿著「正交化逐步加強 + 對稱性限制」的階梯看：

$$
\underbrace{CR}_{\text{0 側正交}} \;\to\; \underbrace{LU}_{\text{0 側正交 + 三角結構}} \;\to\; \underbrace{QR}_{\text{1 側正交 + 三角結構}} \;\to\; \underbrace{Q\Lambda Q^{\mathrm{T}}}_{\substack{\text{2 側正交 + 對角結構}\\\text{（限對稱）}}} \;\to\; \underbrace{U\Sigma V^{\mathrm{T}}}_{\substack{\text{2 側正交 + 對角結構}\\\text{（一般矩陣）}}}
$$

**EVD 在 §6 五大分解中的角色：** 「**對稱情境的對角化**」 — 比 QR 多一層「右側也正交化」，比 SVD 多一層「對稱限制（使左右兩側相同）」。

### 7. 數學要點總結（一張表）

| 性質 | $S = Q\Lambda Q^{\mathrm{T}}$ 的對應 |
|---|---|
| 適用矩陣 | 任意實對稱方陣 $S = S^{\mathrm{T}} \in \mathbb{R}^{n \times n}$（無須正定） |
| $Q$ 的結構 | $n \times n$ 正交矩陣，列為單位特徵向量 $\mathbf{q}_p$，$Q^{\mathrm{T}} = Q^{-1}$ |
| $\Lambda$ 的結構 | $n \times n$ 對角矩陣，對角元素為實特徵值 $\lambda_p$（通常按大小降冪排序）|
| 項數 | $n$（與矩陣維度同） |
| 構造方法 | 算 $\det(S - \lambda I) = 0$ 求 $\lambda_p$ → 解 $(S - \lambda_p I)\mathbf{q}_p = \mathbf{0}$；數值上用 QR 迭代演算法 |
| §4 (MM4) 對應 | $S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$（外積向量左右相同 $\mathbf{q}_p$）|
| §5 Pattern 對應 | **`EVD.png` 標 `using P4`**：(P4) 三明治的「左 = 右轉置 + 對角是特徵值」特化 |
| 投影矩陣 $P_p$ 性質 | 完備（$\sum P_p = I$）+ 正交（$P_p P_q = O$）+ 冪等（$P_p^2 = P_p$）+ 對稱（$P_p^{\mathrm{T}} = P_p$）|
| 求 $S^{-1}$ | $S^{-1} = Q \Lambda^{-1} Q^{\mathrm{T}}$（$\Lambda^{-1}$ 只是對角倒數，前提 $\lambda_p \neq 0$）|
| 求 $S^k$（任意實 $k$） | $S^k = Q \Lambda^k Q^{\mathrm{T}}$（$\Lambda^k$ 只是對角元素 $k$ 次方）|
| 二次型 | $\mathbf{x}^{\mathrm{T}} S \mathbf{x} = \sum_p \lambda_p (\mathbf{q}_p^{\mathrm{T}} \mathbf{x})^2$（譜分解的二次型展開）|
| 計算量 | $O(n^3)$（QR 迭代演算法）|

---

## 圖片詳細描述（Figure Descriptions）

### Figure 6.6: $S = Q\Lambda Q^{\mathrm{T}}$ — 標 using P4

**圖檔：** `docs/book/figs-png/EVD.png`（原始 EPS：`figs/EVD.eps`）
**原書頁碼：** p.11 圖 16
**所屬章節：** §6.4 $S = Q\Lambda Q^{\mathrm{T}}$（**唯一一張**，無對偶圖）
**圖中標記：** **`using P4`**（圓圈標，右下角）

#### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，3×3 對稱矩陣示意，共 8 段：

1. **第 1 段：** 矩陣 $S$ 的方框（內含**淺灰色塊**，無條紋）— 上方有大字 `S`；**淺灰色 = 「對稱結構」的視覺信號**（與 LU/QR 的 $A$ 用條紋色不同，這裡用單色塊強調對稱）；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 矩陣 $Q$（方框內 **3 條等寬綠色直立列，每列底部標 `1`/`2`/`3`**）— 上方有大字 `Q`；綠色 = 「正交且單位長」視覺信號（與 QR 的 $Q$ 同款）；
4. **第 4 段：** 矩陣 $\Lambda$（方框內 **3 個藍色圓點沿對角線排列**，非對角位置完全留白）— 上方有大字 $\Lambda$；**藍點明示「$\Lambda$ 是對角矩陣」**；
5. **第 5 段：** 矩陣 $Q^{\mathrm{T}}$（方框內 **3 條等寬綠色橫躺行，每行左側標 `1`/`2`/`3`**）— 上方有大字 $Q^{\mathrm{T}}$；**$Q$ 直立 + $Q^{\mathrm{T}}$ 橫躺 = 視覺上立刻看出「轉置關係 = 列變行」**；
6. **第 6 段：** 等號 `=`；
7. **第 7–9 段：** 拆解結果，**3 個方框並排，每個都標 $\lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$**：
   - 第 7 段：$\lambda_1 \mathbf{q}_1 \mathbf{q}_1^{\mathrm{T}}$ — 方框內含 **1 條綠色直立列（標 `1`）+ 上方淡綠橫躺行（標 `1`）**，藍點標 $\lambda_1$；
   - 第 8 段：加號 `+`；$\lambda_2 \mathbf{q}_2 \mathbf{q}_2^{\mathrm{T}}$ — **同樣結構，標 `2`**；
   - 第 9 段：加號 `+`；$\lambda_3 \mathbf{q}_3 \mathbf{q}_3^{\mathrm{T}}$ — **同樣結構，標 `3`**；
8. **右下角圖示：** 圓圈內標 `P4`，文字 `using` — **直接標明「本圖用 §5 Pattern 4 視角」**。

**「直立列 + 橫躺行」對偶布局的視覺意義：** 每個 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 拆解圖中，**$\mathbf{q}_p$（綠色直立列）疊在 $\mathbf{q}_p^{\mathrm{T}}$（淡綠橫躺行）之上**，明確展示「自外積 = 列向量乘以自己的轉置」。**這是譜定理「投影矩陣」概念的視覺化** — 每個 $P_p$ 的形狀都是「列 × 行」的 $n \times n$ 矩陣，而非單一的列或行。

**閱讀順序：** 由左到右讀整個等式鏈 `S = Q Λ Q^T = (三個 λ_p P_p 累加)`。重點掃右側的 3 個拆解項，注意「**綠列 + 綠行對偶布局 + 藍點 λ_p 加權**」。

#### 數學內容 (Mathematical Content)

對應數學表示（**(P4) Pattern 4** 三明治視角，左 = 右轉置特化版）：

$$
S = Q \Lambda Q^{\mathrm{T}}
= \begin{bmatrix} | & | & | \\ \mathbf{q}_1 & \mathbf{q}_2 & \mathbf{q}_3 \\ | & | & | \end{bmatrix}
\begin{bmatrix} \lambda_1 & & \\ & \lambda_2 & \\ & & \lambda_3 \end{bmatrix}
\begin{bmatrix} - & \mathbf{q}_1^{\mathrm{T}} & - \\ - & \mathbf{q}_2^{\mathrm{T}} & - \\ - & \mathbf{q}_3^{\mathrm{T}} & - \end{bmatrix}
= \sum_{p=1}^{3} \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}
$$

**關鍵數值關係（對任意對稱 $S$）：**

- $S = S^{\mathrm{T}}$（對稱性）；
- $Q^{\mathrm{T}} Q = Q Q^{\mathrm{T}} = I_n$（正交性）；
- $\sum P_p = I_n$（完備性）；
- $P_p P_q = O$（$p \neq q$，正交性）；
- $P_p^2 = P_p^{\mathrm{T}} = P_p$（冪等對稱性）。

**從 $S$ 提取 $(\lambda_p, \mathbf{q}_p)$：** 用「特徵值分解 + Gram-Schmidt 正交化重複根」算法，數值上用 QR 演算法迭代 — **不像 (MM4) 的外積那樣可直接讀出**，需要解 $\det(S - \lambda I) = 0$。

#### 直覺解讀 (Intuition)

EVD 圖傳達四層核心訊息：

1. **「對稱性 = 視覺鏡像」直覺：** $Q$（綠列直立）和 $Q^{\mathrm{T}}$（綠行橫躺）在 $\Lambda$ 兩側**鏡像對稱**，視覺上立刻看出「左右兩側是同一組向量，只是擺向不同」。**這就是對稱矩陣 $S = S^{\mathrm{T}}$ 的視覺指紋** — 一般矩陣的 (P4) 三明治左右是不同矩陣（$U, V^{\mathrm{T}}$，見 §6.5 SVD），EVD 是「自鏡像」特例；

2. **「對角 $\Lambda$ = 純縮放」直覺：** 中間的 3 個藍點沿對角排列，視覺上明示「**只有對角線有值，非對角全為零**」。$\Lambda$ 的作用是「在每個正交方向上做不同強度的縮放（縮放因子 = 特徵值 $\lambda_p$）」；

3. **「投影矩陣 $P_p$ = 自外積」直覺：** 右側 3 個拆解項的 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ **使用同一個向量做兩次外積**（綠列 × 綠行，左右標號相同 `1`、`2`、`3`），視覺上強調「自外積得到秩 1 投影矩陣」。**這跟 (MM4) 的一般外積 $\mathbf{c}_p \mathbf{r}_p^{\mathrm{T}}$ 不同**（左右標號可以不同），EVD 強制「左右標號相同」；

4. **「譜分解 = 加權的投影累加」直覺：** $S = \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3$ — 每個方向 $\mathbf{q}_p$ 都有一個「強度 $\lambda_p$」，加總就是整個對稱矩陣的全部資訊。**這是譜定理的核心視覺敘述** — 對稱矩陣 = 「正交方向 × 對應強度」的加權集合。

**「using P4」標籤的重要性（S09 PNG 重核確認）：** 原書作者刻意把這張圖標 `using P4`，與 §6.5 SVD 同款 — 等於明說「**EVD 圖跟 SVD 圖是同一種視角（(P4) 三明治），只是 EVD 強制左右兩側互為轉置**」。視覺化可以**直接重用 [ch05 VizScript-03](ch05-patterns.md#vizscript-03) 的 P4 三明治互動**（把 $V^{\mathrm{T}}$ 鎖成 $U^{\mathrm{T}}$，把 $\Sigma$ 換成 $\Lambda$ 含負值），這就是為什麼本章 VizScript-01 採**單 pointer 策略**指 ch05 VizScript-03。

**為什麼這張圖該做成互動視覺化？** 因為 EVD 的核心過程「**對稱矩陣 → 正交基底 + 對角縮放**」是「**從矩陣形狀讀出向量幾何**」的關鍵步驟 — 用戶調 $S$ 看每個 $\lambda_p, \mathbf{q}_p$ 如何變、3D 視窗看「**$S$ 作用 = 在每個 $\mathbf{q}_p$ 方向上拉伸 $\lambda_p$ 倍**」（橢球主軸對齊的幾何直覺）、譜定理 $\sum \lambda_p P_p$ 加權累加的「投影分解」過程。靜態圖只能展示最終結果，**互動 demo 可以展示「拉一個對稱矩陣的元素 → 看特徵值如何變 + 橢球如何旋轉」**，這是 EVD 教學的關鍵突破點（見 VizMark-01）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [譜分解互動 + 橢球主軸對齊 3D] ⭐⭐⭐
> 「拉桿調 $S$ 的元素（強制對稱）→ 即時計算 $\lambda_p, \mathbf{q}_p$ → 動畫展示譜分解 $S = \sum \lambda_p P_p$ 三項累加 → 3D 視窗看單位球被 $S$ 變成橢球（主軸 = $\mathbf{q}_p$ 方向，半徑 = $|\lambda_p|$）→ 視覺驗證 $P_p$ 三性質」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [$P_p$ 三性質視覺驗證] ⭐⭐
> 「3 個 $P_p$ 矩陣並排顯示 + 互動驗證完備（$\sum P_p = I$）/ 正交（$P_p P_q = O$）/ 冪等（$P_p^2 = P_p$）三條性質」
> **詳見劇本：** VizScript-02（章末，精簡版）

> 🎬 **VizMark-03** [2×2 EVD 數值範例] ⭐
> 「用 2×2 範例 $S = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$ 一步一步動畫展示計算過程（特徵值 → 特徵向量 → 譜分解），每步顯示具體數字 + 公式」
> **詳見劇本：** VizScript-03（章末，輕量版）

---

## 視覺化劇本（VizScripts）

### VizScript-01: 譜分解互動 + 橢球主軸對齊（EVD Spectral Decomposition Animation）

**Tier：** ⭐⭐⭐ Tier 2（含譜分解逐項動畫 + 3D 橢球主軸視覺 + $P_p$ 三性質驗證；單 pointer 指 ch05 VizScript-03）
**對應 VizMark：** Figure 6.6 VizMark-01
**預估實作工作量：** S12+ 約 2 session（畫面框架 + 譜分解動畫 1 session + 3D 橢球視覺 1 session）

#### A. 一句話定位

「給一個對稱矩陣 $S$（$n \in \{2, 3\}$），動態展示譜分解 $S = \sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ — 三個秩 1 投影矩陣加權累加 — 並用 3D 視窗看 $S$ 把單位球變成橢球（主軸 = $\mathbf{q}_p$ 方向，半徑 = $|\lambda_p|$），視覺驗證譜定理。」

#### B. 學習目標（Learning Outcome）

- **譜定理直覺：** 看到對稱矩陣，能在腦中想像「**正交方向 + 對應特徵值縮放**」的幾何圖景；
- **特徵向量 = 不變方向：** 透過 3D 視窗看到 $S \mathbf{q}_p = \lambda_p \mathbf{q}_p$（向量方向不變、只縮放）；
- **橢球主軸對齊：** 看到單位球被 $S$ 變成橢球，主軸方向就是 $\mathbf{q}_p$、半徑就是 $|\lambda_p|$；
- **$P_p$ 三性質：** 看完備性（三項加總 = $I$）/ 正交性（$P_p P_q = O$）/ 冪等性（重複投影不變）；
- **跨章連結：** 點 (P4) 按鈕跳 ch05 VizScript-03 看一般三明治結構（理解 EVD 是 P4 的「自鏡像」特例）。

#### C. 互動參數（UI Inputs）

- **矩陣輸入 $S$：** $n \times n$ 格子網格，$n \in \{2, 3\}$，每格 $s_{ij} \in [-9, 9]$ 步進 1；
  - **強制對稱：** 改 $s_{ij}$ 自動同步改 $s_{ji}$（UI 上連動）；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$（書中 2×2 範例，$\lambda = 4, 2$ 兩正特徵值）；
  - 範例 2：$\bigl[\begin{smallmatrix}2&-1\\-1&2\end{smallmatrix}\bigr]$（$\lambda = 3, 1$ 兩正特徵值）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&2\\2&1\end{smallmatrix}\bigr]$（$\lambda = 3, -1$ **一正一負**，橢球變雙曲線）；
  - 範例 4：$\bigl[\begin{smallmatrix}3&0&0\\0&2&0\\0&0&1\end{smallmatrix}\bigr]$（**已是對角**，$Q = I$ 特例）；
  - 範例 5：$\bigl[\begin{smallmatrix}2&1&0\\1&2&0\\0&0&3\end{smallmatrix}\bigr]$（3×3 含一個獨立軸）；
  - 範例 6：$\bigl[\begin{smallmatrix}1&1&1\\1&1&1\\1&1&1\end{smallmatrix}\bigr]$（**退化** rank = 1，$\lambda = 3, 0, 0$，譜分解只有 1 項）；
- **動畫模式切換 (radio)：** `分項動畫（手動下一項）` / `自動播放譜分解` / `對比 $S$ vs 橢球變形`；
- **3D 視窗開關 (checkbox)：** 開啟後右側顯示 3D 視窗（僅當 $n \in \{2, 3\}$ 可用）；
- **顯示模式 (checkbox 三選擇)：** `顯示譜分解` / `顯示橢球` / `顯示 $P_p$ 三性質`；
- **跳轉按鈕：**
  - 「→ (P4) 三明治結構」按鈕（跳 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)，自動把 $V^{\mathrm{T}}$ 鎖成 $U^{\mathrm{T}}$，把 $\Sigma$ 換成 $\Lambda$）；
  - 「→ (MM4) 秩 1 累加」按鈕（跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) 看一般 (MM4) 累加形式）。

#### D. 視覺布局（Layout）

**主畫面三區（標準模式）：**

| 區 | 內容 |
|---|---|
| 左區（輸入） | $S$ 的格子輸入網格（含對稱連動）+ 預設範例選擇器 + radio + 顯示模式 checkbox |
| 中區（譜分解動畫） | $S, Q, \Lambda, Q^{\mathrm{T}}$ 四矩陣並排（鏡像布局） + 拆解後 3 項 $\lambda_p P_p$ 並排（含 + 號）+ 當前正在處理的項高亮（金色框）|
| 右區（3D 視窗，可選） | 3D 座標系中顯示單位球（灰色半透明）→ 變成橢球（金色半透明）+ 3 條 $\mathbf{q}_p$ 主軸（綠箭頭）+ 半徑標 $|\lambda_p|$ |

**底部資訊條：**

- 當前的 $\lambda_p, \mathbf{q}_p$ 數值（小字）；
- 「**譜定理驗證：$\sum \lambda_p P_p = S$**」（綠色 ✓ 顯示，hover 顯示計算過程）；
- 「**$P_p$ 三性質**」（三個小綠 ✓：完備 / 正交 / 冪等）；
- **跳轉按鈕區**（兩個橫向按鈕：→ (P4) 三明治 / → (MM4) 秩 1）。

#### E. 動畫腳本（Storyboard）

**Step 1（0–500ms）：** $S$ 的格子網格從左區滑入中區，特徵值計算啟動（後台），公式區顯示 `det(S - λI) = 0` 求 $\lambda_p$。

**Step 2（500–1500ms）：** $\lambda_p, \mathbf{q}_p$ 計算完成，$Q, \Lambda, Q^{\mathrm{T}}$ 三矩陣依序滑入中區（鏡像布局：$Q$ 在 $\Lambda$ 左側，$Q^{\mathrm{T}}$ 在右側，明顯**鏡像對稱**）；
- 3D 視窗：單位球淡入（灰色，半徑 1）→ $S$ 作用後變成橢球（金色，主軸長度 = $|\lambda_p|$，主軸方向 = $\mathbf{q}_p$ 綠箭頭）；
- 公式區同步顯示 `S = Q Λ Q^T`。

**Step 3（1500–3000ms，第 $p = 1$ 項，$\lambda_1$ 最大）：**
- 高亮第 1 項 $\lambda_1 \mathbf{q}_1 \mathbf{q}_1^{\mathrm{T}}$（金色框）；
- $\mathbf{q}_1$ 從 $Q$ 第 1 列位置「飛出」一份（綠色直立列副本）→ $\mathbf{q}_1^{\mathrm{T}}$ 從 $Q^{\mathrm{T}}$ 第 1 行位置「飛出」一份（淡綠橫躺行副本）→ 兩者疊在第 1 拆解項位置上組成 $P_1 = \mathbf{q}_1 \mathbf{q}_1^{\mathrm{T}}$ 矩陣；
- $\lambda_1$ 藍點從 $\Lambda$ 對角位置「飛出」一份 → 顯示為 $\lambda_1 P_1$ 的係數；
- 累計部分和 $S^{(1)} = \lambda_1 P_1$ 顯示為 3D 視窗中的「**只沿 $\mathbf{q}_1$ 方向的縮放**」（橢球瞬間變一條粗線，沿 $\mathbf{q}_1$ 方向長度 $|\lambda_1|$）。

**Step 4（3000–4500ms，第 $p = 2$ 項，$\lambda_2$）：**
- 類似 Step 3，但用 $\lambda_2, \mathbf{q}_2$；
- 累計部分和 $S^{(2)} = \lambda_1 P_1 + \lambda_2 P_2$ 顯示為 3D 視窗中的「**$\mathbf{q}_1, \mathbf{q}_2$ 兩個方向的縮放疊加**」（線變橢圓）；
- 顯示誤差 $\|S - S^{(2)}\|_F$（若 $n = 2$ 此時誤差 = 0）。

**Step 5（4500–6000ms，第 $p = 3$ 項，$\lambda_3$，若 $n = 3$）：**
- 類似 Step 3，但用 $\lambda_3, \mathbf{q}_3$；
- 累計部分和 $S^{(3)} = \lambda_1 P_1 + \lambda_2 P_2 + \lambda_3 P_3$（**完整**）；
- 3D 視窗：橢圓變完整橢球，主軸對齊 $\{\mathbf{q}_1, \mathbf{q}_2, \mathbf{q}_3\}$；
- 顯示誤差 $\|S - S^{(3)}\|_F = 0$ ✓（譜定理驗證）。

**Step 6（按 `顯示 $P_p$ 三性質` checkbox）：**
- 三個 $P_p$ 矩陣淡入並排顯示；
- **完備性：** 三個 $P_p$ 同時亮起綠光 → 「飛」到一起加總 → 變成 $I_n$（藍色對角點）；
- **正交性：** $P_1 P_2$ 計算動畫 → 結果矩陣全為 0（藍灰）；同樣演示 $P_2 P_3, P_3 P_1$；
- **冪等性：** $P_1$ 自乘 → 結果仍是 $P_1$（高亮自我複製動畫）。

**Step 7（按 `對比` radio）：** 顯示「3D 旋轉動畫」：
- 旋轉 360° 看橢球從不同角度的形狀；
- 標出「**$\mathbf{q}_p$ 方向 = 橢球主軸方向 = $S$ 的不變方向**」；
- 互動拉桿改 $\lambda_p$ 看橢球如何即時拉伸 / 壓扁 / 翻轉（負特徵值 → 鏡像反射）。

#### F. 配色（依全書視覺一致性錨點）

- **綠 `#2ca02c`：** $\mathbf{q}_p$ / $Q$ 的列 / 3D 視窗中的橢球主軸；
- **淺綠（半透明）：** $\mathbf{q}_p^{\mathrm{T}}$ / $Q^{\mathrm{T}}$ 的行（強調轉置 = 同向量擺向不同）；
- **灰 `#cccccc`：** 原始單位球（3D 視窗）/ 對稱輸入 $S$ 的方框 fill；
- **金 `#FFD700`：** 變形後的橢球 / 當前正在處理的項（高亮框）；
- **藍 `#1f77b4`：** $\Lambda$ 的對角元素（藍點）/ 完備性結果 $I$（藍對角點）；
- **紫 `#9467bd`：** 退化警示（範例 6 rank 不足）/ 負特徵值的鏡像反射；
- **紅 `#d62728`：** （此章較少用）誤差條 / $\|S - S^{(k)}\|_F > 0$ 警示。

#### G. 計算邏輯（Numerical Backend）

```python
def spectral_decomposition(S: np.ndarray) -> tuple[np.ndarray, np.ndarray, list[dict]]:
    """Symmetric S → (Q, Lambda, history_for_animation).
    Assumes S is symmetric. Returns eigenvalues sorted descending."""
    assert np.allclose(S, S.T), "S must be symmetric"
    eigvals, eigvecs = np.linalg.eigh(S)  # eigh for symmetric
    # Sort by |eigenvalue| descending (so largest visual contribution first)
    order = np.argsort(-np.abs(eigvals))
    Lambda = np.diag(eigvals[order])
    Q = eigvecs[:, order]
    history = []
    S_partial = np.zeros_like(S, dtype=float)
    for p in range(S.shape[0]):
        q_p = Q[:, p:p+1]
        P_p = q_p @ q_p.T
        lam_p = eigvals[order[p]]
        S_partial = S_partial + lam_p * P_p
        history.append({
            'p': p + 1,
            'lambda_p': lam_p,
            'q_p': q_p.flatten().tolist(),
            'P_p': P_p.tolist(),
            'S_partial': S_partial.tolist(),
            'error_fro': float(np.linalg.norm(S - S_partial, 'fro')),
        })
    return Q, Lambda, history


def verify_P_properties(Q: np.ndarray) -> dict:
    """Verify P_p three properties: completeness, mutual orthogonality, idempotence."""
    n = Q.shape[1]
    P_list = [Q[:, p:p+1] @ Q[:, p:p+1].T for p in range(n)]
    completeness = np.allclose(sum(P_list), np.eye(n))
    orthogonality = all(
        np.allclose(P_list[p] @ P_list[q], 0)
        for p in range(n) for q in range(n) if p != q
    )
    idempotence = all(
        np.allclose(P_list[p] @ P_list[p], P_list[p])
        for p in range(n)
    )
    return {
        'completeness': completeness,
        'orthogonality': orthogonality,
        'idempotence': idempotence,
    }


def ellipsoid_axes(S: np.ndarray) -> tuple[list[float], list[list[float]]]:
    """For 3D visualization: return semi-axis lengths and directions."""
    eigvals, eigvecs = np.linalg.eigh(S)
    semi_axes = [abs(lam) for lam in eigvals]
    directions = [eigvecs[:, p].tolist() for p in range(len(eigvals))]
    return semi_axes, directions
```

**3D 橢球渲染（matplotlib 3D 或 plotly 3D）：**

```python
# 參數化單位球：(cos(u)sin(v), sin(u)sin(v), cos(v))
u, v = np.meshgrid(np.linspace(0, 2*np.pi, 50), np.linspace(0, np.pi, 25))
unit_sphere = np.array([np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v)])
# 應用 S 變形：每個球面點 (x,y,z) → S @ (x,y,z)
ellipsoid = np.einsum('ij,jkl->ikl', S, unit_sphere)
# plotly Surface 渲染
```

**正確性驗證：**

- $Q^{\mathrm{T}} Q = Q Q^{\mathrm{T}} = I$（正交性）；
- $S Q = Q \Lambda$（特徵向量定義）；
- $\sum \lambda_p P_p = S$（譜定理）；
- `verify_P_properties` 三項都為 `True`。

#### H. 邊界情況處理

| 情況 | 偵測 | 處理 |
|---|---|---|
| $S$ 不對稱 | `np.allclose(S, S.T) == False` | UI 強制對稱連動，或彈警示「請輸入對稱矩陣」|
| 重根特徵值 | `len(set(eigvals)) < n`（容差比較）| 在重根子空間內 `np.linalg.eigh` 自動正交化，無需特殊處理 |
| 退化（$\lambda_p = 0$）| `abs(lam_p) < tol` | 譜分解仍正確，只是該項 $\lambda_p P_p = 0$；3D 橢球變扁平 |
| 負特徵值 | `lam_p < 0` | 3D 橢球該軸方向反射（紫色提示），$|\lambda_p|$ 為主軸長 |
| 全零 $S = O$ | `np.allclose(S, 0)` | 所有 $\lambda_p = 0$，分解平凡，3D 橢球縮成原點 |

#### I. 完成標準（Acceptance Criteria）

- [ ] 拉任意對稱矩陣 $S$ 的元素 → $\lambda_p, \mathbf{q}_p$ 即時更新（< 100ms）；
- [ ] 譜分解動畫流暢，每項拆解清晰可見（含 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 自外積過程）；
- [ ] 3D 橢球與單位球變形對應正確，主軸方向 = $\mathbf{q}_p$、半徑 = $|\lambda_p|$；
- [ ] $P_p$ 三性質視覺驗證正確（完備 / 正交 / 冪等都 ✓）；
- [ ] 跳轉到 ch05 VizScript-03 / ch04 VizScript-02 後參數正確帶入；
- [ ] 退化 / 負特徵值 / 重根特徵值的邊界情況都正確處理。

#### J. 反例與常見誤解

- **誤解 1：** 「只有對稱矩陣才有特徵分解。」**正解：** 任意方陣都有特徵分解 $A = X \Lambda X^{-1}$（除了部分需 Jordan 標準形的退化情形），但**只有對稱矩陣保證 $X$ 正交、$\Lambda$ 實對角、$X^{-1} = X^{\mathrm{T}}$**。EVD 的「美麗」來自對稱性的禮物；
- **誤解 2：** 「特徵值必為正。」**正解：** 對稱矩陣的特徵值是實數，但**可正可負可零**（範例 3 是一正一負）。**只有「對稱正定」才保證 $\lambda_p > 0$**（這是 PCA 用協方差矩陣的根本原因）；
- **誤解 3：** 「$Q$ 的列順序可任意。」**正解：** $Q$ 的列順序必須與 $\Lambda$ 的對角元素順序對應（$\mathbf{q}_p$ 是 $\lambda_p$ 對應的特徵向量），通常按 $\lambda_p$ 大小降冪排列（PCA 標準做法）；
- **誤解 4：** 「(P4) 三明治可以隨便用 EVD 看待。」**正解：** EVD 是 (P4) 的「自鏡像 + 對稱」特化，**不能反過來**把任意 (P4) 三明治稱為 EVD。一般 (P4) 是 SVD（§6.5），EVD 是其特殊情形。

#### K. 與其他 VizScript 的關係

- **本章 VizScript-02 / 03：** Tier 1 精簡版分別獨立處理 $P_p$ 三性質驗證和 2×2 數值範例 walkthrough；
- **ch04 VizScript-02 (MM4 秩 1 累加 + Mona Lisa SVD demo)：** 提供「秩 1 累加」的母模板。EVD 的「$\sum \lambda_p P_p$」是「對稱情境的 (MM4)」，動畫可重用；
- **ch05 VizScript-03 (P4 三明治)：** **本 VizScript 的單 pointer 目標**。EVD 是 (P4) 的「左 = 右轉置」特化，視覺布局共用「三明治」基本結構；
- **ch05 VizScript-02 (P3 動態系統)：** P3 是 $X D X^{-1}$（一般特徵分解）；EVD 的對稱版直接用 $Q D Q^{\mathrm{T}}$ 取代，動態系統 demo 可重用框架（如「對稱版動態系統」demo）；
- **ch06f VizScript-01 (SVD)：** SVD 是 EVD 的「一般化」（雙側不同正交矩陣）。**本 VizScript 的 3D 橢球視覺與 SVD 的「奇異值橢球」直接對應** — EVD 橢球是「對稱情境的 SVD 橢球」；
- **後續：** S12+ 實作時，本 VizScript 與 ch06f VizScript-01（SVD）共享 3D 橢球渲染棧，可顯著節省工時。

#### L. 配套素材清單

- **必備：** Python 3.11+、NumPy（`linalg.eigh`）、matplotlib 3D 或 plotly 3D（橢球渲染）、reactive UI 框架（marimo/streamlit）；
- **可選：** scipy.linalg（提供 `eigh_tridiagonal` 等更快的對稱矩陣特徵值算法）；
- **教學素材：** 「對稱矩陣典型例子」清單（協方差、Hessian、Gram 矩陣、二次型）每個各一張說明卡；
- **未來擴展：** 「協方差矩陣的 PCA 應用」demo（用真實資料如 Iris 資料集）、「Hessian 二次優化」demo。

#### M. 預期使用者反饋

- **「終於懂了為什麼對稱矩陣這麼特別」：** 透過 3D 橢球主軸對齊 + $Q^{\mathrm{T}} = Q^{-1}$ 的視覺對比，使用者建立「對稱性 = 雙側正交 + 計算便宜」的核心直覺；
- **「譜定理原來這麼具體」：** 譜分解的「$\sum \lambda_p P_p$ 加權累加」動畫讓抽象譜定理變成可看見的「投影 + 縮放」過程；
- **「PCA 的數學基礎終於清楚了」：** 透過協方差矩陣 EVD demo（M 段擴展），使用者理解「PCA = 對協方差矩陣做 EVD，挑前幾個最大特徵值對應的 $\mathbf{q}_p$ 作為主成分」；
- **「(P4) 三明治原來有這麼多變種」：** 透過跨章跳轉看 ch05 VizScript-03 一般 (P4) → 回 EVD 自鏡像 (P4) → 再到 ch06f SVD 雙側不同 (P4)，建立「(P4) 是 §6 後三章的共同骨架」整合視角。

---

### VizScript-02: $P_p$ 三性質視覺驗證（精簡）

**Tier：** ⭐⭐ Tier 1（精簡 13 段）
**對應 VizMark：** Figure 6.6 VizMark-02
**預估實作工作量：** S12+ 約 0.5 session

#### A. 一句話定位

「給一個對稱矩陣 $S$，視覺化驗證投影矩陣 $P_p$ 的三條性質：完備（$\sum P_p = I$）/ 正交（$P_p P_q = O$）/ 冪等（$P_p^2 = P_p$）。」

#### B. 學習目標

- 把譜定理的抽象性質「**投影矩陣群**」變成具體的矩陣加法 / 乘法演示；
- 建立「正交基底 + 投影 = 完整覆蓋空間」的直覺。

#### C. 互動參數（精簡）

- **預設範例選擇器：** 5 個對稱矩陣（與 VizScript-01 共用）；
- **顯示模式 (radio)：** `完備性` / `正交性` / `冪等性`。

#### D-E. 視覺布局 + 動畫腳本（合併精簡）

**布局：** 上方 $S$ 矩陣 + 中間 3 個 $P_p$ 並排（每個展示 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 自外積結構）+ 底部驗證結果區。

**動畫：**
- 切換 `完備性`：3 個 $P_p$ 同時亮綠光 → 「飛」到一起加總 → 變成 $I_n$（藍色對角點，動畫 800ms）；
- 切換 `正交性`：選兩個 $P_p, P_q$（$p \neq q$）→ 計算 $P_p P_q$ 動畫 → 結果矩陣全為 0（藍灰填充 + 顯示 `= O`）；
- 切換 `冪等性`：選一個 $P_p$ → $P_p \cdot P_p$ 計算動畫 → 結果仍為 $P_p$（高亮自我複製動畫）。

#### F-M. 配色 / 計算 / 完成標準（共用 VizScript-01 規範，略）

**單一新功能：** 把 VizScript-01 的「Step 6 $P_p$ 三性質驗證」獨立成單章節，方便快速演示譜定理代數性質而不用看完整動畫。

---

### VizScript-03: 2×2 EVD 數值範例 walkthrough（輕量）

**Tier：** ⭐ Tier 1（輕量輪廓）
**對應 VizMark：** Figure 6.6 VizMark-03
**預估實作工作量：** S12+ 約 0.3 session

#### A. 一句話定位

「用 2×2 範例 $S = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$ 一步一步動畫展示 EVD 計算過程：求特徵值 → 求特徵向量 → 譜分解，每步顯示具體數字。」

#### B-M. 簡述

**步驟動畫：**

1. 顯示 $S = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr]$；
2. 計算 $\det(S - \lambda I) = (3-\lambda)^2 - 1 = \lambda^2 - 6\lambda + 8 = 0$；
3. 求解 $\lambda = (6 \pm \sqrt{36-32})/2 = (6 \pm 2)/2$ → $\lambda_1 = 4, \lambda_2 = 2$；
4. 解 $(S - 4I)\mathbf{q}_1 = \mathbf{0}$ → $\mathbf{q}_1 = (1, 1)^{\mathrm{T}}/\sqrt{2}$；
5. 解 $(S - 2I)\mathbf{q}_2 = \mathbf{0}$ → $\mathbf{q}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$；
6. 驗證正交：$\mathbf{q}_1^{\mathrm{T}} \mathbf{q}_2 = 0$ ✓；
7. 組裝 $Q = \frac{1}{\sqrt{2}}\bigl[\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr]$，$\Lambda = \bigl[\begin{smallmatrix}4&0\\0&2\end{smallmatrix}\bigr]$；
8. 譜分解 $S = 4 P_1 + 2 P_2$ 計算每個 $P_p$；
9. 累加驗證 $4 \cdot \frac{1}{2}\bigl[\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr] + 2 \cdot \frac{1}{2}\bigl[\begin{smallmatrix}1&-1\\-1&1\end{smallmatrix}\bigr] = \bigl[\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr] = S$ ✓。

**用途：** 入門教學，讓使用者第一次接觸 EVD 時看到完整計算過程的具體數字。**不含 3D 視窗、不含拖拉互動**，純步進動畫。

---

## 章末延伸

### 與 §1–§5 的來源對應

- **§1（Viewing a Matrix）：** EVD 的「對稱性」可視為「**4 視角中行 = 列轉置**」的特例 — 對稱矩陣的列空間 = 行空間 = $\mathbf{C}(Q)$；
- **§2（Vector × Vector）：** EVD 的 $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 是「自外積」（v2 視角的特例：兩個外積向量相同）；
- **§3（Matrix × Vector）：** EVD 的「$S \mathbf{q}_p = \lambda_p \mathbf{q}_p$」是「**矩陣 × 向量 = 純縮放（不轉向）**」的特殊情境，這定義了「特徵向量 = 不變方向」；
- **§4（MM4）：** 譜分解 $S = \sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 是 (MM4) 「外積之和」的特化（兩個外積向量相同 + 對稱矩陣保證項數 = 維度）；
- **§5（P4）：** **`EVD.png` 直接標 `using P4`**，EVD 是 (P4) 三明治的「自鏡像 + 對角是特徵值」特化。

### 與 §6 其他分解的對應

- **§6.1 CR：** 對對稱 $S$ 應用 CR 得到 $C, R$，但 $C, R$ 一般不對稱；EVD 直接利用對稱性免去 CR 的「找獨立列」步驟；
- **§6.2 LU：** 對稱 $S$ 的 LU 是 $S = L D L^{\mathrm{T}}$（對稱版 LU），$L$ 下三角、$D$ 對角；EVD 比 LU **多一層正交化**（$L$ 變正交 $Q$）；
- **§6.3 QR：** QR 是「列正交化」（一般矩陣）；EVD 是「對稱矩陣的雙側正交化」。**從 QR 到 EVD = 強制 $A$ 對稱 + 把 $R$ 也正交化變對角**；
- **§6.5 SVD：** **SVD 是 EVD 的一般化** — 任意矩陣 $A$ 的 $A^{\mathrm{T}} A$ 對稱半正定 → 用 EVD 得到右奇異向量 $V$ 和奇異值平方 $\Sigma^2$；同樣 $AA^{\mathrm{T}}$ EVD 得 $U$。**SVD = 兩個 EVD 的整合**（詳見 §6.5）。

### 工程應用前瞻（S12+ 實作目標）

- **PCA（主成分分析）：** 對協方差矩陣 $C = \frac{1}{N} X^{\mathrm{T}} X$ 做 EVD，挑前 $k$ 個最大特徵值對應的 $\mathbf{q}_p$ 作為主成分。本 VizScript-01 加 PCA demo（用 Iris 資料集，2D/3D 視覺降維過程）；
- **譜聚類（Spectral Clustering）：** 對相似度矩陣（對稱）做 EVD，用前幾個 $\mathbf{q}_p$ 作為新特徵空間的座標，再做 K-means。本章 VizScript-01 可擴展為「圖譜分析」demo；
- **二次型優化：** Hessian 矩陣 $H$ EVD → 看 $\lambda_p$ 符號判斷「凸 / 凹 / 鞍點」，看 $\mathbf{q}_p$ 方向決定下降方向。本 VizScript-01 可擴展為「優化問題的二次型可視化」demo；
- **量子力學：** 可觀測量算符 $\hat{O}$ EVD → 特徵值 = 觀測結果、特徵向量 = 對應的量子態。本章 VizScript-01 可擴展為「量子算符的譜分解」demo；
- **振動模態分析：** 結構矩陣 $K$（剛度矩陣，對稱半正定）EVD → 特徵值 = 振動頻率平方、特徵向量 = 振動模態。本章 VizScript-01 可擴展為「彈簧—質量系統的模態分解」demo。

### 來源對照

| 元素 | 來源 |
|---|---|
| 數學公式 | `from-tex/en.md` line 430–505、`from-tex/zh.md` line 418–492 |
| 圖片 | `figs-png/EVD.png`（原始 EPS：`figs/EVD.eps`，原書 p.11）|
| Strang 連結 | LA for Everyone Sec. 6.3（對稱正定矩陣） |
| Pattern 連結 | §5 (P4) 三明治，本書 PNG 直接標 `using P4` |
| (MM4) 連結 | §4 (MM4) 外積之和，EVD 是「自外積」特化 |
| 跨章 pointer | [ch05 VizScript-03](ch05-patterns.md#vizscript-03)（單 pointer，PNG 標 P4）/ [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)（次要 pointer，看 (MM4) 累加）|
