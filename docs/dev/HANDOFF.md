# 跨 Session 交接文件 (Handoff Document)

> **用途：** 每個 session 結束時更新此檔案，下一個 session 開始時讀取以恢復 context。
> **更新者：** Claude（每次 session 結束前自動更新）

---

## 最後更新

- **Session:** S11（**S11 整合 + 校對 + 統一 5 項任務 100% 完成**，下階段 S12+ 進入 Python 視覺化實作）
- **日期:** 2026-05-13
- **狀態:** **S11 全 5 項任務完成：** (3) 跨檔 anchor 校驗 — 39 處 `#vizscript-NN` 連結邏輯全對 + 修復 9 處 broken `#N` 短 anchor（方案 B 重指 ch06f vizscript-01/03）；(5) 資料一致性校驗 — VizScript 36 / `using XX` 地圖與 HANDOFF 一致 / Tier 統計表 6 處校正（總數 33→36、Matrix World Tier 2 旗艦補入、ch06a 改 Tier 1+pointer、附錄 3 個列入）+ S12+ 三批排程連動修正；(1) BOOK.md 完整合併 — 8650 行單檔 / fence-code-aware awk 降一級避開 Python code block 內 `#` 註解 / 含全書目錄 + 統計表 + 視覺錨點段；(2) [VIZ-CATALOG.md](../book/VIZ-CATALOG.md) 抽取 — 241 行純 metadata 索引 / 36 條目（首批 2 + 次批 9 + 末批 A 7 + B 3 + C 15）+ 全章節順序總覽表 + 跨章 pointer ASCII 連動圖 + 進度追蹤段；(4) 風格統一檢查 — SCHEMA.md 新增 §3.5「全書視覺錨點」（配色 6 主色 + 輔助色階 + cell + 動畫 + **3D 視角預設 elevation=25° azimuth=-60°**）+ VIZ_SCHEMA.md cross-reference + 23 處 sed 修正（13 處 X ms→Xms / 10 處 px 空格）；**額外**：Back 提供 8 本 Strang 版權 PDF 至 docs/book/，.gitignore 雙保險防護（pattern + 5 白名單）+ memory feedback_private_pdfs.md（PDF 不 push / md 內可大段引用原文兩層級分開）；back-conclusion.md root heading「33→36」修正。**全書整合完成，S12+ 從 VIZ-CATALOG 首批 Tier 3 旗艦（ch04 V-02 + ch06f V-01）開始 Python 視覺化實作。**

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
- [x] **S02** §1 Viewing a Matrix - 4 Ways：`ch01-viewing-matrix.md`（418 行）— 1 圖描述 + 2 VizMark + 2 VizScript
- [x] **S02** 全書術語慣例 B 派 → A 派切換 + `SCHEMA.md` §3.1 規範更新 + SOP_DRAFT.md §2.4 教訓記錄
- [x] **S03** §2 Vector × Vector - 2 Ways：`ch02-vec-vec.md`（497 行）— 1 圖描述 + 2 VizMark + 2 VizScript；驗證 ch01 範本可複用
- [x] **S03** SOP_DRAFT.md §2.8 對比 / 對偶結構章節寫作模式 + 全書視覺一致性錨點 + 版本 0.4
- [x] **S04** §3 Matrix × Vector - 2 Ways + 4-Subspaces：`ch03-mat-vec.md`（935 行）— 3 圖描述 + 4 VizMark + 4 VizScript
- [x] **S04** SOP_DRAFT.md §2.9 多 VizMark 分級策略 + 版本 0.5
- [x] **S05** §4 Matrix × Matrix - 4 Ways：`ch04-mat-mat.md`（849 行）— 1 圖含 4 子圖描述 + 4 VizMark + 4 VizScript（含 ⭐⭐⭐ Tier 3 VizScript-02 MM4 + Mona Lisa SVD demo，§6 SVD 鋪陳全書最強母模板）
- [x] **S05** SOP_DRAFT.md §2.6 補 N-way 單圖章節觀察 + Tier 2/3 選擇 + 版本 0.6
- [x] **S06** §5 Practical Patterns：`ch05-patterns.md`（830 行）— 4 張獨立圖描述 + 6 Pattern + 4 VizMark + 4 VizScript
- [x] **S06** SOP_DRAFT.md §2.6 補 S06 觀察 + 版本 0.7
- [x] **S07** §6 五大分解總覽：`ch06a-five.md`（331 行）+ §6.1 A=CR：`ch06b-CR.md`（545 行）— 兩章 session 模式首次驗證
- [x] **S07 PNG 重核重大發現：原書 CR1/CR2 圖明標 `using P1` / `using P2`** — §6.1–§6.5 跨章連結官方鐵證
- [x] **S07** SOP_DRAFT.md §2.6 補 S07 + 版本 0.8
- [x] **S08** §6.2 A=LU：`ch06c-LU.md`（654 行）+ §6.3 A=QR：`ch06d-QR.md`（541 行）— 主章 + 主章兩章 session 模式驗證
- [x] **S08 PNG 重核重大發現：`using XX` 跨章 pointer 標記譜系擴大至 MM4** — LU1 無標、LU2 標 `using MM4`、QR 標 `using P1`
- [x] **S08** SOP_DRAFT.md §2.6 補 S08 5 觀察 + 版本 0.9
- [x] **S09** §6.4 S=QΛQᵀ：`ch06e-QLQ.md`（695 行）+ §6.5 A=UΣVᵀ：`ch06f-USV.md`（**934 行，全書最長章**）— §6 主章序列收尾 + 全書 §6 唯一 Tier 3 主 VizScript
- [x] **S09 PNG 重核重大發現：EVD 與 SVD 都標 `using P4`** — §6.x 7 張主圖 `using XX` 最終地圖：CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4
- [x] **S09 「雙 pointer 復活判準」明文化** — PNG 標記重複 + 內容旗艦同根雙條件
- [x] **S09 Tier 3 主 VizScript 首次出現在 §6** — SVD VizScript-01 與 ch04 VizScript-02 並列「核心骨架雙旗艦」
- [x] **S09** SOP_DRAFT.md §2.6 補 S09 6 觀察 + 版本 0.10
- [x] **S10 §1–§6 全書內容 100% 完成**：撰寫 Foreword + Conclusion + 3 附錄（5 個 md 檔 / 1290 行 / 3 VizMark / 3 VizScript）
  - **front-foreword.md**（158 行，0 VizMark）— Strang 推薦序英中對照 + 三大主題導讀（圖解優於符號 / 超越行列點積 / 線性組合+秩 1 矩陣完成代數的藝術）+ 1920-2026 緣起 + 路線 A/B/C
  - **back-conclusion.md**（198 行，0 VizMark）— Hiranabe 結論英中對照 + **全書 33 個 VizScript 總覽表（S11 整合橋樑）+ Tier 分佈統計 + S12+ 實作優先順序三批排程 + 全書 S00–S10 里程碑回顧 + 5 個參考文獻 + 致謝**
  - **appendix-map-eigenvalues.md**（272 行，⭐⭐ Tier 1 + pointer 指 ch06e EVD）— 12 類矩陣 × 特徵值幾何位置完整表 + 與 §6.4 EVD 三層遞進關係 + 與 (P4) 三明治連結 + 12 格 dashboard 互動劇本
  - **appendix-matrix-world.md**（**328 行，⭐⭐⭐ Tier 2 旗艦 — S12+ 全書互動式教材首頁**）— 11 層同心橢圓繼承樹（從 Matrix → Square → Diagonalizable → Normal → Symmetric → ... → {I, O}）+ 偽反矩陣全矩陣統一公式 + 兩條軸線設計（縱深 ⊥ 橫向）+ 13 段 A-M 完整 dashboard 劇本（含 3 模式切換 + 章節過濾器 + 範例矩陣辨認）
  - **appendix-four-subspaces.md**（334 行，⭐⭐ Tier 1 + pointer 指 ch03 V-02 + ch06f V-03）— Strang 正交分解定理 + SVD 構造 4 子空間標準正交基底 + **新增「解 $A\mathbf{x}=\mathbf{b}$ 完整解空間結構視覺」** 段：特解 + 零空間平移仿射子空間 + 最小範數最優解 $\mathbf{x}^* = A^{+}\mathbf{b}$（與 [appendix-matrix-world.md](../book/appendix-matrix-world.md) 底部偽反公式對應）
- [x] **S10 PNG 重核重大發現：3 張附錄 PNG 皆無 `using XX` 標記** — HANDOFF 預估「MapofEigenvalues 可能標 P3」推翻；附錄 PNG 是「**地圖層級 / 基本概念圖**」非「Pattern 套用層級」，標記譜系與主章 §6.x 不同
- [x] **S10 HANDOFF 累積錯誤校正：全書 VizScript 數從 23 校正為 36**（主章 33 + 附錄 3）— 前 session 多次累積寫 23 是漏算（ch03/ch04/ch05 各 4 VizScript = 12 個，多算少數 ~10）
- [x] **S10** SOP_DRAFT.md §2.6 補 S10 7 觀察 + 版本 0.11
- [x] **S11 任務 (3) 跨檔 anchor 校驗：** grep 全書 39 處 `#vizscript-NN` 連結邏輯全對 + 發現 9 處 broken `#N` 短 anchor 全部在 appendix-matrix-world.md (3) + appendix-four-subspaces.md (6)，方案 B 修復（重指 ch06f-USV.md#vizscript-01 或 #vizscript-03，符合附錄「pointer 哲學」）
- [x] **S11 任務 (5) 資料一致性校驗：** VizScript 36 ✓ / `using XX` 標記地圖（CR1=P1, CR2=P2, LU1=無, LU2=MM4, QR=P1, EVD=P4, SVD=P4, 附錄 3 張無）與 HANDOFF 完全一致 / Tier 統計表 6 處校正（總數 33→36、Matrix World V-01 補入 Tier 2 旗艦獨立分類、ch06a V-01 從 Tier 2 改 Tier 1+pointer、附錄 3 個列入、Tier 2 從~10 改 14 主章+1 旗艦、Tier 1 拆 Tier 1+pointer 3 個與 Tier 1 精簡 15 個）+ S12+ 三批排程連動修正（次批新增 Matrix World 旗艦 + 修「ch06b/c/d/e 5 個」→ 4 個）
- [x] **S11 任務 (1) BOOK.md 完整合併：** [BOOK.md](../book/BOOK.md) 8650 行單檔 / 16 個 md 依序串接（front-foreword → ch01–ch06f → back-conclusion → 3 附錄）/ fence-code-aware awk 降一級避開 Python code block 內 `#` 註解 / 含 root heading + 全書目錄 + Tier 統計 + `using XX` 標記地圖 + §6 篇幅比例 + S11 新增「全書視覺錨點」段（3D 視角預設 elevation=25° azimuth=-60° 等）
- [x] **S11 任務 (2) [VIZ-CATALOG.md](../book/VIZ-CATALOG.md) 抽取：** 241 行純 metadata 索引（不複製內容）/ 36 條目（首批 2 + 次批 9 + 末批 A 7 + B 3 + C 15）+ 全章節順序總覽 + 跨章 pointer ASCII 連動圖 + 進度追蹤段（⏳/🔨/✅/⚠️/🔄 五狀態）/ 每行 7 欄位 metadata（連結 + Tier + 批次 + 估時 + 互動類型 + 數學基底 + 跨章 pointer + 狀態）
- [x] **S11 任務 (4) 風格統一檢查：** SCHEMA.md 新增 §3.5「全書視覺錨點」（4 子節：配色 hex+RGB+輔助色階 / cell 寫法 / 動畫時間錨點 / 3D 視角預設）+ 版本 0.2；VIZ_SCHEMA.md §2.2 寫作要點補 cross-reference + 新增 §2.3 對照表 + 版本 0.2；sed 修空格不一致 13 處 X ms → Xms（macOS sed `\b` 不支援，改用無 boundary）+ 10 處 px 空格統一；BOOK.md 重新生成同步全部 S11 修正
- [x] **S11 額外處理 — Strang 8 本版權 PDF 防護：** Back 提供 Linear Algebra for Everyone / Intro to LA / LA and Learning from Data / Diff Eq + LA / CSE / Calculus Vol 1-3 至 docs/book/ 私人參考用；.gitignore 雙保險（`docs/book/*.pdf` pattern + 5 白名單反白）；memory feedback_private_pdfs.md 兩層級分開（PDF 檔本身絕對不 push / md 檔內可大段引用原文以提升完整性，Back 明確授權）+ back-conclusion.md root heading「33→36」修正

### 進行中
- 無，S11 已收尾，**整合 + 校對 + 統一 5 項任務 100% 完成 + Strang 版權 PDF 防護 + memory 更新**

### 待辦（多 session 路線圖 v3 — S11 整合 + S12+ 視覺化實作）

> 互動式 Python 視覺化的「技術棧 / PoC」決策延後到全書 md 化完成（S11）後，於 S12+ 啟動。

| Session | 主題 | 預期產出 |
|---|---|---|
| ✅ S01 + S01.5 | 機械轉換 + 雙 Schema 規劃 | `from-tex/`、`from-pdf/`、`figs-png/`、`SCHEMA.md`、`VIZ_SCHEMA.md`、`_merged.md` |
| ✅ S02 | §1 Viewing a Matrix - 4 Ways | `ch01-viewing-matrix.md`（418 行） |
| ✅ S03 | §2 Vector × Vector - 2 Ways | `ch02-vec-vec.md`（497 行） |
| ✅ S04 | §3 Matrix × Vector - 2 Ways（含 4-Subspaces） | `ch03-mat-vec.md`（935 行） |
| ✅ S05 | §4 Matrix × Matrix - 4 Ways | `ch04-mat-mat.md`（849 行） |
| ✅ S06 | §5 Practical Patterns | `ch05-patterns.md`（830 行） |
| ✅ S07 | §6 五大分解總覽 + §6.1 A=CR（兩章 session）| `ch06a-five.md`（331 行）+ `ch06b-CR.md`（545 行） |
| ✅ S08 | §6.2 A=LU + §6.3 A=QR | `ch06c-LU.md`（654 行）+ `ch06d-QR.md`（541 行） |
| ✅ S09 | §6.4 S=QΛQᵀ + §6.5 A=UΣVᵀ | `ch06e-QLQ.md`（695 行）+ `ch06f-USV.md`（**934 行，全書最長**） |
| ✅ S10 | Foreword + Conclusion + 3 附錄 | `front-foreword.md`（158）+ `back-conclusion.md`（198）+ `appendix-map-eigenvalues.md`（272）+ `appendix-matrix-world.md`（**328 旗艦**）+ `appendix-four-subspaces.md`（334）= **1290 行 + 3 VizMark** |
| ✅ S11 | 整合 + 校對 + 風格統一 + `BOOK.md` + `VIZ-CATALOG.md` + Strang PDF 防護 | [BOOK.md](../book/BOOK.md)（8650 行）+ [VIZ-CATALOG.md](../book/VIZ-CATALOG.md)（241 行 metadata）+ SCHEMA.md §3.5 全書視覺錨點 + 9 處 anchor 修復 + Tier 表 6 處校正 + 23 處風格 sed 修正 + .gitignore PDF 防護 |
| **→ S12** | **Python 視覺化技術棧 PoC + 首批 Tier 3 旗艦實作起步** | 技術棧決策（推薦 Marimo + plotly 3D + matplotlib + scikit-learn + Pillow）+ 從 [VIZ-CATALOG.md](../book/VIZ-CATALOG.md) 首批挑題：ch04 V-02 (MM4 + Mona Lisa) 或 ch06f V-01 (SVD Master) 開始 PoC，預估各 3 session |
| S12+ | Python 視覺化技術棧決策 + 從 VIZ-CATALOG 挑題目開做 PoC | （延後到 S11 後再細規劃，預估 ~28–30 session）|

### S12+ 起步建議（S11 已完成，本段為下一階段路線）

1. **S12+ 「技術棧 PoC + 首批旗艦 PoC」session**（預估 ~3 session 技術棧 + 各 3 session 旗艦）：
   - **技術棧 PoC：** Marimo notebook + plotly 3D + matplotlib + scikit-learn + Pillow（圖像 / Mona Lisa demo）+ scipy（pinv / eig 等）—  跑通 hello world + 1 個簡單 widget
   - **首批 Tier 3 旗艦 PoC：** 從 [VIZ-CATALOG.md 首批](../book/VIZ-CATALOG.md#-首批--核心骨架旗艦2-個-tier-3-旗艦6-session) 挑：
     - **選項 A：** [ch04 V-02 MM4 + Mona Lisa](../book/ch04-mat-mat.md#vizscript-02) — 母模板，後續所有 §6 五分解都 pointer 到此
     - **選項 B：** [ch06f V-01 SVD Master](../book/ch06f-USV.md#vizscript-01) — 全書最強規格 + 4 應用切換 + 雙 pointer 設計
   - 推薦 A 先做（母模板優勢 + 完成後 §6 五分解 pointer 全部解鎖）

2. **依賴鏈考量：** ch04 V-02 完成後解鎖：ch06b/c/d V-01 全部 pointer / ch06a V-01 dashboard 控制器 / ch06f V-01（雙 pointer 主指向）

3. **參考工件：**
   - [BOOK.md](../book/BOOK.md) — 整本書離線閱讀版（8650 行）
   - [VIZ-CATALOG.md](../book/VIZ-CATALOG.md) — 入口 metadata 索引（**S12+ 開工每天用此檔挑題目**）
   - [SCHEMA.md §3.5](../book/SCHEMA.md#35-全書視覺錨點s11-規範化) — 全書視覺錨點規範（配色 / cell / 動畫 / 3D 視角）
   - [VIZ_SCHEMA.md §2.3](../book/VIZ_SCHEMA.md#23-全書視覺錨點-cross-references11-規範化) — VizScript 撰寫時的視覺錨點 cross-reference
   - [docs/dev/sop/SOP_DRAFT.md](sop/SOP_DRAFT.md) — 累積 11 個 session 寫作經驗 + S11 整合教訓

4. **Strang 8 本版權 PDF 已備齊：**（私人參考，不 push GitHub）
   - 寫互動式劇本時可引 Linear Algebra for Everyone Ch.7（SVD）/ Linear Algebra and Learning from Data Ch.1（Mona Lisa 原型）等補完數學推導與例題
   - md 內**可大段引用原文**（Back 明確授權，提升 md 完整性）— PDF 檔本身不 push 即可

### S11 起步建議（已完成，保留歷史）

1. **S11 是「整合 / 校對 / 統一 session」** — 預估 1.5h，主要工作不是新撰寫而是合併 + 校驗
2. **核心產出 1：`BOOK.md`** — 把 13 個 md 檔（ch01 + ch02 + ch03 + ch04 + ch05 + ch06a + ch06b + ch06c + ch06d + ch06e + ch06f + front-foreword + back-conclusion + 3 附錄）依正確順序合併為單一檔案：
   - **順序：** front-foreword.md → ch01–ch06f → back-conclusion.md → appendix-map-eigenvalues.md → appendix-matrix-world.md → appendix-four-subspaces.md
   - **整合動作：** 重新編號章節（1, 2, 3, 4, 5, 6, 6.1, 6.2, ..., 6.5, A, B, C）+ 統一目錄 + 統一 footer
3. **核心產出 2：`VIZ-CATALOG.md`** — 抽取全書 36 個 VizScript（33 主章 + 3 附錄）的索引：
   - 每個 VizScript 一行：標題 / Tier / 章節 / 預估實作 session 數 / S12+ 優先順序批次
   - **Tier 3 旗艦排在最前**：[ch04 V-02](../book/ch04-mat-mat.md#vizscript-02) MM4 Mona Lisa + [ch06f V-01](../book/ch06f-USV.md#vizscript-01) SVD Master
   - **Tier 2 旗艦：** [appendix-matrix-world V-01](../book/appendix-matrix-world.md#vizscript-01) 全書互動式教材首頁
   - **Tier 2 主章：** ~10 個
   - **Tier 1：** ~20 個
4. **跨檔 anchor link 校驗：** 全書有大量 markdown 內部連結（如 `[ch06f V-01](ch06f-USV.md#vizscript-01)`），需 grep + 驗證所有 anchor 是否實際存在：
   ```
   grep -nE "\]\([a-zA-Z0-9_-]+\.md#" docs/book/*.md
   ```
   每個目標檔案內 grep `#` 對應 anchor 是否實際生成。
5. **風格統一檢查：**
   - 術語一致性：所有「列 / 行」是否符合 A 派慣例（column = 列直立 / row = 行橫躺）
   - 配色 hex 統一：全書綠 `#2ca02c` / 粉紅 `#d62728` / 藍 `#1f77b4` / 紫 `#9467bd` / 橙 `#ff7f0e` / 金 `#FFD700` 是否一致
   - cell 尺寸 / 動畫時間 / 3D 視角等視覺錨點是否一致
6. **資料一致性校驗：**
   - 確認 VizScript 總數 36（不再是 23）
   - 確認每個章節「本章 VizMark 數」是否與實際 grep VizScript 結果吻合
   - 確認每個分解章「PNG `using XX` 標記」是否與最終地圖（CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4/3 附錄=無）一致
7. **`BOOK.md` 目錄結構建議：**
   ```
   # 目錄
   - Foreword（Strang 推薦序 + 三大主題）
   - §1 Viewing a Matrix - 4 Ways
   - §2 Vector × Vector - 2 Ways
   - §3 Matrix × Vector - 2 Ways（含 4-Subspaces）
   - §4 Matrix × Matrix - 4 Ways
   - §5 Practical Patterns（P1/P2/P1'/P2'/P3/P4）
   - §6 The Five Factorizations of a Matrix
     - §6 Overview
     - §6.1 A = CR
     - §6.2 A = LU
     - §6.3 A = QR
     - §6.4 S = QΛQᵀ
     - §6.5 A = UΣVᵀ
   - Conclusion & Acknowledgements + 全書 36 個 VizScript 總覽
   - Appendix A：Map of Eigenvalues
   - Appendix B：Matrix World（全書互動式索引地圖 — S12+ 首頁）
   - Appendix C：The Four Subspaces and the Solutions to Ax=b
   - References
   ```
8. **S12+ 從 S11 產出開始：** VIZ-CATALOG.md 直接決定 S12+ 實作優先序，第一批 = Tier 3 兩支旗艦（ch04 V-02 + ch06f V-01）共 6 session，完成後可宣稱「全書互動式教材核心骨架 80%」

### 工件清單（S11 起步前必讀）

| 檔案 | 用途 |
|---|---|
| `docs/book/SCHEMA.md` | 章節 md 結構 + 圖片四欄描述格式（A 派術語） |
| `docs/book/VIZ_SCHEMA.md` | VizMark 標記 + VizScript 13 段 A-M 格式（含 800 字範例） |
| `docs/book/_merged.md` | **S10 已更新**：章節進度追蹤（S10 標 [x]）+ 章節↔圖檔對映 + VizScript 總數 36 校正 + S10 完成里程碑表 |
| `docs/book/front-foreword.md` | **S10 成稿，散文章節 + 推薦序英中對照範本**（158 行，0 VizMark）|
| `docs/book/ch01-viewing-matrix.md` | **S02 成稿，A 派術語的參考範本**（單視角章節） |
| `docs/book/ch02-vec-vec.md` | **S03 成稿，對比 / 對偶結構章節範本** |
| `docs/book/ch03-mat-vec.md` | **S04 成稿，多 VizMark + 多圖章節範本 + 4-Subspaces 標誌圖**（S10 4 子空間附錄 pointer 目標）|
| `docs/book/ch04-mat-mat.md` | **S05 成稿，N-way 單圖章節範本 + VizScript-02 母模板（S09 SVD 雙 pointer 主 pointer 目標 + S10 4 子空間附錄 SVD 構造）** |
| `docs/book/ch05-patterns.md` | **S06 成稿，多獨立小圖章節範本 + 「Tier 1 + pointer」策略首例**（S10 EVD/SVD 附錄 副 pointer 目標）|
| `docs/book/ch06a-five.md` | **S07 成稿，§6 開門總覽範本**（短章節 + Tier1+pointer dashboard，**S10 Matrix World 附錄 Tier 2 旗艦的母模板放大版**）|
| `docs/book/ch06b-CR.md` | **S07 成稿，§6.x 分解主章節範本（雙 pointer + 對偶兩圖 + `using PX` 跨章標記）** |
| `docs/book/ch06c-LU.md` | **S08 成稿，分解主章節範本（單 pointer + `using MM4`）** |
| `docs/book/ch06d-QR.md` | **S08 成稿，分解主章節範本（單圖 + 3D 視覺 + `using P1`）** |
| `docs/book/ch06e-QLQ.md` | **S09 成稿，對稱譜分解章 + 橢球 3D + 單 pointer + `using P4`**（S10 Map of Eigenvalues 附錄 pointer 目標）|
| `docs/book/ch06f-USV.md` | **S09 成稿，全書最長章 + Tier 3 主 VizScript + 雙 pointer + `using P4`**（S10 Four Subspaces 附錄 V-03 pointer 目標 + S10 Matrix World 附錄底部偽反公式對應）|
| `docs/book/back-conclusion.md` | **S10 成稿，結論 + 全書 33 個主章 VizScript 總覽（S11 整合橋樑）+ 全書里程碑回顧** |
| `docs/book/appendix-map-eigenvalues.md` | **S10 成稿，12 類矩陣 × 特徵值幾何附錄**（⭐⭐ Tier 1 + pointer，與 §6.4 EVD 三層遞進連結）|
| `docs/book/appendix-matrix-world.md` | **S10 成稿，旗艦 Tier 2 — 11 層同心橢圓 + 全書互動式教材首頁設計** |
| `docs/book/appendix-four-subspaces.md` | **S10 成稿，4 子空間整合附錄 + 解 $A\mathbf{x}=\mathbf{b}$ 完整結構視覺**（S11 整合時驗證連結是否準確）|
| `docs/book/from-tex/{en,zh}.md` | pandoc 轉換結果（含 LaTeX 公式原文）|
| `docs/book/from-pdf/{en,zh}.txt` | pdftotext 純文字（補 pandoc 缺漏）|
| `docs/book/figs-png/*.png` | 50 張 PNG 圖檔（vision-ready，S10 確認附錄 3 張無 `using XX` 標記）|
| `docs/dev/sop/SOP_DRAFT.md` | **S10 已更新版本 0.11**：§2.6 補 S00–S10 共 11 個 session 各章寫作策略 + S10 補附錄整合模式 7 觀察 — **S11 直接沿用** |

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
| 2026-05-12 | **S02 中途決策變更：術語慣例改採華文主流 A 派（column = 列直立 / row = 行橫躺）** | 與中國大陸、日本、多數 Python 中文文件、本書簡中譯本一致 |
| 2026-05-12 | SOP_DRAFT.md 新增「術語慣例必須在 S01 鎖死」教訓條 | S02 中途改 A 派付出整檔重寫 0.5h 成本 |
| 2026-05-12 | **S03 確立「全書視覺一致性錨點」（SOP §2.8）：配色 hex / cell 尺寸 / 動畫時間統一化** | S04+ 撰寫 VizScript 時直接套用 |
| 2026-05-12 | **S03 確立「對比 / 對偶結構章節寫作模式」** | §3、§4、§6 均適用同一格式，減少每章設計成本 |
| 2026-05-12 | **S04 確立「多 VizMark 章節分級寫作策略」（SOP §2.9）：⭐⭐⭐ 完整 / ⭐⭐ 精簡 / ⭐ 輪廓** | ch03 4 個 VizMark 若全寫 800 字會膨脹 |
| 2026-05-12 | **S04 確立「4-Subspaces 圖是全書視覺化最高 priority 之一（⭐⭐⭐ Tier 3）」** | Strang 兩塊大餅圖是線性代數核心定理的視覺載體 |
| 2026-05-12 | **S05 確立「N-way 單圖章節寫作模式」+ ⭐⭐⭐ 劇本可選 Tier 2 / Tier 3** | ch04 VizScript-02 (MM4 + Mona Lisa SVD demo) 寫成 Tier 3 — §6 SVD 視覺前置 |
| 2026-05-12 | **S05 確立「§4 (MM4) 是 §6 五大分解的視覺基石」** | 5 大分解都可用 (MM4) 展開成「秩 1 之和」 |
| 2026-05-12 | **S06 教訓：HANDOFF 章節描述漏 P4** | 起步前必須對著原書 PNG 重核 Pattern/Figure 數量 |
| 2026-05-12 | **S06 確立「Tier 1 + pointer」省篇幅策略** | ch05 VizScript-03 (P4) 採此策略，§6 5 大分解每章都可重用 |
| 2026-05-12 | **S06 確立「對偶 Pattern 用對偶總表呈現」** | 節省 ~40% 篇幅且閱讀時更易對照 |
| 2026-05-12 | **S07 確立「兩章 session 模式」（總覽短 + 主章長）** | §6 五大分解總覽單獨一個 session 太浪費 |
| 2026-05-12 | **S07 重大發現：原書 PNG `using PX` 標記是跨章連結官方鐵證** | CR1.png 標 `using P1`、CR2.png 標 `using P2` |
| 2026-05-12 | **S07 確立「雙 pointer VizScript 設計」** | ch06b VizScript-01 首例驗證可行 |
| 2026-05-12 | **S07 確立「對偶兩張圖（列視角 + 行視角）是 §6.1–§6.5 全書一致模式」** | CR1+CR2 對偶展示「列秩 = 行秩」 |
| 2026-05-12 | **S08 重大發現：`using XX` 跨章 pointer 標記譜系擴大至 MM4** | 跨章 pointer 不只連 ch05 (P1-P4)，也連 ch04 (MM1-MM4) |
| 2026-05-12 | **S08 確立「單 pointer 比雙 pointer 更常見」規律** | PNG 標什麼 `using XX`，VizScript 就指對應章 |
| 2026-05-12 | **S08 確立「分解章篇幅由『應用面廣度』決定」** | LU 含解 Ax=b、QR 含最小平方法、CR 含列秩=行秩證明 |
| 2026-05-12 | **S08 確立「3D 投影視覺是 QR 章獨有需求」** | 3D 渲染棧成 §6 必備 |
| 2026-05-12 | **S08 確立「主章 + 主章兩章 session 模式」** | 兩個獨立分解主章放同一 session 可行 |
| 2026-05-12 | **S09 重大發現：EVD 與 SVD PNG 都標 `using P4`** | §6.x 7 張主圖 `using XX` 最終地圖：CR1=P1/CR2=P2/LU1=無/LU2=MM4/QR=P1/EVD=P4/SVD=P4 |
| 2026-05-12 | **S09 確立「雙 pointer 復活判準」明文化** | 雙條件「PNG 標記重複 + 內容旗艦同根」雙成立才升級 |
| 2026-05-12 | **S09 確立「Tier 3 主 VizScript 首次出現在 §6」** | SVD VizScript-01 與 ch04 VizScript-02 並列「核心骨架雙旗艦」|
| 2026-05-12 | **S09 確立「§6 主章序列篇幅比例 1.0:1.20:0.99:1.28:1.71，SVD 為集大成終章」** | SVD 章 934 行為平均章節 1.6 倍 |
| 2026-05-12 | **S09 確立「§6 章節雙 pointer 設計地圖規律」** | 對偶兩張圖（CR）+ 集大成章（SVD）採雙 pointer |
| 2026-05-12 | **S10 重大發現：3 張附錄 PNG（MapofEigenvalues / MatrixWorld / 4-Subspaces）皆無 `using XX` 標記** | 附錄 PNG 是「**地圖層級 / 基本概念圖**」非 Pattern 套用層級，標記譜系與主章 §6.x 不同 |
| 2026-05-12 | **S10 確立「附錄重整合 vs 主章重教學」雙模式** | 附錄 3 個 VizMark 都採「pointer 到主章 VizScript」策略，不重複實作（map → ch06e、4-subspaces → ch03 V-02 + ch06f V-03、Matrix World 跨全書索引）|
| 2026-05-12 | **S10 確立「Matrix World 互動式索引地圖首次升級為 Tier 2 旗艦」** | appendix-matrix-world V-01 設計為「**S12+ 全書互動式教材的首頁**」（讀者進入教材的標準入口），與 ch06a V-01 五分解 dashboard 互補（前者分類學索引、後者分解視覺索引）|
| 2026-05-12 | **S10 確立「全書 33 個 VizScript 總覽段是 S11 整合的橋樑」** | back-conclusion.md 新增此段（原書無）讓 S11 BOOK.md / VIZ-CATALOG.md 整合直接抽取，省 0.5 session 額外整理 |
| 2026-05-12 | **S10 校正「HANDOFF 累積錯誤 — VizScript 數從 23 校為 36」** | 前 session 累積寫 23 是漏算 ch03/ch04/ch05 各 4 = 12 個；S11 整合時 grep 校驗為共識統計值的標準步驟 |
| 2026-05-12 | **S10 確立「四子空間附錄新增『解 $A\mathbf{x}=\mathbf{b}$ 完整解空間結構視覺』」** | 與 [appendix-matrix-world.md](../book/appendix-matrix-world.md) 底部偽反公式 $A^{+} = V\Sigma^{+}U^{\mathrm{T}}$ 對應，把「解方程」完整結構（特解 + 零空間 + 仿射子空間 + 最小範數最優解）整合進附錄；§6.5 SVD 章未深入此面 |
| 2026-05-13 | **S11 確立「broken anchor 修復方案 B：重指 VizScript 級 anchor」** | 附錄本來就是「重整合 → pointer 到主章 VizScript」設計，9 處 broken `#N` 短 anchor 改指 `#vizscript-01/03` 比指 `§N` 段落更符合附錄哲學 |
| 2026-05-13 | **S11 確立「BOOK.md vs VIZ-CATALOG.md 雙檔組合最有效」** | BOOK.md = 整本書下載/離線閱讀（8650 行）；VIZ-CATALOG.md = 入口 metadata 索引（241 行純連結 + 7 欄位）— 兩個不是替代而是補充，S12+ 開工先看 catalog 挑題再跳原章節讀 13 段 A-M 劇本 |
| 2026-05-13 | **S11 確立「fence-code-aware awk 降一級策略」** | sed `g/^#/##/` 第一輪會誤把 ch06e Python code block 內「# 參數化單位球」「# plotly Surface 渲染」等註解改為 ## heading；改用 awk + ``` fence 追蹤狀態解 — 未來 BOOK.md 重新生成都用此邏輯 |
| 2026-05-13 | **S11 確立「全書 3D 視角預設規範 elevation=25° azimuth=-60°」** | 全書 109 次 3D 提及但 S11 前只 1 處明確聲明（ch03 V-02）；補規範後 ch06d/06e/06f/App C 等 3D VizScript 有共同錨點，S12+ 實作渲染風格一致 |
| 2026-05-13 | **S11 確立「動畫時間 / px 寫法強制統一無空格 `Xms` / `AAxBB px`」** | 全書 X ms (16) vs Xms (38) 不一致，sed 統一為無空格 ms；px 統一中間 × 兩側無空格、px 前 1 空格；macOS BSD sed 不支援 `\b` word boundary 需注意 |
| 2026-05-13 | **S11 確立「Strang 版權 PDF 兩層級分開處理」** | PDF 檔本身絕對不 push GitHub（.gitignore pattern + 5 白名單反白）；md 檔內可大段引用原文（Back 明確授權「重點是 md 完整性」）— S12+ 撰寫補充章節可直接引 Strang 原始定義/例題 |
| 2026-05-13 | **S11 確立「back-conclusion.md Tier 統計表是 VIZ-CATALOG.md 的單一真相來源」** | S11 把 conclusion 表從「主章 33 個」校為「全書 36 個」+ 加入 Matrix World Tier 2 旗艦 + ch06a 改 Tier 1+pointer + 附錄 3 個列入 — VIZ-CATALOG.md 直接引此表為統計基礎 |

---

## 檔案變更追蹤

### S00 / S01 / S01.5 / S02–S09 詳見 SESSION_INDEX.md

簡述：S00 初始化、S01 機械轉換 + Schema、S02–S09 撰寫 9 個主章節 md 檔（ch01–ch06f 共 6824 行 + 33 個主章 VizScript）。

### S10 新增/修改的檔案

| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/front-foreword.md | 新增 | **序言 158 行，0 VizMark** — Strang 推薦序英中對照 + 三大主題導讀 + 1920-2026 緣起 + 路線 A/B/C 三條閱讀路線 |
| docs/book/back-conclusion.md | 新增 | **結論 198 行，0 VizMark** — Hiranabe 結論英中對照 + **全書 33 個 VizScript 總覽表（S11 整合橋樑）+ Tier 分佈統計 + S12+ 實作優先順序三批排程 + 全書 S00–S10 里程碑回顧 + 5 個參考文獻 + 致謝**|
| docs/book/appendix-map-eigenvalues.md | 新增 | **附錄 A 272 行，⭐⭐ Tier 1 + pointer 指 ch06e EVD** — 12 類矩陣 × 特徵值幾何位置完整表 + 對應 §6.4 EVD 三層遞進關係 + 與 (P4) 三明治連結 + 12 格 dashboard 互動劇本 13 段 A-M |
| docs/book/appendix-matrix-world.md | 新增 | **附錄 B 328 行，⭐⭐⭐ Tier 2 旗艦 — S12+ 全書互動式教材首頁** — 11 層同心橢圓繼承樹（Matrix → Square → Diagonalizable → Normal → Symmetric → ... → {I, O}）+ 偽反矩陣全矩陣統一公式 $A^{+} = V\Sigma^{+}U^{\mathrm{T}}$ + 兩條軸線設計（縱深特殊性 ⊥ 橫向對稱性）+ 13 段 A-M 完整 dashboard 劇本（含 3 模式切換 + 章節過濾器 + 範例矩陣辨認）|
| docs/book/appendix-four-subspaces.md | 新增 | **附錄 C 334 行，⭐⭐ Tier 1 + pointer 指 ch03 V-02 + ch06f V-03** — Strang 正交分解定理 + SVD 構造 4 子空間標準正交基底 + **新增「解 $A\mathbf{x}=\mathbf{b}$ 完整解空間結構視覺」** 段：特解 + 零空間平移仿射子空間 + 最小範數最優解 $\mathbf{x}^* = A^{+}\mathbf{b}$ + 整合 §3 + §6.5 + Matrix World 三章 |
| docs/book/_merged.md | 修改 | S10 標 [x]，VizMark 計數「3 附錄合計 ⭐⭐⭐ × 1 + ⭐⭐ × 2 + ⭐ × 0」（含 Matrix World 旗艦 Tier 2）+ §S10 附錄 PNG 重核發現新規律（3 張附錄 PNG 皆無 `using XX` 標記）+ 新增 S10 完成里程碑表（13 個 md 檔 / ~8100 行 / 36 個 VizScript / 2 Tier 3 旗艦 + 1 Tier 3 候選 + 1 Tier 2 旗艦地圖 / `using XX` 完整地圖）|
| docs/dev/sop/SOP_DRAFT.md | 修改 | §2.6 補 S10 耗時資料點（~2.5h / 1290 行 / 5 個檔案 / 3 VizMark = 1 Tier 2 旗艦 + 2 Tier 1）+ 7 觀察（附錄 PNG 無標記新規律 / 附錄重整合 vs 主章重教學雙模式 / Matrix World Tier 2 旗艦首次出現 / Conclusion 33 VizScript 總覽段是 S11 橋樑 / HANDOFF 累積錯誤校正 23→36 / 散文章節耗時規律 / 附錄章節耗時規律）+ 版本記錄追加 0.11 |
| docs/dev/CURRENT_SESSION.log | 修改 | S10 啟動 + 即時記錄 + 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S10 一行 |

### S11 新增/修改的檔案

| 檔案 | 動作 | 說明 |
|------|------|------|
| docs/book/BOOK.md | 新增 | **8650 行全書合併單檔** — 16 個 md 依序串接（front-foreword → ch01–ch06f → back-conclusion → 3 附錄）+ root heading + 全書目錄 + Tier 統計表 + using XX 標記地圖 + §6 篇幅比例 + S11 新增「全書視覺錨點」段；採 fence-code-aware awk 降一級避開 Python code block 內 `#` 註解 |
| docs/book/VIZ-CATALOG.md | 新增 | **241 行純 metadata 索引** — 36 個 VizScript 三批排程（首批 2 + 次批 9 + 末批 A 7 + B 3 + C 15）+ 全章節順序總覽 + 跨章 pointer ASCII 連動圖 + 進度追蹤（⏳/🔨/✅/⚠️/🔄 五狀態）+ 每行 7 欄位 metadata（連結 + Tier + 批次 + 估時 + 互動類型 + 數學基底 + 跨章 pointer + 狀態）|
| docs/book/SCHEMA.md | 修改 | 新增 §3.5「全書視覺錨點」段（4 子節：3.5.1 配色 6 主色 hex+RGB+輔助色階兩變形+灰階補助 / 3.5.2 cell 像素尺寸規範 / 3.5.3 動畫時間錨點 + 無空格寫法 / 3.5.4 **3D 視角預設 elevation=25° azimuth=-60°**）+ 版本記錄追加 0.2 |
| docs/book/VIZ_SCHEMA.md | 修改 | §2.2 寫作要點 3/4 補 SCHEMA.md §3.5 cross-reference + 新增 §2.3「全書視覺錨點 cross-reference」對照表（4 項）+ 版本記錄追加 0.2 |
| docs/book/back-conclusion.md | 修改 | Tier 統計表 6 處校正（總數 33→36、Matrix World V-01 補入 Tier 2 旗艦獨立分類、ch06a V-01 從 Tier 2 改 Tier 1+pointer、附錄 3 個列入、Tier 2 從~10 改 14 主章+1 旗艦、Tier 1 拆 Tier 1+pointer 3 個與 Tier 1 精簡 15 個）+ S12+ 三批排程連動修正 + root heading「33→36」修正 |
| docs/book/appendix-matrix-world.md | 修改 | 3 處 broken `#N` anchor → `#vizscript-01/03`（方案 B）：`#6`→V-01、`#64`→V-01、`#2`→V-03 |
| docs/book/appendix-four-subspaces.md | 修改 | 6 處 broken `#N` anchor → `#vizscript-01/03`（方案 B）：4 個 `#4`→V-03 / `#64`→V-01 / `#7`→拿掉 anchor（無對應 VizScript）|
| docs/book/appendix-map-eigenvalues.md | 修改 | sed 修 X ms→Xms 空格不一致（與其他附錄一起批次處理）|
| .gitignore | 修改 | 新增 `docs/book/*.pdf` pattern + 5 個白名單反白（The-Art-of-Linear-Algebra*.pdf / MapofEigenvalues.pdf / MatrixWorld.pdf）防 8 本 Strang 版權 PDF 誤 push |
| docs/dev/sop/SOP_DRAFT.md | （pending）| S11 整合 + 風格統一教訓待補（session-end Step 5b 處理）|
| docs/dev/CURRENT_SESSION.log | 修改 | S11 啟動 + 即時記錄（含 5 項任務逐步完成）+ 結束記錄 |
| docs/dev/SESSION_INDEX.md | 修改 | 追加 S11 一行 |
| docs/dev/RETROSPECTIVE.md | 修改 | S11 對話反思追加（session-end Step 6 處理）|
| ~/.claude/projects/.../memory/feedback_private_pdfs.md | 新增（memory）| Strang 8 本版權 PDF 兩層級處理規範（PDF 不 push / md 內可大段引用原文，Back 授權）|
| ~/.claude/projects/.../memory/MEMORY.md | 修改（memory）| 補一行 index 指向 feedback_private_pdfs.md |

---

## 技術筆記

### Repo 原始內容概覽
- **LaTeX 主檔**：`The-Art-of-Linear-Algebra.tex`（英文）、`-j.tex`（日文）、`-zh-CN.tex`（簡中）
- **編好的 PDF**：三種語言版本均已存在
- **圖檔來源**：`Illustrations.pptx`（PowerPoint），透過 makefile 流程印成 PS → EPS → 嵌入 LaTeX

### 互動式版本技術選項（S12+ 決策，目前傾向）

| 方案 | 優點 | 缺點 |
|------|------|------|
| **Marimo + matplotlib + plotly + scikit-learn + Pillow**（S02–S10 VizScript 首選） | 反應式 notebook、純 Python、可匯出 HTML、3D / 影像 / PCA 全支援 | 較新生態系較小 |
| Streamlit + Plotly | 部署成網頁簡單、互動流暢 | 不適合 notebook 形式閱讀 |
| Jupyter + ipywidgets + matplotlib | 標準、容易分享 .ipynb | 互動效能一般、需要 kernel |
| Plotly + Dash | 視覺化品質最高 | 學習曲線較陡 |
| Manim | 動畫效果最好（3Blue1Brown 同款） | 不互動、是動畫腳本 |
| 純 HTML + JS（D3 / Three.js） | 任何瀏覽器可開 | 跳脫 Python 生態 |

**S08–S10 觀察累積（3D 渲染棧成 §6 必備 + Mona Lisa 影像處理 + 多應用切換 + Matrix World 同心橢圓向量化 + 4 子空間 3D 仿射視覺）：**
- §6.3 QR：3D 投影視覺（matplotlib 3D / plotly 3D）；
- §6.4 EVD：3D 橢球主軸對齊（plotly 3D 為主，因參數球面渲染流暢度高）；
- §6.5 SVD：**全書最複雜的視覺化棧** — 3D 橢球 + Mona Lisa（Pillow + numpy）+ Iris PCA + 推薦評分視覺 + 4 子空間（重用 ch03）
- **S10 Matrix World 附錄 Tier 2 旗艦：** 11 層同心橢圓需向量化縮放支援（plotly SVG path 為主）+ 章節過濾器 + 範例矩陣辨認需 `numpy.linalg.eig` + `scipy.linalg.norm`
- **S10 Four Subspaces 附錄：** 仿射子空間 3D 視覺（通解平面平行 $\mathbf{N}(A)$ 通過 $\mathbf{x}_p$），需 `plotly.graph_objects.Surface` + `numpy.linalg.pinv`

**結論：S12+ 必確認技術棧支援所有需求**：**Marimo + plotly 3D + matplotlib + scikit-learn + Pillow** 為最低限度組合（涵蓋全書 36 個 VizScript）。

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
| spectral theorem | 譜定理 | — |
| singular value decomposition (SVD) | 奇異值分解（SVD）| — |
| eigenvalue decomposition (EVD) | 特徵值分解（EVD）/ 譜分解 | — |
| Eckart-Young theorem | Eckart-Young 定理 / 最佳低秩近似定理 | — |
| Moore-Penrose pseudoinverse | Moore-Penrose 偽反 / 偽反矩陣 | — |
| Frobenius norm | Frobenius 範數 / F 範數 | — |
| principal component analysis (PCA) | 主成分分析 | — |
| **normal matrix** | **正規矩陣**（S10 新增 — Matrix World L5 層）| — |
| **Markov matrix** | **Markov 矩陣**（S10 新增 — Map of Eigenvalues 12 類之一）| — |
| **nilpotent matrix** | **冪零矩陣**（S10 新增 — Map of Eigenvalues 12 類之一）| — |
| **anti-symmetric / skew-symmetric** | **反對稱矩陣**（S10 新增 — Map of Eigenvalues 12 類之一）| — |
| **Jordan form** | **Jordan 形式**（S10 新增 — Matrix World L4b）| — |
| **affine subspace** | **仿射子空間**（S10 新增 — Four Subspaces 附錄解 $A\mathbf{x}=\mathbf{b}$）| — |

**矩陣尺寸：** $A \in \mathbb{R}^{m \times n}$ 表示 **$m$ 行 $n$ 列**（$m$ rows, $n$ columns）。$m$ = 行數、$n$ = 列數。
**矩陣乘法形狀：** $A \in \mathbb{R}^{m \times k}$、$B \in \mathbb{R}^{k \times n}$、$AB = C \in \mathbb{R}^{m \times n}$。**內維 $k$ 必須對齊**。

### 全書視覺一致性錨點（S03 確立，S08+ 補 3D + 金色主元 + 黃色中間結果，S09 補 SVD 雙色對比，S10 補附錄 4 子空間配色一致 + Matrix World 11 層橢圓深藍）

- **配色 hex：** 綠（列 / 直立 / 正交向量 / **U / 列空間**）`#2ca02c`、粉紅 / 紅（行 / 橫躺 / 投影向量 / **V^T / 行空間 / SVD 雙側獨立指紋**）`#d62728`、藍點（個別數字 / 對角元素 / **σ_p 與 λ_p / Matrix World 橢圓邊框 / Map of Eigenvalues 複平面背景**）`#1f77b4`、灰填充 `#cccccc`（原始向量 / 已剝離元素 / **單位球 / 對稱輸入 / Map of Eigenvalues 複平面格線**）、子空間半透明 alpha 0.3、紫色（特徵基底 / 動態系統 / CR 第 3 列 / **退化警示 / 4 子空間零空間方向 / 負特徵值反射**）`#9467bd`、橙色（CR 第 2 列 / 接近依賴警示 / **秩 k 截斷曲線 / Map of Eigenvalues 特徵值點**）`#ff7f0e`、**金色 `#FFD700`**：主元 / 當前正在處理的列 / **變形後的橢球 / EVD 橢球 / Matrix World hover 高亮 / Four Subspaces 特解**、**黃色**：中間結果 $\mathbf{w}_p$（減投影後未單位化）/ Four Subspaces 仿射通解平面（alpha 0.3）
- **cell 尺寸：** 預設 60×60 px，極小 80×80（$m=n=2$）、極大 48×48（$m=n=6$）
- **3D 視窗尺寸：** 預設 600×480 px、視角 elev=25° azim=-60°（S08 QR 章 / S09 EVD 章 / S09 SVD 章 / S10 Four Subspaces 仿射子空間都必備）
- **動畫時間：** 視角切換 600–800ms、平行性高亮淡入 200ms、子空間維度變化 600ms、飛行軌跡 700ms、秩 1 累加 400ms / 項、緩動 ease-in-out、peeling 動畫 600ms / 楔形（S08）、Gram-Schmidt 減投影 500ms / 投影（S08）、譜分解逐項累加 1500ms / 項（S09）、橢球變形 800ms（S09）、SVD 應用切換 500ms（S09）、**Matrix World hover 200 ms 邊框加粗 + click 400 ms panel 滑入 + 章節過濾 600 ms 淡入淡出（S10）、Four Subspaces 通解平面平移 800 ms（S10）**
- **數值範圍：** $a_{ij} \in [-9, 9]$ 步進 1，維度 $m, n \in [2, 6]$（3D 限 $\{2, 3\}$、SVD demo Mona Lisa 400×250 / Iris 150×4）；對角元素 $d_p \in [-3, 3]$ 步進 0.5、特徵值 $\lambda_p \in [-9, 9]$、奇異值 $\sigma_p \geq 0$、**Map of Eigenvalues $z$ 拉桿 $z = a + bi$ $a, b \in [-3, 3]$ 步進 0.1（S10）、Four Subspaces 矩陣 $A$ $a_{ij} \in [-3, 3]$ 步進 0.5（S10）**
- **N-way 切換動畫：** 多視角 tab 切換時 800ms 動畫含「色塊重排 + 重染色 + 公式同步」三層
- **對角矩陣表現：** 藍圓點直徑 12–14px 沿對角線排列、**非對角位置完全留白不畫 0**、$d_p$ 改變時藍點半徑 ∝ $|d_p|$
- **動態系統軌跡：** 軌跡藍漸變（淡 → 深 = 時間順序）、當前點紫實心 8px、特徵向量綠箭頭
- **CR 三色標記（S07）：** $A$ 的列 1 = 藍 / 列 2 = 橙 / 列 3 = 紫
- **LU 楔形視覺（S08）：** 楔形 $p$ 大小 ∝ 殘餘子矩陣 $A_p$ 範圍
- **QR 上三角藍點（S08）：** $R$ 用藍點 + 上三角形狀排列展示
- **EVD 鏡像對稱布局（S09）：** $Q$（綠列直立）和 $Q^{\mathrm{T}}$（綠行橫躺）在 $\Lambda$ 兩側鏡像對稱 — 對稱矩陣的視覺指紋
- **SVD 雙色獨立布局（S09）：** $U$（綠列直立）和 $V^{\mathrm{T}}$（**粉紅行橫躺**）使用不同顏色對比 — 雙側獨立的視覺指紋（與 EVD 同色形成對比）
- **譜分解投影矩陣 $P_p$（S09）：** $P_p = \mathbf{q}_p \mathbf{q}_p^{\mathrm{T}}$ 顯示為「綠列 + 淡綠橫躺行」自外積（左右標號相同）
- **SVD 秩 1 拆解（S09）：** $\sigma_p \mathbf{u}_p \mathbf{v}_p^{\mathrm{T}}$ 顯示為「綠列 + 淡粉紅橫躺行」一般外積（左右標號相同但顏色不同）
- **跨章跳轉按鈕（S07–S10）：** 白底深綠邊框 + 「→」字樣，hover 填色 `#2ca02c`；按鈕分四類「→ (MM4) 累加 / Mona Lisa」（指 ch04 V-02）/「→ (P1)(P2) 對角」（指 ch05 V-01）/「→ (P4) 三明治」（指 ch05 V-03，S09 補 EVD/SVD pointer）/「→ 4 子空間」（指 ch03 V-02，S09 補 SVD 整合，S10 補附錄 C pointer）
- **附錄旗艦 Matrix World 視覺（S10）：** 同心橢圓深藍邊框 + 章節過濾器粉紅標記 + 範例矩陣對應層漸變色（最外淺藍 → 最內紫紅）+ hover 黃金高亮 + Tier 標記顏色說明面板
- **附錄 Map of Eigenvalues 視覺（S10）：** 12 格 grid view 並列 + 點任一格 zoom 800×600 + 拉桿即時動畫 200 ms 平滑移動橙色特徵值點
- **附錄 Four Subspaces 解 $A\mathbf{x}=\mathbf{b}$ 視覺（S10）：** 紫色零空間 + 金色特解 + 黃半透明通解平面 + 綠色最小範數最優解 4 色組合 + 殘差數值即時顯示

### 章節撰寫速度資料點（S10 更新 + 完整里程碑回顧）

- **S02 §1（含 A 派切換重寫 0.5h）：** 1.5h / 418 行 / 2 VizMark
- **S03 §2（ch01 範本可複用）：** 1h / 497 行 / 2 VizMark
- **S04 §3（4 VizMark 分級策略）：** 1.5h / 935 行 / 4 VizMark
- **S05 §4（1 圖含 4 子圖 + 4 VizMark）：** 1h / 849 行 / 4 VizMark
- **S06 §5（4 圖各獨立 + 6 Pattern + 4 VizMark）：** 1h / 830 行 / 4 VizMark
- **S07 §6 總覽 + §6.1（兩章 session）：** 2h / 876 行（331 + 545）/ 4 VizMark — 兩章 session 模式首次驗證
- **S08 §6.2 LU + §6.3 QR（兩章主章模式）：** 2.5h / 1195 行（654 + 541）/ 6 VizMark — 主章 + 主章模式驗證 + 3D 渲染棧導入
- **S09 §6.4 EVD + §6.5 SVD（兩章主章模式收尾）：** 3h / 1629 行（695 + 934）/ 7 VizMark — SVD 章 934 行為全書最長 + Tier 3 主 VizScript 首次出現在 §6
- **S10 Foreword + Conclusion + 3 附錄（散文 + 附錄混合 session）：** **~2.5h / 1290 行（158 + 198 + 272 + 328 + 334）/ 3 VizMark（1 Tier 2 旗艦 + 2 Tier 1 + pointer）— 附錄重整合 vs 主章重教學雙模式確立 + Matrix World 升級 Tier 2 旗艦（S12+ 全書首頁）**
- **S11 預估：** **~1.5h / 整合工作（不新撰寫）**：BOOK.md 合併（13 個 md 檔依順序串接 + 重新編號）+ VIZ-CATALOG.md 抽取（36 個 VizScript 索引）+ 跨檔 anchor link grep 校驗 + 風格 / 配色 / 術語統一檢查 + 資料一致性校驗（VizScript 總數 36、`using XX` 標記譜系、雙 pointer / 單 pointer 分佈）
- **S11 實際：** **~2h / 整合 + 校對 + 統一 5 項任務 + Strang PDF 防護**：(3) anchor 校驗 9 處 broken 修復 / (5) 一致性 Tier 表 6 處校正 / (1) BOOK.md 8650 行（**含 fence-code-aware awk 教訓**：第一輪 sed `g/^#/##/` 誤把 ch06e Python code block 內 `# 參數化單位球` 等註解改為 ## heading，重生用 awk 解決）/ (2) VIZ-CATALOG.md 241 行 / (4) SCHEMA §3.5 新增 + 23 處 sed 修正（**macOS BSD sed 不支援 `\b` word boundary，需改用 `([0-9]) ms` 不帶 boundary**）+ 額外 Strang 版權 PDF 雙保險 .gitignore 防護 + memory feedback 兩層級分開記憶

**§1–§6 + 序言 + 結論 + 3 附錄累計（S10 收尾）：** 共 **13 個 md 檔（ch01–ch06f 9 個主章 + front-foreword + back-conclusion + 3 附錄）= 總計 ~8100 行**（主章 6824 行 + S10 散文/附錄 1290 行）+ **36 個 VizScript**（4 個 Tier 3：[ch04 V-02](../book/ch04-mat-mat.md#vizscript-02) + [ch06f V-01](../book/ch06f-USV.md#vizscript-01) 兩支主旗艦 + ch04 V-01（Tier 2）+ ch06f V-02（Tier 2）；多支 Tier 2 含 [appendix-matrix-world V-01](../book/appendix-matrix-world.md#vizscript-01) 旗艦 + 多支 Tier 1）。**§1–§6 全書內容 100% 完成**，下階段轉入「校對 + 整合 + 風格統一」（S11）。

### §4 (MM4) 與 §6 五大分解的鋪陳對應（S09 完整定版，S10 補附錄連結）

| §6 分解 | (MM4) 形式 | VizScript 結構複用 | PNG `using XX` 標記 | Pointer 設計 |
|---|---|---|---|---|
| $A = CR$ | $A = \sum_p \mathbf{c}_p \mathbf{r}^*_p$（$r$ 項） | ch04 V-02 + ch05 V-01 | CR1 標 P1、CR2 標 P2 | 雙 pointer（對偶兩張圖）|
| $A = LU$ | $A = \sum_p \mathbf{l}_p \mathbf{u}^*_p$（$n$ 項） | ch04 V-02 | LU1 無標、LU2 標 MM4 | 單 pointer 指 ch04 |
| $A = QR$ | $A = \sum_p \mathbf{q}_p \mathbf{r}^*_p$（$n$ 項） | ch05 V-01 | QR 標 P1 | 單 pointer 指 ch05 |
| $S = Q\Lambda Q^{\mathrm{T}}$ | $S = \sum_p \lambda_p \mathbf{q}_p \mathbf{q}^{\mathrm{T}}_p$（自外積）| ch05 V-03 | EVD 標 P4 | 單 pointer 指 ch05 |
| $A = U\Sigma V^{\mathrm{T}}$ | $A = \sum_p \sigma_p \mathbf{u}_p \mathbf{v}^{\mathrm{T}}_p$（一般外積）| ch04 V-02 + ch05 V-03 | SVD 標 P4 | 雙 pointer（集大成 + 內容旗艦同根）|
| **附錄 A Map of Eigenvalues**（S10）| — | 重用 ch06e V-01（EVD 詳解）| **無 using 標**（地圖層級）| Tier 1 + pointer 指 ch06e |
| **附錄 B Matrix World**（S10 旗艦）| 含全部 5 分解 + 偽反 | 整合全書 36 個 VizScript 索引 | **無 using 標**（標 Strang section number）| **Tier 2 旗艦** — 跨全書索引 dashboard |
| **附錄 C The Four Subspaces**（S10）| — | 重用 ch03 V-02 + ch06f V-03 + 新增解 $A\mathbf{x}=\mathbf{b}$ 視覺 | **無 using 標**（基本概念）| Tier 1 + pointer 指 ch03 + ch06f |

**S10 結論（§1–§6 全書 md 化收尾）：** ch04 V-02（MM4 + Mona Lisa SVD demo）+ ch06f V-01（SVD 完整互動）+ appendix-matrix-world V-01（全書互動式教材首頁）= **「全書互動式教材的核心三旗艦」**（兩支 Tier 3 內容旗艦 + 一支 Tier 2 索引旗艦）。**S12+ 實作優先順序明確化：**

1. **首批實作（核心骨架）：** ch04 V-02（3 session）+ ch06f V-01（3 session）+ appendix-matrix-world V-01（2 session）= **8 session 完成核心三旗艦，宣稱「全書互動式教材核心骨架 100%」**
2. **次批實作（主章 Tier 2 + 4 子空間整合）：** ch06b/c/d/e V-01 各 2 session = 8 session；ch03 V-02（4 子空間 3D，視時間升 Tier 3）3 session；ch01–ch05 各章 V-01（共 5 個 Tier 2）共 7 session；3 附錄各 V-02+ 共 3 session
3. **末批實作（Tier 1 輕量 + walkthrough）：** ~6 session
4. **Total S12+ 預估：** **~30 session 完成完整互動式教材**（不含技術棧 PoC 初期 ~3 session）。整個專案總 S00–S40 = ~40 session

**§6 章節雙 pointer 設計地圖規律（S09 確立，S10 附錄延續）：**

- **雙 pointer 採用：** 對偶兩張圖（CR1+CR2）+ 集大成終章（SVD）；
- **單 pointer 採用：** 單張圖且非集大成章（LU / QR / EVD）+ 附錄基本概念圖（Map of Eigenvalues / 4-Subspaces）；
- **Tier 2 跨全書索引：** Matrix World 附錄無 pointer 是「**自身就是全書 36 個 VizScript 的彙整索引**」
- **判準：** PNG `using XX` 標記重複 + 內容旗艦同根**雙條件**成立才升級雙 pointer。

---

## 新 Session 開始時的指令

```
請先讀取以下檔案恢復 context：
1. docs/dev/HANDOFF.md — 上次 session 狀態（本檔，S11 收工版）
2. docs/dev/SESSION_INDEX.md — 歷史 session 列表（含 S11）
3. docs/dev/CURRENT_SESSION.log — 上一次 session 即時記錄
4. docs/book/VIZ-CATALOG.md — **S12+ 開工首要檔（入口 metadata 索引，挑題目用）**
5. docs/book/BOOK.md — 全書合併單檔（8650 行，整本書離線閱讀版）
6. docs/book/SCHEMA.md（§3.5 全書視覺錨點 — 配色 / cell / 動畫 / 3D 視角預設）+ docs/book/VIZ_SCHEMA.md（§2.3 cross-reference）
7. docs/book/ch01–ch05 + ch06a–ch06f（9 主章）+ front-foreword + back-conclusion + 3 附錄 = 16 個 md 範本（VizScript 13 段 A-M 完整劇本）
8. docs/dev/sop/SOP_DRAFT.md（含 S00–S10 全部章節寫作策略；S11 整合教訓待 session-end 時補）
9. docs/dev/RETROSPECTIVE.md — Session 對話反思（S11 收工版含 1 條反思條目）
然後從「S12+ 起步建議」決定本次任務：技術棧 PoC + 首批 Tier 3 旗艦選 ch04 V-02 (MM4 + Mona Lisa，母模板，推薦先做) 或 ch06f V-01 (SVD Master，全書最強規格)。可參考 Strang 版權 PDF（docs/book/*.pdf，已 .gitignore 不 push）補完數學推導與例題。
```
