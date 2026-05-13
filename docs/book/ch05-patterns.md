# 第 5 章. 實用模式（Practical Patterns）

> **原書頁碼：** p.5–7
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` 第 127–203 行
> **本章圖數：** 4（Figure 5.1 = P1/P2、Figure 5.2 = P1'/P2'、Figure 5.3 = P3、Figure 5.4 = P4）
> **本章 VizMark 數：** 4（⭐⭐⭐ × 2 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成 / [ ] 校對中

---

## 章節摘要

§4 的四種視角（MM1/MM2/MM3/MM4）已涵蓋所有 $AB$ 的拆解方式。本章把這些視角**特殊化**到三類在工程中極常見的「**配置**」上：(P1) (P1') 用對角矩陣**從右**乘 → **column scaling**（列縮放）；(P2) (P2') 用對角矩陣**從左**乘 → **row scaling**（行縮放）；(P3) $XD\mathbf{c}$ 是「對角線上嵌一個向量」的三明治結構，等於「**特徵向量按特徵值加權後再以初始條件係數線組**」 — 解微分方程 $\frac{d\mathbf{u}}{dt} = A\mathbf{u}$ 與遞迴方程 $\mathbf{u}_{n+1} = A\mathbf{u}_n$ 的核心；(P4) $U \Sigma V^{\mathrm{T}}$ 是「兩個正交矩陣夾一個對角矩陣」的三明治結構，等於「秩 1 矩陣按奇異值加權後相加」 — **特徵值分解與 SVD 共用的視覺骨架**。

> ⚠ **本章是 §6 五大分解的「最後一塊鋪陳」。** P1/P2/P1'/P2' 解釋對角矩陣的視覺角色（§6.4 $S = Q\Lambda Q^{\mathrm{T}}$ 與 §6.5 $A = U\Sigma V^{\mathrm{T}}$ 的中間項）；P3 把「特徵值 / 特徵向量 / 初始條件」三件事接合成「微分方程通解」（§6.4 的工程動機）；P4 把整個 (MM4) 視角包裝成「三明治結構」 — §6.4–§6.5 兩大分解都直接套此模式。

> ⚠ **術語提醒：** column = 列（直立、綠色）、row = 行（橫躺、粉紅色）。對角矩陣 $D$ 視作「**只在對角線存活**」的特殊形狀，視覺上以「藍色圓點 stack」表示對角元素 $d_1, d_2, \ldots$。

> ### 💡 背後觀念：對角矩陣與三明治結構為什麼是線代核心？
>
> 本章是 §6 五大分解的最後鋪陳，6 個 Pattern 看似分散，背後其實由**一個共同主題**串起 — **「對角矩陣承載按 index 加權的本質，兩基底承載方向」**。3 條設計動機問題：
>
> - **[Q11：對角矩陣 $D$ 為什麼這麼特別？](appendix-D-why.md#q11)** — 對角矩陣不是「貧瘠」結構，而是「**矩陣世界中的標量**」 — 它擁有四個超能力：純倍率作用（不耦合）/ 冪反指數逐元素 / 彼此恆可交換 / 特徵值行列式跡直接讀。§6 五大分解全部把對角矩陣（或其變形）放在「中間項」 — 這是「**把任意矩陣設法逼近成兩基底夾對角**」的世紀大計畫的設計核心。
> - **[Q12：(P3) 動態系統為什麼能用特徵值預測長期？](appendix-D-why.md#q12)** — 從矩陣 $A$ 的 $n^2$ 個元素，到「只看 $n$ 個特徵值預測長期」，這個資訊濃縮率不是巧合。(P3) 用「**座標變換 → 解耦演化 → 座標反變換**」三步走把原本耦合的演化拆解為 $n$ 條獨立指數曲線，長期由 $\lambda_{\max}$ 主導 — Fibonacci 黃金比例就是這個原理的具體例子。PageRank、PCA、馬可夫穩態、量子基態能量都靠 (P3) 撐起。
> - **[Q13：(P4) 三明治 $A = X\Lambda X^{-1}$ 為什麼是線代核心？](appendix-D-why.md#q13)** — (P4) 不是技術技巧而是**世界觀**：「任何複雜的線性變換，本質上都可分解為『**找到看清結構的最好視角 → 純對角縮放 → 換回原視角**』三段式」。§6 五大分解都是 (P4) 的特例：EVD 是「完美三明治」（兩基底相同 $Q$）、SVD 是「最強三明治」（兩基底不同 $U, V$）。19 世紀末到 20 世紀中期的線代主流研究就是「把任意矩陣化為三明治結構」這個 dream 的展開 — Sylvester、Jordan、Schmidt、Eckart-Young 100 年積累。

---

## 數學要點

設 $A \in \mathbb{R}^{m \times n}$（$m$ 行 $n$ 列）、$B \in \mathbb{R}^{m \times n}$（待左乘對象）、$D \in \mathbb{R}^{n \times n}$ 與 $D' \in \mathbb{R}^{m \times m}$ 為對角矩陣。$X \in \mathbb{R}^{n \times n}$ 為可逆方陣（特徵向量矩陣），$\mathbf{c} \in \mathbb{R}^n$ 為向量。$U \in \mathbb{R}^{m \times r}$、$\Sigma \in \mathbb{R}^{r \times r}$ 對角、$V^{\mathrm{T}} \in \mathbb{R}^{r \times n}$。

### Pattern 對應 §4 視角總表

| Pattern | 公式 | 對應 §4 視角 | 直覺 | §6 用途 |
|---|---|---|---|---|
| **(P1)** | $A B = C$，$B$ 任意 | (MM2) + (Mv2) | 從右乘 → $C$ 列是 $A$ 列的線組 | (MM2) 一般化 |
| **(P2)** | $B A = C$，$B$ 任意 | (MM3) + (vM2) | 從左乘 → $C$ 行是 $A$ 行的線組 | (MM3) 一般化 |
| **(P1')** | $A D = [d_1 \mathbf{a}_1\ \cdots\ d_n \mathbf{a}_n]$ | (MM2) 之特例（$B = D$） | 從右乘對角矩陣 → **每一列各自被一個對角元素縮放** | $Q\Lambda$、$U\Sigma$ |
| **(P2')** | $D' B = [d'_1 \mathbf{b}^*_1; \cdots; d'_m \mathbf{b}^*_m]^{\mathrm{T}}$ | (MM3) 之特例（$A = D'$） | 從左乘對角矩陣 → **每一行各自被一個對角元素縮放** | $\Lambda Q^{\mathrm{T}}$、$\Sigma V^{\mathrm{T}}$ |
| **(P3)** | $X D \mathbf{c} = \sum_p c_p d_p \mathbf{x}_p$ | (P1') + (Mv2) 串接 | $\mathbf{c}$ 先被 $D$ 縮成 $D\mathbf{c}$，再以 $D\mathbf{c}$ 為係數線組 $X$ 的列 | $X e^{\Lambda t} \mathbf{c}$ 通解 |
| **(P4)** | $U \Sigma V^{\mathrm{T}} = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ | (P1') + (MM4) 串接 | $\Sigma$ 先把 $V^{\mathrm{T}}$ 各行縮成 $\sigma_p \mathbf{v}^{\mathrm{T}}_p$，再用 (MM4) 把 $U$ 列 ⊗ 縮放後的行做秩 1 累加 | **特徵值 / SVD 分解共骨架** |

### (P1) Pattern 1 — 從右乘任意矩陣（列運算）

**公式：** $A B$，其中 $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$ 任意。

由 (MM2) + (Mv2) 知道：

$$
A B = A \begin{bmatrix} \mathbf{b}_1 & \cdots & \mathbf{b}_n \end{bmatrix} = \begin{bmatrix} A\mathbf{b}_1 & \cdots & A\mathbf{b}_n \end{bmatrix}, \qquad A\mathbf{b}_j = \sum_{p=1}^k b_{pj} \mathbf{a}_p
$$

- **直覺：** 從**右**乘 $B$ 是「**列運算**」 — $B$ 每一直立列 $\mathbf{b}_j$ 都是「混合 $A$ 列的配方」。三個 $\mathbf{b}_j$ 各自混出一條 $\mathbf{c}_j$。
- **關鍵推論：** $\mathbf{C}(AB) \subseteq \mathbf{C}(A)$。

### (P2) Pattern 2 — 從左乘任意矩陣（行運算）

**公式：** $A B$，把 $A$ 視為「左側操作對 $B$」（即 $A$ 是對 $B$ 行做線組的係數矩陣）。對應 (MM3) + (vM2)：

$$
A B = \begin{bmatrix} \mathbf{a}^*_1 \\ \vdots \\ \mathbf{a}^*_m \end{bmatrix} B = \begin{bmatrix} \mathbf{a}^*_1 B \\ \vdots \\ \mathbf{a}^*_m B \end{bmatrix}, \qquad \mathbf{a}^*_i B = \sum_{p=1}^k a_{ip} \mathbf{b}^*_p
$$

- **直覺：** 從**左**乘 $A$ 是「**行運算**」 — $A$ 每一橫躺行 $\mathbf{a}^*_i$ 都是「混合 $B$ 行的配方」。三個 $\mathbf{a}^*_i$ 各自混出一條 $\mathbf{c}^*_i$。
- **關鍵推論：** $\mathbf{C}((AB)^{\mathrm{T}}) \subseteq \mathbf{C}(B^{\mathrm{T}})$（即「行空間」遺傳自 $B$）。
- **(P1) ↔ (P2) 對偶口訣：** 「**從右乘看 $B$ 直立列、從左乘看 $A$ 橫躺行**」。

### (P1') Pattern 1' — 從右乘對角矩陣（純列縮放）

**公式：** 設 $A \in \mathbb{R}^{m \times n}$、$D = \operatorname{diag}(d_1, \ldots, d_n) \in \mathbb{R}^{n \times n}$，則：

$$
A D = \begin{bmatrix} \mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n \end{bmatrix} \begin{bmatrix} d_1 & & \\ & \ddots & \\ & & d_n \end{bmatrix} = \begin{bmatrix} d_1 \mathbf{a}_1 & d_2 \mathbf{a}_2 & \cdots & d_n \mathbf{a}_n \end{bmatrix}
$$

- **直覺：** 對角矩陣從右乘 → **第 $p$ 直立列被 $d_p$ 縮放**（不混合，純倍率）。視覺上 $A$ 的綠直立列「各自被自己對應的對角元素拉長 / 縮短」。
- **(P1) 的退化情形：** 把 $B$ 設為對角矩陣，(P1) 中「線組混合」退化成「純倍率」 — 每個 $\mathbf{c}_j$ 只用到 $A$ 的一條列（其他係數為 0）。
- **§6 用途：** $S = Q \Lambda Q^{\mathrm{T}}$ 中的 $Q\Lambda$ 步驟 = $Q$ 從右乘 $\Lambda$ → 每個特徵向量 $\mathbf{q}_p$ 被自己的特徵值 $\lambda_p$ 縮放；$A = U \Sigma V^{\mathrm{T}}$ 中的 $U\Sigma$ 步驟同理 → 每個左奇異向量 $\mathbf{u}_p$ 被自己的奇異值 $\sigma_p$ 縮放。

### (P2') Pattern 2' — 從左乘對角矩陣（純行縮放）

**公式：** 設 $B \in \mathbb{R}^{m \times n}$、$D = \operatorname{diag}(d_1, \ldots, d_m) \in \mathbb{R}^{m \times m}$，則：

$$
D B = \begin{bmatrix} d_1 & & \\ & \ddots & \\ & & d_m \end{bmatrix} \begin{bmatrix} \mathbf{b}^*_1 \\ \vdots \\ \mathbf{b}^*_m \end{bmatrix} = \begin{bmatrix} d_1 \mathbf{b}^*_1 \\ \vdots \\ d_m \mathbf{b}^*_m \end{bmatrix}
$$

- **直覺：** 對角矩陣從左乘 → **第 $p$ 橫躺行被 $d_p$ 縮放**。視覺上 $B$ 的粉紅橫躺行「各自被自己對應的對角元素拉長 / 縮短」。
- **(P2) 的退化情形：** 把 $A$ 設為對角矩陣，(P2) 中「行線組」退化成「純倍率」。
- **§6 用途：** $\Lambda Q^{\mathrm{T}}$ 步驟（$\Lambda$ 從左乘 $Q^{\mathrm{T}}$ → 每個 $\mathbf{q}^{\mathrm{T}}_p$ 被 $\lambda_p$ 縮放）；$\Sigma V^{\mathrm{T}}$ 步驟（$\Sigma$ 從左乘 $V^{\mathrm{T}}$ → 每個 $\mathbf{v}^{\mathrm{T}}_p$ 被 $\sigma_p$ 縮放）。

### (P1') ↔ (P2') 對偶總表

| 視角 | 公式 | 直覺 | 對應 §4 視角 |
|---|---|---|---|
| **(P1')** $AD$ | 對角矩陣**從右**乘 → **每一直立列**乘對角元素 | 「直立列縮放」（綠列拉長 / 縮短） | (MM2) 之退化 |
| **(P2')** $DB$ | 對角矩陣**從左**乘 → **每一橫躺行**乘對角元素 | 「橫躺行縮放」（粉紅行拉長 / 縮短） | (MM3) 之退化 |

**口訣：** 「**右乘對角 → 縮直立列、左乘對角 → 縮橫躺行**」 — 這是對角矩陣最基礎的視覺角色，整個 §6 都會反覆用到。

### (P3) Pattern 3 — 三明治 $X D \mathbf{c}$（特徵基底加權線組）

**公式：** 設 $X = [\mathbf{x}_1\ \cdots\ \mathbf{x}_n] \in \mathbb{R}^{n \times n}$（可逆）、$D = \operatorname{diag}(d_1, \ldots, d_n)$、$\mathbf{c} \in \mathbb{R}^n$。則：

$$
X D \mathbf{c} = X \begin{bmatrix} d_1 c_1 \\ d_2 c_2 \\ \vdots \\ d_n c_n \end{bmatrix} = \sum_{p=1}^n c_p\, d_p\, \mathbf{x}_p
$$

**兩步拆解：** ① 先 $D \mathbf{c}$ → 把 $\mathbf{c}$ 的每個分量乘以對應的 $d_p$（這是 (Mv2) 的退化 — 對角矩陣作用在向量上 = 分量逐個縮放）；② 再 $X (D\mathbf{c})$ → 用 $D\mathbf{c}$ 為係數對 $X$ 的列做線組（這是 (Mv2) 標準形式）。

#### §6.4 微分方程 / 遞迴方程的工程動機

**設定：** $A \in \mathbb{R}^{n \times n}$、$\mathbf{u}(0) = \mathbf{u}_0$。考慮兩類動態系統：

$$
\frac{d \mathbf{u}(t)}{dt} = A \mathbf{u}(t) \quad \text{（連續時間）}; \qquad \mathbf{u}_{n+1} = A \mathbf{u}_n \quad \text{（離散時間）}
$$

設 $A$ 有特徵分解 $A = X \Lambda X^{-1}$（$\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$、$X$ 列為特徵向量 $\mathbf{x}_p$），且初始條件可被特徵基底展開：

$$
\mathbf{u}_0 = c_1 \mathbf{x}_1 + \cdots + c_n \mathbf{x}_n \quad \Longleftrightarrow \quad \mathbf{c} = X^{-1} \mathbf{u}_0
$$

則兩類問題的通解都是 (P3) 形式：

$$
\boxed{
\mathbf{u}(t) = e^{At} \mathbf{u}_0 = X e^{\Lambda t} X^{-1} \mathbf{u}_0 = X e^{\Lambda t} \mathbf{c} = \sum_{p=1}^n c_p\, e^{\lambda_p t}\, \mathbf{x}_p
}
$$

$$
\boxed{
\mathbf{u}_n = A^n \mathbf{u}_0 = X \Lambda^n X^{-1} \mathbf{u}_0 = X \Lambda^n \mathbf{c} = \sum_{p=1}^n c_p\, \lambda_p^n\, \mathbf{x}_p
}
$$

對應 (P3) 中的 $D$ 各為「$e^{\Lambda t}$」與「$\Lambda^n$」 — 兩者都是對角矩陣，元素分別是 $e^{\lambda_p t}$ 與 $\lambda_p^n$。

- **直覺三層：** ① 把初始條件 $\mathbf{u}_0$ 用特徵向量基底寫成 $\mathbf{c}$（座標變換）；② 每個特徵分量按自己的特徵值「演化」（連續時間：$e^{\lambda_p t}$ 指數成長 / 衰減；離散時間：$\lambda_p^n$ 幾何級數）；③ 把演化後的分量重新組裝回原座標系（線組 $X$ 列）。
- **特徵值分類：** $\operatorname{Re}(\lambda_p) > 0$ → 該分量爆炸成長；$\operatorname{Re}(\lambda_p) < 0$ → 該分量衰減；$\operatorname{Re}(\lambda_p) = 0, \operatorname{Im}(\lambda_p) \neq 0$ → 純振盪；$|\lambda_p| > 1$（離散）→ 不穩定；$|\lambda_p| < 1$ → 穩定收斂到 0。
- **§6 鋪陳：** (P3) 是「為什麼要做特徵分解」的工程理由 — 解動態系統的標準工具。§6.4 會把這個構造完整展開。

### (P4) Pattern 4 — 三明治 $U \Sigma V^{\mathrm{T}}$（兩矩陣夾對角的秩 1 之和）

**公式：** 設 $U \in \mathbb{R}^{m \times r}$、$\Sigma = \operatorname{diag}(\sigma_1, \ldots, \sigma_r)$、$V^{\mathrm{T}} \in \mathbb{R}^{r \times n}$。則：

$$
U \Sigma V^{\mathrm{T}} = \underbrace{\begin{bmatrix} \mathbf{u}_1 & \cdots & \mathbf{u}_r \end{bmatrix}}_{U} \underbrace{\begin{bmatrix} \sigma_1 & & \\ & \ddots & \\ & & \sigma_r \end{bmatrix}}_{\Sigma} \underbrace{\begin{bmatrix} \mathbf{v}^{\mathrm{T}}_1 \\ \vdots \\ \mathbf{v}^{\mathrm{T}}_r \end{bmatrix}}_{V^{\mathrm{T}}} = \sum_{p=1}^r \sigma_p\, \mathbf{u}_p\, \mathbf{v}^{\mathrm{T}}_p
$$

**兩步拆解：** ① 先 $\Sigma V^{\mathrm{T}}$ → (P2') 縮放每個 $\mathbf{v}^{\mathrm{T}}_p$ 為 $\sigma_p \mathbf{v}^{\mathrm{T}}_p$；② 再 $U(\Sigma V^{\mathrm{T}})$ → (MM4) 把 $U$ 列 ⊗ 縮放後的行做秩 1 累加。

或等價地：① 先 $U \Sigma$ → (P1') 縮放每個 $\mathbf{u}_p$ 為 $\sigma_p \mathbf{u}_p$；② 再 $(U\Sigma) V^{\mathrm{T}}$ → (MM4) 累加。

- **直覺：** **「兩個正交基底 + 一個對角矩陣 = 矩陣的最簡分解」** — $U$ 的列是「結果的基底」、$V^{\mathrm{T}}$ 的行是「來源的基底」、$\Sigma$ 的對角元素 $\sigma_p$ 是「兩基底之間的伸縮率」。
- **(P4) 同時是特徵值與 SVD 的骨架：**
  - **特徵值分解（對稱矩陣）：** $S = Q \Lambda Q^{\mathrm{T}} = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$（兩基底相同 = $Q$）。
  - **SVD（任意矩陣）：** $A = U \Sigma V^{\mathrm{T}} = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$（兩基底不同）。
- **§6 鋪陳：** (P4) 是 (P3) 的「矩陣化」 — (P3) 是 $X D \mathbf{c}$（一個向量），(P4) 是 $U \Sigma V^{\mathrm{T}}$（一個矩陣）。**P3 處理動態系統、P4 處理矩陣分解，都靠對角矩陣承載「按 index 加權」的本質。**

### (P3) ↔ (P4) 對偶與升級

| 視角 | 公式 | 對角元素角色 | 結果類型 | §6 章節 |
|---|---|---|---|---|
| **(P3)** $X D \mathbf{c}$ | $\sum_p c_p d_p \mathbf{x}_p$ | $d_p = e^{\lambda_p t}$ 或 $\lambda_p^n$ — 動態演化因子 | 向量（$\mathbf{u}(t)$ 或 $\mathbf{u}_n$） | §6.4 特徵值分解 |
| **(P4)** $U \Sigma V^{\mathrm{T}}$ | $\sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ | $\sigma_p$ — 兩基底間的伸縮率 | 矩陣（$A$ 本身） | §6.4 ($Q\Lambda Q^{\mathrm{T}}$) / §6.5 ($U\Sigma V^{\mathrm{T}}$) |

**結論口訣：** 「**對角矩陣 = 按 index 加權**」 — (P1')(P2') 對 column / row 做加權、(P3) 對「特徵分量的動態演化」做加權、(P4) 對「秩 1 圖層的能量」做加權。從 (P1') 到 (P4) 是同一概念的層層升級。

---

## Figure 5.1: Pattern 1, 2 — (P1), (P2)

> **檔案：** `figs-png/Pattern12.png`
> **原書位置：** Figure 7（p.5 上半）

#### 視覺結構 (Visual Structure)

整圖**上下兩排**，上排展示 (P1)、下排展示 (P2)，左右各分三段（左 = 等號形式、中 = 解構成 3 條子等式、右 = 「using …」標籤連回 §4 視角）。

- **上排（P1）：** 左段顯示「3 條綠直立列 $A$ × 3×3 灰底點陣 $B$ = 3 條灰直立列 $C$」；中段把 $C$ 展開成 3 條獨立子等式：「$\mathbf{c}_1 = \bullet \cdot \mathbf{a}_1 + \bullet \cdot \mathbf{a}_2 + \bullet \cdot \mathbf{a}_3$」「$\mathbf{c}_2 = \cdots$」「$\mathbf{c}_3 = \cdots$」（每個 $\bullet$ 是來自 $B$ 直立列的對應分量，淡藍 / 橘 / 紫三色區分對應 $B$ 的 3 直立列）；右段「using MM2 + Mv2」標籤。
- **下排（P2）：** 左段顯示「3 條粉紅橫躺行（縱向 stack）$A$ × 3 條粉紅橫躺行 $B$ = 3 條灰橫躺行 $C$」（注意此處 $A$ 是「從左乘的對象」，視覺上仍標 $B$ 在右、$A$ 在左 — 但**作用方向相反**）；中段展開 3 條子等式：「$\mathbf{c}^*_1 = \bullet \cdot \mathbf{b}^*_1 + \bullet \cdot \mathbf{b}^*_2 + \bullet \cdot \mathbf{b}^*_3$」⋯ ；右段「using MM3 + vM2」標籤。
- **配色：** $A$ 的列綠 `#2ca02c`、$B$ 的行粉紅 `#d62728`、係數藍 / 橘 / 紫圓點對應 §4 中「係數來源」、$C$ 灰填充 `#eeeeee` + 深灰框 `#333333`。

#### 數學內容 (Mathematical Content)

(P1)：$AB = [A\mathbf{b}_1\ A\mathbf{b}_2\ A\mathbf{b}_3] = [b_{11}\mathbf{a}_1+b_{21}\mathbf{a}_2+b_{31}\mathbf{a}_3,\ \ldots]$。

(P2)：$AB = [\mathbf{a}^*_1 B;\ \mathbf{a}^*_2 B;\ \mathbf{a}^*_3 B]$，每行 = $a_{i1}\mathbf{b}^*_1 + a_{i2}\mathbf{b}^*_2 + a_{i3}\mathbf{b}^*_3$。

兩排對比：(P1) 的「係數來自 $B$ 的直立列」與 (P2) 的「係數來自 $A$ 的橫躺行」是嚴格對偶（轉置）。

#### 直覺解讀 (Intuition)

「**從右乘 = 切 $B$ 的直立列做 $A$ 列的線組（P1）；從左乘 = 切 $A$ 的橫躺行做 $B$ 行的線組（P2）**」。這張圖把 §4 (MM2) (MM3) 的核心訊息「**乘法方向決定切誰**」用「3 條子等式並列」的視覺方式強調出來。中央展開的子等式把整個 $C$ 拆成「逐列 / 逐行」獨立計算 — 這對寫程式的人是極自然的視角（NumPy 的 for-loop 視角）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [對角矩陣統一互動] ⭐⭐⭐
> **位置：** Figure 5.1 + Figure 5.2 / §5 / (P1) (P2) (P1') (P2') 統合
> **詳見劇本：** VizScript-01（章末）

---

## Figure 5.2: Pattern 1', 2' — (P1'), (P2')

> **檔案：** `figs-png/Pattern11-22.png`
> **原書位置：** Figure 8（p.5 下半）

#### 視覺結構 (Visual Structure)

整圖**左右兩塊**，左塊 (P1')、右塊 (P2')，每塊各分上下兩段（上 = 色塊等式、下 = 文字描述 + 公式）。

- **左塊（P1' — $AD$，從右乘對角）：** 上段顯示「3 條綠直立列 $A$ × 對角 $D$（用 3 個藍色實心圓點沿對角線排列、其餘位置留白）= 3 條綠直立列 $AD$（與 $A$ 同色但每條被『藍點疊在頂端』 — 視覺暗示『被縮放』）」；下段文字「Applying a diagonal matrix from the right scales each column.」+ 公式 `AD = [a₁ a₂ a₃] diag(d₁, d₂, d₃) = [d₁a₁ d₂a₂ d₃a₃]`。
- **右塊（P2' — $DB$，從左乘對角）：** 上段顯示「對角 $D$（藍點對角排列）× 3 條粉紅橫躺行 $B$（縱向 stack）= 3 條粉紅橫躺行 $DB$（每條疊一個藍點在最左 — 暗示『被縮放』）」；下段文字「Applying a diagonal matrix from the left scales each row.」+ 公式 `DB = diag(d₁, d₂, d₃) [b₁*; b₂*; b₃*] = [d₁b₁*; d₂b₂*; d₃b₃*]`。
- **配色：** $A$ 列綠 `#2ca02c`、$B$ 行粉紅 `#d62728`、對角元素藍 `#1f77b4` 圓點（直徑 12px）；對角矩陣的「非對角位置」**完全留白**（不畫 0 元素，視覺強調「對角矩陣 = 只有對角線存在」）。

#### 數學內容 (Mathematical Content)

(P1')：$A D = [d_1 \mathbf{a}_1\ d_2 \mathbf{a}_2\ d_3 \mathbf{a}_3]$ — 每一直立列被自己對應的對角元素縮放。

(P2')：$D B = [d_1 \mathbf{b}^*_1;\ d_2 \mathbf{b}^*_2;\ d_3 \mathbf{b}^*_3]$ — 每一橫躺行被自己對應的對角元素縮放。

對偶：$(AD)^{\mathrm{T}} = D^{\mathrm{T}} A^{\mathrm{T}} = D A^{\mathrm{T}}$（對角矩陣 $D = D^{\mathrm{T}}$），故 (P1') 與 (P2') 完全是「轉置對稱」的兩面。

#### 直覺解讀 (Intuition)

「**右乘對角 → 縮直立列；左乘對角 → 縮橫躺行**」 — 對角矩陣是矩陣世界中**最簡單的「按 index 加權」工具**，不混合任何資訊，純倍率。這個極簡視覺（綠列被「藍點戴上帽子」拉長 / 縮短）是 §6.4 / §6.5 整個分解骨架的視覺起點 — $Q\Lambda$ 之 $\Lambda$、$U\Sigma$ 之 $\Sigma$，都是這個「列縮放動畫」。讀者若能在 0.5 秒內看懂 (P1')、就有資格挑戰 (P4)；若能再 0.5 秒看懂 (P4)、SVD 的視覺骨架已掌握 80%。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [對角矩陣統一互動] ⭐⭐⭐
> **位置：** Figure 5.1 + Figure 5.2 / §5 / 4 個 Pattern 統合
> **核心概念：** 一鍵切換 (P1) (P2) (P1') (P2') 看「右 / 左乘」與「任意 / 對角」二維對比
> **互動梗概：** 4 個 tab 切換 + 對角元素 slider 拉動時看到「綠列各自被縮放」的動畫；切換成 (P1) 時 $B$ 從對角矩陣補滿成任意矩陣，視覺上出現「線組混合」效果
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-04** [數值步進] ⭐
> **位置：** Figure 5.2 / §5 / (P1') 數值 walkthrough
> **詳見劇本：** VizScript-04（章末，輕量版）

---

## Figure 5.3: Pattern 3 — (P3) — $X D \mathbf{c}$ 三明治

> **檔案：** `figs-png/Pattern3.png`
> **原書位置：** Figure 9（p.6）

#### 視覺結構 (Visual Structure)

整圖**橫向布局**，左中右三段。

- **左段：** 「3 條綠直立列 $X$（$\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3$）× 對角 $D$（藍點 stack）× 一條紫色實心直立列 $\mathbf{c}$（紫圓點 stack 縱向 3 個）」 — 三明治結構左半邊。
- **中段：** 「$=$」 + 三項相加 「$\bullet \cdot \mathbf{x}_1 + \bullet \cdot \mathbf{x}_2 + \bullet \cdot \mathbf{x}_3$」 — 每個 $\bullet$ 是「藍 + 紫」雙圓點（暗示『$d_p \cdot c_p$』兩因子相乘）疊在綠列前。
- **右段：** 文字描述「This pattern makes another combination of columns. You will encounter this in differential/recurrence equations.」+ 完整公式 `XDc = [x₁ x₂ x₃] diag(d₁, d₂, d₃) [c₁; c₂; c₃] = c₁d₁x₁ + c₂d₂x₂ + c₃d₃x₃`。
- **配色：** 特徵向量 $X$ 列綠（與 $A$ 列同色，提示「列空間概念繼承」）、對角 $D$ 元素藍、係數向量 $\mathbf{c}$ 紫 `#9467bd`（新色 — 為「特徵基底中的座標」獨立配色）、結果項中的雙圓點是「藍 + 紫」並排顯示 $d_p \cdot c_p$。

#### 數學內容 (Mathematical Content)

$X D \mathbf{c} = X \begin{bmatrix} d_1 c_1 \\ d_2 c_2 \\ d_3 c_3 \end{bmatrix} = c_1 d_1 \mathbf{x}_1 + c_2 d_2 \mathbf{x}_2 + c_3 d_3 \mathbf{x}_3$ — 三因子相乘 $\sum c_p d_p \mathbf{x}_p$。

兩步拆解：
1. **先 $D \mathbf{c}$**（(Mv2) 退化）：$\mathbf{c}$ 各分量被對應對角元素縮放，得到新向量 $D\mathbf{c} = (d_1 c_1, d_2 c_2, d_3 c_3)^{\mathrm{T}}$。
2. **再 $X (D\mathbf{c})$**（(Mv2) 標準）：用 $D\mathbf{c}$ 為係數對 $X$ 列做線組。

或等價地：先 $X D$（(P1') 縮放 $X$ 各列為 $d_p \mathbf{x}_p$）、再 $(XD) \mathbf{c}$（(Mv2) 線組）。

**§6.4 微分 / 遞迴方程通解的具體實例：**

- 連續：$\mathbf{u}(t) = X e^{\Lambda t} \mathbf{c} = \sum c_p e^{\lambda_p t} \mathbf{x}_p$，這裡 $D = e^{\Lambda t} = \operatorname{diag}(e^{\lambda_p t})$。
- 離散：$\mathbf{u}_n = X \Lambda^n \mathbf{c} = \sum c_p \lambda_p^n \mathbf{x}_p$，這裡 $D = \Lambda^n = \operatorname{diag}(\lambda_p^n)$。

#### 直覺解讀 (Intuition)

(P3) 的精髓是「**換基底 → 各分量獨立演化 → 換回原基底**」三段式：

1. **換基底：** $\mathbf{c} = X^{-1} \mathbf{u}_0$，把原座標 $\mathbf{u}_0$ 換成「特徵基底中的座標 $\mathbf{c}$」。
2. **各分量獨立演化：** 在特徵基底裡，$A$ 變成對角矩陣 $\Lambda$，每個分量 $c_p$ 各自按 $e^{\lambda_p t}$ 或 $\lambda_p^n$ 演化（互不干擾） — 這就是對角矩陣 $D$ 出現的原因。
3. **換回原基底：** $X (D\mathbf{c})$ 把演化後的特徵分量重新組裝回原座標。

**為何要做特徵分解？** 因為「**對角矩陣容易處理 — 無耦合**」。沒有特徵分解的話，連續系統需要解 $n$ 個耦合微分方程；做了特徵分解 $A = X \Lambda X^{-1}$，就變成 $n$ 個獨立的標量方程（每個只涉及一個 $\lambda_p$）。**(P3) 是「為什麼特徵值是工程師的最好朋友」的視覺答案。**

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-02** [P3 動態系統 demo] ⭐⭐⭐
> **位置：** Figure 5.3 / §5 / (P3) + §6.4 鋪陳
> **核心概念：** 拉時間 $t$ slider 看 $\mathbf{u}(t) = \sum c_p e^{\lambda_p t} \mathbf{x}_p$ 的軌跡，分量按特徵值各自演化
> **詳見劇本：** VizScript-02（章末）

---

## Figure 5.4: Pattern 4 — (P4) — $U \Sigma V^{\mathrm{T}}$ 三明治

> **檔案：** `figs-png/Pattern4.png`
> **原書位置：** Figure 10（p.7）

#### 視覺結構 (Visual Structure)

整圖**橫向布局**，左中右三段。

- **左段：** 「3 條綠直立列 $U$（$\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3$）× 對角 $\Sigma$（藍點 stack）× 3 條粉紅橫躺行 $V^{\mathrm{T}}$（縱向 stack）」 — 完整三明治結構。
- **中段：** 「$=$」 + 三個秩 1 矩陣方塊相加 「$\sigma_1 \mathbf{u}_1 \mathbf{v}^{\mathrm{T}}_1 + \sigma_2 \mathbf{u}_2 \mathbf{v}^{\mathrm{T}}_2 + \sigma_3 \mathbf{u}_3 \mathbf{v}^{\mathrm{T}}_3$」 — 每個秩 1 矩陣方塊用「灰底 + 一條綠直立列疊在最左 + 一條粉紅橫躺行疊在最上 + 藍圓點在交叉處」的「**十字交叉**」視覺表示「綠 ⊗ 粉紅」外積結構。秩 1 矩陣**方塊間**有「+」號連接、最左有「$=$」連接到三明治。
- **右段：** 文字描述「A matrix is broken down to a sum of rank 1 matrices, as in singular value/eigenvalue decomposition.」+ 完整公式 `UΣVᵀ = [u₁ u₂ u₃] diag(σ₁, σ₂, σ₃) [v₁ᵀ; v₂ᵀ; v₃ᵀ] = σ₁u₁v₁ᵀ + σ₂u₂v₂ᵀ + σ₃u₃v₃ᵀ`。
- **配色：** $U$ 列綠、$V^{\mathrm{T}}$ 行粉紅、$\Sigma$ 對角藍點（點直徑與 P3 同 12px，提示「同類角色」）、秩 1 矩陣方塊內部灰填 + 邊框 `#333333` 凸顯外積結構。

#### 數學內容 (Mathematical Content)

$U \Sigma V^{\mathrm{T}} = \sum_{p=1}^r \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ — 三因子相乘等於 $r$ 個秩 1 矩陣按 $\sigma_p$ 加權後相加。

兩步拆解（兩種等價路徑）：
- **路徑 A：** 先 $\Sigma V^{\mathrm{T}}$（(P2') 縮放每行為 $\sigma_p \mathbf{v}^{\mathrm{T}}_p$），再 $U(\Sigma V^{\mathrm{T}})$（(MM4) 累加）。
- **路徑 B：** 先 $U \Sigma$（(P1') 縮放每列為 $\sigma_p \mathbf{u}_p$），再 $(U\Sigma) V^{\mathrm{T}}$（(MM4) 累加）。

**重要特例：**
- **特徵值分解（對稱矩陣）：** $S = Q \Lambda Q^{\mathrm{T}}$ — 同一個正交矩陣 $Q$ 同時擔任「左基底」與「右基底」（轉置版）。$Q\Lambda Q^{\mathrm{T}} = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$。
- **SVD（任意矩陣）：** $A = U \Sigma V^{\mathrm{T}}$ — 兩個不同的正交矩陣 $U, V$ 分別是「左 / 右」基底。
- **共通骨架：** 都是「**正交基底 + 對角矩陣 + 正交基底**」的三明治。**對角元素的大小決定該秩 1 圖層的「能量」**，取前 $k$ 大者是最佳低秩近似（Eckart–Young）。

#### 直覺解讀 (Intuition)

(P4) 是 (MM4) 的「**結構化版本**」 — (MM4) 對任何 $AB$ 都成立，但 (P4) 加了三個約束讓拆解「最有意義」：

1. **$U$ 與 $V$ 都正交**（$U^{\mathrm{T}} U = I$、$V^{\mathrm{T}} V = I$） → 秩 1 圖層之間「**幾何上正交**」，互不干擾。
2. **對角矩陣 $\Sigma$ 元素非負且降冪排列**（$\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r > 0$） → 「**前面的圖層比後面的重要**」 — 截斷時保留前 $k$ 個自動是最佳。
3. **唯一性：** 對任何 $A$，這樣的 $U, \Sigma, V$ 存在且基本唯一（差異僅在 $\sigma$ 重複時的旋轉自由度）。

**為何 (P4) 是「整本書的終點」？** 因為它把 §1（4 視角看矩陣）、§2（向量乘法）、§3（矩陣 × 向量）、§4 (MM4)（外積之和）、§5 (P1')(P2')（對角縮放）全部整合到一個結構裡。**讀完 (P4) 等於讀完整本書的視覺骨架**，§6 後面的 5 個分解都只是「填細節 + 加性質約束」。

> 💡 **與 ch04 VizScript-02 的關係：** ch04 已用 Mona Lisa 64×64 SVD 做完整動畫示範「秩 1 圖層累加 + 截斷誤差」，本章不重做 — 直接 pointer 到 ch04，僅在 VizScript-03 補一個「**P4 三明治結構互動**」（Tier 1 輕量版）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-03** [P4 三明治結構] ⭐⭐
> **位置：** Figure 5.4 / §5 / (P4) + §6.4 / §6.5 鋪陳
> **詳見劇本：** VizScript-03（章末，精簡 — 累加動畫指向 ch04 VizScript-02）

---

## 視覺化劇本（VizScripts）

### VizScript-01: 對角矩陣統一互動（P1 / P2 / P1' / P2' Toggle）

#### A. 一句話定位
單一畫面 4 個 tab 切換 (P1) (P2) (P1') (P2')，看「**右乘 / 左乘**」與「**任意矩陣 / 對角矩陣**」二維對比 — 對角矩陣 slider 拉動時，視覺即時呈現「綠直立列被自己的對角元素拉長 / 縮短」（P1'）或「粉紅橫躺行被自己的對角元素拉長 / 縮短」（P2'）的純倍率動畫；切換到 (P1) (P2) 時 $B$ / $A$ 從對角矩陣「補滿」成任意矩陣，視覺上出現「線組混合」漸入效果。

#### B. 學習目標（Learning Outcome）
- 使用者能在 4 個 tab 之間自由切換並指出每個視角下「縮放對象 / 縮放因子」的視覺位置。
- 使用者能說出「右乘對角 → 縮直立列、左乘對角 → 縮橫躺行」口訣。
- 使用者能在「對角元素 → 任意元素」漸入動畫中觀察到「(P1') 是 (P1) 的退化、(P2') 是 (P2) 的退化」。
- 使用者能拉 $d_p$ 滑桿到 0 看到對應直立列 / 橫躺行「整條消失」 — 直觀理解「對角元素為 0 = 該維度被刪除」（連到 §6.5 SVD 的低秩截斷）。
- 使用者能在切換 (P1) ↔ (P2) 時觀察到視覺上的「**轉置對稱**」 — 兩者完全是「左 ↔ 右、列 ↔ 行」鏡像。

#### C. 待視覺化的數學物件
- **物件清單：** 矩陣 $A \in \mathbb{R}^{m \times n}$（綠直立列 stack）、矩陣 $B \in \mathbb{R}^{m \times n}$（粉紅橫躺行 stack）、對角矩陣 $D \in \mathbb{R}^{n \times n}$（藍點 stack）、結果矩陣 $C$（依模式以「縮放後的綠 / 粉紅」表示）。
- **預設值：** $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$、$D = \operatorname{diag}(1, 2, 3)$、$B = D$（初始狀態 (P1') = (P1) 的退化）。
- **維度範圍：** $m, n \in [2, 5]$（保持 cell 視覺清晰）。
- **數值範圍：** $a_{ij}, b_{ij} \in [-9, 9]$ 步進 1；$d_p \in [-3, 3]$ 步進 0.5（對角元素範圍縮小，便於觀察直立列「拉長 / 縮短」效果）。
- **退化情形：**
  - $D = I$：(P1') (P2') 結果與輸入完全相同（無縮放）。
  - $d_p = 0$ 對某 $p$：對應第 $p$ 直立列 / 橫躺行整條變灰、消失。
  - $D$ 元素全相同 = $\alpha$：所有列 / 行被同一倍率縮放（純標量乘法 $\alpha A$）。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 65% 主舞台 + 中 10% 公式區 + 下 25% 控制列。
- **主舞台：** 1100×360 px 白底，左 30% 顯示「左乘運算元」、中 10% 顯示乘號、右 30% 顯示「右乘運算元」、再右 30% 顯示等號 + 結果。依模式不同，左 / 右運算元身分對調：
  - **(P1) mode：** 左 = $A$（綠直立列）、右 = $B$（任意，灰底 + 細格線）。
  - **(P2) mode：** 左 = $A$（任意，灰底 + 細格線）、右 = $B$（粉紅橫躺行）。
  - **(P1') mode：** 左 = $A$（綠直立列）、右 = $D$（藍點對角，無背景框）。
  - **(P2') mode：** 左 = $D$（藍點對角）、右 = $B$（粉紅橫躺行）。
- **對角矩陣表現：** 藍圓點直徑 14px，沿對角線排列，**非對角位置完全留白**（不畫 0 元素，視覺強調「只有對角線存在」）。
- **結果區色塊：** 縮放後的列 / 行用「原色 + 寬度依 $|d_p|$ 比例縮放」呈現（如 $d_2 = 2$ 時第 2 列寬度變 2 倍；$d_2 = 0.5$ 時變 0.5 倍）。負 $d_p$ 用「漸層斜線」紋理表示「方向反轉」。
- **配色：** 綠 `#2ca02c` / 粉紅 `#d62728` / 藍對角 `#1f77b4` / 灰填 `#eeeeee` / 漸層 alpha 0.3 / 負值斜線紋理。
- **公式區：** 即時 LaTeX 14pt mono。
- **字型 / 字級：** 視角標題 18pt sans bold、cell 數字 12pt mono、控制列 12pt。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 視角 mode | tab × 4 | P1 / P2 / P1' / P2' | P1' | 即時 + 動畫 |
| $m$ | slider | [2, 5] | 3 | 即時 |
| $n$ | slider | [2, 5] | 3 | 即時 |
| $a_{ij}$（綠列模式時） | slider grid | [-9, 9] step 1 | 1..9 | 即時 |
| $b_{ij}$（粉紅行模式時） | slider grid | [-9, 9] step 1 | 0..0 | 即時 |
| $d_p$（對角模式時） | slider × $n$ | [-3, 3] step 0.5 | 1, 2, 3 | 即時 |
| 「補滿成任意矩陣」 | button | — | — | click → 從 $D$ 漸入到任意 $B$（觸發 800ms 動畫） |
| 公式逐項高亮 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click |

#### F. 輸出畫面細節（Outputs）
- **(P1') 模式：** 結果區 $n$ 條綠直立列各自寬度 = 原寬 × $|d_p|$；每條列上方標 `$d_p \mathbf{a}_p$`；對角矩陣藍點的圓點半徑與 $|d_p|$ 成正比（視覺加強）。
- **(P2') 模式：** 結果區 $m$ 條粉紅橫躺行各自高度 = 原高 × $|d_p|$；每條行左方標 `$d_p \mathbf{b}^*_p$`。
- **(P1) 模式：** 結果區 $n$ 條綠直立列，每條為「$A$ 列的線性組合」，顯示「$\mathbf{c}_j = b_{1j}\mathbf{a}_1 + b_{2j}\mathbf{a}_2 + \ldots$」公式 + 各 $\mathbf{a}_p$ 對應位置以淡色虛線連到結果列。
- **(P2) 模式：** 對偶行為。
- **公式區：** 依模式即時 LaTeX 顯示對應 (P1)–(P2') 之一。
- **左下角狀態列：** `mode: P1' | shape: (3×3)·diag(d) = (3×3) | scale: [1, 2, 3]`。

#### G. 互動行為（Interactions）
- **切換 mode tab：** 觸發 600ms 切換動畫（見 §H）；公式區同步切換 LaTeX。
- **拉動 $d_p$ slider：** 對應第 $p$ 直立列 / 橫躺行寬度（高度）即時更新，動畫 200ms ease-out。
- **拉動 $a_{ij}$ / $b_{ij}$ slider：** cell 內數字立即更新；對應位置高亮 200ms。
- **「補滿成任意矩陣」button：** 從當前對角矩陣 $D$ 漸入到隨機 $B$（800ms），逐 cell 從 0 漸入；動畫過程中視覺上「從 (P1') 漸變成 (P1)」，幫助理解兩者關係。
- **拉動 $m$ / $n$ slider：** 矩陣形狀重繪 + slider grid 重建。
- **快捷鍵：** `1`–`4` → 切到對應 mode、`Space` → mode 循環、`R` → reset、`F` → 觸發「補滿」按鈕。

#### H. 動畫腳本（mode 切換）
- **(P1') → (P1)：**「右側 $D$ 對角藍點 stack 漸入填滿成隨機 $B$ 灰色 cell（800ms 整體 fade-in）」+「結果區的綠列從『純倍率縮放』漸變為『線組混合』顯示淡色虛線連線」。
- **(P1) → (P2)：**「整個畫面左右鏡像翻轉」+「綠列 ↔ 粉紅行對調」+「公式同步翻轉」+「左 / 右運算元身分交換」。動畫 600ms。
- **(P2) → (P2')：**「左側 $A$ 灰色 cell 漸出收回成 $D$ 藍點 stack」+「結果區粉紅行從『線組混合』漸變為『純倍率縮放』」。
- **(P2') → (P1')：**「整個畫面左右鏡像翻轉」+「粉紅行 ↔ 綠列對調」+「對角矩陣從左移到右」。
- **總長度：** 600ms（mode 內切換）/ 800ms（含「補滿」漸入）。
- **緩動：** ease-in-out cubic-bezier(0.4, 0, 0.2, 1)。

#### I. 邊界與錯誤處理
- **$D$ 元素全為 0：** 結果矩陣全 0、灰底 + 提示「對角全 0 = 結果為 0 矩陣」。
- **某 $d_p = 0$：** 對應列 / 行漸隱（opacity 1 → 0.15）+ 邊框虛線 + tooltip「該維度被刪除（rank 降 1）」。
- **拖動 slider 過快：** debounce 30ms。
- **mode 切換中再切換：** 動畫 reverse 後接續到目標。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - P1' tab：「右乘對角 → 縮列：第 $p$ 直立列 × $d_p$」
  - P2' tab：「左乘對角 → 縮行：第 $p$ 橫躺行 × $d_p$」
  - P1 tab：「右乘任意 = 列線組（混合）」
  - P2 tab：「左乘任意 = 行線組（混合）」
  - $d_p$ slider：「拉到 0 看該列消失（rank 降 1）」
  - 「補滿」button：「看 (P1') 怎麼漸變成 (P1) — 對角 → 任意」
- **Walkthrough（首次開啟自動觸發）：**
  - Step 1：「現在是 (P1')：右乘對角矩陣 → 每一綠直立列被自己的藍點縮放」
  - Step 2：「拉 $d_2$ 滑桿從 1 到 3，看第 2 列變寬」
  - Step 3：「拉 $d_2$ 到 0，看第 2 列消失 — rank 降 1」
  - Step 4：「按 `2` 切到 (P2')：對角矩陣移到左邊、改為縮行」
  - Step 5：「按『補滿』看 (P1') → (P1) 的漸變」
- **常見誤解警示：**
  - 「對角矩陣不一定是方陣 — 可以是 $m \times n$ 對角（非對角位置 0），但本章假設方陣以避免混淆」
  - 「右乘對角 ≠ 左乘對角，矩陣乘法不可交換 — 視覺上很明顯：縮列 ≠ 縮行」
- **延伸閱讀：** 原書 p.5–6、§6.4 ($Q\Lambda Q^{\mathrm{T}}$)、§6.5 ($U\Sigma V^{\mathrm{T}}$)。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib + matplotlib.animation + marimo.ui。
- **替代方案：** Streamlit + Plotly。
- **關鍵 API：**
  - `matplotlib.patches.Rectangle` 畫綠列 / 粉紅行 / 灰塊。
  - `matplotlib.patches.Circle` 畫藍對角圓點。
  - `matplotlib.transforms.Affine2D().scale()` 處理「列寬隨 $d_p$ 變化」。
  - `marimo.ui.tabs` (4 modes)、`marimo.ui.slider`、`marimo.ui.array`。
  - `numpy.diag` / `numpy.outer` 計算。
- **檔案結構：**
  ```
  viz/
    ch05_patterns.py             # 主入口（含 VizScript-01 / 02 / 03 / 04）
    _common/
      palette.py                 # 沿用 §1–§4 配色
      matrix_canvas.py           # 沿用：綠列 / 粉紅行 / 灰塊原語
      diagonal_widget.py         # 新增：對角矩陣藍點 stack（含 d_p slider 綁定）
  ```
- **效能：** mode 切換動畫預先計算所有 keyframe；slider 拖動 debounce 30ms。
- **測試：** 4 modes 各 1 張 snapshot；$d_p = 0$ 退化 1 張；「補滿」漸入中段 t=400ms 1 張。

#### L. 驗收標準（Acceptance Criteria）
- [ ] 4 mode tab 切換動畫 ≤ 600ms，60fps。
- [ ] 拉 $d_p$ slider 即時更新對應列 / 行寬度，動畫 ≤ 200ms。
- [ ] $d_p = 0$ 時對應列 / 行 opacity 0.15、邊框虛線、tooltip 顯示「rank 降 1」。
- [ ] 「補滿」button 觸發 800ms 漸入動畫 — 從對角到任意矩陣。
- [ ] 公式區 LaTeX 渲染 < 50ms。
- [ ] Walkthrough 5 步驟自動觸發。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 4 mode 純並列靜態圖、無動畫切換、$d_p$ slider 改用文字 input。
- **Tier 3 擴充：** + 加 3D 視窗顯示「綠列縮放」對列空間幾何的影響（$d_p$ 改變 → 列空間從 3D 平面退化成 2D 直線等）。
- **估時：** 1 session

---

### VizScript-02: P3 動態系統互動（$X D \mathbf{c}$ 與微分 / 遞迴方程）

#### A. 一句話定位
拉時間 $t$ slider 看 $\mathbf{u}(t) = \sum_p c_p e^{\lambda_p t} \mathbf{x}_p$ 的軌跡演化（連續模式）或拉步數 $n$ slider 看 $\mathbf{u}_n = \sum_p c_p \lambda_p^n \mathbf{x}_p$ 的軌跡跳躍（離散模式）；左側 (P3) 三明治結構 $X D \mathbf{c}$ 的對角元素 $d_p = e^{\lambda_p t}$（或 $\lambda_p^n$）即時更新；右側 2D / 3D 軌跡圖即時顯示 $\mathbf{u}$ 在原座標空間的位置 + 各特徵分量分解的「彩色子向量」。

#### B. 學習目標（Learning Outcome）
- 使用者能在「拉 $t$ 滑桿」時直觀感受「**特徵分量按特徵值各自演化**」 — $\lambda > 0$ 分量爆炸、$\lambda < 0$ 分量衰減、$\lambda = 0$ 分量靜止。
- 使用者能說出「(P3) = 換特徵基底 + 各分量獨立演化 + 換回原基底」三步驟。
- 使用者能解釋「對角矩陣為什麼出現 — 因為特徵基底中無耦合」。
- 使用者能在「離散 vs 連續」切換中觀察到 $\lambda^n$ 與 $e^{\lambda t}$ 的差異（$\lambda > 1$ 離散爆炸 vs $\operatorname{Re}(\lambda) > 0$ 連續爆炸）。
- 使用者能在「複數特徵值」demo 中觀察到「振盪 + 衰減 / 成長」的螺旋軌跡（連到 §6.4 的振盪解）。

#### C. 待視覺化的數學物件
- **物件清單：** 特徵向量矩陣 $X = [\mathbf{x}_1, \ldots, \mathbf{x}_n]$（綠直立列 stack）、特徵值對角矩陣 $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$、初始條件係數 $\mathbf{c} = X^{-1} \mathbf{u}_0$（紫直立向量）、時間 $t$（或步數 $n$）、即時對角矩陣 $D(t) = e^{\Lambda t}$（或 $\Lambda^n$）、結果向量 $\mathbf{u}(t) = X D(t) \mathbf{c}$。
- **預設值（兩種模式）：**
  - **2D demo（穩定吸引子）：** $A = \begin{bmatrix} -0.5 & 0 \\ 0 & -0.2 \end{bmatrix}$（已對角，$\lambda_1 = -0.5, \lambda_2 = -0.2$，$\mathbf{x}_1 = (1, 0)^{\mathrm{T}}, \mathbf{x}_2 = (0, 1)^{\mathrm{T}}$），$\mathbf{u}_0 = (3, 2)^{\mathrm{T}}$ → 軌跡螺旋收斂到原點（$t \to \infty$）。
  - **2D demo（振盪）：** $A = \begin{bmatrix} 0 & 1 \\ -1 & 0 \end{bmatrix}$（$\lambda = \pm i$），純振盪、軌跡是圓。
  - **3D demo：** 自訂 $3 \times 3$ 矩陣，使用者拉 slider 設特徵值。
- **維度範圍：** $n \in \{2, 3\}$（高維無法視覺化軌跡）。
- **數值範圍：** $\lambda_p \in [-2, 2]$（避免數值溢位）；$t \in [0, 10]$ 步進 0.05；$n \in [0, 50]$ 步進 1（離散）。
- **退化情形：**
  - $\lambda_p = 0$：對應分量靜止不動。
  - $\mathbf{c}$ 在某個 $\mathbf{x}_p$ 方向分量為 0：該分量永遠不出現在軌跡中。
  - 重複特徵值：不可對角化的情況提示「使用 Jordan form」（不在本互動範圍）。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 60% 主舞台（左 40% (P3) 結構 + 右 60% 軌跡圖） + 中 15% 分量分解條 + 下 25% 控制列。
- **(P3) 結構區：** 顯示 $X D(t) \mathbf{c}$ 三明治，$D(t)$ 的藍對角圓點半徑隨 $|d_p(t)|$ 即時變化（$d_p$ 變大 → 藍點變大 + 加深，$d_p$ 變小 → 縮小 + 變淡）；右下角同時顯示「兩步拆解」迷你縮圖：① $D\mathbf{c}$ 中間結果向量、② $X(D\mathbf{c})$ 結果。
- **軌跡圖（2D）：** 600×480 px 笛卡兒座標系，原點居中、軸範圍依預設自適應；軌跡用「藍實線 + 不同 $t$ 點用淡 → 深漸變」顯示完整路徑；當前 $\mathbf{u}(t)$ 用紫色實心圓點標記；初始 $\mathbf{u}_0$ 用空心圓點標記；特徵向量 $\mathbf{x}_1, \mathbf{x}_2$ 從原點畫綠箭頭（長度依 $|c_p \mathbf{x}_p|$）。
- **軌跡圖（3D）：** 同上但用 plotly.graph_objects.Scatter3d 或 matplotlib 3D；旋轉 / 縮放互動。
- **分量分解條：** 中 15% 區域顯示 $n$ 條「彩色長條」，每條長度 = $|c_p e^{\lambda_p t}|$（連續）或 $|c_p \lambda_p^n|$（離散）、顏色依特徵值正負（藍 = 衰減 / 紅 = 成長 / 綠 = 振盪）。
- **配色：** 特徵向量 $\mathbf{x}_p$ 綠 `#2ca02c`、對角元素藍 `#1f77b4`、初始 $\mathbf{c}$ 紫 `#9467bd`、軌跡藍 `#1f77b4` 漸變、分量條依正負（衰減藍 / 成長紅 / 振盪綠）。
- **字型 / 字級：** 軌跡圖座標 12pt、分量條標籤 11pt、控制列 12pt。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 模式 | radio | 連續 / 離散 | 連續 | 切換重建 |
| $t$（連續） | slider | [0, 10] step 0.05 | 0 | 即時 |
| $n$（離散） | slider | [0, 50] step 1 | 0 | 即時 |
| play / pause | button | — | pause | click |
| 自動播放速度 | slider | 50ms – 1s / step | 200ms | 即時 |
| 預設 demo | radio | 穩定 / 振盪 / 不穩定 / 自訂 | 穩定 | 切換重建 |
| $\lambda_p$（自訂模式） | slider × $n$ | [-2, 2] step 0.1 | 預設值 | 即時 |
| $\mathbf{x}_p$（自訂模式） | slider grid | [-3, 3] step 0.1 | 預設值 | 即時 |
| $\mathbf{u}_0$（自訂） | slider × $n$ | [-5, 5] step 0.1 | (3, 2, 0...) | 即時 |
| 顯示分量分解 | checkbox | on / off | on | 即時 |
| 顯示軌跡尾跡 | checkbox | on / off | on | 即時 |
| 重設 | button | — | — | click |

#### F. 輸出畫面細節（Outputs）
- **(P3) 結構區：**
  - $X$ 列：固定（不變）。
  - $D(t)$ 對角圓點：半徑 ∝ $|d_p(t)|$，顏色依正負（藍 / 紅）；hover 顯示 `$d_p(t) = e^{\lambda_p t} = 0.61$` 之類數字。
  - $\mathbf{c}$：固定（不變）。
  - 中間 $D\mathbf{c}$：紫色 stack，每個元素 = $d_p(t) c_p$，即時更新。
  - 結果 $\mathbf{u}(t)$：紫色實心向量，與軌跡圖紫點同步。
- **軌跡圖：**
  - 完整軌跡曲線（漸變色）。
  - 當前位置紫點（直徑 8px）。
  - 特徵向量綠箭頭（長度即時 = $|c_p e^{\lambda_p t}|$）。
  - 「+」分解：$\mathbf{u}(t) = c_1 e^{\lambda_1 t} \mathbf{x}_1 + c_2 e^{\lambda_2 t} \mathbf{x}_2$ 顯示為「兩條彩色子向量首尾相接」（從原點 → 第一個分量端點 → $\mathbf{u}(t)$）。
  - 角落顯示 `$t = 2.30 \mid \mathbf{u}(t) = (1.20, 1.32)^{\mathrm{T}}$`。
- **分量分解條：** $n$ 條長條 + 即時數字 `$c_1 e^{\lambda_1 t} = 1.20$`、`$c_2 e^{\lambda_2 t} = 0.85$`。
- **公式區：** `$\mathbf{u}(t) = X e^{\Lambda t} \mathbf{c} = \sum_p c_p e^{\lambda_p t} \mathbf{x}_p$` 即時 LaTeX。

#### G. 互動行為（Interactions）
- **拉 $t$ slider：** 軌跡圖紫點即時移動；(P3) 結構區藍點半徑同步更新；分量條長度同步更新。
- **play 自動播放：** $t$ 從 0 到 10 自動推進，到達後暫停 1 秒、重設 $t = 0$ 再循環。
- **切換模式：** 連續 → 離散時 $t$ slider 變 $n$ slider，軌跡從連續曲線變「離散點 stack」（每個點之間用淡灰虛線連接表示「跳躍順序」）。
- **切換 demo：** 軌跡圖、分量條、(P3) 結構區全部重繪；保留前一個 demo 的軌跡淡灰色作為對比 1 秒後消失。
- **拉 $\lambda_p$ slider（自訂模式）：** 軌跡完全重算 + 重繪；提示「特徵值改變導致軌跡質變」。
- **快捷鍵：** `Space` play / pause、`→` $t$ += 0.1、`←` $t$ -= 0.1、`R` reset、`D` 切換 demo（循環）、`M` 切換模式。

#### H. 動畫腳本（時間演化）
- **每 frame（$t$ 增加 $\Delta t$）：**
  - **t → t+Δt（200ms 預設速度）：**
    - **0–30ms：** 計算新 $\mathbf{u}(t+\Delta t)$ + $D(t+\Delta t)$ 的對角元素。
    - **30–150ms：** 軌跡圖紫點滑動到新位置（lerp）；尾跡延伸；分量子向量端點同步移動。
    - **30–150ms：** (P3) 結構區藍點半徑 lerp 到新值；分量條長度 lerp。
    - **150–200ms：** 數字字級閃一下提示變化（特別當 $|d_p|$ 改變超過 20% 時）。
- **緩動：** linear（時間軸最自然）。
- **倒退（拉 $t$ slider 往左）：** 軌跡曲線「縮回」到當前 $t$，紫點移到對應位置。

#### I. 邊界與錯誤處理
- **$\lambda > 0$ 大值（成長爆炸）：** 軌跡延伸超出畫布時自動縮放座標系（座標範圍動態擴大），右上角顯示「auto-zoom: range expanded to ±20」。
- **$\lambda$ 為複數：** 自動切換到「振盪」demo（單獨展示複數特徵值的螺旋）；提示「複數特徵值 → 振盪解」。
- **重複特徵值：** 計算特徵向量時若 $X$ 不可逆（$\det X = 0$），紅色警告「特徵向量不獨立 — Jordan form 需要」+ 暫停動畫。
- **拉 slider 過快：** debounce 50ms。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - $t$ slider：「時間 — 拉動看每個分量按 $e^{\lambda_p t}$ 演化」
  - $\lambda_p$ slider：「特徵值 — 控制第 $p$ 分量的成長 / 衰減速度」
  - 分量條：「$|c_p e^{\lambda_p t}|$ — 該分量目前的能量」
  - (P3) 結構：「對角矩陣 $D(t) = e^{\Lambda t}$ 隨時間變化 — 每個對角元素獨立演化」
- **Walkthrough（首次自動觸發）：**
  - Step 1：「現在 $t = 0$，$D = I$，$\mathbf{u}(0) = \mathbf{u}_0$（初始位置）」
  - Step 2：「拉 $t$ 滑桿到 1.0，看軌跡走出第一段，每個分量按 $e^{\lambda_p}$ 縮放」
  - Step 3：「注意分量條：$\lambda_1 = -0.5$ 的分量越來越短（衰減）」
  - Step 4：「按 play 看完整軌跡螺旋收斂到原點」
  - Step 5：「切到『振盪』demo 看複數特徵值的圓形軌跡」
  - Step 6：「切到『不穩定』demo 看 $\lambda > 0$ 的爆炸軌跡」
- **常見誤解警示：**
  - 「(P3) 中的 $D$ 不是矩陣 $A$ 的對角化 — 是 $e^{\Lambda t}$ 或 $\Lambda^n$，是 $\Lambda$ 的『時間版本』」
  - 「$X$ 是特徵向量矩陣，不是任意可逆矩陣 — 用其他基底拆 $\mathbf{u}_0$ 不會給出無耦合解」
  - 「$e^{\Lambda t}$ ≠ $e^{At}$ 的元素 — 是『先對角化再指數』」
- **延伸閱讀：** 原書 p.6、§6.4 ($Q\Lambda Q^{\mathrm{T}}$)、Strang LAFE Sec. 6.4 Systems of Differential Equations。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib + matplotlib.animation（小 demo）；3D demo 建議 Plotly（軌跡互動旋轉 / 縮放品質好）。
- **替代方案：** Streamlit + Plotly。
- **關鍵 API：**
  - `numpy.linalg.eig(A)` 算特徵值與向量。
  - `scipy.linalg.expm(A * t)` 算 $e^{At}$（驗證用）。
  - `numpy.einsum('ij,j,j->i', X, np.exp(eigvals * t), c)` 計算 $\mathbf{u}(t)$。
  - `matplotlib.animation.FuncAnimation` 連續播放。
  - `plotly.graph_objects.Scatter3d` 3D 軌跡。
- **檔案結構：**
  ```
  viz/
    ch05_patterns.py
    _common/
      eig_solver.py              # 特徵值計算 + 退化偵測
      trajectory_plot.py         # 2D / 3D 軌跡共用繪製
      diagonal_widget.py         # 沿用 VizScript-01
  ```
- **效能：** 軌跡預計算 200 個時間點 + cache；slider 拖動只查表；自動播放用 FuncAnimation 60fps。
- **測試：** 4 demo（穩定 / 振盪 / 不穩定 / 自訂）各 1 張 snapshot；$t = 0, 1, 5, 10$ 各 1 張；$\lambda$ 為複數時 1 張。

#### L. 驗收標準（Acceptance Criteria）
- [ ] 拉 $t$ slider 即時更新軌跡紫點 + (P3) 藍點半徑，動畫 ≤ 150ms。
- [ ] 4 個預設 demo 切換流暢、保留前一個軌跡 1 秒。
- [ ] play 自動播放 60fps、可暫停 / 倒退。
- [ ] 自訂模式下拉 $\lambda_p$ slider 軌跡完全重繪 < 200ms。
- [ ] 複數特徵值正確顯示螺旋（不應拋例外）。
- [ ] Walkthrough 6 步驟自動觸發。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 2
- **Tier 1 對應：** 純靜態 4 個 demo 並列、無互動 slider。
- **Tier 3 擴充：** + 加「相空間流場」（vector field）疊在軌跡圖背景；+ 不同初始條件多軌跡同畫面對比；+ 連到實際工程例（彈簧質量系統 / 化學反應動力學 / 人口模型）。
- **估時：** 1.5 session（含 demo 配置與 walkthrough）

---

### VizScript-03: P4 三明治結構（$U \Sigma V^{\mathrm{T}}$ 互動 — 精簡版）

#### A. 一句話定位
靜態 + 輕量互動展示 $U \Sigma V^{\mathrm{T}} = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ 的三明治結構分解；左側顯示三明治、右側顯示秩 1 之和；拉 $\sigma_p$ slider 看「該秩 1 圖層的能量隨 $\sigma_p$ 縮放」 + 切換到「特徵值版（$Q\Lambda Q^{\mathrm{T}}$）」看兩者結構差異 — **不重做累加 / 截斷 demo（指向 ch04 VizScript-02）**。

#### B. 學習目標（Learning Outcome）
- 使用者能說出「(P4) = 兩個正交基底 + 一個對角矩陣」三層結構。
- 使用者能在「$U\Sigma V^{\mathrm{T}}$ ↔ $Q\Lambda Q^{\mathrm{T}}$」切換時觀察「兩基底相同（特徵值）vs 兩基底不同（SVD）」的差異。
- 使用者能拉 $\sigma_p$ slider 看「對應秩 1 圖層的視覺亮度（能量）」隨之變化。
- 使用者能說出「(P4) 是 §6.4 / §6.5 兩大分解的共骨架」。
- 使用者能跟著 pointer 跳到 ch04 VizScript-02 看完整累加 / 截斷動畫。

#### C. 待視覺化的數學物件
- 矩陣 $U \in \mathbb{R}^{m \times r}$（綠列）、$\Sigma = \operatorname{diag}(\sigma_1, \ldots, \sigma_r)$（藍對角）、$V^{\mathrm{T}} \in \mathbb{R}^{r \times n}$（粉紅行）、$r$ 個秩 1 矩陣 $\sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$、最終 $A = U\Sigma V^{\mathrm{T}}$。
- **預設值：** $m = n = 3, r = 3$；$U, V$ 預設為 $3 \times 3$ 旋轉矩陣（互不相同）；$\Sigma = \operatorname{diag}(3, 2, 1)$。
- **特徵值模式預設：** $S = Q \Lambda Q^{\mathrm{T}}$ 中 $Q$ = 旋轉矩陣、$\Lambda = \operatorname{diag}(2, 1, -1)$。
- **退化情形：** $\sigma_p = 0$ 對應秩 1 圖層完全消失；$\sigma_p$ 全相等 → 各圖層能量相同（無「主成分」概念）。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 75% 主舞台 + 下 25% 控制列。
- **主舞台（左右兩塊）：**
  - **左 50%：** 三明治結構 $U \Sigma V^{\mathrm{T}}$（綠 + 藍 + 粉紅）+ 「$=$」+ 完整結果矩陣 $A$（cell heatmap，藍 → 白 → 紅 colormap）。
  - **右 50%：** $r$ 個秩 1 矩陣方塊並列 + 「+」號連接 + 「$=$」+ $A$ 副本。每個秩 1 方塊內畫「綠直立列 + 粉紅橫躺行 + 藍圓點交叉」（沿用 ch04 VizScript-02 的「+ 字交叉」原語）；方塊邊框粗細 ∝ $|\sigma_p|$（視覺強調能量大小）。
- **配色：** 沿用全章配色；秩 1 方塊內熱圖用「藍 → 白 → 紅」colormap。
- **公式區（下緣）：** `$U \Sigma V^{\mathrm{T}} = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$` 即時 LaTeX。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| 模式 | radio | SVD ($U\Sigma V^{\mathrm{T}}$) / 特徵值 ($Q\Lambda Q^{\mathrm{T}}$) | SVD | 切換重建 |
| $r$ | slider | [1, 4] | 3 | 即時 |
| $\sigma_p$ / $\lambda_p$ | slider × $r$ | [-3, 3] step 0.5 | 3, 2, 1 / 2, 1, -1 | 即時 |
| 跳到 ch04 VizScript-02 | button | — | — | click → 開新 tab / 跳頁 |
| 重設 | button | — | — | click |

#### F. 輸出畫面細節（Outputs）
- **三明治區：** $\Sigma$ 藍點半徑 ∝ $|\sigma_p|$；hover 顯示 `$\sigma_2 = 2.0$`。
- **秩 1 方塊：** 邊框粗細 ∝ $|\sigma_p|$；hover 第 $p$ 方塊 → tooltip 顯示「$\sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$，能量占比 = $\sigma_p^2 / \sum \sigma^2$ = 64.3%」+ 對應 $\mathbf{u}_p$（綠列）+ $\mathbf{v}^{\mathrm{T}}_p$（粉紅行）在三明治中高亮。
- **結果矩陣 $A$：** cell heatmap 即時更新；colormap 範圍依 $\max|A_{ij}|$ 自適應。

#### G. 互動行為（Interactions）
- **拉 $\sigma_p$ slider：** 對應秩 1 方塊邊框粗細即時更新 + 內熱圖顏色強度同步變化；最終 $A$ 重算。
- **拉 $r$ slider：** 秩 1 方塊數量增減（fade in / out 200ms）；三明治結構 $\Sigma$ 對角元素數變化。
- **切換 SVD ↔ 特徵值模式：** 整體重繪 — SVD 模式 $U \neq V$（兩種顏色基底）、特徵值模式 $U = V = Q$（同色，提示「兩基底相同」）。動畫 600ms。
- **「跳到 ch04 VizScript-02」button：** 開新 tab 或跳到對應劇本（看完整累加 / 截斷 / Mona Lisa demo）。

#### H. 動畫腳本
- **無複雜動畫**（Tier 1 設計）；slider 拉動時所有更新即時 < 100ms。
- **模式切換：** 600ms「兩基底融合 / 分離」動畫 — SVD → 特徵值時 $V$ 漸漸轉色融合到 $U$；反向則分離。

#### I. 邊界與錯誤處理
- **$\sigma_p = 0$：** 對應秩 1 方塊變灰底 + 邊框虛線 + 提示「能量 0 — 不貢獻」。
- **$r = 0$：** 結果矩陣全 0、提示「rank 0」。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - SVD mode：「$U, V$ 不同 — 適用任意矩陣」
  - 特徵值 mode：「$U = V = Q$ — 僅適用對稱矩陣」
  - $\sigma_p$ slider：「拉到 0 看該秩 1 圖層消失」
  - 「跳到 ch04」：「看完整累加 / 截斷 / Mona Lisa SVD 影像 demo」
- **Walkthrough（首次自動）：**
  - Step 1：「(P4) = 三明治結構：兩個正交基底 + 對角矩陣」
  - Step 2：「右側秩 1 方塊：每個是 $\sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$」
  - Step 3：「拉 $\sigma_2$ slider 看第 2 個方塊邊框變細 — 能量降低」
  - Step 4：「切到『特徵值』模式看 $U = V = Q$ — 對稱矩陣的特例」
  - Step 5：「想看完整累加 / Mona Lisa demo？按『跳到 ch04』」
- **常見誤解警示：**
  - 「(P4) 不限對稱矩陣 — 但特徵值版需要對稱性」
  - 「$\sigma_p$ 永遠非負；$\lambda_p$ 可以是負或複數」
- **延伸閱讀：** 原書 p.7、§6.4、§6.5、ch04 VizScript-02、Strang LAFE Sec. 7.4。

#### K. 技術實作建議（Tech Stack Hints）
- **首選方案：** Marimo + matplotlib（與 VizScript-01 共用畫面框架）。
- **關鍵 API：**
  - `numpy.linalg.svd(A)` 取 $U, \Sigma, V^{\mathrm{T}}$。
  - `numpy.linalg.eigh(S)` 取對稱矩陣特徵值（保證實數）。
  - 沿用 ch04 `_common/rank1_layer.py`。
- **檔案結構：** 沿用 `ch05_patterns.py`，本劇本約 200 行（小型）。

#### L. 驗收標準（Acceptance Criteria）
- [ ] 拉 $\sigma_p$ slider 即時更新 < 100ms。
- [ ] 模式切換動畫 600ms 流暢。
- [ ] 「跳到 ch04 VizScript-02」按鈕功能正確（開新分頁或滾動到對應位置）。
- [ ] $\sigma_p = 0$ 退化處理正確。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 1
- **Tier 2 擴充：** + 「能量重排序」radio（按 $\sigma_p$ 升 / 降序排列秩 1 方塊）+ 「對稱性檢查」按鈕（驗證輸入是否對稱矩陣，不對稱時切回 SVD 模式）。
- **Tier 3 擴充：** 與 ch04 VizScript-02 合併為單一互動，含累加 / 截斷 / Mona Lisa demo（但這在 ch04 已實作，本章不重複）。
- **估時：** 0.5 session

---

### VizScript-04: P1' 數值步進 walkthrough（輕量版）

#### A. 一句話定位
按播放鍵，從 $\mathbf{a}_1$ 到 $\mathbf{a}_n$ 依序高亮 $A$ 的每一直立列、同時對應的對角元素 $d_p$ 變紅（被選中），動畫顯示 $d_p \mathbf{a}_p$ 從原 $A$ 區域複製、被「藍點戴上帽子」、寬度按 $|d_p|$ 拉伸 / 縮短後落入結果區的對應位置 — 整個 $AD$ 計算過程的純數值 walkthrough。

#### B. 學習目標（Learning Outcome）
- 使用者能跟著動畫一步一步看完 $AD$ 的「**逐列縮放**」過程。
- 使用者能在中學 / 大一程度建立「對角矩陣 = 列縮放器」的具體心智模型。
- 使用者能說出每一步「現在處理第 $p$ 列、被縮放因子是 $d_p$、結果是 $d_p \mathbf{a}_p$」。

#### C. 待視覺化的數學物件
- $A \in \mathbb{R}^{m \times n}$（綠列 stack）、$D = \operatorname{diag}(d_1, \ldots, d_n)$（藍點 stack）、結果 $AD$（綠列被縮放後的 stack）。
- **預設值：** $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$、$D = \operatorname{diag}(2, 0.5, -1)$（含一個 < 1、一個負值，便於展示三種視覺效果）。
- **維度範圍：** $m = n = 3$（固定，輕量版不調尺寸）。
- **退化情形：** $d_p = 0$ 對應列消失（變灰、寬度為 0）。

#### D. 視覺布局（Visual Layout）
- **整體比例：** 上 80% 主舞台 + 下 20% 控制列。
- **主舞台：** 左 30% 顯示 $A$（綠列 stack）、中 15% 顯示 $D$（藍點 stack）+ 「$=$」、右 40% 顯示結果 $AD$（隨動畫逐列填入）+ 上方公式區「$AD = [d_1\mathbf{a}_1\ d_2\mathbf{a}_2\ d_3\mathbf{a}_3]$」逐項高亮。
- **配色：** 沿用；當前處理中的列 / 對角元素用「閃爍橘 `#ff7f0e`」高亮。

#### E. 輸入控制（Inputs）
| Widget | 類型 | 範圍 / 選項 | 預設 | 觸發時機 |
|---|---|---|---|---|
| play / pause / reset | button × 3 | — | — | click |
| 速度 | slider | 500ms – 3s / step | 1500ms | 即時 |
| 跳到第 $p$ 步 | slider | [0, n] | 0 | 即時 |
| $d_p$（可選） | slider × n | [-3, 3] step 0.5 | (2, 0.5, -1) | 即時（中斷動畫） |

#### F. 輸出畫面細節（Outputs）
- **動畫每一步：**
  - $A$ 的第 $p$ 列邊框閃爍橘色 200ms。
  - $D$ 的第 $p$ 對角藍點變紅 200ms。
  - 「$d_p \mathbf{a}_p$」標籤在中央上方淡入。
  - 第 $p$ 列被「複製出來」，飛到結果區對應位置 + 寬度 lerp 到 $|d_p|$ 倍 + 若 $d_p < 0$ 加斜線紋理。
- **進度條：** 下方顯示當前處於第 $p$ 步 / 總 $n$ 步。

#### G. 互動行為（Interactions）
- **play：** 按 1500ms / 步速度自動推進，到達 $p = n$ 後暫停。
- **pause：** 暫停在當前步。
- **reset：** 結果區清空、回到 $p = 0$。
- **跳到第 $p$ 步 slider：** 立即跳轉，前 $p$ 步結果靜態顯示。
- **快捷鍵：** `Space` play / pause、`R` reset、`→` 下一步、`←` 上一步。

#### H. 動畫腳本
- **單步（$p \to p+1$）：**
  - **0–200ms：** 第 $p$ 列邊框閃爍橘 + $d_p$ 藍點變紅。
  - **200–600ms：** 列複製出 + 飛到結果區 + 寬度 lerp。
  - **600–1000ms：** 結果區該位置 cell 數字逐個淡入（從上到下）。
  - **1000–1500ms：** 全部 settle，準備下一步。
- **緩動：** ease-out。

#### I. 邊界與錯誤處理
- **$d_p = 0$：** 對應列「消失動畫」（寬度從原寬度 lerp 到 0）+ 結果區留白。
- **$d_p < 0$：** 結果列加斜線紋理 + tooltip「方向反轉」。

#### J. 教學支援（Teaching Aids）
- **Tooltip：**
  - play 按鈕：「逐列看 $AD = [d_1\mathbf{a}_1, d_2\mathbf{a}_2, d_3\mathbf{a}_3]$ 是怎麼算出來的」
  - 速度 slider：「拉慢看清楚每一步的 lerp」
- **Walkthrough：** 與動畫合一，無額外 step。
- **延伸閱讀：** ch05 VizScript-01（看 4 個 Pattern 比較）。

#### K. 技術實作建議
- **首選方案：** Marimo + matplotlib.animation（簡單，無需多模式）。
- **檔案結構：** 整合到 `ch05_patterns.py`，約 100 行。

#### L. 驗收標準
- [ ] 動畫每步 1500ms 流暢。
- [ ] 跳轉 slider 同步前 $p$ 步結果。
- [ ] $d_p < 0$ 與 $d_p = 0$ 退化提示正確。

#### M. 互動深度 Tier + 估時
- **本劇本目標 Tier：** Tier 1
- **估時：** 0.3 session

---

## 章末延伸

### 與前面章節的連結

- **§1 (Viewing Matrix - 4 Ways)：** 對角矩陣是「列為單位向量倍數 + 行為單位向量倍數」的特例 — (P1') (P2') 是 §1 第 2 / 第 3 視角的退化版。
- **§2 (Vector × Vector)：** (P3) 中 $D \mathbf{c}$ 是 (Mv2) 的退化（對角矩陣作用在向量 = 分量縮放）；$X(D\mathbf{c})$ 是 (Mv2) 標準式。(P4) 中的秩 1 矩陣 $\mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ 是 §2 (v2) 外積的直接套用。
- **§3 (Matrix × Vector)：** (P3) 整體就是 $X(D\mathbf{c})$ 即 (Mv2) 應用在「對角縮放後的向量」上。
- **§4 (Matrix × Matrix - 4 Ways)：**
  - (P1) = (MM2) + (Mv2) 的整合。
  - (P2) = (MM3) + (vM2) 的整合。
  - (P1') = (MM2) 的退化（$B = D$）。
  - (P2') = (MM3) 的退化（$A = D$）。
  - (P4) = (P1') + (MM4) 串接 — **整個 (MM4) 視角的「結構化版本」**。

### 後續章節的應用

- **§6.1 ($A = CR$)：** 用 (P1) 視角理解「$C$ 從右乘 $R$ → $A$ 是 $C$ 列的線組」。
- **§6.2 ($A = LU$)：** $L$（單位下三角）從左乘 $U$（上三角）— 用 (P2) 理解「$L$ 行對 $U$ 行做線組」。
- **§6.3 ($A = QR$)：** 同 LU 視角，但 $Q$ 正交。
- **§6.4 ($S = Q \Lambda Q^{\mathrm{T}}$)：** **直接套 (P4) 模板** — $Q$ 從右乘 $\Lambda$ 套 (P1')、結果再從右乘 $Q^{\mathrm{T}}$ 套 (MM4)；最終 $S = \sum \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$。**(P3) 解釋為什麼要做這個分解** — 解動態系統。
- **§6.5 ($A = U \Sigma V^{\mathrm{T}}$)：** **直接套 (P4) 模板** — $U$ 從右乘 $\Sigma$ 套 (P1')、結果再從右乘 $V^{\mathrm{T}}$ 套 (MM4)；最終 $A = \sum \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$。Mona Lisa SVD demo 的視覺基礎在 ch04 VizScript-02。

### 工程實作的對應

- **(P1') / (P2') 程式視角：** NumPy `A @ np.diag(d)` ≡ `A * d`（廣播自動處理列縮放）；`np.diag(d) @ B` ≡ `d[:, None] * B`（行縮放）。**對角矩陣不應該存成完整 $n \times n$ 矩陣** — 浪費 $n^2 - n$ 個 0。
- **(P3) 程式視角：** 解 $\mathbf{u}(t) = X e^{\Lambda t} X^{-1} \mathbf{u}_0$ 的高效寫法：先算 $\mathbf{c} = X^{-1} \mathbf{u}_0$（一次 `np.linalg.solve`），之後查 $\mathbf{u}(t) = X(\exp(\lambda t) \cdot \mathbf{c})$（每個 $t$ 一次 $O(n^2)$）。比直接 `expm(A * t) @ u0` 快很多（避免每個 $t$ 重算矩陣指數）。
- **(P4) 程式視角：** SVD 截斷只要切片 `A_k = U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]`。低秩近似的記憶體成本是 $O(k(m+n))$，遠小於原矩陣 $O(mn)$。

---

## 來源對照

| 內容 | 來源檔案 / 段落 |
|---|---|
| Pattern 文字描述 | `from-tex/en.md` 第 127–203 行 / `from-tex/zh.md` 第 122–196 行 |
| Figure 5.1 (Pattern12.png) | `figs-png/Pattern12.png`（原書 Figure 7） |
| Figure 5.2 (Pattern11-22.png) | `figs-png/Pattern11-22.png`（原書 Figure 8） |
| Figure 5.3 (Pattern3.png) | `figs-png/Pattern3.png`（原書 Figure 9） |
| Figure 5.4 (Pattern4.png) | `figs-png/Pattern4.png`（原書 Figure 10） |
| (P3) 微分方程通解 | 原書 p.6 / Strang LAFE Sec. 6.4 |
| (P4) 三明治結構 | 原書 p.7 / Strang LAFE Sec. 7.1 / Sec. 7.4 |
| 4 視角對應 §4 | 本書 ch04-mat-mat.md §4 (MM1)–(MM4) |
| (MM4) 累加 / 截斷 demo | 本書 ch04-mat-mat.md VizScript-02（ch05 VizScript-03 指標到此） |
| 配色 / cell 尺寸 / 動畫時間 | 本書 SOP_DRAFT.md §2.8 全書視覺一致性錨點 |
