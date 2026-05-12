# 6. 矩陣的五大分解（The Five Factorizations of a Matrix）— 總覽

> **原書頁碼：** p.7–p.8（總覽表），實際細節 p.8–p.13（§6.1–§6.5）
> **對應 .tex 段落：** `The-Art-of-Linear-Algebra.tex` § The Five Factorizations of a Matrix（en.md line 205–254 為總覽段；§6.1–§6.5 自 256 起）
> **本章圖數：** 1（總覽圖 `5-Factorizations.png`）
> **本章 VizMark 數：** 1（⭐⭐⭐ × 1，Tier 1 + pointer）
> **狀態：** [x] 已完成（S07）

---

## 章節摘要

§1–§4 把矩陣的「乘法」拆成四個視角（MM1/MM2/MM3/MM4），§5 把幾個實用配置（對角矩陣縮放、$XD\mathbf{c}$、$U\Sigma V^{\mathrm{T}}$ 三明治）提煉為 Pattern。本章 §6 是全書的**結論章**：把所有矩陣（square、rectangular、symmetric、orthogonal、任意）對應到**五個經典分解**，並且每個分解都能用前面建立的視覺語彙（綠色直立列 / 粉紅橫躺行 / 藍點對角元素 / 三明治結構）一眼看出形狀。

五大分解：

1. **$A = CR$** — 任意矩陣 → 獨立列（column）× 行階梯形（row echelon form）。**列秩 = 行秩**最直觀的證明。
2. **$A = LU$** — 方陣（無 row exchange）→ 下三角 × 上三角。Gaussian 消去法的矩陣化。
3. **$A = QR$** — 任意列獨立矩陣 → 正交列 × 上三角。Gram–Schmidt 正交化。
4. **$S = Q\Lambda Q^{\mathrm{T}}$** — 對稱矩陣 → 特徵向量 × 對角特徵值 × 特徵向量轉置。**$S$ 而非 $A$，凸顯只適用對稱**。
5. **$A = U\Sigma V^{\mathrm{T}}$** — **任意矩陣**（含長方）→ 兩組正交基 × 對角奇異值。最一般的「分解之王」。

本章作為**第 6 章的開門總覽**，重點不在公式細節（細節留給 §6.1–§6.5），而在三件事：

- **形狀辨識**：5 個分解的視覺結構各自的「指紋」（哪個是兩塊綠色直立列？哪個有藍點對角？哪個是三明治？）；
- **適用條件**：什麼形狀的矩陣（rectangular vs square、general vs symmetric vs orthogonal）對應哪個分解；
- **與 §1–§5 的關係**：每個分解都能用 (MM4) 寫成「秩 1 之和」，並且每個分解都是 §5 某個 Pattern 的特例或組合。

掌握本章，後續 §6.1–§6.5 就只剩「驗證形狀 + 推導步驟」。

---

## 數學要點

### 1. 五大分解總表

| 編號 | 分解 | 適用矩陣 | 三因子形狀 | 核心定理 / 用途 | 細節章節 |
|---|---|---|---|---|---|
| **F1** | $A = CR$ | 任意 $m \times n$ | $\underbrace{C}_{m \times r}\underbrace{R}_{r \times n}$（$r$ = rank） | **列秩 = 行秩** | §6.1（`ch06b-CR.md`） |
| **F2** | $A = LU$ | 方陣 $n \times n$（無 row exchange） | $\underbrace{L}_{n \times n}\underbrace{U}_{n \times n}$（下三角 × 上三角） | 解 $A\mathbf{x}=\mathbf{b}$ 的 Gaussian 消去 | §6.2（`ch06c-LU.md`） |
| **F3** | $A = QR$ | $m \times n$ 列獨立（$m \ge n$） | $\underbrace{Q}_{m \times n}\underbrace{R}_{n \times n}$（正交列 × 上三角） | Gram–Schmidt、最小二乘 | §6.3（`ch06d-QR.md`） |
| **F4** | $S = Q\Lambda Q^{\mathrm{T}}$ | **對稱**方陣 $n \times n$ | $\underbrace{Q}_{n \times n}\underbrace{\Lambda}_{n \times n}\underbrace{Q^{\mathrm{T}}}_{n \times n}$（三明治：正交 × 對角 × 正交轉置） | 譜定理、PCA、二次型 | §6.4（`ch06e-QLQ.md`） |
| **F5** | $A = U\Sigma V^{\mathrm{T}}$ | **任意** $m \times n$ | $\underbrace{U}_{m \times m}\underbrace{\Sigma}_{m \times n}\underbrace{V^{\mathrm{T}}}_{n \times n}$（三明治：正交 × 矩形對角 × 正交轉置） | 低秩近似、PCA、Eckart–Young | §6.5（`ch06f-USV.md`） |

**符號規約：**

- $r$ = $\operatorname{rank}(A)$，本章用「分解 reduces to $r$ outer products」這個視角串連 §4 (MM4)；
- $C$ 的列 = $A$ 的**獨立列**；$R$ = $A$ 的 reduced row echelon form（去掉零行）；
- $L$ = 下三角，對角為 1；$U$ = 上三角，對角為主元（pivot）；
- $Q$ = 正交（orthogonal），$Q^{\mathrm{T}}Q = I$（列正交，「窄而長」形狀時為左逆）；
- $\Lambda$ = 對角矩陣，藍點為特徵值 $\lambda_i$；$\Sigma$ = 矩形對角，藍點為奇異值 $\sigma_i \ge 0$ 且降冪；
- **F4 用 $S$ 不用 $A$**：原書刻意換符號強調「對稱才能 $Q^{\mathrm{T}}$ 對應 $Q^{-1}$」。

### 2. 視覺辨識指紋（看圖 1 秒辨形狀）

對應 `5-Factorizations.png` 的視覺語彙（綠 = 直立列、粉紅 = 橫躺行、藍點 = 對角元素或正交基的「點群」標記）：

| 分解 | 視覺指紋（從左到右） |
|---|---|
| $A = CR$ | **2 塊綠色直立列**（$C$，獨立列）× **2 塊粉紅橫躺行**（$R$，行階梯） |
| $A = LU$ | **3 階遞減綠色直立列**（$L$，下三角縮短）× **3 階遞減粉紅橫躺行**（$U$，上三角縮短） |
| $A = QR$ | **3 條等高綠色直立列**（$Q$，正交）× **6 個藍點三角排列**（$R$，上三角對角強調） |
| $S = Q\Lambda Q^{\mathrm{T}}$ | **3 條綠色直立列**（$Q$）× **3 個藍點對角**（$\Lambda$）× **3 條綠色橫躺行**（$Q^{\mathrm{T}}$）— **第一個三明治** |
| $A = U\Sigma V^{\mathrm{T}}$ | **3 條綠色直立列**（$U$）× **2 個藍點對角**（$\Sigma$，**個數 = rank**）× **2 條粉紅橫躺行**（$V^{\mathrm{T}}$）— **第二個三明治** |

**形狀辨識口訣：**

- **看「直立列 × 橫躺行」雙層** → CR / LU / QR（「外積之和」之兩層結構）；
- **看「三明治」三層** → QΛQᵀ / UΣVᵀ（「正交 × 對角 × 正交」之三層結構，與 §5 (P3)(P4) 同骨架）；
- **看「藍點對角數量」** → CR/LU/QR 沒對角；QΛQᵀ 對角數 = $n$（含零特徵值也算）；UΣVᵀ 對角數 = $r$（**rank 就是非零奇異值個數**）。

### 3. (MM4) 視角統一形式 — 五大分解都是「秩 1 之和」

§4 (MM4) 教過：兩矩陣相乘 = 兩矩陣的「列 × 行」外積之和。**五大分解全部可用 (MM4) 寫成同一個形式**，只是配料不同：

$$
\text{(共同骨架)} \qquad XY^{\mathrm{T}} \;=\; \sum_{p=1}^{r} \mathbf{x}_p \, \mathbf{y}^{\mathrm{T}}_p
$$

逐個對應到五大分解：

| 分解 | (MM4) 形式 | 項數 | 每項的意義 |
|---|---|---|---|
| $A = CR$ | $A = \displaystyle\sum_{p=1}^{r} \mathbf{c}_p \, \mathbf{r}^{*}_p$ | $r$ | 第 $p$ 個獨立列 × 對應的行階梯行 |
| $A = LU$ | $A = \displaystyle\sum_{p=1}^{n} \mathbf{l}_p \, \mathbf{u}^{*}_p$ | $n$ | 第 $p$ 個 $L$ 列 × 第 $p$ 個 $U$ 行（**剝皮 / peeling**） |
| $A = QR$ | $A = \displaystyle\sum_{p=1}^{n} \mathbf{q}_p \, \mathbf{r}^{*}_p$ | $n$ | 第 $p$ 個正交列 × 第 $p$ 個 $R$ 行 |
| $S = Q\Lambda Q^{\mathrm{T}}$ | $S = \displaystyle\sum_{p=1}^{n} \lambda_p \, \mathbf{q}_p \, \mathbf{q}^{\mathrm{T}}_p$ | $n$ | $\lambda_p$ 加權的特徵向量自外積（**對稱秩 1**） |
| $A = U\Sigma V^{\mathrm{T}}$ | $A = \displaystyle\sum_{p=1}^{r} \sigma_p \, \mathbf{u}_p \, \mathbf{v}^{\mathrm{T}}_p$ | $r$ | $\sigma_p$ 加權的「左 × 右奇異向量」外積 |

**關鍵共通結構：** 每個分解都是「$r$ 或 $n$ 個秩 1 矩陣之和」。差別在：

- **單向 vs 雙向**：CR/LU/QR 是「列向量 × 行向量」，QΛQᵀ/UΣVᵀ 是「向量 × 對角加權 × 向量」（**三明治**）；
- **是否有對角加權**：QΛQᵀ/UΣVᵀ 把「分量大小」抽出成對角矩陣 $\Lambda$ 或 $\Sigma$；
- **基底是否正交**：QR/QΛQᵀ/UΣVᵀ 的「列 / 行向量」彼此正交（內積為 0），CR/LU 不一定。

**這個共通骨架是 §6.1–§6.5 撰寫的母模板**：每章只要回到 (MM4) 累加圖，把 $\mathbf{x}_p$、$\mathbf{y}_p$ 換成各自分解的角色，視覺化的核心動畫就完成。

### 4. 五大分解的「升級鏈」結構

從 (P1)/(P2) 列縮放 → (P1')/(P2') 對角縮放 → (P3) $XD\mathbf{c}$ → (P4) $U\Sigma V^{\mathrm{T}}$ 是 §5 的升級鏈。§6 的五大分解也呈相似升級結構，可看作 §5 Pattern 的「應用版」：

| 階 | 結構複雜度 | 對應分解 | §5 Pattern 對應 |
|---|---|---|---|
| 1 | **兩因子（列 × 行）** | $A = CR$、$A = LU$、$A = QR$ | (P1)/(P2)（列縮放、行縮放） |
| 2 | **三因子（三明治）** | $S = Q\Lambda Q^{\mathrm{T}}$ | (P3)（$XD\mathbf{c}$ 升級，去掉 $\mathbf{c}$，得對稱矩陣分解） |
| 3 | **三因子非方陣（最一般）** | $A = U\Sigma V^{\mathrm{T}}$ | (P4)（$U\Sigma V^{\mathrm{T}}$ 三明治，§5 已預先鋪陳） |

**直覺：** §5 的 (P3)(P4) 不是「孤立的奇技淫巧」，而是 §6.4 / §6.5 的視覺前奏。§6.4 把 (P3) 中的 $\mathbf{c}$ 拿掉、把 $X$ 限制成正交，就得 $S = Q\Lambda Q^{\mathrm{T}}$；§6.5 直接把 (P4) 的圖搬過來、加上「奇異值降冪 + 列獨立」條件，就得 SVD。

### 5. 適用矩陣對照（哪種矩陣對應哪些分解）

| 矩陣類別 | 適用分解 |
|---|---|
| 任意 $m \times n$（含長方、退化） | **$A = CR$**（一定有）、**$A = U\Sigma V^{\mathrm{T}}$**（一定有） |
| $m \times n$ 列獨立（$m \ge n$，$\operatorname{rank}(A) = n$） | + **$A = QR$** |
| 方陣 $n \times n$ 可逆 + 無 row exchange | + **$A = LU$** |
| 方陣 $n \times n$ 可對角化 | + $A = X\Lambda X^{-1}$（**非正交**，本書 §6 未強調，留給附錄） |
| **對稱**方陣 $n \times n$（即 $S = S^{\mathrm{T}}$） | + **$S = Q\Lambda Q^{\mathrm{T}}$**（**強保證實特徵值 + 正交特徵向量**） |
| 正定（positive definite）對稱方陣 | + Cholesky $S = L L^{\mathrm{T}}$（本書 §6 未列，是 $LU$ 的對稱特例） |

**兩個「萬能」分解：** $A = CR$ 和 $A = U\Sigma V^{\mathrm{T}}$ 對**任何**矩陣都成立（含 $r < \min(m, n)$ 的退化情況）。這也解釋為什麼 SVD 被稱為「**矩陣分解之王**」— 它對所有矩陣都能跑、永遠存在、永遠是 $\sigma_p \ge 0$ 降冪、永遠提供最佳低秩近似。

---

## 圖片詳細描述（Figure Description）

### Figure 6.0: 五大分解總覽（The Five Factorizations of a Matrix）

**圖檔：** `docs/book/figs-png/5-Factorizations.png`（原始 EPS：`figs/5-Factorizations.eps`）
**原書頁碼：** p.7–p.8（表 1）
**所屬章節：** §6 開門總覽

#### 視覺結構 (Visual Structure)

整張圖是一個**直立排列的 5 列總表**，每列代表一個分解。每列由**左、中、右三欄**組成：

- **左欄（公式）：** 大字體 LaTeX 公式（$A=CR$、$A=LU$、$A=QR$、$S=Q\Lambda Q^{\mathrm{T}}$、$A=U\Sigma V^{\mathrm{T}}$）；
- **中欄（視覺示意）：** 用前面章節建立的視覺語彙（綠色直立列 = column、粉紅橫躺行 = row、藍色實心圓點 = 對角元素 / 正交基標記）排出每個分解的「形狀指紋」；
- **右欄（三行文字）：** 各分解的核心性質與用途說明（英文原文）。

5 列由上而下：

1. **$A=CR$**：2 塊綠色直立列 緊接著 2 塊粉紅橫躺行（無對角元素），形狀像「兩塊綠木板 + 兩塊粉紅木板」對接；
2. **$A=LU$**：3 塊**遞減高度**的綠色直立列（左最高、中次之、右最矮，呈下三角剪影）緊接著 3 塊**遞減長度**的粉紅橫躺行（上最長、中次之、下最短，呈上三角剪影）；
3. **$A=QR$**：3 塊**等高**的綠色直立列（凸顯正交而非三角）緊接著一個矩陣框框內擺 6 個藍點（呈倒三角排列，凸顯 $R$ 是上三角矩陣，藍點為主元位置）；
4. **$S=Q\Lambda Q^{\mathrm{T}}$**：3 塊綠色直立列 緊接著 3 個藍點對角（從左上到右下排列，中間矩陣的非對角位置完全留白）緊接著 3 塊**綠色橫躺行**（注意：第三塊與第一塊是同色綠，因為 $Q^{\mathrm{T}}$ 就是 $Q$ 的轉置，**第一個三明治結構**）；
5. **$A=U\Sigma V^{\mathrm{T}}$**：3 塊綠色直立列（$U$）緊接著 2 個藍點對角（$\Sigma$，**只有 2 個而不是 3 個** — 視覺強調「rank = 2 < 3」，即矩形對角矩陣只有 $r$ 個非零奇異值）緊接著 2 塊**粉紅**橫躺行（$V^{\mathrm{T}}$，注意：與 $U$ 不同色，因為 $U$ 和 $V$ 是兩組不同的正交基，**第二個三明治結構**）。

**閱讀順序：** 由上而下逐行讀，每行從左（公式）到中（圖）到右（文字）。先掃中欄看「形狀差異」，再回左欄對公式。

#### 數學內容 (Mathematical Content)

5 個分解的數學定義（公式如「§數學要點」總表）。中欄的視覺示意對應以下符號：

- **綠色直立列：** $C / L / Q / U$ 等矩陣的**列向量**（column vectors）；
- **粉紅橫躺行：** $R / U / V^{\mathrm{T}}$ 等矩陣的**行向量**（row vectors）；
- **藍色實心圓點：** $\Lambda$ 的特徵值 $\lambda_i$、$\Sigma$ 的奇異值 $\sigma_i$、$R$（in QR）的主元位置 — 整體傳達「對角矩陣的非零位置」；
- **遞減高度 / 長度的綠 / 粉紅塊：** 三角矩陣（下三角 / 上三角）的「列高度遞減」或「行長度遞減」視覺化；
- **等高 / 等寬正交列：** 正交矩陣 $Q$ 的列在「長度相同 + 互相垂直」上的視覺暗示。

**關鍵尺寸：** 雖然圖中只畫示意 3×3 大小，但比例傳達了：

- CR：$C$ 是「窄而瘦長」（$m \times r$，$r < n$），$R$ 是「矮而寬」（$r \times n$）；
- QR：$Q$ 是「列獨立」與 $A$ 同寬，$R$ 是方陣；
- QΛQᵀ：$Q$ 是方陣、$\Lambda$ 是方對角；
- UΣVᵀ：$U$、$V$ 都是方正交，但 $\Sigma$ 可以是矩形（$m \times n$），多餘部分為零。

#### 直覺解讀 (Intuition)

這張圖是全書的「**最後一頁的速查表**」— 把前面 §1–§5 建立的所有視覺語彙，**一次性套用到 5 個經典分解**，讓讀者一眼看出：

- 「**綠 × 粉紅** = 兩矩陣相乘的最自然色配對」（從 §1 視角開始延續到全書）；
- 「**藍點 = 對角元素 / 個別數字**」（從 §1 一直貫穿）；
- 「**三明治結構** = 三因子 + 中間是對角」（§5 (P3)(P4) 已預先教會，§6.4/§6.5 直接套用）；
- 「**遞減 / 等高 / 對齊** = 三角 vs 正交的視覺指紋」（§6.2 vs §6.3 vs §6.4 的關鍵區別）。

對教學的價值：**讀完前 5 章的讀者，看到本頁 5 行視覺示意，應該能脫口而出每行對應的分解名稱和用途**，無需查公式。本圖就是要訓練這個「形狀 → 分解」的反射弧。

**為什麼這張圖該做成互動視覺化？** 因為形狀辨識需要「同一個矩陣 $A$ 同時看 5 種分解結果」的對照能力。靜態圖只能五個並列死板地看；互動 demo 可以「拉桿選矩陣類型（任意 / 列獨立 / 方陣 / 對稱）→ 自動 highlight 哪些分解適用、哪些不適用 → 點某個分解就 toggle 出該分解的具體數值 + 視覺色塊重排」。這對「形狀 → 適用分解」的反射弧訓練比靜態圖快 10 倍以上（見 VizMark-01）。

#### 視覺化機會（VizMark 引用）

> 🎬 **VizMark-01** [五分解互動切換] ⭐⭐⭐ Tier 1 + pointer
> 「拉桿選矩陣類型 → 自動標記適用分解 → 點分解 toggle 具體數值 + 視覺色塊；(MM4) 累加 demo 全部 pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)」
> **詳見劇本：** VizScript-01（章末）

---

## 視覺化劇本（VizScripts）

### VizScript-01: 五大分解互動切換（5-Factorization Toggle Dashboard）

**Tier：** ⭐⭐⭐ Tier 1 + pointer（核心畫面控制器，秩 1 累加 demo 全部 delegate 到 ch04 VizScript-02）
**對應 VizMark：** VizMark-01（Figure 6.0）
**預估實作工作量：** S12+ 約 1.5 session（畫面框架 + 5 個分解的數值生成 + 適用性閘門邏輯；秩 1 累加動畫**不在本劇本**，重用 ch04 母模板）

> **設計策略（S07 首次正式使用「跨章 pointer」）：**
>
> 本劇本只負責**畫面切換 + 數值對照 + 形狀視覺化**，五個分解的「秩 1 累加動畫」全部不重複實作 — 透過按鈕「→ 看 (MM4) 秩 1 累加動畫」跳轉到 ch04 VizScript-02 並把該分解的 $(\mathbf{x}_p, \mathbf{y}_p)$ 序列當參數傳入。對偶結構（三明治）也透過按鈕「→ 看 P3/P4 三明治動畫」跳轉到 [ch05 VizScript-02](ch05-patterns.md#vizscript-02) / [ch05 VizScript-03](ch05-patterns.md#vizscript-03)。這個策略讓本章在「概念整合」上聚焦，不重複耗工時在已有動畫上。

#### A. 一句話定位

「給一個矩陣 $A$，**同時**看它對應 5 個分解的形狀，並透過點擊跳到每個分解的詳細動畫。」

#### B. 學習目標（Learning Outcome）

- **形狀辨識反射弧：** 看到矩陣類型，1 秒內知道哪些分解適用、哪些不適用；
- **視覺指紋記憶：** 把 5 個分解的視覺結構烙進腦中（兩因子 vs 三明治、有對角 vs 無對角、降冪 vs 等高）；
- **「分解之王」直覺：** 親手切「對稱→任意→退化」，看到只有 CR 和 SVD 永遠適用，建立「SVD 是萬能」的直覺。

#### C. 互動參數（UI Inputs）

- **矩陣類型選擇器（radio）：** 5 個選項 — 「任意 $m \times n$」/ 「列獨立 $m \ge n$」/「方陣可逆」/「對稱方陣」/「自訂（手動輸入）」；
- **尺寸滑桿：** $m \in [2, 6]$、$n \in [2, 6]$；對稱模式 $m = n$ 連動；
- **秩滑桿（rank）：** $r \in [1, \min(m,n)]$（控制「滿秩 vs 退化」，影響 CR 和 SVD 的有效項數）；
- **5 個分解開關（checkbox / tab）：** 點開即顯示該分解的數值 + 視覺示意，**未開啟保持灰階占位**；
- **「→ (MM4) 累加動畫」跳轉按鈕：** 每個分解開關旁有此按鈕，點擊跳 ch04 VizScript-02 並帶該分解的秩 1 序列；
- **「→ 三明治動畫」跳轉按鈕：** QΛQᵀ 和 UΣVᵀ 兩個分解有此按鈕，跳 ch05 VizScript-02/03。

#### D. 視覺布局（Layout）

**主畫面 5 行 × 3 欄總表結構（仿 Figure 6.0）：**

| 行 | 欄 1（公式） | 欄 2（形狀視覺化） | 欄 3（數值 + 跳轉按鈕） |
|---|---|---|---|
| 1 | $A = CR$ | 動態色塊（綠 $C$ + 粉紅 $R$，比例與當前 $r$ 同步） | $\dim C$、$\dim R$、 $r$；按鈕 1（→ MM4 累加） |
| 2 | $A = LU$ | 遞減綠 $L$ + 遞減粉紅 $U$（若不適用，灰階 + 圖示「✗ row exchange needed」） | $L$、$U$ 三角元素；按鈕 1 |
| 3 | $A = QR$ | 等高綠 $Q$ + 上三角藍點 $R$ | $Q^{\mathrm{T}}Q = I$ 驗證面板；按鈕 1 |
| 4 | $S = Q\Lambda Q^{\mathrm{T}}$ | 三明治 + $\lambda_p$ 對角藍點 | 特徵值列表；按鈕 1、按鈕 2（→ P3 三明治） |
| 5 | $A = U\Sigma V^{\mathrm{T}}$ | 三明治 + $\sigma_p$ 對角藍點（個數 = $r$） | 奇異值列表（降冪）；按鈕 1、按鈕 2（→ P4 三明治） |

**頂端控制條：** 矩陣類型 / 尺寸 / 秩；**底部結果條：** 適用性閘門總覽（5 個分解 ✓/✗ 圖示）。

#### E. 動畫流程（Animation Sequence）

1. **(0s) 初始：** 載入「3×3 對稱矩陣」預設，5 行皆綠色 ✓ 適用（對稱方陣是 5 個分解全適用的特例）；
2. **(用戶切「任意 $4 \times 3$」)：** LU 自動變灰打 ✗ （非方陣）、QΛQᵀ 變灰打 ✗（非對稱）；CR/QR/SVD 保留 ✓；色塊比例重排（800ms 動畫）；
3. **(用戶調秩 $r = 2$)：** CR 的綠 $C$ 從 3 列縮成 2 列、SVD 的藍點對角從 3 個縮成 2 個；其他不變；
4. **(用戶點 QR 行的「→ MM4」按鈕)：** 跳轉到 ch04 VizScript-02，自動載入 $(\mathbf{q}_p, \mathbf{r}^*_p)$ 3 對秩 1 序列；
5. **(用戶切「對稱方陣 $3 \times 3$」)：** 全部 5 行恢復 ✓；點 QΛQᵀ 行的「→ P3」按鈕，跳 ch05 VizScript-02 並載入該對稱矩陣的特徵分解作為 $XD\mathbf{c}$ 的特例（$\mathbf{c} = \mathbf{e}_p$ 單位向量逐個）。

#### F. 預設 demo 序列

1. **「對稱方陣 $3 \times 3$」**（全 5 ✓，教學起點，建立「對稱矩陣分解最多」直覺）；
2. **「任意 $4 \times 3$ 滿秩」**（CR/QR/SVD ✓，LU/QΛQᵀ ✗，教學「為什麼 SVD 是萬能」）；
3. **「任意 $4 \times 3$ rank 2 退化」**（只剩 CR 和 SVD ✓，凸顯萬能性）；
4. **「對稱半正定」**（5 ✓ 且 $\lambda_p \ge 0$，鋪陳 §6.5 SVD 是 QΛQᵀ 的推廣）。

#### G. 色彩與樣式（依全書視覺一致性錨點）

- 綠 `#2ca02c`（直立列）/ 粉紅 `#d62728`（橫躺行）/ 藍 `#1f77b4`（對角元素 / 主元）；
- 灰 `#cccccc`（不適用分解的占位）；
- ✓ 綠勾、✗ 紅叉圖示在右側適用性閘門條；
- 跳轉按鈕：白底深綠邊框 + 「→」字樣，hover 時填色 `#2ca02c`。

#### H. 公式同步區（Equation Sync Panel）

底部 LaTeX 公式區，依當前 hover 的分解動態切換：

```
A = CR    →    A = ∑_{p=1}^{r} c_p r^*_p
```

**hover 時可拆解高亮：** $\mathbf{c}_p$（綠閃 200ms）、$\mathbf{r}^*_p$（粉紅閃 200ms），與右側形狀視覺化同步。

#### I. 邊界條件與防呆

- **退化情況：** 用戶輸入 $r > \min(m, n)$ 自動 clip 並提示「rank 上限 = $\min(m, n)$」；
- **不適用分解的處理：** 灰階占位 + tooltip 「對稱不滿足 / 非方陣 / row exchange needed」說明原因，不是直接隱藏（教學上要看到「為什麼不能」）；
- **跳轉按鈕的狀態管理：** 點擊後保留當前矩陣資料；返回時自動恢復先前的選擇狀態。

#### J. 教學節奏建議

- **第 1 階段（0–1 分鐘）：** 用戶看預設「對稱方陣」，全 5 ✓，建立「最特殊的矩陣 = 最多分解」直覺；
- **第 2 階段（1–3 分鐘）：** 切「任意長方矩陣」，看到 LU/QΛQᵀ 變灰，引發「為什麼？」思考；
- **第 3 階段（3–5 分鐘）：** 切「退化 rank 2」，看到 QR 也變灰（若 $m < n$ 或退化），只剩 CR 和 SVD；建立「萬能分解」反射弧；
- **第 4 階段（5–10 分鐘）：** 點各個分解的「→」按鈕，跳轉到 ch04 / ch05 的母模板動畫看細節。

#### K. 變化版本（Variation）

- **「對比模式」：** 同時開啟兩個分解（如 QΛQᵀ + UΣVᵀ），左右對照三明治形狀差異（對稱用同色 / 非對稱用雙色）；
- **「時間切換模式」：** 自動每 3 秒切下一個矩陣類型，5 個分解的適用性閘門呈現動態勾叉變化，類似教學影片自動播放。

#### L. 為何不直接做秩 1 累加動畫（採 pointer 策略的理由）

- **不重複實作工時：** ch04 VizScript-02 已實作 (MM4) 累加動畫 + Mona Lisa SVD demo，本章 5 個分解共用此母模板，pointer 即可重用；
- **概念定位差異：** 本章 ch06a 是「**比較 5 個分解的差異**」，焦點是「形狀指紋」而非「累加細節」；累加細節在母模板看，效果更好；
- **S12+ 工時估算：** 若不採 pointer 策略，本劇本需重做 5 套秩 1 累加動畫（5 × 0.5 session = 2.5 session）；採 pointer 後只需 1 套畫面框架（1.5 session），節省 1 session 工時。

#### M. 驗收條件（Acceptance Criteria）

- 用戶切換 5 種矩陣類型，5 個分解的適用性閘門即時更新（< 100ms 響應）；
- 點任一「→」按鈕，能正確跳轉並帶當前矩陣資料；
- 5 個分解的數值面板與形狀視覺化同步（拉桿改秩，CR/SVD 的綠塊個數與藍點個數同步變化）；
- 「對稱半正定」demo 中，QΛQᵀ 與 UΣVᵀ 的數值應完全一致（$\lambda_p = \sigma_p$、$Q = U = V$），驗證 §6.4 / §6.5 的特例關係；
- 視覺輸出與 `5-Factorizations.png` 的 5 行佈局完全吻合（同樣的綠 / 粉紅 / 藍配色 + 三明治結構）。

---

## 章末延伸

- **後續章節連結：**
  - [→ ch06b-CR.md](ch06b-CR.md)（§6.1 $A=CR$ — 列秩 = 行秩，第一個分解，建立「分解就是因數分解」直覺）
  - [→ ch06c-LU.md](ch06c-LU.md)（§6.2 $A=LU$ — Gaussian 消去法的矩陣化）
  - [→ ch06d-QR.md](ch06d-QR.md)（§6.3 $A=QR$ — Gram–Schmidt 正交化）
  - [→ ch06e-QLQ.md](ch06e-QLQ.md)（§6.4 $S=Q\Lambda Q^{\mathrm{T}}$ — 對稱譜分解，連通 §5 (P3)）
  - [→ ch06f-USV.md](ch06f-USV.md)（§6.5 $A=U\Sigma V^{\mathrm{T}}$ — SVD，分解之王，連通 §5 (P4)）

- **前置章節傳承：**
  - [← ch04-mat-mat.md](ch04-mat-mat.md) §4 (MM4) 視角是本章 5 大分解的母模板（秩 1 之和的共同骨架）；
  - [← ch05-patterns.md](ch05-patterns.md) §5 (P1)/(P2) 是 CR/LU/QR 的視覺前奏，(P3)/(P4) 是 QΛQᵀ/UΣVᵀ 的視覺前奏。

- **延伸閱讀：**
  - Gilbert Strang《Linear Algebra for Everyone》第 6 章（5 個分解的詳細推導 + 應用 — PCA、最小二乘、低秩近似）；
  - Trefethen & Bau《Numerical Linear Algebra》Lecture 4–5（QR / SVD 數值穩定算法）；
  - 附錄 `Map_of_Eigenvalues_5.7.png`（5.7 版特徵值地圖，把 §6.4 / §6.5 的位置標出來）；
  - 附錄 `World_of_Matrices.png`（矩陣世界地圖，5 大分解就是這個地圖的「主要道路」）。

---

## 來源對照

- **原書英文版：** `The-Art-of-Linear-Algebra.tex` § The Five Factorizations of a Matrix（en.md line 205–254 為總覽段；§6.1–§6.5 自 256 起）/ `The-Art-of-Linear-Algebra.pdf` p.7–p.8 表 1
- **原書簡中版：** `The-Art-of-Linear-Algebra-zh-CN.tex` § 矩阵的五种分解（zh.md line 197–246 為總覽段）
- **作者：** Kenji Hiranabe（《Linear Algebra for Everyone》Gilbert Strang 著的圖解筆記）
- **原 repo：** https://github.com/junoback/The-Art-of-Linear-Algebra
- **授權：** Apache 2.0

---

> **撰寫者註（S07）：** 本章是 §6 的開門總覽，刻意短（~400 行）+ 單一 VizMark + 採「Tier 1 + pointer」策略。後續 §6.1–§6.5 五章各自詳述一個分解，每章的「(MM4) 秩 1 累加」demo 都 pointer 到 [ch04 VizScript-02](ch04-mat-mat.md#vizscript-02)、「三明治」demo（QΛQᵀ / UΣVᵀ）都 pointer 到 [ch05 VizScript-02/03](ch05-patterns.md#vizscript-02)。本策略讓 §6 五章合計可節省 ~3 session 的視覺化重做工時（S06 SOP §2.6 補強驗證）。
