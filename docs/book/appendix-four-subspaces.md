# 附錄 C：四個基本子空間（The Four Subspaces and the Solutions to $A\mathbf{x} = \mathbf{b}$）

> **原書頁碼：** 英文版 References 第 5 條（p.34，無獨立 slidedeck，含於 4-Subspaces 圖）/ 簡中版同
> **對應 .tex 段落：** `from-tex/en.md` 第 612–617 行（References 區）/ 圖檔：`4-Subspaces.png`（與 §3 同款）
> **本章圖數：** 1（`4-Subspaces.png`，與 [ch03 § Figure 3.2](ch03-mat-vec.md) 同款）
> **本章 VizMark 數：** 1（⭐⭐ Tier 1 + pointer 指 [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) + [ch06f VizScript-03](ch06f-USV.md#vizscript-03)）
> **PNG `using XX` 標記：** **無**（S10 PNG 重核確認 — 4-Subspaces 圖是「基本概念圖」非 Pattern 套用層級）
> **狀態：** [x] 已完成

---

## 章節摘要

《The Four Subspaces and the Solutions to $A\mathbf{x} = \mathbf{b}$》是 Gilbert Strang 設計、Kenji Hiranabe 繪製的標誌性視覺化，**並非《Linear Algebra for Everyone》主書內容**，而是 Strang 在多本著作中反覆強調的「**線性代數最重要的一張圖**」。它把矩陣 $A \in \mathbb{R}^{m \times n}$ 對應的**四個基本子空間** — 行空間 $\mathbf{C}(A^{\mathrm{T}})$ + 零空間 $\mathbf{N}(A)$（在 $\mathbb{R}^n$ 上）和列空間 $\mathbf{C}(A)$ + 左零空間 $\mathbf{N}(A^{\mathrm{T}})$（在 $\mathbb{R}^m$ 上）— 用「**兩塊大餅圖**」呈現，並標註「**互相垂直**」「**維度和 = 全空間維度**」兩條關鍵關係。本附錄是 §3 [Matrix × Vector](ch03-mat-vec.md) + §6.5 [SVD](ch06f-USV.md) 的「**整合性收尾**」 — 與主章節相比，附錄**重「鳥瞰整合」而非「從零教學」**：（1）補 SVD 構造 4 子空間的**完整算法視角**（從 EVD 整合到 SVD 對齊）；（2）補解 $A\mathbf{x} = \mathbf{b}$ 的**完整解空間結構**（一般解 = 特解 + 零空間解）；（3）pointer 到 §3 / §6.5 已完成的旗艦 VizScript（[ch03 VizScript-02](ch03-mat-vec.md#vizscript-02)、[ch06f VizScript-03](ch06f-USV.md#vizscript-03)）。

---

## 數學要點

### 1. 四個基本子空間的定義與維度

> 給定矩陣 $A \in \mathbb{R}^{m \times n}$ rank $r$，存在**四個基本子空間**：

| 子空間 | 符號 | 定義 | 維度 | 所屬全空間 |
|---|---|---|---|---|
| **列空間** | $\mathbf{C}(A)$ | $\{A\mathbf{x}: \mathbf{x} \in \mathbb{R}^n\}$（所有 $A\mathbf{x}$） | $r$ | $\mathbb{R}^m$ |
| **零空間** | $\mathbf{N}(A)$ | $\{\mathbf{x}: A\mathbf{x} = \mathbf{0}\}$ | $n - r$ | $\mathbb{R}^n$ |
| **行空間** | $\mathbf{C}(A^{\mathrm{T}})$ | $\{\mathbf{y} A: \mathbf{y} \in \mathbb{R}^m\}$（所有 $\mathbf{y}A$） | $r$ | $\mathbb{R}^n$ |
| **左零空間** | $\mathbf{N}(A^{\mathrm{T}})$ | $\{\mathbf{y}: \mathbf{y} A = \mathbf{0}\}$ | $m - r$ | $\mathbb{R}^m$ |

### 2. 兩條核心關係（圖中明示）

#### 關係 A：正交補關係

$$
\mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}}) \quad \text{（在 } \mathbb{R}^n \text{ 上）}
$$
$$
\mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}}) \quad \text{（在 } \mathbb{R}^m \text{ 上）}
$$

#### 關係 B：直和分解

$$
\mathbb{R}^n = \mathbf{N}(A) \oplus \mathbf{C}(A^{\mathrm{T}}) \quad \text{維度 } n = (n-r) + r
$$
$$
\mathbb{R}^m = \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}}) \quad \text{維度 } m = r + (m-r)
$$

### 3. SVD 構造 4 子空間的標準正交基底（附錄重點 ⭐）

> §6.5 SVD 的 $A = U \Sigma V^{\mathrm{T}}$ 提供「**4 子空間的標準正交基底**」 — 這是 SVD 最深刻的應用之一。

**從 SVD 直接讀出 4 子空間基底：**

設 $A \in \mathbb{R}^{m \times n}$ rank $r$，SVD 分解為 $A = U \Sigma V^{\mathrm{T}}$，其中 $U = [\mathbf{u}_1, \ldots, \mathbf{u}_m]$、$V = [\mathbf{v}_1, \ldots, \mathbf{v}_n]$、$\Sigma$ 對角元 $\sigma_1 \geq \cdots \geq \sigma_r > 0 = \sigma_{r+1} = \cdots$。則：

$$
\begin{array}{ll}
\mathbf{C}(A) & = \mathrm{span}\{\mathbf{u}_1, \ldots, \mathbf{u}_r\} \quad \text{（} U \text{ 前 } r \text{ 列）} \\
\mathbf{N}(A^{\mathrm{T}}) & = \mathrm{span}\{\mathbf{u}_{r+1}, \ldots, \mathbf{u}_m\} \quad \text{（} U \text{ 後 } m-r \text{ 列）} \\
\mathbf{C}(A^{\mathrm{T}}) & = \mathrm{span}\{\mathbf{v}_1, \ldots, \mathbf{v}_r\} \quad \text{（} V \text{ 前 } r \text{ 列）} \\
\mathbf{N}(A) & = \mathrm{span}\{\mathbf{v}_{r+1}, \ldots, \mathbf{v}_n\} \quad \text{（} V \text{ 後 } n-r \text{ 列）} \\
\end{array}
$$

**SVD 的「**4 子空間最佳對齊性質**」：** $U$ 和 $V$ 是**標準正交矩陣**（$U^{\mathrm{T}}U = I_m$、$V^{\mathrm{T}}V = I_n$），所以「**列空間的基底彼此正交、零空間的基底彼此正交**」 — 這是其他分解（CR / LU / QR / EVD）無法提供的優勢。**SVD 同時最優地對齊 4 子空間，是「線性代數最完整的視覺定理」**。詳細展開見 [ch06f VizScript-03 4 子空間 SVD 構造](ch06f-USV.md#vizscript-03)。

### 4. 解 $A\mathbf{x} = \mathbf{b}$ 的完整解空間結構（附錄重點 ⭐）

> 用 4 子空間結構可以**完整解析** $A\mathbf{x} = \mathbf{b}$ 的解（這是 Strang 圖題目「**Solutions to $A\mathbf{x} = \mathbf{b}$**」的由來）。

#### 情況 A：$\mathbf{b} \in \mathbf{C}(A)$（有解）

**特解：** $\mathbf{x}_p$ 滿足 $A\mathbf{x}_p = \mathbf{b}$
**通解：** $\mathbf{x} = \mathbf{x}_p + \mathbf{x}_n$，其中 $\mathbf{x}_n \in \mathbf{N}(A)$

$$
\boxed{\text{完整解} = \text{特解} + \text{零空間解}}
$$

**幾何視覺：** 通解是 $\mathbb{R}^n$ 中一個「**平移過的子空間**」（仿射子空間） — 通過 $\mathbf{x}_p$ 平行於 $\mathbf{N}(A)$ 的子空間。

**唯一解條件：** $\mathbf{N}(A) = \{\mathbf{0}\}$（即 $r = n$，全列獨立）

#### 情況 B：$\mathbf{b} \notin \mathbf{C}(A)$（無解）

**最小二乘解：** 找 $\mathbf{x}^*$ 使 $\| A\mathbf{x}^* - \mathbf{b} \|^2$ 最小
**公式：** $\mathbf{x}^* = A^{+} \mathbf{b}$（用偽反矩陣，見 [Matrix World 附錄](appendix-matrix-world.md) 底部公式）

**幾何視覺：** $\mathbf{x}^*$ 把 $\mathbf{b}$ **投影到** $\mathbf{C}(A)$（在 $\mathbb{R}^m$ 上正交投影）然後反推回 $\mathbb{R}^n$。

#### 通用解（含正則化）

$$
\mathbf{x}^* = A^{+} \mathbf{b} = V \Sigma^{+} U^{\mathrm{T}} \mathbf{b}
$$

這是 SVD 提供的「**最小二乘 + 最小範數**」最優解 — 比任何單純的「特解 + 零空間解」更穩健（避免病態方程的浮點誤差放大）。

### 5. 與 §3、§6.5 主章節的整合對照（附錄定位）

| 概念 | §3 主章節 | §6.5 主章節 | 本附錄補充 |
|---|---|---|---|
| 4 子空間定義 | [ch03 §3 第 2 段](ch03-mat-vec.md) 從 $A\mathbf{x}$ 與 $\mathbf{y}A$ 引入 | [ch06f VizScript-03](ch06f-USV.md#vizscript-03) SVD 對齊 | **整合鳥瞰** — 4 子空間是 §3 入門 + §6.5 集大成 |
| 兩塊大餅圖視覺 | [ch03 Figure 3.2](ch03-mat-vec.md) + [VizScript-02](ch03-mat-vec.md#vizscript-02) ⭐⭐⭐ Tier 3 候選 | [ch06f VizScript-03](ch06f-USV.md#vizscript-03) SVD 構造版 | **pointer 整合** — 本附錄不重複實作 |
| SVD 基底對齊 | 未深入 | [ch06f VizScript-03 構造算法](ch06f-USV.md#vizscript-03) | **正交分解定理完整版** |
| 解 $A\mathbf{x}=\mathbf{b}$ | [ch03 §3 第 3 段](ch03-mat-vec.md) 零空間引入 | [ch06f VizScript-01 推薦系統 / 矩陣補全應用](ch06f-USV.md#vizscript-01) | **完整解空間結構** + 最小二乘 + 正則化 |
| 偽反矩陣 $A^{+}$ | 未涉及 | [ch06f §7 與其他分解關係](ch06f-USV.md)（總結表段，無對應 VizScript） | **整合定義 + 與 Matrix World 連結** |

**附錄定位：** 本附錄是「**§3 + §6.5 + Matrix World 三章的橋樑**」 — 不重複教學，只整合三章的觀點 + 補解 $A\mathbf{x}=\mathbf{b}$ 完整結構 + pointer 到旗艦 VizScript。

---

## 圖片詳細描述（Figure Description）

### Figure C.1: 四個基本子空間（The Four Subspaces）— 無 `using` 標記，與 [ch03 Figure 3.2](ch03-mat-vec.md) 同款

**圖檔：** `docs/book/figs-png/4-Subspaces.png`（原始 EPS：`figs/4-Subspaces.eps`）
**原書頁碼：** §3 + References 第 5 條（同款圖）
**所屬章節：** 附錄 C（與 [ch03 §3](ch03-mat-vec.md) 共用此圖）

#### 視覺結構 (Visual Structure)

整體**左右對稱兩塊大餅**結構：

- **左塊（$\mathbb{R}^n$）：**
  - 上方大白色方塊（傾斜約 30°）標 "row space"、"all $\mathbf{y}A$"，方塊中央嵌粉紅色 3 個橫躺長條（**行向量**，標 $\mathbf{C}(A^{\mathrm{T}})$、$\dim = r$）
  - 下方小白色方塊標 "nullspace"、"$A\mathbf{x} = \mathbf{0}$"（標 $\mathbf{N}(A)$、$\dim = n-r$）
  - 兩塊垂直連接，標「perpendicular」並寫小直角符號
  - 左側標籤：$\mathbb{R}^n$、$\mathbf{C}(A^{\mathrm{T}})$、$\mathbf{N}(A)$
  - 底部標：$\mathbb{R}^n = \mathbf{N}(A) + \mathbf{C}(A^{\mathrm{T}})$、$\mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}})$

- **右塊（$\mathbb{R}^m$）：**
  - 上方大白色方塊（傾斜約 30° 鏡像）標 "column space"、"all $A\mathbf{x}$"，方塊中央嵌綠色 2 個直立長條（**列向量**，標 $\mathbf{C}(A)$、$\dim = r$）
  - 下方小白色方塊標 "left nullspace"、"$\mathbf{y}A = \mathbf{0}$"（標 $\mathbf{N}(A^{\mathrm{T}})$、$\dim = m-r$）
  - 標「perpendicular」+ 小直角符號
  - 右側標籤：$\mathbb{R}^m$、$\mathbf{C}(A)$、$\mathbf{N}(A^{\mathrm{T}})$
  - 底部標：$\mathbb{R}^m = \mathbf{C}(A) + \mathbf{N}(A^{\mathrm{T}})$、$\mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}})$

- **上方箭頭：** $\mathbb{R}^n \xrightarrow{A \in \mathbb{R}^{m \times n}} \mathbb{R}^m$，表示「矩陣 $A$ 是從 $\mathbb{R}^n$ 到 $\mathbb{R}^m$ 的映射」

- **整體色調：** 純白背景、深藍細線框 `#1f77b4`、行向量（左）粉紅 `#d62728`、列向量（右）綠色 `#2ca02c` — **這是全書配色錨點的「**起源**」**（[ch03 §3](ch03-mat-vec.md) 之後所有章節都沿用此配色）

- **視覺引導：** 讀者**先看上方箭頭**（理解 $A$ 是 $\mathbb{R}^n \to \mathbb{R}^m$ 映射）→ **看左塊**（$\mathbb{R}^n$ 拆成「行空間 + 零空間」兩個互相垂直子空間）→ **看右塊**（$\mathbb{R}^m$ 拆成「列空間 + 左零空間」兩個互相垂直子空間）→ **最後對照**「行空間和列空間維度都是 $r$」（圖的「秘密」 = **列秩 = 行秩定理**，[ch06b CR 章](ch06b-CR.md) 已詳述）

#### 數學內容 (Mathematical Content)

$$
A: \mathbb{R}^n \to \mathbb{R}^m, \quad A \in \mathbb{R}^{m \times n}, \quad \mathrm{rank}(A) = r \leq \min(m, n)
$$

**四個子空間的形式定義：**

$$
\begin{array}{ll}
\mathbf{C}(A) & = \mathrm{span}\{\mathbf{a}_1, \ldots, \mathbf{a}_n\} = \{A\mathbf{x}: \mathbf{x} \in \mathbb{R}^n\} \subset \mathbb{R}^m \\
\mathbf{N}(A) & = \{\mathbf{x} \in \mathbb{R}^n: A\mathbf{x} = \mathbf{0}\} \subset \mathbb{R}^n \\
\mathbf{C}(A^{\mathrm{T}}) & = \mathrm{span}\{\mathbf{a}^*_1, \ldots, \mathbf{a}^*_m\} = \{\mathbf{y} A: \mathbf{y} \in \mathbb{R}^m\} \subset \mathbb{R}^n \\
\mathbf{N}(A^{\mathrm{T}}) & = \{\mathbf{y} \in \mathbb{R}^m: \mathbf{y} A = \mathbf{0}\} \subset \mathbb{R}^m \\
\end{array}
$$

**正交分解定理（Strang's Fundamental Theorem of Linear Algebra）：**

$$
\begin{cases}
\mathbb{R}^n = \mathbf{N}(A) \oplus \mathbf{C}(A^{\mathrm{T}}), & \mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}}) \\
\mathbb{R}^m = \mathbf{C}(A) \oplus \mathbf{N}(A^{\mathrm{T}}), & \mathbf{C}(A) \perp \mathbf{N}(A^{\mathrm{T}}) \\
\dim \mathbf{C}(A) = \dim \mathbf{C}(A^{\mathrm{T}}) = r & \text{（列秩 = 行秩）} \\
\dim \mathbf{N}(A) = n - r, \quad \dim \mathbf{N}(A^{\mathrm{T}}) = m - r
\end{cases}
$$

#### 直覺解讀 (Intuition)

這張圖是「**Strang 對線性代數最重要的單一視覺貢獻**」 — 把矩陣 $A$ 的所有結構性質**壓縮到一張圖**。**最重要的三條洞察：**

**洞察 1：「兩塊大餅 = 兩個全空間 = 兩種對偶視角」** — 左塊看 $\mathbb{R}^n$（從「行向量」+「點積」角度，對應 [§3 (Mv1)](ch03-mat-vec.md)），右塊看 $\mathbb{R}^m$（從「列向量」+「線性組合」角度，對應 [§3 (Mv2)](ch03-mat-vec.md)）。**這是 §1–§3 教學主軸「**4 ways viewing a matrix**」的視覺收斂點**。

**洞察 2：「正交補定理 = 秩-零定理」** — 圖中「上塊（行/列空間）⊥ 下塊（零空間）」+ 兩塊維度相加 = 全空間維度，是 **rank-nullity theorem 的視覺呈現**：
$$
\dim \mathbf{C}(A^{\mathrm{T}}) + \dim \mathbf{N}(A) = r + (n-r) = n
$$
這個定理是線性代數最基本但最深刻的定理之一，圖把它變成「**一看就懂**」。

**洞察 3：「列秩 = 行秩 = $r$ 的圖示證明」** — 圖中左塊「行空間維度 = $r$」+ 右塊「列空間維度 = $r$」**兩個都標 $r$**。這就是 [ch06b CR 章](ch06b-CR.md) 詳述的列秩 = 行秩定理 — **CR 分解的 $C$ 是「列空間基底」、$R$ 是「行階梯形」，兩個視角的 $r$ 相同**。

**為什麼這張圖是 SVD 的「終極前奏」？**

§6.5 SVD 提供「**4 子空間的標準正交基底**」 — 用 $A = U \Sigma V^{\mathrm{T}}$ 同時把這四個子空間的基底**正交對齊**。**SVD 是 4-Subspaces 圖的「**填色版本**」 — 不只告訴你 4 個子空間存在，還給出每個子空間的「**最佳座標系**」**。詳見 [ch06f VizScript-03 SVD 4 子空間構造](ch06f-USV.md#vizscript-03)。

**常見誤解：**

- **「行空間和列空間是同一個東西嗎？」** 不！它們維度相同（都 $= r$），但**屬於不同的全空間**（$\mathbf{C}(A^{\mathrm{T}}) \subset \mathbb{R}^n$、$\mathbf{C}(A) \subset \mathbb{R}^m$）。當 $m \neq n$ 時兩個全空間維度不同，所以兩個子空間「**只是維度數字相同，是兩個獨立子空間**」。
- **「零空間和左零空間哪個比較重要？」** 對解 $A\mathbf{x}=\mathbf{b}$ 來說是**零空間**（決定解的多重性）；對解 $\mathbf{y}A=\mathbf{c}$ 來說是**左零空間**。對 SVD 而言**兩個同等重要**（都是 $U/V$ 的後段列）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [4 子空間整合互動 + 解 $A\mathbf{x}=\mathbf{b}$ 視覺化] ⭐⭐ Tier 1 + pointer
> **位置：** Figure C.1 / 附錄 C 整圖
> **核心概念：** 4 子空間正交分解 + SVD 構造基底 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構
> **互動梗概：** 採「**整合 pointer 策略**」 — 不重複實作 4 子空間動畫（已在 [ch03 VizScript-02](ch03-mat-vec.md#vizscript-02) 完成 ⭐⭐⭐ Tier 3 候選），不重複實作 SVD 構造（已在 [ch06f VizScript-03](ch06f-USV.md#vizscript-03) 完成）。本附錄 VizMark 只負責「**整合面板**」：左半重用 ch03 4 子空間結構視覺、右半新增「**解 $A\mathbf{x}=\mathbf{b}$ 完整結構互動**」（特解 + 零空間解 + 仿射子空間 + 最小二乘投影 + 偽反矩陣公式）+ 兩個跳轉按鈕。
> **詳見劇本：** VizScript-01（章末）

---

## 視覺化劇本（VizScripts）

### VizScript-01: 4 子空間整合 + 解 $A\mathbf{x}=\mathbf{b}$ 視覺（Four Subspaces Integration — Tier 1 + pointer）

**Tier：** ⭐⭐ Tier 1 + pointer（核心整合面板，4 子空間結構動畫 pointer 到 [ch03 V-02](ch03-mat-vec.md#vizscript-02)，SVD 構造 pointer 到 [ch06f V-03](ch06f-USV.md#vizscript-03)）
**對應 VizMark：** Figure C.1 / VizMark-01

> 本劇本只負責**整合面板 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構新視覺**，4 子空間結構動畫（Strang 兩塊大餅）已在 ch03 V-02 ⭐⭐⭐ Tier 3 候選實作，SVD 構造（4 子空間基底正交對齊）已在 ch06f V-03 實作。本附錄不重複，透過按鈕「→ 看 4 子空間結構詳解」與「→ 看 SVD 4 基底構造」跳轉到對應章節。

#### A. 一句話定位

把 Strang 4-Subspaces 圖實作為「**整合面板**」 — 4 子空間結構與 SVD 基底構造由其他 VizScript 負責，本面板專注「**解 $A\mathbf{x}=\mathbf{b}$ 完整結構視覺**」（特解 + 零空間解 + 仿射子空間 + 最小二乘 + 偽反矩陣），讓讀者「**從 4 子空間直接看到所有 $A\mathbf{x}=\mathbf{b}$ 的可能解**」。

#### B. 學習目標（Learning Outcome）

讀者完成此互動後能夠：

1. **整合 §3 + §6.5 視角**：把入門期的 4 子空間概念與集大成期的 SVD 對齊整合
2. **理解 $A\mathbf{x}=\mathbf{b}$ 解空間**：知道完整解 = 特解 + 零空間平移、無解時用最小二乘
3. **連結偽反矩陣**：理解 $\mathbf{x}^* = A^{+}\mathbf{b}$ 是「**最小二乘 + 最小範數**」最優解
4. **連結 Matrix World**：理解本附錄與 [Matrix World](appendix-matrix-world.md) 底部偽反公式的對應

#### C. 整體布局（雙面板 + 跳轉按鈕）

- **左面板（400×600 px）：** 縮小版 4 子空間結構（重用 [ch03 V-02](ch03-mat-vec.md#vizscript-02) 視覺），無互動但顯示「→ 看 4 子空間結構詳解」按鈕
- **右面板（800×600 px，主互動）：** **「解 $A\mathbf{x}=\mathbf{b}$ 完整結構互動視覺」**：
  - 中央：3D 視角的 $\mathbb{R}^n$ 子空間表示（$n = 2$ 或 3）
  - 標出 $\mathbf{N}(A)$（紫色平面或線）
  - 標出 $\mathbf{x}_p$ 特解（金色點）
  - 標出 通解平面（$\mathbf{x}_p + \mathbf{N}(A)$，半透明黃色仿射子空間）
  - 標出 $\mathbf{x}^* = A^{+}\mathbf{b}$（綠色點，「最小範數最優解」位置）
  - 顯示 $A^{+}\mathbf{b}$ 是「**最近原點的通解**」直觀理解

- **上方控制條：** 拉桿選 $m, n \in \{2, 3\}$、輸入 $A$ 矩陣（自動算 rank $r$）、輸入 $\mathbf{b}$、選「有解 / 無解」情境

- **下方輸出區：** 顯示 $A^{+}$（用 SVD 算）、特解 $\mathbf{x}_p$、通解形式、最小二乘解 $\mathbf{x}^* = A^{+}\mathbf{b}$

#### D. 可調參數（拉桿）

- **矩陣 $A$ 維度：** $m, n \in \{2, 3\}$（保 3D 可視）
- **矩陣 $A$ 元素：** $a_{ij} \in [-3, 3]$ 步進 0.5
- **右側向量 $\mathbf{b}$：** $b_i \in [-3, 3]$ 步進 0.5
- **情境切換：** 「保證有解（$\mathbf{b}$ 在 $\mathbf{C}(A)$）/ 強制無解（$\mathbf{b}$ 在 $\mathbf{N}(A^{\mathrm{T}})$）/ 一般情形」

#### E. 顏色配方（沿用全書錨點）

- **零空間 $\mathbf{N}(A)$：** 紫色 `#9467bd` 半透明（沿 ch05 P3 / S09 4 子空間錨點）
- **特解 $\mathbf{x}_p$：** 金色 `#FFD700` 實心點（沿用 §6.x EVD 變形後橢球錨點）
- **通解平面（仿射子空間）：** 半透明黃色 alpha 0.3
- **最小範數最優解 $\mathbf{x}^*$：** 綠色 `#2ca02c` 實心點
- **列空間 $\mathbf{C}(A)$ 投影（右塊）：** 綠色半透明 alpha 0.3（與全書一致）
- **正交補 perpendicular 標記：** 灰直角符號

#### F. 動畫節奏

- **拉桿即時更新：** 矩陣 / 向量改變後，特解 / 通解平面 / 最優解以 300ms 平滑移動到新位置
- **情境切換動畫：** 800ms「保證有解 → 強制無解」過渡時，$\mathbf{b}$ 慢慢移出 $\mathbf{C}(A)$，最小二乘解 $\mathbf{x}^*$ 浮現（不再是 $\mathbf{x}_p$）
- **跨子空間切換：** 點「→ 看 4 子空間結構詳解」按鈕後，左面板放大、右面板淡出，整體切換到 [ch03 V-02](ch03-mat-vec.md#vizscript-02)

#### G. 公式同步顯示（右面板下方）

- 即時顯示：
  1. SVD 分解：$A = U \Sigma V^{\mathrm{T}}$（$U, \Sigma, V$ 矩陣即時更新）
  2. 偽反：$A^{+} = V \Sigma^{+} U^{\mathrm{T}}$
  3. 通解：$\mathbf{x} = \mathbf{x}_p + c_1 \mathbf{v}_{r+1} + \cdots + c_{n-r} \mathbf{v}_n$（$\mathbf{v}_j$ 是 SVD 的零空間基底）
  4. 最小範數最優解：$\mathbf{x}^* = A^{+}\mathbf{b}$（數值結果）
  5. 殘差：$\| A\mathbf{x}^* - \mathbf{b} \|_2$（若 > 0 表示無解情境）

#### H. 驗收標準

1. **3D 視覺正確：** 拉桿任意組合下，3D 視窗中的「**通解平面 = 平行 $\mathbf{N}(A)$ 通過 $\mathbf{x}_p$**」幾何關係始終成立
2. **最小範數性質：** $\mathbf{x}^* = A^{+}\mathbf{b}$ 確實是「**通解中最接近原點**」的點（可驗證 $\mathbf{x}^* \perp \mathbf{N}(A)$）
3. **無解情境準確：** 強制無解時，殘差 > 0 + $\mathbf{b}$ 在 $\mathbf{C}(A)$ 上的投影是 $A\mathbf{x}^*$
4. **跳轉正確：** 兩個跳轉按鈕分別準確跳到 [ch03 V-02](ch03-mat-vec.md#vizscript-02) 與 [ch06f V-03](ch06f-USV.md#vizscript-03)

#### I. 邊界與健壯性

- **rank 退化：** $A = O$ 時提示「零矩陣，所有 $\mathbf{x}$ 都是 $\mathbf{N}(A)$」+ 跳過 SVD 計算
- **數值容差：** 用 SVD 算 $A^{+}$ 時 $\sigma_p < 10^{-10}$ 視為 0（避免 1/0 爆炸）
- **超高維度：** $m, n > 3$ 時自動關閉 3D 視覺、改顯示「**4 子空間維度表 + 偽反公式**」

#### J. 字幕 / 標題 / 圖例

- **頂部：** 「**4 子空間 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構整合**（Strang's Big Picture Integration）」
- **底部圖例：** 「紫 = 零空間、金 = 特解、黃半透明 = 通解平面、綠 = 最小範數最優解、灰直角 = 正交」

#### K. 教學引導文案

- **首次進入：** 「**4 子空間是 §3 入門 + §6.5 集大成 + 整本書的『**結構主軸**』**。本附錄整合三種觀點。左面板看 4 子空間結構（→ 點按鈕看 ch03 V-02 詳解），右面板看 $A\mathbf{x}=\mathbf{b}$ 的完整解空間 — 拉桿改 $A, \mathbf{b}$，**注意通解 = 特解 + 零空間平移**。」
- **情境切換時：** 「現在 $\mathbf{b}$ 不在 $\mathbf{C}(A)$ 中 — 方程無精確解。但 SVD 提供 $\mathbf{x}^* = A^{+}\mathbf{b}$ 作為『**最小二乘最優解**』，最小化 $\| A\mathbf{x} - \mathbf{b} \|^2$。注意 $\mathbf{x}^*$ 同時也是『**通解中最接近原點**』的點（最小範數）。」

#### L. 平台技術建議（S12+ 實作）

- **建議平台：** Marimo + plotly 3D（仿射子空間可視）+ matplotlib（公式 LaTeX 渲染）
- **核心套件：** `numpy.linalg.svd`（SVD 計算偽反）、`numpy.linalg.pinv`（直接算 $A^{+}$ 對照驗證）、`plotly.graph_objects.Surface`（通解平面）、`marimo.ui.slider`（拉桿群）

#### M. 延伸與替代方案

- **延伸 1：** 加入 4 子空間的**正交投影矩陣**視覺（$P_C = A A^{+}$ 是「**到 $\mathbf{C}(A)$ 的正交投影**」、$P_{C^{\mathrm{T}}} = A^{+} A$ 是「**到 $\mathbf{C}(A^{\mathrm{T}})$ 的正交投影**」）
- **延伸 2：** 整合 [Map of Eigenvalues](appendix-map-eigenvalues.md) 中「投影矩陣 $P^2 = P = P^{\mathrm{T}}$」格 — 看正交投影矩陣的特徵值 $\lambda \in \{0, 1\}$
- **替代方案：** D3 + Three.js 可實現相同 3D 視覺，但需自寫線代計算（不如 numpy + scipy 方便）

---

## 章末延伸

- **後續章節連結：** 無（本附錄為全書最後）
- **回到全書索引：** [→ § Matrix World 全書地圖](appendix-matrix-world.md)（從這裡點任一元素跳到對應章節）
- **回到主章節：**
  - [→ §3 Matrix × Vector 入門（4 子空間首次出現）](ch03-mat-vec.md)
  - [→ §6.5 SVD 集大成（4 子空間正交對齊）](ch06f-USV.md)
- **延伸閱讀：**
  - Gilbert Strang, *Introduction to Linear Algebra*, 第 3.5 節「Dimensions of the Four Subspaces」
  - Strang YouTube 課程 18.06「Linear Algebra」第 14 講「The Four Fundamental Subspaces」
  - 線代核心定理：Fundamental Theorem of Linear Algebra（Strang）

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` line 612–617（References 第 5 條，無獨立 PDF，與 §3 圖共用）
- **原書簡中版：** 簡中 zh.md 無此 References 條目（簡中版只列 References 1–4，省略第 5 條）
- **圖檔：** `figs-png/4-Subspaces.png`（同款圖也用於 [ch03 §3](ch03-mat-vec.md) Figure 3.2）
- **作者：** Gilbert Strang（概念）+ Kenji Hiranabe（artwork）
- **PNG 重核（S10）：** **無 `using XX` 標記**（基本概念圖，非 Pattern 套用層級；4 子空間是 §3 主軸 + §6.5 SVD 對齊的基本結構）
- **授權：** Apache 2.0
