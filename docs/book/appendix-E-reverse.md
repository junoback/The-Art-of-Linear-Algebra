# 附錄 E：逆向設計 — 從實際問題反推矩陣運算

> **附錄定位：** 全書 13 個主章 + Appendix D 22 條 Q&A 都採「**正向**」視角 — 先給定運算規則，再說明意義與用處。本附錄改採「**逆向**」視角 — **從工程/科學中的實際問題出發，一步步反推出矩陣運算規則本身**。
>
> **與 Appendix D 的對偶關係：**
>
> - **Appendix D「背後觀念」** = 用 3-layer 框架（① 歷史脈絡 + ② 設計過程還原 + ③ 概念昇華）橫切剖析每條規則「為什麼這樣設計」
> - **Appendix E「逆向設計」** = 走完整 **5 步反推鏈**，從「實際問題」一步步**推出運算規則本身**
> - 兩者**互補**：D 從橫切面剖析，E 從縱向走一遍；D 解答「為什麼」，E 展示「**怎麼從零反推出來**」
>
> **核心信念：** 矩陣運算（點積 / 外積 / 矩陣乘法 / 列空間 / 4 子空間 / 五大分解 / 偽反）**沒有一個是憑空發明的**。它們**全部**是某個「實際問題 + 還原需求」反推出來的**唯一可能規則**。本附錄走 7 條鏈（R01-R07），把這個反推過程具體可視化。
>
> **使用建議：** 與 Appendix D 一樣，可在主章遇到 `🔄 逆向設計` callout 時點連結跳來看；或從 R01 連讀至 R07 當作「全書反推路線」整體導讀。
>
> **編寫進度：** S19 啟動（Back 提出逆向設計視角全書第二骨架）→ R01 PoC 通過 → R02 同 session 寫 → R03-R07 後續 session 補。

---

## 5 步反推骨架（鏈條通則）

每條鏈（R01-R07）都遵循 **5 步反推骨架**：

1. **實際問題（結果需求）** — 工程 / 科學中反覆出現的某類問題
2. **物件化（抽離係數與變數）** — 把問題從「方程組語言」抽象到「矩陣物件」層次；同時釐清「對矩陣物件的合法操作必須對應方程組層的合法變形」（**抽離–還原的可逆閉合**）
3. **尋找未知運算 ◯** — 寫下短公式 $A \mathbin{\bigcirc} \mathbf{x} = \mathbf{b}$（或類似），◯ 是未知的
4. **閉合需求反推 ◯ 的規則** — 由「還原原問題的需求」**唯一強制** ◯ 必須長什麼樣
5. **副產物自動冒出** — 規則確立後，相關性質、概念、定理**全部作為副產物自動冒出**

最後一步**昇華 + 跨鏈連結 + Strang 鎖核**。

---

## 反推鏈總覽表

| 鏈 | 反推目標 | 從哪個實際問題出發 | Step 4 核心觀察 |
|---|---|---|---|
| [R01](#r01) | (Mv1) $A\mathbf{x}$ 點積規則 | n 變數 m 條件線性問題 | 點積對位相加是唯一能還原所有方程的運算 |
| [R02](#r02) | 外積 $\mathbf{u}\mathbf{v}^{\top}$ | 構造「秩 1 原子」 | column × row 自動產生 m×n 矩陣，最小可分離單位 |
| [R03](#r03) | 矩陣乘法 $AB$ | 兩個變換的合成 | $(AB)\mathbf{x} = A(B\mathbf{x})$ 強制 row-column 點積 |
| [R04](#r04) | 列空間 / 零空間 / 4 子空間 | $A\mathbf{x}=\mathbf{b}$ 何時有解 / 何時唯一 | 對偶必然產物 |
| [R05](#r05) | A = CR 分解 | 視覺化 rank | C 收容獨立 column、R 是 RREF |
| [R06](#r06) | 偽反矩陣 $A^{+}$ | rank-deficient 仍要最優解 | SVD 集大成 |
| [R07](#r07) | (P4) 三明治分解 | 視角切換 + 對角縮放 | 函數合成 + 譜定理 |

---

## R01: 反推 (Mv1) $A\mathbf{x}$ 點積規則 {#r01}

### Step 0: 我們在做什麼

| | 視角 | 切入問題 |
|---|---|---|
| **正向**（傳統教科書） | 給你 $A\mathbf{x}$ 定義 → 解釋意義 | 「$A\mathbf{x}$ 怎麼算？」 |
| **逆向**（本鏈） | 給你問題 → 反推 $A\mathbf{x}$ 規則 | **「$A\mathbf{x}$ 為什麼非這樣不可？」** |

走完這條鏈會看到：**$A\mathbf{x}$ 不是任意規定，它是被「閉合需求」逼出來的唯一可能規則** — 一旦明白這點，(Mv2) 雙視角、列空間、rank、矩陣乘法、五大分解，全部會作為副產物**自動冒出來**。

### Step 1: 實際問題（結果需求）

工程 / 科學中**反覆出現**的同一類問題：

> **n 個未知量、m 個線性條件**，每個條件用未知量的線性組合表達一個結果。

3 個典型例子：

- **食譜**：3 種食材克數 → 3 種營養素總量（熱量 / 蛋白質 / 纖維）
- **電路**：5 個節點 × Kirchhoff 電流定律 → 5 條方程
- **化學配平**：4 個分子係數 × 元素守恆

**最一般形式：**

$$b_i = a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n, \quad i = 1, \ldots, m$$

#### 主例題（貫穿全鏈）：3 種食材(n) × 2 種營養指標(m)

| 食材 | 熱量 (kcal/g) | 纖維 (g/g) |
|---|---|---|
| 紅蘿蔔 $x_1$ | 2 | 1 |
| 馬鈴薯 $x_2$ | 3 | −1 |
| 洋蔥 $x_3$ | 1 | 4 |

方程組：

$$\begin{cases} 2x_1 + 3x_2 + x_3 = b_1 \quad \text{(熱量總和)} \\ x_1 - x_2 + 4x_3 = b_2 \quad \text{(纖維總和)} \end{cases}$$

設 $\mathbf{x} = (1, 1, 2)^{\top}$（g，食材重量），代入算 $\mathbf{b}$：

- $b_1 = 2(1) + 3(1) + 1(2) = 7$
- $b_2 = 1(1) - 1(1) + 4(2) = 8$

所以 $\mathbf{b} = (7, 8)^{\top}$。

**結果需求：** 給定一份食材組合的份量 $\mathbf{x} = (x_1, \ldots, x_n)^{\top}$（g），能**機械地**算出對應的所有營養素總量 $\mathbf{b} = (b_1, \ldots, b_m)^{\top}$。份量 $\mathbf{x}$ 會隨每次需求變動，但「怎麼從份量算營養素」這條規則本身是**固定的**（由食材成分表決定）。

### Step 2: 第一步 — 物件化（抽離係數與變數）

注意：營養素 i 的總量 $b_i$ 由**兩部分**決定 — 食材的份量 $\mathbf{x} = (x_1, \ldots, x_n)^{\top}$ 是這次的**輸入**（會隨需求變動），而所有食材對應營養素 i 的含量 $(a_{i1}, \ldots, a_{in})$ 則**完全決定**「營養素 i 的總量怎麼從 $\mathbf{x}$ 算出來」這條規則本身（食材成分表查得到，**不隨輸入變動**）。

「規則固定 / 輸入變動」這個分工正是下一步**物件化**的動機：把不變的規則 $\{a_{ij}\}$ 抽離出來，獨立成一個物件。

把 $\{a_{ij}\}$ 從 $a_{ij}x_j$ 中剝離，獨立排成 m×n 表格：

$$A = \begin{bmatrix} 2 & 3 & 1 \\ 1 & -1 & 4 \end{bmatrix}, \quad \mathbf{x} = \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix}, \quad \mathbf{b} = \begin{bmatrix} 7 \\ 8 \end{bmatrix}$$

#### 完整解集（因 m=2 < n=3，無窮多解）

先解零空間 — 求 $\mathbf{v}$ 使 $A\mathbf{v} = \mathbf{0}$：

- $2v_1 + 3v_2 + v_3 = 0$
- $v_1 - v_2 + 4v_3 = 0$ → $v_1 = v_2 - 4v_3$

代回：$5v_2 - 7v_3 = 0$。設 $v_3 = 5$ → $\mathbf{v} = (-13, 7, 5)^{\top}$（驗證：$-26+21+5=0$ ✓，$-13-7+20=0$ ✓）。

$$\boxed{\text{原解集：} \mathbf{x} = (1, 1, 2)^{\top} + t \cdot (-13, 7, 5)^{\top}, \quad t \in \mathbb{R}}$$

#### Step 2 加強：對 A 的操作必須對應方程組層的合法代數變形

物件化後，A 看起來只是「一個獨立的數字表格」 — 似乎可以隨意操作。**但其實不行**。

A 之所以**還代表原方程組**，前提是：

> **對 A 的任何操作，必須對應方程組層的某個合法代數變形；否則操作後的 A' 不再代表原方程組（解集會斷裂）。**

這個原則叫**抽離–還原的可逆閉合**。

我們**只用初中代數會的方程組變形語言**（不需任何矩陣乘法概念）來描述合法 / 非法操作。這在邏輯上很關鍵 — 矩陣乘法要等 Step 4 才被推出來，**現在還不能用它解釋自己**。

**方程組層的 3 條合法代數變形**（中學就會的）：

| 變形 | 對 A 的 entry 怎麼動 | 對 b 的 entry 怎麼動 |
|---|---|---|
| ① 整條方程乘非零常數 c | A 的某 row 全部 entry × c | b 對應 entry × c |
| ② 兩條方程互換 | A 的兩條 row 整條對調 | b 對應兩 entry 對調 |
| ③ 方程 i 加方程 j 的 c 倍 | A row i 各 entry += c × (row j 對應 entry) | b entry i += c × b entry j |

---

**✓ 合法操作 1：方程 (1) 乘 2**

方程組層：

- 原 (1): $2x_1 + 3x_2 + x_3 = 7$ → 乘 2 → $4x_1 + 6x_2 + 2x_3 = 14$
- 原 (2): $x_1 - x_2 + 4x_3 = 8$（不動）

A 與 b 同步動（**entry 級**）：

- A row 1：$(2, 3, 1) \to (4, 6, 2)$
- b entry 1：$7 \to 14$

$$A' = \begin{bmatrix} 4 & 6 & 2 \\ 1 & -1 & 4 \end{bmatrix}, \quad \mathbf{b}' = \begin{bmatrix} 14 \\ 8 \end{bmatrix}$$

**驗證 $\mathbf{x}^* = (1, 1, 2)$：** 新 (1') $4 + 6 + 4 = 14$ ✓，(2) $1 - 1 + 8 = 8$ ✓

**為何合法：** 等式兩邊同乘非零數**可逆**（再乘 $\tfrac{1}{2}$ 就能還原）→ 解集完全不變。

---

**✓ 合法操作 2：交換方程 (1) 與 (2)**

方程組層：方程順序對調，每條方程內容不變。

A 與 b 同步動：

$$A' = \begin{bmatrix} 1 & -1 & 4 \\ 2 & 3 & 1 \end{bmatrix}, \quad \mathbf{b}' = \begin{bmatrix} 8 \\ 7 \end{bmatrix}$$

**驗證 $\mathbf{x}^*$：** (1') $1 - 1 + 8 = 8$ ✓，(2') $2 + 3 + 2 = 7$ ✓

**為何合法：** 方程順序不影響解 → 解集完全不變。

---

**✓ 合法操作 3：方程 (2) 減去 ½ × 方程 (1)（消去 $x_1$）**

方程組層展開：

- ½ × (1)：$x_1 + \tfrac{3}{2}x_2 + \tfrac{1}{2}x_3 = \tfrac{7}{2}$
- 新 (2) = (2) − ½×(1)：

$$\underbrace{(1-1)}_{0}x_1 + \underbrace{(-1-\tfrac{3}{2})}_{-5/2}x_2 + \underbrace{(4-\tfrac{1}{2})}_{7/2}x_3 = \underbrace{8 - \tfrac{7}{2}}_{9/2}$$

化簡：$-\tfrac{5}{2}x_2 + \tfrac{7}{2}x_3 = \tfrac{9}{2}$

A 與 b 同步動：

- A row 1：$(2, 3, 1)$（不動）
- A row 2：$(1, -1, 4) \to (0, -\tfrac{5}{2}, \tfrac{7}{2})$
- b entry 1：$7$（不動）
- b entry 2：$8 \to \tfrac{9}{2}$

$$A' = \begin{bmatrix} 2 & 3 & 1 \\ 0 & -\tfrac{5}{2} & \tfrac{7}{2} \end{bmatrix}, \quad \mathbf{b}' = \begin{bmatrix} 7 \\ \tfrac{9}{2} \end{bmatrix}$$

**驗證 $\mathbf{x}^*$：** (1) $2+3+2=7$ ✓，新 (2) $-\tfrac{5}{2} + 7 = \tfrac{9}{2}$ ✓

**這個動作就是高斯消去法的一步**：$x_1$ 從第 2 式消失，剩下只關於 $x_2, x_3$ 的方程，變數逐步減少 → 最終可逐個解出。

**為何合法：** 操作可逆 — 新 (2) 再加上 ½×(1) 就還原回原 (2)；保留的原 (1) 加新 (2) 也能反推原 (1), (2)。→ 解集完全不變。

---

**❌ 破壞操作 1：方程 (1) 乘 0**

方程組層：原 (1) $2x_1 + 3x_2 + x_3 = 7$ 乘 0 → $0 = 0$（變成空泛恆等式）。

A 與 b 同步動：

$$A' = \begin{bmatrix} 0 & 0 & 0 \\ 1 & -1 & 4 \end{bmatrix}, \quad \mathbf{b}' = \begin{bmatrix} 0 \\ 8 \end{bmatrix}$$

新方程組：「$0 = 0$」（恆真）+「$x_1 - x_2 + 4x_3 = 8$」

**解集對比：**

| 系統 | 解集 | 維度 |
|---|---|---|
| 原系統 | 一條直線 $(1,1,2) + t(-13,7,5)$ | 1 維 |
| 新系統 | 平面 $\{(x_1,x_2,x_3): x_1-x_2+4x_3=8\}$ | 2 維 |

**反例**（新解但非原解）：$(0, -8, 0)$

- 新 (2): $0 - (-8) + 0 = 8$ ✓
- 原 (1): $0 + 0 + 0 = 0 \neq 7$ ✗

→ **解集從 1 維直線擴張到 2 維平面** ✗

**為何破壞：** 「乘 0」操作**不可逆** — 從 $0 = 0$ 無法反推回原 $2x_1 + 3x_2 + x_3 = 7$（資訊永久丟失）。

---

**❌ 破壞操作 2：只對 A 做消去動作，但 b 沒同步動**

對 A 做 $R_2 \to R_2 - \tfrac{1}{2}R_1$（合法操作 3 的 A 部分），但 b 保留 $(7, 8)^{\top}$ 不改：

$$A' = \begin{bmatrix} 2 & 3 & 1 \\ 0 & -\tfrac{5}{2} & \tfrac{7}{2} \end{bmatrix}, \quad \mathbf{b}' = \begin{bmatrix} 7 \\ \mathbf{8} \end{bmatrix} \text{（沒改！）}$$

新 (2)：$-\tfrac{5}{2}x_2 + \tfrac{7}{2}x_3 = 8$

**驗證 $\mathbf{x}^* = (1, 1, 2)$：** $-\tfrac{5}{2} + 7 = \tfrac{9}{2} \neq 8$ ✗

**$\mathbf{x}^*$ 不再是解** — 解集偏移到別處去了。

**為何破壞：** 方程 (2) − ½×(1) 後，「左邊變了，右邊也必須同步變」才是合法代數變形。左邊變右邊沒變 = **等式平衡破壞** — 這已經不是「對原方程的合法變形」，是憑空捏造一條新方程。

---

**❌ 破壞操作 3：把 A 的某兩個 entry 互換（非整 row 整 column）**

把 $a_{12} = 3$ 和 $a_{21} = 1$ 互換：

$$A_{bad} = \begin{bmatrix} 2 & \mathbf{1} & 1 \\ \mathbf{3} & -1 & 4 \end{bmatrix}$$

新方程組：

- (1'): $2x_1 + x_2 + x_3 = ?$
- (2'): $3x_1 - x_2 + 4x_3 = ?$

**驗證 $\mathbf{x}^* = (1, 1, 2)$：**

- (1') 左邊 = $2 + 1 + 2 = 5$（原 $b_1 = 7$ 不再相等）
- (2') 左邊 = $3 - 1 + 8 = 10$（原 $b_2 = 8$ 不再相等）

要讓 $\mathbf{x}^*$ 是新系統的解，b 得改成 $(5, 10)^{\top}$ — 這已經是**徹底不同的系統**。

**為何破壞：** 這個動作**沒有任何方程組層的對應** — 你做不到「對原方程組做某種合法變形」最後得到 (1'), (2')。它不是 (1), (2) 的任何加減乘除組合，是憑空在 entry 層亂改。

---

#### Step 2 加強的結論

$$\boxed{\text{對 A 的合法操作} \iff \text{方程組層存在可逆的代數變形對應}}$$

**合法**（解集完全不變）：

- ① 整條 row 乘非零常數（A 與 b 同步動）
- ② 兩條 row 整條對調（A 與 b 同步動）
- ③ 一條 row 加另一條的倍數（A 與 b 同步動）

**破壞**（解集斷裂）：

- ❌ row 乘 0（不可逆 → 解集擴張）
- ❌ 只動 A 不動 b（等式平衡破壞 → 解集偏移）
- ❌ 任意 entry 亂改 / 跨 row 互換 entry（不對應任何方程組變形）

**這條對應關係保證 A 物件化後仍代表原方程組。**

#### 暗線埋伏（等 Step 4 後再展開）

> 上述合法操作 ①②③ 看似是 3 條獨立規則，但其實它們會**全部統一為「Step 4 反推出來的 ◯ 規則」下的一種特殊運算結構**。等矩陣乘法 ◯ 在 Step 4 被反推出來後，我們會看到：
>
> 「對 A 做 ①②③ 合法操作」自動等同於「**在 A 左邊接一個小矩陣 $M$ 做 ◯ 運算**」 — 而且 $M$ 必須滿足一種「可逆」的代數條件。這條對應**會在後面的 [R03 矩陣乘法](#r03) 鏈兌現**，現在不需要先懂。

**Step 2 階段只需要記住：對 A 的合法操作 = 方程組層的合法代數變形（中學代數）。**

### Step 3: 尋找一個運算符號 ◯

我們希望寫一條短公式

$$A \mathbin{\bigcirc} \mathbf{x} = \mathbf{b}$$

讓它**機械地展開**得到原本所有 m 個方程。

**◯ 是未知的。** 我們現在要**反推**它必須長什麼樣子。

### Step 4: 閉合需求逼出 ◯ 的規則（具體 → 一般）

要還原第 i 個營養素的總量方程

$$b_i = a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n$$

主例題用熱量 $b_1$ 的具體數字看（A 第 1 row $(2, 3, 1)$ × 份量 $\mathbf{x} = (1, 1, 2)^{\top}$）：

$$b_1 = \underbrace{2}_{a_{11}} \cdot \underbrace{1}_{x_1} + \underbrace{3}_{a_{12}} \cdot \underbrace{1}_{x_2} + \underbrace{1}_{a_{13}} \cdot \underbrace{2}_{x_3} = 2 + 3 + 2 = 7$$

辨識結構 — 「**對位相乘再相加**」 — 這正是兩個向量的**點積**（[Q04 點積為什麼是分量相乘再相加](appendix-D-why.md#q04)）。

$$\boxed{b_1 = \underbrace{\begin{bmatrix} 2 & 3 & 1 \end{bmatrix}}_{\text{A 第 1 row}} \cdot \underbrace{\begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix}}_{\mathbf{x}} = 2(1) + 3(1) + 1(2) = 7}$$

同理 $b_2$：

$$b_2 = \begin{bmatrix} 1 & -1 & 4 \end{bmatrix} \cdot \begin{bmatrix} 1 \\ 1 \\ 2 \end{bmatrix} = 1(1) + (-1)(1) + 4(2) = 1 - 1 + 8 = 8 \ \checkmark$$

**一般化：對任意 m, n：**

$$\boxed{(A\mathbf{x})_i = \sum_{j=1}^{n} a_{ij} x_j = (\text{A 第 i row}) \cdot \mathbf{x}}$$

**這就是 (Mv1) $A\mathbf{x}$ 點積讀法 — 被閉合需求反推、不能是別的**。

**◯ = 矩陣 - 向量乘法**從 Step 4 開始正式存在。

### Step 5: 副產物 1 — 維度規則自動冒出

點積要兩個等長向量。主例題：

- A 第 1 row $(2, 3, 1)$ 長度 = **3**（= A 的 column 數 n）
- $\mathbf{x} = (1, 1, 2)^{\top}$ 長度 = **3**（= x 的 row 數）
- 等長 → 點積成立 ✓

**反例：x 改 4 維 $(1, 1, 2, 5)^{\top}$：**

- A 第 1 row 長度 3 ≠ x 長度 4
- 點積無定義 → $A\mathbf{x}$ 無定義 ✗

**結論：**

$$\boxed{\text{A 的 column 數} = \mathbf{x} \text{ 的 row 數}}$$

不是規定，是**「點積要能做」強制反推**的。

### Step 6: 副產物 2 — (Mv2) 線組合自動冒出

把 $\mathbf{b}$ 從 row 方向**重新組織**到 column 方向：

$$\mathbf{b} = \begin{bmatrix} 2x_1 + 3x_2 + x_3 \\ x_1 - x_2 + 4x_3 \end{bmatrix}$$

**把 $x_j$ 提到外面**（每個 $x_j$ 出現在每個 row 的第 j 項）：

$$\mathbf{b} = \begin{bmatrix} 2x_1 \\ x_1 \end{bmatrix} + \begin{bmatrix} 3x_2 \\ -x_2 \end{bmatrix} + \begin{bmatrix} x_3 \\ 4x_3 \end{bmatrix} = x_1 \begin{bmatrix} 2 \\ 1 \end{bmatrix} + x_2 \begin{bmatrix} 3 \\ -1 \end{bmatrix} + x_3 \begin{bmatrix} 1 \\ 4 \end{bmatrix}$$

$$\boxed{A\mathbf{x} = x_1 \cdot \mathbf{c}_1 + x_2 \cdot \mathbf{c}_2 + x_3 \cdot \mathbf{c}_3 \quad \text{(其中 } \mathbf{c}_j = \text{A 第 j column)}}$$

**驗證 with $\mathbf{x} = (1, 1, 2)^{\top}$：**

$$1\begin{bmatrix} 2 \\ 1 \end{bmatrix} + 1\begin{bmatrix} 3 \\ -1 \end{bmatrix} + 2\begin{bmatrix} 1 \\ 4 \end{bmatrix} = \begin{bmatrix} 2 + 3 + 2 \\ 1 - 1 + 8 \end{bmatrix} = \begin{bmatrix} 7 \\ 8 \end{bmatrix} \ \checkmark$$

**關鍵洞察：(Mv2) 不是另一條規則，是同一個 ◯ 規則的另一種展開方式。** 對應 [Q07 為什麼要有 2 個視角（點積 + 線性組合）](appendix-D-why.md#q07) 的根源。

### Step 7: 副產物 3 — 列空間 + rank

從 (Mv2)：所有可能 $\mathbf{b}$ 都形如 $x_1 \mathbf{c}_1 + x_2 \mathbf{c}_2 + x_3 \mathbf{c}_3$。

主例題 column：$\mathbf{c}_1 = (2, 1)^{\top}$, $\mathbf{c}_2 = (3, -1)^{\top}$, $\mathbf{c}_3 = (1, 4)^{\top}$。

**獨立性測試**：$\mathbf{c}_3$ 是不是 $\mathbf{c}_1, \mathbf{c}_2$ 的線組合？求 $\alpha, \beta$ 使 $\alpha \mathbf{c}_1 + \beta \mathbf{c}_2 = \mathbf{c}_3$：

$$\begin{cases} 2\alpha + 3\beta = 1 \\ \alpha - \beta = 4 \end{cases} \quad \to \quad \alpha = \beta + 4 \to 2(\beta+4) + 3\beta = 1 \to 5\beta = -7$$

$$\boxed{\beta = -\frac{7}{5}, \quad \alpha = \frac{13}{5}}$$

**驗證：**

$$\frac{13}{5}\begin{bmatrix} 2 \\ 1 \end{bmatrix} + \left(-\frac{7}{5}\right)\begin{bmatrix} 3 \\ -1 \end{bmatrix} = \begin{bmatrix} 26/5 - 21/5 \\ 13/5 + 7/5 \end{bmatrix} = \begin{bmatrix} 5/5 \\ 20/5 \end{bmatrix} = \begin{bmatrix} 1 \\ 4 \end{bmatrix} = \mathbf{c}_3 \ \checkmark$$

**所以 $\mathbf{c}_3$ 是冗餘的，rank(A) = 2**（3 個 column 但只 2 個獨立）。

**列空間 $\mathbf{C}(A) = \mathbb{R}^2$**（$\mathbf{c}_1, \mathbf{c}_2$ 線性獨立且共張 $\mathbb{R}^2$）→ 任何 $\mathbf{b} \in \mathbb{R}^2$ 都有解，但解不唯一（呼應 Step 2 算出的 1 維解集直線）。

**Rank-Nullity 驗證：**

$$\boxed{\dim \mathbf{C}(A) + \dim \mathbf{N}(A) = n \quad \to \quad 2 + 1 = 3 \ \checkmark}$$

對應 [Q08 四個基本子空間為什麼會自然冒出](appendix-D-why.md#q08) 與 [Q15 A=CR 列秩=行秩自然冒出](appendix-D-why.md#q15) 的根源。

### Step 8: 雙路閉合驗證

**(Mv1) 路徑：**

$$A\mathbf{x} = \begin{bmatrix} (2)(1) + (3)(1) + (1)(2) \\ (1)(1) + (-1)(1) + (4)(2) \end{bmatrix} = \begin{bmatrix} 7 \\ 8 \end{bmatrix}$$

**(Mv2) 路徑：**

$$A\mathbf{x} = 1\begin{bmatrix} 2 \\ 1 \end{bmatrix} + 1\begin{bmatrix} 3 \\ -1 \end{bmatrix} + 2\begin{bmatrix} 1 \\ 4 \end{bmatrix} = \begin{bmatrix} 7 \\ 8 \end{bmatrix}$$

兩條路徑**數值完全一致** — 因為它們是同一個 ◯ 規則的兩種展開方式。

### Step 9: 線性 vs 非線性邊界（公式對比）

**改成非線性問題：**

$$\begin{cases} 2x_1^2 + 3x_2 + x_3 = b_1 \\ x_1 - x_2 + 4x_3^2 = b_2 \end{cases}$$

**嘗試物件化：** $A = \begin{bmatrix} 2 & 3 & 1 \\ 1 & -1 & 4 \end{bmatrix}$（係數抽出來看似一樣）

**反例驗證**（用 $\mathbf{x} = (2, 1, 1)^{\top}$）：

| 計算方式 | 結果 |
|---|---|
| 矩陣 (Mv1) 點積 $A\mathbf{x}$ 第 1 分量 | $2(2) + 3(1) + 1(1) = 8$ |
| 原非線性方程 第 1 式 | $2(2)^2 + 3(1) + 1(1) = 8 + 3 + 1 = 12$ |
| 差異 | $12 - 8 = 4 \neq 0$ ✗ |

**矩陣語言無法還原非線性方程** — 它**只在「每個 $x_j$ 一次方」這個前提下閉合**。

非線性問題需要：

- **Taylor 展開**（在某點局部線性化 → 切平面用矩陣表達）
- **kernel trick**（透過 $\phi(\mathbf{x})$ 把非線性 lift 到高維線性）
- **神經網路**（線性層 + 非線性激活函數交替堆疊）

**全都是「矩陣框架 + 非線性配件」的混合**。

### Step 10: 昇華 — 完整反推鏈圖

$$\boxed{\text{線性問題（n 變數 m 條件）}} \xrightarrow{\substack{\text{合法操作} \\ \text{保持解集}}} \boxed{\text{物件化：A, x, b}} \xrightarrow{\substack{\text{尋找 ◯} \\ \text{還原所有方程}}} \boxed{\text{點積規則 = 唯一可能}}$$

$$\downarrow \text{副產物自動冒出}$$

$$\boxed{\text{維度規則}} \cdot \boxed{\text{(Mv2) 線組合}} \cdot \boxed{\text{列空間}} \cdot \boxed{\text{rank}}$$

**核心洞察：**

> 矩陣 - 向量乘法不是被「發明」的，它是線性問題物件化後**唯一自洽的還原機器**。所有矩陣演算法（高斯消去 / LU / QR / EVD / SVD）的正確性，根基都在「對 A 的操作 = 方程組層的合法代數操作」這個閉合對應上 — 此鏈在 [R03](#r03) 兌現「①②③ 合法操作 = 左乘可逆 M」的暗線。

### Step 11: R01 連結 R02-R07（鏈條樹）

| 後續鏈 | 從 R01 哪個副產物出發 | 反推主題 |
|---|---|---|
| [R02：外積 $\mathbf{u}\mathbf{v}^{\top}$](#r02) | (Mv2) 線組合 | 「秩 1 原子」反推 |
| [R03：矩陣乘法 AB](#r03) | (Mv1) + 合成 $(AB)\mathbf{x} = A(B\mathbf{x})$ | 函數合成反推 |
| [R04：列空間 / 零空間 / 4 子空間](#r04) | (Mv2) + rank | 「有解 / 唯一」反推 |
| [R05：A=CR](#r05) | (Mv2) + 獨立 column | rank 視覺化反推 |
| [R06：偽反 $A^{+}$](#r06) | R04 + SVD | rank-deficient 最優解反推 |
| [R07：(P4) 三明治](#r07) | R03 + 譜定理 | 視角切換 + 對角縮放反推 |

### Step 12: Strang 鎖核

> "The matrix $A$ contains all the information about the linear transformation $T$. The way we multiply $A$ times $\mathbf{x}$ — that's the way $T$ acts on $\mathbf{x}$."
>
> — Gilbert Strang, *Linear Algebra for Everyone*, §1.4

Strang 直白：**矩陣乘法的規則 = 線性變換的作用方式。不是規定，是反推。**

---

## R02: 反推外積 $\mathbf{u}\mathbf{v}^{\top}$（從「秩 1 原子」需求） {#r02}

### Step 0: 我們在做什麼

R01 反推了 (Mv1) $A\mathbf{x}$，並從中發現 **(Mv2) 線組合**讀法：$A\mathbf{x} = x_1\mathbf{c}_1 + x_2\mathbf{c}_2 + \cdots + x_n\mathbf{c}_n$。

注意到 (Mv2) 把 $A\mathbf{x}$ 寫成「**幾個有結構的東西累加**」的形式。R02 進一步追問：

> **如果反過來問：給定一個 m×n 矩陣 $M$，能不能把它拆成「最小、最簡單的單位」之和？這些「最小單位」長什麼樣？**

走完這條鏈會看到：**外積 $\mathbf{u}\mathbf{v}^{\top}$ 是矩陣世界的「原子」 — 它是被「最小可分離單位」需求反推出來的**。

### Step 1: 實際問題 — 構造「秩 1 原子」

**結果需求：** 我們想找一種**最簡單的非平凡矩陣** — 一個 m×n 矩陣，但「資訊含量」最小。

「資訊含量最小」的具體標準（從 R01 學到的 rank 概念）：

> 一個矩陣的「資訊含量」可用 **rank** 度量。最小非零 rank = 1。

**問題：** 怎麼**從零構造**一個 rank = 1 的 m×n 矩陣 $M$？

#### 主例題：從食譜資料造一個 rank 1 矩陣

接續 R01 食譜場景，假設我們現在只關心**單一營養素「熱量」對單一食材**「紅蘿蔔」的關係。

但我們有**多種紅蘿蔔（不同大小）** 與**多個盤子（不同份量）**：

- 紅蘿蔔 size 編號 1, 2, 3（mass = 10g, 20g, 30g 三種規格）
- 盤子份量 編號 1, 2（pieces = 4 顆, 7 顆兩種規格）

第 i 種紅蘿蔔的「單顆熱量」= 2 × mass_i（kcal）；第 j 種盤子的「總顆數」= pieces_j。

**問題：構造一個 3×2 矩陣 $M$，其中 $m_{ij}$ = 「第 i 種紅蘿蔔 × 第 j 種盤子的總熱量」。**

- $m_{11} = 2 \cdot 10 \cdot 4 = 80$ kcal
- $m_{12} = 2 \cdot 10 \cdot 7 = 140$ kcal
- $m_{21} = 2 \cdot 20 \cdot 4 = 160$ kcal
- $m_{22} = 2 \cdot 20 \cdot 7 = 280$ kcal
- $m_{31} = 2 \cdot 30 \cdot 4 = 240$ kcal
- $m_{32} = 2 \cdot 30 \cdot 7 = 420$ kcal

$$M = \begin{bmatrix} 80 & 140 \\ 160 & 280 \\ 240 & 420 \end{bmatrix}$$

**重要觀察：** $M$ 的每個 entry $m_{ij}$ 都可以**乾淨地拆成**「只依賴 i 的部分」× 「只依賴 j 的部分」：

$$m_{ij} = \underbrace{(2 \cdot \text{mass}_i)}_{u_i,\ \text{只跟 i 有關}} \cdot \underbrace{\text{pieces}_j}_{v_j,\ \text{只跟 j 有關}}$$

設 $\mathbf{u} = (20, 40, 60)^{\top}$（單顆熱量 2 × mass）、$\mathbf{v} = (4, 7)^{\top}$（顆數），則 $m_{ij} = u_i v_j$。

### Step 2: 第一步 — 物件化（兩個向量 + 矩陣）

把上述觀察抽象化 — $\mathbf{u}$ 收集「只跟 i 有關的因子」（單顆熱量 $2 \cdot \text{mass}_i$，隨紅蘿蔔 size 變動），$\mathbf{v}$ 收集「只跟 j 有關的因子」（盤子顆數 $\text{pieces}_j$，隨盤子規格變動）。**兩個向量是互相獨立的兩個輸入維度**：

$$\mathbf{u} = \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_m \end{bmatrix} \in \mathbb{R}^m, \quad \mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} \in \mathbb{R}^n$$

期望產出一個 m×n 矩陣 $M$，其 entry $m_{ij} = u_i v_j$（i, j 兩個獨立索引各自從 $\mathbf{u}, \mathbf{v}$ 取一個分量配對相乘）。

**這就是「rank 1 原子」的構造需求** — 任何能寫成「(只跟 i 有關) × (只跟 j 有關)」的矩陣都是 rank 1。

#### Step 2 加強：對 $\mathbf{u}, \mathbf{v}$ 的合法操作

不像 R01 我們不必對 $\mathbf{u}, \mathbf{v}$ 做高斯消去 — 但有一個值得注意的**對稱性合法操作**：

**✓ 合法操作：縮放對偶（$\mathbf{u} \to c\mathbf{u}$, $\mathbf{v} \to \tfrac{1}{c}\mathbf{v}$）**

$$m_{ij} = u_i v_j = (cu_i)\left(\tfrac{1}{c}v_j\right) = u'_i v'_j$$

→ 同一個 $M$ 可以由**無窮多對** $(\mathbf{u}, \mathbf{v})$ 構造（縮放對偶）。這是「秩 1 原子」的內在自由度。

**❌ 破壞操作：對 $\mathbf{u}$ 加常數 c（非縮放）**

$m'_{ij} = (u_i + c) v_j = u_i v_j + c v_j$ → $M' = M + c \cdot \mathbf{1}\mathbf{v}^{\top}$，多出一項 $\mathbf{1}\mathbf{v}^{\top}$ 是另一個秩 1 矩陣 — $M'$ rank 可能 ≤ 2 但**已經不是純 $\mathbf{u}\mathbf{v}^{\top}$**，破壞了「rank 1 原子」的純度。

### Step 3: 尋找一個運算符號 ◯

我們想寫一條短公式：

$$\mathbf{u} \mathbin{\bigcirc} \mathbf{v} = M$$

讓它**機械地產生** $m_{ij} = u_i v_j$。

**◯ 是未知的。** 注意：這次的 ◯ 是「**兩個向量產生一個矩陣**」的運算 — 跟 R01 ($A\mathbf{x}$) 不同（矩陣 + 向量產生向量）。

### Step 4: 閉合需求反推 ◯ 的規則

要還原 $m_{ij} = u_i v_j$（對所有 i, j），我們需要 ◯ 把 $\mathbf{u}$ 的第 i 個分量與 $\mathbf{v}$ 的第 j 個分量配對相乘。

**最自然的表達方式：** 把 $\mathbf{u}$ 寫成**直行**（column 向量），把 $\mathbf{v}$ 寫成**橫行**（row 向量 = $\mathbf{v}^{\top}$），然後**「直行 × 橫行」**：

$$\underbrace{\begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_m \end{bmatrix}}_{m \times 1} \cdot \underbrace{\begin{bmatrix} v_1 & v_2 & \cdots & v_n \end{bmatrix}}_{1 \times n} = \underbrace{\begin{bmatrix} u_1 v_1 & u_1 v_2 & \cdots & u_1 v_n \\ u_2 v_1 & u_2 v_2 & \cdots & u_2 v_n \\ \vdots & \vdots & & \vdots \\ u_m v_1 & u_m v_2 & \cdots & u_m v_n \end{bmatrix}}_{m \times n}$$

**為什麼是這個結構？** 因為 $m_{ij}$ 必須**只依賴 i 和 j 的索引**，沒有跨索引的求和（不像點積把所有索引加總成一個數）。**保留 i 和 j 為兩個獨立維度** = 直行 × 橫行的形狀規則。

主例題具體：

$$\mathbf{u}\mathbf{v}^{\top} = \begin{bmatrix} 20 \\ 40 \\ 60 \end{bmatrix} \begin{bmatrix} 4 & 7 \end{bmatrix} = \begin{bmatrix} 80 & 140 \\ 160 & 280 \\ 240 & 420 \end{bmatrix} = M \ \checkmark$$

**逐 entry 驗算 $m_{ij} = u_i v_j$：**

| (i, j) | $u_i \cdot v_j$ | $m_{ij}$ |
|---|---|---|
| (1, 1) | $20 \cdot 4 = 80$ | 80 ✓ |
| (1, 2) | $20 \cdot 7 = 140$ | 140 ✓ |
| (2, 1) | $40 \cdot 4 = 160$ | 160 ✓ |
| (2, 2) | $40 \cdot 7 = 280$ | 280 ✓ |
| (3, 1) | $60 \cdot 4 = 240$ | 240 ✓ |
| (3, 2) | $60 \cdot 7 = 420$ | 420 ✓ |

**這就是外積 $\mathbf{u}\mathbf{v}^{\top}$ 規則 — 被「秩 1 原子構造」反推、不能是別的**。

$$\boxed{(\mathbf{u}\mathbf{v}^{\top})_{ij} = u_i v_j}$$

### Step 5: 副產物 1 — 形狀規則自動冒出

從直行 × 橫行的結構：

- $\mathbf{u}$ 是 $m \times 1$（column 向量）
- $\mathbf{v}^{\top}$ 是 $1 \times n$（row 向量）
- 結果 $\mathbf{u}\mathbf{v}^{\top}$ 是 $m \times n$（矩陣）

**內維度** $1 = 1$（自動匹配，因為兩個都是「一條向量」）；**外維度** $m \times n$ 決定結果形狀。

注意這跟 R01 的維度規則（A 的 column 數 = $\mathbf{x}$ 的 row 數）是**同一條規則的特例** — 後面 R03 會看到它在 AB 中以一般形式出現。

### Step 6: 副產物 2 — 秩 1 自動冒出

$M = \mathbf{u}\mathbf{v}^{\top}$ 的**所有 column** 都是 $\mathbf{u}$ 的倍數：

$$M = \begin{bmatrix} v_1 \mathbf{u} & v_2 \mathbf{u} & \cdots & v_n \mathbf{u} \end{bmatrix}$$

主例題：

$$M = \begin{bmatrix} 4 \cdot \mathbf{u} & 7 \cdot \mathbf{u} \end{bmatrix} = \begin{bmatrix} 4 \cdot (20, 40, 60)^{\top} & 7 \cdot (20, 40, 60)^{\top} \end{bmatrix} = \begin{bmatrix} 80 & 140 \\ 160 & 280 \\ 240 & 420 \end{bmatrix} \ \checkmark$$

**所有 column 都是 $\mathbf{u}$ 的倍數 → 列空間 $\mathbf{C}(M)$ = $\mathbf{u}$ 一條直線（1 維）→ rank($M$) = 1。**

同理**所有 row 都是 $\mathbf{v}^{\top}$ 的倍數**（第 i 條 row 是 $u_i \mathbf{v}^{\top}$）→ 行空間 $\mathbf{C}(M^{\top})$ = $\mathbf{v}$ 一條直線（1 維）→ rank($M^{\top}$) = 1。

**呼應 R01 學到的「列秩 = 行秩」：** 兩個 1 維子空間呼應 rank 1 統一定義。

對應 [Q05 外積為什麼是「列 × 行 = 秩 1 矩陣」](appendix-D-why.md#q05)。

### Step 7: 副產物 3 — (Mv2) 線組合的「秩 1 拆解」視角

回頭看 R01 Step 6 的 (Mv2)：

$$A\mathbf{x} = x_1 \mathbf{c}_1 + x_2 \mathbf{c}_2 + \cdots + x_n \mathbf{c}_n$$

每一項 $x_j \mathbf{c}_j$ **本身就是一個秩 1 矩陣的 row-1 切片** — 但更深刻的形式是把 $A\mathbf{x}$ 看作矩陣乘法的特例（這要等 R03 才完整）。

**真正的拆解觀察：把矩陣 A 拆成秩 1 矩陣之和。**

對 R01 主例題 $A = \begin{bmatrix} 2 & 3 & 1 \\ 1 & -1 & 4 \end{bmatrix}$，可以拆成 3 個秩 1 矩陣（每個 column 配對一個基底 row）：

$$A = \begin{bmatrix} 2 \\ 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \end{bmatrix} + \begin{bmatrix} 3 \\ -1 \end{bmatrix}\begin{bmatrix} 0 & 1 & 0 \end{bmatrix} + \begin{bmatrix} 1 \\ 4 \end{bmatrix}\begin{bmatrix} 0 & 0 & 1 \end{bmatrix}$$

**驗算第一項：** $\begin{bmatrix} 2 \\ 1 \end{bmatrix}\begin{bmatrix} 1 & 0 & 0 \end{bmatrix} = \begin{bmatrix} 2 & 0 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ ✓

**3 項相加：** $\begin{bmatrix} 2 & 0 & 0 \\ 1 & 0 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 3 & 0 \\ 0 & -1 & 0 \end{bmatrix} + \begin{bmatrix} 0 & 0 & 1 \\ 0 & 0 & 4 \end{bmatrix} = \begin{bmatrix} 2 & 3 & 1 \\ 1 & -1 & 4 \end{bmatrix} = A$ ✓

**重大發現：** 任何 m×n 矩陣都可寫成「最多 n 個秩 1 矩陣之和」。這是 (MM4) 列乘行讀法的根源，也是 SVD 「奇異值降冪秩 1 累加」的源頭。

對應主章 [§4 (MM4) 列 × 行讀法](ch04-mat-mat.md) 和 [§6.5 SVD 秩 1 累加](ch06f-USV.md#vizscript-01)。

### Step 8: 雙路閉合驗證

**路徑 1：直接 entry 計算 $m_{ij} = u_i v_j$**

(R02 主例題已驗算 6 個 entry，全對)

**路徑 2：用 column 線組合視角 $M = [v_1 \mathbf{u} | v_2 \mathbf{u} | \cdots | v_n \mathbf{u}]$**

$$M = \begin{bmatrix} 4 \cdot \mathbf{u} & 7 \cdot \mathbf{u} \end{bmatrix} = \begin{bmatrix} 4 \cdot (20, 40, 60)^{\top} & 7 \cdot (20, 40, 60)^{\top} \end{bmatrix}$$

兩條路徑數值完全一致 ✓

### Step 9: 邊界 — 為什麼不能更小

**問：可以更小嗎？rank 0 矩陣（全零矩陣）算「原子」嗎？**

答：rank 0 = 零矩陣，是平凡情形（吸收元），不算「資訊單位」。**rank 1 才是最小非零原子**。

**問：能不能反過來把任何矩陣拆成「更原子」的單位（譬如 rank 0.5）？**

答：不能。**rank 是整數**（線性獨立 column 個數），沒有「rank 0.5」概念。秩 1 確實是分解的最細粒度。

### Step 10: 昇華 — 外積是矩陣世界的「原子」

$$\boxed{\text{兩個向量}\ \mathbf{u},\ \mathbf{v}} \xrightarrow{\substack{\text{尋找 ◯} \\ \text{產生 rank 1 矩陣}}} \boxed{\mathbf{u}\mathbf{v}^{\top}\ \text{= 直行 × 橫行}}$$

$$\downarrow \text{副產物自動冒出}$$

$$\boxed{\text{形狀規則}} \cdot \boxed{\text{rank 1}} \cdot \boxed{\text{矩陣秩 1 拆解（MM4 / SVD 之源）}}$$

**核心洞察：**

> 外積 $\mathbf{u}\mathbf{v}^{\top}$ 不是被「發明」的，它是「**最小可分離的非零矩陣資訊單位**」需求反推出來的唯一規則。整個矩陣理論（包括 (MM4) 列 × 行、A=CR、SVD 秩 1 累加）都建立在「**外積是矩陣世界的原子**」這個核心信念之上。

### Step 11: R02 連結 R03（鏈條樹）

R02 給 R03 鋪了重要的兩個底子：

| R02 給 R03 的工具 | R03 怎麼用 |
|---|---|
| 外積 $\mathbf{u}\mathbf{v}^{\top}$ 規則 | (MM4) 列 × 行讀法 = AB 拆成秩 1 之和 |
| 秩 1 拆解觀察 | AB 的所有讀法（行 / 列 / 行乘列 / 列乘行）都是同一個 (Mv1) ◯ 的延伸 |

### Step 12: Strang 鎖核

> "Rank 1 matrices are the building blocks of all matrices. Every matrix is a sum of rank 1 pieces. The simplest matrices are the most important."
>
> — Gilbert Strang, *Linear Algebra for Everyone*, §1.2

Strang 直白：**秩 1 矩陣是所有矩陣的積木。外積是這些積木的構造規則。**

---

## R03: 反推矩陣乘法 AB（從「函數合成」需求） {#r03}

> 🚧 **後續 session 補（預估 1 session）。**
>
> **預定鏈條：**
>
> - **Step 1 實際問題：** 兩個變換 $\mathbf{y} = B\mathbf{x}$、$\mathbf{z} = A\mathbf{y}$ 的合成（典型例：旋轉 + 縮放 / 變數替換 + 微分運算 / 編碼 + 解碼）
> - **Step 2 物件化 + Step 2 加強：** 兩個矩陣 A, B；引入「合成必須一致 $(AB)\mathbf{x} = A(B\mathbf{x})$」當作閉合需求；**兌現 R01 暗線：對 A 的合法操作 ①②③ 統一為「左乘可逆 M」**
> - **Step 4 反推：** $(AB)_{ij}$ 必須是 A 第 i row 與 B 第 j column 的點積
> - **Step 6-7 副產物：** AB 的 4 種讀法（行讀 / 列讀 / 行乘列 / 列乘行）+ 不可交換性 + 結合律
> - **Step 11 連結：** R04（列空間繼承）+ R07（三明治）

---

## R04: 反推列空間 / 零空間 / 4 子空間（從「有解 / 唯一」需求） {#r04}

> 🚧 **後續 session 補（預估 1 session）。**
>
> **預定鏈條：**
>
> - **Step 1 實際問題：** 給定 A, $\mathbf{b}$，問「$A\mathbf{x}=\mathbf{b}$ 有解嗎？解唯一嗎？」
> - **Step 4 反推：**「有解」反推出列空間 $\mathbf{C}(A)$；「唯一」反推出零空間 $\mathbf{N}(A)$
> - **Step 6 副產物：** 對偶必然 → 行空間 $\mathbf{C}(A^{\top})$、左零空間 $\mathbf{N}(A^{\top})$ 自動冒出
> - **Step 7 副產物：** rank-nullity 定理 + Big Picture 正交分解 → 解的完整結構（特解 + 零空間）

---

## R05: 反推 A=CR 分解（從「rank 視覺化最小拆解」需求） {#r05}

> 🚧 **後續 session 補（預估 0.5 session）。**
>
> **預定鏈條：**
>
> - **Step 1 實際問題：** 想用「最樸素」的方式視覺化 rank（不引入正交化、特徵值等高階工具）
> - **Step 4 反推：** C = A 的獨立 column 集；R = 把 A 寫成 C 的線組合的係數（即 RREF）
> - **Step 6 副產物：** 列秩 = 行秩自然冒出（C 是 m×r，R 是 r×n，rank 都是 r）
> - **Step 11 連結：** R01 (Mv2) 線組合 → CR 是「(Mv2) 的矩陣化精煉版」

---

## R06: 反推偽反矩陣 $A^{+}$（從「rank-deficient 仍要最優解」需求） {#r06}

> 🚧 **後續 session 補（預估 1 session）。**
>
> **預定鏈條：**
>
> - **Step 1 實際問題：** $A\mathbf{x}=\mathbf{b}$ 無解（$\mathbf{b} \notin \mathbf{C}(A)$）或 rank 不滿時，仍要找「最佳解」
> - **Step 2 物件化：** 4 種情形（一解 / 無窮多解 / 無解 / rank-deficient）統一處理
> - **Step 4 反推：** 用 SVD $A = U\Sigma V^{\top}$ 構造 $A^{+} = V\Sigma^{+}U^{\top}$（$\Sigma^{+}$ 把非零奇異值倒數，零值保留）
> - **Step 6 副產物：** 最小範數最優解 $\mathbf{x}^{*} = A^{+}\mathbf{b}$；對所有 4 情形統一 → Moore-Penrose 4 公理
> - **Step 11 連結：** [Q22 解 Ax=b 為什麼是核心](appendix-D-why.md#q22) 的終點

---

## R07: 反推 (P4) 三明治分解（從「視角切換 + 對角縮放」需求） {#r07}

> 🚧 **後續 session 補（預估 1 session）。**
>
> **預定鏈條：**
>
> - **Step 1 實際問題：** 某個變換 $T$ 在標準座標下很複雜，但**換個視角**就變成「純對角縮放」（譬如旋轉的特徵值是複數但物理意義是旋轉角度）
> - **Step 2 物件化：** 把「視角」物件化成可逆矩陣 P（換基底）；把「對角縮放」物件化成 $\Lambda$
> - **Step 4 反推：** $A = P\Lambda P^{-1}$（譜定理 / EVD）→ 一般化為 $A = U\Sigma V^{\top}$（SVD，雙端視角）
> - **Step 6 副產物：** 五大分解全部是「三明治」的不同強度（LU 弱 / QR 中 / EVD 強 / SVD 最強 / CR 最樸素）
> - **Step 11 連結：** [Q13 (P4) 三明治為什麼線代核心](appendix-D-why.md#q13)、[Q18 譜定理](appendix-D-why.md#q18)、[Q19 SVD](appendix-D-why.md#q19) 的鏈式整合

---

## R01-R07 與 Appendix D 22 Q&A 對照表

> 🚧 **R02-R07 全部完成後填。** 預期格式：每條鏈對應到 Appendix D 哪幾條 Q&A 的「② 設計過程還原」層，標出**互補關係**（D 從橫切面剖析，E 從縱向走一遍）。

---

## R01-R07 與主章 13 個運算規則對照表

> 🚧 **R02-R07 全部完成後填。** 預期格式：每條鏈對應主章哪個運算（如 R01 ↔ §3 (Mv1) / R02 ↔ §2 (Vv2) 外積 / R03 ↔ §4 (MM4) / ...），並寫上「主章如何用 callout 連到本附錄」。

---

## 修訂紀錄

- **S19** (2026-05-15) — Back 提出「逆向設計視角」全書第二骨架；確立 5 步反推骨架 + 22 條 Q&A 對偶式設計；R01 PoC 通過（食譜 2×3 主例題貫穿 / Step 2 加強「方程組層代數語言」/ 暗線埋伏在 R03 兌現）；R02 同 session 完成（食譜衍生 rank 1 矩陣構造，外積規則被「最小資訊單位」需求反推）；R03-R07 預留標題段，後續 session 補。
