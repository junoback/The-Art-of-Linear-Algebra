# 6.2 矩陣分解 2：$A = LU$（Lower–Upper Triangular Factorization）

> **原書頁碼：** p.9–p.10
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` §6.2 $A=LU$（en.md line 307–377 / zh.md line 295–365）
> **本章圖數：** 2（`LU1.png` 無標、`LU2.png` 明標 **using MM4**）
> **本章 VizMark 數：** 3（⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1）
> **狀態：** [x] 已完成（S08）

---

## 章節摘要

$A = LU$ 是 §6 五大分解的**第二個**，也是與「**手算求解 $A\mathbf{x} = \mathbf{b}$**」最直接相關的一個。它的物理出發點是**高斯消去法**（Gaussian elimination）：把方陣 $A$ 用一連串的「行運算」（row operations）化簡成上三角矩陣 $U$，而把這些行運算「記下來」（順序）形成的下三角矩陣 $L$（單位對角）正好滿足 $A = LU$。

具體流程：

1. 用初等行運算矩陣 $E$ 把 $A$ 變成上三角 $U$：$EA = U$；
2. 反推：$A = E^{-1} U$，令 $L = E^{-1}$（必為下三角且對角線為 1）；
3. 得 $A = LU$，**$L$ 下三角 + 單位對角、$U$ 上三角 + 主元（pivots）在對角**。

求解 $A\mathbf{x} = \mathbf{b}$ 因此可拆成**兩步三角方程**：

$$
A\mathbf{x} = \mathbf{b} \;\Longleftrightarrow\; LU\mathbf{x} = \mathbf{b} \;\Longleftrightarrow\;
\begin{cases} L\mathbf{c} = \mathbf{b} & \text{(前代 / forward substitution)} \\ U\mathbf{x} = \mathbf{c} & \text{(後代 / back substitution)} \end{cases}
$$

這把「一個 $n \times n$ 的全密集方程」轉成「兩個 $n \times n$ 的三角方程」，計算量從 $O(n^3)$ 的高斯消去（含主元搜尋）降為 $O(n^2)$ 的兩次三角回代 — 在多個右端項 $\mathbf{b}_1, \mathbf{b}_2, \ldots$ 共用同一個 $A$ 時，**$LU$ 只算一次、回代算多次**，是數值線性代數最重要的計算結構之一。

本章的「視覺出發點」與 §6.1 CR 不同：

- **§6.1 CR** 是「掃描列、留獨立」的直觀算法；
- **§6.2 LU** 是「**遞迴 rank 1 peeling**」— 從 $A$ 的左上角剝下一個秩 1 矩陣（$\mathbf{l}_1 \mathbf{u}^*_1$）、留下右下角的子矩陣 $A_2$、再對 $A_2$ 重複，剝下第二個秩 1 矩陣……直到剝光。最後 $n$ 個 $\mathbf{l}_p \mathbf{u}^*_p$ 拼起來就是 $LU$。

**與 §4 (MM4) 的連結是 LU 視覺化的核心：** 原書 `LU2.png` 右下角直接標 `using MM4`，明示「$LU$ 是 (MM4) 的特例 — 但 $\mathbf{l}_p$ 是下三角列、$\mathbf{u}^*_p$ 是上三角行」。本章 VizScript 因此採**單 pointer 策略**：(MM4) 累加 demo 直接 pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)；本章獨立寫的是 **peeling 過程動畫 + 高斯消去步驟對齊 + 三角結構視覺化** 等 LU 特有的內容。

數值範例（本章貫穿，原書 Sec.2.3 經典示範）：

$$
A = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}
\;=\;
\underbrace{\begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}}_{L}
\underbrace{\begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix}}_{U}
$$

讀者用高斯消去驗證：

1. 第二行 $-$ 2 × 第一行：$(4, 3, 3) - 2(2, 1, 1) = (0, 1, 1)$（$L_{21} = 2$）；
2. 第三行 $-$ 4 × 第一行：$(8, 7, 9) - 4(2, 1, 1) = (0, 3, 5)$（$L_{31} = 4$）；
3. 第三行 $-$ 3 × 新的第二行：$(0, 3, 5) - 3(0, 1, 1) = (0, 0, 2)$（$L_{32} = 3$）；
4. 得 $U$，$L$ 即記下的「行乘數」加上單位對角線。

> ### 💡 背後觀念：A=LU 為什麼存在？2000 年的東方演算法如何被代數化封裝？
>
> 高斯消去法看起來是個「**演算法**」（一步步消除元素），$A = LU$ 卻是個「**靜態分解**」（一行矩陣等式）。為什麼一個逐步演算法可以壓縮成一行等式？而這條等式為什麼**至少存在 2000 年的演算法直到 1948 年才被代數化命名**？2 條設計動機問題：
>
> - **[Q16：A=LU 為什麼存在？高斯消去法為什麼能壓縮成兩三角矩陣？](appendix-D-why.md#q16)** — 高斯消去其實有兩千年歷史 — 中國《九章算術》方程章（公元 1 世紀）的「**遍乘直除**」就是它的東方原型，比 Gauss 早 1800 年。Newton 1707 → Gauss 1809（Ceres 軌道、「高斯消去」命名源頭）→ Doolittle 1878 → **Turing 1948**（首次系統研究數值穩定性 + 引入 partial pivoting + **首次明確稱呼此為「LU 分解」**）。LU 是「**演算法 → 代數結構**」這個現代數學核心方法論在線代中**最古老的案例**。三角矩陣的六大性質（前代 / 後代 / 行列式對角元素相乘 / 特徵值讀對角 / 反矩陣仍三角 / 乘法封閉）讓它成為「介於對角與一般矩陣之間的中間結構」。
> - **[Q14：為什麼要把矩陣「分解」？](appendix-D-why.md#q14)** — LU 是 §6「**求解 $A\mathbf{x} = \mathbf{b}$**」動機的最直接工具。一次 LU 分解 $O(n^3)$ + 每次求解 $O(n^2)$（前代 + 後代）— 這就是 LAPACK / NumPy / MATLAB 默認用 LU 解 $A\mathbf{x} = \mathbf{b}$ 的根本理由。LU 也展示了 5 個跨領域「**因果結構**」的代數刻畫（訊號處理因果濾波器 / 時序 AR 模型 / 動態規劃 DAG / 編譯器最佳化 / 拓樸電路）— 三角矩陣是「**分而治之**」哲學的代數骨架。

---

## 數學要點

### 1. 定義與形狀

$$
A_{n \times n} = L_{n \times n} \, U_{n \times n}
$$

- **$L$（Lower triangular）：** 下三角矩陣，**對角線元素恆為 1**（單位下三角 / unit lower triangular），對角線下方填消去過程的「行乘數」$L_{ij} = \dfrac{a_{ij}^{(j)}}{a_{jj}^{(j)}}$（$i > j$）；
- **$U$（Upper triangular）：** 上三角矩陣，**對角線元素是主元**（pivots）$u_{ii}$，對角線上方填消去後的剩餘元素，對角線下方全為零；
- **形狀：** 兩者都是 $n \times n$ 方陣（$LU$ 標準形式要求 $A$ 是方陣）；
- **可分解條件：** 若高斯消去過程**不需要換行**（即所有主元都非零），則 $A$ 可分解為 $LU$。若需要換行，則 $PA = LU$，其中 $P$ 是置換矩陣（permutation）— 本章先處理 $A = LU$ 的乾淨情形。

### 2. 與 (MM4) 視角的連結 — 秩 1 之和（核心 ⭐）

把 $A = LU$ 套用 §4 (MM4) 「列 × 行外積之和」視角：

$$
A = LU = \sum_{p=1}^{n} \mathbf{l}_p \, \mathbf{u}^{*}_p
$$

- $\mathbf{l}_p$ = $L$ 的第 $p$ 列（綠色直立，**從第 $p$ 列起非零**，前面 $p-1$ 個元素必為 0）；
- $\mathbf{u}^{*}_p$ = $U$ 的第 $p$ 行（粉紅橫躺，**從第 $p$ 行起非零**，前面 $p-1$ 個元素必為 0）；
- $\mathbf{l}_p \mathbf{u}^*_p$ 是「左上角為零、右下角為秩 1 子塊」的特殊秩 1 矩陣 — 視覺上像「**從左上角向右下角延伸的秩 1 楔形**」（wedge）。

**關鍵差異對比 §6.1 CR：**

| 性質 | $A = CR$（$r$ 項） | $A = LU$（$n$ 項） |
|---|---|---|
| 項數 | $r = \operatorname{rank}(A)$ | $n$（即使 rank 不足，項數仍是 $n$，只是某些 $\mathbf{l}_p \mathbf{u}^*_p$ 變成全零項） |
| $\mathbf{l}_p$ / $\mathbf{c}_p$ 結構 | $\mathbf{c}_p$ 可任意（從 $A$ 取獨立列） | $\mathbf{l}_p$ **強制下三角**：前 $p-1$ 個元素為 0 |
| $\mathbf{u}^*_p$ / $\mathbf{r}^*_p$ 結構 | $\mathbf{r}^*_p$ 可任意（RREF 行） | $\mathbf{u}^*_p$ **強制上三角**：前 $p-1$ 個元素為 0 |
| 視覺特徵 | 綠列 × 粉紅行的「完整網格」 | 綠列 × 粉紅行的「**右下角楔形**」（左上 $p-1$ 行/列為零） |
| 連結 §5 | (P1)/(P2)（using P1/P2 標記） | (MM4)（using MM4 標記） |

**範例展開（$n = 3$，原書 Sec.2.3 範例）：**

$$
A = \mathbf{l}_1 \mathbf{u}^*_1 + \mathbf{l}_2 \mathbf{u}^*_2 + \mathbf{l}_3 \mathbf{u}^*_3
$$

具體計算：

- $\mathbf{l}_1 \mathbf{u}^*_1 = \begin{bmatrix}1\\2\\4\end{bmatrix} \begin{bmatrix}2 & 1 & 1\end{bmatrix} = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 2 & 2 \\ 8 & 4 & 4 \end{bmatrix}$（**滿格秩 1，是 $A$ 的「外層楔形」**）；

- $\mathbf{l}_2 \mathbf{u}^*_2 = \begin{bmatrix}0\\1\\3\end{bmatrix} \begin{bmatrix}0 & 1 & 1\end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 3 & 3 \end{bmatrix}$（**第 1 行 / 列為零，右下 2×2 秩 1，是 $A_2$ 的「外層楔形」**）；

- $\mathbf{l}_3 \mathbf{u}^*_3 = \begin{bmatrix}0\\0\\1\end{bmatrix} \begin{bmatrix}0 & 0 & 2\end{bmatrix} = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 2 \end{bmatrix}$（**只剩右下角單一元素，是 $A_3$ 的「核」**）；

- 三項相加 $= \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix} = A \;\checkmark$。

**這就是 `LU2.png` 標 `using MM4` 的意義：** 三個秩 1 矩陣相加 = $A$，**每個秩 1 矩陣的「非零範圍」逐層向右下角縮小**（楔形 → 楔形 → 點），這是 (MM4) 在「三角結構」中的特化。

### 3. 高斯消去（Gaussian Elimination）= 反向 peeling

把第 2 節的展開「**從 $A$ 倒推**」就是高斯消去：

$$
A_1 = A, \quad A_{p+1} = A_p - \mathbf{l}_p \mathbf{u}^*_p, \qquad p = 1, 2, \ldots, n
$$

具體過程（以本章範例為例）：

| 步驟 | 動作 | 矩陣狀態 |
|---|---|---|
| $p = 1$ | 取 $A_1 = A$ 第 1 行 $\mathbf{u}^*_1 = (2, 1, 1)$；取第 1 列 $\div$ 主元 $\mathbf{l}_1 = (1, 2, 4)^{\mathrm{T}}$（除以 $a_{11} = 2$） | $A_1 = \begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}$ |
| $A_2 = A_1 - \mathbf{l}_1 \mathbf{u}^*_1$ | 第 1 行 / 列「**清零**」，子矩陣 $A_2$ 出現於右下 | $A_2 = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 3 & 5 \end{bmatrix}$ |
| $p = 2$ | 取 $A_2$ 第 2 行 $\mathbf{u}^*_2 = (0, 1, 1)$；取第 2 列 $\div$ 主元 $\mathbf{l}_2 = (0, 1, 3)^{\mathrm{T}}$ | $A_2$（同上） |
| $A_3 = A_2 - \mathbf{l}_2 \mathbf{u}^*_2$ | 第 2 行 / 列也清零 | $A_3 = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 2 \end{bmatrix}$ |
| $p = 3$ | 取 $A_3$ 第 3 行 $\mathbf{u}^*_3 = (0, 0, 2)$；取第 3 列 $\div$ 主元 $\mathbf{l}_3 = (0, 0, 1)^{\mathrm{T}}$ | $A_3$（同上） |
| $A_4 = A_3 - \mathbf{l}_3 \mathbf{u}^*_3$ | 全零，結束 | $\mathbf{0}$ |

完整對應：

- $L = [\mathbf{l}_1 \;|\; \mathbf{l}_2 \;|\; \mathbf{l}_3] = \begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}$（每個 $\mathbf{l}_p$ 排成 $L$ 的第 $p$ 列）；
- $U = \begin{bmatrix} \mathbf{u}^*_1 \\ \mathbf{u}^*_2 \\ \mathbf{u}^*_3 \end{bmatrix} = \begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 2 \end{bmatrix}$（每個 $\mathbf{u}^*_p$ 排成 $U$ 的第 $p$ 行）。

**遞迴 peeling 的視覺隱喻：** $A$ 像一個三層洋蔥，每次剝掉外層的「秩 1 楔形」（$\mathbf{l}_p \mathbf{u}^*_p$），露出內層更小的子矩陣 $A_{p+1}$。最後一層是右下角一個純量（主元 $u_{nn}$）。**這是 LU1 圖的核心訊息**。

### 4. 求解 $A\mathbf{x} = \mathbf{b}$ 的兩步法（Forward + Back Substitution）

求解流程：

$$
A\mathbf{x} = \mathbf{b} \quad\Longleftrightarrow\quad LU\mathbf{x} = \mathbf{b} \quad\Longleftrightarrow\quad
\underbrace{L\mathbf{c} = \mathbf{b}}_{\text{前代}} \;\to\; \underbrace{U\mathbf{x} = \mathbf{c}}_{\text{後代}}
$$

**前代（forward substitution）：** $L\mathbf{c} = \mathbf{b}$ 中 $L$ 下三角且對角為 1：

$$
\begin{cases}
c_1 = b_1 \\
c_2 = b_2 - L_{21} c_1 \\
c_3 = b_3 - L_{31} c_1 - L_{32} c_2 \\
\vdots
\end{cases}
$$

**從第 1 行往下推**，每行只用「前面已算好的 $c$」減去乘積。

**後代（back substitution）：** $U\mathbf{x} = \mathbf{c}$ 中 $U$ 上三角且對角為主元：

$$
\begin{cases}
x_n = c_n / u_{nn} \\
x_{n-1} = (c_{n-1} - u_{n-1,n} x_n) / u_{n-1, n-1} \\
\vdots \\
x_1 = (c_1 - u_{12} x_2 - \cdots - u_{1n} x_n) / u_{11}
\end{cases}
$$

**從第 $n$ 行往上推**，每行只用「後面已算好的 $x$」減去乘積、除以主元。

**範例：** 設 $\mathbf{b} = (1, 5, 17)^{\mathrm{T}}$，用上面的 $L, U$ 求 $\mathbf{x}$。

1. **前代** $L\mathbf{c} = \mathbf{b}$：
   - $c_1 = 1$；
   - $c_2 = 5 - 2 \cdot 1 = 3$；
   - $c_3 = 17 - 4 \cdot 1 - 3 \cdot 3 = 4$；
   - $\mathbf{c} = (1, 3, 4)^{\mathrm{T}}$。

2. **後代** $U\mathbf{x} = \mathbf{c}$：
   - $x_3 = 4 / 2 = 2$；
   - $x_2 = (3 - 1 \cdot 2) / 1 = 1$；
   - $x_1 = (1 - 1 \cdot 1 - 1 \cdot 2) / 2 = -1$；
   - $\mathbf{x} = (-1, 1, 2)^{\mathrm{T}}$。

3. **驗證** $A\mathbf{x}$：$\begin{bmatrix}2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9\end{bmatrix} \begin{bmatrix}-1 \\ 1 \\ 2\end{bmatrix} = \begin{bmatrix}-2+1+2 \\ -4+3+6 \\ -8+7+18\end{bmatrix} = \begin{bmatrix}1 \\ 5 \\ 17\end{bmatrix} = \mathbf{b}$ ✓。

**多右端項的優勢：** 對 $k$ 個不同的 $\mathbf{b}_1, \ldots, \mathbf{b}_k$，分解 $LU$ 只算一次（$O(n^3)$），之後每個 $\mathbf{b}_i$ 只要 $O(n^2)$ 回代。**這是反矩陣 $A^{-1}$ 不需要也不該明算的數值理由** — 用 $LU$ 解一連串 $A\mathbf{x}_i = \mathbf{b}_i$ 永遠比算出 $A^{-1}$ 再相乘穩定且高效。

### 5. 為什麼 $L$ 必為「單位下三角」、$U$ 必為「上三角」

從第 3 節的構造看：

- **$\mathbf{l}_p$ 的形狀**（$p = 1, \ldots, n$）：
  - 前 $p-1$ 個元素為 0（因為 $A_p$ 的前 $p-1$ 行 / 列已被前面的 peeling 清零）；
  - 第 $p$ 個元素 $= 1$（取自身行除以自己 = 1，即 $A_p$ 的 $(p, p)$ 主元除以自己）；
  - 第 $p+1, \ldots, n$ 個元素 $=$ $A_p$ 的第 $p$ 列下方元素除以主元；
  - 排成 $L$ 的第 $p$ 列 → **下三角 + 對角 = 1**。

- **$\mathbf{u}^*_p$ 的形狀**：
  - 前 $p-1$ 個元素為 0；
  - 第 $p$ 個元素 $=$ 主元 $u_{pp}$；
  - 第 $p+1, \ldots, n$ 個元素 $=$ $A_p$ 的第 $p$ 行右側元素；
  - 排成 $U$ 的第 $p$ 行 → **上三角**。

**視覺化記憶口訣：** 「$L$ 對角為 1 是因為主元搬到 $U$」— $A_p$ 的 $(p, p)$ 元素本身既是 $\mathbf{l}_p$ 的第 $p$ 個（除以自己 = 1），又是 $\mathbf{u}^*_p$ 的第 $p$ 個（保留原值 = 主元）。**這個「分配」是 $LU$ 唯一性的關鍵**（若不規定 $L$ 對角為 1，主元可以隨意分配給 $L$ 或 $U$）。

### 6. $A = LU$ 與其他四個分解的關係

| 關係 | 內容 |
|---|---|
| **LU ↔ CR** | LU 是「方陣 + 三角結構」的 CR，項數變 $n$ 而非 $r$，且 $\mathbf{l}_p, \mathbf{u}^*_p$ 多了「前綴零」的三角限制 |
| **LU ↔ QR** | QR 把「下三角 $L$」換成「正交 $Q$」（保留 $R$ 上三角）— $A = QR$ 的 $Q$ 是「$A$ 的列做 Gram–Schmidt」後得到的正交基底。**從 LU 到 QR = 把 $L$ 正交化** |
| **LU ↔ SVD** | SVD 把「下三角 $L$ + 上三角 $U$」雙端都換成正交（$U, V^{\mathrm{T}}$），中間留對角 $\Sigma$。**從 LU 到 SVD = 兩端都正交化** |
| **LU ↔ QΛQᵀ** | QΛQᵀ 限對稱 $S$ 且 $L = Q$、$U = \Lambda Q^{\mathrm{T}}$；對對稱 $S$ 還有 $S = LDL^{\mathrm{T}}$（Cholesky 的廣義版），與 $LU$ 同源但加對稱性 |

**結論：** $A = LU$ 是「**最少結構**」的數值分解 — 只要求 $A$ 是「無需換行」的方陣，分解後的 $L, U$ 各保留三角結構。其他三個更高階分解（QR、QΛQᵀ、SVD）都可以看成「在 LU 的三角結構上**疊正交性**」。從教學順序看，**LU 是進入「分解的數值意義」最自然的起點**（解方程 + 多右端項），CR 是進入「分解的概念意義」最自然的起點（列秩 = 行秩）。

### 7. 數學要點總結（一張表）

| 性質 | $A = LU$ 的對應 |
|---|---|
| 適用矩陣 | 方陣 $A_{n \times n}$，無需換行（即所有主元非零）；否則需 $PA = LU$ |
| $L$ 的結構 | 下三角 + 單位對角，下方填行乘數 $L_{ij}$ |
| $U$ 的結構 | 上三角 + 主元在對角，上方填消去剩餘元素 |
| 項數 | $n$（即使退化，項數仍 $n$，但某些 $\mathbf{l}_p \mathbf{u}^*_p$ 為全零） |
| 構造方法 | 高斯消去（前向）/ rank 1 peeling（等價反向）|
| §4 (MM4) 對應 | $A = \sum_{p=1}^{n} \mathbf{l}_p \mathbf{u}^*_p$（**`LU2.png` 標 `using MM4`**）|
| §5 Pattern 對應 | 無直接 (P1)(P2) 標記（不像 §6.1 CR）；但 (MM4) = (P1) 廣義版 |
| 求解 $A\mathbf{x} = \mathbf{b}$ | 兩步：$L\mathbf{c} = \mathbf{b}$（前代）+ $U\mathbf{x} = \mathbf{c}$（後代）|
| 計算量 | $LU$ 分解 $O(n^3)$、回代 $O(n^2)$；多右端項共用 $LU$ 大幅省時 |

---

## 圖片詳細描述（Figure Descriptions）

### Figure 6.3: 從 $A$ 遞迴 rank 1 peeling 得到 $L, U$（LU1）

**圖檔：** `docs/book/figs-png/LU1.png`（原始 EPS：`figs/LU1.eps`）
**原書頁碼：** p.9 圖 13
**所屬章節：** §6.2 $A = LU$（peeling 解構視角）
**圖中標記：** 無 `using PX` 標籤（與 §6.1 CR1/CR2、§6.2 LU2 不同）

#### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**，共 9 段：

1. **第 1 段：** 矩陣 $A$ 的方框（灰色填充正方形），上方有大字 `A`；
2. **第 2 段：** 等號 `=`；
3. **第 3 段：** 第 1 個秩 1 矩陣 — 方框內**整個外層**有色填充：**第 1 行（粉紅橫條）+ 第 1 列（綠直條）+ 內部灰底**（代表「外層楔形 = $\mathbf{l}_1 \mathbf{u}^*_1$ 的非零範圍佔據整個矩陣」）；
4. **第 4 段：** 加號 `+`；
5. **第 5 段：** 第 2 個秩 1 矩陣 — 方框內**第 2 行（粉紅橫條，較第 1 個小）+ 第 2 列（綠直條，較小）+ 右下灰底**（外層楔形向內縮一格）；
6. **第 6 段：** 加號 `+`；
7. **第 7 段：** 第 3 個秩 1 矩陣 — 方框內**只有右下角一小塊粉紅 + 一小塊綠**（外層楔形縮到最內，剩單一像素點）；
8. **第 8 段：** 等號 `=`；
9. **第 9–10 段：** 結果 $L$ 和 $U$：
   - $L$：方框內 **3 條等寬綠色直立列，從高到低**（$\mathbf{l}_1$ 最高滿格、$\mathbf{l}_2$ 中、$\mathbf{l}_3$ 最矮）— 視覺直觀展示「下三角 + 對角 1」；
   - $U$：方框內 **3 條等高粉紅橫躺行，從長到短**（$\mathbf{u}^*_1$ 最長、$\mathbf{u}^*_2$ 中、$\mathbf{u}^*_3$ 最短）— 視覺直觀展示「上三角 + 主元」。

**閱讀順序：** 由左到右讀「$A$ = 楔形 1 + 楔形 2 + 楔形 3 = $L$ × $U$」。**注意三個楔形的「非零範圍逐層向右下角縮小**」的視覺序列 — 這是 peeling 過程的核心訊息。

#### 數學內容 (Mathematical Content)

對應原書 §6.2 的核心公式：

$$
A = \underbrace{\mathbf{l}_1 \mathbf{u}^*_1}_{\text{楔形 1（滿格）}}
+ \begin{bmatrix} 0 & 0 & 0 \\ 0 & \multicolumn{2}{c}{} \\ 0 & \multicolumn{2}{c}{A_2} \end{bmatrix}
= \underbrace{\mathbf{l}_1 \mathbf{u}^*_1}_{\text{楔形 1}}
+ \underbrace{\mathbf{l}_2 \mathbf{u}^*_2}_{\text{楔形 2}}
+ \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & A_3 \end{bmatrix}
= L U
$$

對應本章範例 $A = \bigl[\begin{smallmatrix}2&1&1\\4&3&3\\8&7&9\end{smallmatrix}\bigr]$：

- **楔形 1** $= \mathbf{l}_1 \mathbf{u}^*_1 = \begin{bmatrix}2 & 1 & 1\\ 4 & 2 & 2\\ 8 & 4 & 4\end{bmatrix}$（**整個 3×3 都有色**，因 $\mathbf{l}_1, \mathbf{u}^*_1$ 全非零）；
- **楔形 2** $= \mathbf{l}_2 \mathbf{u}^*_2 = \begin{bmatrix}0 & 0 & 0\\ 0 & 1 & 1\\ 0 & 3 & 3\end{bmatrix}$（**右下 2×2 有色**，第 1 行 / 列為零）；
- **楔形 3** $= \mathbf{l}_3 \mathbf{u}^*_3 = \begin{bmatrix}0 & 0 & 0\\ 0 & 0 & 0\\ 0 & 0 & 2\end{bmatrix}$（**只右下 1×1 有色**）。

**注意「綠色直條」與「粉紅橫條」的視覺對應：**

- $\mathbf{l}_p$ 直立排在「綠列」位置，所以圖中每個楔形的左側總有一條綠色直條；
- $\mathbf{u}^*_p$ 橫躺排在「粉紅行」位置，所以圖中每個楔形的頂端總有一條粉紅橫條；
- 兩者相交的「左上格」是楔形的「主元位置」（雖然圖中顯示為整個內框灰色，但實際是 $L_{pp} \cdot u_{pp}$ 的乘積，這個位置決定整個楔形的縮放）。

#### 直覺解讀 (Intuition)

LU1 是「**從 $A$ 倒推到 $L, U$**」的視覺證明 — 與 §6.1 CR 「掃描列、留獨立」的離散邏輯不同，**LU 是「連續剝皮」的視覺**：

- **三個楔形視覺上「**逐層向右下角縮小**」** — 楔形 1 最大（滿格）、楔形 2 中等（右下 2×2）、楔形 3 最小（右下 1×1）；
- **每個楔形的「綠列」和「粉紅行」共用一個主元** — 第 $p$ 個楔形的主元在 $(p, p)$ 位置；
- **三個楔形之和精確還原 $A$** — 因為「外層楔形 + 內層子矩陣」就是 $A$ 的一個重新拆解，且每次拆解都剝掉一個秩 1（rank 1）的部分；
- **最終結果 $L$ 的「綠列高度」與 $U$ 的「粉紅行長度」對應** — $\mathbf{l}_1$ 是最高的（滿格 $n$ 個元素，3 個），$\mathbf{l}_n$ 是最矮的（只有自己一個元素，1 個）；$\mathbf{u}^*_1$ 是最長的（$n$ 個元素），$\mathbf{u}^*_n$ 是最短的（1 個）。

**為什麼沒有 `using PX` 標籤？** 因為 LU1 強調的是 **「**從 $A$ 解構到子矩陣 $A_2, A_3$**」** 的遞迴過程，是「**消去演算法的視覺化**」，不是「線性組合視角」（P1/P2）也不是「外積累加視角」（MM4）。LU1 與 LU2 構成對偶：**LU1 = 解構（peeling）、LU2 = 重組（MM4 累加）**。

**這張圖該做成互動視覺化的理由：** 靜態圖只能展示三個固定的楔形，**互動 demo 可以讓用戶調 $A$ 看到每個楔形如何隨主元變化、消去過程如何遞迴前進、子矩陣 $A_2, A_3$ 如何「浮現」於右下角**。這是把「高斯消去」從「行運算口訣」變成「視覺數字流動」的最佳切入點。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [LU 雙視角切換 + 三色 rank 1 peeling 動畫] ⭐⭐⭐
> 「拉桿調 $A$ 的元素 → 動態剝下三個秩 1 楔形 → 同步顯示 $L, U$ 結構；toggle 切換 peeling 視角（LU1）/ MM4 合成視角（LU2）/ 並排兩者」
> **詳見劇本：** VizScript-01（章末）

> 🎬 **VizMark-02** [高斯消去步驟對齊] ⭐⭐
> 「逐步消去動畫：每步顯示『目前主元位置 / 行乘數 $L_{ij}$ / 消去後的 $A_p$』，最後對齊到 $L, U$」
> **詳見劇本：** VizScript-02（章末，精簡版）

> 🎬 **VizMark-03** [3×3 範例 walkthrough] ⭐
> 「用書中範例 $\bigl[\begin{smallmatrix}2&1&1\\4&3&3\\8&7&9\end{smallmatrix}\bigr]$ 一步一步動畫展示三次 peeling，每步顯示具體數字」
> **詳見劇本：** VizScript-03（章末，輕量版）

---

### Figure 6.4: 從 $L, U$ 用 (MM4) 重組 $A$（LU2）— 標 using MM4

**圖檔：** `docs/book/figs-png/LU2.png`（原始 EPS：`figs/LU2.eps`）
**原書頁碼：** p.9 圖 14
**所屬章節：** §6.2 $A = LU$（重組視角，**標 using MM4**）

#### 視覺結構 (Visual Structure)

整張圖**左右橫向布局**（與 LU1 對偶但方向相反，從 $L, U$ 出發重組 $A$），共 11 段：

1. **第 1 段：** $L$（方框內 3 條綠色直立列，從高到低）；
2. **第 2 段：** $U$（方框內 3 條粉紅橫躺行，從長到短）；
3. **第 3 段：** 等號 `=`；
4. **第 4 段：** 第 1 個秩 1 矩陣 — 方框內**外層楔形**（第 1 行粉紅 + 第 1 列綠 + 內部灰）；
5. **第 5 段：** 加號 `+`；
6. **第 6 段：** 第 2 個秩 1 矩陣 — 方框內**第 2 層楔形**（第 2 行粉紅 + 第 2 列綠 + 右下 2×2 灰）；
7. **第 7 段：** 加號 `+`；
8. **第 8 段：** 第 3 個秩 1 矩陣 — 方框內**最內層**（只右下 1×1 粉紅 + 綠）；
9. **第 9 段：** （隱含）等號 `=` 連接到 $A$，但 LU2 圖直接終止於 3 個秩 1 矩陣的疊加（讀者心中想像疊加結果 = $A$）；
10. **第 10–11 段：** **右下角圖示**：圓圈內標 `MM 4`（兩行），左側文字 `using` — **直接標明「本圖用 §4 Pattern MM4 視角」**，即「矩陣乘法 = 列 × 行外積之和」。

**閱讀順序：** 由左到右讀整個等式鏈 $L \cdot U =$ 楔形 1 $+$ 楔形 2 $+$ 楔形 3。**「$\cdot$」隱在 $L$ 和 $U$ 並排之間**，因為 $LU$ 的乘法被 (MM4) 視角「拆解」為三個秩 1 矩陣的疊加。

#### 數學內容 (Mathematical Content)

對應數學表示（**(MM4) 視角的標準形式**）：

$$
LU = \sum_{p=1}^{n} \mathbf{l}_p \mathbf{u}^*_p
= \mathbf{l}_1 \mathbf{u}^*_1 + \mathbf{l}_2 \mathbf{u}^*_2 + \mathbf{l}_3 \mathbf{u}^*_3 = A
$$

對應本章範例：

- $\mathbf{l}_1 \mathbf{u}^*_1 = (1, 2, 4)^{\mathrm{T}} (2, 1, 1) = \begin{bmatrix}2&1&1\\4&2&2\\8&4&4\end{bmatrix}$；
- $\mathbf{l}_2 \mathbf{u}^*_2 = (0, 1, 3)^{\mathrm{T}} (0, 1, 1) = \begin{bmatrix}0&0&0\\0&1&1\\0&3&3\end{bmatrix}$；
- $\mathbf{l}_3 \mathbf{u}^*_3 = (0, 0, 1)^{\mathrm{T}} (0, 0, 2) = \begin{bmatrix}0&0&0\\0&0&0\\0&0&2\end{bmatrix}$；
- 三項相加 $= A$ ✓。

**與 §4 (MM4) 的關係（using MM4 標籤的重要性）：**

- §4 (MM4) 是「**$AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$**」的一般化版（$A$ 任意 $m \times k$，$B$ 任意 $k \times n$，$\mathbf{a}_p$ = $A$ 第 $p$ 列、$\mathbf{b}^*_p$ = $B$ 第 $p$ 行）；
- LU2 把這個 (MM4) **套用到 $L, U$**：$\mathbf{a}_p \to \mathbf{l}_p$、$\mathbf{b}^*_p \to \mathbf{u}^*_p$；
- 特化點：$\mathbf{l}_p$ 是「下三角列」（前 $p-1$ 個 0）、$\mathbf{u}^*_p$ 是「上三角行」（前 $p-1$ 個 0）— **這是 (MM4) 的「三角特例」**。

「`using MM4` 標籤」的意涵：原書作者**刻意**標明「LU 重組」就是 (MM4) 的應用。這代表視覺化可以**直接重用 ch04 VizScript-02 的秩 1 累加動畫**，只是把「自由的 $\mathbf{a}_p, \mathbf{b}^*_p$」換成「三角的 $\mathbf{l}_p, \mathbf{u}^*_p$」。這個跨章連結是 S07 PNG 重核發現的「**`using XX` 標記是跨章 pointer 官方鐵證**」的延續。

#### 與 LU1 的對偶關係（重要）

| | LU1 | LU2 |
|---|---|---|
| 視角 | 解構（從 $A$ 倒推 $L, U$）| 重組（從 $L, U$ 推 $A$）|
| 流程 | $A$ → 楔形 1 + $A_2$ → 楔形 1 + 楔形 2 + $A_3$ → ... → $LU$ | $L \cdot U$ → 楔形 1 + 楔形 2 + 楔形 3 → $A$ |
| 強調 | 「**剝皮**」（peeling）的遞迴過程 | 「**累加**」（accumulation）的展開過程 |
| 連結 §4/§5 | 無直接標籤（peeling 是 LU 特有演算法）| **`using MM4`**（直接點明 §4 (MM4)）|
| 教學意義 | 解釋「為什麼」可以分解（高斯消去）| 解釋「怎麼」用分解（重組）|
| 視覺化建議 | 動畫遞迴剝皮，子矩陣 $A_2, A_3$ 浮現 | 動畫秩 1 累加，pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) |

**這對「對偶圖」延續 §6.1 CR1/CR2 的全書一致模式：** 每個分解（CR、LU、QR、QΛQᵀ、SVD）都從「**正向**」（解構）和「**反向**」（重組）兩個方向各畫一張圖。S08 LU 進一步驗證了這個模式 — 預期 §6.4 QΛQᵀ 和 §6.5 SVD 也會有類似的對偶兩張圖。

#### 直覺解讀 (Intuition)

LU2 是「**$LU$ 怎麼重新組成 $A$**」的視覺證明 — 把 $L, U$ 的乘法「展開為三個秩 1 楔形的加法」。讀者看到：

- **第 1 個楔形** 來自 $L$ 的第 1 列 × $U$ 的第 1 行 — 整個矩陣都有貢獻（因 $\mathbf{l}_1, \mathbf{u}^*_1$ 全非零）；
- **第 2 個楔形** 來自 $L$ 的第 2 列 × $U$ 的第 2 行 — 因 $L_{12} = 0, U_{21} = 0$，第 1 行 / 列為零，貢獻集中於右下 2×2；
- **第 3 個楔形** 來自 $L$ 的第 3 列 × $U$ 的第 3 行 — 因前兩元素都為 0，只剩右下 1×1 的「主元 $u_{33}$ 自己」。

**「逐層內縮」的視覺意義：** $L, U$ 的三角結構**強制**了每個秩 1 矩陣的「非零範圍向右下角縮小」。這是「**結構驅動的稀疏化**」— 與 §5 (P3)(P4) 的「對角矩陣 sandwich」類似（三角矩陣是 sandwich 的「**單側版**」）。

**為什麼 `using MM4` 標籤這麼關鍵？** 它把「LU 看似神秘的數值算法」**還原**到「§4 教過的最直接矩陣乘法視角」— **沒有新概念**，只是 (MM4) 套到三角結構上。讀者學過 §4 (MM4) 後，LU2 立刻可以「秒懂」，無需重新建立心智模型。**這是原書「五大分解都用 (MM4) 統一視角」的設計核心**。

#### 視覺化機會（VizMark 引用）

LU2 主要由 VizMark-01 涵蓋（與 LU1 共用對偶切換）。

> 🎬 **VizMark-01** [LU 雙視角切換]（同 LU1，含 MM4 重組模式）
> **詳見劇本：** VizScript-01（章末）

---

## 視覺化劇本（VizScripts）

### VizScript-01: LU 雙視角切換 + 三色 rank 1 peeling 動畫（LU Toggle Animation）

**Tier：** ⭐⭐⭐ Tier 2（含 peeling/MM4 雙模式切換 + 三色秩 1 累加動畫；MM4 模式單 pointer 指 ch04 VizScript-02）
**對應 VizMark：** Figure 6.3 VizMark-01、Figure 6.4 VizMark-01
**預估實作工作量：** S12+ 約 2 session（畫面框架 1 session + 互動邏輯與高斯消去計算 1 session）

#### A. 一句話定位

「給一個方陣 $A$，動態展示 $LU$ 分解的兩個視角 — peeling（從 $A$ 剝下三個秩 1 楔形）/ MM4（從 $L, U$ 累加成 $A$）— 並切換兩者，視覺驗證 $A = LU = \sum_p \mathbf{l}_p \mathbf{u}^*_p$。」

#### B. 學習目標（Learning Outcome）

- **peeling 遞迴直覺：** 看到一個方陣，能想像它「逐層剝下秩 1 楔形」的過程，把高斯消去從口訣化為視覺；
- **MM4 累加直覺：** 看到 $L, U$，能立刻看出「列 × 行外積之和」結構，**LU 是 (MM4) 的三角特例**；
- **雙視角切換：** 透過 peeling 模式和 MM4 模式的對偶呈現，建立「**解構 = 重組的反向操作**」的反射弧；
- **跨章連結：** 點 (MM4) 按鈕跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02) 看一般化的秩 1 累加（不限三角）。

#### C. 互動參數（UI Inputs）

- **矩陣輸入 $A$：** $n \times n$ 格子網格，$n \in [2, 5]$，每格 $a_{ij} \in [-9, 9]$ 步進 1；
- **預設範例選擇器：**
  - 範例 1：$\bigl[\begin{smallmatrix}2&1&1\\4&3&3\\8&7&9\end{smallmatrix}\bigr]$（書中範例，無需換行，主元 $2, 1, 2$）；
  - 範例 2：$\bigl[\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr]$（最小 2×2 範例）；
  - 範例 3：$\bigl[\begin{smallmatrix}1&1&1\\1&2&3\\1&3&6\end{smallmatrix}\bigr]$（Pascal 矩陣，全主元 = 1）；
  - 範例 4：$\bigl[\begin{smallmatrix}2&4&2\\1&3&5\\3&5&7\end{smallmatrix}\bigr]$（中等大小，主元混合正負）；
  - 範例 5：$\bigl[\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr]$（**陷阱題**：主元 = 0，需要換行，顯示「LU 失敗 → 改用 PA = LU」提示）；
- **視角切換 (radio)：** `peeling 視角 (LU1)` / `MM4 重組視角 (LU2)` / `同時看兩者（並排）`；
- **掃描速度滑桿：** 自動 peeling / 累加動畫的速度（0.5×–4×）；
- **跳轉按鈕：**
  - 「→ (MM4) 一般秩 1 累加」按鈕（跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)，自動載入 $(\mathbf{l}_p, \mathbf{u}^*_p)$ 序列當作 $(\mathbf{a}_p, \mathbf{b}^*_p)$）；
  - 「→ 解方程 demo」按鈕（跳本章 VizScript-02 的「前代 + 後代」流程）。

#### D. 視覺布局（Layout）

**主畫面三區（並排視角時）：**

| 區 | 內容 |
|---|---|
| 左區（輸入） | $A$ 的格子輸入網格 + 預設範例選擇器 + 滑桿 |
| 中區（peeling 視角 LU1） | $A$（灰格）$= \mathbf{l}_1 \mathbf{u}^*_1 + \cdots + \mathbf{l}_n \mathbf{u}^*_n$，逐項剝下動畫 + 子矩陣 $A_2, A_3$ 在右下角浮現 + 最終 $L, U$ 在右側 |
| 右區（MM4 重組視角 LU2） | $L \cdot U =$ 三個秩 1 楔形相加，逐項累加動畫；底部 `using MM4` 圖示（圓圈標）+ 跳轉按鈕指 ch04 VizScript-02 |

**底部資訊條：**

- $n$ = 當前矩陣大小；
- $L$ 和 $U$ 的形狀（$n \times n$ × $n \times n$）；
- 每個主元 $u_{pp}$ 顯示（大字）+ 是否為零（紅警示）；
- 「**換行警示**」：若某主元為 0，顯示「需要 PA = LU，本動畫先跳過」（範例 5 陷阱題使用）。

#### E. 動畫腳本（Storyboard）

**Step 1（0–600ms）：** $A$ 的格子網格從左區滑入中區，每格元素淡入。

**Step 2（600–1200ms）：** **第 1 個 peeling**：
- 第 1 列高亮綠 → 主元 $a_{11}$ 高亮金 → 第 1 列除以主元變成 $\mathbf{l}_1$（綠色直條浮出，移到右側 $L$ 的第 1 列位置）；
- 第 1 行高亮粉紅 → 變成 $\mathbf{u}^*_1$（粉紅橫條浮出，移到右側 $U$ 的第 1 行位置）；
- 楔形 1 ($\mathbf{l}_1 \mathbf{u}^*_1$) 出現在中區「楔形堆疊」位置（外層楔形）；
- $A$ 減去楔形 1，第 1 行 / 列清零（變灰），右下角 $(n-1) \times (n-1)$ 子矩陣 $A_2$ 浮現（藍色高亮邊框）。

**Step 3（1200–1800ms）：** **第 2 個 peeling**：對 $A_2$ 重複上述，得 $\mathbf{l}_2, \mathbf{u}^*_2$，楔形 2 加入堆疊（內縮楔形）。

**Step 4（1800–2400ms）：** **第 3 個 peeling**：對 $A_3$ 重複，得 $\mathbf{l}_n, \mathbf{u}^*_n$，楔形 $n$ 加入堆疊（最內楔形）。

**Step 5（2400–3000ms）：** 完成。$A$ 全變灰（已被剝光）、$L, U$ 在右側完整顯示、中區堆疊三個楔形排列「外→中→內」。

**Step 6（可選，按 MM4 視角切換）：** 切到右區的 MM4 重組視角：
- $L, U$ 從中區複製到右區左上；
- 每個 $\mathbf{l}_p \mathbf{u}^*_p$ 楔形從左下「飛入」累加區（外積動畫）；
- 累加區的灰色 $A$ 逐步「充實」（每加一項變亮一些）；
- 最終 $A$ 完全顯示，與中區的 $A$ 並排（驗證一致）；
- 底部 `using MM4` 標籤淡入 + 「→ ch04 VizScript-02」按鈕高亮。

**Step 7（按「解方程」按鈕）：** 跳到 VizScript-02 流程。

#### F. 配色（依全書視覺一致性錨點）

- **綠 `#2ca02c`：** $L$ 的列 $\mathbf{l}_p$ / 楔形左側綠條 / 主元周邊的綠輔助線；
- **粉紅 `#d62728`：** $U$ 的行 $\mathbf{u}^*_p$ / 楔形頂端粉紅條 / 主元周邊的粉紅輔助線；
- **金 `#FFD700`（新增）：** 主元 $u_{pp}$ 高亮（即將被剝離的位置）；
- **藍 `#1f77b4`：** $A_p$ 子矩陣的邊框 / 解方程模式下 $\mathbf{b}$ 向量的元素；
- **灰 `#cccccc`：** 已被剝離的元素（變淡）；
- **紫 `#9467bd`：** 換行警示（當主元 = 0 時）。

#### G. 計算邏輯（Numerical Backend）

```python
def lu_factorization_peeling(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, list[np.ndarray]]:
    """Return L, U, and the list of intermediate A_p matrices and rank-1 wedges."""
    n = A.shape[0]
    A_p = A.astype(float).copy()
    L = np.eye(n)
    U = np.zeros((n, n))
    wedges = []
    A_history = [A_p.copy()]
    for p in range(n):
        pivot = A_p[p, p]
        if abs(pivot) < 1e-12:
            raise ValueError(f"Pivot zero at row {p}, need PA = LU")
        u_p = A_p[p, :].copy()       # u^*_p
        l_p = A_p[:, p] / pivot       # l_p, with l_p[p] = 1
        wedge = np.outer(l_p, u_p)    # rank-1 wedge
        wedges.append(wedge)
        L[:, p] = l_p
        U[p, :] = u_p
        A_p = A_p - wedge
        A_history.append(A_p.copy())
    return L, U, wedges, A_history
```

**驗證：** $\sum_p \text{wedges}[p] = A$（與 LU2 視角）；$L \cdot U = A$（與 LU1 結果）。

#### H. 跨章 pointer 邏輯

- **「→ (MM4) 秩 1 累加」按鈕（MM4 重組模式可見）：**
  - 點擊 → 跳 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)；
  - 自動把當前 $(\mathbf{l}_p, \mathbf{u}^*_p)$ 序列載入為 ch04 的 $(\mathbf{a}_p, \mathbf{b}^*_p)$ 序列；
  - ch04 動畫自動進入「3 項累加」模式並對齊本章的 peeling 順序。

- **「→ 解方程 demo」按鈕（peeling 模式可見）：**
  - 點擊 → 進入本章 VizScript-02 的「前代 + 後代」流程；
  - 自動帶入當前 $L, U$ + 預設 $\mathbf{b} = (1, 5, 17)^{\mathrm{T}}$。

#### I. UI 元件清單（Component Inventory）

| 元件 | 類型 | 預期實作 |
|---|---|---|
| 矩陣格子網格 | grid input | $n \times n$ 個 `<input type="number">`，autocomplete 整數 |
| 預設範例下拉 | select | 5 個範例 |
| 視角 radio | radio group | 3 選項（peeling / MM4 / 並排）|
| 動畫速度滑桿 | range | 0.5–4.0，step 0.25 |
| 跳轉按鈕 | button | 2 個（→ ch04、→ 解方程）|
| 主元高亮指示 | label | 顯示當前主元值 + 換行警示 |
| 楔形堆疊 | layered SVG | 3 層 SVG 楔形依序疊加 |
| $L, U$ 結構顯示 | 2 個小矩陣框 | 綠列 / 粉紅行排列 |

#### J. 教學文案（Voiceover / Caption Script）

- **開場：** 「$A = LU$ 把方陣拆成下三角 $L$ 乘上三角 $U$。但**這是怎麼來的**？答案是『**逐層剝下秩 1 楔形**』。」
- **第 1 次 peeling：** 「取 $A$ 的第 1 列除以主元 $a_{11}$，得 $\mathbf{l}_1$；取第 1 行直接成 $\mathbf{u}^*_1$。兩者外積 $\mathbf{l}_1 \mathbf{u}^*_1$ 是『**外層楔形**』。從 $A$ 減去這個楔形，剩下的就是小一號的子矩陣 $A_2$。」
- **遞迴：** 「對 $A_2$ 重複同樣動作，得 $\mathbf{l}_2, \mathbf{u}^*_2$ 和『**內縮楔形**』。再對 $A_3$ 重複……直到剝光。」
- **MM4 切換：** 「現在從另一個方向看：把 $L$ 的每列 × $U$ 的對應行相加，剛好還原 $A$。**這就是 §4 (MM4) 教過的『列 × 行外積之和』** — 圖右下角 `using MM4` 標籤就是在點明這件事。」
- **總結：** 「LU 分解的兩個視角 — peeling（解構）和 MM4（重組）— 是同一件事的兩個方向。**這是高斯消去的視覺化本質**。」

#### K. 退化案例 + 邊界處理（Edge Cases）

- **主元為零：** 顯示紅色警示「需要換行 (PA = LU)，本動畫只示範可直接分解的情形」，提供「換到範例 1」按鈕；
- **數值不穩定：** 當主元 $|u_{pp}| < 10^{-6}$ 顯示橙色警示「主元接近零，數值不穩，建議換行」；
- **退化矩陣（rank < n）：** $LU$ 仍可能存在（某些 $\mathbf{l}_p \mathbf{u}^*_p$ 為全零項），動畫顯示對應的楔形「淡出/消失」效果；
- **$n = 2$ 最小情形：** 只有兩次 peeling，動畫節奏加快（每步 500ms）；
- **大型矩陣（$n > 5$）：** 不開放（避免畫面塞）；S12+ 可考慮 $n = 6, 7$ 但需 scrolling。

#### L. 學習評量提示（Assessment Hooks）

互動結束時提供「**理解檢核**」：

1. **概念題：** 「如果 $A$ 的第 1 列除了 $a_{11}$ 全為 0，第 1 個楔形 $\mathbf{l}_1 \mathbf{u}^*_1$ 會長什麼樣？」（答：只有第 1 行有色，因 $\mathbf{l}_1 = (1, 0, 0)^{\mathrm{T}}$，外積只取出 $\mathbf{u}^*_1$ 的第 1 行）；
2. **計算題：** 「給 $L = \bigl[\begin{smallmatrix}1&0\\3&1\end{smallmatrix}\bigr], U = \bigl[\begin{smallmatrix}2&5\\0&7\end{smallmatrix}\bigr]$，畫出兩個秩 1 楔形並驗證相加 = $LU$。」
3. **遞迴題：** 「為什麼 peeling 的子矩陣 $A_{p+1}$ 的左上角 $p \times p$ 必為零？」（答：被前 $p$ 個楔形「完全覆蓋」並減去）；
4. **跨章連結題：** 「點 → ch04 VizScript-02 按鈕，把當前 $\mathbf{l}_p, \mathbf{u}^*_p$ 序列看成自由列向量 / 行向量，動畫應該還原 $A$。**這個一致性說明什麼？**」（答：(MM4) 是 LU 的母模板，LU 只是 (MM4) 的三角特化）。

#### M. 實作里程碑（Milestones for S12+）

1. **M1（第 1 session）：** 畫面框架（左/中/右三區 + 預設範例選擇 + radio）；
2. **M2：** Peeling 動畫（單視角 LU1）— 三步剝皮 + 子矩陣浮現；
3. **M3：** MM4 重組動畫（單視角 LU2）— 三步秩 1 累加；
4. **M4（第 2 session）：** 雙視角並排 + 同步控制 + 速度滑桿；
5. **M5：** 跨章 pointer 整合（→ ch04 VizScript-02 + → 解方程 demo）；
6. **M6：** 邊界處理（主元為零警示 + 退化情形）；
7. **M7：** 教學文案 + 評量檢核 + 5 個預設範例驗證；
8. **M8：** Demo 部署 + 嵌入 ch06c-LU.md。

---

### VizScript-02: 高斯消去步驟 + 解 $A\mathbf{x} = \mathbf{b}$（精簡）

**Tier：** ⭐⭐ Tier 1 精簡（不含對偶切換，只展示前代 + 後代流程）
**對應 VizMark：** Figure 6.3 VizMark-02
**預估實作工作量：** S12+ 約 1 session

#### A. 一句話定位

「給定 $L, U, \mathbf{b}$，動畫展示『前代解 $L\mathbf{c} = \mathbf{b}$ → 後代解 $U\mathbf{x} = \mathbf{c}$』，並驗證 $A\mathbf{x} = \mathbf{b}$。」

#### B–D. 互動 + 布局

- **輸入：** $L, U$ 從 VizScript-01 帶入（或手動輸入 / 預設範例）+ $\mathbf{b}$ 列向量輸入（$n$ 個元素 $\in [-20, 20]$）；
- **布局：** 上半部「前代區」（$L \cdot \mathbf{c} = \mathbf{b}$ 三角方程組）+ 下半部「後代區」（$U \cdot \mathbf{x} = \mathbf{c}$ 三角方程組）。

#### E. 動畫腳本

**Step 1（前代）：** 從第 1 行往下，依序計算 $c_1, c_2, \ldots, c_n$：
- $c_1 = b_1$（直接讀）；
- $c_2 = b_2 - L_{21} c_1$（高亮 $L_{21}$ 和 $c_1$ 的乘積，從 $b_2$ 減去）；
- $c_3 = b_3 - L_{31} c_1 - L_{32} c_2$（更長的減法鏈）；
- ...
- 每步顯示具體數字計算過程 + 結果 $c_p$ 填入右側 $\mathbf{c}$ 向量。

**Step 2（後代）：** 從第 $n$ 行往上，依序計算 $x_n, x_{n-1}, \ldots, x_1$：
- $x_n = c_n / u_{nn}$（高亮主元 $u_{nn}$）；
- $x_{n-1} = (c_{n-1} - u_{n-1, n} x_n) / u_{n-1, n-1}$；
- ...
- 每步顯示具體計算 + 結果填入右側 $\mathbf{x}$ 向量。

**Step 3（驗證）：** 計算 $A\mathbf{x}$ 並與 $\mathbf{b}$ 並排顯示「✓ 相等」。

#### F–G. 配色 + 計算邏輯

配色同 VizScript-01。

```python
def forward_substitution(L: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = L.shape[0]
    c = np.zeros(n)
    for i in range(n):
        c[i] = b[i] - L[i, :i] @ c[:i]
    return c

def back_substitution(U: np.ndarray, c: np.ndarray) -> np.ndarray:
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (c[i] - U[i, i+1:] @ x[i+1:]) / U[i, i]
    return x
```

#### H–M. 其餘段落

精簡版只保留核心動畫 + 1 個範例（$\mathbf{b} = (1, 5, 17)^{\mathrm{T}}$），其餘段落直接複用 VizScript-01 的設定（避免重複）。預估文字 ~500 字，動畫 1.5 分鐘。

---

### VizScript-03: 3×3 範例 walkthrough（輕量）

**Tier：** ⭐ Tier 1 輕量（單一範例逐步動畫，無互動參數）
**對應 VizMark：** Figure 6.3 VizMark-03
**預估實作工作量：** S12+ 約 0.5 session

#### A. 一句話定位

「對範例 $A = \bigl[\begin{smallmatrix}2&1&1\\4&3&3\\8&7&9\end{smallmatrix}\bigr]$ 逐步動畫展示 peeling 三步驟，每步顯示具體數字。」

#### B–E. 簡述

- **輸入：** 無（固定範例）；
- **動畫腳本：** 3 段（剝下楔形 1 → 楔形 2 → 楔形 3），每段約 4 秒，總長 12 秒；
- **目標：** 入門用，學生第一次看 LU peeling 時用此 demo 建立直覺，看完後再點 VizScript-01 自由探索。

#### F–M. 其餘段落

配色同 VizScript-01；無互動，純線性動畫；無評量。預估文字 ~300 字。

---

## 小結

- **§6.2 A=LU** 是 §6 五大分解的第二個，數值上最重要（解 $A\mathbf{x} = \mathbf{b}$ 的標準方法）；
- **與 (MM4) 的連結直接顯式：** LU2 圖標 `using MM4`，是 S07 PNG 重核發現的「跨章 pointer 官方鐵證」第二例；
- **三個 VizScript：** ⭐⭐⭐ 雙視角（peeling/MM4）切換 + ⭐⭐ 前代/後代解方程 + ⭐ 範例 walkthrough；
- **下一章 §6.3 A=QR：** 把 LU 的「下三角 $L$」換成「正交 $Q$」，引入 Gram–Schmidt 正交化過程。
