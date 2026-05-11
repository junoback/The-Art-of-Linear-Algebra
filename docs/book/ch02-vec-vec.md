# 第 2 章. 向量乘以向量 — 兩種視角（Vector × Vector — 2 Ways）

> **原書頁碼：** p.2
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 49–67 行
> **本章圖數：** 1
> **本章 VizMark 數：** 2（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 0）
> **狀態：** [x] 已完成 / [ ] 校對中

---

## 章節摘要

兩個向量相乘，依方向不同會產出兩種**完全不同尺寸**的結果。**(v1) 點積 (dot product)** 是「行向量 × 列向量 = 一個數字」，把兩個向量的對應分量乘起來再加總，結果是純量。**(v2) 外積 (outer product)** 是「列向量 × 行向量 = 一個矩陣」，產出的不是數字而是一整個**秩 1 矩陣 (rank 1 matrix)**，這個矩陣的每一列都是 $\mathbf{a}$ 的倍數，每一行都是 $\mathbf{b}^{\mathrm{T}}$ 的倍數。

(v1) 是讀者早就熟悉的初等運算；(v2) 才是本書的關鍵 — 它是 §6 五大矩陣分解（CR / LU / QR / $Q\Lambda Q^{\mathrm{T}}$ / $U\Sigma V^{\mathrm{T}}$）的共同骨架，因為任何矩陣都可以寫成若干個秩 1 矩陣（外積）之和。本章只看 1 張圖，但這張圖建立的「**外積 = 秩 1 矩陣**」直覺，會在後續每一章都用到。

> ⚠ **術語提醒（沿用 §1 全書慣例）：** column = 列（直立、綠色）、row = 行（橫躺、粉紅色）。本章兩個視角的「方向」是核心 — **(v1)** 是「橫躺 × 直立」（夾住中間像三明治）、**(v2)** 是「直立 × 橫躺」（外撐開像漢堡）。記住這個對比，後面所有矩陣乘法視角都能秒判斷產物是純量還是矩陣。

---

## 數學要點

兩個向量 $\mathbf{a} \in \mathbb{R}^m$、$\mathbf{b} \in \mathbb{R}^m$（或 $\mathbf{b} \in \mathbb{R}^n$，視運算而定），有兩種「相乘」方式：

### (v1) 點積 / 內積（Dot Product / Inner Product）

$$
\mathbf{a} \cdot \mathbf{b}
\;=\;
\mathbf{a}^{\mathrm{T}} \mathbf{b}
\;=\;
\begin{bmatrix} a_1 & a_2 & \cdots & a_m \end{bmatrix}
\begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix}
\;=\;
\sum_{k=1}^{m} a_k b_k
\;\in\; \mathbb{R}
$$

- **維度約束：** $\mathbf{a}$ 與 $\mathbf{b}$ 必須在同一個 $\mathbb{R}^m$。
- **形狀運算：** $(1 \times m)(m \times 1) = (1 \times 1)$，結果是純量。
- **原書 (v1) 範例：**

$$
\begin{bmatrix} 1 & 2 & 3 \end{bmatrix}
\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
=
\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \cdot \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
= x_1 + 2x_2 + 3x_3
$$

### (v2) 外積（Outer Product）→ 秩 1 矩陣

$$
\mathbf{a} \mathbf{b}^{\mathrm{T}}
\;=\;
\begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_m \end{bmatrix}
\begin{bmatrix} b_1 & b_2 & \cdots & b_n \end{bmatrix}
\;=\;
\begin{bmatrix}
a_1 b_1 & a_1 b_2 & \cdots & a_1 b_n \\
a_2 b_1 & a_2 b_2 & \cdots & a_2 b_n \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_m b_1 & a_m b_2 & \cdots & a_m b_n
\end{bmatrix}
\;\in\; \mathbb{R}^{m \times n}
$$

- **維度約束：** $\mathbf{a}$ 與 $\mathbf{b}$ 可以住在**不同維度**的空間（$\mathbf{a} \in \mathbb{R}^m$、$\mathbf{b} \in \mathbb{R}^n$）。
- **形狀運算：** $(m \times 1)(1 \times n) = (m \times n)$，結果是矩陣。
- **秩：** 只要 $\mathbf{a} \ne \mathbf{0}$ 且 $\mathbf{b} \ne \mathbf{0}$，$\operatorname{rank}(\mathbf{a}\mathbf{b}^{\mathrm{T}}) = 1$。
- **結構觀察：** 矩陣的第 $j$ 直立列等於 $b_j \mathbf{a}$（$\mathbf{a}$ 的純量倍數）；第 $i$ 橫躺行等於 $a_i \mathbf{b}^{\mathrm{T}}$（$\mathbf{b}^{\mathrm{T}}$ 的純量倍數）。**所有列彼此平行、所有行彼此平行** — 這就是秩 1 的視覺意涵。
- **原書 (v2) 範例：**

$$
\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
\begin{bmatrix} x & y \end{bmatrix}
=
\begin{bmatrix}
x & y \\
2x & 2y \\
3x & 3y
\end{bmatrix}
$$

### 對偶關係（v1 ↔ v2）

把同樣的兩個直立向量 $\mathbf{a}, \mathbf{b} \in \mathbb{R}^m$，**夾住中間（v1）** vs **撐到外面（v2）**，就決定產物是純量還是矩陣：

$$
\underbrace{\mathbf{a}^{\mathrm{T}} \mathbf{b}}_{\text{純量}\; \in \mathbb{R}}
\quad\text{vs}\quad
\underbrace{\mathbf{a}\, \mathbf{b}^{\mathrm{T}}}_{\text{矩陣}\; \in \mathbb{R}^{m \times m}}
$$

這個「夾 / 撐」對比是本章視覺化最值得做動畫的點（見 VizMark-02）。

### 對應原書章節（Strang《Linear Algebra for Everyone》）

- Sec. 1.1 (p.2) Linear combination and dot products — 對應 (v1)
- Sec. 1.3 (p.25) Matrix of Rank One — 對應 (v2)
- Sec. 1.4 (p.29) Row way and column way — (v1) 與 (v2) 的對偶引子

---

## 圖片區

### Figure 2.1: 向量乘以向量的兩種視角（Vector × Vector — (v1), (v2)）

**圖檔：** `docs/book/figs-png/VectorTimesVector.png`（原始 EPS：`figs/VectorTimesVector.eps`）
**原書頁碼：** p.2
**所屬章節：** §2

#### 視覺結構 (Visual Structure)

此圖採「左右並列兩區」結構，左半 (v1) 點積、右半 (v2) 外積，各區由「**抽象色塊示意（上）+ 具體數字範例（下）**」兩層組成。

- **左半：(v1) 點積**
  - 左上角小灰圈內標 `v1`，標示此區編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **粉紅色橫條** —— 行向量（row vector，橫躺）。
    2. **綠色直條** —— 列向量（column vector，直立）。
    3. **粉紅與綠重疊成的小方塊** —— 表示對應分量相乘逐項堆疊。
    4. **單一藍色實心圓點** —— 一個純量（數字）。
    5. 右側標註文字：`Dot product (number)`。
  - 抽象示意下方文字：**"Dot product (a·b) is expressed as $\mathbf{a}^{\mathrm{T}}\mathbf{b}$ in matrix language and yields a number."**
  - 具體範例（最下方）：
    $$\begin{bmatrix} 1 & 2 & 3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \cdot \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = x_1 + 2x_2 + 3x_3$$
- **右半：(v2) 外積 → 秩 1 矩陣**
  - 左上角小灰圈內標 `v2`，標示此區編號。
  - 抽象示意（由左至右以 `=` 連接）：
    1. **綠色直條** —— 列向量（column vector，直立）。
    2. **粉紅色橫條** —— 行向量（row vector，橫躺）。
    3. **完整方塊**：上緣一條粉紅橫條（標記第一橫躺行的來源）、左緣一條綠直條（標記第一直立列的來源）、其餘以淺灰填滿（表示矩陣其他元素都由兩者乘積決定）。
    4. **6 個藍色實心圓點**排成 $3 \times 2$ 網格 —— 表示產出的秩 1 矩陣有 6 個元素，但只有 1 個自由度。
    5. 右側標註文字：`Rank 1 Matrix`。
  - 抽象示意下方文字：**"$\mathbf{a}\mathbf{b}^{\mathrm{T}}$ is a matrix ($\mathbf{a}\mathbf{b}^{\mathrm{T}} = A$). If neither $a, b$ are 0, the result $A$ is a rank 1 matrix."**
  - 具體範例（最下方）：
    $$\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}\begin{bmatrix} x & y \end{bmatrix} = \begin{bmatrix} x & y \\ 2x & 2y \\ 3x & 3y \end{bmatrix}$$
- **配色語意（沿用 §1）：** 綠 = 列向量 / 直立、粉紅 = 行向量 / 橫躺、藍點 = 個別數字、灰 = 結構填充。
- **左右兩區的形狀對比：** (v1) 結果端只有一個藍點（純量），(v2) 結果端是 $3 \times 2$ 共 6 個藍點的矩形（矩陣）。這個「端點圖形的大小差」是讀者要一眼讀懂的核心訊息。

讀者的視覺動線：先看左半 (v1) 確認「點積 = 一個數」這個熟悉概念 → 跳到右半 (v2) 注意端點從「一個點」變成「一塊矩陣」 → 對比兩個抽象示意的開頭：(v1) 是「粉紅 × 綠」、(v2) 是「綠 × 粉紅」順序顛倒 → 連結到下方具體範例驗證。

#### 數學內容 (Mathematical Content)

圖中演示的兩個運算：

**(v1) 點積：**

$$
\mathbf{a}^{\mathrm{T}} \mathbf{b}
= \begin{bmatrix} 1 & 2 & 3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}
= x_1 + 2x_2 + 3x_3 \in \mathbb{R}
$$

其中：

$$
\mathbf{a} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix},\;
\mathbf{b} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \in \mathbb{R}^3
$$

**(v2) 外積：**

$$
\mathbf{a}\, \mathbf{b}^{\mathrm{T}}
= \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \begin{bmatrix} x & y \end{bmatrix}
= \begin{bmatrix} x & y \\ 2x & 2y \\ 3x & 3y \end{bmatrix} \in \mathbb{R}^{3 \times 2}
$$

其中：

$$
\mathbf{a} = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix} \in \mathbb{R}^3,\;
\mathbf{b} = \begin{bmatrix} x \\ y \end{bmatrix} \in \mathbb{R}^2
\;\Rightarrow\;
\mathbf{b}^{\mathrm{T}} = \begin{bmatrix} x & y \end{bmatrix}
$$

**秩驗證：** $\det\begin{bmatrix} x & y \\ 2x & 2y \end{bmatrix} = 2xy - 2xy = 0$；任兩個直立列 $(x, 2x, 3x)^{\mathrm{T}}$ 與 $(y, 2y, 3y)^{\mathrm{T}}$ 皆為 $\mathbf{a} = (1,2,3)^{\mathrm{T}}$ 的純量倍數 $x \cdot \mathbf{a}$、$y \cdot \mathbf{a}$，所以**列空間 (column space) 只有 1 維**，$\operatorname{rank} = 1$。

**維度檢核（最常出錯處）：**
- (v1) 內外都是 $\mathbb{R}^3$，能夠相乘是因為 $(1 \times 3)(3 \times 1) = (1 \times 1)$ 的中間維度 3 對得起來。
- (v2) $\mathbf{a} \in \mathbb{R}^3$、$\mathbf{b} \in \mathbb{R}^2$，**兩個向量本來不在同一空間也沒關係** — 外積要的是「外面」的維度 $m=3$ 與 $n=2$ 各自當行 / 列數，「中間」的維度恆為 1。

#### 直覺解讀 (Intuition)

**1. 「方向」決定結果是純量還是矩陣。** 同樣兩個直立列向量 $\mathbf{a}, \mathbf{b} \in \mathbb{R}^m$，把哪一個轉置（變橫躺）會徹底改變結果尺寸：
- 第一個轉置成橫躺（$\mathbf{a}^{\mathrm{T}} \mathbf{b}$）→ 「橫躺夾住直立」→ 結果壓縮成 1 個數字。
- 第二個轉置成橫躺（$\mathbf{a} \mathbf{b}^{\mathrm{T}}$）→ 「直立撐開橫躺」→ 結果擴張成 $m \times m$ 矩陣。

可以記成「**夾 (clamp) → 純量**、**撐 (extend) → 矩陣**」。

**2. 秩 1 矩陣的「平行性」結構。** $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 的每一直立列都是 $\mathbf{a}$ 的純量倍數（係數來自 $\mathbf{b}$）、每一橫躺行都是 $\mathbf{b}^{\mathrm{T}}$ 的純量倍數（係數來自 $\mathbf{a}$）。這意味著：
- **列空間 (column space) 是一條過原點的直線**：$\operatorname{span}\{\mathbf{a}\} \subset \mathbb{R}^m$。
- **行空間 (row space) 也是一條過原點的直線**：$\operatorname{span}\{\mathbf{b}\} \subset \mathbb{R}^n$。
- 這就是「rank 1」的幾何畫面 — 不是兩條獨立方向，而是「一條方向（$\mathbf{a}$）被縮放後在不同位置複製」的結構。

**3. 為何 (v2) 是後續章節的鑰匙。** 全書 §6 的五大矩陣分解，看似分別在做不同的事，但本質都是把矩陣寫成**若干個秩 1 矩陣的和**：

$$
A = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^{\mathrm{T}} + \sigma_2 \mathbf{u}_2 \mathbf{v}_2^{\mathrm{T}} + \cdots + \sigma_r \mathbf{u}_r \mathbf{v}_r^{\mathrm{T}}
\quad\text{(SVD 的最終形式)}
$$

QR、LU、$Q\Lambda Q^{\mathrm{T}}$ 也都能寫成類似的「秩 1 矩陣加總」形式。若 (v2) 沒讀通，後續章節會覺得每個分解都是「魔術公式」；讀通後，會看出它們都是同一個外積框架的變奏。

**4. 點積與內積的詞彙混用。** 在 $\mathbb{R}^m$ 上、實數係數時，"dot product" 與 "inner product" 指同一件事（$\sum a_k b_k$）。在更廣義的內積空間裡兩者才有區別（內積會加共軛或加權），但本書全程在 $\mathbb{R}^m$ 上，可視為同義詞。

**常見誤解警示：**
- **$\mathbf{a}^{\mathrm{T}}\mathbf{b}$ 與 $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 不可互換** — 前者是 $1 \times 1$ 純量，後者是 $m \times n$ 矩陣，差異不只是寫法。
- **「外積」一詞在不同教材有不同意思** — 本書（與 Strang）指的是 $\mathbf{a}\mathbf{b}^{\mathrm{T}}$（產生矩陣）；某些物理 / 幾何脈絡用「外積」指 cross product $\mathbf{a} \times \mathbf{b}$（產生向量，限 $\mathbb{R}^3$）。本書內 outer product 一律指**矩陣產出**。
- **秩 1 矩陣不一定每個元素都非零** — 若 $\mathbf{a}$ 或 $\mathbf{b}$ 有某個分量為 0，對應的整列 / 整行就是 0，但只要兩向量都非零向量，整個矩陣的秩仍是 1（不會是 0）。

**為什麼這張圖該做成互動視覺化？** 因為「夾 vs 撐」、「拉某個分量導致整列 / 整行同步縮放」這類概念是動態的 — 讀者拉動 $\mathbf{a}, \mathbf{b}$ 的分量值，看著秩 1 矩陣的所有列同步等比例變化，會直接「看到」rank 1 的視覺意涵；這是靜態圖永遠做不到的事（見 VizMark-01）。另外 (v1) ↔ (v2) 的視角切換動畫，能把「同樣兩個向量、轉置誰決定產物尺寸」這個對偶結構在 1 秒內演完（見 VizMark-02）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [拉桿調參] ⭐⭐⭐
> **位置：** Figure 2.1 / §2 / (v2) 外積區
> **核心概念：** 外積 $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 產生秩 1 矩陣，**每列彼此平行、每行彼此平行**
> **互動梗概：** 拉 $\mathbf{a}, \mathbf{b}$ 各分量 slider，矩陣 6 格即時重算 + 高亮顯示「此列是 $\mathbf{a}$ 的幾倍」「此行是 $\mathbf{b}^{\mathrm{T}}$ 的幾倍」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [切換視角] ⭐⭐
> **位置：** Figure 2.1 / §2 / (v1) ↔ (v2) 對偶
> **核心概念：** 同樣兩個直立向量，轉置誰決定產物是純量 (v1) 還是秩 1 矩陣 (v2)
> **互動梗概：** toggle 切換 (v1) / (v2)，畫面演動畫「橫躺向量在左 vs 在右」的位移與結果端點的大小變化
> **詳見劇本：** VizScript-02（章末）

---

## 視覺化劇本（VizScripts）

> 本章兩個 VizMark 對應兩個 VizScript。格式遵 `VIZ_SCHEMA.md` §2（A–M 共 13 段）。
> 兩個劇本實作時可合成單一視覺化頁面（共用控制列、共用畫布），不必拆兩支獨立程式。

### VizScript-01: 外積與秩 1 矩陣（Outer Product → Rank 1 Visualizer）

#### A. 一句話定位
讓使用者拉動兩個向量的分量，即時看「列向量 × 行向量 = 秩 1 矩陣」的所有元素同步等比例變化。

#### B. 學習目標（Learning Outcome）
- 使用者能說出「外積產出 $m \times n$ 矩陣，秩永遠是 1」（除非有零向量）。
- 使用者能在腦中預測：若把 $\mathbf{a}$ 的第 2 分量乘以 2，矩陣的哪些 cell 會變、變成多少。
- 使用者能指認「每直立列都是 $\mathbf{a}$ 的純量倍數」、「每橫躺行都是 $\mathbf{b}^{\mathrm{T}}$ 的純量倍數」這兩種平行結構。
- 使用者能透過視覺驗證「列空間是 $\operatorname{span}\{\mathbf{a}\}$ 一維直線」這個敘述。
- 使用者能理解「為何 $\mathbf{a}$ 或 $\mathbf{b}$ 任一為零時 rank 變 0、否則恆為 1」。

#### C. 待視覺化的數學物件
- **物件清單：** 列向量 $\mathbf{a} \in \mathbb{R}^m$、行向量 $\mathbf{b}^{\mathrm{T}} \in \mathbb{R}^{1 \times n}$（內部以列向量 $\mathbf{b} \in \mathbb{R}^n$ 儲存）、外積矩陣 $A = \mathbf{a}\mathbf{b}^{\mathrm{T}} \in \mathbb{R}^{m \times n}$。
- **預設值：** $\mathbf{a} = (1, 2, 3)^{\mathrm{T}}$、$\mathbf{b} = (x, y)^{\mathrm{T}} = (1, 1)^{\mathrm{T}}$（與原書一致；$x = y = 1$ 起始讓 cell 初值就是 $\mathbf{a}$ 的整數倍，易觀察）。
- **維度範圍：** $m \in [2, 6]$、$n \in [2, 6]$。
- **數值範圍：** $a_i, b_j \in [-9, 9]$ 步進 1（與 §1 一致）。
- **退化情形：**
  - **任一向量全零** → 矩陣全零、$\operatorname{rank} = 0$；右側資訊框紅字警示「rank = 0（至少一向量為零）」。
  - **某分量為 0** → 對應整列 / 整行為 0，但 rank 仍 = 1；該整列 / 整行以淺灰底標示。
  - **$\mathbf{a} = \mathbf{b}$ 且 $m = n$** → $A = \mathbf{a}\mathbf{a}^{\mathrm{T}}$ 是對稱秩 1 矩陣；額外顯示 "symmetric rank 1" 標籤。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 左 30% 向量輸入區（兩個向量 slider + 數值顯示）、中 45% 主畫面外積矩陣、右 25% 資訊區（公式 + rank + 平行性檢視）。
- **主畫面尺寸：** 600 × 480 px，白底；cell 60×60 px 視 $m, n$ 自動縮放。
- **向量輸入區布局：**
  - 上半：**列向量 $\mathbf{a}$**（綠色直條，$m$ 個 slider 縱向排列，每個 slider 旁顯示當前值）。
  - 下半：**行向量 $\mathbf{b}^{\mathrm{T}}$**（粉紅色橫條，$n$ 個 slider 橫向排列，每個 slider 上方顯示當前值）。
  - 視覺位置呼應外積式：$\mathbf{a}$ 在左（外積結果矩陣的左側）、$\mathbf{b}^{\mathrm{T}}$ 在上（結果矩陣的上方）。
- **主畫面內容：** $m \times n$ 矩陣 cell 網格，每 cell 顯示計算結果 $a_i \cdot b_j$；左側 cell 邊緣對齊 $\mathbf{a}$ slider、上側 cell 邊緣對齊 $\mathbf{b}^{\mathrm{T}}$ slider。
- **資訊區內容：** 公式 $A = \mathbf{a}\mathbf{b}^{\mathrm{T}}$ 即時用當前值渲染（MathJax）、`rank(A) = 1`（紅色字當為 0、綠色字當為 1）、「平行性檢視」radio（off / 顯示列平行 / 顯示行平行）。
- **配色（hex）：**
  - $\mathbf{a}$ 區域與「列平行」高亮：`#2ca02c`（綠，alpha 0.4 底）
  - $\mathbf{b}^{\mathrm{T}}$ 區域與「行平行」高亮：`#d62728`（粉紅，alpha 0.4 底；實際偏紅但呼應 §1）
  - 矩陣 cell 文字：`#000000` 16pt monospace
  - 零分量導致的整列 / 整行：淡灰底 `#eeeeee`
  - rank = 0 警示：紅字 `#cc0000`、rank = 1 正常：綠字 `#1a8a1a`
- **字型 / 字級：** 公式區 16pt MathJax；矩陣 cell 16pt monospace；slider 標籤 12pt sans。
- **邊距：** 上下左右各 20px、cell 間距 4px、輸入區與主畫面間距 24px。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| $m$ | slider | [2, 6] step 1 | 3 | 即時 |
| $n$ | slider | [2, 6] step 1 | 2 | 即時 |
| $a_i$ ($i=1\ldots m$) | slider 縱排 | [-9, 9] step 1 | $(1,2,3,\ldots)$ | 即時 |
| $b_j$ ($j=1\ldots n$) | slider 橫排 | [-9, 9] step 1 | $(1, 1, \ldots)$ | 即時 |
| 平行性檢視 | radio (3) | off / 列平行 / 行平行 | off | 即時 |
| 重設 | button | — | — | click → 還原預設 |

#### F. 輸出畫面細節（Outputs）
- **每 cell 即時顯示：** $a_i \cdot b_j$ 的乘積（整數運算，無浮點誤差）。
- **「列平行」模式：** 每一直立列被綠色色塊覆蓋，並在列底顯示 `= $b_j$ × $\mathbf{a}$`；hover 某列時其他列半透明 0.3 凸顯。
- **「行平行」模式：** 每一橫躺行被粉紅色色塊覆蓋，並在行右顯示 `= $a_i$ × $\mathbf{b}^{\mathrm{T}}$`；hover 某行時其他行半透明 0.3。
- **公式區即時更新：**
  $$A = \begin{bmatrix} a_1 \\ \vdots \\ a_m \end{bmatrix} \begin{bmatrix} b_1 & \cdots & b_n \end{bmatrix} = \begin{bmatrix} a_1 b_1 & \cdots & a_1 b_n \\ \vdots & \ddots & \vdots \\ a_m b_1 & \cdots & a_m b_n \end{bmatrix}$$
  以實際數字渲染。
- **rank 顯示：** `rank(A) = ` + 由 `numpy.linalg.matrix_rank(A, tol=1e-9)` 計算的值（恆 0 或 1）。

#### G. 互動行為（Interactions）
- **拉動 $a_i$ slider：** 該 cell 列（第 $i$ 橫躺行）整列即時重算；若處於「行平行」模式，該行整體縮放動畫 200ms。
- **拉動 $b_j$ slider：** 第 $j$ 直立列整列即時重算；若處於「列平行」模式，該列整體縮放動畫 200ms。
- **hover cell $(i, j)$：** 該 cell 加粗外框；tooltip 顯示 `A[${i}][${j}] = ${a_i}} × ${b_j} = ${a_i * b_j}`。
- **click cell $(i, j)$：** 該 cell 持續高亮 + 同時把 $a_i$ slider 與 $b_j$ slider 兩條控制端標出紅圈，視覺連結「這格的值來自這兩個 slider」。
- **快捷鍵：** `R` 切到「列平行」、`C` 切到「行平行」、`O` 關閉、`0` 把所有 slider 歸零（演示 rank = 0）。

#### H. 動畫腳本（平行性高亮淡入）
- **t=0–200ms:** radio 切到「列平行」時，全矩陣各直立列從無背景到綠色底 alpha 0 → 0.4 漸入，「= $b_j$ × $\mathbf{a}$」標籤從下方滑入。
- **t=200ms 後:** 穩態，等待 hover 或下次切換。
- **總長度：** 200ms。
- **緩動：** ease-out（CSS cubic-bezier(0, 0, 0.2, 1)）。
- **暫停 / 倒轉：** 否。

#### I. 邊界與錯誤處理
- **$\mathbf{a} = \mathbf{0}$ 或 $\mathbf{b} = \mathbf{0}$：** 全矩陣 cell 變灰、文字置中顯示 `0`；右側 rank 紅字「rank = 0」；公式區下方紅字提示「至少一向量為零，外積退化」。
- **某 $a_i = 0$：** 第 $i$ 橫躺行整行淡灰底，cell 仍顯示 `0`；rank 仍 = 1，提示「第 $i$ 行為零，但 rank 維持 1」。
- **$m = n = 6$ 最大：** cell 縮為 48×48 px、字級 14pt、slider 較密；動畫禁用避免頓。
- **$m = n = 2$ 最小：** cell 增為 80×80 px，slider 標籤字級放大 14pt。
- **使用者拖動 slider 過快：** debounce 30ms 避免重畫風暴。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - $a_i$ slider：「列向量 $\mathbf{a}$ 的第 $i$ 個分量（直立綠色那條）」
  - $b_j$ slider：「行向量 $\mathbf{b}^{\mathrm{T}}$ 的第 $j$ 個分量（橫躺粉紅那條）」
  - 平行性 radio：「打開後可看到外積結果矩陣的所有直立列彼此平行（或所有橫躺行彼此平行），這就是 rank 1 的視覺意涵」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「左邊是直立列向量 $\mathbf{a}$，上面是橫躺行向量 $\mathbf{b}^{\mathrm{T}}$」
  - Step 2：「中間每個 cell 是對應的 $a_i \times b_j$」
  - Step 3：「按右下『列平行』，看到每一直立列其實是 $\mathbf{a}$ 的不同倍數」
  - Step 4：「拉 $\mathbf{a}$ 任一分量，看到對應整橫躺行同步縮放 — 這就是 rank 1」
  - Step 5：「拉到所有 $a_i = 0$，rank 變 0，外積退化」
- **常見誤解警示：** 「rank 1 不代表只有 1 個非零元素 — 是 1 個自由度（一條方向被複製）」
- **延伸閱讀：** 原書 p.2 §2、本專案 `ch02-vec-vec.md`、Strang LAFE Sec. 1.3 (p.25) Matrix of Rank One。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo（反應式 notebook）+ matplotlib（2D 矩陣繪製）+ marimo.ui（控制元件）
- **替代方案：** Streamlit + Plotly heatmap（如需網頁分享，平行性高亮用 `go.Heatmap` + `shapes` 疊圖）
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫 cell + 色塊
  - `matplotlib.text.Text` 放數字 + 公式（公式用 `r"$...$"`）
  - `marimo.ui.slider`、`marimo.ui.radio`、`marimo.ui.button`
  - `numpy.outer(a, b)` 計算外積、`numpy.linalg.matrix_rank` 計算秩
- **檔案結構：**
  ```
  viz/
    ch02_outer_product.py        # 主入口（含 VizScript-01 與 02 共用畫面）
    _common/
      palette.py                 # 沿用 §1 配色（綠 #2ca02c / 粉紅 #d62728 / 灰）
      vector_canvas.py           # 直立列與橫躺行的繪圖工具（給 §3+ 重用）
  ```
- **效能：** 拉 slider 時用 `ax.clear()` 重畫 cell + 文字即可；勿在每次更新時 `plt.figure()`。建議在 `marimo.cache` 包住 `numpy.outer` 計算（雖然很快，但維持模式一致）。
- **測試：** snapshot test：預設值矩陣輸出 + rank = 0 退化情況 + symmetric ($\mathbf{a} = \mathbf{b}$) 情況各 1 張 PNG，CI 比對。

#### L. 驗收標準（Acceptance Criteria）
- [ ] $\mathbf{a}, \mathbf{b}$ 各分量 slider 拉動後，矩陣 cell 重算 < 100ms 完成。
- [ ] 「列平行」模式高亮正確：所有直立列皆同色綠底，且 hover 某列時其他列半透明。
- [ ] 「行平行」模式高亮正確：所有橫躺行皆同色粉底，且 hover 某行時其他行半透明。
- [ ] 任一向量設為全零時，rank 顯示「0」紅字 + 退化提示文字出現。
- [ ] $m, n$ 在 [2, 6] 範圍內可拉動，cell 永不重疊、永不出框。
- [ ] Walkthrough 5 步驟首次開啟自動觸發，可關閉並有「再看一次」按鈕。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純顯示 $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 矩陣 + 兩組 slider，無平行性高亮、無動畫。
- **Tier 3 擴充：** + 拖曳 $\mathbf{a}$ 在 2D / 3D 空間的箭頭端點改值（geometric drag）+ 旁邊同步畫「列空間 = $\operatorname{span}\{\mathbf{a}\}$ 一條直線」3D 視角。
- **估時：** 1.5 session（含測試與 walkthrough）

---

### VizScript-02: 點積 vs 外積對偶切換（Dot ↔ Outer Duality）

#### A. 一句話定位
讓使用者 toggle 切換 (v1) / (v2)，看同樣兩個直立向量 $\mathbf{a}, \mathbf{b}$ 因為**轉置誰**而產出截然不同尺寸的結果。

#### B. 學習目標（Learning Outcome）
- 使用者能說出 (v1) $\mathbf{a}^{\mathrm{T}}\mathbf{b}$ 的形狀運算是 $(1 \times m)(m \times 1) = (1 \times 1)$ 純量。
- 使用者能說出 (v2) $\mathbf{a}\mathbf{b}^{\mathrm{T}}$ 的形狀運算是 $(m \times 1)(1 \times n) = (m \times n)$ 矩陣。
- 使用者能解釋「為什麼 (v1) 要求兩向量同維度、(v2) 不需要」。
- 使用者能在切換時看出哪個向量被轉置（橫躺起來）、結果端點如何從一個點擴張成一塊矩陣。

#### C. 待視覺化的數學物件
- **物件清單：** 列向量 $\mathbf{a} \in \mathbb{R}^m$、列向量 $\mathbf{b} \in \mathbb{R}^n$（在 (v1) 模式時要求 $m = n$）；產物 $s = \mathbf{a}^{\mathrm{T}}\mathbf{b} \in \mathbb{R}$（v1）或 $A = \mathbf{a}\mathbf{b}^{\mathrm{T}} \in \mathbb{R}^{m \times n}$（v2）。
- **預設值：** $\mathbf{a} = (1, 2, 3)^{\mathrm{T}}$、$\mathbf{b} = (1, 1, 1)^{\mathrm{T}}$（預設 $m = n = 3$ 讓兩種視角都可運作）。
- **維度範圍：** $m, n \in [2, 6]$；在 (v1) 模式時 UI 強制鎖 $n = m$（切到 (v1) 時 $n$ slider 跟著 $m$ 同步並顯示鎖頭符號）。
- **數值範圍：** 同 VizScript-01。
- **退化情形：**
  - **(v1) $\mathbf{a} \perp \mathbf{b}$（點積 = 0）：** 結果顯示 `0`，配文字「兩向量正交」。
  - **(v2) $\mathbf{a} = \mathbf{0}$ 或 $\mathbf{b} = \mathbf{0}$：** 與 VizScript-01 相同的零矩陣退化處理。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 75% 主動畫畫面、下 25% 控制列（含 (v1)/(v2) toggle + 共用的 $\mathbf{a}, \mathbf{b}$ slider）。
- **主畫面尺寸：** 800 × 480 px，白底；中央是運算式佈局，由左至右四段：**[向量 1] — [向量 2] — [`=`] — [結果]**。
- **(v1) 模式排列：** [粉紅橫條 $\mathbf{a}^{\mathrm{T}}$] [綠直條 $\mathbf{b}$] `=` [單一藍點，藍點旁公式 `s = ...`]。
- **(v2) 模式排列：** [綠直條 $\mathbf{a}$] [粉紅橫條 $\mathbf{b}^{\mathrm{T}}$] `=` [$m \times n$ 藍點網格矩陣]。
- **公式區（畫面右上角，疊在主畫面內）：** 即時 LaTeX 公式 + 結果端的形狀標籤 `(1×1)` 或 `(m×n)`。
- **配色：** 同 VizScript-01 + §1（綠 / 粉紅 / 藍點 / 灰底）。
- **字型 / 字級：** 結果區公式 18pt MathJax、向量內部分量數字 14pt monospace。
- **邊距：** 上下 20px、左右 30px。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 | toggle | v1 / v2 | v1 | 即時（含 500ms 動畫過渡） |
| $m$ | slider | [2, 6] step 1 | 3 | 即時 |
| $n$ | slider | [2, 6] step 1 | 3 | 即時（v1 模式時與 $m$ 鎖定同步） |
| $a_i$ | slider $m$ 個 | [-9, 9] step 1 | $(1,2,3)$ | 即時 |
| $b_j$ | slider $n$ 個 | [-9, 9] step 1 | $(1,1,1)$ | 即時 |

#### F. 輸出畫面細節（Outputs）
- **(v1) 結果端：** 單一藍點（直徑 32px），點旁文字 `s = a₁b₁ + a₂b₂ + ... + aₘbₘ = ${value}`；當 $s = 0$ 額外標籤「⊥」。
- **(v2) 結果端：** $m \times n$ 藍點網格 + 每 cell 對應數字 `a_i × b_j`；左緣綠色細條（標 $\mathbf{a}$ 來源）、上緣粉色細條（標 $\mathbf{b}^{\mathrm{T}}$ 來源），與圖 2.1 右側抽象示意一致。
- **形狀標籤：** (v1) 時顯示 `(1×$m$)·($m$×1) = (1×1) 純量`；(v2) 時顯示 `($m$×1)·(1×$n$) = ($m$×$n$) 矩陣`。
- **rank 顯示：** (v2) 模式時右下角顯示 rank（0 或 1）；(v1) 模式時改顯示「Dot product = $s$」。

#### G. 互動行為（Interactions）
- **toggle v1 ↔ v2：** 觸發轉置動畫（見 §H）；公式區同步切換。
- **拉動 $a_i$ / $b_j$ slider：** 結果端即時重算；(v1) 模式時藍點上的文字更新；(v2) 模式時對應 cell 更新。
- **hover 向量某分量：**
  - (v1) 模式：對應位置的 $\mathbf{a}^{\mathrm{T}}$ 與 $\mathbf{b}$ 同時高亮，並在點積展開式中對應項加粗。
  - (v2) 模式：對應整行 / 整列亮起。
- **快捷鍵：** `1` 切到 v1、`2` 切到 v2、`Space` toggle。

#### H. 動畫腳本（v1 ↔ v2 轉置切換）
- **從 v1 → v2:**
  - **t=0:** v1 穩態（粉紅橫條 + 綠直條 + 藍點）。
  - **t=0–200ms:** 結果藍點 fade out（opacity 1 → 0）。
  - **t=200–500ms:** 左邊粉紅橫條「立起來」變綠直條（旋轉 90° 並換色，500ms 內完成）；同時右邊綠直條「躺下來」變粉紅橫條。實作上：把 $\mathbf{a}$ 的橫躺 row vector 圖示縮短 + 顏色由粉紅變綠 + 高度增加；$\mathbf{b}$ 反之。
  - **t=500–700ms:** 中央出現空白矩陣框（淡入），cell 逐個從中心向外展開（stagger 30ms / cell）填上數字。
  - **t=700ms 後:** v2 穩態。
- **從 v2 → v1:** 反向重播（cell 收回 → 矩陣框消失 → 兩個向量旋轉換色 → 藍點淡入）。
- **總長度：** 700ms。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。
- **暫停 / 倒轉：** 是（提供「再播一次」按鈕；toggle 過程中按 Esc 立即停在當前 frame）。

#### I. 邊界與錯誤處理
- **v1 模式但 $m \ne n$：** UI 不允許（slider 鎖定）；若使用者用快捷鍵硬切，跳出 toast「v1 需要兩向量同維度，已自動把 $n$ 設為 $m$」。
- **動畫進行中再切換：** debounce 100ms 或等動畫完成才接受下一次 toggle，避免狀態錯亂。
- **$m = n = 6$ 大尺寸 + v2：** 矩陣 cell 縮為 48×48 px；動畫禁用 stagger 改用整體 fade。
- **點積結果絕對值 > 999：** 結果文字字級自動由 18pt 降為 14pt 避免溢框。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - toggle (v1)：「行向量 × 列向量 = 一個數字（純量）」
  - toggle (v2)：「列向量 × 行向量 = 一個秩 1 矩陣」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在是 (v1) 視角，左邊粉紅橫條是 $\mathbf{a}^{\mathrm{T}}$、右邊綠直條是 $\mathbf{b}$」
  - Step 2：「結果只有一個藍點 — 一個數字」
  - Step 3：「按右下 toggle 切換到 (v2)」
  - Step 4：「兩個向量轉了 90 度 — 左邊變綠直條 $\mathbf{a}$、右邊變粉紅橫條 $\mathbf{b}^{\mathrm{T}}$」
  - Step 5：「結果從 1 個藍點擴張成一塊矩陣 — 但只有 1 個自由度（rank 1）」
- **常見誤解警示：**
  - 「(v1) 與 (v2) 不是計算順序的選擇，是把哪個向量轉置的選擇」
  - 「點積得到的數字 = 外積矩陣的跡 (trace)？」 — **錯**，這只在 $m = n$ 且 $\mathbf{a} = \mathbf{b}$ 時近似成立（$\operatorname{tr}(\mathbf{a}\mathbf{a}^{\mathrm{T}}) = \|\mathbf{a}\|^2 = \mathbf{a}^{\mathrm{T}}\mathbf{a}$）；一般 $\mathbf{a} \ne \mathbf{b}$ 時兩者不等。
- **延伸閱讀：** 原書 p.2、`ch02-vec-vec.md` 數學要點段。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib + `matplotlib.animation.FuncAnimation`（控制 v1↔v2 動畫）+ marimo.ui。
- **替代方案：** D3.js + SVG（如需高品質網頁動畫；旋轉換色用 CSS transform + filter）。
- **關鍵 API：**
  - `matplotlib.transforms.Affine2D().rotate_deg_around()` 做向量旋轉動畫
  - `matplotlib.animation.FuncAnimation(fig, update, frames=42, interval=16)`（700ms / 42 frames）
  - `matplotlib.patches.FancyArrowPatch` 做向量箭頭（也可用 Rectangle）
- **檔案結構：** 與 VizScript-01 同檔（`viz/ch02_outer_product.py`），共用 `_common/palette.py` 與 `vector_canvas.py`。
- **效能：** 動畫期間預先計算所有 frame 的座標 / 顏色，存 list，避免每 frame 重算。動畫結束後切回 reactive 模式。
- **測試：** 動畫關鍵 frame（t=0 / 200 / 500 / 700ms）各 1 張 snapshot PNG。

#### L. 驗收標準（Acceptance Criteria）
- [ ] v1 ↔ v2 toggle 動畫總長 ≤ 700ms，60fps 無 frame drop。
- [ ] v1 模式下 $m \ne n$ 不可能發生（UI 鎖定）。
- [ ] 點積結果 $\mathbf{a}^{\mathrm{T}}\mathbf{b} = 0$ 時自動標示「⊥」。
- [ ] 切換動畫中再按 toggle 不導致狀態錯亂（debounce 或佇列）。
- [ ] Walkthrough 5 步驟首次開啟自動觸發。
- [ ] 公式區 LaTeX 渲染 < 50ms 完成（MathJax cache）。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純靜態並列兩張圖（v1 + v2），無動畫無切換。
- **Tier 3 擴充：** + 把 $\mathbf{a}, \mathbf{b}$ 同時也在 2D 平面上畫成箭頭，動畫顯示「夾角」（點積幾何意涵 $\mathbf{a}^{\mathrm{T}}\mathbf{b} = \|\mathbf{a}\|\|\mathbf{b}\|\cos\theta$）。
- **估時：** 1.5 session（含動畫調校與 walkthrough）

---

## 章末延伸

- **後續章節連結：** [→ ch03-mat-vec.md](ch03-mat-vec.md) — §3 矩陣乘以向量（Matrix × Vector）也有兩種視角（dot product way / linear combination way），是本章 (v1) 與 (v2) 的自然推廣。

- **延伸閱讀 / 相關概念：**
  - Strang《Linear Algebra for Everyone》Sec. 1.1（線性組合與點積）、Sec. 1.3（秩 1 矩陣）、Sec. 1.4（行 / 列方法）— 原書直接對應段落。
  - 後續 §6 五大分解皆以「秩 1 矩陣之和」為共同骨架；本章 (v2) 是必備前置知識。
  - **跨領域類比：** 神經網路裡的權重外積更新（Hebbian rule、低秩近似 LoRA）本質就是「外積 → 秩 1 矩陣」的應用 — 不在本書範圍但值得知道。

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 49–67 / `The-Art-of-Linear-Algebra.pdf` p.2
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` line 47–66
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0
