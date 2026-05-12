# 附錄 B：矩陣世界（Matrix World）— 全書地圖

> **原書頁碼：** 英文版 References 第 4 條（p.34）/ 簡中版同
> **對應 .tex 段落：** `from-tex/en.md` 第 604–610 行（References 區）/ 完整 PDF：[`MatrixWorld.pdf`](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MatrixWorld.pdf)
> **本章圖數：** 1（`MatrixWorld.png`）
> **本章 VizMark 數：** 1（⭐⭐⭐ Tier 2 旗艦索引地圖 — S12+ 將作為「全書互動式教材的首頁」）
> **PNG `using XX` 標記：** **無**（S10 PNG 重核確認 — 圖內標記是 Strang《Linear Algebra for Everyone》的 section number（1.4 / 7.1 / 4.4 / 6.2 / 6.3 / 4.2 / 2.4 / 3.5 等），不是本書 Pattern 標記）
> **狀態：** [x] 已完成

---

## 章節摘要

《Matrix World》是 Kenji Hiranabe 於 2020 年發布、2023 年 v1.5 修訂的獨立 slidedeck，**並非《Linear Algebra for Everyone》主書內容**，而是「**所有矩陣類別的同心橢圓全景地圖**」。它把從最廣的「**矩陣 $m \times n$**」開始，一層一層往內縮，最終縮到「**單位矩陣 $I$ + 零矩陣 $O$**」這個最核心。每一層橢圓代表一類矩陣的**繼承關係**（內層 ⊂ 外層）：方陣 ⊂ 矩陣、可對角化 ⊂ 方陣、Normal ⊂ 可對角化、對稱 ⊂ Normal、正定 ⊂ 對稱 ... 直到 $I, O$。每層都標註「**對應的矩陣分解**」（如外圈標 $A = CR$ / $A = U\Sigma V^{\mathrm{T}}$、方陣層標 $A = QR$ / $A = LU$、對稱層標 $S = Q\Lambda Q^{\mathrm{T}}$、可對角化層標 $A = X\Lambda X^{-1}$）+「**對應 Strang 書的 section number**」（1.4 / 7.1 / 4.4 / 2.3 / 6.2 / 6.3 / 4.2 等）。本附錄是**全書 §1–§6 的「視覺索引」**，每個元素都 pointer 到對應章節 + VizScript。互動式版本 ⭐⭐⭐ Tier 2 旗艦規格：「點任一橢圓 / 標籤 / 分解符號 → 自動跳到對應章節 + VizScript」，是 S12+ 完成後**互動式教材的首頁**。

---

## 數學要點

### 1. 同心橢圓的繼承層次（核心 ⭐）

> Matrix World 的核心邏輯是：**外層橢圓包含內層橢圓**，數學上表示「**外層的矩陣集合 ⊇ 內層**」。也就是「**內層的矩陣是外層的特例**」 — 性質越特殊、約束越多、橢圓越內。

**完整 11 層繼承樹（從外到內）：**

| 層級 | 矩陣類別 | 定義 / 約束 | 對應 Strang 書 section | 對應本互動式版本 |
|---|---|---|---|---|
| **L0（最外）** | **Matrix $m \times n$** | 任意實矩陣 | 1.4 | [ch01](ch01-viewing-matrix.md) |
| L1 | 含分解 $A = CR$ / $A = U\Sigma V^{\mathrm{T}}$ | 任意矩陣可分解 | 1.4 / 7.1 | [ch06b CR](ch06b-CR.md) / [ch06f SVD](ch06f-USV.md) |
| **L2** | **Square Matrix $n \times n$** | $m = n$ | — | [ch06](ch06a-five.md) |
| L2a | Invertible | $\det A \neq 0$，$\forall \lambda \neq 0$ | — | [ch06f §6.5](ch06f-USV.md) |
| L2b | Singular | $\det A = 0$，$\exists \lambda = 0$ | — | [Map of Eigenvalues](appendix-map-eigenvalues.md) |
| L3 | 含分解 $A = QR$ / $A = LU$ | 方陣分解 | 4.4 / 2.3 | [ch06d QR](ch06d-QR.md) / [ch06c LU](ch06c-LU.md) |
| **L4** | **Diagonalizable** | $\exists X, \Lambda: A = X\Lambda X^{-1}$，$X$ 可逆 | 6.2 | [ch06e EVD](ch06e-QLQ.md) §7 |
| L4a | 含分解 $A = X\Lambda X^{-1}$ | 一般可對角化 | 6.2 | [ch06e](ch06e-QLQ.md) |
| L4b | 不可對角化（Jordan form）| $A = X J X^{-1}$，$J$ 含 Jordan 塊 | A7 | [ch06e § Jordan 補述](ch06e-QLQ.md) |
| **L5** | **Normal** | $A^{\mathrm{T}}A = A A^{\mathrm{T}}$，**正交對角化** | A5 | [ch06e § 對稱推廣](ch06e-QLQ.md) |
| **L6** | **Symmetric** | $S = S^{\mathrm{T}}$，$\forall \lambda \in \mathbb{R}$ | 2.4 | [ch06e EVD](ch06e-QLQ.md) §1 |
| L6a | 含分解 $S = Q\Lambda Q^{\mathrm{T}}$ | 對稱譜分解 | 6.3 | [ch06e](ch06e-QLQ.md) |
| L7a | **Positive Semidefinite** | $\forall \lambda \geq 0$，$\forall A^{\mathrm{T}}A$ | 6.3 | [Map of Eigenvalues](appendix-map-eigenvalues.md) |
| **L7b** | **Positive Definite** | $\forall \lambda > 0$ | 6.3 | [Map of Eigenvalues](appendix-map-eigenvalues.md) |
| L8a | **Orthogonal** | $Q^{-1} = Q^{\mathrm{T}}$，$\forall \| \lambda \| = 1$ | 4.4 | [ch06d QR](ch06d-QR.md) |
| L8b | Permutation | $Q$ 為單位矩陣的列排列 | 2.4 | [ch05 (P1)(P2)](ch05-patterns.md) |
| **L9** | **Projection** | $P^2 = P = P^{\mathrm{T}}$，$\lambda \in \{0, 1\}$ | 4.2 | [ch05 (P4)](ch05-patterns.md) / [ch06d QR](ch06d-QR.md) |
| **L10** | **Diagonal** | 對角矩陣，$\Sigma = \text{diag}(\sigma^2, \sigma^2)$、$\Lambda = \text{diag}(\lambda, \lambda)$ | — | [ch05 (P1)(P2)](ch05-patterns.md) |
| **L11（最內）** | **$I, O$** | 單位矩陣 + 零矩陣 | — | [Map of Eigenvalues](appendix-map-eigenvalues.md) |

### 2. 偽反矩陣的全矩陣統一公式（底部標註）

> 圖底部標：$A^{-1} = V\Sigma^{-1}U^{\mathrm{T}} \quad \leftrightarrow \quad A^{+} = V\Sigma^{+}U^{\mathrm{T}}$ (3.5, 7.4)

這是 **Matrix World 的最重要單一發現** — Strang 把「逆矩陣（只對可逆方陣有效）」與「**Moore-Penrose 偽反矩陣 $A^{+}$**（對任意矩陣有效）」用 **SVD 統一**：

$$
A = U \Sigma V^{\mathrm{T}} \implies
\begin{cases}
A^{-1} = V \Sigma^{-1} U^{\mathrm{T}} & \text{若 } A \text{ 方且可逆} \\
A^{+} = V \Sigma^{+} U^{\mathrm{T}} & \text{對任意 } A \in \mathbb{R}^{m \times n}
\end{cases}
$$

其中 $\Sigma^{+}$ 是 $\Sigma$ 的偽反（$\sigma_p > 0$ 取倒數，$\sigma_p = 0$ 維持 0）。**$A^{+}$ 把「逆矩陣」這個只對可逆方陣有效的概念，推廣到所有 $m \times n$ 矩陣** — 這是 SVD 的核心應用之一（已在 [ch06f §6 (4 大應用)](ch06f-USV.md#6) 詳述）。

### 3. Matrix World 的兩條軸線

> Matrix World 不只是同心橢圓 — 它把矩陣分類**沿兩條軸線**展開：

#### 軸線 A：縱深（外 → 內）= 性質越特殊

```
Matrix → Square → Diagonalizable → Normal → Symmetric → Positive Definite → Diagonal → I, O
```

每層加上一個約束（$m = n$、可對角化、$A^{\mathrm{T}}A = AA^{\mathrm{T}}$、$S = S^{\mathrm{T}}$、$\lambda > 0$、...），直到單位矩陣 $I$ 與零矩陣 $O$（最強約束）。

#### 軸線 B：橫向（左 ↔ 右）= 對稱 vs 一般

每層左半多放「**一般情形的分解**」（$A = X\Lambda X^{-1}$ 對角化、$A = LU$ 三角化、$A = QR$ Gram-Schmidt），右半放「**正交 / 對稱版本**」（$S = Q\Lambda Q^{\mathrm{T}}$、$A = U\Sigma V^{\mathrm{T}}$、Permutation 對角）。**這是 §6 五大分解的「視覺地圖化」** — 看一張圖即可知道每個分解屬於哪一類矩陣、誰是誰的特例。

### 4. 連結 §6 五大分解總覽

| 五大分解 | 在 Matrix World 中的位置 | 適用矩陣 | 本互動式版本 |
|---|---|---|---|
| $A = CR$ | **最外層 L1** | 任意矩陣 | [ch06b](ch06b-CR.md) |
| $A = U\Sigma V^{\mathrm{T}}$ | **最外層 L1**（與 CR 同層）| 任意矩陣 | [ch06f](ch06f-USV.md) |
| $A = LU$ | L3（方陣層）| 方陣（多數可解 $A\mathbf{x}=\mathbf{b}$）| [ch06c](ch06c-LU.md) |
| $A = QR$ | L3（方陣層）+ L8（正交層補強）| 方陣（含瘦長 $m \geq n$）| [ch06d](ch06d-QR.md) |
| $S = Q\Lambda Q^{\mathrm{T}}$ | **L6（對稱層）** | 僅對稱矩陣 | [ch06e](ch06e-QLQ.md) |

**讀圖直覺：** 從外往內，分解越「特化」、適用範圍越窄、但結構越優美。**SVD 是「**唯一一個適用任意矩陣**」的分解** — 這就是為什麼 SVD 是「**集大成終章**」（[ch06f](ch06f-USV.md) 已詳述）。

---

## 圖片詳細描述（Figure Description）

### Figure B.1: 矩陣世界（Matrix World）— v1.5（2023-03-02）

**圖檔：** `docs/book/figs-png/MatrixWorld.png`（原始 PDF：`MatrixWorld.pdf` v1.5）
**原書頁碼：** Slidedeck 獨立發布（References 第 4 條，v1.5 修訂版）
**所屬章節：** 附錄 B

#### 視覺結構 (Visual Structure)

整體**一張大圖**呈現「**同心橢圓宇宙**」：

- **整體布局：** 中央是橢圓巢狀結構（從最外的「Matrix ($m \times n$)」一直縮到最內的「$I, O$」），左右兩側散佈著「**範例矩陣**」（如 $\Lambda = \bigl[\begin{smallmatrix}1&2&3\\4&5&6\end{smallmatrix}\bigr]$、$\Lambda = \bigl[\begin{smallmatrix}2&1\\0&2\end{smallmatrix}\bigr]$、$\Lambda = \bigl[\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr]$ 等）+「**分解符號 + section number**」（深灰底白字的標籤如「1.4 $A=CR$」「7.1 $A=U\Sigma V^{\mathrm{T}}$」）

- **同心橢圓層次（從外到內）：**
  1. **最外橢圓：** 標 "Matrix ($m \times n$)"，內含「$A = CR$」(1.4) 與「$A = U\Sigma V^{\mathrm{T}}$」(7.1)，標註「row rank = column rank」「SVD: orthonormal basis $U, V$」
  2. **第 2 層：** 「Square Matrix ($n \times n$)」，分為「Invertible（$\det(\Lambda) \neq 0$, all $\lambda \neq 0$）」與「Singular（at least one $\lambda = 0$, $\det(\Lambda) = 0$）」
  3. **第 3 層：** 「$A = QR$」(4.4，左 Gram-Schmidt) 與「$A = LU$」(2.3，右 Triangularize，「$U$ has at least one zero row」說明）
  4. **第 4 層：** "Diagonalizable" + 兩種分解：「$A = X\Lambda X^{-1}$」(6.2，左) 與「$A = XJX^{-1}$」(A7，右，$J$ = Jordan form)
  5. **第 5 層：** "Normal" (A5)，"$A^{\mathrm{T}}A = AA^{\mathrm{T}}$, diagonalizable by orthogonal matrix"
  6. **第 6 層（重要）：** "Symmetric" (2.4)，"$S = S^{\mathrm{T}}$, all $\lambda$ are real"，含「$S = Q\Lambda Q^{\mathrm{T}}$」(6.3) 與「Positive Semidefinite」(6.3) 兩標籤
  7. **第 7 層：** "Orthogonal" (4.4)，"$Q^{-1} = Q^{\mathrm{T}}$, all $|\lambda| = 1$"，內含 "Permutation" (2.4) 「permutation of $I$, all $\lambda$ are roots of 1」
  8. **第 8 層：** "Projection" (4.2)，"$P^2 = P = P^{\mathrm{T}}, \lambda = 1$ or $0$"
  9. **第 9 層：** "Diagonal"，$\Sigma = \bigl[\begin{smallmatrix}\sigma^2&\\&\sigma^2\end{smallmatrix}\bigr]$ 與 $\Lambda = \bigl[\begin{smallmatrix}\lambda&\\&\lambda\end{smallmatrix}\bigr]$
  10. **第 10 層：** "Positive Definite" (6.3)，"all $\lambda > 0$"
  11. **最內層：** "$I, O$"（單位矩陣 + 零矩陣）

- **底部標：** $A^{-1} = V\Sigma^{-1}U^{\mathrm{T}} \leftrightarrow A^{+} = V\Sigma^{+}U^{\mathrm{T}}$ (3.5, 7.4) — 偽反矩陣統一公式

- **右上角圖例：** "Matrix Factorization"（深灰底，矩陣分解標籤）+ "Appearing section"（淺灰底，Strang 書 section number）

- **左下角署名：** "Drawn by Kenji Hiranabe / with the help of Prof. Gilbert Strang / (v1.5, Mar.2nd, 2023)" + 右下 CC-BY 授權標誌

- **整體色調：** 同心橢圓深藍細線 `#1f77b4`、分解標籤深灰底 `#666666` + 白字、section number 淺灰底 + 黑字、範例矩陣黑色純文字無背景；風格冷靜學術，無花俏色彩

- **視覺引導：** 讀者**先看最外橢圓**（理解「這是所有矩陣的全景」）→ **沿軸線縱深往內**（每層加一個約束）→ **對照分解符號**（每層適用的矩陣分解）→ **看 section number**（Strang 書中對應的詳細展開）

#### 數學內容 (Mathematical Content)

**同心橢圓的集合論表達：**

$$
\{I, O\} \subset \text{Diagonal} \subset \text{Positive Definite} \subset \text{Symmetric} \subset \text{Normal} \subset \text{Diagonalizable} \subset \text{Square} \subset \text{Matrix}
$$

**對偶分支（向左 / 向右）：**

$$
\begin{cases}
\text{左分支（一般）：} & A = X\Lambda X^{-1} \quad (\text{可對角化}) \\
\text{右分支（對稱）：} & S = Q\Lambda Q^{\mathrm{T}} \quad (\text{對稱對角化}) \\
\text{底層統一：} & A^{+} = V\Sigma^{+}U^{\mathrm{T}} \quad (\text{適用任意 } A) \\
\end{cases}
$$

**11 層繼承樹的層數約束遞增表：**

$$
\begin{array}{ll}
\text{Matrix:} & \text{無約束} \\
\text{Square:} & m = n \\
\text{Diagonalizable:} & \exists X: A = X \Lambda X^{-1} \\
\text{Normal:} & A^{\mathrm{T}} A = A A^{\mathrm{T}} \\
\text{Symmetric:} & S = S^{\mathrm{T}} \\
\text{Positive Semidefinite:} & \forall \lambda \geq 0 \\
\text{Positive Definite:} & \forall \lambda > 0 \\
\text{Orthogonal:} & Q^{\mathrm{T}}Q = I \\
\text{Projection:} & P^2 = P = P^{\mathrm{T}} \\
\text{Diagonal:} & A_{ij} = 0 \text{ for } i \neq j \\
\{I, O\}: & A = I \text{ or } A = O \\
\end{array}
$$

#### 直覺解讀 (Intuition)

Matrix World 是「**矩陣分類學的視覺百科**」 — 把所有重要矩陣類別、五大分解、對應 Strang 書章節**整合在一張圖**。**最重要的三條洞察：**

**洞察 1：「外層的矩陣分解適用更廣，內層的分解更精緻」** — 最外層的 $A = CR$ 和 $A = U\Sigma V^{\mathrm{T}}$ 適用**任意矩陣**，但分解結構相對「弱」（CR 的 $C$/$R$ 不對稱、SVD 的 $U/V$ 雖然正交但需排序）。最內層的對稱譜分解 $S = Q\Lambda Q^{\mathrm{T}}$ 只適用對稱矩陣，但結構**最優美**（$Q$ 兩側對稱、$\Lambda$ 對角全實）。**這個「廣 vs 精」的折衷是 §6 五大分解設計的核心邏輯**。

**洞察 2：「偽反矩陣 $A^{+}$ 統一了所有逆運算」** — 圖底部「$A^{-1} = V\Sigma^{-1}U^{\mathrm{T}} \leftrightarrow A^{+} = V\Sigma^{+}U^{\mathrm{T}}$」是整個 Matrix World 的「**底層統一定理**」。**任何矩陣**（含 singular、瘦長、矮胖）都可用 SVD 算偽反，這把「解 $A\mathbf{x}=\mathbf{b}$」從「方陣可逆」推廣到「**任意矩陣的最小範數解**」（[ch06f §6.4 推薦系統 / 矩陣補全](ch06f-USV.md#64) 的核心應用）。

**洞察 3：「Symmetric 是矩陣世界的『樞紐』類別」** — 從圖中可見：
- Symmetric → Positive Semidefinite → Positive Definite 是**連續正定性**的階梯
- Symmetric → $S = Q\Lambda Q^{\mathrm{T}}$ 是**正交對角化**的標誌
- Symmetric ⊂ Normal ⊂ Diagonalizable 是**對稱推廣**的階梯
- 任意矩陣 $A$ → $A^{\mathrm{T}}A$ 是「**從任意推導出對稱**」的標準操作（SVD 構造算法核心，見 [ch06f §2 SVD 構造](ch06f-USV.md#2)）

**常見誤解：**

- **「Diagonal ⊂ Positive Definite ⊂ Symmetric — 是否所有對角矩陣都是正定？」** 不！只有「對角元全正」的對角矩陣才是正定。圖中 Diagonal 在 Positive Definite **內**只是表示「**對角矩陣是正定矩陣的一個重要子例**」（若對角元正則正定）。實際上「對角元含負數」的對角矩陣（如 $\bigl[\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\bigr]$）是 Symmetric 但非 Positive Definite。
- **「Normal ⊂ Diagonalizable — 是否所有 normal 都可對角化？」** 是！這正是「Normal」的定義：**用正交矩陣 $Q$ 對角化**。Normal 是「**對稱矩陣的複數版本推廣**」（用 unitary 取代 orthogonal、Hermitian 取代 symmetric）。

**對比另一種看法（Map of Eigenvalues 並列網格）：**

- **Matrix World**（本附錄）用「**同心橢圓**」看類別**繼承**關係 — 適合「**理解誰是誰的特例**」
- **Map of Eigenvalues**（[appendix-map-eigenvalues.md](appendix-map-eigenvalues.md)）用「**並列網格**」看特徵值**位置**指紋 — 適合「**分類辨識**」

兩個附錄是「**同一矩陣分類問題的對偶視覺化**」 — Matrix World 從「**繼承結構**」切入，Map of Eigenvalues 從「**幾何指紋**」切入。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [互動式索引地圖 + 跳轉 dashboard] ⭐⭐⭐ Tier 2 旗艦（**S12+ 將作為「全書互動式教材的首頁」**）
> **位置：** Figure B.1 / 附錄 B 整圖
> **核心概念：** 同心橢圓全書地圖 + 點任一元素跳轉到對應章節 / VizScript
> **互動梗概：** 11 層同心橢圓互動式呈現，每層 hover 顯示說明 + click 觸發兩種行為之一：（A）展開該層的數學定義 + 範例矩陣 mini-dashboard；（B）「→ 跳轉到 chXX 詳細展開」直接導向對應章節。每個分解符號（$A = CR$、$A = LU$、$A = QR$、$A = X\Lambda X^{-1}$、$S = Q\Lambda Q^{\mathrm{T}}$、$A = U\Sigma V^{\mathrm{T}}$、$A^{+}$）都是可點擊按鈕，跳到對應 [ch06a–f](ch06a-five.md) 或 [Map of Eigenvalues](appendix-map-eigenvalues.md)。
> **詳見劇本：** VizScript-01（章末）

---

## 視覺化劇本（VizScripts）

### VizScript-01: 矩陣世界互動式索引地圖（Matrix World Interactive Index — Tier 2 旗艦）

**Tier：** ⭐⭐⭐ Tier 2 旗艦 — **S12+ 將作為「全書互動式教材的首頁」**（與 [ch06a VizScript-01](ch06a-five.md#vizscript-01) 五分解 dashboard 互補：前者是分類學索引、後者是分解視覺化索引）
**對應 VizMark：** Figure B.1 / VizMark-01

> 本劇本是「**全書導覽中樞**」 — 不重複實作任何具體分解動畫（那些都在各章 VizScript），只負責「**辨認矩陣類別 + 跳轉**」。每個橢圓 / 分解符號 / section number 都是 pointer，把整本互動式教材編織成「**從一張地圖點任何元素跳到對應章節 + VizScript**」的網狀結構。**這是 S12+ 完成後讀者進入教材的標準入口**。

#### A. 一句話定位

把 Hiranabe 的同心橢圓全書地圖實作為互動式 dashboard，11 層橢圓 + 13 個分解符號 + 8 個 Strang section number 全部可點擊跳轉到對應章節，作為全書互動式教材的「**首頁 + 導覽中樞**」。

#### B. 學習目標（Learning Outcome）

讀者完成此互動後能夠：

1. **建立全書地圖直覺**：看到「Matrix World 一張圖」即知道全書內容架構
2. **理解類別繼承**：理解 11 層橢圓的「**外層 ⊇ 內層 = 內層 ⊂ 外層**」邏輯
3. **連結五大分解的適用範圍**：知道哪個分解屬於哪層橢圓、為什麼 SVD 在最外層
4. **使用導覽**：從任一橢圓 / 分解 / section number 跳轉到本互動式版本對應 VizScript

#### C. 整體布局（單一旗艦視窗 + 三模式切換）

- **預設模式 = Map view：** 1200×900 px 主視窗呈現完整同心橢圓地圖（與原圖類似但向量化、可縮放）；右側 200 px 圖例區顯示「分解符號 = 灰底白字、section number = 淺灰底黑字、範例矩陣 = 純文字」+ Tier 標記顏色說明
- **Hover 模式：** 滑鼠 hover 任一橢圓 / 分解 / section number 時，該元素**高亮 + 上方浮現 tooltip** 顯示「**類別名 / 數學定義 / 對應章節 / 點此跳轉**」
- **Click 模式：** 點任一可互動元素觸發「**Mini-Dashboard panel 從右側滑出**」（panel 400 px 寬）顯示：類別詳細數學定義 + 3 個範例矩陣（含特徵值即時計算）+ 三個 pointer 按鈕「→ 看 [chXX] 詳解」「→ 看相關 VizScript」「→ 看 Map of Eigenvalues」

#### D. 可調參數（拉桿 + 過濾器）

- **層級可見度（11 個 checkbox）：** 可勾選/隱藏每層橢圓（如只看 L2 Square Matrix 以下）
- **分解符號可見度（13 個 checkbox）：** 可勾選/隱藏 13 個分解標籤
- **章節 highlight 過濾器：** 下拉選單「§1 / §2 / §3 / §4 / §5 / §6.1 / ... / §6.5」— 選一個章節即高亮 Matrix World 中所有對應元素（如選 §6.5 SVD 即高亮最外層橢圓 + $A = U\Sigma V^{\mathrm{T}}$ 標籤 + 底部 $A^{+}$ 公式 + Singular 區塊）
- **範例矩陣輸入區：** 拖入或貼上自訂 $3 \times 3$ 矩陣，**自動辨認該矩陣屬於哪些層**（高亮對應橢圓） — 例：輸入對稱矩陣，從外到內高亮 Matrix → Square → Diagonalizable → Normal → Symmetric

#### E. 顏色配方（沿用全書錨點 + 旗艦特色）

- **同心橢圓邊框：** 深藍 `#1f77b4` 細線（原圖風格）
- **Hover 高亮：** 該橢圓邊框 → 加粗 + 黃金 `#FFD700`（沿用 §6.x EVD 橢球變形色）
- **跳轉按鈕：** 白底深綠邊框 `#2ca02c`（全書一致）
- **分解符號標籤：** 深灰 `#666666` 底 + 白字（原圖風格）
- **範例矩陣（拖入）對應高亮：** 多層同時高亮時，按「**外 → 內**」漸變色（最外淺藍、最內紫紅）
- **章節過濾器高亮：** 該章節對應元素加粉紅 `#d62728` 點綴標記

#### F. 動畫節奏

- **Hover 進入：** 200 ms 加粗邊框 + tooltip 淡入
- **Click 觸發 Panel：** 400 ms 右側 panel 滑入（ease-out）+ Map view 縮小到 800 px 寬
- **章節過濾器切換：** 600 ms 所有非該章節元素淡出至 30% 透明度，該章節元素閃爍 2 次後保持高亮
- **範例矩陣辨認動畫：** 800 ms「**從外到內**」依序高亮對應層橢圓（呈現「往內收斂」直覺）
- **跳轉按鈕點擊：** 200 ms fade-out Map view + 800 ms 過渡到目標 VizScript

#### G. 公式同步顯示（Mini-Dashboard panel）

- 點任一元素後 panel 顯示：
  1. **類別名 + 集合論定義**（如「Symmetric: $\{S \in \mathbb{R}^{n \times n}: S = S^{\mathrm{T}}\}$」）
  2. **範例矩陣 3 個**（小、中、大，含特徵值即時計算與屬性檢驗）
  3. **相關分解的公式**（如 Symmetric panel 顯示 $S = Q\Lambda Q^{\mathrm{T}}$）
  4. **「Strang 書對應 section」連結**（如 [section 2.4 / 6.3](ch06e-QLQ.md)）
  5. **「相關 VizScript」按鈕列表**（如 Symmetric panel 列 [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01)、[Map of Eigenvalues VizScript-01](appendix-map-eigenvalues.md#vizscript-01)）

#### H. 驗收標準

1. **所有 11 層橢圓可獨立 hover/click**，無重疊干擾（z-index 從外到內遞增）
2. **13 個分解符號全部可點擊**並正確跳轉（CR / LU / QR / $X\Lambda X^{-1}$ / $S = Q\Lambda Q^{\mathrm{T}}$ / $U\Sigma V^{\mathrm{T}}$ / $A^{+}$ / $XJX^{-1}$ 等）
3. **範例矩陣輸入辨認準確：** 至少正確辨識 8 類常見矩陣（對稱 / 反對稱 / 正交 / 投影 / 對角 / Markov / 冪零 / 一般可對角化），辨認準確率 > 95%
4. **章節過濾器：** 切換 14 個章節（§1–§5 + ch06a–f + 3 附錄）任一，對應元素高亮無遺漏
5. **跳轉準確：** 任一 pointer 按鈕跳轉到對應 VizScript 並把上下文（如輸入矩陣）帶入

#### I. 邊界與健壯性

- **小尺寸矩陣輸入：** 1×1 純數字（純拉桿）視為 Diagonal 子集；2×2 / 3×3 完整辨認；4×4+ 顯示「**矩陣較大、辨認可能耗時 < 200 ms**」 progress bar
- **數值容差：** 對稱性檢驗用 $\| S - S^{\mathrm{T}} \|_F < 10^{-6}$ 容差（避免浮點誤差）
- **退化情形：** 對全零矩陣 $O$ 直接跳到「$O$ 是最內層」說明
- **辨認失敗：** 若矩陣不屬於任一已知類別，提示「**此矩陣是『一般 Matrix』** — 從最外層開始」

#### J. 字幕 / 標題 / 圖例

- **頂部：** 「Matrix World — 全書互動式索引地圖（Hiranabe 2020 / v1.5 2023）」
- **左下：** 「點任一橢圓 / 分解符號 / section number 可跳轉」
- **右側圖例：** 圖例區固定 200 px，含「分解符號樣式 / section number 樣式 / hover 高亮樣式 / 跳轉按鈕樣式」
- **章末小字：** 「Drawn by Kenji Hiranabe, with the help of Prof. Gilbert Strang (CC-BY)」

#### K. 教學引導文案（嵌入互動視窗）

- **首次進入：** 「歡迎進入 Matrix World — 全書互動式索引地圖。**請從最外層橢圓 hover 起，沿著縱深往內探索**。每層代表一類矩陣，內層是外層的特例。點任一元素可跳到對應章節。」
- **章節過濾器觸發後：** 「您正在過濾 [§6.5 SVD] 相關元素 — 看 SVD 在 Matrix World 中的位置：**最外層橢圓（適用任意矩陣）+ 底部偽反公式**。點高亮元素跳到該 VizScript 詳細展開。」
- **範例矩陣輸入辨認後：** 「您輸入的矩陣屬於 [Symmetric] 類別 — 自外到內依序屬於：Matrix → Square → Diagonalizable → Normal → **Symmetric**。建議從 ch06e EVD 開始閱讀。」

#### L. 平台技術建議（S12+ 實作）

- **建議平台：** Marimo（反應式 notebook）+ plotly（同心橢圓可向量化縮放）+ matplotlib（高品質匯出 PNG / SVG 備用）
- **核心套件：** `plotly.graph_objects.Scatter`（橢圓 paths）、`marimo.ui.dropdown`/`checkbox`/`text_input`（過濾器 + 矩陣輸入）、`numpy.linalg.eig`（範例矩陣特徵值計算）、`scipy.linalg.norm`（對稱性容差檢驗）
- **資料結構：** 11 層橢圓 + 13 個分解符號 + 8 個 section number 共 32 個可點擊區域，全部編碼為 plotly traces 或 shapes
- **效能：** 預估 32 個 traces 渲染 < 100 ms；hover/click 互動 < 50 ms
- **匯出：** SVG 向量格式（保留印刷品質）+ 互動式 HTML（離線可用）

#### M. 延伸與替代方案

- **延伸 1（Tier 3 升級候選）：** 加入「**Matrix World 隨時間演化動畫**」 — 從最內 $\{I, O\}$ 出發，逐層展開到最外，視覺化「**矩陣分類學是如何構建的**」
- **延伸 2：** 整合 [Map of Eigenvalues](appendix-map-eigenvalues.md) — 點任一類別不只跳對應章節，也跳到 Map of Eigenvalues 同名格子看特徵值幾何位置
- **延伸 3：** 整合 [The Four Subspaces](appendix-four-subspaces.md) — 點 SVD 元素時自動展開 Strang 兩塊大餅圖（[ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) 的 SVD 整合版）
- **替代方案：** 純 HTML + D3 可實現相同 dashboard，D3 對 SVG 同心圓互動原生支援更好；但 numpy 計算特徵值 / 對稱性檢驗仍需 Python 後端

---

## 章末延伸

- **後續章節連結：** [→ § The Four Subspaces 附錄](appendix-four-subspaces.md)
- **前面章節連結：** [← § Map of Eigenvalues 附錄](appendix-map-eigenvalues.md)
- **回到主章節索引：** [→ §6 五大分解總覽](ch06a-five.md)
- **延伸閱讀：**
  - Hiranabe 原 slidedeck v1.5：<https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MatrixWorld.pdf>
  - 博客介紹：<https://anagileway.com/2020/09/29/matrix-world-in-linear-algebra-for-everyone/>
  - Strang《Linear Algebra for Everyone》第 1–7 章（Matrix World 中所有 section number 對應原書頁碼）

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 604–610（References 第 4 條，附 PDF 連結 + 圖嵌入）
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 586–592
- **原始 slidedeck：** [`MatrixWorld.pdf`](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MatrixWorld.pdf)（v1.5，Hiranabe + Strang 合作 2023-03-02 修訂）
- **作者：** Kenji Hiranabe（with help of Prof. Gilbert Strang），CC-BY 授權
- **PNG 重核（S10）：** **無 `using XX` 標記**（圖內標記是 Strang 書 section number：1.4 / 7.1 / 4.4 / 6.2 / 6.3 / 4.2 / 2.4 / 2.3 / 3.5 / 7.4 + A5 / A7，不是本書 Pattern 標記）
- **授權：** Apache 2.0
