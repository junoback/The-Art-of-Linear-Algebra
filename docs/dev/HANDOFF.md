# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** S08（§6.2 A=LU + §6.3 A=QR 完成，**主章 + 主章兩章 session 模式驗證**）
- **日期:** 2026-05-12
- **狀態:** `ch06c-LU.md`（654 行，3 VizMark：⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1，LU 雙視角 peeling/MM4 切換 + 單 pointer 指 ch04）+ `ch06d-QR.md`（541 行，3 VizMark：⭐⭐⭐ × 1 / ⭐⭐ × 1 / ⭐ × 1，Gram-Schmidt 動畫 + 3D 投影 + 單 pointer 指 ch05）完成；**S08 PNG 重核重大發現：LU1 無 `using` 標、LU2 標 `using MM4`、QR 標 `using P1` — `using XX` 跨章 pointer 標記譜系擴大至 MM4**；單 pointer VizScript 設計（PNG 標什麼就指什麼）確立；3D 投影視覺確立為 QR 章獨有需求；SOP §2.6 補「主章 + 主章模式 / 單 pointer 規律 / 3D 視窗必備 / using XX 譜系擴大」+ 版本 0.9；下次 S09 從 §6.4 QΛQᵀ + §6.5 SVD 開始（兩章 session 延續，SVD 預期是全書最長 ~700 行）

---

## 專案目標（最高層）

把 Kenji Hiranabe 的《The Art of Linear Algebra》（基於 Gilbert Strang《Linear Algebra for Everyone》的圖解筆記）轉換為**互動式 Python 視覺化教材**：

- 原書中的圖解（5 大矩陣分解：CR / LU / QR / QΛQ' / UΣV'、向量/矩陣運算的 4 種觀點、特徵值地圖、Matrix World）轉成 Python 互動視覺化
- 公式可調整參數即時看到結果（互動式）
- 保留原書的「直覺優先」教學風格

---

## 當前工作狀態

### 已完成
- [x] **S00** 從 GitHub clone 原 repo、確認內容、session 管理系統初始化
- [x] **S01** 整體 md 化規劃定版（10 session 路線圖）
- [x] **S01** 機械轉換：pandoc `.tex` → md（英文 624 行 / 簡中 601 行），位於 `docs/book/from-tex/`
- [x] **S01** 機械轉換：PDF → 純文字（pdftotext 英 861 / 簡中 657 行；ghostscript txtwrite 對照版 `*-gs.txt`），位於 `docs/book/from-pdf/`
- [x] **S01** EPS → PNG 全部 50 張轉檔完成（ghostscript），位於 `docs/book/figs-png/`（共 888 KB）
- [x] **S01** 撰寫 `docs/book/SCHEMA.md`（章節格式 + 四欄位圖片描述規範）
- [x] **S01** 撰寫 `docs/book/_merged.md`（進度追蹤表 + 章節↔圖檔對映）
- [x] **S01** 工具備齊：pandoc 3.8.3、pdftotext (poppler) 26.04、ghostscript 10.0、epstopdf
- [x] **S01.5** 補規劃：撰寫 `VIZ_SCHEMA.md`（VizMark 5 型 + VizScript 13 段 A-M 格式，含 800 字範例）+ 修訂 SCHEMA.md + 重寫 `_merged.md` 路線圖（S02-S11）
- [x] **S02** §1 Viewing a Matrix - 4 Ways：`ch01-viewing-matrix.md`（418 行）— 1 圖描述 + 2 VizMark + 2 VizScript（VizScript-01 ⭐⭐⭐ + VizScript-02 ⭐⭐，各 13 段 A-M 完整）
- [x] **S02** 全書術語慣例 B 派 → A 派切換（**column = 列直立 / row = 行橫躺**，與華文主流一致）+ `SCHEMA.md` §3.1 規範更新 + SOP_DRAFT.md §2.4 教訓記錄
- [x] **S03** §2 Vector × Vector - 2 Ways：`ch02-vec-vec.md`（497 行）— 1 圖描述 + 2 VizMark + 2 VizScript；驗證 ch01 範本可複用
- [x] **S03** SOP_DRAFT.md §2.8 對比 / 對偶結構章節寫作模式 + 全書視覺一致性錨點 + 版本 0.4
- [x] **S04** §3 Matrix × Vector - 2 Ways + 4-Subspaces：`ch03-mat-vec.md`（935 行）— 3 圖描述 + 4 VizMark + 4 VizScript（⭐⭐⭐ × 2 完整 / ⭐⭐ × 1 精簡 / ⭐ × 1 輪廓）
- [x] **S04** SOP_DRAFT.md §2.9 多 VizMark 分級策略 + 版本 0.5
- [x] **S05** §4 Matrix × Matrix - 4 Ways：`ch04-mat-mat.md`（849 行）— 1 圖含 4 子圖描述 + 4 VizMark + 4 VizScript：
  - **VizScript-01** ⭐⭐⭐ Tier 2 4 視角 tab 切換（13 段 A-M 完整 ~1000 字）
  - **VizScript-02** ⭐⭐⭐ Tier 3 MM4 秩 1 累加 + Mona Lisa SVD demo + 重排序對比 + 誤差曲線（13 段 A-M 完整 ~1200 字，**§6 SVD 鋪陳全書最強候選之一**）
  - **VizScript-03** ⭐⭐ Tier 1 維度檢核（精簡 13 段）
  - **VizScript-04** ⭐ Tier 1 MM1 walkthrough（輕量輪廓）
- [x] **S05** SOP_DRAFT.md §2.6 補 §4 耗時資料點（1h / 849 行）+ 新觀察「N-way 單圖章節需拆 N 個子圖獨立段」+ 「⭐⭐⭐ 劇本可選 Tier 2 / Tier 3」 + 版本 0.6
- [x] **S06** §5 Practical Patterns：`ch05-patterns.md`（830 行）— 4 張獨立圖描述（Pattern12 / Pattern11-22 / Pattern3 / Pattern4）+ 6 Pattern（P1/P2/P1'/P2'/P3/P4）+ 4 VizMark + 4 VizScript
- [x] **S06** SOP_DRAFT.md §2.6 補 §5 耗時資料點（1h / 830 行）+ 4 觀察 + 版本 0.7
- [x] **S07** §6 五大分解總覽：`ch06a-five.md`（331 行）— 5 大分解總表 + 視覺辨識指紋 + (MM4) 統一形式 + 升級鏈結構 + 適用矩陣對照 + Figure 6.0 四欄描述 + 1 VizMark Tier 1 + pointer dashboard
- [x] **S07** §6.1 A=CR：`ch06b-CR.md`（545 行）— 7 個數學要點段 + Figure 6.1 CR1 標 using P1 + Figure 6.2 CR2 標 using P2 + 3 VizMark（⭐⭐⭐ Tier 2 雙 pointer 設計指 ch04+ch05 / ⭐⭐ Tier 1 / ⭐ Tier 1）
- [x] **S07 PNG 重核重大發現：原書 CR1/CR2 圖明標 `using P1` / `using P2`** — §6.1–§6.5 跨章連結官方鐵證
- [x] **S07** SOP_DRAFT.md §2.6 補 S07 耗時資料點（2h / 876 行 / 兩章 session 模式）+ 4 觀察 + 版本 0.8
- [x] **S08** §6.2 A=LU：`ch06c-LU.md`（654 行）— 7 個數學要點段（定義 / (MM4) 連結 / 高斯消去 = 反向 peeling / 解 Ax=b 兩步法 / 三角結構推導 / 與其他分解關係 / 總結表）+ Figure 6.3 LU1（peeling，**無 using 標**）+ Figure 6.4 LU2（**標 using MM4**）+ 3 VizMark：
  - **VizScript-01** ⭐⭐⭐ Tier 2「LU 雙視角切換（peeling/MM4）+ 三色 rank 1 累加動畫」**單 pointer 指 [ch04 VizScript-02](docs/book/ch04-mat-mat.md#vizscript-02)**（因 LU2 標 MM4 而非 P1/P2）
  - **VizScript-02** ⭐⭐ Tier 1 「前代 + 後代解 $A\mathbf{x}=\mathbf{b}$」（精簡 13 段）
  - **VizScript-03** ⭐ Tier 1 「3×3 範例 walkthrough」（輕量逐步動畫）
- [x] **S08** §6.3 A=QR：`ch06d-QR.md`（541 行）— 7 個數學要點段（定義 / Gram-Schmidt 流程 / (P1) 連結反向公式 / $\mathbf{C}(A)=\mathbf{C}(Q)$ 不變量 / 最小平方法應用 / 與其他分解關係 / 總結表）+ Figure 6.5 QR 四欄描述（**標 using P1**）+ 3 VizMark：
  - **VizScript-01** ⭐⭐⭐ Tier 2「Gram-Schmidt 正交化動畫 + 3D 投影視覺 + (P1) 列拆解」**單 pointer 指 [ch05 VizScript-01](docs/book/ch05-patterns.md#vizscript-01)**（因 QR 標 P1 不標 MM4）
  - **VizScript-02** ⭐⭐ Tier 1 「3D 投影視覺」（精簡 13 段）
  - **VizScript-03** ⭐ Tier 1 「2×2 數字 walkthrough」（輕量逐步動畫）
- [x] **S08 PNG 重核重大發現：`using XX` 跨章 pointer 標記譜系擴大至 MM4** — LU1 無標、LU2 標 `using MM4`、QR 標 `using P1`；§6.4/§6.5 起步前必逐張 PNG 對 P1/P2/P3/P4/MM1/MM2/MM3/MM4 共 8 種候選重核
- [x] **S08** SOP_DRAFT.md §2.6 補 S08 耗時資料點（2.5h / 1195 行 / 主章 + 主章模式）+ 5 觀察（using XX 譜系擴大至 MM4 / 單 pointer 比雙 pointer 更常見 / 分解章篇幅由應用面廣度決定 / 3D 投影視覺是 QR 章獨有需求 / 主章 + 主章模式驗證可行）+ 版本 0.9

### 進行中
- 無，S08 已收尾

### 待辦（多 session 路線圖 v2 — 方案 A 整合 VizMark+VizScript）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S11）後，於 S12+ 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| ✅ S01 + S01.5 | 機械轉換 + 雙 Schema（章節 / 視覺化）+ 路線圖補規劃 | `from-tex/`、`from-pdf/`、`figs-png/`、`SCHEMA.md`、`VIZ_SCHEMA.md`、`_merged.md` |
| ✅ S02 | §1 Viewing a Matrix - 4 Ways | `ch01-viewing-matrix.md`（418 行，2 VizMark + 2 VizScript） |
| ✅ S03 | §2 Vector × Vector - 2 Ways | `ch02-vec-vec.md`（497 行，2 VizMark + 2 VizScript） |
| ✅ S04 | §3 Matrix × Vector - 2 Ways（含 4-Subspaces） | `ch03-mat-vec.md`（935 行，4 VizMark + 4 VizScript） |
| ✅ S05 | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md`（849 行，4 VizMark + 4 VizScript） |
| ✅ S06 | §5 Practical Patterns | `ch05-patterns.md`（830 行，4 VizMark + 4 VizScript） |
| ✅ S07 | §6 五大分解總覽 + §6.1 A=CR（兩章 session） | `ch06a-five.md`（331 行 + 1 VizMark）+ `ch06b-CR.md`（545 行 + 3 VizMark） |
| ✅ S08 | §6.2 A=LU + §6.3 A=QR（兩章 session 主章 + 主章模式） | `ch06c-LU.md`（654 行 + 3 VizMark）+ `ch06d-QR.md`（541 行 + 3 VizMark） |
| **→ S09** | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ（兩章 session 主章 + 主章模式延續） | `ch06e-QLQ.md`、`ch06f-USV.md` — **SVD 預期是全書最長 ~700 行** |
| S10 | Foreword + Conclusion + 附錄 | `front-foreword.md`、`back-conclusion.md`、`appendix-map-eigenvalues.md`、`appendix-matrix-world.md` |
| S11 | 整合 + 校對 + 統一 + `BOOK.md` + `VIZ-CATALOG.md` | 合併版書 + 視覺化候選池目錄 |
| S12+ | Python 視覺化技術棧決策 + 從 VIZ-CATALOG 挑題目開做 PoC | （延後到 S11 後再細規劃，預估 ~20 session）|

### S09 起步建議

1. **S09 是「主章 + 主章」兩章 session 模式延續 S08** — 預估 3.5h，共 ~1300 行（§6.4 QΛQᵀ ~600 行 + §6.5 SVD ~700 行，**SVD 是分解之王，全書最長**）
2. **起步前必做：對 PNG 重核 `using XX` 標記（依 S07/S08 教訓）** — 候選包含：
   - **§6.4 QΛQᵀ**：可能有 `EVD1.png`、`EVD2.png`、`AQLambdaQT.png`、`SymmetricSpec.png` 等 — 預期可能標 `using P3` 或 `using P4`（三明治 sandwich 結構），對應 ch05 (P3)/(P4) Pattern
   - **§6.5 SVD**：可能有 `SVD1.png`、`SVD2.png`、`USigmaVT.png` 等 — 預期可能標 `using P4`（三明治）或 `using MM4`（秩 1 累加 = SVD 截斷），分別對應 ch05 或 ch04
   - **8 種 `using XX` 候選：** P1 / P2 / P3 / P4 / MM1 / MM2 / MM3 / MM4
3. **§6.4 S=QΛQᵀ (`ch06e-QLQ.md`)**（~600 行）：
   - 限**對稱矩陣** $S$，特徵分解（EVD / spectral decomposition）
   - $S = Q\Lambda Q^{\mathrm{T}}$：$Q$ 特徵向量正交基底（正交矩陣）、$\Lambda$ 對角主元 = 特徵值 $\lambda_p$
   - **與 (MM4) 連結：** $S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$（$\lambda_p$ 縮放下的秩 1 之和）
   - **與 §5 (P4) 連結：** $Q \Lambda Q^{\mathrm{T}}$ 是「正交 × 對角 × 正交」三明治 = (P4) 的特例
   - 預期 PNG 可能標 `using P4`（或 `using MM4`）
   - VizScript-01 ⭐⭐⭐ Tier 2：對稱矩陣 EVD 動畫 + 譜分解視覺（特徵向量旋轉到對齊坐標軸 + 縮放 + 旋轉回原座標）+ 雙 pointer 指 ch04 + ch05
   - VizScript-02 ⭐⭐ Tier 1：對稱性視覺檢核
   - VizScript-03 ⭐ Tier 1：2×2 EVD walkthrough
4. **§6.5 A=UΣVᵀ (`ch06f-USV.md`)**（~700 行）：
   - **任意 $m \times n$ 矩陣** $A$，奇異值分解（SVD）
   - $A = U\Sigma V^{\mathrm{T}}$：$U$ 左奇異向量正交基底（$m \times m$）、$\Sigma$ 對角奇異值 $\sigma_p$ 降冪、$V$ 右奇異向量正交基底（$n \times n$）
   - **與 (MM4) 連結：** $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$（**全書最重要公式之一**，秩 1 截斷 = 低秩近似）
   - **與 §5 (P4) 連結：** $U \Sigma V^{\mathrm{T}}$ 是「正交 × 對角 × 正交」三明治 = (P4) 的核心
   - **與 ch04 VizScript-02 (Mona Lisa SVD demo) 完美對應 — 雙 pointer 候選**
   - 預期 PNG 可能多張對偶（左奇異視角 / 右奇異視角 / 4 subspaces 視角），標 `using P4` 或 `using MM4`
   - VizScript-01 ⭐⭐⭐ **Tier 3**（全書最高規格，SVD 是分解之王）：動畫展示 SVD 4 子空間（含 ch03 4-Subspaces 圖的視覺整合）+ Mona Lisa SVD 低秩近似 demo（與 ch04 VizScript-02 同源）+ 4 種應用切換（壓縮 / PCA / 降噪 / 推薦系統）
   - VizScript-02 ⭐⭐⭐ Tier 2：奇異值降冪視覺
   - VizScript-03 ⭐⭐ Tier 1：與 PCA 連結
   - VizScript-04 ⭐ Tier 1：2×2 SVD walkthrough
5. **遵 SOP §2.6 主章 + 主章兩章 session 模式 + 「PNG 標什麼就指什麼」單 pointer 策略** — §6.4/§6.5 都採此設計，但 SVD 因「秩 1 截斷 + 三明治」雙重連結，可能首次重啟雙 pointer 設計（同時指 ch04 + ch05）
6. **從 `from-tex/en.md` 抓 §6.4（line 430+）和 §6.5（line 507+）**
7. **3D 投影視覺在 §6.4 EVD 也適用** — 對稱矩陣 EVD 的「正交特徵向量」是 3D 視覺最強場景之一（橢球主軸對齊）；§6.5 SVD 也適用「4 subspace 視角」

### 工件清單（S09+ 撰寫前必讀）

| 檔案 | 用途 |
|---|---|
| `docs/book/SCHEMA.md` | 章節 md 結構 + 圖片四欄描述格式（A 派術語） |
| `docs/book/VIZ_SCHEMA.md` | VizMark 標記 + VizScript 13 段 A-M 格式（含 800 字範例） |
| `docs/book/_merged.md` | 章節進度追蹤 + 章節↔圖檔對映表 + VizMark 計數 |
| `docs/book/ch01-viewing-matrix.md` | **S02 成稿，A 派術語的參考範本**（單視角章節） |
| `docs/book/ch02-vec-vec.md` | **S03 成稿，對比 / 對偶結構章節範本**（多視角章節） |
| `docs/book/ch03-mat-vec.md` | **S04 成稿，多 VizMark + 多圖章節範本 + 4-Subspaces 標誌圖** |
| `docs/book/ch04-mat-mat.md` | **S05 成稿，N-way 單圖章節範本（1 圖含 N 子圖）+ VizScript-02 母模板**（§6 5 大分解每個都連回 (MM4)） |
| `docs/book/ch05-patterns.md` | **S06 成稿，多獨立小圖章節範本 + 「Tier 1 + pointer」策略首例** |
| `docs/book/ch06a-five.md` | **S07 成稿，§6 開門總覽範本**（短章節 + 1 VizMark Tier1+pointer dashboard） |
| `docs/book/ch06b-CR.md` | **S07 成稿，§6.x 分解主章節範本**（雙 pointer VizScript 設計 + 對偶兩張圖 CR1/CR2 + `using PX` 跨章標記） |
| `docs/book/ch06c-LU.md` | **S08 成稿，分解主章節範本（無對偶圖差異）**（雙視角切換 peeling/MM4 + 單 pointer 指 ch04 + `using MM4` 跨章標記） |
| `docs/book/ch06d-QR.md` | **S08 成稿，分解主章節範本（單圖 + 3D 視覺）**（Gram-Schmidt 動畫 + 3D 投影 + 單 pointer 指 ch05 + `using P1` 跨章標記） |
| `docs/book/from-tex/{en,zh}.md` | pandoc 轉換結果（含 LaTeX 公式原文）|
| `docs/book/from-pdf/{en,zh}.txt` | pdftotext 純文字（補 pandoc 缺漏）|
| `docs/book/figs-png/*.png` | 50 張 PNG 圖檔（vision-ready）|
| `docs/dev/sop/SOP_DRAFT.md` | §2.6 + §2.8 + §2.9 + S06/S07/S08 補「Tier 1 + pointer」+「雙 pointer」+「兩章 session 模式」+「主章 + 主章模式」+「單 pointer 規律」+「3D 視窗 in QR」 — **S09+ 直接沿用** |

---

## 關鍵決策記錄

| 日期 | 決策 | 原因 |
|------|------|------|
| 2026-05-11 | 啟用跨 session 管理系統 | 使用者明確表示這是長期跨多 session 專案 |
| 2026-05-11 | 不修改原 repo 的 LaTeX/PPT 檔案 | 原檔是書的成品，互動式版本應該是新增層而非取代 |
| 2026-05-12 | 全書 md 化路線：機械轉換 + 圖片詳細描述 | 原書本質是圖解，純文字 md 無法傳達內容，需逐圖寫描述 |
| 2026-05-12 | 描述語言：繁體中文，術語括號保留英文（例：列空間 (column space)） | 使用者偏好繁中，但保留英文術語便於對照原書與通用文獻 |
| 2026-05-12 | 範圍：英文版 + 簡中版兩語並做，跳過日文版 | 使用者選擇方案 2（雙語），日文版主要差異是翻譯不影響視覺化 |
| 2026-05-12 | 圖片描述格式採四欄位 schema：視覺結構/數學內容/直覺解讀/視覺化機會（VizMark） | 後三欄位對應未來 Python 視覺化的圖形、計算、互動三層 |
| 2026-05-12 | **S01.5 補規劃**：方案 A — 章節 session 整合「描述 + VizMark + VizScript」三類工作 | 視覺化劇本品質強烈依賴對圖的深度理解，分離反而會浪費；+3 session 屬可接受比例 |
| 2026-05-12 | **VizScript 細緻度：細版 ~800 字 / 個（13 段 A-M 固定格式）** | 目標是直接餵 LLM 生 Python 程式不需補充細節，避免 S12+ 實作時來回問細節 |
| 2026-05-12 | 新增 `VIZ_SCHEMA.md` + `VIZ-CATALOG.md`（S11 產出） | VizMark 散在各章便於閱讀；VIZ-CATALOG 集中彙整供 S12+ 挑題目實作 |
| 2026-05-12 | 章節切分微調：§5 獨立 1 session、§6 拆 3 session（總覽+CR / LU+QR / QΛQᵀ+UΣVᵀ）| 視覺化工作量讓每 session 章節密度降為 ~0.7 章 |
| 2026-05-12 | git origin 是上游 junoback repo，**收工 commit 留本地不 push** ~~已撤銷 (2026-05-12 S03 末)~~ | 防誤推到別人 repo；建議 fork 或抽出獨立 repo 後再 push |
| 2026-05-12 | **S03 末撤銷上條：確認 `junoback/The-Art-of-Linear-Algebra` GitHub repo 即為使用者本人（Back Kuo）的 fork，push 到 origin/main 安全** | 使用者直接授權；之後可正常 `git push` 不需再問 |
| 2026-05-12 | **S02 中途決策變更：術語慣例改採華文主流 A 派（column = 列直立 / row = 行橫躺）** | 與中國大陸、日本、多數 Python 中文文件、本書簡中譯本一致；台灣本土教科書傳統採 B 派正好相反，本書讀者若來自此背景需校準 |
| 2026-05-12 | SOP_DRAFT.md 新增「術語慣例必須在 S01 鎖死」教訓條 | S02 中途改 A 派付出整檔重寫 0.5h 成本；若拖到 S05+ 全書反轉成本會幾何級數膨脹 |
| 2026-05-12 | **S03 確立「全書視覺一致性錨點」（SOP §2.8）：配色 hex / cell 尺寸 / 動畫時間統一化** | S04+ 撰寫 VizScript 時直接套用，不重新發明，除非特殊章節（如 SVD 需要 colormap 表達 σ 大小）才允許偏離 |
| 2026-05-12 | **S03 確立「對比 / 對偶結構章節寫作模式」：§ 數學要點 加對比段 + 直覺段提煉記憶口訣** | §3（dot way vs combination way）、§4（4 ways）、§6（5 大分解）均適用同一格式，減少每章設計成本 |
| 2026-05-12 | **S04 確立「多 VizMark 章節分級寫作策略」（SOP §2.9）：⭐⭐⭐ 完整 13 段 / ⭐⭐ 精簡 / ⭐ 輪廓** | ch03 4 個 VizMark 若全寫 800 字會膨脹到 1300+ 行失焦；分級後 935 行可控 |
| 2026-05-12 | **S04 確立「4-Subspaces 圖是全書視覺化最高 priority 之一（⭐⭐⭐ Tier 3）」** | Strang 兩塊大餅圖是線性代數核心定理（rank-nullity / 投影 / SVD）的視覺載體；VizScript-02 估 3 session 實作，是 §6 SVD 預先鋪陳的關鍵互動 |
| 2026-05-12 | **S05 確立「N-way 單圖章節寫作模式」（SOP §2.6 補）：1 張圖含 N 子圖時，圖描述段需把每個子圖拆獨立段** | ch04 Figure 4.1 是 4 子圖 (MM1/MM2/MM3/MM4) 2×2 排版，每子圖 ~15 行獨立段描述。配合 §2.9 分級策略，849 行控制良好 |
| 2026-05-12 | **S05 確立「⭐⭐⭐ 劇本可選 Tier 2 或 Tier 3」** | ch04 VizScript-01 (4 視角切換) 寫成 Tier 2（1.5 session）、VizScript-02 (MM4 + Mona Lisa SVD demo) 寫成 Tier 3（2.5 session）。S12+ 時間預算決定要實作幾支 Tier 3 |
| 2026-05-12 | **S05 確立「§4 (MM4) 是 §6 五大分解的視覺基石」** | $A = CR / LU / QR$ / $S = Q\Lambda Q^{\mathrm{T}}$ / $A = U\Sigma V^{\mathrm{T}}$ 都可用 (MM4) 展開成「秩 1 之和」；§6 5 章寫作時必引 §4 (MM4) 作對應，**VizScript-02 是 SVD 的視覺前置** |
| 2026-05-12 | **S06 教訓：HANDOFF 章節描述漏 P4** — 起步前必須對著原書 PNG 重核 Pattern/Figure 數量，不能信任前 session 的記憶 | 原書 §5 有 4 張圖 6 個 Pattern（P1/P2/P1'/P2'/P3/P4），HANDOFF 只列 5 個。下次 §6 5 章前需逐章對 PNG 確認分解數與圖數 |
| 2026-05-12 | **S06 確立「Tier 1 + pointer」省篇幅策略**（SOP §2.6 補）：當章節 VizMark 與「全書旗艦劇本」（如 ch04 VizScript-02 SVD）功能重疊時，本章只寫 Tier 1 + 跳轉按鈕指向旗艦劇本 | ch05 VizScript-03 (P4) 採此策略，節省 ~200 行 + S12+ 工時。§6 5 大分解每章都可重用：每章只寫各分解的「特殊性質」demo（正交 / 對稱 / 三角等），(MM4) 累加 demo 全部 pointer 到 ch04 VizScript-02 |
| 2026-05-12 | **S06 確立「對偶 Pattern 用對偶總表呈現」** — 兩兩對偶結構（如 (P1)↔(P2)、(P1')↔(P2')）用 3 列 × 4 欄對偶總表寫，而非兩兩獨立寫描述 | 節省 ~40% 篇幅且閱讀時更易對照。§6 5 大分解中如有對偶結構（如 $LU$ 與 $L^{\mathrm{T}}D L$）可複用 |
| 2026-05-12 | **S07 確立「兩章 session 模式」**（SOP §2.6 補）：總覽短章節（§6、§6.x）+ 主章節合併成一個 session 處理 | §6 五大分解總覽單獨一個 session 太浪費（331 行），與 §6.1 合 session 後 876 行 / 2h，比兩個獨立 session 省 0.5h。S08/S09 也採兩章模式（LU+QR / QΛQᵀ+SVD）|
| 2026-05-12 | **S07 重大發現：原書 PNG `using PX` 標記是跨章連結官方鐵證** — CR1.png 標 `using P1`、CR2.png 標 `using P2`，§5 Pattern 直接連到 §6.1 | §6.2–§6.5 起步前必逐張 PNG 核對是否有 `using PX` 標記。預期：LU1/LU2 可能標 (P1)(P2) 或 (MM4)；QR 可能標 (P1) Gram–Schmidt；QΛQᵀ/SVD 可能標 (P3)(P4) 三明治。確認後 VizScript 採對應的 pointer 設計 |
| 2026-05-12 | **S07 確立「雙 pointer VizScript 設計」** — 同一 VizScript 可同時指向 ch04 VizScript-02（看 (MM4) 累加）+ ch05 VizScript-01（看 (P1)(P2) 對角特例） | ch06b VizScript-01 首例驗證可行 |
| 2026-05-12 | **S07 確立「對偶兩張圖（列視角 + 行視角）是 §6.1–§6.5 全書一致模式」** | CR1(列) + CR2(行) 對偶展示「列秩 = 行秩」；預期 §6.2 LU1/LU2、§6.4 EVD、§6.5 SVD 都有類似對偶 |
| 2026-05-12 | **S08 重大發現：`using XX` 跨章 pointer 標記譜系擴大至 MM4** — LU1 無 using 標、LU2 標 `using MM4`、QR 標 `using P1` | S07 只發現 P1/P2，S08 補上 MM4 — 跨章 pointer 不只連 ch05 (P1-P4)，也連 ch04 (MM1-MM4)。S09 起步必對 8 種候選逐張 PNG 重核 |
| 2026-05-12 | **S08 確立「單 pointer 比雙 pointer 更常見」規律** — PNG 標什麼 `using XX`，VizScript 就指對應章；不強行加多 pointer | LU 章標 MM4 只指 ch04、QR 章標 P1 只指 ch05；S07 ch06b 雙 pointer 是特例（CR 兩張對偶圖一張標 P1 一張標 P2 才合理採雙 pointer）。S09 SVD 章因「秩 1 截斷 + 三明治」雙重連結可能再現雙 pointer |
| 2026-05-12 | **S08 確立「分解章篇幅由『應用面廣度』決定」** — LU 654 行 > CR 545 行 ≈ QR 541 行 | LU 含解 Ax=b 兩步法、QR 含最小平方法、CR 含列秩=行秩證明；應用面越廣篇幅越長。SVD（含壓縮 / PCA / 降噪 / 推薦）預期 ~700 行為全書最長 |
| 2026-05-12 | **S08 確立「3D 投影視覺是 QR 章獨有需求」** — Gram-Schmidt 投影幾何意義在 2D 不夠豐富 | QR VizScript-01 必含 3D 視窗（matplotlib 3D 或 plotly 3D）；S09 EVD 章也適用「對稱譜 → 橢球主軸」3D 視覺、SVD 章也適用「4 subspaces」3D 視覺。對 S12+ 工件清單影響：3D 渲染棧成 §6 必備 |
| 2026-05-12 | **S08 確立「主章 + 主章兩章 session 模式」** — S07 是「總覽 + 主章」（短+長），S08 升級為「主章 + 主章」（長+長） | 兩個獨立分解主章放同一 session 完全可行，2.5h / 1195 行比兩 session 預估省 0.5h。S09（QΛQᵀ + SVD）也用此模式但預期 3.5h / 1300 行（SVD 700+ 行為全書最長）|

---

## 檔案變更追蹤

### S00 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/dev/HANDOFF.md | 新增 | Session 交接文件 |
| docs/dev/SESSION_INDEX.md | 新增 | Session 索引 |
| docs/dev/CURRENT_SESSION.log | 新增 | 即時記錄 |
| docs/dev/sop/SOP_DRAFT.md | 新增 | SOP 草稿 |

### S01 + S01.5 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/SCHEMA.md | 新增 | 章節 md 結構 + 圖片四欄描述格式 |
| docs/book/VIZ_SCHEMA.md | 新增（S01.5） | VizMark 標記 + VizScript 13 段細緻劇本格式 |
| docs/book/_merged.md | 新增 / 重寫（S01.5）| 章節進度追蹤 + 章節↔圖檔對映 + VizMark 計數欄 |
| docs/book/from-tex/{en,zh}.md | 新增 | pandoc 轉換 |
| docs/book/from-pdf/{en,zh}.txt | 新增 | pdftotext 純文字 |
| docs/book/figs-png/*.png | 新增 | 50 張 PNG |

### S02–S07 新增/修改的檔案
- S02：`ch01-viewing-matrix.md`（418 行）
- S03：`ch02-vec-vec.md`（497 行）
- S04：`ch03-mat-vec.md`（935 行）
- S05：`ch04-mat-mat.md`（849 行）
- S06：`ch05-patterns.md`（830 行）
- S07：`ch06a-five.md`（331 行）+ `ch06b-CR.md`（545 行）
- 每 session 同時更新 _merged.md / SOP_DRAFT.md / CURRENT_SESSION.log / SESSION_INDEX.md

### S08 新增/修改的檔案
| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/ch06c-LU.md | 新增 | **§6.2 A=LU：654 行**，7 個數學要點段（含解 Ax=b 兩步法 + peeling 遞迴）+ Figure 6.3 LU1 (peeling 無 using) + Figure 6.4 LU2 (標 `using MM4`) + 3 VizMark：⭐⭐⭐ Tier 2 LU 雙視角切換單 pointer 指 ch04 / ⭐⭐ Tier 1 前代+後代解方程 / ⭐ Tier 1 3×3 範例 walkthrough |
| docs/book/ch06d-QR.md | 新增 | **§6.3 A=QR：541 行**，7 個數學要點段（含 Gram-Schmidt + 最小平方法）+ Figure 6.5 QR (標 `using P1`) + 3 VizMark：⭐⭐⭐ Tier 2 Gram-Schmidt 動畫 + 3D 投影視覺單 pointer 指 ch05 / ⭐⭐ Tier 1 3D 純投影 / ⭐ Tier 1 2×2 數字 walkthrough |
| docs/book/_merged.md | 修改 | S08 標記 [x]，VizMark 計數「LU 1/1/1 + QR 1/1/1」（合計 ⭐⭐⭐ × 2 / ⭐⭐ × 2 / ⭐ × 2）|
| docs/dev/sop/SOP_DRAFT.md | 修改 | §2.6 補 S08 耗時資料點（2.5h / 1195 行 / 主章 + 主章模式）+ 5 觀察 + 版本記錄追加 0.9 |
| docs/dev/CURRENT_SESSION.log | 修改 | S08 啟動 + 即時記錄 + 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S08 一行 |

---

## 技術筆記

### Repo 原始內容概覽
- **LaTeX 主檔**：`The-Art-of-Linear-Algebra.tex`（英文）、`-j.tex`（日文）、`-zh-CN.tex`（簡中）
- **編好的 PDF**：三種語言版本均已存在
- **圖檔來源**：`Illustrations.pptx`（PowerPoint），透過 makefile 流程印成 PS → EPS → 嵌入 LaTeX

### 互動式版本技術選項（S12+ 決策，目前傾向）
| 方案 | 優點 | 缺點 |
|------|------|------|
| **Marimo + matplotlib + marimo.ui**（S02–S08 VizScript 首選） | 反應式 notebook、純 Python、可匯出 HTML | 較新生態系較小 |
| Streamlit + Plotly | 部署成網頁簡單、互動流暢 | 不適合 notebook 形式閱讀 |
| Jupyter + ipywidgets + matplotlib | 標準、容易分享 .ipynb | 互動效能一般、需要 kernel |
| Plotly + Dash | 視覺化品質最高 | 學習曲線較陡 |
| Manim | 動畫效果最好（3Blue1Brown 同款） | 不互動、是動畫腳本 |
| 純 HTML + JS（D3 / Three.js） | 任何瀏覽器可開 | 跳脫 Python 生態 |

**S08 觀察（3D 渲染棧成 §6 必備）：** QR 章 VizScript-01 必含 3D 視窗展示 Gram-Schmidt 投影；§6.4 EVD 章預期也需 3D（對稱矩陣的橢球主軸對齊）；§6.5 SVD 章預期需 3D（4 subspaces）。**結論：S12+ 必確認技術棧支援 3D 視覺化**：matplotlib 3D（基本但靜態）/ plotly 3D（流暢但較重）/ Three.js（純 web 但脫離 Python 生態）。**最可能選擇：Marimo + plotly 3D**（反應式 + 3D 流暢 + 純 Python）。

### 全書術語慣例（A 派 — 華文主流）

| 英文 | 中文 | 視覺方向 |
|---|---|---|
| matrix | 矩陣 | — |
| row | 行 | 橫躺 |
| column | 列 | 直立 |
| row vector | 行向量 | 橫躺 |
| column vector | 列向量 | 直立 |
| row space | 行空間 $\mathbf{C}(A^{\mathrm{T}})$ | — |
| column space | 列空間 $\mathbf{C}(A)$ | — |
| nullspace | 零空間 $\mathbf{N}(A)$ | — |
| left nullspace | 左零空間 $\mathbf{N}(A^{\mathrm{T}})$ | — |
| rank | 秩 | — |
| subspace | 子空間 | — |
| basis | 基底 | — |
| linear combination | 線性組合 | — |
| dot product / inner product | 點積 / 內積 | — |
| outer product | 外積（→ 秩 1 矩陣）| — |
| factorization | 分解 | — |
| eigenvalue / eigenvector | 特徵值 / 特徵向量 | — |
| singular value | 奇異值 | — |
| perpendicular / orthogonal | 正交 / 垂直 | — |
| orthogonal complement | 正交補 | — |
| diagonal matrix | 對角矩陣 | 藍點對角排列、非對角位置留白 |
| row reduced echelon form (RREF) | 行階梯形（列簡化形）矩陣 | — |
| identity matrix | 單位矩陣 | — |

**矩陣尺寸：** $A \in \mathbb{R}^{m \times n}$ 表示 **$m$ 行 $n$ 列**（$m$ rows, $n$ columns）。$m$ = 行數、$n$ = 列數。

**矩陣乘法形狀：** $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$AB = C \in \mathbb{R}^{m \times n}$。**內維 $k$ 必須對齊**。

### 全書視覺一致性錨點（S03 確立，S08+ 補 3D + 金色主元 + 黃色中間結果）

- **配色 hex：** 綠（列 / 直立 / 正交向量）`#2ca02c`、粉紅 / 紅（行 / 橫躺 / 投影向量）`#d62728`、藍點（個別數字 / 對角元素 / $R$ 上三角元素）`#1f77b4`、灰填充 `#cccccc`（原始向量 / 已剝離元素）、子空間半透明 alpha 0.3、紫色（特徵基底 / 動態系統 / CR 第 3 列 / 退化警示）`#9467bd`、橙色（CR 第 2 列 / 接近依賴警示）`#ff7f0e`、**金色 `#FFD700`（S08 新增）**：主元 / 當前正在處理的列、**黃色（S08 新增）**：中間結果 $\mathbf{w}_p$（減投影後未單位化）
- **cell 尺寸：** 預設 60×60 px，極小 80×80（$m=n=2$）、極大 48×48（$m=n=6$）
- **3D 視窗尺寸：** 預設 600×480 px、視角 elev=25° azim=-60°（S08 QR 章 VizScript-01 / VizScript-02 必備）
- **動畫時間：** 視角切換 600–800ms、平行性高亮淡入 200ms、子空間維度變化 600ms、飛行軌跡 700ms、秩 1 累加 400ms / 項、緩動 ease-in-out、**peeling 動畫 600ms / 楔形（S08）**、**Gram-Schmidt 減投影 500ms / 投影（S08）**
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1，維度 $m, n \in [2, 6]$（3D 限 $\{2, 3\}$、SVD demo 64×64 像素）；對角元素 $d_p \in [-3, 3]$ 步進 0.5
- **N-way 切換動畫：** 多視角 tab 切換時 800ms 動畫含「色塊重排 + 重染色 + 公式同步」三層
- **對角矩陣表現：** 藍圓點直徑 12–14px 沿對角線排列、**非對角位置完全留白不畫 0**、$d_p$ 改變時藍點半徑 ∝ $|d_p|$
- **動態系統軌跡：** 軌跡藍漸變（淡 → 深 = 時間順序）、當前點紫實心 8px、特徵向量綠箭頭
- **CR 三色標記（S07 新增）：** $A$ 的列 1 = 藍 / 列 2 = 橙 / 列 3 = 紫；對應 $R$ 的對應行用相同色標。退化矩陣顯示「→ 0」淡出動畫
- **LU 楔形視覺（S08 新增）：** 楔形 $p$ 大小 ∝ 殘餘子矩陣 $A_p$ 範圍（第 1 個滿格、第 2 個右下 (n-1)×(n-1)、第 3 個右下 (n-2)×(n-2)...）；綠色直條代表 $\mathbf{l}_p$、粉紅橫條代表 $\mathbf{u}^*_p$
- **QR 上三角藍點（S08 新增）：** $R$ 用藍點 + 上三角形狀排列展示，下三角區域留白
- **跨章跳轉按鈕（S07 新增 / S08 補）：** 白底深綠邊框 + 「→」字樣，hover 填色 `#2ca02c`；按鈕分三類「→ (MM4) 累加」（指 ch04 VizScript-02）/「→ (P1)(P2) 對角」（指 ch05 VizScript-01）/「→ 解方程 demo」（章內跳轉）；單 pointer / 雙 pointer 視 PNG `using XX` 標記決定

### 章節撰寫速度資料點（S08 更新）

- **S02 §1（含 A 派切換重寫 0.5h）：** 1.5h / 418 行 / 2 VizMark
- **S03 §2（ch01 範本可複用）：** 1h / 497 行 / 2 VizMark
- **S04 §3（4 VizMark 分級策略）：** 1.5h / 935 行 / 4 VizMark
- **S05 §4（1 圖含 4 子圖 + 4 VizMark）：** 1h / 849 行 / 4 VizMark
- **S06 §5（4 圖各獨立 + 6 Pattern + 4 VizMark）：** 1h / 830 行 / 4 VizMark
- **S07 §6 總覽 + §6.1（兩章 session）：** 2h / 876 行（331 + 545）/ 4 VizMark（1 + 3）— **兩章 session 模式首次驗證**
- **S08 §6.2 LU + §6.3 QR（兩章主章模式）：** 2.5h / 1195 行（654 + 541）/ 6 VizMark（3 + 3）— **主章 + 主章模式驗證 + 3D 渲染棧導入**
- **預估後續：** §6.4 QΛQᵀ 1.5h / §6.5 SVD 2h（S09 共 3.5h 最重，~1300 行，SVD ~700 行是全書最長）

### §4 (MM4) 與 §6 五大分解的鋪陳對應（S05 新增，S06/S07/S08 補強）

| §6 分解 | (MM4) 形式 | VizScript 結構複用 | PNG `using XX` 標記（S07/S08 確認） |
|---|---|---|---|
| $A = CR$ | $A = \sum_p \mathbf{c}_p \mathbf{r}^*_p$（$r$ 項） | ch04 VizScript-02 + ch05 VizScript-01 **雙 pointer** | **CR1 標 P1、CR2 標 P2**（S07 確認）|
| $A = LU$ | $A = \sum_p \mathbf{l}_p \mathbf{u}^*_p$（$n$ 項） | ch04 VizScript-02 **單 pointer**（強調下三角 × 上三角） | **LU1 無標、LU2 標 MM4**（S08 確認）|
| $A = QR$ | $A = \sum_p \mathbf{q}_p \mathbf{r}^*_p$（$n$ 項） | ch05 VizScript-01 **單 pointer**（強調 $\mathbf{q}_p$ 正交） | **QR 標 P1**（S08 確認）|
| $S = Q\Lambda Q^{\mathrm{T}}$ | $S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$ | ch04 VizScript-02 + ch05 VizScript-02/03 三明治 **雙 pointer** 候選 | EVD 待 S09 確認（預期 P4 或 MM4）|
| $A = U\Sigma V^{\mathrm{T}}$ | $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$ | ch04 VizScript-02 完整繼承 + ch05 VizScript-02/03 三明治 **雙 pointer** 候選 | SVD 待 S09 確認（預期 P4 + MM4 雙標）|

**結論（S08 升級版）：** ch04 VizScript-02（MM4 秩 1 累加 + Mona Lisa SVD demo）+ ch05 VizScript-01/02/03 + ch06b VizScript-01（雙 pointer）+ ch06c VizScript-01（LU 雙視角單 pointer）+ ch06d VizScript-01（QR Gram-Schmidt 3D 單 pointer）= §6.4–§6.5 兩章 VizScript 的完整母模板組合。**S09 寫作時：**
1. 各章 (MM4) 累加 demo 一律 pointer 到 ch04 VizScript-02
2. (P3)(P4) 三明治 demo 一律 pointer 到 ch05 VizScript-02/03（若 PNG 標 `using P3/P4`）
3. SVD VizScript-01 可能採 **Tier 3**（與 ch04 VizScript-02 同級，全書最長劇本），含「壓縮 / PCA / 降噪 / 推薦」4 應用切換
4. EVD VizScript-01 預期 Tier 2 含 3D「橢球主軸對齊」動畫（譜分解的幾何直覺）
5. **S12+ 實作 ch04 VizScript-02 + ch05 VizScript-01/02/03 + ch06b/c/d VizScript-01 後，§6.4–§6.5 兩章 VizScript 可加速實作 80–85%**（比 S07 估的 70-80% 還高，因 LU/QR 母模板再補強）

---

## 新 Session 開始時的指令

```
請先讀取以下檔案恢復 context：
1. docs/dev/HANDOFF.md — 上次 session 狀態（本檔）
2. docs/dev/SESSION_INDEX.md — 歷史 session 列表
3. docs/dev/CURRENT_SESSION.log — 上一次 session 即時記錄
4. docs/book/SCHEMA.md + docs/book/VIZ_SCHEMA.md — 雙 Schema 規範（A 派術語）
5. docs/book/ch01–ch05 + ch06a–ch06d — 9 套範本：單視角 / 對比結構 / 多圖多 VizMark / N-way 單圖 / 多獨立小圖 / Tier1+pointer 總覽 / §6.x 主章節對偶兩圖 / 分解主章節無對偶差異 / 分解主章節單圖 3D
6. docs/dev/sop/SOP_DRAFT.md §2.6 補「主章 + 主章模式 / 單 pointer 規律 / 3D 視窗在 QR / 4 種 `using XX` 標記候選」 + §2.8 全書視覺錨點 + §2.9 多 VizMark 分級策略
然後繼續「待辦」中的第一項任務（S09 §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ — 兩章 session「主章 + 主章」模式延續，起步前對 EVD/SVD 相關 PNG 核對 8 種 using XX 標記候選；SVD 預期是全書最長 ~700 行）。
```
