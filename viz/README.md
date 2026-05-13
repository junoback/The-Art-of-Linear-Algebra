# viz/ — 互動式 Python 視覺化

把 Strang / Hiranabe《The Art of Linear Algebra》16 個內容 md 中的 36 個 VizScript（主章 33 + 附錄 3）+ 22 條 Q&A 背後觀念，轉成「app 式書籍」的互動式 Python 教材。

## 技術棧（S16 PoC 確立）

- **Python 3.12**（pin 在 `.python-version`，符合 Pyodide WASM target）
- **uv** — env / 套件管理（取代 pip / poetry / conda）
- **[Marimo](https://marimo.io/)** ≥ 0.23 — 反應式 Python notebook（一動 slider 整頁自動重算）+ `marimo export html-wasm` 匯出單一靜態 HTML
- **plotly** ≥ 6 — 互動式 2D/3D 視覺化（首選）
- **matplotlib** ≥ 3.10 — 靜態 / 影像式視覺化備援
- **scikit-learn** ≥ 1.8 — PCA / KMeans / SVD 工具庫
- **Pillow** ≥ 12 — 影像處理（Mona Lisa SVD demo 等）
- **NumPy** ≥ 2.4、**SciPy** ≥ 1.17

## 為什麼選 Marimo（vs Jupyter / Streamlit / Observable）

| 對手 | 弱點 | Marimo 勝出 |
|---|---|---|
| Jupyter | 非反應式（要按 Run All）；hidden state 容易踩雷 | 自動 DAG 重算 |
| Streamlit | 需要 server，不能單檔部署 | `export html-wasm` 出來就是靜態頁 |
| Observable | JavaScript，數學庫要全部重寫 | 原生 Python，sklearn/Pillow/scipy 全可用 |

詳見 HANDOFF.md 對 S15 → S16 過渡的決策段。

## 上手

```bash
# 1. 安裝 uv（macOS）
brew install uv

# 2. clone 後進入 viz/
cd viz

# 3. 互動式開啟（瀏覽器自動跳出）
uv run marimo edit ch01_mv1_poc.py

# 4. 唯讀互動式（讀者模式 / share 給朋友）
uv run marimo run ch01_mv1_poc.py

# 5. 匯出成單一靜態 HTML（含 WASM Pyodide runtime ~27 MB）
uv run marimo export html-wasm ch01_mv1_poc.py -o dist/ch01_mv1_poc

# 6. 本地驗證 WASM 版（必須 over HTTP，不能 file://）
uv run python -m http.server --directory dist 8765
# 開 http://localhost:8765/ch01_mv1_poc/
```

## 目前 notebook

| 檔案 | 主題 | 狀態 | 對應書內章節 |
|---|---|---|---|
| `hello.py` | Marimo 反應式 + LaTeX + NumPy hello world | ✅ S16 PoC | — |
| `ch01_mv1_poc.py` | 2×2 矩陣 slider × 2D 向量 plotly 互動，同時展示 (Mv1) 點積 + (Mv2) 線性組合兩觀點 | ✅ S16 PoC | [ch01-viewing-matrix.md](../docs/book/ch01-viewing-matrix.md) |

下一批計畫（S17+）：依 [docs/book/VIZ-CATALOG.md](../docs/book/VIZ-CATALOG.md) 首批 Tier 3 旗艦：
- **ch04 V-02 MM4 + Mona Lisa SVD demo**（母模板，完成後 §6 五分解 pointer 全解鎖）
- **ch06f V-01 SVD Master**（4 應用切換：壓縮 / PCA / 降噪 / 推薦）

## 部署

`dist/<notebook>/` 是完全靜態目錄，含 Pyodide runtime + Marimo runtime + notebook bundle。可直接 push 到：

- GitHub Pages（push `dist/` 整目錄到 `gh-pages` branch）
- Cloudflare Pages / Netlify / Vercel（拖目錄即部署）

**注意：** WASM 版需 HTTP 服務，不可 `file://` 直接開（瀏覽器 CORS 限制）。

## 開發守則

- 寫 Marimo cell 時，**只在 `@app.cell` 函式內**修改邏輯，函式外的 `app = marimo.App()` / `if __name__ == "__main__": app.run()` 等樣板不要動
- 全書視覺錨點規範見 [SCHEMA.md §3.5](../docs/book/SCHEMA.md#35-全書視覺錨點s11-規範化)（配色 hex / cell 尺寸 / 動畫時間 / 3D 視角預設 `elevation=25°, azimuth=-60°`）
- VizScript 13 段 A-M 格式見 [VIZ_SCHEMA.md](../docs/book/VIZ_SCHEMA.md)
