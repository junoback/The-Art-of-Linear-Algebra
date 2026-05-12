# 附錄 D：背後觀念 Q&A — 為什麼運算規則長這樣？

> **附錄定位：** 全書每個運算規則 / 定理 / 矩陣分解都不是憑空的數學遊戲，而是**為了解決特定問題量身打造的設計**。本附錄用 Q&A 形式集中回答「**這條規則為什麼長這樣？**」這類動機問題，補完主章「**怎麼算**」之外的「**為什麼這樣算**」維度。
>
> **3-layer 框架：** 每條 Q&A 採固定三層結構：
>
> 1. **① 歷史脈絡** — 這條規則何時、由誰、為了什麼問題而生
> 2. **② 設計過程還原** — 從問題出發逆向推導出規則本身（含完整代數推導 + 小例題）
> 3. **③ 概念昇華** — 一句話收尾，把規則昇華為更高階的概念
>
> **使用建議：** 在主章遇到 `💡 背後觀念` callout 時點連結跳來本附錄看詳盡版；或從頭到尾連讀本附錄當作「全書動機導讀」。
>
> **編寫進度：** S12（規劃 + Foreword~§3）→ S13（§4~§5）→ S14（§6 五大分解）→ S15（附錄 + 整合收尾）；全書 22 條 Q&A，目前進度見下方目錄表。

---

## 目錄與進度

| Q# | 標題 | 對應主章 | 狀態 |
|---|---|---|---|
| [Q01](#q01) | 為什麼線性代數要從「圖解」開始學？ | front-foreword | ✅ 已完成（S12） |
| [Q02](#q02) | 矩陣為什麼存在？「把表格看成單一物件」是什麼躍進？ | §1 | ✅ 已完成（S12） |
| [Q03](#q03) | 為什麼同一個矩陣要看成 4 種視角？ | §1 | ✅ 已完成（S12） |
| [Q04](#q04) | 點積為什麼是「分量相乘再相加」？ | §2 | ✅ 已完成（S12） |
| [Q05](#q05) | 外積為什麼是「列 × 行 = 秩 1 矩陣」？ | §2 | ✅ 已完成（S12） |
| [Q06](#q06) | $A\mathbf{x}$ 為什麼這樣定義？ | §3 | ✅ 已完成（S12） |
| [Q07](#q07) | 為什麼要有 2 個視角（點積 + 線性組合）？ | §3 | ✅ 已完成（S12） |
| [Q08](#q08) | 四個基本子空間為什麼會自然冒出？ | §3 | ✅ 已完成（S12） |
| **Q09** | **矩陣乘法為什麼是「行乘列」？** | **§4** | **✅ 已完成（S12 PoC）** |
| Q10 | 為什麼乘法不可交換 $AB \ne BA$？ | §4 | 🚧 規劃中 |
| Q11 | 對角矩陣 $D$ 為什麼這麼特別？ | §5 | 🚧 規劃中 |
| Q12 | (P3) 動態系統為什麼能用特徵值預測長期？ | §5 | 🚧 規劃中 |
| Q13 | (P4) 三明治 $A = X\Lambda X^{-1}$ 為什麼是線代核心？ | §5 | 🚧 規劃中 |
| Q14 | 為什麼要把矩陣「分解」？ | §6 | 🚧 規劃中 |
| Q15 | A=CR 為什麼成立？「列秩 = 行秩」怎麼自然冒出？ | §6.1 | 🚧 規劃中 |
| Q16 | A=LU 為什麼存在？高斯消去法為什麼能壓縮成兩三角矩陣？ | §6.2 | 🚧 規劃中 |
| Q17 | A=QR 為什麼需要正交化？Gram-Schmidt 從哪冒出來？ | §6.3 | 🚧 規劃中 |
| Q18 | $S=Q\Lambda Q^{\mathrm{T}}$ 為什麼對稱矩陣特徵向量自動正交？ | §6.4 | 🚧 規劃中 |
| Q19 | $A=U\Sigma V^{\mathrm{T}}$ SVD 為什麼對任何矩陣都存在？ | §6.5 | 🚧 規劃中 |
| Q20 | 特徵值的「地圖」為什麼能畫得出來？ | Appendix A | 🚧 規劃中 |
| Q21 | Matrix World 為什麼是「同心橢圓繼承樹」而非「樹狀」？ | Appendix B | 🚧 規劃中 |
| Q22 | 「解 $A\mathbf{x}=\mathbf{b}$」為什麼是線代的核心問題？ | Appendix C | 🚧 規劃中 |

> **術語提醒：** 本附錄沿用全書 A 派慣例 — **column = 列（直立、綠色）、row = 行（橫躺、粉紅色）**。歷史出處引用若採 B 派（列 = Row、行 = Column）時會在註解標明，避免混淆。

---

## Q01：為什麼線性代數要從「圖解」開始學？ {#q01}

> **觸發問題：** 傳統線性代數教科書從「行列式 → 矩陣運算 → 反矩陣公式 → 特徵值」一路符號推到底，學生算得出答案卻看不到結構。為什麼 Strang 和 Hiranabe 都主張**反轉教學順序、圖解優先**？這個策略真的有效嗎？
>
> **對應主章：** [front-foreword](front-foreword.md)
>
> **3-layer 涵蓋：** ① 歷史 / ③ 昇華

### ① 歷史脈絡：Strang 五十年教學的反思

線性代數教學的「反轉」不是一次性發生的事件，而是 Gilbert Strang 在 MIT 教線代五十年中**漸進完成的革命**：

- **1976 年第 1 版《Linear Algebra and Its Applications》** — Strang 第一本教科書，採傳統「行列式 → 求逆 → 特徵值」順序，但他在後續多版中逐漸把「**子空間 + 線性組合 + 投影**」推前。
- **2003 年 MIT OCW 18.06「Linear Algebra」上線** — 史上最熱門 OCW 課之一，**Strang 在第 1 堂課的第 1 個圖就畫「行視角 vs 列視角」雙視角**，直接顛覆傳統。他多次在訪談中說：「I want students to **see** linear algebra, not just compute it.」
- **2020 年《Linear Algebra for Everyone》（LAFE）** — Strang 75 歲時親自寫的「**反傳統教科書**」，全書以圖優先、符號為輔；第 1 章直接從「**矩陣 $A$ 的列空間**」切入，行列式被推到第 5 章才出現（傳統書通常在第 2 章）。
- **2021 年 Hiranabe《The Art of Linear Algebra》** — Kenji Hiranabe（日本敏捷顧問，非數學家）讀完 LAFE 後做的視覺筆記，把「圖解優先」推到極致 — 每個概念都有圖、每個運算都有 4 種視角、5 大分解都有彩色圖示。本書即 Hiranabe 視覺筆記的中文化與互動化擴展。

### ③ 概念昇華：圖解優先 vs 符號優先

線性代數的對象**本質是幾何 / 結構**（向量空間、子空間、變換），不是數值或元素 — 但傳統教學讓學生淹沒在「行列式 4 階展開」「逆矩陣的伴隨矩陣公式」這類**計算迷霧**裡。等學生終於通過考試，已經錯過了「**矩陣是動詞**」的核心直覺。

#### 符號優先 vs 圖解優先的對比

| 概念 | 符號優先 | 圖解優先 |
|---|---|---|
| 矩陣乘法 | $c_{ij} = \sum_k a_{ik} b_{kj}$ 機械記憶 | 「先 $B$ 變換、再 $A$ 變換」函數合成（見 [Q09](#q09)） |
| 列秩 = 行秩 | 用初等列變換 + 初等行變換各自化簡，比較主軸數量 | $A=CR$ 分解的構造性證明 — 兩個視角看同一個 $r$（見 [Q15](#q15)） |
| 特徵值 | 解 $\det(A - \lambda I) = 0$ | 「找變換的不變方向 + 沿該方向的縮放倍數」 |
| SVD | $U^{\mathrm{T}} A V = \Sigma$ 推導 | 「對任意矩陣，都能找到正交輸入基底 → 縮放 → 正交輸出基底」（見 [Q19](#q19)） |

#### Strang 的核心觀察

**圖解優先 = 先看到結構、後補符號 = 學生能用幾何直覺判斷答案的合理性**，而不只是「公式算出來就信」。

但**圖解優先 ≠ 不要符號**。本書（與 LAFE、Hiranabe）的順序都是「**圖 → 直覺 → 符號 → 推導 → 互動驗證**」5 階。Hiranabe 在原書 Foreword 引 Confucius：

> "I hear and I forget. I see and I remember. I do and I understand."
> （我聽，我忘記；我看，我記得；我做，我懂。）

**本書再加一階「互動 = do」**，把學習推到「動手做 → 真正懂」 — 這就是全書 36 個 VizScript 的設計目的（見 [VIZ-CATALOG.md](VIZ-CATALOG.md)）。

### 延伸閱讀

**本書相關章節：**
- [Foreword](front-foreword.md) — 三大主題導讀 + 1920–2026 緣起時間線
- [§1 ch01 Figure 1.1 四視角](ch01-viewing-matrix.md#figure-11-矩陣的四種視角viewing-a-matrix-in-4-ways) — 圖解優先的第一個示範
- [VIZ-CATALOG.md](VIZ-CATALOG.md) — 全書 36 個互動視覺化劇本索引

**現代教科書 + 學術資源：**
- Strang, G. (1976), *Linear Algebra and Its Applications* (1st ed.), Academic Press — Strang 第一本教科書
- Strang, G. (2003+), MIT OCW 18.06 *Linear Algebra* — 史上最熱門 OCW 課之一
- **Strang, G. (2020), *Linear Algebra for Everyone*, Wellesley–Cambridge Press** — 反傳統，圖解優先
- Hiranabe, K. (2021+), *The Art of Linear Algebra* (GitHub) — 視覺筆記版（本書翻譯擴展之源）

---

## Q02：矩陣為什麼存在？「把表格看成單一物件」是什麼躍進？ {#q02}

> **觸發問題：** 矩陣本質就是「把一群數字排成方陣」 — 但這只是**記法**，為什麼數學家要把這個記法**獨立為代數物件**（可以加、可以乘、可以求逆、可以分解）？這個躍進到底有多重要？
>
> **對應主章：** [§1 ch01 章節摘要](ch01-viewing-matrix.md#章節摘要)
>
> **3-layer 涵蓋：** ① 歷史 / ③ 昇華

### ① 歷史脈絡：從「記法」到「物件」的躍進

矩陣的歷史是「**記法越來越成熟、物件性越來越明確**」的緩慢演進：

| 時間 | 人物 | 貢獻 | 矩陣的地位 |
|---|---|---|---|
| 西元前 1 世紀 | 《九章算術》 | 用方陣記載聯立方程係數，行間消元解三元一次 | 記法（運算的工作區）|
| 1683 | 關孝和（日本） | 行列式概念雛形（《解伏題之法》），解線性方程 | 記法 + 衍生量 |
| 1693 | Leibniz | 行列式系統化（私人通信） | 記法 + 衍生量 |
| 1750 | Cramer | Cramer 法則 — 用行列式系統地解 $n$ 元 $n$ 元方程 | 記法 |
| **1850** | **Sylvester** | 命名 "Matrix"（拉丁文「子宮 / 母體」），但仍視為記法 | 記法（已命名） |
| **1858** | **Cayley** | *A Memoir on the Theory of Matrices* — **首次把矩陣獨立為代數物件**：定義 $+, \times, A^{-1}, I, O, p(A)$ | **代數物件** |
| 1878 | Frobenius | 矩陣的標準形、不變量、極小多項式 | 抽象代數結構 |

### ② 設計過程還原：物件化解決了什麼問題？

**沒有矩陣（純方程組視角）：** 解 3 個方程要展開 3 行；解 100 個方程要展開 100 行；想「合成兩組方程」要逐項代入展開（見 [Q09](#q09) 的代入過程）。

**有矩陣後：** $A\mathbf{x} = \mathbf{b}$、$\mathbf{y} = AB\mathbf{x}$ 兩個符號就濃縮了**任意維度**的方程組與變換合成。

#### 例：「100 個未知數 100 個方程」的問題

| 視角 | 書寫量 | 思考單位 |
|---|---|---|
| 方程組視角 | $100 \times 100 = 10000$ 個係數寫成 100 行方程 | 個別係數 $a_{ij}$ |
| 矩陣物件視角 | 一個符號 $A$ + 一個方程 $A\mathbf{x} = \mathbf{b}$ | 整個 $A$ 作為物件 |

#### 物件化的代數紅利

一旦把 $A$ 當物件，我們就可以：

1. **加法：** $A + B$（兩組變換的疊加）
2. **乘法：** $AB$（兩組變換的合成，見 [Q09](#q09)）
3. **逆：** $A^{-1}$（變換的撤銷）
4. **分解：** $A = LU = QR = U\Sigma V^{\mathrm{T}}$（把複雜變換拆成簡單成分）
5. **函數：** $p(A) = A^2 + 3A + I$（多項式作用於矩陣）
6. **譜：** 特徵值 / 奇異值（變換的「指紋」）

**這 6 條每一條都是線性代數的核心章節**。沒有物件化，這 6 條都不存在 — 我們只會困在「展開每個係數」的迷霧中。

### ③ 概念昇華：抽象階層提升的數學設計

「矩陣物件化」是數學中「**抽象階層提升（abstraction lifting）**」的典範。從原子到複合物的階層：

```
標量 (scalar)    →   向量 (vector)    →   矩陣 (matrix)     →   張量 (tensor)
單一數字 a            一組有序數字 v        一張表格 A             高維資料塊 T
1×1                   n×1                   m×n                    d₁×d₂×...×dₖ
(無結構)              (方向 + 長度)         (變換 + 子空間)        (多模態資料)
```

每一階都把上一階「**封裝（encapsulate）**」為新單位，再對新單位定義新運算。這個設計原則跟物件導向程式設計（OOP）的「類別封裝實例」、跟物理學的「粒子封裝為分子封裝為材料」、跟生物學的「細胞封裝為組織封裝為器官」**完全相同** — 都是「**讓複雜性被抽象階層藏起來**」這條普世法則。

**矩陣是這個普世法則在 19 世紀對線性方程組的應用。** Cayley 1858 的躍進不只是命名一個新物件，而是宣告「**線性方程組可以被當作單一物件來操作**」 — 從此以後，數學家、物理學家、工程師、資料科學家**不必再面對個別係數**，而是面對矩陣這個整體。這個躍進是現代計算科學、量子力學、機器學習能夠成立的**前提條件**。

### 延伸閱讀

**本書相關章節：**
- [§1 ch01 章節摘要](ch01-viewing-matrix.md#章節摘要) — 矩陣的 4 種視角（元素 / 列 / 行 / 子矩陣）皆建立於物件化之上
- [Q03](#q03) — 為什麼物件化的矩陣要有 4 種視角
- [Q09](#q09) — Cayley 1858 矩陣乘法的設計過程

**歷史原典：**
- 《九章算術》方程章（西元前 1 世紀，劉徽 263 年注本）
- 關孝和 (1683)《解伏題之法》— 日本獨立發明行列式
- **Cayley, A. (1858), *A Memoir on the Theory of Matrices*, Philosophical Transactions of the Royal Society of London, 148, 17–37** — 矩陣物件化的標誌性論文
- Frobenius, F. G. (1878), *Über lineare Substitutionen und bilineare Formen*, Journal für die reine und angewandte Mathematik — 矩陣的標準形與不變量

---

## Q03：為什麼同一個矩陣要看成 4 種視角？ {#q03}

> **觸發問題：** 矩陣 $A$ 就是一張固定的方陣，為什麼本書 §1 開門就強調「**同一個 $A$ 可以從 4 個視角看**」（元素 $a_{ij}$ / 直立列 $\mathbf{a}_j$ / 橫躺行 $\mathbf{a}^*_i$ / 子矩陣 block）？這 4 個視角是並列的還是有層次的？為什麼不能只用一個視角從頭講到尾？
>
> **對應主章：** [§1 ch01 數學要點](ch01-viewing-matrix.md#數學要點)
>
> **3-layer 涵蓋：** ② 推導 / ③ 昇華

### ② 設計過程：4 個視角各自服務什麼問題？

矩陣的 4 個視角不是並列裝飾，**每個視角都是為了讓某類問題「看起來最自然」而設計**：

| 視角 | 切法 | 最自然的問題 | 後續章節主要應用 |
|---|---|---|---|
| **V1 元素 $a_{ij}$** | 拆成 $m \times n$ 個獨立數字 | 「**計算**」 — 點積規則 (MM1)、程式實作 (for loop)、運算量分析 ($O(mnk)$) | §4 (MM1)、計算複雜度 |
| **V2 直立列 $\mathbf{a}_j$** | 拆成 $n$ 個 $\mathbb{R}^m$ 向量 | 「**列空間 / 線性組合**」 — $A\mathbf{x}$ 是 $A$ 各列的線性組合 (Mv2)；$\mathbf{C}(A)$ 是 $A$ 的列張成 | §3 (Mv2)、§4 (MM2)、§6.1 CR、§6.5 SVD |
| **V3 橫躺行 $\mathbf{a}^*_i$** | 拆成 $m$ 個 $\mathbb{R}^{1 \times n}$ 向量 | 「**行空間 / 方程組**」 — $A\mathbf{x} = \mathbf{b}$ 的每個元素是 $A$ 一橫躺行與 $\mathbf{x}$ 的點積；行階梯形 | §3 (Mv1)、§4 (MM3)、§6.2 LU、4 子空間 |
| **V4 子矩陣 block** | 拆成 $\begin{bmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{bmatrix}$ 等結構 | 「**分解 / Schur complement / 平行運算**」 — Schur complement 解 block 系統、block-wise 乘法、大型矩陣分散式計算 | §6 SVD 雙正交基底（U / V）、Schur 分解、矩陣計算的快取友善設計 |

#### 同一問題的不同視角效率天差地遠

**例 1：判斷 $\mathbf{b}$ 是否在 $A$ 的列空間裡（即 $A\mathbf{x} = \mathbf{b}$ 是否有解）**

- **V1 元素視角：** 機械求解 $\mathbf{x}$，看有沒有解 → 高斯消去法跑完才能判斷 → $O(n^3)$
- **V2 列視角：** 問「$\mathbf{b}$ 能不能寫成 $A$ 直立列的線性組合？」→ 從幾何直覺一秒判斷（$\mathbf{b}$ 在 $\mathbf{C}(A)$ 平面上嗎？）→ 概念上 $O(1)$

**例 2：計算秩 $r = \text{rank}(A)$**

- **V1 元素視角：** 跑高斯消去法數主軸 → 機械
- **V2 列視角：** 數 $A$ 的線性獨立直立列 → 列秩
- **V3 行視角：** 數 $A$ 的線性獨立橫躺行 → 行秩
- **結論：** V2 = V3（列秩 = 行秩，[Q15](#q15) 詳述）— **兩個視角看到同一個量**，這個現象本身就是線代最深刻的結果之一（Strang 4 大基本定理之首）

**例 3：矩陣乘法 $AB$ 的 4 種讀法**

- **V1：** (MM1) 點積（每個元素獨立算）
- **V2：** (MM2) 列線性組合（$C$ 的每列是 $A$ 列的線組合）
- **V3：** (MM3) 行線性組合（$C$ 的每行是 $B$ 行的線組合）
- **V4：** (MM4) 子矩陣 block，或極端化為**秩 1 之和**（$AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$）

**4 個視角看 $AB$ 都對，但只有 (MM4) 視角能直接通往 SVD 與低秩近似**（見 [§4 ch04 (MM4)](ch04-mat-mat.md#mm4-外積之和方式sum-of-outer-products--rank-1-decomposition-way--本章核心) 與 [Q09 §③](#q09)）。

### ③ 概念昇華：問題決定視角，視角不是個人偏好

「**4 個視角是並列的、可互換的**」是初學者的誤解。實際上：

> **視角不是個人偏好，是「問題決定視角」的數學設計原則。**

#### 三角形面積公式類比

**同一個三角形，從不同的邊出發看，會得到不同的面積公式**：

- 基 × 高 / 2（基底視角）
- 海倫公式 $\sqrt{s(s-a)(s-b)(s-c)}$（三邊視角）
- $\frac{1}{2} ab \sin C$（雙邊夾角視角）
- $\dfrac{abc}{4R}$（外接圓半徑視角）

**公式不同，三角形是同一個。** 哪個公式最好用，**取決於你手上有什麼資訊** — 若已知三邊用海倫；若已知兩邊夾角用 $\frac{1}{2}ab\sin C$；若已知外接圓用 $abc/4R$。

#### 矩陣 4 視角同理

| 手上的資訊 / 任務 | 最自然的視角 |
|---|---|
| 寫 BLAS 矩陣乘法 / for-loop 實作 | V1 元素 |
| 解 $A\mathbf{x} = \mathbf{b}$ | V3 行（每行 = 一個方程） |
| 做主成分分析（PCA）/ 機器學習 sample matrix | V2 列（每列 = 一個 sample） |
| 大規模平行運算 / 分散式儲存 | V4 block |
| 設計矩陣分解（CR / SVD） | V2 列為主 + V3 行為輔 |

**4 個視角的等價性 = 線性代數「所有結果無論從哪個視角推都會殊途同歸」的優美性質**，也是 §6 五大分解全部都同時提供「列視角」與「行視角」兩讀法的根本原因（見 §6.1 CR 對偶兩圖 / §6.4 EVD 對偶 / §6.5 SVD 雙正交基底）。

### 延伸閱讀

**本書相關章節：**
- [§1 ch01 數學要點](ch01-viewing-matrix.md#數學要點) — 4 視角的正式定義
- [§1 VizScript-01 四視角切換動畫](ch01-viewing-matrix.md#vizscript-01) — 動態看視角等價
- [§3 ch03 (Mv1)/(Mv2)](ch03-mat-vec.md#mv1-點積方式dot-product-way) — V3 / V2 視角的 $A\mathbf{x}$ 應用
- [§4 ch04 (MM1)–(MM4)](ch04-mat-mat.md#mm1-點積方式element-wise-dot-product-way) — 4 視角的乘法擴展
- [Q07](#q07) — 為什麼 $A\mathbf{x}$ 要有 2 視角

**現代教科書：**
- Strang, G. (2020), *Linear Algebra for Everyone*, §1.1 "The Column Picture" — 強調列視角優於行視角

---

## Q04：點積為什麼是「分量相乘再相加」？ {#q04}

> **觸發問題：** 兩個向量 $\mathbf{u}, \mathbf{v} \in \mathbb{R}^n$ 的點積定義為 $\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i$ — 把對應分量相乘再加總。**為什麼是「相乘再相加」這個組合**？為什麼不是「相減取平方再加總」（那是距離）、不是「相乘再相乘」、不是別的形式？這個定義是從什麼動機推出來的？
>
> **對應主章：** [§2 ch02 章節摘要](ch02-vec-vec.md#章節摘要)
>
> **3-layer 涵蓋：** ① 歷史 / ② 推導 / ③ 昇華

### ① 歷史脈絡：點積的三個源頭

點積不是某一個人發明的，而是 19 世紀末**三條獨立的思路**最後**殊途同歸**：

- **1773 Lagrange** 在《Mécanique Analytique》中使用兩向量「相乘為標量」的運算分析力學
- **1844 Grassmann**《Ausdehnungslehre》（《擴張論》）引入「內積（inner product）」與「外積（outer product）」並列的代數結構，但不被當代數學界重視
- **1881 Gibbs** 在 *Elements of Vector Analysis* 中系統化向量分析，**命名 "dot product"** 並推廣至物理學
- **20 世紀初** Hilbert / von Neumann 將點積抽象化為「**內積空間（inner product space）**」公理體系，成為泛函分析基石

### ② 設計過程還原：三個動機殊途同歸

點積的「分量相乘再相加」公式可以從**三個截然不同的動機**獨立推出，最後得到同一個式子 — 這正是它「**自然 / 必然**」的鐵證。

#### 動機 A：幾何（投影 + 餘弦定理）

**目標：** 定義一個運算「測量兩向量的對齊程度」。直覺上希望：

- 兩向量**同向**時 → 運算結果**最大**
- 兩向量**垂直**時 → 運算結果為 **0**
- 兩向量**反向**時 → 運算結果**最負**

最自然的數學物件是 $\|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$（$\theta$ = 夾角）— 滿足三條件。**但這個式子怎麼用分量算出來？**

**用餘弦定理推導：** 三角形三邊長為 $\|\mathbf{u}\|$、$\|\mathbf{v}\|$、$\|\mathbf{u} - \mathbf{v}\|$，夾角為 $\theta$：

$$
\|\mathbf{u} - \mathbf{v}\|^2 \;=\; \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 - 2 \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta
$$

左邊用分量展開：

$$
\|\mathbf{u} - \mathbf{v}\|^2 = \sum_i (u_i - v_i)^2 = \sum_i u_i^2 - 2 \sum_i u_i v_i + \sum_i v_i^2 = \|\mathbf{u}\|^2 - 2 \sum_i u_i v_i + \|\mathbf{v}\|^2
$$

兩式相減消去 $\|\mathbf{u}\|^2 + \|\mathbf{v}\|^2$：

$$
\boxed{
\sum_i u_i v_i \;=\; \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta \;=\; \mathbf{u} \cdot \mathbf{v}
}
$$

**結論：** 「**分量相乘再相加**」這個公式**等於**「**兩向量長度乘積乘以夾角餘弦**」 — 兩者完全等價。**幾何意義（對齊程度）強制了代數形式（相乘再相加）。**

#### 動機 B：物理（功 = 力 · 位移）

物理中「**功（work）**」的定義：當力 $\mathbf{F}$ 作用於物體並使其產生位移 $\mathbf{d}$ 時，做功為：

$$
W = \|\mathbf{F}\| \|\mathbf{d}\| \cos\theta
$$

直覺：力與位移同向時做最大功、垂直時做零功、反向時做負功。

**分量計算：** 把力和位移分解到 $x, y, z$ 軸：$\mathbf{F} = (F_x, F_y, F_z)$、$\mathbf{d} = (d_x, d_y, d_z)$。在 $x$ 軸方向，力做功為 $F_x \cdot d_x$；同理 $y$ 軸 $F_y d_y$、$z$ 軸 $F_z d_z$。總功 = **各軸做功相加**：

$$
W = F_x d_x + F_y d_y + F_z d_z = \mathbf{F} \cdot \mathbf{d}
$$

**結論：** 物理上「**功是純量**（不是向量）」的事實 + 「**各軸獨立做功再加總**」的可加性，**自然強制**了點積的「分量相乘再相加」形式。

#### 動機 C：代數（內積空間公理）

抽象地定義「**內積**」為滿足下列 4 公理的二元運算 $\langle \cdot, \cdot \rangle : V \times V \to \mathbb{R}$：

1. **對稱性：** $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$
2. **第一變量線性：** $\langle a\mathbf{u} + b\mathbf{w}, \mathbf{v} \rangle = a \langle \mathbf{u}, \mathbf{v} \rangle + b \langle \mathbf{w}, \mathbf{v} \rangle$
3. **正定性：** $\langle \mathbf{u}, \mathbf{u} \rangle \ge 0$，且 $= 0 \iff \mathbf{u} = \mathbf{0}$
4. **共軛對稱性（複數情形）：** $\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$（實數情形退化為對稱性）

**定理：** 在 $\mathbb{R}^n$ 的**標準基底**下，唯一同時滿足這 4 公理且最簡單的形式是 $\sum_i u_i v_i$。

**證明大意：** 由對稱性 + 雙線性，$\langle \mathbf{u}, \mathbf{v} \rangle$ 完全由「基底向量之間的內積矩陣 $G_{ij} = \langle \mathbf{e}_i, \mathbf{e}_j \rangle$」決定。若取「最簡單」的情況 $G_{ij} = \delta_{ij}$（標準基底正交），即 $\langle \mathbf{e}_i, \mathbf{e}_j \rangle = 1$ if $i=j$ else $0$，則：

$$
\langle \mathbf{u}, \mathbf{v} \rangle = \sum_{i,j} u_i v_j \langle \mathbf{e}_i, \mathbf{e}_j \rangle = \sum_{i,j} u_i v_j \delta_{ij} = \sum_i u_i v_i
$$

**結論：** 點積是「在標準基底正交假設下，最簡單的內積實現」 — 由公理 + 簡單性自然推出。

#### 三個動機殊途同歸

| 動機 | 出發點 | 推出的公式 |
|---|---|---|
| 幾何 | 餘弦定理 + 投影 | $\sum_i u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$ |
| 物理 | 功 = 各軸獨立做功之和 | $\sum_i F_i d_i$ |
| 代數 | 內積公理 + 標準基底正交 | $\sum_i u_i v_i$ |

**三條路通向同一個公式**。這就是點積為什麼**不是憑空定義**，而是**幾何、物理、代數三重必然性的交點**。

### ③ 概念昇華：對齊度量是線代半壁江山

點積的本質是「**測量兩向量的對齊程度**」 — 從這個簡單度量出發，線性代數的**半壁江山**由此展開：

| 衍生概念 | 點積版定義 |
|---|---|
| **長度（norm）** | $\|\mathbf{u}\| = \sqrt{\mathbf{u} \cdot \mathbf{u}}$ |
| **單位向量** | $\hat{\mathbf{u}} = \mathbf{u} / \|\mathbf{u}\|$ |
| **正交（perpendicular）** | $\mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0$ |
| **夾角** | $\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$ |
| **投影** | $\text{proj}_{\mathbf{v}} \mathbf{u} = \frac{\mathbf{u} \cdot \mathbf{v}}{\mathbf{v} \cdot \mathbf{v}} \mathbf{v}$ |
| **距離** | $d(\mathbf{u}, \mathbf{v}) = \|\mathbf{u} - \mathbf{v}\| = \sqrt{(\mathbf{u}-\mathbf{v}) \cdot (\mathbf{u}-\mathbf{v})}$ |
| **Cauchy–Schwarz 不等式** | $|\mathbf{u} \cdot \mathbf{v}| \le \|\mathbf{u}\| \|\mathbf{v}\|$ |
| **Gram–Schmidt 正交化** | 迭代「減去投影」直到所有方向正交 |
| **QR 分解** | 列空間的正交化結果（[§6.3](ch06d-QR.md)，[Q17](#q17)） |
| **譜定理（對稱矩陣）** | 對稱矩陣的特徵向量自動兩兩正交（[§6.4](ch06e-QLQ.md)，[Q18](#q18)） |
| **SVD** | 兩個正交基底之間的對角變換（[§6.5](ch06f-USV.md)，[Q19](#q19)） |
| **最小平方法** | 投影到列空間（殘差與列空間正交） |

**所以點積不是線性代數的「一個工具」，是「一個基本句法」。** 整本書 §2 → §3 → §4 → §6 中所有運算的展開，本質上都是「**反覆使用點積**」的演化。

### 延伸閱讀

**本書相關章節：**
- [§2 ch02 (v1) 點積方式](ch02-vec-vec.md#v1-點積方式dot-product-way) — 點積的正式定義 + 4 視角
- [§2 ch02 VizScript-01](ch02-vec-vec.md#vizscript-01) — 點積幾何互動
- [§6.3 ch06d QR 分解](ch06d-QR.md) — Gram–Schmidt 從點積出發
- [§6.4 ch06e EVD](ch06e-QLQ.md) — 對稱矩陣特徵向量正交（[Q18](#q18)）
- [Q05](#q05) — 外積：點積的鏡像伴侶

**歷史原典：**
- Lagrange, J.-L. (1788), *Mécanique Analytique* — 力學中的向量乘積雛形
- **Grassmann, H. (1844), *Die lineale Ausdehnungslehre* (《線性擴張論》)** — 內積與外積的代數對偶
- **Gibbs, J. W. (1881), *Elements of Vector Analysis*** — "dot product" 命名與系統化

**現代教科書：**
- Strang, G. (2020), *Linear Algebra for Everyone*, §1.1 "The Geometry of Linear Algebra"

---

## Q05：外積為什麼是「列 × 行 = 秩 1 矩陣」？ {#q05}

> **觸發問題：** 點積 $\mathbf{u} \cdot \mathbf{v} = \sum_i u_i v_i$ 把兩個向量壓成**一個標量**；外積 $\mathbf{u} \mathbf{v}^{\mathrm{T}}$ 卻把兩個向量展開成**一個矩陣**。**為什麼同樣是兩個向量相乘，會冒出兩個截然不同的結果？外積這個矩陣為什麼一定是秩 1**？這個運算為什麼如此重要？
>
> **對應主章：** [§2 ch02 (v2) 外積方式](ch02-vec-vec.md#v2-外積方式outer-product-way)
>
> **3-layer 涵蓋：** ② 推導 / ③ 昇華

### ② 設計過程還原：點積與外積的對偶設計

考慮兩個向量 $\mathbf{u} \in \mathbb{R}^m$、$\mathbf{v} \in \mathbb{R}^n$（可以維度不同）。兩個向量之間，有**兩種根本不同的「相乘」方式**：

| 運算 | 形狀規則 | 元素規則 | 結果形狀 | 結果秩 |
|---|---|---|---|---|
| **點積（內積）** | $\mathbf{u}^{\mathrm{T}} \mathbf{v}$，必須**同維度** | 「**對應分量相乘再相加**」 — 全部壓縮成 1 個數 | $1 \times 1$ 標量 | — |
| **外積** | $\mathbf{u} \mathbf{v}^{\mathrm{T}}$，**維度可不同** | 「**所有分量對對相乘鋪平**」 — 展開成 $m \times n$ 表 | $m \times n$ 矩陣 | $1$（秩 1） |

#### 為什麼一個壓成標量、一個展成矩陣？

從**矩陣乘法**的角度看，兩種運算其實是**同一個矩陣乘法在不同形狀下的特例**：

- **點積：** 視 $\mathbf{u}, \mathbf{v}$ 為 $n \times 1$ 列向量，計算 $\mathbf{u}^{\mathrm{T}} \mathbf{v}$（形狀 $1 \times n$ 乘 $n \times 1$）→ 結果 $1 \times 1$ 標量
- **外積：** 視 $\mathbf{u}$ 為 $m \times 1$、$\mathbf{v}^{\mathrm{T}}$ 為 $1 \times n$，計算 $\mathbf{u} \mathbf{v}^{\mathrm{T}}$（形狀 $m \times 1$ 乘 $1 \times n$）→ 結果 $m \times n$ 矩陣

**矩陣乘法的形狀規則**（$(m \times k)(k \times n) = (m \times n)$，見 [Q09](#q09)）**自動決定**了兩種結果：

- 中間維度 $k$ 大、外圍維度 $m, n$ 小（$= 1, 1$）→ 結果是**標量**（點積）
- 中間維度 $k$ 小（$=1$）、外圍維度 $m, n$ 大 → 結果是**矩陣**（外積）

兩者是「**矩陣乘法的對偶極限**」 — 一個壓到最小、一個展到最大。

#### 為什麼外積矩陣的秩一定是 1？

**定義：** $C = \mathbf{u} \mathbf{v}^{\mathrm{T}}$，元素 $c_{ij} = u_i v_j$。

**直立列觀察：** $C$ 的第 $j$ 直立列為：

$$
\mathbf{c}_j = (u_1 v_j, u_2 v_j, \ldots, u_m v_j)^{\mathrm{T}} = v_j \cdot (u_1, u_2, \ldots, u_m)^{\mathrm{T}} = v_j \cdot \mathbf{u}
$$

**所有直立列都是 $\mathbf{u}$ 的純量倍數！** 列空間 $\mathbf{C}(C) = \text{span}\{\mathbf{u}\}$ 只有一個方向 → **秩 = 1**。

**橫躺行觀察：** 同理 $C$ 的第 $i$ 橫躺行為 $u_i \cdot \mathbf{v}^{\mathrm{T}}$ — 所有橫躺行都是 $\mathbf{v}^{\mathrm{T}}$ 的純量倍數 → 行空間也是一維 → **行秩 = 1 = 列秩**。

#### 小例題

取 $\mathbf{u} = (1, 2, 3)^{\mathrm{T}}$、$\mathbf{v} = (4, 5)^{\mathrm{T}}$：

$$
\mathbf{u} \mathbf{v}^{\mathrm{T}} =
\begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}
\begin{bmatrix} 4 & 5 \end{bmatrix}
=
\begin{bmatrix}
1{\cdot}4 & 1{\cdot}5 \\
2{\cdot}4 & 2{\cdot}5 \\
3{\cdot}4 & 3{\cdot}5
\end{bmatrix}
=
\begin{bmatrix}
4 & 5 \\
8 & 10 \\
12 & 15
\end{bmatrix}
$$

**檢查秩：**
- 直立列：$(4, 8, 12)^{\mathrm{T}} = 4 \mathbf{u}$、$(5, 10, 15)^{\mathrm{T}} = 5 \mathbf{u}$ — 兩列都是 $\mathbf{u}$ 的倍數 → 列空間一維 → 秩 1 ✓
- 橫躺行：$(4, 5) = 1 \cdot \mathbf{v}^{\mathrm{T}}$、$(8, 10) = 2 \cdot \mathbf{v}^{\mathrm{T}}$、$(12, 15) = 3 \cdot \mathbf{v}^{\mathrm{T}}$ — 三行都是 $\mathbf{v}^{\mathrm{T}}$ 的倍數 → 行秩 1 ✓

### ③ 概念昇華：秩 1 矩陣是線代的「原子」

外積的真正威力**不是**這個運算本身，而是它定義出一個**特殊的矩陣家族**：**秩 1 矩陣**。秩 1 矩陣是線性代數的「**原子**」，所有矩陣都可以**由秩 1 矩陣「原子」線性組合而成**。

#### 三大「秩 1 原子之和」結構

| 結構 | 公式 | 詮釋 |
|---|---|---|
| **(MM4) 矩陣乘法** | $AB = \sum_{p=1}^{k} \mathbf{a}_p \mathbf{b}^*_p$ | 任意矩陣乘積 = $k$ 個秩 1 矩陣之和 |
| **CR 分解** | $A = CR = \sum_{p=1}^{r} \mathbf{c}_p \mathbf{r}^*_p$ | 任意矩陣 = $r$ 個秩 1 矩陣之和（$r$ = rank） |
| **SVD（Eckart–Young）** | $A = \sum_{p=1}^{r} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ | 任意矩陣 = $r$ 個「最重要 → 最次要」排序的秩 1 矩陣加權之和 |

**SVD 的視角最深刻：** 截斷前 $k$ 項 $A_k = \sum_{p=1}^{k} \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 是「**$A$ 的最佳秩 $k$ 近似**」（Eckart–Young 定理）— 這就是**低秩近似、影像壓縮（Mona Lisa SVD demo）、PCA、推薦系統、潛在語意分析、attention 機制（QKᵀ 也是外積）**的數學根源。

#### 為什麼秩 1 矩陣特別「簡單」？

秩 1 矩陣 $\mathbf{u}\mathbf{v}^{\mathrm{T}}$ 的所有資訊**只藏在兩個向量** $\mathbf{u} \in \mathbb{R}^m$、$\mathbf{v} \in \mathbb{R}^n$ 裡（$m + n$ 個數），但展開後是一個 $mn$ 元素的矩陣。**壓縮率 $\frac{m+n}{mn}$ 在 $m, n$ 大時極小**，例如 $1000 \times 1000$ 矩陣若是秩 1，只需儲存 2000 個數而非 $10^6$ — 這就是「**低秩 = 高壓縮 = 高效率**」的本源。

> **總結：** 外積定義的不只是一個運算，而是定義了**秩 1 矩陣這個基本原子**。「點積把兩向量壓到 0 維（標量），外積把兩向量展到 2 維（秩 1 矩陣）」是矩陣乘法在兩個極限下的對偶 — 兩者是同一條規則的兩端。**從秩 1 原子之和出發理解矩陣乘法（MM4 視角），是 Strang 在 LAFE 中強調的「矩陣乘法真正核心」（見 [Q09 §③](#q09)），也是現代資料科學的數學基石。**

### 延伸閱讀

**本書相關章節：**
- [§2 ch02 (v2) 外積方式](ch02-vec-vec.md#v2-外積方式outer-product-way) — 外積的正式定義 + 4 視角
- [§2 ch02 VizScript-02](ch02-vec-vec.md#vizscript-02) — 外積秩 1 矩陣的視覺化
- [§4 ch04 (MM4) 外積之和方式](ch04-mat-mat.md#mm4-外積之和方式sum-of-outer-products--rank-1-decomposition-way--本章核心) — 矩陣乘法的「真正核心」視角
- [§4 ch04 VizScript-02 秩 1 累加 + Mona Lisa SVD demo](ch04-mat-mat.md#vizscript-02) — Tier 3 旗艦
- [§6.1 ch06b A=CR](ch06b-CR.md) — 秩 $r$ 個秩 1 矩陣之和的最直觀分解
- [§6.5 ch06f A=UΣVᵀ](ch06f-USV.md) — Eckart–Young 定理 + 4 大應用
- [Q19](#q19) — SVD 為什麼對任何矩陣都存在

**現代教科書：**
- Strang, G. (2020), *Linear Algebra for Everyone*, §1.4 "Matrix Multiplication AB and CR" — 秩 1 之和是矩陣乘法核心
- Strang, G. (2019), *Linear Algebra and Learning from Data*, Ch.1 — Mona Lisa SVD 原型

---

## Q06：$A\mathbf{x}$ 為什麼這樣定義？ {#q06}

> **觸發問題：** 在所有線性代數運算中，$A\mathbf{x}$ 是最基本的動作 — 但它的定義「**$A$ 各橫躺行與 $\mathbf{x}$ 做點積**」（或等價地「**$A$ 各直立列以 $\mathbf{x}$ 各分量為係數的線性組合**」）看起來規則特殊。**為什麼是這樣？這個定義是隨意的還是自然冒出的？**
>
> **對應主章：** [§3 ch03 章節摘要](ch03-mat-vec.md#章節摘要)
>
> **3-layer 涵蓋：** ① 歷史 / ② 推導 / ③ 昇華

### ① 歷史脈絡：從聯立方程的係數矩陣自然冒出

$A\mathbf{x}$ 的定義跟矩陣本身的歷史一起誕生 — 19 世紀中葉，當 Sylvester / Cayley 把矩陣獨立為代數物件時（見 [Q02](#q02)、[Q09](#q09)），最迫切的需求就是把**聯立方程的左邊**用矩陣記法濃縮。**$A\mathbf{x}$ 就是這個濃縮過程的產物 — 它不是事後設計的，是從寫法簡化的需求中自然浮現的**。

### ② 設計過程還原：從方程組到 $A\mathbf{x}$ 的浮現

給定一組 $m$ 個方程、$n$ 個未知數 $x_1, \ldots, x_n$ 的聯立方程：

$$
\begin{cases}
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n = b_1 \\
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n = b_2 \\
\;\vdots \\
a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n = b_m
\end{cases}
$$

**目標：把這 $m$ 個方程濃縮成單一矩陣方程 $A\mathbf{x} = \mathbf{b}$。**

#### 步驟 1：拆出 $A$、$\mathbf{x}$、$\mathbf{b}$

把左邊的係數寫成矩陣 $A$，未知數寫成向量 $\mathbf{x}$，右邊寫成向量 $\mathbf{b}$：

$$
A = \begin{bmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{bmatrix},
\quad
\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix},
\quad
\mathbf{b} = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix}
$$

#### 步驟 2：要求 $A\mathbf{x}$ = 方程左邊

我們希望 $A\mathbf{x}$ 的結果**就是聯立方程的左邊**（即 $m$ 個方程的左邊值組成的向量）。也就是希望：

$$
A\mathbf{x} = \begin{bmatrix}
a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n \\
a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n \\
\vdots \\
a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n
\end{bmatrix}
$$

#### 步驟 3：觀察規律 — 兩種等價讀法

**讀法 A：以橫躺行為單位 — (Mv1) 點積方式**

第 $i$ 個元素 $a_{i1} x_1 + a_{i2} x_2 + \cdots + a_{in} x_n$ **正是 $A$ 第 $i$ 橫躺行與 $\mathbf{x}$ 的點積**：

$$
(A\mathbf{x})_i = \mathbf{a}^*_i \cdot \mathbf{x}
$$

這是教科書最常見的視角 — 「**$A$ 各橫躺行 $\cdot$ $\mathbf{x}$**」。

**讀法 B：以直立列為單位 — (Mv2) 線性組合方式**

把同一個結果**按 $x_j$ 重新排列**：

$$
A\mathbf{x} = x_1 \begin{bmatrix} a_{11} \\ a_{21} \\ \vdots \\ a_{m1} \end{bmatrix} + x_2 \begin{bmatrix} a_{12} \\ a_{22} \\ \vdots \\ a_{m2} \end{bmatrix} + \cdots + x_n \begin{bmatrix} a_{1n} \\ a_{2n} \\ \vdots \\ a_{mn} \end{bmatrix}
= x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \cdots + x_n \mathbf{a}_n
$$

**這正是「$A$ 各直立列以 $\mathbf{x}$ 各分量為係數的線性組合」** — Strang 強調的「**列視角是線性代數的鑰匙**」（見 [Q07](#q07)）。

#### 步驟 4：兩讀法等價

兩讀法都從同一個 $A\mathbf{x}$ 出發，只是**按行展開（讀法 A）vs 按列展開（讀法 B）** — 機械等價。每個元素的值都是 $\sum_j a_{ij} x_j$，視角不同但答案一樣。

#### 小例題

取 $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$、$\mathbf{x} = \begin{bmatrix} 7 \\ 8 \\ 9 \end{bmatrix}$。

**讀法 A（按行點積）：**

$$
A\mathbf{x} = \begin{bmatrix} (1, 2, 3) \cdot (7, 8, 9) \\ (4, 5, 6) \cdot (7, 8, 9) \end{bmatrix} = \begin{bmatrix} 7 + 16 + 27 \\ 28 + 40 + 54 \end{bmatrix} = \begin{bmatrix} 50 \\ 122 \end{bmatrix}
$$

**讀法 B（按列線性組合）：**

$$
A\mathbf{x} = 7 \begin{bmatrix} 1 \\ 4 \end{bmatrix} + 8 \begin{bmatrix} 2 \\ 5 \end{bmatrix} + 9 \begin{bmatrix} 3 \\ 6 \end{bmatrix} = \begin{bmatrix} 7 \\ 28 \end{bmatrix} + \begin{bmatrix} 16 \\ 40 \end{bmatrix} + \begin{bmatrix} 27 \\ 54 \end{bmatrix} = \begin{bmatrix} 50 \\ 122 \end{bmatrix}
$$

**結果一致 ✓** — 同一個 $A\mathbf{x}$，兩種等價讀法。

### ③ 概念昇華：$A\mathbf{x}$ 是線代的基本動作

$A\mathbf{x}$ 看起來是「矩陣對向量的計算」，但本質上是**矩陣作為函數（變換）對向量的「作用」**：

$$
A : \mathbb{R}^n \longrightarrow \mathbb{R}^m,
\qquad
\mathbf{x} \longmapsto A\mathbf{x}
$$

矩陣 $A$ 同時承擔兩個角色：

| 角色 | $A\mathbf{x} = \mathbf{b}$ 的解讀 |
|---|---|
| **方程組的係數表** | 給定 $\mathbf{b}$，求滿足方程的 $\mathbf{x}$（解線性系統） |
| **線性變換的矩陣** | 給定 $\mathbf{x}$，計算變換後的 $\mathbf{b}$（向量映射） |

**這兩個角色通過 $A\mathbf{x}$ 統一**。從第一個角色出發 → 高斯消去法、LU 分解、Cramer 法則、解集結構（[Q22](#q22)）；從第二個角色出發 → 列空間、零空間、4 子空間、特徵值、SVD（[Q08](#q08)、[Q18](#q18)、[Q19](#q19)）。

**$A\mathbf{x}$ 是線代「動詞 + 受詞」結構的最小單位** — 整本書 §3 → §4 → §5 → §6 都是「**$A\mathbf{x}$ 的合成、分解、推廣**」：

- $AB\mathbf{x} = A(B\mathbf{x})$（兩個動作的合成 → 矩陣乘法 [Q09](#q09)）
- $A^k \mathbf{x}$（動作重複 → 動態系統與特徵值 [Q12](#q12)）
- $A = U\Sigma V^{\mathrm{T}}$（動作的分解 → SVD [Q19](#q19)）

### 延伸閱讀

**本書相關章節：**
- [§3 ch03 (Mv1) 點積方式](ch03-mat-vec.md#mv1-點積方式dot-product-way) — 讀法 A 完整版
- [§3 ch03 (Mv2) 線性組合方式](ch03-mat-vec.md#mv2-線性組合方式linear-combination-way) — 讀法 B 完整版
- [Q07](#q07) — 為什麼兩讀法都需要（不能只用其中一個）
- [Q08](#q08) — 4 子空間從 $A\mathbf{x}$ 和 $\mathbf{y}^{\mathrm{T}}A$ 的 2 視角交叉自然冒出
- [Q09](#q09) — $A\mathbf{x}$ 推廣到 $AB$ 的設計

**現代教科書：**
- Strang, G. (2020), *Linear Algebra for Everyone*, §1.1 "Linear Combinations are the Key" — 強調讀法 B（線性組合視角）

---

## Q07：為什麼要有 2 個視角（點積 + 線性組合）？ {#q07}

> **觸發問題：** 既然 $A\mathbf{x}$ 的兩種讀法（點積 vs 線性組合）數值上完全等價，**為什麼本書 §3 還要花力氣同時教兩種視角？挑一個用不就好了嗎？Strang 為什麼明確說「列視角是線代的鑰匙」**？
>
> **對應主章：** [§3 ch03 (Mv1)/(Mv2) 對偶關係](ch03-mat-vec.md#對偶關係mv1--mv2)
>
> **3-layer 涵蓋：** ③ 昇華

### ③ 概念昇華：兩視角各服務什麼不同問題？

兩讀法數值等價，但**它們揭示的「結構」完全不同**。挑哪個視角直接影響你看見的問題答案。

#### 視角分工總表

| 視角 | (Mv1) 點積方式 | (Mv2) 線性組合方式 |
|---|---|---|
| **數學形式** | $(A\mathbf{x})_i = \mathbf{a}^*_i \cdot \mathbf{x}$ | $A\mathbf{x} = \sum_j x_j \mathbf{a}_j$ |
| **思考單位** | 「每個輸出元素獨立算」 | 「輸出向量是各列的混合」 |
| **服務問題** | 「**算出輸出**」 — 計算機 / 程式 | 「**輸出在哪裡**」 — 幾何 / 結構 |
| **適合視覺化** | 一行一行掃過去（教科書式） | 列向量像「base color」，$\mathbf{x}$ 是「混色配方」 |
| **直接通往** | 高斯消去法、行階梯形、行運算 | 列空間 $\mathbf{C}(A)$、線性獨立、秩 |
| **後續章節主導** | §6.2 LU 分解（行消元） | §6.1 CR、§6.3 QR、§6.5 SVD（全部都拆「列」） |
| **Strang 評價** | 「Correct, but not the heart」 | 「**The key to linear algebra**」 |

#### 關鍵案例：「$A\mathbf{x} = \mathbf{b}$ 是否有解？」的兩視角對比

**問題：** 給定 $A, \mathbf{b}$，判斷方程有解嗎？

**(Mv1) 點積視角：** 要解 $\mathbf{x}$，跑高斯消去法跑完才能判斷 → 機械、計算密集、看不到結構。

**(Mv2) 線性組合視角：** 把問題重述為「**$\mathbf{b}$ 能不能寫成 $A$ 各直立列的線性組合？**」也就是問：「**$\mathbf{b}$ 在列空間 $\mathbf{C}(A)$ 裡嗎？**」

- 若 $\mathbf{b} \in \mathbf{C}(A)$ → 有解
- 若 $\mathbf{b} \notin \mathbf{C}(A)$ → 無解

**幾何上一秒判斷**（例：在 $\mathbb{R}^3$ 中，若 $\mathbf{C}(A)$ 是一個平面、$\mathbf{b}$ 在平面外，就無解）。

> Strang 在《Linear Algebra for Everyone》§1.1 一開門就說：
>
> > "The column space tells us **when** $A\mathbf{x} = \mathbf{b}$ can be solved — $\mathbf{b}$ must be in $\mathbf{C}(A)$."
> > （列空間告訴我們**何時** $A\mathbf{x} = \mathbf{b}$ 有解 — $\mathbf{b}$ 必須在 $\mathbf{C}(A)$ 中。）

#### 為什麼 Strang 強調「列視角是鑰匙」？

**因為線代的核心概念全部都是「列空間的衍生」：**

- **列空間 $\mathbf{C}(A)$：** 所有 $A\mathbf{x}$ 可能輸出的集合 — 從列視角直接看到
- **秩 $r$：** 線性獨立的列數 — 從列視角直接數
- **零空間 $\mathbf{N}(A)$：** 使「列線性組合為零」的 $\mathbf{x}$ — 從列視角直接構造
- **4 子空間定理（[Q08](#q08)）：** 列空間 + 行空間 + 兩個零空間的正交分解
- **CR 分解（[Q15](#q15)）：** 把 $A$ 拆成「線性獨立列 $C$」乘「線性組合係數 $R$」
- **QR 分解（[Q17](#q17)）：** 用 Gram-Schmidt 把 $A$ 的列正交化
- **SVD（[Q19](#q19)）：** 把 $A$ 的列空間和行空間用奇異值連結

**(Mv1) 點積視角只通往「計算 / 程式實作」，(Mv2) 列視角通往「結構 / 幾何 / 分解」**。沒有 (Mv2)，這半本線代就看不到。

#### 但 (Mv1) 也不可或缺

不要誤會 — **(Mv1) 不是「劣勢視角」**，只是服務不同問題：

| 任務 | 適合視角 |
|---|---|
| 寫 NumPy / BLAS 矩陣乘法函數 | (Mv1) — for-loop friendly |
| 高斯消去法、行運算 | (Mv1) — 一行一個方程 |
| 解 $A\mathbf{x} = \mathbf{b}$ 的具體 $\mathbf{x}$ | (Mv1) → LU 分解 |
| 判斷有沒有解、解集結構 | (Mv2) — 列空間視角 |
| 設計 SVD、CR、QR 分解 | (Mv2) — 列空間視角 |
| 機器學習：feature 表是直立列 | (Mv2) — 一列一個 sample |
| 神經網路：權重矩陣 × 輸入 | (Mv2) — 線性組合的多層堆疊 |

**所以本書 §3 同時教 2 視角的原因：** (Mv1) 是「**算**」、(Mv2) 是「**看**」。學會 (Mv1) 才能實作、學會 (Mv2) 才能思考。**缺一不可，但傳統教科書習慣只強調 (Mv1) — 這是現代線代教學要修正的地方**。

#### Strang 原話補充

Strang 在《Linear Algebra for Everyone》序言中明確說：

> "Most linear algebra books start with the **dot product** (row picture). I prefer to start with the **column picture** — linear combinations. This is the heart of linear algebra."
>
> （多數線代書從點積（行視角）開始。我偏好從列視角 — 線性組合 — 開始。這是線代的核心。）

本書沿用 Strang 的安排：**§3 同時教 2 視角但給 (Mv2) 更高的權重**，並在 §4–§6 全書中以 (Mv2) 為主導視角解釋分解結構。

### 延伸閱讀

**本書相關章節：**
- [§3 ch03 (Mv1)/(Mv2) 對偶關係](ch03-mat-vec.md#對偶關係mv1--mv2) — 對偶總表
- [§3 ch03 VizScript-01](ch03-mat-vec.md#vizscript-01) — 兩視角切換動畫
- [Q06](#q06) — $A\mathbf{x}$ 兩讀法的數學等價性
- [Q08](#q08) — 4 子空間從 2 視角的交叉自然冒出

**現代教科書：**
- Strang, G. (2020), *Linear Algebra for Everyone*, §1.1 "Linear Combinations and Columns" — 一開門就強調列視角

---

## Q08：四個基本子空間為什麼會自然冒出？ {#q08}

> **觸發問題：** Strang 稱「**四個基本子空間（four fundamental subspaces）**」為「**線性代數的地圖**」 — 但這 4 個子空間（列空間 $\mathbf{C}(A)$、行空間 $\mathbf{C}(A^{\mathrm{T}})$、零空間 $\mathbf{N}(A)$、左零空間 $\mathbf{N}(A^{\mathrm{T}})$）為什麼正好是 **4** 個？為什麼**這 4 個剛好兩兩正交**？這些定理是巧合，還是必然？
>
> **對應主章：** [§3 ch03 四個基本子空間](ch03-mat-vec.md#四個基本子空間the-four-fundamental-subspaces)
>
> **3-layer 涵蓋：** ② 推導 / ③ 昇華

### ② 設計過程還原：4 個子空間 = 2 運算 × 2 視角的交叉產物

4 個子空間**不是人為定義的概念**，而是從「**$A\mathbf{x}$ 的 2 視角**」與「**右乘 $A$ vs 左乘 $A^{\mathrm{T}}$ 的 2 方向**」交叉產生的**自然產物**。

#### 步驟 1：兩個方向（左乘 vs 右乘）

對矩陣 $A \in \mathbb{R}^{m \times n}$，有兩個基本「動作」：

| 動作 | 形式 | 輸入空間 | 輸出空間 |
|---|---|---|---|
| **右乘（從右）** | $\mathbf{x} \mapsto A\mathbf{x}$ | $\mathbb{R}^n$ | $\mathbb{R}^m$ |
| **左乘（從左）** | $\mathbf{y} \mapsto A^{\mathrm{T}}\mathbf{y}$ | $\mathbb{R}^m$ | $\mathbb{R}^n$ |

#### 步驟 2：每個動作的「輸出範圍 + 零點」

對任何線性變換 $f$，自然有兩個關聯子空間：

| 概念 | 含意 |
|---|---|
| **像（image / range）** | 所有可能的輸出 $\{f(\mathbf{x}) : \mathbf{x} \in \text{domain}\}$ |
| **核（kernel / null）** | 映射到零的輸入 $\{\mathbf{x} : f(\mathbf{x}) = \mathbf{0}\}$ |

#### 步驟 3：交叉組合 → 4 子空間

| 動作 | 像 | 核 |
|---|---|---|
| 右乘 $A$ | $\{A\mathbf{x}\} = \mathbf{C}(A)$ 列空間 | $\{\mathbf{x} : A\mathbf{x} = \mathbf{0}\} = \mathbf{N}(A)$ 零空間 |
| 左乘 $A^{\mathrm{T}}$ | $\{A^{\mathrm{T}}\mathbf{y}\} = \mathbf{C}(A^{\mathrm{T}})$ 行空間 | $\{\mathbf{y} : A^{\mathrm{T}}\mathbf{y} = \mathbf{0}\} = \mathbf{N}(A^{\mathrm{T}})$ 左零空間 |

**2 個動作 × 2 個關聯子空間 = 4 個基本子空間。** 不可能多、不可能少。

#### 步驟 4：自然冒出的正交性

**關鍵定理：$\mathbf{N}(A) \perp \mathbf{C}(A^{\mathrm{T}})$**

**證明：** 假設 $\mathbf{x} \in \mathbf{N}(A)$，即 $A\mathbf{x} = \mathbf{0}$。把 $A\mathbf{x}$ 用 (Mv1) 點積視角展開：

$$
A\mathbf{x} =
\begin{bmatrix}
\mathbf{a}^*_1 \cdot \mathbf{x} \\
\mathbf{a}^*_2 \cdot \mathbf{x} \\
\vdots \\
\mathbf{a}^*_m \cdot \mathbf{x}
\end{bmatrix}
= \mathbf{0}
$$

意即 $\mathbf{a}^*_i \cdot \mathbf{x} = 0$ for all $i$ — **$\mathbf{x}$ 與 $A$ 的每一橫躺行都垂直**。由於 $\mathbf{C}(A^{\mathrm{T}})$ 就是這些橫躺行的線性張成，$\mathbf{x}$ 與 $\mathbf{C}(A^{\mathrm{T}})$ 整個空間垂直 → $\mathbf{x} \in \mathbf{C}(A^{\mathrm{T}})^{\perp}$。

**等價反向：** 反過來若 $\mathbf{x}$ 與 $A$ 每一橫躺行都垂直，則 $A\mathbf{x} = \mathbf{0}$，即 $\mathbf{x} \in \mathbf{N}(A)$。

**所以 $\mathbf{N}(A) = \mathbf{C}(A^{\mathrm{T}})^{\perp}$**（這兩個子空間互為正交補餘）。

**對偶定理：** 對 $A^{\mathrm{T}}$ 同理可證 $\mathbf{N}(A^{\mathrm{T}}) = \mathbf{C}(A)^{\perp}$。

#### 步驟 5：兩個維度等式（rank–nullity）

由「**正交補餘 → 維度可加**」直接推：

$$
\boxed{
\dim \mathbf{C}(A^{\mathrm{T}}) + \dim \mathbf{N}(A) = n
\qquad
\dim \mathbf{C}(A) + \dim \mathbf{N}(A^{\mathrm{T}}) = m
}
$$

#### 步驟 6：列秩 = 行秩

從上式可以證明（這是更深的結果，[Q15](#q15) 詳述）：

$$
\boxed{
\dim \mathbf{C}(A) = \dim \mathbf{C}(A^{\mathrm{T}}) = r
}
$$

**列秩 = 行秩 = $r$** — 從 4 子空間框架自然推出。

#### Strang 的 4 子空間圖（Big Picture）

Strang 4 大基本定理可以用一張「**big picture**」總結：

```
                            A 的作用
                    ───────────────────────

$\mathbb{R}^n$ (n 維)                                $\mathbb{R}^m$ (m 維)
    ┌───────────────────┐                ┌───────────────────┐
    │ 行空間            │  ───── A ───>  │ 列空間            │
    │ C(A^T)            │                │ C(A)              │
    │ dim = r           │                │ dim = r           │
    │                   │                │                   │
    │ ⊥                 │                │ ⊥                 │
    │                   │                │                   │
    │ 零空間            │  ───── A ───>  │ 0 向量            │
    │ N(A)              │                │                   │
    │ dim = n−r         │                │                   │
    └───────────────────┘                └───────────────────┘
                                                  ↑
                                         左零空間 N(A^T), dim = m−r
                                         (A 不到達的補餘方向)
```

**這張圖是線性代數的「地圖」 — 整本書 §3 → §4 → §5 → §6 都在這張地圖上展開。**

### ③ 概念昇華：4 子空間是線性代數的地理

Strang 在《Linear Algebra for Everyone》§3 開門就說：

> "The four fundamental subspaces are the **geography of linear algebra**."
> （四個基本子空間是線性代數的**地理**。）

「地理」不是裝飾詞 — 它精確描述了：**任何線性代數的問題都可以放到這張地圖上找位置**。

#### 4 子空間怎麼把整個線性代數「組織」起來？

| 問題 | 4 子空間的解釋 |
|---|---|
| **$A\mathbf{x} = \mathbf{b}$ 有解嗎？** | $\mathbf{b} \in \mathbf{C}(A)$ 嗎？（[Q22](#q22)） |
| **$A\mathbf{x} = \mathbf{b}$ 解唯一嗎？** | $\mathbf{N}(A) = \{\mathbf{0}\}$ 嗎？（若不是，解集 = 特解 + $\mathbf{N}(A)$） |
| **$A$ 滿秩嗎？** | $\dim \mathbf{C}(A) = \min(m, n)$？ |
| **最小平方法 $\hat{\mathbf{x}} = \arg\min \|\mathbf{b} - A\mathbf{x}\|$** | 把 $\mathbf{b}$ 投影到 $\mathbf{C}(A)$，殘差 $\mathbf{r} = \mathbf{b} - A\hat{\mathbf{x}} \in \mathbf{N}(A^{\mathrm{T}})$（與列空間正交） |
| **SVD 構造（[Q19](#q19)）** | $V$ 的前 $r$ 列是 $\mathbf{C}(A^{\mathrm{T}})$ 的正交基底；$V$ 的後 $n{-}r$ 列是 $\mathbf{N}(A)$ 的正交基底；$U$ 的前 $r$ 列是 $\mathbf{C}(A)$ 的正交基底；$U$ 的後 $m{-}r$ 列是 $\mathbf{N}(A^{\mathrm{T}})$ 的正交基底 — **SVD 給出 4 子空間的標準正交基底** |
| **零空間平移仿射子空間** | $A\mathbf{x} = \mathbf{b}$ 的完整解集 = 特解 $\mathbf{x}_p$ + 整個 $\mathbf{N}(A)$（[appendix-four-subspaces](appendix-four-subspaces.md)） |
| **偽反矩陣 $A^{+}$** | 把 $\mathbf{C}(A)$ 內的點映回 $\mathbf{C}(A^{\mathrm{T}})$；把 $\mathbf{N}(A^{\mathrm{T}})$ 內的點映到 $\mathbf{0}$（[appendix-matrix-world](appendix-matrix-world.md)） |

> **結論：** 4 個子空間**不是 4 個任意挑出的子空間**，是「**$A\mathbf{x}$ 與 $A^{\mathrm{T}}\mathbf{y}$ 各自像與核**」的窮舉。**「2 方向 × 2 概念 = 4」是組合上不可避免的數字 — 不可能多、不可能少。** 它們兩兩正交、維度相加等於矩陣兩個維度、列秩 = 行秩 — 這些「優美」的結果不是巧合，而是「**$A$ 作用 = 將 $\mathbb{R}^n$ 分成（行空間 + 零空間），$A^{\mathrm{T}}$ 作用 = 將 $\mathbb{R}^m$ 分成（列空間 + 左零空間）**」這個雙向分解的必然產物。**Strang FTLA 是線性代數的核心定理**，從這個框架出發 → 解線性系統、最小平方法、SVD、Moore–Penrose 偽反、譜分解，全部都是 4 子空間的某種具體化。

### 延伸閱讀

**本書相關章節：**
- [§3 ch03 四個基本子空間](ch03-mat-vec.md#四個基本子空間the-four-fundamental-subspaces) — 正式定義
- [§3 ch03 VizScript-03 Strang Big Picture](ch03-mat-vec.md#vizscript-03) — 4 子空間互動視覺化 ⭐⭐⭐
- [appendix-four-subspaces.md](appendix-four-subspaces.md) — 4 子空間整合附錄 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構
- [appendix-matrix-world.md](appendix-matrix-world.md) — 偽反矩陣（4 子空間的標準正交基底連結）
- [Q06](#q06) / [Q07](#q07) — $A\mathbf{x}$ 與 2 視角是 4 子空間的前置
- [Q15](#q15) — 列秩 = 行秩的證明（CR 分解視角）
- [Q19](#q19) — SVD 構造 4 子空間正交基底
- [Q22](#q22) — 解 $A\mathbf{x}=\mathbf{b}$ 的解集結構

**現代教科書：**
- **Strang, G. (2020), *Linear Algebra for Everyone*, Ch.3 "The Four Fundamental Subspaces"** — 4 子空間是線代地理的核心比喻
- Strang, G. (1993), "The Fundamental Theorem of Linear Algebra", *American Mathematical Monthly*, 100(9), 848–855 — Strang 4 大基本定理的單篇論文

---

## Q09：矩陣乘法為什麼是「行乘列」？ {#q09}

> **觸發問題：** 矩陣加法和純量乘法都很直覺 — 對應位置相加 / 整體放大 — 唯獨矩陣乘法的規則複雜得多：必須把「左矩陣的橫躺行（row）」與「右矩陣的直立列（column）」對應元素相乘再相加。**為什麼一定要這樣定義？這個規則是隨意湊出來的嗎？**
>
> **對應主章：** [§4 ch04 (MM1) 點積方式](ch04-mat-mat.md#mm1-點積方式element-wise-dot-product-way)
>
> **3-layer 涵蓋：** ① 歷史 / ② 推導 / ③ 昇華 全有

### ① 歷史脈絡：先有方程，後有矩陣

#### 東方源頭：兩千年前的《九章算術》

「把係數排成方陣來解聯立方程」這個想法，在東方早已存在。中國漢代《**九章算術**》第八卷「**方程**」章（西元前 1 世紀成書，劉徽 263 年作注），記載了一個三元一次聯立方程的解法。原文如下：

> 今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；
> 上禾二秉，中禾三秉，下禾一秉，實三十四斗；
> 上禾一秉，中禾二秉，下禾三秉，實二十六斗。
> 問上、中、下禾實一秉各幾何？

用現代記法即解：

$$
\begin{cases}
3 a + 2 b + 1 c = 39 \\
2 a + 3 b + 1 c = 34 \\
1 a + 2 b + 3 c = 26
\end{cases}
$$

《九章算術》的解法是把所有係數排成方陣（**用算籌橫列直排**），然後做「直除」（橫向加減消元）— 這本質上就是**現代的高斯消去法**。但中國數學家**只把方陣當作運算的記法**，而沒有把它當作**獨立的代數物件**來研究。

#### 西方定義：19 世紀中葉

- **1850 年：** 英國數學家 **James Joseph Sylvester** 在論文 *Additions to the articles "On a new class of theorems" and "On Pascal's theorem"* 中，首次使用拉丁文「**Matrix**」（意為「子宮 / 母體」）來命名「孕育行列式的方陣」。但此時仍視為記法。
- **1858 年：** **Arthur Cayley** 在開創性論文 *A Memoir on the Theory of Matrices*（《矩陣理論論文集》，Philosophical Transactions of the Royal Society of London, 148, 17–37）中，**首次把矩陣獨立為代數物件**，系統地定義了：
  - 矩陣加法、純量乘法
  - 矩陣乘法
  - 單位矩陣 $I$、零矩陣 $O$
  - 反矩陣 $A^{-1}$
  - 「矩陣多項式」 $A^2, A^3, \ldots, p(A)$

#### Cayley 的初心：合成兩個運算

Cayley 在原論文一開篇就明說：

> "The fundamental notion involved in the theory of matrices is that of the composition or multiplication of two operations."
>
> （**矩陣理論的根本概念就是兩個運算的合成或乘法。**）

換言之，**Cayley 設計矩陣乘法不是為了好玩，是為了讓「兩個線性變換的合成」可以用一種濃縮、機械化的記法表達。** 那個看似複雜的「行 · 列」乘法規則，是這個目的下**自然冒出的必然結果**，下面我們完整還原這個推導。

### ② 設計過程還原：從變數連續代換還原乘法規則

#### 問題：兩組線性變換要合成

假設我們手上有**兩組線性變換**：

**第一組** — 把中間變數 $\mathbf{u} = (u_1, u_2)$ 映射到輸出 $\mathbf{y} = (y_1, y_2, y_3)$：

$$
\begin{cases}
y_1 = a_{11} u_1 + a_{12} u_2 \\
y_2 = a_{21} u_1 + a_{22} u_2 \\
y_3 = a_{31} u_1 + a_{32} u_2
\end{cases}
\qquad \text{用矩陣寫：} \mathbf{y} = A \mathbf{u},
\;
A = \begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22} \\
a_{31} & a_{32}
\end{bmatrix}
$$

**第二組** — 把輸入 $\mathbf{x} = (x_1, x_2)$ 映射到中間變數 $\mathbf{u}$：

$$
\begin{cases}
u_1 = b_{11} x_1 + b_{12} x_2 \\
u_2 = b_{21} x_1 + b_{22} x_2
\end{cases}
\qquad \text{用矩陣寫：} \mathbf{u} = B \mathbf{x},
\;
B = \begin{bmatrix}
b_{11} & b_{12} \\
b_{21} & b_{22}
\end{bmatrix}
$$

#### 需求：直接得到 $\mathbf{y}$ 對 $\mathbf{x}$ 的關係

我們想消去中間變數 $\mathbf{u}$，直接知道輸入 $\mathbf{x}$ 怎麼變成輸出 $\mathbf{y}$。**沒有矩陣記法之前，我們只能笨拙地代入展開。** 以 $y_1$ 為例：

$$
y_1 \;=\; a_{11} u_1 + a_{12} u_2
$$

把 $u_1 = b_{11} x_1 + b_{12} x_2$ 與 $u_2 = b_{21} x_1 + b_{22} x_2$ 代入：

$$
\begin{aligned}
y_1
&= a_{11} (b_{11} x_1 + b_{12} x_2) + a_{12} (b_{21} x_1 + b_{22} x_2) \\
&= a_{11} b_{11} x_1 + a_{11} b_{12} x_2 + a_{12} b_{21} x_1 + a_{12} b_{22} x_2 \\
&= \underbrace{(a_{11} b_{11} + a_{12} b_{21})}_{x_1 \text{ 的新係數}} x_1 \;+\; \underbrace{(a_{11} b_{12} + a_{12} b_{22})}_{x_2 \text{ 的新係數}} x_2
\end{aligned}
$$

#### 關鍵觀察：新係數的規律

仔細看 $x_1$ 前的新係數 $(a_{11} b_{11} + a_{12} b_{21})$，它由兩部分構成：

| 來源 | 內容 |
|---|---|
| **$A$ 的第 1 橫躺行（row）** | $(\,a_{11},\; a_{12}\,)$ |
| **$B$ 的第 1 直立列（column）** | $(\,b_{11},\; b_{21}\,)^{\mathrm{T}}$ |
| **新係數** | $a_{11} \cdot b_{11} + a_{12} \cdot b_{21}$ |

這正是「**$A$ 第 1 行 · $B$ 第 1 列**」的**點積**！同理：

- $x_2$ 前的係數 $(a_{11} b_{12} + a_{12} b_{22})$ = $A$ 第 1 行 · $B$ 第 2 列。
- 若繼續展開 $y_2$，會得到 $A$ 第 2 行 · $B$ 第 $j$ 列。
- 一般地，$y_i$ 對 $x_j$ 的新係數 = **$A$ 第 $i$ 橫躺行 · $B$ 第 $j$ 直立列**。

#### 一般化：矩陣乘法的標準定義

若 $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$，定義 $C = AB \in \mathbb{R}^{m \times n}$，其元素為：

$$
\boxed{
c_{ij}
\;=\;
\sum_{p=1}^{k} a_{ip}\, b_{pj}
\;=\;
\mathbf{a}^*_i \cdot \mathbf{b}_j
}
$$

其中 $\mathbf{a}^*_i$ 是 $A$ 的第 $i$ 橫躺行、$\mathbf{b}_j$ 是 $B$ 的第 $j$ 直立列。**這就是教科書的 (MM1) 點積規則** — 它**不是憑空的，是「變數連續代換後新係數的必然形式」**。Cayley 把這個自然冒出的規律**直接定義為**矩陣乘法，從此 $\mathbf{y} = A\mathbf{u}$ 與 $\mathbf{u} = B\mathbf{x}$ 的合成可以濃縮為：

$$
\mathbf{y} \;=\; A(B\mathbf{x}) \;=\; (AB)\mathbf{x}
$$

運算規則自動生效，無須每次重複代入展開。

#### 小例題驗證

取

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix},
\quad
B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}
$$

**笨方法（代入展開）：** 對應線性變換為：

$$
\begin{cases} y_1 = u_1 + 2 u_2 \\ y_2 = 3 u_1 + 4 u_2 \end{cases}
\qquad
\begin{cases} u_1 = 5 x_1 + 6 x_2 \\ u_2 = 7 x_1 + 8 x_2 \end{cases}
$$

代入：

$$
\begin{aligned}
y_1 &= (5 x_1 + 6 x_2) + 2(7 x_1 + 8 x_2) = 19 x_1 + 22 x_2 \\
y_2 &= 3(5 x_1 + 6 x_2) + 4(7 x_1 + 8 x_2) = 43 x_1 + 50 x_2
\end{aligned}
$$

**聰明方法（矩陣乘法）：**

$$
AB
\;=\;
\begin{bmatrix}
1{\cdot}5 + 2{\cdot}7 & \quad 1{\cdot}6 + 2{\cdot}8 \\
3{\cdot}5 + 4{\cdot}7 & \quad 3{\cdot}6 + 4{\cdot}8
\end{bmatrix}
\;=\;
\begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}
$$

**結果完全一致 ✓** — 代入法的新係數就是 (MM1) 的矩陣乘法元素。Cayley 把「代入展開」的繁瑣操作壓縮為「行 · 列」的機械規則，這就是矩陣乘法之所以「長這樣」的根本原因。

### ③ 概念昇華：矩陣是高階語言、乘法是函數合成

矩陣是一種**高階語言**：

- **名詞** — 矩陣 $A$ 把「一組 $m \times n$ 個係數」濃縮為**單一物件**。
- **動詞** — 矩陣乘法 $AB$ 把「兩個變換的合成」濃縮為**單一運算**。

從這個視角看，矩陣乘法的本質**不是「行乘列」的機械操作**，而是**函數合成（function composition）**：

$$
\boxed{
(AB)(\mathbf{x}) \;=\; A\bigl(B(\mathbf{x})\bigr)
}
$$

也就是「**先 $B$ 變換、再 $A$ 變換**」這個動作的代數記法。從此理解：

| 矩陣現象 | 函數合成本質 |
|---|---|
| **為什麼乘法不可交換 $AB \ne BA$？** | 函數合成不可交換 — 「先穿襪再穿鞋」≠「先穿鞋再穿襪」（詳見 [Q10](#q10)） |
| **為什麼有結合律 $(AB)C = A(BC)$？** | 函數合成天然有結合律 — $((f \circ g) \circ h)(x) = f(g(h(x))) = (f \circ (g \circ h))(x)$ |
| **為什麼矩陣加法直覺、乘法複雜？** | 加法只是「同位置相加」沒有結構意義；乘法承載「變換合成」的完整資訊 |
| **為什麼 $A I = I A = A$？** | 「不做事」這個變換（恆等函數）合成任何變換都等於原變換 |
| **為什麼 $(AB)^{-1} = B^{-1} A^{-1}$（順序顛倒）？** | 「先穿襪再穿鞋」的逆動作是「先脫鞋再脫襪」 — 合成的逆順序顛倒 |

#### Strang 的補充洞見：點積規則不是矩陣乘法的核心

值得注意的是，Strang 在《Linear Algebra for Everyone》§1.4 特別強調：

> "The dot product rule is correct, but it is **not the heart** of matrix multiplication. The heart is the rank-1 decomposition $AB = \sum_p \mathbf{a}_p \mathbf{b}^*_p$ — **columns of A times rows of B**."
>
> （點積規則沒錯，但**不是矩陣乘法的核心**。**核心是秩 1 分解** — $A$ 的直立列乘 $B$ 的橫躺行。）

也就是本書 §4 的 [(MM4) 外積之和方式](ch04-mat-mat.md#mm4-外積之和方式sum-of-outer-products--rank-1-decomposition-way--本章核心)：

$$
AB \;=\; \sum_{p=1}^{k} \mathbf{a}_p \mathbf{b}^*_p
\qquad
(\text{A 的列} \times \text{B 的行}，\text{秩 1 矩陣的疊加})
$$

**為什麼這才是「核心」？** 因為 (MM4) 視角直接揭示「矩陣乘法本質是秩 1 圖層的線性組合」 — 這正是 §6 SVD（$A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$）、CR 分解、低秩近似（Eckart–Young 定理）的**真正鑰匙**。詳見 [ch04 VizScript-02 MM4 秩 1 累加動畫](ch04-mat-mat.md#vizscript-02)。

**所以對「為什麼矩陣乘法這樣定義」的最完整答案是：**

> Cayley 設計矩陣乘法的初心是**簡化線性變換的合成**（從歷史出發，(MM1) 點積規則自然冒出）；但矩陣乘法**最有威力的視角**是 Strang 強調的 (MM4) 外積之和（直立列 × 橫躺行 → 秩 1 矩陣疊加）— 它把矩陣乘法昇華為**「以秩 1 為原子的可加結構」**，這個視角是線性代數從 19 世紀的「方程求解工具」躍升為 21 世紀的「資料科學語言」的關鍵橋樑。

### 延伸閱讀

**本書相關章節：**
- [§4 ch04 (MM1) 點積方式](ch04-mat-mat.md#mm1-點積方式element-wise-dot-product-way) — 規則本體
- [§4 ch04 (MM4) 外積之和](ch04-mat-mat.md#mm4-外積之和方式sum-of-outer-products--rank-1-decomposition-way--本章核心) — Strang 強調的「真正核心」
- [§4 ch04 VizScript-01 四視角切換](ch04-mat-mat.md#vizscript-01) — 互動式對照四種等價視角
- [§4 ch04 VizScript-02 MM4 秩 1 累加 + Mona Lisa SVD demo](ch04-mat-mat.md#vizscript-02) — Tier 3 旗艦
- [Q10](#q10) — 為什麼乘法不可交換（函數合成的不可交換本質）
- [Q14](#q14) — 為什麼要把矩陣「分解」（秩 1 為原子的可加結構是 §6 五大分解的共同根源）

**歷史原典：**
- 《**九章算術**》方程章（漢代，西元前 1 世紀成書，劉徽 263 年作注）— 高斯消去法的最早記載，但僅把方陣當記法
- Sylvester, J. J. (1850), *Additions to the articles "On a new class of theorems" and "On Pascal's theorem"*, **Philosophical Magazine** — "Matrix" 一詞首次出現
- **Cayley, A. (1858)**, *A Memoir on the Theory of Matrices*, **Philosophical Transactions of the Royal Society of London**, 148, 17–37 — 矩陣代數正式定義，矩陣乘法規則明文化

**現代教科書：**
- Strang, G. (2020), *Linear Algebra for Everyone*, §1.4 "Matrix Multiplication AB and CR"（強調 (MM4) 是矩陣乘法的真正核心，並用 $A=CR$ 作為入門分解）
- Strang, G. (2023), *Introduction to Linear Algebra* (6th ed.), §2.4 "Rules for Matrix Operations"（傳統「行 · 列」規則完整推導）

---

## 其餘 13 條（Q10–Q22）— 規劃中

依 S13–S15 路線圖逐步補完：

- **S13** — Q10（§4 不可交換）+ Q11–Q13（§5 對角 / P3 / P4）
- **S14** — Q14（分解整體動機）+ Q15–Q19（§6 五大分解各 1）
- **S15** — Q20–Q22（3 附錄）+ 主章 callout 批次插入 + 整合收尾

每條 Q&A 採與 Q01–Q09 相同的 3-layer 結構（① 歷史 → ② 推導 → ③ 昇華 + 延伸閱讀），篇幅約 1000–2500 字含舉例 + 推導 + 經典出處引用。

---

> **附錄末更新時間：** S12 (2026-05-13) — Q01–Q09 完成（9/22，41%）
