# VIZ-CATALOG — 全書 36 個 VizScript 實作目錄

> **用途：** S12+ Python 視覺化實作的「**入口 metadata 索引**」。本檔不複製 VizScript 內容（劇本完整版在各章節 md 檔內），只記錄每個 VizScript 的身份證 + 跳轉連結 + 實作 metadata + 進度追蹤。
>
> **產出時間：** S11 整合階段（2026-05-13）
> **總計：** 36 個 VizScript（主章 33 + 附錄 3）
> **狀態：** S12+ 尚未開工（全部 ⏳）
>
> **如何使用：**
> 1. **挑題目：** 從 Tier 3 旗艦開始 / 按批次順序 / 或挑你感興趣的章節
> 2. **點連結跳轉：** 每行的標題連結直接跳到原章節 md 的對應 VizScript 段
> 3. **看劇本：** 原章節內每個 VizScript 都有 13 段 A-M 完整劇本（~800 字 / 個）+ 上方數學要點 + 圖片描述
> 4. **跨章 pointer：** 旗艦 VizScript 多採 pointer 設計（不重複實作），需先把 pointer 目標完成
> 5. **更新進度：** 開始實作 → ⏳ → 🔨；完成 → 🔨 → ✅；阻塞 → ⚠️

---

## 全書 Tier 分佈統計（S11 校正版）

| Tier | 數量 | 預估 session 總數 |
|---|---|---|
| ⭐⭐⭐ Tier 3 旗艦 | 2 | 6 |
| ⭐⭐⭐ Tier 3 候選（升級空間）| 1 | 2–3 |
| ⭐⭐⭐ Tier 2 旗艦（附錄）| 1 | 4 |
| ⭐⭐ Tier 2 主章 | 14 | ~28（各 2 session）|
| ⭐⭐ Tier 1 + pointer | 3 | ~2（各 0.5–1）|
| ⭐ Tier 1（精簡 / 輕量）| 15 | ~8（各 0.5）|
| **總計** | **36** | **~50 session**（不含技術棧 PoC 初期 ~3）|

---

## S12+ 批次計畫（三批排程）

### 🚀 首批 — 核心骨架旗艦（2 個 Tier 3 旗艦，6 session）

完成後可宣稱「**全書互動式教材核心骨架 80%**」

| # | 連結 | Tier | 估時 | 互動類型 | 數學基底 | 跨章 pointer | 狀態 |
|---|------|------|------|----------|----------|--------------|------|
| 1 | [ch04 V-02 MM4 外積累加 + Mona Lisa SVD demo](ch04-mat-mat.md#vizscript-02) | ⭐⭐⭐ T3 旗艦 | 3s | 累加動畫 + 圖像 demo + 秩截斷 slider | (MM4) | → 影響全 §6 五分解 V-01 | ⏳ |
| 2 | [ch06f V-01 SVD 完整互動 + 4 應用切換](ch06f-USV.md#vizscript-01) | ⭐⭐⭐ T3 旗艦 | 3s | dashboard + 4 應用切換（壓縮/PCA/降噪/推薦）| SVD + (P4) + (MM4) | ↔ ch04 V-02 + ch05 V-03（雙 pointer，全書唯一）| ⏳ |

### 📚 次批 — 教材首頁 + 4 子空間 + §6 主章（9 個，~19 session）

完成後「**全書主互動 + 教材首頁就緒**」

| # | 連結 | Tier | 估時 | 互動類型 | 數學基底 | 跨章 pointer | 狀態 |
|---|------|------|------|----------|----------|--------------|------|
| 3 | [appendix-matrix-world V-01 矩陣世界索引地圖](appendix-matrix-world.md#vizscript-01) | ⭐⭐⭐ T2 旗艦 | 4s | **11 層同心橢圓 + 13 段 dashboard**（S12+ 教材首頁）| 全書統合 | → 全書各章 + ch06a V-01（互補）| ⏳ |
| 4 | [ch03 V-02 四個基本子空間互動式（Strang Big Picture）](ch03-mat-vec.md#vizscript-02) | ⭐⭐⭐ T3 候選 | 2–3s | 兩塊大餅圖動畫 + drag 拖曳 | 4 Subspaces + SVD | ↔ ch06f V-01 / appendix-four-subspaces V-01 | ⏳ |
| 5 | [ch06b V-01 CR 拆解 + 對偶 + RREF](ch06b-CR.md#vizscript-01) | ⭐⭐ T2 | 2s | 雙視角 toggle + 三色獨立列高亮 + RREF 動畫 | (P1) + (P2) + (MM4) + CR | ↔ ch04 V-02 + ch05 V-01（雙 pointer）| ⏳ |
| 6 | [ch06c V-01 LU 雙視角 + peeling 動畫](ch06c-LU.md#vizscript-01) | ⭐⭐ T2 | 2s | peeling/MM4 雙模式切換 + 三色秩 1 累加 | (MM4) + LU | → ch04 V-02（單 pointer）| ⏳ |
| 7 | [ch06d V-01 Gram–Schmidt + 3D 投影](ch06d-QR.md#vizscript-01) | ⭐⭐ T2 | 2s | Gram–Schmidt 逐步動畫 + 3D 投影 + (P1) 列拆解 | (P1) + QR | → ch05 V-01（單 pointer）| ⏳ |
| 8 | [ch06e V-01 譜分解 + 橢球主軸 3D](ch06e-QLQ.md#vizscript-01) | ⭐⭐ T2 | 2s | 譜分解逐項動畫 + 3D 橢球 + Pₚ 三性質 | (P4) + EVD | → ch05 V-03（單 pointer）| ⏳ |
| 9 | [ch01 V-01 矩陣四視角切換](ch01-viewing-matrix.md#vizscript-01) | ⭐⭐ T2 | 2s | 4 視角靜態切換 + cell 編輯 + walkthrough | (V1)–(V4) | — | ⏳ |
| 10 | [ch02 V-01 外積與秩 1 矩陣](ch02-vec-vec.md#vizscript-01) | ⭐⭐ T2 | 2s | 拖曳箭頭 + 秩 1 矩陣即時繪製 | Outer + Rank 1 | — | ⏳ |
| 11 | [ch05 V-01 對角矩陣統一互動](ch05-patterns.md#vizscript-01) | ⭐⭐ T2 | 2s | P1/P2/P1'/P2' 四 mode 切換 + dᵢ slider | (P1)/(P2)/(P1')/(P2') | ← ch06b V-01 + ch06d V-01 | ⏳ |

### 🎁 末批 — 剩餘 Tier 2 + Tier 1 + 附錄 pointer（25 個，~10 session）

完成後「**全書 36 個 VizScript 100% 互動**」

#### 末批 A：剩餘 Tier 2 主章（7 個，~14 session 但多可平行）

| # | 連結 | Tier | 估時 | 互動類型 | 數學基底 | 跨章 pointer | 狀態 |
|---|------|------|------|----------|----------|--------------|------|
| 12 | [ch01 V-02 矩陣維度同步重組](ch01-viewing-matrix.md#vizscript-02) | ⭐⭐ T2 | 2s | mn slider + 維度即時重畫 | (V1)–(V4) | — | ⏳ |
| 13 | [ch02 V-02 點積 vs 外積對偶切換](ch02-vec-vec.md#vizscript-02) | ⭐⭐ T2 | 2s | dot ↔ outer toggle + 2D/3D 幾何 | Dot + Outer | — | ⏳ |
| 14 | [ch03 V-01 Mv1 ↔ Mv2 視角切換](ch03-mat-vec.md#vizscript-01) | ⭐⭐ T2 | 2s | Dot/LC 兩 way toggle | (Mv1)/(Mv2) | — | ⏳ |
| 15 | [ch03 V-03 vM1 ↔ vM2 行向量切換](ch03-mat-vec.md#vizscript-03) | ⭐⭐ T2 | 0.5s | transpose 邏輯 + 連動 V-01 | (vM1)/(vM2) | ← ch03 V-01（共用引擎）| ⏳ |
| 16 | [ch04 V-01 矩陣乘以矩陣 4 視角切換](ch04-mat-mat.md#vizscript-01) | ⭐⭐ T2 | 2s | 4-way toggle 動畫 | (MM1)–(MM4) | — | ⏳ |
| 17 | [ch05 V-02 P3 動態系統互動](ch05-patterns.md#vizscript-02) | ⭐⭐ T2 | 2s | 軌跡動畫 + 微分/遞迴方程 | (P3) + EVD | ← ch06e V-01 | ⏳ |
| 18 | [ch06f V-02 奇異值降冪 + Eckart–Young](ch06f-USV.md#vizscript-02) | ⭐⭐ T2 | 2s | σ 降冪動畫 + 低秩近似誤差曲線 | SVD + Eckart–Young | ← ch06f V-01 | ⏳ |

#### 末批 B：Tier 1 + pointer（3 個，~2 session — 核心是 dashboard 控制器）

| # | 連結 | Tier | 估時 | 互動類型 | 數學基底 | 跨章 pointer | 狀態 |
|---|------|------|------|----------|----------|--------------|------|
| 19 | [ch06a V-01 五分解互動切換 dashboard](ch06a-five.md#vizscript-01) | ⭐⭐ T1+ptr | 1s | 5 分解 toggle + 形狀視覺 + 跳轉按鈕 | CR/LU/QR/EVD/SVD | → ch04 V-02 + ch05 V-02/03 + 每個 §6.x V-01 | ⏳ |
| 20 | [appendix-map-eigenvalues V-01 特徵值地圖 12 格](appendix-map-eigenvalues.md#vizscript-01) | ⭐⭐ T1+ptr | 1s | 12 格 dashboard + 拉桿 + 跳轉 | 特徵值幾何 + EVD | → ch06e V-01 + ch05 V-03 | ⏳ |
| 21 | [appendix-four-subspaces V-01 4 子空間整合 + 解 Ax=b](appendix-four-subspaces.md#vizscript-01) | ⭐⭐ T1+ptr | 0.5s | 左面板 4 子空間 + 右面板解 Ax=b 結構 + 跳轉 | 4 Subspaces + SVD + Aˆ+ | → ch03 V-02 + ch06f V-03 | ⏳ |

#### 末批 C：Tier 1 精簡 / 輕量（15 個，~7.5 session — 簡單 walkthrough）

| # | 連結 | Tier | 估時 | 互動類型 | 數學基底 | 跨章 pointer | 狀態 |
|---|------|------|------|----------|----------|--------------|------|
| 22 | [ch03 V-04 列空間軌跡掃描](ch03-mat-vec.md#vizscript-04) | ⭐ T1 | 0.5s | 軌跡掃描動畫 | 列空間 | — | ⏳ |
| 23 | [ch04 V-03 維度檢核 Shape Validator](ch04-mat-mat.md#vizscript-03) | ⭐ T1 | 0.5s | 維度即時檢核 + 內維對齊 | 矩陣維度 | — | ⏳ |
| 24 | [ch04 V-04 MM1 點積 walkthrough](ch04-mat-mat.md#vizscript-04) | ⭐ T1 | 0.5s | per-element 點積 tour | (MM1) | — | ⏳ |
| 25 | [ch05 V-03 P4 三明治結構](ch05-patterns.md#vizscript-03) | ⭐ T1 | 0.5s | UΣVᵀ slider + 即時更新 | (P4) | ← ch06e/f V-01 | ⏳ |
| 26 | [ch05 V-04 P1' 數值步進 walkthrough](ch05-patterns.md#vizscript-04) | ⭐ T1 | 0.5s | 數值步進動畫 | (P1') | — | ⏳ |
| 27 | [ch06b V-02 rank–獨立列對應動畫](ch06b-CR.md#vizscript-02) | ⭐ T1 | 0.5s | 改 A 看 r 變化 | rank + CR | — | ⏳ |
| 28 | [ch06b V-03 2×3 範例 walkthrough](ch06b-CR.md#vizscript-03) | ⭐ T1 | 0.5s | 單一範例逐步動畫 | CR | — | ⏳ |
| 29 | [ch06c V-02 高斯消去 + 解 Ax=b](ch06c-LU.md#vizscript-02) | ⭐ T1 | 0.5s | 前代 + 後代流程動畫 | LU + 解方程 | — | ⏳ |
| 30 | [ch06c V-03 3×3 LU 範例 walkthrough](ch06c-LU.md#vizscript-03) | ⭐ T1 | 0.5s | 單一範例逐步 | LU | — | ⏳ |
| 31 | [ch06d V-02 3D 投影視覺](ch06d-QR.md#vizscript-02) | ⭐ T1 | 0.5s | 純 3D 投影動畫 | QR + 3D 投影 | — | ⏳ |
| 32 | [ch06d V-03 2×2 QR 範例 walkthrough](ch06d-QR.md#vizscript-03) | ⭐ T1 | 0.5s | 單一範例逐步數字 | QR | — | ⏳ |
| 33 | [ch06e V-02 Pₚ 三性質視覺驗證](ch06e-QLQ.md#vizscript-02) | ⭐ T1 | 0.5s | 投影矩陣 Pₚ 三性質驗證 | EVD + 投影 | — | ⏳ |
| 34 | [ch06e V-03 2×2 EVD 範例 walkthrough](ch06e-QLQ.md#vizscript-03) | ⭐ T1 | 0.5s | 單一範例逐步 | EVD | — | ⏳ |
| 35 | [ch06f V-03 4 子空間 SVD 構造](ch06f-USV.md#vizscript-03) | ⭐ T1 | 0.5s | 4 子空間 + SVD 基底（重用 ch03 V-02 母模板）| SVD + 4 Subspaces | ← ch03 V-02 + appendix-four-subspaces V-01 | ⏳ |
| 36 | [ch06f V-04 2×2 SVD 範例 walkthrough（Strang 經典）](ch06f-USV.md#vizscript-04) | ⭐ T1 | 0.5s | 單一範例逐步（Strang 教材經典範例）| SVD | — | ⏳ |

---

## 全 36 個 VizScript 完整總覽表（按章節順序）

> 上方按「批次」排，這裡按「章節順序」排（便於對照原書結構）。

| Ch | V | 連結 | 標題（縮短） | Tier | 批次 | 估時 | 跨章 pointer |
|---|---|------|--------------|------|------|------|--------------|
| §1 | 01 | [→](ch01-viewing-matrix.md#vizscript-01) | 矩陣的四種觀看視角（4 Ways Toggle）| T2 | 次批 | 2s | — |
| §1 | 02 | [→](ch01-viewing-matrix.md#vizscript-02) | 矩陣維度同步重組（Dimensions Synchronizer）| T2 | 末批 A | 2s | — |
| §2 | 01 | [→](ch02-vec-vec.md#vizscript-01) | 外積與秩 1 矩陣（Outer Product → Rank 1）| T2 | 次批 | 2s | — |
| §2 | 02 | [→](ch02-vec-vec.md#vizscript-02) | 點積 vs 外積對偶切換（Dot ↔ Outer Duality）| T2 | 末批 A | 2s | — |
| §3 | 01 | [→](ch03-mat-vec.md#vizscript-01) | Mv1 ↔ Mv2 視角切換 | T2 | 末批 A | 2s | — |
| §3 | 02 | [→](ch03-mat-vec.md#vizscript-02) | **四個基本子空間互動式（Strang Big Picture）** | T3 候選 | 次批 | 2–3s | ↔ ch06f V-01 / appendix-four-subspaces V-01 |
| §3 | 03 | [→](ch03-mat-vec.md#vizscript-03) | vM1 ↔ vM2 行向量切換 | T2 | 末批 A | 0.5s | ← ch03 V-01 |
| §3 | 04 | [→](ch03-mat-vec.md#vizscript-04) | 列空間軌跡掃描（Column Space Trace）| T1 | 末批 C | 0.5s | — |
| §4 | 01 | [→](ch04-mat-mat.md#vizscript-01) | 矩陣乘以矩陣 4 視角切換 | T2 | 末批 A | 2s | — |
| §4 | 02 | [→](ch04-mat-mat.md#vizscript-02) | **(MM4) 外積累加 + Mona Lisa SVD demo** | **T3 旗艦** | **首批** | 3s | → 影響全 §6 五分解 V-01 |
| §4 | 03 | [→](ch04-mat-mat.md#vizscript-03) | 維度檢核（Shape Validator）| T1 | 末批 C | 0.5s | — |
| §4 | 04 | [→](ch04-mat-mat.md#vizscript-04) | MM1 點積 walkthrough | T1 | 末批 C | 0.5s | — |
| §5 | 01 | [→](ch05-patterns.md#vizscript-01) | 對角矩陣統一互動（P1/P2/P1'/P2' Toggle）| T2 | 次批 | 2s | ← ch06b V-01 + ch06d V-01 |
| §5 | 02 | [→](ch05-patterns.md#vizscript-02) | P3 動態系統互動 | T2 | 末批 A | 2s | ← ch06e V-01 |
| §5 | 03 | [→](ch05-patterns.md#vizscript-03) | P4 三明治結構（UΣVᵀ）| T1 | 末批 C | 0.5s | ← ch06e/f V-01 |
| §5 | 04 | [→](ch05-patterns.md#vizscript-04) | P1' 數值步進 walkthrough | T1 | 末批 C | 0.5s | — |
| §6 | 01 | [→](ch06a-five.md#vizscript-01) | 五分解互動切換 dashboard | T1 + ptr | 末批 B | 1s | → ch04 V-02 + ch05 V-02/03 + §6.x V-01 |
| §6.1 | 01 | [→](ch06b-CR.md#vizscript-01) | CR 拆解 + 對偶 + RREF | T2 | 次批 | 2s | ↔ ch04 V-02 + ch05 V-01（雙 pointer）|
| §6.1 | 02 | [→](ch06b-CR.md#vizscript-02) | rank–獨立列對應動畫 | T1 | 末批 C | 0.5s | — |
| §6.1 | 03 | [→](ch06b-CR.md#vizscript-03) | 2×3 CR 範例 walkthrough | T1 | 末批 C | 0.5s | — |
| §6.2 | 01 | [→](ch06c-LU.md#vizscript-01) | LU 雙視角 + peeling 動畫 | T2 | 次批 | 2s | → ch04 V-02 |
| §6.2 | 02 | [→](ch06c-LU.md#vizscript-02) | 高斯消去 + 解 Ax=b | T1 | 末批 C | 0.5s | — |
| §6.2 | 03 | [→](ch06c-LU.md#vizscript-03) | 3×3 LU 範例 walkthrough | T1 | 末批 C | 0.5s | — |
| §6.3 | 01 | [→](ch06d-QR.md#vizscript-01) | Gram–Schmidt + 3D 投影 + (P1)| T2 | 次批 | 2s | → ch05 V-01 |
| §6.3 | 02 | [→](ch06d-QR.md#vizscript-02) | 3D 投影視覺 | T1 | 末批 C | 0.5s | — |
| §6.3 | 03 | [→](ch06d-QR.md#vizscript-03) | 2×2 QR 範例 walkthrough | T1 | 末批 C | 0.5s | — |
| §6.4 | 01 | [→](ch06e-QLQ.md#vizscript-01) | 譜分解 + 橢球主軸 3D | T2 | 次批 | 2s | → ch05 V-03 |
| §6.4 | 02 | [→](ch06e-QLQ.md#vizscript-02) | Pₚ 三性質視覺驗證 | T1 | 末批 C | 0.5s | — |
| §6.4 | 03 | [→](ch06e-QLQ.md#vizscript-03) | 2×2 EVD 範例 walkthrough | T1 | 末批 C | 0.5s | — |
| §6.5 | 01 | [→](ch06f-USV.md#vizscript-01) | **SVD Master + 4 應用切換** | **T3 旗艦** | **首批** | 3s | ↔ ch04 V-02 + ch05 V-03（雙 pointer）|
| §6.5 | 02 | [→](ch06f-USV.md#vizscript-02) | 奇異值降冪 + Eckart–Young | T2 | 末批 A | 2s | ← ch06f V-01 |
| §6.5 | 03 | [→](ch06f-USV.md#vizscript-03) | 4 子空間 SVD 構造（重用 ch03 V-02）| T1 | 末批 C | 0.5s | ← ch03 V-02 + appendix-four-subspaces |
| §6.5 | 04 | [→](ch06f-USV.md#vizscript-04) | 2×2 SVD 範例 walkthrough（Strang 經典）| T1 | 末批 C | 0.5s | — |
| App A | 01 | [→](appendix-map-eigenvalues.md#vizscript-01) | 特徵值地圖 12 格 dashboard | T1 + ptr | 末批 B | 1s | → ch06e V-01 + ch05 V-03 |
| App B | 01 | [→](appendix-matrix-world.md#vizscript-01) | **矩陣世界索引地圖（教材首頁）** | **T2 旗艦** | **次批** | 4s | → 全書各章 + ch06a V-01 |
| App C | 01 | [→](appendix-four-subspaces.md#vizscript-01) | 4 子空間整合 + 解 Ax=b | T1 + ptr | 末批 B | 0.5s | → ch03 V-02 + ch06f V-03 |

---

## 跨章 Pointer 連動圖（旗艦級 VizScript 之間的依賴）

```
                  [App B 矩陣世界索引地圖]
                  Tier 2 旗艦（教材首頁）
                  ↓ ↓ ↓ ↓ 全書索引
                  ↓
   ┌──────────────┼──────────────┐
   ↓              ↓              ↓
[ch04 V-02 MM4 + Mona Lisa]   [ch06f V-01 SVD Master]
  Tier 3 旗艦 #1                Tier 3 旗艦 #2
   ↑          ↖              ↗  ↑
   |           ↖           ↗    |
   |           (雙 pointer 全書唯一)
   |             ↖       ↗
   |              ↘     ↗
   ↑          [ch05 V-03 P4 三明治]
   ↑           (副 pointer)
   ↑
[ch06a V-01 五分解 dashboard]
  Tier 1 + pointer（§6 控制器）
   ↓ ↓ ↓ ↓ ↓
   ├→ §6.1 CR V-01  → 又指 ch04 V-02 + ch05 V-01
   ├→ §6.2 LU V-01  → 又指 ch04 V-02
   ├→ §6.3 QR V-01  → 又指 ch05 V-01
   ├→ §6.4 EVD V-01 → 又指 ch05 V-03
   └→ §6.5 SVD V-01 → ch06f V-01 旗艦（已列首批）

[ch03 V-02 4-Subspaces Strang Big Picture]
  Tier 3 候選 → 升級空間
   ↑              ↓
   |              ↓
[App C 4 子空間整合]     [ch06f V-03 4 子空間 SVD 構造]
  Tier 1 + ptr           Tier 1
   ↓
   ↓
[ch06f V-01 SVD Master 也用到 4 子空間]
```

**閱讀重點：**
- **核心骨架雙旗艦 (ch04 V-02 + ch06f V-01)** 是全書最高優先級
- **教材首頁 (App B Matrix World)** 是 S12+ 完成後讀者的入口
- **ch03 V-02 4-Subspaces** 是 Strang 標誌性視覺，與 SVD 章 + 附錄 C 三方連動
- **ch06a V-01 五分解 dashboard** 是 §6 章節控制器（Tier 1 + pointer 但連動 5 個 Tier 2 主章）
- **雙 pointer 設計只在 ch06b V-01 (CR) + ch06f V-01 (SVD)** 出現 — 對偶兩圖 + 集大成章的特例

---

## 進度追蹤（S12+ 開始實作後手動更新）

| 狀態符號 | 意義 |
|---|---|
| ⏳ | 未開始 |
| 🔨 | 實作中 |
| ✅ | 完成（含 Tier 升級記錄）|
| ⚠️ | 阻塞 / 等待依賴（如 ch06a V-01 需等 ch04 V-02 完成）|
| 🔄 | 重做 / 升級中（如 ch03 V-02 從 T3 候選升級為 T3 旗艦）|

**進度統計（即時更新）：**

```
首批：⏳⏳         (0 / 2)
次批：⏳⏳⏳⏳⏳⏳⏳⏳⏳  (0 / 9)
末批 A：⏳⏳⏳⏳⏳⏳⏳    (0 / 7)
末批 B：⏳⏳⏳            (0 / 3)
末批 C：⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳  (0 / 15)
全書：⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳⏳  (0 / 36 = 0%)
```

---

## 工件清單（S12+ 起步前必讀）

| 檔案 | 用途 |
|---|---|
| [`docs/book/VIZ-CATALOG.md`](VIZ-CATALOG.md)（本檔）| **入口 metadata 索引** — 挑題 + 跳轉 + 進度追蹤 |
| [`docs/book/BOOK.md`](BOOK.md) | 全書合併版（離線閱讀 / PDF 匯出）|
| [`docs/book/SCHEMA.md`](SCHEMA.md) | 章節 md 結構規範 |
| [`docs/book/VIZ_SCHEMA.md`](VIZ_SCHEMA.md) | VizMark 標記 + VizScript 13 段 A-M 格式 |
| ch01–ch06f 各 md 檔 | **實作詳情頁** — 每個 VizScript 的 13 段 A-M 完整劇本 |
| appendix-* 各 md 檔 | 附錄 3 個 VizScript 詳情 |
| [`docs/book/figs-png/`](figs-png/) | 50 張 PNG 原始視覺參考（含 `using XX` 標記）|
| [`docs/dev/sop/SOP_DRAFT.md`](../dev/sop/SOP_DRAFT.md) | 累積 11 個 session 寫作經驗 — S12+ 視覺化的對應 SOP 起步 |

---

## 變更歷史

| 日期 | Session | 變更 |
|---|---|---|
| 2026-05-13 | S11 | 初版生成（從各章節 md 抽取 36 個 VizScript metadata，三批排程明確化）|

