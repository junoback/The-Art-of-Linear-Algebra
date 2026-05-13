# 6.5 矩陣分解 5：$A = U \Sigma V^{\mathrm{T}}$（Singular Value Decomposition / SVD）

> **原書頁碼：** p.12–p.13
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.5 $A = U\Sigma V^{\mathrm{T}}$（en.md line 507–569 / zh.md line 494–558）
> **本章圖數：** 1（`SVD.png`，原書圖中明標 **using P4**）
> **本章 VizMark 數：** 4（⭐⭐⭐ × 1 Tier 3 / ⭐⭐⭐ × 1 Tier 2 / ⭐⭐ × 1 / ⭐ × 1）— **全書 VizMark 密度最高的章節**
> **狀態：** [x] 已完成（S09，全書最長章節 + 唯一 Tier 3 主 VizScript）

---

## 章節摘要

$A = U \Sigma V^{\mathrm{T}}$ 是 §6 五大分解的**最後一個**，也是**最重要的一個**。它是書中 Hiranabe 多次強調「**MM4 的旗艦應用**」（見 ch04 VizScript-02 母模板），也是 Strang「**Linear Algebra for Everyone**」全書的**封頂定理**（Sec. 7.1 Singular Values and Singular Vectors）。SVD 的三大特殊地位：

1. **唯一適用「任意 $m \times n$ 矩陣」的分解** — 不需方陣、不需對稱、不需正定、不需可逆、不需列獨立。**SVD 對所有矩陣都存在且唯一**（給定奇異值降冪排序後）；
2. **「最佳低秩近似定理（Eckart–Young）」的實作工具** — 取前 $k$ 個秩 1 項 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 累加，就是「在 Frobenius / 譜範數意義下最接近 $A$ 的秩 $k$ 矩陣」；
3. **「四子空間」的完美對齊工具** — $\mathbf{u}, \mathbf{v}$ 同時給出列空間 / 行空間 / 零空間 / 左零空間的正交基底（Strang 的經典「兩塊大餅」圖直接由 SVD 構造）。

**SVD 在工程實務中的「四大旗艦應用」：**

| 應用 | 用途 | SVD 角色 |
|---|---|---|
| **影像 / 資料壓縮** | 用秩 $k$ 近似節省儲存 | 取前 $k$ 個 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$，誤差由 $\sigma_{k+1}$ 控制 |
| **PCA（主成分分析）** | 降維 + 找主要變化方向 | 對置中資料 $X$ 做 SVD，$V$ 的列 = 主成分方向，$\sigma_p^2/N$ = 主成分變異 |
| **降噪 / 去模糊** | 移除小奇異值（雜訊）| 截斷 $\sigma_p < \tau$ 後重組 = 低通濾波 |
| **推薦系統 / 矩陣補全** | 用低秩結構填補缺失 | 用戶 × 產品評分矩陣的 SVD 找潛在因子（Latent Factor Model）|

**`using P4` 標記的意義（S09 PNG 重核發現）：** 原書 `SVD.png` 右下角圓圈標 `P4`（**S09 重大發現，與 EVD 同款**），明示「SVD 圖的視覺視角是 §5 Pattern 4 三明治」— 這跟 §6.4 EVD 標的也是 `using P4` 完全一致。**SVD 是 (P4) 的最一般情境** — 左側 $U$ 與右側 $V^{\mathrm{T}}$ **不同的兩個正交矩陣**（不像 EVD 強制相同），中間 $\Sigma$ 對角是非負的奇異值（不像 EVD 的特徵值可正可負）。

**本章 VizScript 策略（雙 pointer 設計，本章特例）：** 雖然 SVD PNG 標 `using P4`（按 S08 規律應單 pointer 指 ch05 P4），但 SVD 與 ch04 VizScript-02 (MM4 + Mona Lisa SVD demo) **本質同根** — 「秩 1 累加 + 低秩近似」這個視覺概念在 ch04 已實作 Mona Lisa demo，SVD 章直接是 Mona Lisa demo 的「**理論完整版**」。因此本章 VizScript-01 採**雙 pointer**：
- **主 pointer：** [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)（看 (MM4) 秩 1 累加 + Mona Lisa SVD demo 的母模板）
- **副 pointer：** [ch05 VizScript-03](ch05-patterns.md#vizscript-03)（看 (P4) 三明治結構）

**雙 pointer 復活的判準（S09 修正 SOP §2.6 規律）：** 不只看 PNG 標記（`using XX`），也看「**內容鐵證**」 — 當該章核心 demo 與另一章已實作的旗艦 demo 同根時，可破例升級雙 pointer。**SVD 是這個判準的首例 + 全書最強烈的例子**（Mona Lisa SVD demo 就是為了 SVD 而提前在 ch04 鋪陳的）。

**對比 EVD（§6.4）— SVD 與 EVD 的關係：**

| 性質 | $S = Q\Lambda Q^{\mathrm{T}}$（EVD）| $A = U\Sigma V^{\mathrm{T}}$（SVD）|
|---|---|---|
| 矩陣限制 | 必須對稱 $S = S^{\mathrm{T}}$ | **任意 $m \times n$**（無限制）|
| 形狀 | $n \times n$ 方陣 | $m \times n$ **可長方** |
| 左側 | 正交 $Q$（$n \times n$）| 正交 $U$（$m \times m$ 或 $m \times r$）|
| 中間 | 對角 $\Lambda$（特徵值 $\lambda_p \in \mathbb{R}$）| 對角 $\Sigma$（奇異值 $\sigma_p \geq 0$）|
| 右側 | 正交 $Q^{\mathrm{T}}$（**= 左側轉置**）| 正交 $V^{\mathrm{T}}$（**與 $U$ 不同**）|
| 對角元素符號 | $\lambda_p$ 可正可負可零 | $\sigma_p$ **強制非負** |
| 與 (MM4) 連結 | $\sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$（自外積）| $\sum \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$（**一般外積**）|
| `using` 標記 | EVD 標 (P4) | SVD 標 (P4) |
| 求 $A^{-1}$ | $Q \Lambda^{-1} Q^{\mathrm{T}}$ | $V \Sigma^{-1} U^{\mathrm{T}}$（**或** Moore–Penrose 偽反 $V \Sigma^+ U^{\mathrm{T}}$）|
| 唯一性 | $\lambda_p$ 唯一（重根除外） | $\sigma_p$ 唯一（重根除外）|

**核心升級點：** 從 EVD 升級到 SVD = **解除「對稱」限制 + 把右側 $Q^{\mathrm{T}}$ 解放成獨立的 $V^{\mathrm{T}}$ + 把 $\Lambda$（可負）改成 $\Sigma$（非負）**。這是「**雙側獨立正交化的對角分解**」 — 任何矩陣都可以這樣分解。

**EVD 與 SVD 的橋梁公式（核心定理）：** 對任意 $A$：

$$
\boxed{
A^{\mathrm{T}} A = V \Sigma^{\mathrm{T}} \Sigma V^{\mathrm{T}} = V \Sigma^2 V^{\mathrm{T}}, \qquad
A A^{\mathrm{T}} = U \Sigma \Sigma^{\mathrm{T}} U^{\mathrm{T}} = U \Sigma^2 U^{\mathrm{T}}
}
$$

— 即 **$A^{\mathrm{T}} A$ 的 EVD 給出 $V$ 和 $\Sigma^2$；$AA^{\mathrm{T}}$ 的 EVD 給出 $U$ 和同樣的 $\Sigma^2$**。這就是「**SVD = 兩個對稱矩陣的 EVD 整合**」的精準描述。

數值範例（本章主貫穿，2×2 對稱版讓 SVD 退化成 EVD，方便對照 §6.4）：

$$
A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} = U \Sigma V^{\mathrm{T}}
\;=\;
\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
\begin{bmatrix} 3 & 0 \\ 0 & 1 \end{bmatrix}
\dfrac{1}{\sqrt{2}}\begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}
$$

**驗證（對稱 $A$ 時 SVD = EVD）：** $U = V = Q$（同一個正交矩陣），$\Sigma = |\Lambda|$（取絕對值；本例 $\lambda = 3, 1$ 都正所以 $\Sigma = \Lambda$）。**這展示「對稱情境是 SVD 的特例」。**

第二範例（不對稱 2×2，展示 $U \neq V$）：

$$
A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}
$$

$$
A^{\mathrm{T}} A = \begin{bmatrix} 25 & 20 \\ 20 & 25 \end{bmatrix}
$$

特徵值 $\lambda = 45, 5$，所以 $\sigma_1 = \sqrt{45} = 3\sqrt{5} \approx 6.708$，$\sigma_2 = \sqrt{5} \approx 2.236$。$V$ 由 $A^{\mathrm{T}} A$ 的特徵向量組成、$U$ 由 $A A^{\mathrm{T}}$ 的特徵向量組成（或用 $\mathbf{u}_p = A \mathbf{v}_p / \sigma_p$）。**$U \neq V$**（因為 $A$ 不對稱）。

第三範例（長方 3×2，展示「reduced SVD」的形狀）：

$$
A = \begin{bmatrix} 1 & 1 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}_{3 \times 2}
$$

$$
A^{\mathrm{T}} A = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}_{2 \times 2}, \quad \lambda = 3, 1, \quad \sigma_1 = \sqrt{3}, \sigma_2 = 1
$$

Reduced SVD：$U \in \mathbb{R}^{3 \times 2}$、$\Sigma \in \mathbb{R}^{2 \times 2}$、$V^{\mathrm{T}} \in \mathbb{R}^{2 \times 2}$。**只有 $r = \operatorname{rank}(A) = 2$ 項非零秩 1 之和**：

$$
A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}} + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^{\mathrm{T}}
$$

— 這是 SVD.png 直接展示的形式。

> ### 💡 背後觀念：SVD 為什麼是「線代之冠」？為什麼對任意矩陣都存在？
>
> $A = U\Sigma V^{\mathrm{T}}$ 是 §6 五大分解的**壓軸** — 它對**任意** $m \times n$ 矩陣都存在，不要求方陣、不要求對稱、不要求滿秩、不要求可逆。對比 EVD 只對「可對角化方陣」存在、CR / LU / QR 都有額外限制，SVD 為什麼能突破所有限制？為什麼 Strang 稱它為「**the most important theorem in linear algebra**」？4 條設計動機問題：
>
> - **[Q19：SVD 為什麼對任何矩陣都存在？](appendix-D-why.md#q19)** — SVD 是線代生命力最持久的單一概念：**Beltrami 1873** 首次發現（雙線性形式對角化）→ Jordan 1874 變分定義 → Sylvester 1889 矩陣語言 → Schmidt 1907 無限維 + 低秩近似觀察 → **Eckart-Young 1936 最佳低秩近似定理**（資料科學基石）→ Golub-Kahan 1965 第一實用演算法 → 1990s+ ML 核心工具。雙證明路徑：① 透過 $A^{\mathrm{T}}A$ 譜定理（$A^{\mathrm{T}}A$ 對稱半正定**普世構造** + Q18 譜定理**普世定理** → SVD **普世存在**）+ ② Jordan 1874 變分定義 $\sigma_1 = \max \|A\mathbf{x}\|$。3 大突破：不需方陣 / 不需可對角化 / 奇異值永遠非負實。
> - **[Q14：為什麼要把矩陣「分解」？](appendix-D-why.md#q14)** — SVD 是唯一**同時對應所有 6 大工程動機**的分解：求解（$\mathbf{x}^{*} = A^{+}\mathbf{b}$ 最小範數最佳解）/ 求冪 / 求反（偽反 $A^{+}$ 對任意矩陣存在）/ 穩定性（奇異值 = 條件數）/ 壓縮（Eckart-Young 截斷）/ 結構理解（4 子空間正交基底）— **一個分解，看清所有**。這就是為什麼 Strang 在 LAFE Ch.7 用整章寫 SVD 並稱它為「**the most important theorem in linear algebra**」。
> - **[Q08：四個基本子空間為什麼會自然冒出？](appendix-D-why.md#q08)** — SVD **自動給出** 4 子空間的正交基底：$U_r$ = 列空間 $\mathbf{C}(A)$、$U_0$ = 左零空間 $\mathbf{N}(A^{\mathrm{T}})$、$V_r$ = 行空間 $\mathbf{C}(A^{\mathrm{T}})$、$V_0$ = 零空間 $\mathbf{N}(A)$ — Strang 經典「兩塊大餅」圖直接由 SVD 構造。
> - **[Q13：(P4) 三明治為什麼線代核心？](appendix-D-why.md#q13)** — SVD 是 (P4) 三明治的**最強形式**（兩基底分開 $U \ne V$、適用任意矩陣），是「**視角切換 → 純對角縮放 → 視角切換回來**」這個哲學的**最一般實現**。EVD 是「兩基底合一」的完美三明治、SVD 是「兩基底分開」的最強三明治 — 兩者構成 §6 (P4) 譜系的雙頂峰。

---

## 數學要點

### 1. 定義與形狀（Full SVD vs Reduced SVD）

**Full SVD（完整版）：**

$$
A_{m \times n} = U_{m \times m} \, \Sigma_{m \times n} \, V^{\mathrm{T}}_{n \times n}
$$

- $U$：$m \times m$ 正交方陣，列為「左奇異向量」 $\mathbf{u}_1, \ldots, \mathbf{u}_m$；
- $\Sigma$：$m \times n$ 「**長方對角**」矩陣，對角元素為奇異值 $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_{\min(m,n)} \geq 0$，**非對角元素全為零**；
- $V$：$n \times n$ 正交方陣，列為「右奇異向量」 $\mathbf{v}_1, \ldots, \mathbf{v}_n$；
- $V^{\mathrm{T}}$：行為 $\mathbf{v}_p^{\mathrm{T}}$。

**Reduced SVD（簡化版，原書圖示用此）：**

$$
A_{m \times n} = U_{m \times r} \, \Sigma_{r \times r} \, V^{\mathrm{T}}_{r \times n}, \qquad r = \operatorname{rank}(A)
$$

- 只取「**非零奇異值對應的部分**」 — 對應的 $\mathbf{u}_p, \mathbf{v}_p$；
- 等價於 $A = \sum_{p=1}^{r} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$；
- **書中 SVD.png 是 reduced SVD**（看圖中 $U$ 是 3 列、$\Sigma$ 是 2 個藍點 = 2 個非零 $\sigma$、$V^{\mathrm{T}}$ 是 2 行）。

**選哪個？** 工程實務通常用 **reduced SVD**（節省記憶體、對應「秩 $r$ 才是有效資訊」的直覺）；理論證明常用 **full SVD**（保留 $U, V$ 的「正交方陣」性質方便代數推導）。

**可分解條件：** **任意實 $m \times n$ 矩陣**都有 SVD（無例外，包含全零矩陣 $A = O$ 也有 $\sigma_p \equiv 0$ 的平凡分解）。**這是 SVD 比所有其他分解都「親民」的根本特性**。

### 2. SVD 的構造算法（核心 ⭐）— 兩個對稱矩陣 EVD 的整合

SVD 的存在性可以用「兩個對稱矩陣的 EVD」來證明，這也是數值計算 SVD 的基礎方法之一。

**Step 1：** 構造 $A^{\mathrm{T}} A$（$n \times n$，**對稱半正定**）。

- **對稱性：** $(A^{\mathrm{T}} A)^{\mathrm{T}} = A^{\mathrm{T}} A$ ✓（顯然）；
- **半正定：** 對任意 $\mathbf{x}$，$\mathbf{x}^{\mathrm{T}} (A^{\mathrm{T}} A) \mathbf{x} = \|A \mathbf{x}\|^2 \geq 0$ ✓。

**Step 2：** 對 $A^{\mathrm{T}} A$ 做 EVD（§6.4）：

$$
A^{\mathrm{T}} A = V \Lambda V^{\mathrm{T}}
$$

— $V$ 正交、$\Lambda$ 對角（特徵值 $\lambda_p \geq 0$ 因半正定）。**令 $\sigma_p = \sqrt{\lambda_p}$（取非負平方根，按降冪排序）。**

**Step 3：** 對非零 $\sigma_p > 0$，定義左奇異向量：

$$
\mathbf{u}_p = \dfrac{A \mathbf{v}_p}{\sigma_p}
$$

**驗證 $\mathbf{u}_p$ 正交且單位長：**

$$
\mathbf{u}_p^{\mathrm{T}} \mathbf{u}_q = \dfrac{1}{\sigma_p \sigma_q} (A \mathbf{v}_p)^{\mathrm{T}} (A \mathbf{v}_q) = \dfrac{1}{\sigma_p \sigma_q} \mathbf{v}_p^{\mathrm{T}} A^{\mathrm{T}} A \mathbf{v}_q = \dfrac{\lambda_q}{\sigma_p \sigma_q} \mathbf{v}_p^{\mathrm{T}} \mathbf{v}_q = \dfrac{\sigma_q^2}{\sigma_p \sigma_q} \delta_{pq} = \delta_{pq}
$$

— 左奇異向量自動正交且單位長 ✓。

**Step 4：** 對零奇異值 $\sigma_p = 0$，對應 $\mathbf{v}_p \in \mathbf{N}(A)$（$A$ 的零空間），$\mathbf{u}_p$ 不由公式定義，**任選一組張成 $\mathbf{N}(A^{\mathrm{T}})$（$A$ 的左零空間）的正交單位基底**填入 $U$ 的剩餘行。

**Step 5：** 組裝 $U, \Sigma, V$。

**對稱對偶（也可從 $AA^{\mathrm{T}}$ 出發）：**

$$
AA^{\mathrm{T}} = U \Sigma \Sigma^{\mathrm{T}} U^{\mathrm{T}} = U \Sigma^2 U^{\mathrm{T}}
$$

— **$AA^{\mathrm{T}}$ 的 EVD 直接給出 $U$ 和同樣的 $\sigma_p^2$**。所以 $V$ 從 $A^{\mathrm{T}} A$ 來、$U$ 從 $AA^{\mathrm{T}}$ 來。

**這個構造的視覺含義：** SVD = 「**先在 $\mathbb{R}^n$ 找一組正交方向 $\mathbf{v}_p$（讓 $A$ 把它們映射到正交方向）**」 + 「**對應的 $\mathbf{u}_p$ 自動是正交的**」+ 「**縮放因子是 $\sigma_p$**」。**SVD 找到了「$A$ 把正交映射到正交」的特殊方向組** — 一般矩陣不會把任意正交基底保持為正交，但 SVD 找到了那組「最特別的」正交基底（$\mathbf{v}_p$）使映射後仍正交（$\mathbf{u}_p$）。

### 3. 與 (P4) 視角的連結 — 三明治結構（核心 ⭐）

**(P4) Pattern（§5）：** 「兩個矩陣夾一個對角矩陣 = 秩 1 之和（用對角元素加權）」

$$
\underbrace{U}_{\text{左側}} \underbrace{D}_{\text{對角}} \underbrace{V^{\mathrm{T}}}_{\text{右側}} = \sum_p d_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

**SVD 是 (P4) 的「最一般情境」** — 左側 $U$ 與右側 $V^{\mathrm{T}}$ **是兩個獨立的正交矩陣**（不像 EVD 強制 $U = V$），對角 $\Sigma$ 是非負的奇異值：

$$
A = \underbrace{U}_{\text{左 = 左奇異向量正交基底}} \underbrace{\Sigma}_{\text{對角 = 奇異值（非負降冪）}} \underbrace{V^{\mathrm{T}}}_{\text{右 = 右奇異向量正交基底（與 U 不同）}}
= \sum_p \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

**對照表（SVD vs EVD vs 一般 (P4)）：**

| 元素 | (P4) 一般形式 | EVD 特化 | **SVD 完整版** |
|---|---|---|---|
| 左側 | $U$（任意） | $Q$（正交，特徵向量） | $U$（**正交，左奇異向量**） |
| 對角 | $D$（任意對角） | $\Lambda$（特徵值，可負） | $\Sigma$（**奇異值，非負降冪**） |
| 右側 | $V^{\mathrm{T}}$（任意） | $Q^{\mathrm{T}}$（左側轉置） | $V^{\mathrm{T}}$（**與 $U$ 不同的正交矩陣**） |
| 矩陣性質 | 任意 | 對稱 + 任意 | **任意（無限制）** |
| 秩 1 形式 | $\sum d_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ | $\sum \lambda_p \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$（自外積） | $\sum \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$（**一般外積**） |
| 對稱性 | 無 | $S = S^{\mathrm{T}}$ | **無**（任意 $A$） |

**「using P4」標籤的意涵（與 EVD 對比）：** 原書 `SVD.png` 標 `using P4`，與 `EVD.png` 同款 — 但意義不同：
- **EVD 標 P4**：是 (P4) 的「**自鏡像 + 對角是特徵值**」特化（兩側相同）；
- **SVD 標 P4**：是 (P4) 的「**雙側獨立 + 對角是奇異值（非負）**」一般情境。

**`SVD = 完整 P4`，`EVD = 對稱 P4 特例`。** 這就是為什麼 §6.5 排在 §6.4 後面 — 一般情境放後面，特殊情境（更強限制）放前面，方便讀者「從特殊推一般」。

**連結 (MM4) — 本章雙 pointer 的「內容鐵證」：**

$$
A = \sum_{p=1}^{r} \underbrace{\sigma_p \mathbf{u}_p}_{\text{係數 × 列}} \cdot \underbrace{\mathbf{v}_p^{\mathrm{T}}}_{\text{行}} = \sum_{p=1}^{r} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

這正好是 (MM4) 「外積之和」的形式，**且是「最有意義的 (MM4)」** — 因為 $\sigma_p$ 按大小降冪排，所以「**前幾項貢獻最大、後幾項貢獻最小**」，這就是「**最佳低秩近似**」的根本（見第 5 節 Eckart–Young）。**ch04 VizScript-02 的 Mona Lisa SVD demo 就是預先實作了 SVD 章的核心視覺化** — SVD 章直接 pointer 到 ch04 即可，無須重複實作。

### 4. 四子空間的 SVD 對齊（核心 ⭐）— Strang 兩塊大餅圖的 SVD 構造

回顧 §3 4-Subspaces：對任意 $A$ 有四個基本子空間：

- **行空間** $\mathbf{C}(A^{\mathrm{T}}) \subset \mathbb{R}^n$（維度 = $r$）；
- **零空間** $\mathbf{N}(A) \subset \mathbb{R}^n$（維度 = $n - r$）；
- **列空間** $\mathbf{C}(A) \subset \mathbb{R}^m$（維度 = $r$）；
- **左零空間** $\mathbf{N}(A^{\mathrm{T}}) \subset \mathbb{R}^m$（維度 = $m - r$）。

**SVD 直接給出四子空間的正交基底：**

| 子空間 | 維度 | SVD 正交基底 |
|---|---|---|
| 行空間 $\mathbf{C}(A^{\mathrm{T}})$ | $r$ | $\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$（**$V$ 的前 $r$ 列**）|
| 零空間 $\mathbf{N}(A)$ | $n - r$ | $\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\}$（**$V$ 的後 $n - r$ 列**）|
| 列空間 $\mathbf{C}(A)$ | $r$ | $\{\mathbf{u}_1, \ldots, \mathbf{u}_r\}$（**$U$ 的前 $r$ 列**）|
| 左零空間 $\mathbf{N}(A^{\mathrm{T}})$ | $m - r$ | $\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\}$（**$U$ 的後 $m - r$ 列**）|

**SVD 的「對齊性質」：** 對 $1 \leq p \leq r$，$A \mathbf{v}_p = \sigma_p \mathbf{u}_p$ — 這意味著 **$A$ 把 $\mathbf{v}_p$（行空間中的方向）映射到 $\sigma_p \mathbf{u}_p$（列空間中的對應方向）**。對 $p > r$，$A \mathbf{v}_p = \mathbf{0}$（$\mathbf{v}_p$ 在零空間中）。

**這是 Strang 兩塊大餅圖的精準數學表達** — SVD 的 $\mathbf{u}, \mathbf{v}$ 同時把「行空間 / 零空間」和「列空間 / 左零空間」分別正交分解，並用對角 $\sigma_p$ 連結兩側。**SVD 是「線性代數最完整的視覺定理」**，在 ch03 4-Subspaces 已有 ⭐⭐⭐ Tier 3 VizScript-02 母模板。

**對 SVD 來說有特殊意義的維度等式（rank-nullity 的 SVD 版）：**

$$
\underbrace{r}_{\text{非零 }\sigma_p \text{ 個數}} + \underbrace{(n - r)}_{\text{零 }\sigma_p \text{ 在 }V\text{ 側的個數}} = n, \qquad
r + (m - r) = m
$$

— **「奇異值的『非零個數』就是矩陣的秩 $r$」**。這是 SVD 給出 $\operatorname{rank}(A)$ 最直接、數值上最穩定的方法（比 RREF / 高斯消去都好）。

### 5. 最佳低秩近似定理（Eckart–Young Theorem）— SVD 的旗艦應用（核心 ⭐）

**定理（Eckart–Young 1936）：** 對任意 $A_{m \times n}$，定義「**秩 $k$ SVD 截斷**」為

$$
A_k = \sum_{p=1}^{k} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}, \qquad k \leq r
$$

則 **$A_k$ 是「在 Frobenius 範數 / 譜範數意義下最接近 $A$ 的秩 $k$ 矩陣」**：

$$
\min_{\substack{B_{m \times n} \\ \operatorname{rank}(B) \leq k}} \|A - B\|_F = \|A - A_k\|_F = \sqrt{\sigma_{k+1}^2 + \sigma_{k+2}^2 + \cdots + \sigma_r^2}
$$

$$
\min_{\substack{B_{m \times n} \\ \operatorname{rank}(B) \leq k}} \|A - B\|_2 = \|A - A_k\|_2 = \sigma_{k+1}
$$

**直覺：** 「**捨棄最小的奇異值，誤差就最小**」 — 因為奇異值按降冪排，最後幾個 $\sigma_p$ 對矩陣的「能量貢獻」最少，移除它們造成的誤差最小。

**這是「**SVD 在所有應用中發揮作用的根本理由**」：**

- **影像壓縮：** 一張 $1000 \times 1000$ 影像（100 萬像素）用秩 $k = 50$ 近似，僅需儲存 $50 \cdot (1000 + 1000) = 100{,}000$ 個數（壓縮 10 倍），且視覺品質常常可接受（$\sigma_{51}$ 很小）；
- **PCA 降維：** 取前 $k$ 個 $\mathbf{v}_p$ 作為主成分，保留「方差最大」的 $k$ 個方向；
- **降噪：** 截斷小奇異值（雜訊集中在小 $\sigma_p$）即可去噪；
- **推薦系統：** 用低秩 $A_k$ 補全用戶 × 產品評分矩陣（Matrix Factorization）。

**Eckart–Young 證明大綱：** 用 $\|A - B\|_F^2 = \operatorname{tr}((A-B)^{\mathrm{T}}(A-B))$ + 推導 $B$ 的最佳形式必為 $A$ 的 SVD 截斷 + 用奇異值的「極值性質」 $\sigma_k = \min_{\dim S = m - k + 1} \max_{\mathbf{x} \in S, \|\mathbf{x}\|=1} \|A\mathbf{x}\|$。詳細證明見 Strang 7.2 或 Trefethen & Bau Lecture 5。

**這個定理對 ch04 VizScript-02 (Mona Lisa SVD demo) 是「靈魂」** — Mona Lisa 從 $k = 1, 2, 5, 10, 20, 50$ 依序顯示，每個 $k$ 都是「**最佳秩 $k$ 近似**」（不是隨意的低秩矩陣）。**SVD 章 VizScript-01 直接 pointer 到 ch04 看 Mona Lisa demo**，無須重複實作。

### 6. SVD 的四大旗艦應用詳解（本章獨有，全書最豐富的應用章）

#### 6.1 影像 / 資料壓縮

**核心想法：** 影像（灰階）= $m \times n$ 矩陣，每個元素是像素亮度。對影像做 SVD，取前 $k$ 個秩 1 項組合 = 「**用 $k$ 個「特徵圖案」線性組合表達整張圖**」。

**儲存比較：**

- 原始：$m \times n$ 個數（如 $1000 \times 1000 = 10^6$）；
- 秩 $k$ 近似：$k(m + n) + k$ 個數（$U$ 的前 $k$ 列 + $V$ 的前 $k$ 列 + $k$ 個 $\sigma_p$）；
- **壓縮比 $\approx mn / (k(m+n))$**，當 $k \ll \min(m,n)$ 時壓縮極顯著。

**典型範例：** Mona Lisa $400 \times 250$ 像素 = 10 萬。秩 $k = 20$ 重建：$20 \cdot 650 + 20 = 13{,}020$，壓縮約 7.7 倍，視覺品質可接受（**詳見 ch04 VizScript-02 Mona Lisa demo**）。

#### 6.2 PCA（主成分分析）

**核心想法：** 給一筆資料 $X_{N \times d}$（$N$ 筆樣本、$d$ 個特徵），先「**置中**」（每行減平均）得 $\tilde{X}$，對 $\tilde{X}$ 做 SVD：

$$
\tilde{X} = U \Sigma V^{\mathrm{T}}
$$

**$V$ 的列（前 $k$ 個 $\mathbf{v}_p$）= 主成分方向。** 每個主成分對應的「方差貢獻」為 $\sigma_p^2 / N$。

**降維：** $\tilde{X}_{N \times d} \to \tilde{X} V_k = U_k \Sigma_k$（$N \times k$ 矩陣，每筆樣本變 $k$ 維）。

**為什麼用 SVD 不用直接對 $\tilde{X}^{\mathrm{T}} \tilde{X}$ 做 EVD？** 因為當 $N$ 很大時，$\tilde{X}^{\mathrm{T}} \tilde{X}$ 計算昂貴且數值不穩；SVD 直接對 $\tilde{X}$ 做（不算 $\tilde{X}^{\mathrm{T}} \tilde{X}$），數值穩定且效率更高。**現代 PCA 演算法都用 SVD。**

**經典應用：** 人臉識別（Eigenfaces）、基因表達分析、金融資料降維、特徵工程。

#### 6.3 降噪 / 去模糊

**核心想法：** 假設「**訊號集中在大奇異值對應的方向、雜訊集中在小奇異值對應的方向**」，截斷小奇異值即可降噪。

**算法：**

1. 對含雜訊的訊號 $A_{\text{noisy}}$ 做 SVD；
2. 設定閾值 $\tau$（如 $\tau = 0.01 \cdot \sigma_1$ 或用 Stein 不偏估計）；
3. 截斷：$A_{\text{denoised}} = \sum_{p: \sigma_p > \tau} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$；
4. （或軟閾值）替換每個 $\sigma_p \to \max(\sigma_p - \tau, 0)$。

**應用：** 影像降噪、地震訊號分離、語音降噪、生醫訊號（EEG/ECG）去人造干擾。

#### 6.4 推薦系統 / 矩陣補全

**核心想法：** 用戶 × 產品評分矩陣 $A_{N \times M}$（$N$ 個用戶、$M$ 個產品）通常**極度稀疏**（大部分用戶沒看過大部分產品 → 缺失值）。假設「**用戶喜好可由少數潛在因子（latent factors）描述**」 → 完整矩陣是低秩的。

**算法（Latent Factor Model）：**

1. 對已知評分位置做正則化最佳化 $\min \|P_{\Omega}(A - U \Sigma V^{\mathrm{T}})\|_F^2 + \lambda(\|U\|_F^2 + \|V\|_F^2)$；
2. 解得低秩近似 $A \approx U_k \Sigma_k V_k^{\mathrm{T}}$；
3. **預測缺失評分：** $A_{ij} \approx (U_k \Sigma_k V_k^{\mathrm{T}})_{ij}$（用 $i$ 用戶的 $k$ 維潛在因子 + $j$ 產品的 $k$ 維潛在因子內積）。

**經典案例：** Netflix Prize（2006–2009，獎金 100 萬美元）的核心解法之一就是 SVD 變體。

### 7. $A = U\Sigma V^{\mathrm{T}}$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **SVD ↔ CR** | CR 給出列空間基底 $C$，但 $C$ 不一定正交；SVD 直接給出**正交**列空間基底 $U_{[:, :r]}$。**SVD 是 CR 的「正交化升級版」**且唯一適用任意矩陣 |
| **SVD ↔ LU** | LU 解 $A\mathbf{x} = \mathbf{b}$ 用兩步反代（限方陣 + 主元）；SVD 解 $A\mathbf{x} = \mathbf{b}$ 用 $\mathbf{x} = V \Sigma^{+} U^{\mathrm{T}} \mathbf{b}$（**Moore–Penrose 偽反**，**任意矩陣**都可解，給出最小二乘解） |
| **SVD ↔ QR** | QR 是「列正交化」（限列獨立）；SVD 是「**雙側正交化**」（任意矩陣）。**從 QR 到 SVD = 把 $R$ 也正交化變對角 $\Sigma$**。實務上**奇異值計算的標準算法是「先 QR 化簡，再 EVD」** — QR 是 SVD 計算的中間步驟 |
| **SVD ↔ EVD** | **SVD 是 EVD 的「一般化」** — EVD 限對稱、$U = V$；SVD 任意矩陣、$U \neq V$。對任意 $A$：$A^{\mathrm{T}} A$ EVD 給 $V, \Sigma^2$；$AA^{\mathrm{T}}$ EVD 給 $U, \Sigma^2$。**SVD = 兩個對稱半正定矩陣 EVD 的整合** |

**結論：** $A = U\Sigma V^{\mathrm{T}}$ 是「**任意矩陣的雙側獨立正交對角化**」 — 是五大分解中最一般、最完整、最重要的一個。沿著「正交化逐步加強 + 限制逐步解除」的階梯看：

$$
\underbrace{CR}_{\text{0 側正交}} \;\to\; \underbrace{LU}_{\text{0 側正交 + 三角}} \;\to\; \underbrace{QR}_{\text{1 側正交 + 三角}} \;\to\; \underbrace{Q\Lambda Q^{\mathrm{T}}}_{\substack{\text{2 側正交 + 對角}\\\text{（限對稱，鏡像）}}} \;\to\; \underbrace{U\Sigma V^{\mathrm{T}}}_{\substack{\text{2 側正交 + 對角}\\\text{（任意矩陣，獨立）}}}
$$

**SVD 是這個階梯的「終點」 — 結構最強（雙側正交 + 對角）+ 適用最廣（任意矩陣）+ 最佳低秩近似（Eckart–Young）+ 四子空間對齊（Strang 兩塊大餅）+ 工程應用最多（壓縮 / PCA / 降噪 / 推薦）。**

### 8. 數學要點總結（一張表）

| 性質 | $A = U\Sigma V^{\mathrm{T}}$ 的對應 |
|---|---|
| 適用矩陣 | **任意實 $m \times n$ 矩陣**（無限制，包含全零、長方、不可逆） |
| $U$ 的結構 | $m \times m$（full）或 $m \times r$（reduced）正交矩陣，列為左奇異向量 $\mathbf{u}_p$，$U^{\mathrm{T}} U = I$ |
| $\Sigma$ 的結構 | $m \times n$（full）或 $r \times r$（reduced）「**長方對角**」矩陣，對角為非負奇異值 $\sigma_1 \geq \cdots \geq \sigma_r > 0$（之後皆 0） |
| $V$ 的結構 | $n \times n$（full）或 $r \times n$（reduced）正交矩陣，列為右奇異向量 $\mathbf{v}_p$，$V^{\mathrm{T}} V = I$ |
| 項數 | $r = \operatorname{rank}(A) \leq \min(m, n)$（reduced）或 $\min(m, n)$（full，含零項）|
| 構造方法 | 對 $A^{\mathrm{T}} A$（或 $AA^{\mathrm{T}}$）做 EVD → 取 $\sqrt{\lambda_p}$ 為 $\sigma_p$ → 用 $\mathbf{u}_p = A\mathbf{v}_p / \sigma_p$ 互推；數值上用「Golub–Reinsch」或「one-sided Jacobi」算法 |
| §4 (MM4) 對應 | $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$（**完整 (MM4) 形式 + 奇異值降冪排序**）|
| §5 Pattern 對應 | **`SVD.png` 標 `using P4`**：(P4) 三明治的「雙側獨立正交 + 對角非負」一般情境 |
| 求 $A^{-1}$（方陣可逆） | $A^{-1} = V \Sigma^{-1} U^{\mathrm{T}}$（對角倒數，前提 $\sigma_p > 0$）|
| 求 Moore–Penrose 偽反 | $A^{+} = V \Sigma^{+} U^{\mathrm{T}}$（**任意矩陣**，$\Sigma^{+}$ 對非零 $\sigma_p$ 取倒數，零保持）|
| 最佳秩 $k$ 近似 | $A_k = \sum_{p \leq k} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$，誤差 $\|A - A_k\|_F = \sqrt{\sum_{p > k} \sigma_p^2}$ |
| 四子空間 | $\mathbf{C}(A^{\mathrm{T}}) = \operatorname{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$，$\mathbf{N}(A) = \operatorname{span}\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\}$，$\mathbf{C}(A) = \operatorname{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_r\}$，$\mathbf{N}(A^{\mathrm{T}}) = \operatorname{span}\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\}$ |
| 計算量 | $O(\min(mn^2, m^2 n))$（標準算法）；隨機化 SVD $O(mn k)$（取前 $k$ 個）|

---

## 圖片詳細描述（Figure Descriptions）

### Figure 6.7: $A = U\Sigma V^{\mathrm{T}}$ — 標 using P4

**圖檔：** `docs/book/figs-png/SVD.png`（原始 EPS：`figs/SVD.eps`）
**原書頁碼：** p.12 圖 17
**所屬章節：** §6.5 $A = U\Sigma V^{\mathrm{T}}$（**唯一一張**，無對偶圖；reduced SVD 形式）
**圖中標記：** **`using P4`**（圓圈標，右下角）

#### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，3×2 長方矩陣示意（reduced SVD），共 8 段：

1. **第 1 段：** 矩陣 $A$ 的方框（內含**淺灰色塊**，**長方形 3 列 × 2 行**）— 上方有大字 `A`；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 矩陣 $U$（方框內 **3 條等寬綠色直立列，每列底部標 `1`/`2`/`3`**，呈 3×2 長方形）— 上方有大字 `U`；綠色 = 「正交且單位長」視覺信號；**注意是 3×2（reduced）不是 3×3（full）**；
4. **第 4 段：** 矩陣 $\Sigma$（方框內 **2 個藍色圓點沿對角線排列**，2×2 方形，非對角位置完全留白）— 上方有大字 $\Sigma$；**藍點明示「$\Sigma$ 是對角」+ 只有 2 個非零（對應 $r = 2$）**；
5. **第 5 段：** 矩陣 $V^{\mathrm{T}}$（方框內 **2 條等寬粉紅色橫躺行，每行左側標 `1`/`2`**，2×2 方形）— 上方有大字 $V^{\mathrm{T}}$；**粉紅色 = 行視角 + 「與 $U$ 不同」的視覺信號**（與 $U$ 綠色形成對比）；
6. **第 6 段：** 等號 `=`；
7. **第 7–8 段：** 拆解結果，**2 個方框並排，每個都標 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$**：
   - 第 7 段：$\sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}}$ — 方框內含 **1 條綠色直立列（標 `1`）+ 上方淡粉紅橫躺行（標 `1`）**，藍點標 $\sigma_1$；
   - 第 8 段：加號 `+`；$\sigma_2 \mathbf{u}_2 \mathbf{v}_2^{\mathrm{T}}$ — **同樣結構，標 `2`**；
8. **右下角圖示：** 圓圈內標 `P4`，文字 `using` — **直接標明「本圖用 §5 Pattern 4 視角」**。

**「綠列 + 粉紅行」對比布局的視覺意義：** 與 EVD 圖（兩側都用綠色）形成鮮明對比 — SVD 的兩側用**不同顏色**，視覺上明確展示「**$U$ 和 $V$ 是兩個不同的正交矩陣**」。**這是 SVD 與 EVD 的視覺指紋差異**：EVD 兩側是「自鏡像」（同色），SVD 兩側是「獨立配對」（異色）。

**閱讀順序：** 由左到右讀整個等式鏈 `A = U Σ V^T = (兩個 σ_p u_p v_p^T 累加)`。重點掃右側的 2 個拆解項，注意「**綠列 + 粉紅行對偶布局 + 藍點 σ_p 加權**」。**reduced SVD 的「項數 = 秩」直觀展示** — 圖中只有 2 項，因為 $r = 2$。

#### 數學內容 (Mathematical Content)

對應數學表示（**(P4) Pattern 4** 三明治視角，雙側獨立正交特化版）：

$$
A = U \Sigma V^{\mathrm{T}}
= \begin{bmatrix} | & | & | \\ \mathbf{u}_1 & \mathbf{u}_2 & \mathbf{u}_3 \\ | & | & | \end{bmatrix}
\begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \\ 0 & 0 \end{bmatrix}
\begin{bmatrix} - & \mathbf{v}_1^{\mathrm{T}} & - \\ - & \mathbf{v}_2^{\mathrm{T}} & - \end{bmatrix}
$$

或（reduced 形式，省略 $\mathbf{u}_3$ 對應的 0 列）：

$$
A = \begin{bmatrix} | & | \\ \mathbf{u}_1 & \mathbf{u}_2 \\ | & | \end{bmatrix}
\begin{bmatrix} \sigma_1 & 0 \\ 0 & \sigma_2 \end{bmatrix}
\begin{bmatrix} - & \mathbf{v}_1^{\mathrm{T}} & - \\ - & \mathbf{v}_2^{\mathrm{T}} & - \end{bmatrix}
= \sum_{p=1}^{2} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}
$$

**關鍵數值關係（對任意 $A$）：**

- $A^{\mathrm{T}} A \mathbf{v}_p = \sigma_p^2 \mathbf{v}_p$（$\mathbf{v}_p$ 是 $A^{\mathrm{T}} A$ 的特徵向量）；
- $A A^{\mathrm{T}} \mathbf{u}_p = \sigma_p^2 \mathbf{u}_p$（$\mathbf{u}_p$ 是 $A A^{\mathrm{T}}$ 的特徵向量）；
- $A \mathbf{v}_p = \sigma_p \mathbf{u}_p$（**SVD 的對齊性質**）；
- $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$（非負降冪排序）；
- $\operatorname{rank}(A) = r = $ 非零 $\sigma_p$ 的個數。

**從 $A$ 提取 $(\sigma_p, \mathbf{u}_p, \mathbf{v}_p)$：** 對 $A^{\mathrm{T}} A$ 做 EVD（§6.4 算法）→ 取平方根 → 用 $\mathbf{u}_p = A\mathbf{v}_p / \sigma_p$ 互推。

#### 直覺解讀 (Intuition)

SVD 圖傳達五層核心訊息：

1. **「雙側獨立 = SVD 的核心」直覺：** $U$（綠列）和 $V^{\mathrm{T}}$（粉紅行）用**不同顏色**展示，視覺上立刻看出「**兩側是兩個獨立的正交矩陣**」。**這是 SVD 與 EVD 的最大差異** — EVD 兩側是同一個 $Q$，SVD 兩側是獨立的 $U, V$；

2. **「對角 $\Sigma$ = 純縮放 + 非負」直覺：** 中間的 2 個藍點沿對角排列，**只有 2 個（不是 3 個）** — 視覺上明示「**reduced SVD 只取非零奇異值**」+ 「奇異值都 $\geq 0$（不像特徵值可負）」+ 「降冪排序（從大到小）」；

3. **「秩 1 拆解 = (MM4) 的最有意義版」直覺：** 右側 2 個拆解項使用**綠列 × 粉紅行**（不同色），視覺上強調「**一般外積 $\mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$**」（與 EVD 自外積 $\mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 對比）。**且兩項按 $\sigma_p$ 降冪排，第 1 項貢獻最大（最佳秩 1 近似）**；

4. **「項數 = 秩」直覺：** 圖中只有 2 項拆解（不是 3 項），直接展示「**SVD 的非零項數 = 矩陣的秩**」。**這是 SVD 給 $\operatorname{rank}(A)$ 最直觀的方法**；

5. **「reduced SVD 適配長方陣」直覺：** $A$ 是 3×2 長方陣，reduced SVD 把 $U$ 也設為 3×2、$V$ 設為 2×2，整個分解在「**有效維度 = 秩 $r$**」下進行，不浪費儲存空間。

**「using P4」標籤的重要性（S09 PNG 重核確認）：** 原書作者刻意把這張圖標 `using P4`，與 §6.4 EVD 同款 — 等於明說「**SVD 圖跟 EVD 圖是同一種視角（(P4) 三明治），只是 SVD 雙側獨立、EVD 雙側同一**」。視覺化可以**直接重用 [ch05 VizScript-03](ch05-patterns.md#vizscript-03) 的 P4 三明治互動**（單 pointer 副線），但因「秩 1 累加 + 低秩近似」與 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) Mona Lisa SVD demo 完全同根，**主 pointer 採雙 pointer 設計指 ch04**。

**為什麼這張圖該做成互動視覺化？** 因為 SVD 是「**全書理論的封頂 + 工程應用最多**」：
- 「秩 1 累加」過程展示「**為何前幾項最重要**」（Eckart–Young 直覺）；
- 「**4 應用切換**」（壓縮 / PCA / 降噪 / 推薦）讓使用者理解 SVD 的實際用途；
- 「**4 子空間視覺**」（與 ch03 4-Subspaces 整合）展示 Strang 兩塊大餅圖的 SVD 構造；
- 「**2D 變形動畫**」（單位圓 → 橢圓）展示 SVD 的幾何直覺：$A = (\text{旋轉}) (\text{縮放}) (\text{旋轉})$。

靜態圖只能展示最終結果，**互動 demo 可以展示「**使用者調 $A$ → 即時更新 4 種應用 + 4 子空間 + 2D/3D 幾何**」**，這是 SVD 教學的關鍵突破點，也是**全書最值得實作 Tier 3 的 VizScript**（見 VizMark-01）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [SVD 完整互動 + 4 應用切換] ⭐⭐⭐ Tier 3
> 「全書旗艦 VizScript：拉桿調 $A$ → 即時 SVD → 4 應用切換（壓縮 / PCA / 降噪 / 推薦）+ 2D/3D 幾何（單位圓 → 橢圓）+ 4 子空間視覺整合 ch03 兩塊大餅圖 + Mona Lisa 低秩近似 demo（雙 pointer 指 ch04 Mona Lisa）」
> **詳見劇本：** VizScript-01（章末，Tier 3 全書最強）

> 🎬 **VizMark-02** [奇異值降冪 + Eckart–Young 視覺] ⭐⭐⭐ Tier 2
> 「Bar chart 顯示 $\sigma_1 \geq \sigma_2 \geq \cdots$ + 累計能量曲線 $\sum_{p \leq k} \sigma_p^2 / \sum \sigma_p^2$ + 滑桿選 $k$ 看截斷誤差 → 視覺化 Eckart–Young 定理」
> **詳見劇本：** VizScript-02（章末）

> 🎬 **VizMark-03** [4 子空間 SVD 構造] ⭐⭐
> 「整合 ch03 4-Subspaces 兩塊大餅圖 + SVD 直接給 $\mathbf{u}_p, \mathbf{v}_p$ 作為基底 + 動畫展示 $A \mathbf{v}_p = \sigma_p \mathbf{u}_p$ 對齊性質」
> **詳見劇本：** VizScript-03（章末，精簡版）

> 🎬 **VizMark-04** [2×2 SVD walkthrough] ⭐
> 「用 2×2 範例 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$ 一步一步動畫展示 SVD 計算過程，每步顯示具體數字」
> **詳見劇本：** VizScript-04（章末，輕量版）

---

## 視覺化劇本（VizScripts）

### VizScript-01: SVD 完整互動 + 4 應用切換（SVD Master Interactive — Tier 3）

**Tier：** ⭐⭐⭐ **Tier 3（全書最強規格，與 ch04 VizScript-02 同級）**
**對應 VizMark：** Figure 6.7 VizMark-01
**預估實作工作量：** S12+ 約 **3 session**（畫面框架 1 session + 4 應用切換 1 session + 4 子空間 + 2D/3D 幾何 1 session）

#### A. 一句話定位

「給一個 $A$（$m \times n$，$m, n \in [2, 6]$），即時計算 SVD → 動態展示秩 1 累加 → 4 個應用切換（壓縮 / PCA / 降噪 / 推薦）+ 2D/3D 幾何（單位圓 → 橢圓）+ 4 子空間視覺，**整合全書所有核心概念**。」

#### B. 學習目標（Learning Outcome）

- **SVD 直覺：** 看到任何矩陣，能在腦中想像「**雙側正交基底 + 對角縮放**」的幾何圖景；
- **奇異值降冪意義：** 看到 $\sigma_p$ 大小與秩 1 項貢獻的對應，建立「**取前 $k$ 項 = 最佳低秩近似**」直覺；
- **4 應用具體化：** 透過 4 個獨立 demo 看到 SVD 在「**壓縮 / PCA / 降噪 / 推薦**」中的具體用法；
- **4 子空間整合：** 透過與 ch03 4-Subspaces 的整合視覺，理解「**SVD 是 Strang 兩塊大餅圖的構造工具**」；
- **2D 幾何直覺：** 單位圓被 $A$ 變成橢圓，主軸方向 = $\mathbf{u}_p$、半徑 = $\sigma_p$；
- **跨章連結（雙 pointer）：** 點 (P4) 跳 ch05 看一般三明治 / 點 (MM4) 跳 ch04 看 Mona Lisa demo。

#### C. 互動參數（UI Inputs）

- **矩陣輸入 $A$：** $m \times n$ 格子網格，$m, n \in [2, 6]$，每格 $a_{ij} \in [-9, 9]$ 步進 1；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr]$（**對稱 2×2，SVD = EVD 退化情境，方便對照 §6.4**）；
  - 範例 2：$\bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$（**Strang 經典 2×2，$\sigma = 3\sqrt{5}, \sqrt{5}$**）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&1\\1&0\\0&1\end{smallmatrix}\bigr]$（**3×2 長方，reduced SVD，書中圖示同形**）；
  - 範例 4：$\bigl[\begin{smallmatrix}1&2&3\\2&4&6\end{smallmatrix}\bigr]$（**rank = 1 退化，只有 1 個非零 $\sigma$**）；
  - 範例 5：$I_3$（單位矩陣，所有 $\sigma_p = 1$，$U = V = I$）；
  - 範例 6：Mona Lisa $400 \times 250$（**真實影像，跳轉到 ch04 Mona Lisa demo**）；
  - 範例 7：Iris 資料集（150×4，**PCA 應用**）；
- **應用模式切換 (主 radio，本 VizScript 核心)：**
  - `基礎 SVD`（純秩 1 累加 + 4 子空間視覺）；
  - `應用 1：壓縮`（連到 Mona Lisa demo）；
  - `應用 2：PCA`（用範例 7 Iris 資料）；
  - `應用 3：降噪`（生成含雜訊訊號 → SVD 截斷）；
  - `應用 4：推薦系統`（生成稀疏評分矩陣 → 矩陣補全）；
- **顯示模式切換 (checkbox 多選)：**
  - `顯示 4 子空間`（整合 ch03 兩塊大餅圖）；
  - `顯示 2D/3D 幾何`（單位圓 → 橢圓動畫）；
  - `顯示秩 $k$ 截斷`（滑桿 $k \in [1, r]$）；
  - `顯示奇異值 bar chart`（含累計能量）；
- **跳轉按鈕（雙 pointer 設計，本 VizScript 全書唯一）：**
  - 「→ (MM4) 秩 1 累加 / Mona Lisa」按鈕（**主 pointer**，跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)）；
  - 「→ (P4) 三明治結構」按鈕（**副 pointer**，跳 [ch05 VizScript-03](ch05-patterns.md#vizscript-03)）；
  - 「→ 4 子空間（ch03）」按鈕（跳 [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02)）；
  - 「→ 對稱情境 EVD」按鈕（跳 [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01)）。

#### D. 視覺布局（Layout）

**主畫面**（Tier 3 規格，分區更密）：

| 區 | 內容 |
|---|---|
| 左上區（輸入 + 範例） | $A$ 的格子輸入網格 + 範例選擇器 + 應用模式 radio |
| 中上區（SVD 矩陣分解） | $A, U, \Sigma, V^{\mathrm{T}}$ 四矩陣並排 + 秩 1 拆解項列下方 |
| 右上區（2D/3D 幾何） | 單位圓 → 橢圓變形動畫 + 主軸方向 $\mathbf{u}_p$（綠箭頭）+ 半徑 $\sigma_p$ |
| 左下區（奇異值 bar chart） | 縱軸 $\sigma_p$、橫軸 $p$ + 累計能量曲線 |
| 中下區（應用 demo 切換） | 依當前應用 mode 顯示：Mona Lisa（壓縮）/ Iris 散點圖（PCA）/ 訊號波形（降噪）/ 評分矩陣（推薦） |
| 右下區（4 子空間視覺，可選） | ch03 兩塊大餅圖 + SVD 給的 $\mathbf{u}_p, \mathbf{v}_p$ 標基底 |

**底部資訊條：**

- 當前的 $\sigma_p, \mathbf{u}_p, \mathbf{v}_p$ 數值（小字滾動）；
- 「**SVD 驗證：$U\Sigma V^{\mathrm{T}} = A$**」綠色 ✓；
- 「**Eckart–Young 驗證：$\|A - A_k\|_F = \sqrt{\sum_{p > k} \sigma_p^2}$**」綠色 ✓（hover 顯示具體數字）；
- **跳轉按鈕區**（4 個橫向按鈕：→ MM4 / → P4 / → 4-Subspaces / → EVD）。

#### E. 動畫腳本（Storyboard）

**Step 1（0–500ms，啟動）：** $A$ 從左上區滑入中上區，後台計算 $A^{\mathrm{T}} A$ 和 $AA^{\mathrm{T}}$ 的 EVD（顯示「Computing SVD…」進度條）。

**Step 2（500–2000ms，SVD 構造）：** $V$ 從 $A^{\mathrm{T}} A$ EVD 滑入右側、$\Sigma^2$ 滑入中間、$U$ 從 $AA^{\mathrm{T}}$ EVD 滑入左側；
- $\Sigma$ 顯示為對角藍點（按降冪排序，最大 $\sigma_1$ 在左上）；
- 公式區依序顯示 $A^{\mathrm{T}} A = V\Sigma^2 V^{\mathrm{T}}$、$AA^{\mathrm{T}} = U\Sigma^2 U^{\mathrm{T}}$、$A = U\Sigma V^{\mathrm{T}}$；
- 2D/3D 幾何區：單位圓淡入（灰色）→ 同步顯示 $A$ 變形成橢圓（金色，主軸 = $\mathbf{u}_p$ 方向、半徑 = $\sigma_p$）。

**Step 3（2000–4000ms，秩 1 累加動畫，類 ch04 VizScript-02 母模板）：**
- 第 1 項 $\sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}}$ 高亮 → 從 $U, \Sigma, V^{\mathrm{T}}$ 取出對應行列「飛」到下方拆解項位置；
- 累計部分和 $A^{(1)}$ 顯示在右側，**同步更新 2D/3D 幾何**（橢圓 → 一條線，沿 $\mathbf{u}_1$ 方向長 $\sigma_1$）；
- 顯示誤差條 $\|A - A^{(1)}\|_F$；
- 重複 Step 3 對 $p = 2, 3, \ldots, r$；
- 最終 $A^{(r)} = A$，誤差條變 0 ✓。

**Step 4（4000–5000ms，奇異值 bar chart 強調）：**
- bar chart 從左下區滑入，每個 $\sigma_p$ 對應一根藍色長條；
- 同步顯示「累計能量曲線」$\sum_{p \leq k} \sigma_p^2 / \sum \sigma_p^2$（紅色折線）；
- 滑桿 $k$ 出現在 chart 下方，使用者可拉動看截斷效果。

**Step 5（按 `應用 1：壓縮`）：**
- 中下區切換為 Mona Lisa 影像（從 ch04 VizScript-02 重用，雙 pointer 體現）；
- 滑桿選 $k$，影像即時更新為秩 $k$ 重建版本；
- 顯示壓縮比 $mn / (k(m+n))$ 與誤差 $\|A - A_k\|_F / \|A\|_F$；
- **「→ Mona Lisa 詳細 demo」按鈕**（跳 ch04 VizScript-02）。

**Step 6（按 `應用 2：PCA`）：**
- 中下區切換為 Iris 資料散點圖（4D → 2D 降維）；
- 顯示 $V$ 的前 2 列作為主成分方向；
- 滑桿選保留主成分數 $k$，散點圖即時投影到前 $k$ 個主成分空間；
- 顯示「方差貢獻」$\sigma_p^2 / N$；
- 三類 Iris（setosa / versicolor / virginica）用三色標示，**清楚展示 PCA 後類別仍可分離**。

**Step 7（按 `應用 3：降噪`）：**
- 中下區切換為含雜訊訊號（如雜訊正弦波 + 隨機矩陣表示 spectrogram）；
- 滑桿選閾值 $\tau$，截斷小於 $\tau$ 的奇異值；
- 同步顯示「原始 vs 降噪」並排對比；
- 顯示信噪比改善（SNR 改進）。

**Step 8（按 `應用 4：推薦系統`）：**
- 中下區切換為稀疏評分矩陣（用戶 × 電影，灰色 = 缺失、彩色 = 已知評分）；
- 滑桿選潛在因子數 $k$，運行矩陣補全演算法；
- 顯示「補全後預測」與「測試集 RMSE」；
- 列出「為使用者推薦的前 5 部電影」。

**Step 9（按 `顯示 4 子空間`）：**
- 右下區從 ch03 整合兩塊大餅圖（已實作的 ch03 VizScript-02 重用）；
- 把 $V$ 的前 $r$ 列標為「行空間正交基底」、$V$ 的後 $n-r$ 列標為「零空間正交基底」；
- 把 $U$ 的前 $r$ 列標為「列空間正交基底」、$U$ 的後 $m-r$ 列標為「左零空間正交基底」；
- 動畫 $A \mathbf{v}_p = \sigma_p \mathbf{u}_p$（**對齊性質**）：左圓上 $\mathbf{v}_p$ 經 $A$ 映射到右圓上 $\sigma_p \mathbf{u}_p$。

**Step 10（互動結束）：** 「**→ Mona Lisa 詳細 demo**」「**→ 對稱情境 EVD**」「**→ P4 一般三明治**」「**→ 4 子空間**」四個按鈕高亮，鼓勵跨章探索。

#### F. 配色（依全書視覺一致性錨點）

- **綠 `#2ca02c`：** $\mathbf{u}_p$ / $U$ 的列 / 列空間 / 2D 橢圓主軸；
- **粉紅 / 紅 `#d62728`：** $\mathbf{v}_p^{\mathrm{T}}$ / $V^{\mathrm{T}}$ 的行 / 行空間（與 $U$ 綠色形成對比，**SVD 雙側獨立的視覺指紋**）；
- **灰 `#cccccc`：** 原始單位圓 / 對稱輸入 $A$ 的方框 fill / 補全前缺失值；
- **金 `#FFD700`：** 變形後的橢圓 / 當前正在處理的項；
- **藍 `#1f77b4`：** $\Sigma$ 的對角元素（藍點，bar chart 的長條）/ 已知評分（推薦系統）；
- **紫 `#9467bd`：** 退化警示（rank 不足）/ 4 子空間中的「零空間方向」；
- **橙 `#ff7f0e`：** 秩 $k$ 截斷曲線 / Iris 資料 versicolor 類；
- **多類別調色盤（PCA 三色）：** 設色（setosa）藍 / 變色（versicolor）橙 / 維色（virginica）綠。

#### G. 計算邏輯（Numerical Backend）

```python
def svd_with_history(A: np.ndarray) -> dict:
    """Full SVD + step-by-step history for animation."""
    U, sigma, Vt = np.linalg.svd(A, full_matrices=False)  # reduced SVD
    r = sum(sigma > 1e-10)  # numerical rank
    history = []
    A_partial = np.zeros_like(A, dtype=float)
    for p in range(len(sigma)):
        u_p = U[:, p:p+1]
        v_p = Vt[p:p+1, :]
        rank1 = sigma[p] * u_p @ v_p
        A_partial = A_partial + rank1
        history.append({
            'p': p + 1,
            'sigma_p': float(sigma[p]),
            'u_p': u_p.flatten().tolist(),
            'v_p': v_p.flatten().tolist(),
            'rank1': rank1.tolist(),
            'A_partial': A_partial.tolist(),
            'error_fro': float(np.linalg.norm(A - A_partial, 'fro')),
            'energy_cumulative': float(np.sum(sigma[:p+1]**2) / np.sum(sigma**2)),
        })
    return {'U': U, 'sigma': sigma, 'Vt': Vt, 'rank': r, 'history': history}


def four_subspaces(A: np.ndarray, tol: float = 1e-10) -> dict:
    """Return SVD-based orthonormal bases for the four fundamental subspaces."""
    U, sigma, Vt = np.linalg.svd(A, full_matrices=True)
    r = sum(sigma > tol)
    return {
        'row_space': Vt[:r].T,        # C(A^T): first r columns of V
        'null_space': Vt[r:].T,       # N(A): last n-r columns of V
        'col_space': U[:, :r],        # C(A): first r columns of U
        'left_null_space': U[:, r:],  # N(A^T): last m-r columns of U
        'rank': r,
    }


def pca(X: np.ndarray, k: int) -> dict:
    """Standard PCA via SVD (assumes X is N x d, rows = samples)."""
    X_centered = X - X.mean(axis=0)
    U, sigma, Vt = np.linalg.svd(X_centered, full_matrices=False)
    components = Vt[:k].T  # d x k, columns = principal directions
    explained_variance = sigma[:k]**2 / X.shape[0]
    projection = X_centered @ components  # N x k
    return {
        'components': components,
        'explained_variance': explained_variance,
        'projection': projection,
        'sigma': sigma,
    }


def low_rank_approx(A: np.ndarray, k: int) -> tuple[np.ndarray, float]:
    """Eckart-Young best rank-k approximation."""
    U, sigma, Vt = np.linalg.svd(A, full_matrices=False)
    A_k = U[:, :k] @ np.diag(sigma[:k]) @ Vt[:k]
    error_fro = float(np.linalg.norm(A - A_k, 'fro'))
    return A_k, error_fro


def denoise_svd(A_noisy: np.ndarray, threshold: float) -> np.ndarray:
    """Hard-threshold denoising via SVD truncation."""
    U, sigma, Vt = np.linalg.svd(A_noisy, full_matrices=False)
    sigma_thresh = np.where(sigma > threshold, sigma, 0)
    return U @ np.diag(sigma_thresh) @ Vt


def matrix_completion_simple(A_observed: np.ndarray, mask: np.ndarray, k: int, n_iter: int = 100) -> np.ndarray:
    """Simple matrix completion via iterated SVD truncation."""
    A = A_observed.copy()
    for _ in range(n_iter):
        A_k, _ = low_rank_approx(A, k)
        A = mask * A_observed + (1 - mask) * A_k
    return A


def ellipse_2d(A: np.ndarray, n_pts: int = 100) -> tuple[np.ndarray, np.ndarray]:
    """For 2D visualization: parametrize unit circle then apply A."""
    theta = np.linspace(0, 2 * np.pi, n_pts)
    unit_circle = np.array([np.cos(theta), np.sin(theta)])
    ellipse = A @ unit_circle
    return unit_circle, ellipse
```

**正確性驗證：**

- $U^{\mathrm{T}} U = V^{\mathrm{T}} V = I$（正交性）；
- $A V = U \Sigma$（對齊性質）；
- $\sum_p \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}} = A$（秩 1 累加完整）；
- `np.linalg.matrix_rank(A) == sum(sigma > tol)`（秩一致）。

#### H. 邊界情況處理

| 情況 | 偵測 | 處理 |
|---|---|---|
| $A$ 全零 | `np.allclose(A, 0)` | 所有 $\sigma_p = 0$，分解平凡，UI 顯示「全零矩陣，rank 0」|
| 退化（$\operatorname{rank} < \min(m, n)$）| 數值 $\sigma_p < tol$ 個數 > 0 | reduced SVD 自動只取非零項，4 子空間區顯示零空間維度 > 0 |
| 重複奇異值 | `len(set(sigma_rounded)) < r` | $\mathbf{u}_p, \mathbf{v}_p$ 在重複特徵子空間內任選正交基底（NumPy 自動處理）|
| $m \neq n$（長方）| 形狀檢查 | 自動切換 reduced SVD（避免 full SVD 浪費），UI 顯示「reduced SVD」標籤 |
| $\Sigma$ 含負對角 | 不可能（SVD 保證 $\sigma_p \geq 0$）| 若數值上出現極小負數，自動歸零並警示 |
| Mona Lisa demo 載入失敗 | 檢查影像檔案 | 顯示「請先下載 Mona Lisa 範例」+ 提供 fallback 隨機 32×32 矩陣 |

#### I. 完成標準（Acceptance Criteria）

- [ ] 拉任意矩陣 $A$ 的元素 → SVD 即時更新（< 200ms 含 4 應用同步）；
- [ ] 秩 1 累加動畫流暢，每項拆解清晰可見；
- [ ] 2D 橢圓變形與 SVD 對齊，主軸方向 = $\mathbf{u}_p$、半徑 = $\sigma_p$；
- [ ] 4 應用切換無延遲，每個 demo 獨立運作；
- [ ] 4 子空間視覺整合 ch03 兩塊大餅圖正確，$A\mathbf{v}_p = \sigma_p \mathbf{u}_p$ 動畫對齊；
- [ ] Eckart–Young 誤差曲線正確，與理論值 $\sqrt{\sum_{p>k} \sigma_p^2}$ 一致；
- [ ] 4 個跨章跳轉按鈕（雙 pointer 主 + 副 + 4-Subspaces + EVD）參數正確帶入；
- [ ] 退化 / 長方 / 重複 / 全零 / Mona Lisa 載入失敗等邊界情況都正確處理。

#### J. 反例與常見誤解

- **誤解 1：** 「SVD 只適用方陣 / 可逆矩陣。」**正解：** SVD 適用**任意** $m \times n$ 矩陣，這是它與 EVD 最大的差異。長方陣、退化矩陣、全零矩陣都有 SVD；
- **誤解 2：** 「奇異值就是特徵值。」**正解：** 奇異值是 $A^{\mathrm{T}} A$ 特徵值的**平方根**（且強制非負）。對對稱正定矩陣：$\sigma_p = \lambda_p$；對對稱含負矩陣：$\sigma_p = |\lambda_p|$；對一般矩陣：兩者無直接關係；
- **誤解 3：** 「$U$ 和 $V$ 可以隨意選。」**正解：** $U$ 由 $AA^{\mathrm{T}}$ 特徵向量決定、$V$ 由 $A^{\mathrm{T}} A$ 特徵向量決定，兩者透過 $A\mathbf{v}_p = \sigma_p \mathbf{u}_p$ 連結。**只有重複奇異值情境下才有選擇自由**；
- **誤解 4：** 「PCA 必須先做共變異矩陣再做 EVD。」**正解：** 現代 PCA 都直接對置中資料 $\tilde{X}$ 做 SVD，不算 $\tilde{X}^{\mathrm{T}} \tilde{X}$（避免數值不穩 + 節省計算）；
- **誤解 5：** 「Eckart–Young 只說 Frobenius 範數。」**正解：** Eckart–Young 對 **Frobenius、譜（2-norm）、核（trace norm，所有 unitarily invariant norm**）都成立，是個非常強的最佳性定理。

#### K. 與其他 VizScript 的關係

- **本章 VizScript-02 / 03 / 04：** Tier 2 / Tier 1 精簡版分別處理奇異值降冪 / 4 子空間構造 / 2×2 數值 walkthrough；
- **ch04 VizScript-02 (MM4 + Mona Lisa SVD demo)：** **本 VizScript 的主 pointer + 「應用 1：壓縮」直接重用** — Mona Lisa demo 的低秩近似互動完全相容，本章 VizScript-01 在 Step 5 直接 embed 或跳轉；
- **ch05 VizScript-03 (P4 三明治)：** **本 VizScript 的副 pointer** — SVD 是 (P4) 的最一般情境，視覺布局共用「三明治」基本結構，但 SVD 強調「雙側獨立」，視覺顏色用綠 + 粉紅對比展示；
- **ch03 VizScript-02 (4-Subspaces 兩塊大餅圖)：** **本 VizScript 「顯示 4 子空間」mode 的整合對象** — SVD 直接給出 4 子空間的正交基底，與 ch03 VizScript-02 完美對接，視為「**SVD 是 4-Subspaces 的構造工具**」；
- **ch06e VizScript-01 (EVD)：** **本 VizScript 的「對稱情境跳轉」對象** — 範例 1 的 $A = \bigl[\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr]$ 是對稱的，SVD 退化為 EVD，跳轉到 ch06e VizScript-01 看對稱情境的譜分解；
- **後續：** S12+ 實作時，本 VizScript 是「**全書集大成的旗艦 demo**」 — 整合 ch03 + ch04 + ch05 + ch06e 五個前置 VizScript，完整實作後就有「**Linear Algebra 全書互動式視覺化教材**」的核心骨架。

#### L. 配套素材清單

- **必備：** Python 3.11+、NumPy（`linalg.svd`）、SciPy（PCA、矩陣補全）、matplotlib + plotly（2D/3D 幾何）、reactive UI 框架（marimo/streamlit）、Pillow（影像處理）；
- **可選：** scikit-learn（PCA 對照、Iris 資料集載入）、surprise（推薦系統矩陣補全標準庫）；
- **資料集：** Mona Lisa $400 \times 250$ 灰階影像（`mona_lisa.png`，從 ch04 重用）、Iris 資料集（150×4，scikit-learn 內建）、MovieLens 1M 評分資料（推薦系統，可選）；
- **教學素材：** 「SVD 4 大應用」一頁總覽圖卡 + 「Eckart–Young 定理」一頁公式卡 + 「PCA vs SVD 等價性」對照表；
- **未來擴展：** 「**隨機化 SVD**」（Halko–Martinsson–Tropp）demo、「**動態 SVD**」（即時更新）demo、「**張量分解**」（HOSVD）延伸介紹。

#### M. 預期使用者反饋

- **「終於懂了 SVD 為何是線代之王」：** 透過 4 應用同時展示，使用者建立「**SVD 是工程實務無所不在的工具**」直覺；
- **「Eckart–Young 原來這麼直觀」：** 透過秩 $k$ 截斷滑桿與誤差曲線，使用者體會「**捨棄最小 $\sigma_p$ = 最佳近似**」；
- **「PCA 不再神秘」：** 透過 Iris 散點圖降維 demo，使用者看到「**主成分 = 方差最大方向 = $V$ 的前 $k$ 列**」；
- **「4 子空間原來是 SVD 構造的」：** 透過與 ch03 兩塊大餅圖的整合，使用者理解「**SVD 是線代最完整的視覺定理**」；
- **「想做的都能做」：** 影像壓縮 / 降維 / 降噪 / 推薦四個應用各有獨立 demo，使用者離開時帶走「**SVD 工程實務工具箱**」；
- **「全書貫通」：** 透過雙 pointer + 4 子空間 + EVD 跨章跳轉，使用者建立「**§1–§6 全書 = 為了 SVD 鋪陳**」的整合視角，實現作者 Hiranabe 的「Art of Linear Algebra」原始意圖。

---

### VizScript-02: 奇異值降冪 + Eckart–Young 視覺（Tier 2）

**Tier：** ⭐⭐⭐ Tier 2（精簡版的旗艦演示，與 VizScript-01 並列）
**對應 VizMark：** Figure 6.7 VizMark-02
**預估實作工作量：** S12+ 約 1 session

#### A. 一句話定位

「給一個 $A$，顯示 bar chart 的 $\sigma_1 \geq \sigma_2 \geq \cdots$ + 累計能量曲線 + 滑桿選 $k$ 看截斷誤差，視覺化 Eckart–Young 定理。」

#### B. 學習目標

- 看 $\sigma_p$ 的「能量分布」（前幾項佔比）；
- 看「秩 $k$ 截斷」的最佳性（誤差 = $\sqrt{\sum_{p>k} \sigma_p^2}$）；
- 建立「**奇異值衰減快 → 適合低秩近似**」直覺。

#### C-M（精簡）

**布局：** 上方 $A$ 矩陣 + 中間 bar chart（$\sigma_p$ 藍長條 + 累計能量紅折線）+ 下方滑桿 $k$ + 右下重建 $A_k$ 預覽 + 誤差條。

**動畫：**
- 拉滑桿 $k$ → bar chart 上前 $k$ 個 bar 高亮綠色、後面變灰 → 重建 $A_k$ 即時更新 → 誤差條長度即時調整；
- 對 $A$ 改元素 → bar chart 即時重新計算 → 累計能量曲線重畫；
- Eckart–Young 公式 $\|A - A_k\|_F = \sqrt{\sum_{p > k} \sigma_p^2}$ 公式區同步顯示具體數字。

**用途：** 快速看「**該取多少 $k$ 才足夠**」 — 工程實務最常問的問題。預設範例可放 Mona Lisa（看奇異值衰減快不快、決定壓縮比）。

---

### VizScript-03: 4 子空間 SVD 構造（精簡）

**Tier：** ⭐⭐ Tier 1（精簡版，重用 ch03 VizScript-02 母模板）
**對應 VizMark：** Figure 6.7 VizMark-03
**預估實作工作量：** S12+ 約 0.5 session（重用 ch03 框架，只需加 SVD 連接層）

#### A. 一句話定位

「用 SVD 直接構造 4 子空間的正交基底，與 ch03 兩塊大餅圖整合：$\{\mathbf{v}_1, \ldots, \mathbf{v}_r\}$ 標行空間、$\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\}$ 標零空間、$\{\mathbf{u}_1, \ldots, \mathbf{u}_r\}$ 標列空間、$\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\}$ 標左零空間。」

#### B. 學習目標

- 看 SVD 與 4 子空間的「直接構造」關係；
- 看 $A \mathbf{v}_p = \sigma_p \mathbf{u}_p$ 的「**對齊映射**」動畫（左圓 → 右圓）；
- 整合 ch03 已實作的 4-Subspaces 視覺。

#### C-M（精簡，重用 ch03 框架）

**布局：** ch03 兩塊大餅圖（左 $\mathbb{R}^n$ + 右 $\mathbb{R}^m$）+ SVD 標記層（$\mathbf{u}_p, \mathbf{v}_p$ 顯示為各子空間正交基底向量）。

**動畫：**
- 對 $A$ 改元素 → 即時重新計算 SVD → 4 子空間基底向量即時更新（含維度變化）；
- 滑鼠 hover 任一個 $\mathbf{v}_p$（左圓）→ 對應 $\mathbf{u}_p$（右圓）高亮 + 標 $\sigma_p$；
- 點 $\mathbf{v}_p$ → 動畫展示 $A \mathbf{v}_p$（左 → 右映射）= $\sigma_p \mathbf{u}_p$（綠箭頭縮放動畫）。

---

### VizScript-04: 2×2 SVD 數值範例 walkthrough（輕量）

**Tier：** ⭐ Tier 1（輕量輪廓）
**對應 VizMark：** Figure 6.7 VizMark-04
**預估實作工作量：** S12+ 約 0.3 session

#### A. 一句話定位

「用 2×2 範例 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$（Strang 經典）一步一步動畫展示 SVD 計算過程。」

#### B-M（簡述）

**步驟動畫：**

1. 顯示 $A = \bigl[\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr]$；
2. 計算 $A^{\mathrm{T}} A = \bigl[\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\bigr]$；
3. 求特徵值：$\det(A^{\mathrm{T}} A - \lambda I) = (25-\lambda)^2 - 400 = 0 \Rightarrow \lambda = 45, 5$；
4. $\sigma_1 = \sqrt{45} = 3\sqrt{5} \approx 6.708$，$\sigma_2 = \sqrt{5} \approx 2.236$；
5. 求 $\mathbf{v}_1$：$(A^{\mathrm{T}} A - 45 I) \mathbf{v}_1 = \mathbf{0} \Rightarrow \mathbf{v}_1 = (1, 1)^{\mathrm{T}}/\sqrt{2}$；
6. 求 $\mathbf{v}_2$：$\mathbf{v}_2 = (1, -1)^{\mathrm{T}}/\sqrt{2}$；
7. 求 $\mathbf{u}_1 = A\mathbf{v}_1 / \sigma_1 = \frac{1}{3\sqrt{5}} \cdot \frac{1}{\sqrt{2}} \cdot \bigl[\begin{smallmatrix}3\\9\end{smallmatrix}\bigr] = \frac{1}{\sqrt{10}}(1, 3)^{\mathrm{T}}$；
8. 求 $\mathbf{u}_2 = A\mathbf{v}_2 / \sigma_2 = \frac{1}{\sqrt{5}} \cdot \frac{1}{\sqrt{2}} \cdot \bigl[\begin{smallmatrix}3\\-1\end{smallmatrix}\bigr] = \frac{1}{\sqrt{10}}(3, -1)^{\mathrm{T}}$；
9. 組裝 $U, \Sigma, V$ 並驗證 $U\Sigma V^{\mathrm{T}} = A$ ✓；
10. 譜分解 $A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}} + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^{\mathrm{T}}$ 計算每項 + 累加驗證。

**用途：** 入門教學，讓使用者第一次接觸 SVD 時看到完整計算過程的具體數字。**不含 4 應用、不含 4 子空間、不含 2D 幾何**，純步進動畫。

---

## 章末延伸

### 與 §1–§5 的來源對應

- **§1（Viewing a Matrix）：** SVD 統一了 4 視角 — $A = U\Sigma V^{\mathrm{T}}$ 同時給出列空間（$U$ 的前 $r$ 列）、行空間（$V$ 的前 $r$ 列）、列線性組合的座標系（$V^{\mathrm{T}}$）、行線性組合的座標系（$U$）；
- **§2（Vector × Vector）：** SVD 的 $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 是「v2 視角的最有意義版」（外積 + 奇異值加權 + 降冪排序）；
- **§3（Matrix × Vector）：** SVD 的「$A \mathbf{v}_p = \sigma_p \mathbf{u}_p$」是「**矩陣 × 向量**」的「**最特別的一組正交基底**」 — 把正交映射到正交（一般矩陣不會）；
- **§4（MM4）：** SVD 是 (MM4) 的「**最有意義版本**」 — 外積之和按貢獻度排序、可截斷得最佳低秩近似（Eckart–Young）；**ch04 VizScript-02 的 Mona Lisa SVD demo 就是 SVD 章的核心預告片**；
- **§5（P4）：** **`SVD.png` 直接標 `using P4`**，SVD 是 (P4) 三明治的「**雙側獨立 + 對角非負**」最一般情境；
- **§3 4-Subspaces：** SVD 直接給出 4 子空間的正交基底（$\mathbf{v}_p$ 標行空間 / 零空間，$\mathbf{u}_p$ 標列空間 / 左零空間），**整合 ch03 VizScript-02 兩塊大餅圖完整 demo**。

### 與 §6 其他分解的對應

- **§6.1 CR：** CR 給出「列空間基底」，SVD 給出「**正交**列空間基底」 — SVD 是 CR 的正交化升級；
- **§6.2 LU：** LU 解 $A\mathbf{x} = \mathbf{b}$（限方陣），SVD 解 $A\mathbf{x} = \mathbf{b}$（**任意矩陣 + Moore–Penrose 偽反**）；
- **§6.3 QR：** QR 是「列正交化」，SVD 是「**雙側正交化**」；數值上 SVD 算法常以 QR 為中間步驟；
- **§6.4 EVD：** EVD 限對稱、$U = V$；SVD 任意矩陣、$U \neq V$。**$A^{\mathrm{T}} A$ EVD 給 $V, \Sigma^2$；$AA^{\mathrm{T}}$ EVD 給 $U, \Sigma^2$。SVD = 兩個對稱半正定矩陣 EVD 的整合**。

### §6 五大分解的視覺指紋總結（本章為終章）

| 分解 | PNG `using` 標記 | 視覺指紋 | 適用矩陣 |
|---|---|---|---|
| $A = CR$ | CR1 標 P1 / CR2 標 P2 | 對偶兩張圖（列視角 + 行視角） | 任意 |
| $A = LU$ | LU1 無標 / LU2 標 MM4 | peeling 逐層楔形 + (MM4) 累加 | 可 LU 分解 |
| $A = QR$ | QR 標 P1 | 綠色直立列（正交基底）+ 藍點上三角 | 列獨立 |
| $S = Q\Lambda Q^{\mathrm{T}}$ | EVD 標 P4 | **左 = 右轉置（鏡像對稱）** + 對角藍點 | **限對稱** |
| $A = U\Sigma V^{\mathrm{T}}$ | SVD 標 P4 | **左綠 + 右粉紅（雙側獨立）** + 對角藍點 + 項數 = 秩 | **任意（無限制）** |

**結論：** §6 五大分解的視覺指紋透過「**`using XX` 標記 + 顏色對比 + 結構元素**」三層編碼，每張 PNG 都是「**自含的視覺定理**」。原書作者 Hiranabe 用 `using XX` 標記建立跨章索引網路（見 ch06a-five.md 升級鏈圖），**S07–S09 三 session 的 PNG 重核工作確立了這個索引網路的完整地圖**。

### 工程應用前瞻（S12+ 實作目標，本章最豐富）

#### 影像 / 訊號處理

- **Mona Lisa SVD 壓縮 demo**（ch04 VizScript-02 + 本章 VizScript-01 整合）；
- **JPEG 壓縮的 SVD 對照**（DCT vs SVD 比較，看 SVD 為何理論最佳但實務用 DCT）；
- **影像降噪 demo**（雜訊正弦波 + SVD 截斷，可加 wavelet 對照）；
- **去模糊 demo**（Tikhonov 正則化 + SVD 截斷，醫學影像應用）。

#### 資料科學

- **Iris PCA demo**（4D → 2D 降維 + 三類別分離視覺化）；
- **MNIST 手寫數字 PCA**（784D → 2D 視覺化 10 類別分布）；
- **Eigenfaces demo**（人臉資料庫 SVD → 特徵臉視覺化）；
- **基因表達分析 PCA**（生醫應用，可選）。

#### 推薦系統

- **MovieLens 推薦 demo**（用戶 × 電影評分矩陣補全）；
- **Netflix Prize 簡化版**（介紹 SVD++、ALS 等變體）；
- **協同過濾 vs 矩陣補全**對照演示。

#### 數值線性代數

- **Moore–Penrose 偽反 demo**（最小二乘解 + SVD 構造）；
- **條件數視覺化** $\kappa(A) = \sigma_1 / \sigma_r$（看奇異值差距如何影響數值穩定性）；
- **隨機化 SVD demo**（Halko–Martinsson–Tropp 算法，大矩陣加速）。

#### 機器學習

- **線性回歸 SVD 求解**（替代正規方程的數值穩定方法）；
- **嶺回歸 SVD 視覺化**（正則化參數對奇異值的縮減效果）；
- **核 PCA**（kernel PCA 介紹 + SVD 在核空間的對應）。

### 本章在全書架構中的定位（總結）

- **理論定位：** §6 五大分解的**最後一個 + 最完整的一個** — 同時滿足「適用最廣（任意矩陣）+ 結構最強（雙側正交對角）+ 應用最多（4 大旗艦應用）+ 直接連接 4 子空間（Strang 兩塊大餅圖）+ 最佳低秩近似（Eckart–Young）」五個指標；
- **VizScript 規格：** **全書唯一的 Tier 3 主 VizScript** — VizScript-01 預估 3 session（與 ch04 VizScript-02 同級），整合 4 應用 + 4 子空間 + 2D 幾何 + Mona Lisa demo；
- **跨章 pointer 設計：** **全書唯一的雙 pointer 主 + 副設計** — 主 pointer 指 ch04 VizScript-02 (MM4 + Mona Lisa)，副 pointer 指 ch05 VizScript-03 (P4)；
- **教學定位：** **§1–§6 全書的「集大成 + 工程化」終章** — 使用者完成本章後應建立「線性代數 = 為了 SVD 鋪陳，SVD = 工程實務的瑞士刀」的整合視角；
- **S12+ 實作優先順序：** **VizScript-01 是全書最值得實作的 demo，預估 3 session 但回報極高** — 完成後即可宣稱「**互動式 Linear Algebra 教材的核心骨架完成 80%**」。

### 來源對照

| 元素 | 來源 |
|---|---|
| 數學公式 | `from-tex/en.md` line 507–569、`from-tex/zh.md` line 494–558 |
| 圖片 | `figs-png/SVD.png`（原始 EPS：`figs/SVD.eps`，原書 p.12）|
| Strang 連結 | LA for Everyone Sec. 7.1（奇異值與奇異向量）、Sec. 7.2（Eckart–Young 定理）|
| Pattern 連結 | §5 (P4) 三明治，本書 PNG 直接標 `using P4` |
| (MM4) 連結 | §4 (MM4) 外積之和，SVD 是「按 $\sigma_p$ 降冪排序的最有意義版」 |
| 4 子空間連結 | §3 4-Subspaces，SVD 直接給出 4 子空間正交基底 |
| 跨章 pointer（**雙 pointer**，全書唯一） | **主 pointer：** [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) (MM4 + Mona Lisa) / **副 pointer：** [ch05 VizScript-03](ch05-patterns.md#vizscript-03) (P4 三明治) / **整合 pointer：** [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) (4-Subspaces) / **對偶 pointer：** [ch06e VizScript-01](ch06e-QLQ.md#vizscript-01) (EVD) |
| Eckart–Young 定理 | Eckart, C., & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika* 1: 211–218 |
| Mona Lisa demo 影像 | `ch04 VizScript-02 配套素材` 重用 |
| Iris 資料集 | scikit-learn 內建（`sklearn.datasets.load_iris()`）|
