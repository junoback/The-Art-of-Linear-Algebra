# 附錄 A：特徵值地圖（Map of Eigenvalues）

> **原書頁碼：** 英文版 References 第 3 條（p.34）/ 簡中版同
> **對應 .tex 段落：** `from-tex/en.md` 第 596–602 行（References 區）/ 完整 PDF：[`MapofEigenvalues.pdf`](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MapofEigenvalues.pdf)
> **本章圖數：** 1（`MapofEigenvalues.png`）
> **本章 VizMark 數：** 1（⭐⭐ Tier 1 + pointer 指 [ch06e EVD VizScript-01](ch06e-QLQ.md#vizscript-01)）
> **PNG `using XX` 標記：** **無**（S10 PNG 重核確認 — HANDOFF 預估「可能標 P3」推翻；附錄是「地圖層級」非 Pattern 套用層級）
> **狀態：** [x] 已完成

---

## 章節摘要

《Map of Eigenvalues》是 Kenji Hiranabe 於 2021 年獨立發布的 slidedeck，**並非《Linear Algebra for Everyone》主書內容**，而是作為「**特徵值的視覺化分類地圖**」的補充作品。它把 12 種常見矩陣類別（從零矩陣 $O$ 到 Markov 矩陣）依「**特徵值在複平面上的幾何位置**」一字排開，讓讀者「**看一張圖就能辨認矩陣類型**」。每個類別給出：（1）類別名稱與符號；（2）小型範例矩陣（3×3）；（3）特徵值的代數條件（如 $\forall \lambda = 0$、$\forall \lambda \in \mathbb{R}$）；（4）特徵值在複平面上的散點圖（橙色圓點）。本附錄是 §6.4 EVD 的「**視覺地圖總覽**」 — 把該章的「對稱矩陣特殊性 $\forall \lambda \in \mathbb{R}$」放回 12 類矩陣的全景中。互動式版本透過「**單一 dashboard 同時呈現 12 類**」+ 拉桿改範例矩陣即時看特徵值移動，讓讀者建立「**矩陣類別 ↔ 特徵值分佈**」的雙向直覺。

> ### 💡 背後觀念：「地圖」為什麼畫得出來？12 個幾何指紋的代數源頭
>
> Hiranabe 把 12 類矩陣依特徵值在複平面的位置「一字排開」 — 對稱在實軸、反對稱在虛軸、正交在單位圓、Markov 在單位圓內含 1、投影只在 $\{0, 1\}$ 兩點 ... 為什麼這些「幾何指紋」是**普遍規律**而非個別觀察？「地圖」這個視覺策略本身為什麼是可能的？背後 200 年代數源頭：
>
> - **[Q20：特徵值的「地圖」為什麼能畫得出來？](appendix-D-why.md#q20)** — 從 **Cauchy 1829 主軸定理**（對稱 → 實軸）→ Hermite 1855 → Cayley 1858 特徵多項式 + Cayley-Hamilton → Perron 1907 + **Frobenius 1912 Perron-Frobenius 定理**（Markov $\lambda = 1$ 與單位圓內）→ Schur 1909 → **Toeplitz 1918 Normal matrix** → Gershgorin 1931 disc → Hiranabe 2021 視覺集大成 共 200 年史。② 8 類矩陣特徵值幾何位置**逐一代數推導**（對稱 $\lambda = \bar\lambda$ / 反對稱 $\lambda + \bar\lambda = 0$ / 正交 $|\lambda|^2 = 1$ / 投影 $\lambda^2 = \lambda$ / 冪零 $\lambda^k = 0$ / $zI$ / 奇異 / Markov）+ 統一機制「**多項式 functional calculus**」（$p(A) = O \Rightarrow p(\lambda) = 0$）。③ **Normal matrix（$A^{\mathrm{T}}A = AA^{\mathrm{T}}$）是地圖能畫的代數源頭** + 實軸/虛軸/單位圓三條對偶曲線對應 Hermitian/skew-Hermitian/unitary（量子力學 $U = e^{-iHt/\hbar}$ 統一範例）+ 「**分類先於分解**」教學作用。
> - **[Q18：譜定理 $S = Q\Lambda Q^{\mathrm{T}}$ 為什麼對稱矩陣特徵向量自動正交？](appendix-D-why.md#q18)** — 地圖上「對稱類 → 實軸」這條曲線的**最核心代數證明**（Cauchy 1829 主軸定理 + $\lambda = \bar\lambda$ 共軛轉置推導）— Map 把這個結果視覺化為「實軸排列」，但**為什麼**它必然如此見 Q18 雙證明。
> - **[Q11：對角矩陣 $D$ 為什麼這麼特別？](appendix-D-why.md#q11)** — Map 中「對角矩陣」位於 12 類核心位置（特徵值 = 對角元素本身），擁有「**矩陣世界中的標量**」四超能力。**「對角化」的本質 = 用 $Q$ 把任意對稱矩陣轉到對角矩陣的座標** — Map 中所有矩陣分類的最簡形式都是對角。

---

## 數學要點

### 1. 12 個矩陣類別與特徵值幾何位置（核心 ⭐）

> **數學物件：** 矩陣 $A \in \mathbb{R}^{n \times n}$（方陣）的**特徵值** $\lambda$ 滿足 $\det(A - \lambda I) = 0$。一般情況下 $\lambda \in \mathbb{C}$（含複數）。Hiranabe 把 12 種「結構化矩陣」依特徵值在**複平面**的分佈集中呈現。
>
> **記號：**
> - 橫軸 = $\mathrm{Re}(\lambda)$（實部）
> - 縱軸 = $\mathrm{Im}(\lambda)$（虛部）
> - 橙色實心圓點 = 每個特徵值的位置

| 矩陣類別 | 符號 / 定義 | 範例（$3 \times 3$）| 特徵值代數條件 | 幾何位置 |
|---|---|---|---|---|
| **零矩陣** | $O$（所有元素 0） | $\bigl[\begin{smallmatrix}0&0&0\\0&0&0\\0&0&0\end{smallmatrix}\bigr]$ | $\forall \lambda = 0$ | 原點 0 重根 |
| **單位矩陣** | $I$（對角全 1） | $\bigl[\begin{smallmatrix}1&0&0\\0&1&0\\0&0&1\end{smallmatrix}\bigr]$ | $\forall \lambda = 1$ | 實軸 1 重根 |
| **投影矩陣** | $P = P^2 = P^{\mathrm{T}}$ | $\bigl[\begin{smallmatrix}1&0&1\\0&1&0\\0&0&0\end{smallmatrix}\bigr]$（注：此例只是示意，真實投影需 $P = P^2$）| $\forall \lambda = 0 \text{ or } 1$ | 實軸 {0, 1} 兩點 |
| **冪零矩陣** | $N$，$\exists k: N^k = O$ | $\bigl[\begin{smallmatrix}0&1&1\\0&0&1\\0&0&0\end{smallmatrix}\bigr]$ | $\forall \lambda = 0$ | 原點重根（但 $N \neq O$）|
| **$zI$（標量倍單位）**| $zI$（對角 $z$）| $\bigl[\begin{smallmatrix}z&0&0\\0&z&0\\0&0&z\end{smallmatrix}\bigr]$ | $\forall \lambda = z$ | 複平面任意點 $z$ 處 |
| **可逆矩陣** | Invertible（$\det A \neq 0$）| 一般密度矩陣 | $\forall \lambda \neq 0$ | 整個複平面**除原點**（散佈）|
| **對稱矩陣** | $S = S^{\mathrm{T}}$ | $\bigl[\begin{smallmatrix}1&2&2\\2&0&1\\2&1&0\end{smallmatrix}\bigr]$ | $\forall \lambda \in \mathbb{R}$ | **實軸上**任意位置 |
| **對稱正定** | $S_+ = S^{\mathrm{T}}, \mathbf{x}^{\mathrm{T}} S \mathbf{x} > 0$ | $\bigl[\begin{smallmatrix}2&0&1\\0&1&0\\1&0&1\end{smallmatrix}\bigr]$ | $\forall \lambda > 0$ | **實軸正半軸** |
| **反對稱矩陣** | $A = -A^{\mathrm{T}}$ | $\bigl[\begin{smallmatrix}0&1&0\\-1&0&1\\0&-1&0\end{smallmatrix}\bigr]$ | $\forall \lambda \in i\mathbb{R}$（純虛數）| **虛軸上**（含原點）|
| **正交矩陣** | $Q$，$Q^{\mathrm{T}}Q = I$ | $\bigl[\begin{smallmatrix}0&1&0\\-1&0&0\\0&0&1\end{smallmatrix}\bigr]$ | $\forall \| \lambda \| = 1$ | **單位圓**上 |
| **Markov 矩陣** | 行和 = 1，$A_{ij} \geq 0$ | $\bigl[\begin{smallmatrix}0&0.2&0.9\\0.9&0&0\\0.1&0.8&0.1\end{smallmatrix}\bigr]$ | $\exists \lambda = 1$，其他 $\| \lambda \| \leq 1$ | **單位圓內**（含圓上 $\lambda=1$）|
| **奇異矩陣** | $\det A = 0$ | 任意 rank-deficient | $\exists \lambda = 0$ | 複平面散佈，**必含原點** |

### 2. 對應 §6.4 EVD 的視覺意義

> Map of Eigenvalues 是 §6.4 EVD（$S = Q \Lambda Q^{\mathrm{T}}$）的「**前置全景**」。EVD 是「**對稱矩陣**」這一**單一類別**的詳細分解 — 而 Map 把這個類別放回 12 個類別的視覺地圖中，讓讀者「**先看到所有可能**，再聚焦對稱**」。

**三層遞進關係：**

1. **Map of Eigenvalues**（本附錄）：12 類全景，每類特徵值在複平面的「位置指紋」
2. **§6.4 EVD**（[ch06e](ch06e-QLQ.md)）：對稱類的詳細分解 $S = Q \Lambda Q^{\mathrm{T}}$，$\Lambda$ 對角元 = 實軸特徵值
3. **§6.5 SVD**（[ch06f](ch06f-USV.md)）：把 EVD 推廣到任意矩陣，奇異值 $\sigma \geq 0$（**實軸正半軸**，類比 Map 中「Positive Definite」位置）

### 3. 與 §5 (P4) 三明治結構的連結

> EVD/SVD 的 (P4) 三明治結構 $S = Q \Lambda Q^{\mathrm{T}}$ 與 $A = U \Sigma V^{\mathrm{T}}$ 都以「**對角矩陣**」為核心。Map of Eigenvalues 中：
>
> - **對角矩陣**（$D$，藍點對角）的特徵值是「**對角元素本身**」 — 因為 $\det(D - \lambda I) = \prod(d_p - \lambda)$
> - 因此「**對角化**」的本質是「**用 $Q$ 把任意對稱矩陣轉到對角矩陣的座標**」 — Map 中對角矩陣是「**所有矩陣類別的最簡形式**」

### 4. 三類特殊矩陣的幾何指紋（深入觀察）

| 矩陣類別 | 幾何指紋 | 為什麼？ |
|---|---|---|
| **對稱** ($S$) | 特徵值全在實軸 | $S^{\mathrm{T}}S = S^2$ 對稱保證 $\lambda$ 實數（譜定理）|
| **反對稱** ($A = -A^{\mathrm{T}}$) | 特徵值全在虛軸 | $A^{\mathrm{T}} = -A$ 導致 $\lambda + \bar\lambda = 0$ |
| **正交** ($Q^{\mathrm{T}}Q = I$) | 特徵值全在單位圓 | 範數保持 $\| Q\mathbf{x} \| = \| \mathbf{x} \|$ 導致 $\| \lambda \| = 1$ |

這三類矩陣構成了「**Normal matrices**」（$A^{\mathrm{T}}A = AA^{\mathrm{T}}$）的三個核心子集 — 詳見 [Matrix World 附錄](appendix-matrix-world.md) 的同心橢圓地圖（Symmetric ⊂ Normal ⊂ Square ⊂ Matrix）。

---

## 圖片詳細描述（Figure Description）

### Figure A.1: 特徵值地圖（Map of Eigenvalues）— 無 `using` 標記

**圖檔：** `docs/book/figs-png/MapofEigenvalues.png`（原始 PDF：`MapofEigenvalues.pdf`）
**原書頁碼：** Slidedeck 獨立發布（References 第 3 條）
**所屬章節：** 附錄 A

#### 視覺結構 (Visual Structure)

整體**2 列 × 6 行**網格，每格是一個矩陣類別的迷你 dashboard：

- **每格的元素：**
  - 左上：類別名稱（粗體大字，如 $O$、$I$、$P$、$N$、$zI$、$S$、$S_+$、$Q$、Markov）
  - 右側：3×3 範例矩陣（方括號包），文字小但清晰
  - 中央：**複平面散點圖**，橫軸 = 實部、縱軸 = 虛部，原點標 0（或對應的座標 1）
  - **特徵值用橙色實心圓點呈現**，重疊處用「堆疊圓圈」表達重根
  - 下方：類別描述文字（如「$P = P^2 = P^{\mathrm{T}}$」、「$\forall \lambda = 0$ or $1$」）

- **第 1 列**（6 個）：$O$（Zero）→ $I$（Identity）→ $P$（Projection）→ $N$（Nilpotent）→ $zI$（z times Identity）→ Invertible（最右獨立大色塊，特徵值散佈整個複平面除原點）

- **第 2 列**（6 個）：$S$（Symmetric，實軸線排列）→ $S_+$（Positive definite，實軸正半部分）→ Anti-symmetric（純虛軸排列）→ $Q$（Orthogonal，單位圓上分佈）→ Markov（單位圓內含 1）→ Singular（最右大色塊，特徵值散佈含原點）

- **整體色調：** 背景純白、外框深藍細線、特徵值橙色實心圓、文字深藍中等粗體 — 風格極簡，目標是「**12 格並列一眼看完**」

- **視覺引導：** 讀者先從**整體網格**辨認結構（2 列 × 6 行），然後**每格獨立讀**（先看名稱 → 看複平面位置 → 看代數條件），最後**橫向對照**（例如：對稱 vs 反對稱 vs 正交三個對偶類別）

#### 數學內容 (Mathematical Content)

$$
A \in \mathbb{R}^{n \times n}, \quad \lambda \in \mathbb{C}, \quad \det(A - \lambda I) = 0
$$

**12 類矩陣的代數條件與幾何位置整理：**

$$
\begin{array}{lll}
\text{Zero }(O) & : & \forall \lambda = 0 \\
\text{Identity }(I) & : & \forall \lambda = 1 \\
\text{Projection }(P=P^2=P^{\mathrm{T}}) & : & \forall \lambda \in \{0, 1\} \\
\text{Nilpotent }(N^k = O) & : & \forall \lambda = 0 \quad (\text{但 } N \neq O)\\
zI & : & \forall \lambda = z \quad (z \in \mathbb{C}) \\
\text{Invertible }(\det A \neq 0) & : & \forall \lambda \neq 0 \\
\text{Symmetric }(S = S^{\mathrm{T}}) & : & \forall \lambda \in \mathbb{R} \\
\text{Positive Definite }(S_+) & : & \forall \lambda > 0 \\
\text{Anti-symmetric }(A = -A^{\mathrm{T}}) & : & \forall \lambda \in i\mathbb{R} \\
\text{Orthogonal }(Q^{\mathrm{T}}Q = I) & : & \forall |\lambda| = 1 \\
\text{Markov }(\mathbf{1}^{\mathrm{T}} A = \mathbf{1}^{\mathrm{T}}) & : & \exists \lambda = 1,\ \text{其他 } |\lambda| \leq 1 \\
\text{Singular }(\det A = 0) & : & \exists \lambda = 0
\end{array}
$$

#### 直覺解讀 (Intuition)

這張圖是「**特徵值的視覺百科**」 — 12 個常見矩陣類別並列，讓讀者建立「**矩陣類別 ↔ 特徵值位置**」的雙向直覺。**最重要的三條洞察：**

**洞察 1：對稱 = 實軸、反對稱 = 虛軸、正交 = 單位圓** — 這三類「**結構化矩陣**」對應**三條幾何曲線**（實軸 / 虛軸 / 單位圓），形成「**Normal matrices 的三大代表**」。§6.4 EVD 是「對稱 = 實軸」這一條的詳細展開。

**洞察 2：投影矩陣的特徵值只能是 0 或 1** — 因為 $P^2 = P$ 蘊含 $\lambda^2 = \lambda$，所以 $\lambda \in \{0, 1\}$。這個性質在 §5 (P3) 動態系統章與 §6.4 EVD 投影矩陣 $P_p$ 三性質都會用到（[ch05 VizScript-03](ch05-patterns.md#vizscript-03)）。

**洞察 3：Markov 矩陣必有 $\lambda = 1$，其他都在單位圓內** — 這是「**穩定態存在性定理**」的視覺呈現。Markov 鏈的長期行為由 $\lambda = 1$ 的特徵向量主導（如 Google PageRank、人口流動模型）。**Markov 矩陣是 §5 (P3) 動態系統的核心應用**。

**常見誤解：**

- **「冪零 $N$ 與零矩陣 $O$ 都有 $\forall \lambda = 0$，是否相同？」** 不同！$O$ 是「**對角化的 0 矩陣**」（$Q\Lambda Q^{\mathrm{T}}, \Lambda = O$），$N$ 是「**不可對角化的 0 特徵值**」（Jordan 塊內部有 1）。Map 用「$O$ 重疊圓點」vs「$N$ 偏移圓點」隱晦表達這個差異。
- **「Anti-symmetric 特徵值都是純虛數，那 0 算嗎？」** 算！0 = $i \cdot 0$ 屬於 $i\mathbb{R}$。**奇數階反對稱矩陣必有 $\lambda = 0$**（因 $\det A = \det(-A^{\mathrm{T}}) = (-1)^n \det A$）。

**對比另一種看法（Matrix World 同心橢圓地圖）：**

- **Map of Eigenvalues** 用「**並列網格**」看特徵值位置 — 適合「**分類辨識**」
- **Matrix World**（見 [appendix-matrix-world.md](appendix-matrix-world.md)）用「**同心橢圓**」看類別包含關係 — 適合「**理解誰是誰的特例**」

兩個附錄是「**同一矩陣分類問題的對偶視覺化**」 — 一個從「**特徵值幾何**」切入，一個從「**矩陣性質繼承關係**」切入。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [動態切換 + 拉桿] ⭐⭐ Tier 1 + pointer
> **位置：** Figure A.1 / 附錄 A 整圖
> **核心概念：** 12 矩陣類別 ↔ 特徵值幾何位置雙向辨認
> **互動梗概：** 12 格 dashboard 並列；點任一格放大顯示，可拉桿調整該類別範例矩陣的某些參數（如 $zI$ 拉動 $z$ 看橙點移動 / 對稱矩陣調整 $S$ 元素看特徵值在實軸滑動 / Markov 改機率看圓內分佈變化）；點任一格的「→ 看 EVD 詳解」跳轉到 [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01)（對稱類詳細展開），點「→ 看 P4 三明治」跳轉到 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)（投影矩陣 $P_p$ 三性質）
> **詳見劇本：** VizScript-01（章末）

---

## 視覺化劇本（VizScripts）

### VizScript-01: 特徵值地圖互動式 dashboard（Map of Eigenvalues Interactive）

**Tier：** ⭐⭐ Tier 1 + pointer（12 格 dashboard 控制器，每格特徵值動畫獨立但結構共用；對稱類詳細展開 pointer 到 ch06e）
**對應 VizMark：** Figure A.1 / VizMark-01

> 本劇本只負責**12 格網格切換 + 單格特徵值即時計算 + 跨類別參數對比**，對稱類的「$Q\Lambda Q^{\mathrm{T}}$ 詳細展開 + 橢球主軸對齊」全部不重複實作 — 透過按鈕「→ 看對稱類 EVD 詳解」跳轉到 [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01)。投影矩陣的「$P_p$ 三性質視覺驗證」也透過按鈕「→ 看 P4 三明治」跳轉到 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)。

#### A. 一句話定位

把 12 個矩陣類別並列為互動式 dashboard，每格可獨立調整範例參數即時看特徵值在複平面上移動，讓讀者建立「**矩陣類別 ↔ 特徵值幾何位置**」的雙向直覺，並從 dashboard 點按鈕跳轉到 §6.4 EVD 的詳細展開。

#### B. 學習目標（Learning Outcome）

讀者完成此互動後能夠：

1. **辨認 12 類矩陣**：看到任意 3×3 矩陣，能依特徵值位置（實軸 / 虛軸 / 單位圓 / 原點 / 散佈）回推矩陣類別
2. **建立對偶直覺**：理解對稱（實軸）↔ 反對稱（虛軸）↔ 正交（單位圓）三類的對稱關係
3. **連結 §6.4 EVD**：理解 EVD 的本質是「對稱類」的詳細分解，整個 Map 是 EVD 的「全景前置」
4. **理解 Markov 應用**：認識 Markov 矩陣 $\lambda = 1$ 對應穩定態的視覺直覺

#### C. 整體布局（2 模式：grid view + zoom view）

- **Grid view（預設）：** 2 列 × 6 行 = 12 格，每格固定 240×180 px 含「類別名 + 縮小矩陣 + 迷你複平面」；hover 該格上方顯示「→ 點此放大互動」
- **Zoom view（點任一格觸發）：** 該格放大為 800×600 px 主視窗 + 左側 200 px 拉桿區（調整範例參數）+ 上方 60 px 按鈕區（含「← 回 Grid」、「→ 看 EVD 詳解」、「→ 看 P4 三明治」等 pointer 按鈕）

#### D. 可調參數（拉桿）

每類別拉桿不同，舉典型代表：

- **$zI$ 類：** 拉桿 $z = a + bi$（$a, b \in [-3, 3]$ 步進 0.1），即時看橙點在複平面移動
- **對稱類 $S$：** 拉桿 6 個獨立參數 $s_{11}, s_{22}, s_{33}, s_{12}, s_{13}, s_{23} \in [-9, 9]$ 步進 1，特徵值在實軸滑動
- **正交類 $Q$（2×2 簡化）：** 拉桿旋轉角 $\theta \in [0, 2\pi]$，特徵值在單位圓上對稱移動
- **Markov 類：** 拉桿 9 個機率參數 $p_{ij} \geq 0$ 且每行和 = 1（用 softmax 強制歸一），主特徵值固定在 $\lambda = 1$，其他特徵值在單位圓內移動

#### E. 顏色配方（沿用全書錨點）

- **特徵值橙點 `#ff7f0e`**：所有類別共用，實心圓直徑 12 px
- **複平面背景**：純白 + 灰格線 `#cccccc` 步進 0.5、原點與單位圓藍細線 `#1f77b4`
- **類別名標籤**：深藍 `#1f77b4` 粗體
- **跳轉按鈕**：白底深綠邊框 `#2ca02c`，hover 填色深綠

#### F. 動畫節奏

- **Grid view → Zoom view 切換：** 該格放大 600ms 緩動 ease-in-out，其他 11 格淡出 300ms
- **拉桿即時更新：** 每次值改變，特徵值橙點以 200ms 平滑移動到新位置（matplotlib `FuncAnimation` 或 plotly transition）
- **Markov 機率歸一動畫：** 拉桿後 softmax 後 400ms 顯示「機率箭頭」表達向歸一收斂

#### G. 公式同步顯示

- **Zoom view 右側顯示：**
  1. 當前矩陣 $A$（$3 \times 3$，數值即時更新）
  2. 特徵多項式 $\det(A - \lambda I)$（展開後的多項式）
  3. 特徵值 $\lambda_1, \lambda_2, \lambda_3$（複數形式，含 Re/Im 兩部分）
  4. 類別代數條件對照（如「目前 $S = S^{\mathrm{T}}$? ✓」即時驗證）

#### H. 驗收標準

1. **拉桿同步性：** 任一拉桿改變後，矩陣 / 多項式 / 特徵值 / 散點位置應 < 300ms 完成同步
2. **跨類別對比：** Grid view 12 格中至少 3 對「對偶類」（對稱 vs 反對稱 / 投影 vs 冪零 / Markov vs Singular）視覺差異一眼可辨
3. **跳轉準確：** 「→ 看 EVD 詳解」按鈕跳轉到 ch06e VizScript-01 並把當前對稱矩陣 $S$ 帶入作為 EVD 範例輸入
4. **常數類別處理：** $O$、$I$ 兩類無拉桿（特徵值固定），只顯示說明文字「特徵值為常數，無互動」

#### I. 邊界與健壯性

- **矩陣對稱性檢查：** 對稱類拉桿改變後自動 enforce $S_{ij} = S_{ji}$
- **正交性檢查：** 正交類用「先參數化（旋轉角 / Givens 角）→ 構造 $Q$」避免讀者拉到非正交狀態
- **Markov 行和檢查：** 每次拉桿後重新 softmax，但顯示「正規化前的原始機率」供使用者直覺輸入
- **退化特徵值警告：** 多重特徵值（如 $\lambda_1 = \lambda_2$）用紫色高亮，提示「重根 / 可能不可對角化」（連結 ch06e § 對稱矩陣特殊性）

#### J. 字幕 / 標題 / 圖例

- **Grid view 頂部：** 「特徵值地圖：12 個矩陣類別的視覺百科」
- **Zoom view 頂部：** 「[類別名]：拉桿即時看特徵值移動」
- **底部圖例：** 「橙點 = 特徵值在複平面位置」「藍圓 = 單位圓」「灰格 = 0.5 步進複平面」

#### K. 教學引導文案（嵌入互動視窗）

- **Grid view 初次進入：** 「12 格並列特徵值地圖。點任一格放大互動。試從『**對稱類**』開始，看實軸上 3 個橙點隨拉桿滑動。」
- **Zoom view 進入後：** 「現在看到的是 [類別名]。拉桿改變範例矩陣，注意特徵值如何在 [實軸 / 虛軸 / 單位圓 / ...] 上移動。再點頂端按鈕『→ 看 EVD 詳解』看對稱矩陣的完整分解。」

#### L. 平台技術建議（S12+ 實作）

- **建議平台：** Marimo（反應式 notebook）+ plotly（複平面散點動畫流暢度高）
- **核心套件：** `numpy.linalg.eig`（計算特徵值，含複數）、`plotly.graph_objects.Scatter`（橙點）、`marimo.ui.slider`（拉桿群）、`marimo.ui.button`（跳轉按鈕）
- **資料流：** 拉桿 → 矩陣 → `np.linalg.eig` → 特徵值 → plotly scatter update
- **效能：** 12 格 grid view 不需即時計算（預先計算範例固定值），只 Zoom view 觸發即時計算（每次拉桿 < 5ms）

#### M. 延伸與替代方案

- **延伸 1：** Tier 2 升級 — 增加「4×4 / 5×5 矩陣支援」（部分類別需更多參數）
- **延伸 2：** Tier 3 候選 — 整合 [Matrix World](appendix-matrix-world.md) 同心橢圓地圖，讓使用者點 Matrix World 任一圈層 → 自動跳到 Map of Eigenvalues 對應格
- **替代方案：** 純 HTML + D3 可實現相同 dashboard，但 D3 需手寫複數計算（不如 numpy 方便）

---

## 章末延伸

- **後續章節連結：** [→ § Matrix World 附錄](appendix-matrix-world.md)
- **回到主章節：** [→ §6.4 EVD（對稱類詳細展開）](ch06e-QLQ.md) / [→ §6.5 SVD（推廣到任意矩陣）](ch06f-USV.md)
- **延伸閱讀：**
  - Hiranabe 原 slidedeck：<https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MapofEigenvalues.pdf>
  - 博客介紹：<https://anagileway.com/2021/10/01/map-of-eigenvalues/>
  - Strang《Linear Algebra for Everyone》第 7 章「Eigenvalues and Eigenvectors」

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 596–602（References 第 3 條，附 PDF 連結）
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 578–584
- **原始 slidedeck：** [`MapofEigenvalues.pdf`](https://github.com/kenjihiranabe/The-Art-of-Linear-Algebra/blob/main/MapofEigenvalues.pdf)（v1.x，Kenji Hiranabe 2021 獨立發布）
- **作者：** Kenji Hiranabe（[twitter @hiranabe](https://twitter.com/hiranabe)，<https://anagileway.com>）
- **PNG 重核（S10）：** **無 `using XX` 標記**（HANDOFF 預估「可能標 P3」推翻；附錄是「地圖層級」非 Pattern 套用層級）
- **授權：** Apache 2.0
