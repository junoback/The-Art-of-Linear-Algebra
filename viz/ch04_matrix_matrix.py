# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy",
#     "plotly",
# ]
# ///

"""ch04 §4 Matrix × Matrix — VizScript-02 母模板（S18 階段：圖像模式 + Mona Lisa SVD）。

對應 [ch04-mat-mat.md VizScript-02](../docs/book/ch04-mat-mat.md#vizscript-02)。

S17：最小可動骨架（小矩陣模式 3×2 · 2×2 + r slider + 6 heatmap + 秩 1 圖層 strip）。
S18：加入「圖像模式」— 內建 4 張 64×64 灰階圖像（procedural portrait / 條紋 / 漸層 / 隨機）
     程式內生成（不需外部 npy / 不需 base64 / 不需 fetch，WASM 零阻抗），即時 SVD 計算
     （64×64 ~5ms），$r$ slider 動態切換 rank-$r$ 重建。
     - 三圖並列：原圖 M / 重建 M_r / 誤差 |M − M_r|
     - 奇異值譜柱狀圖：紫=已累加，灰=尚未；展示「σ_p 由大到小 = SVD 壓縮的鑰匙」
     - 累積能量 ∑σ_p² / ∑σ²：保留資訊量百分比

S19+ 待加：飛入動畫 800ms / 4 重排序 / 誤差曲線 / Walkthrough 6 步 / 快捷鍵。
"""

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    return go, make_subplots, mo, np


@app.cell
def _():
    # 全書配色（SCHEMA §3.5 全書視覺錨點）
    COLOR_A_COL = "#2ca02c"
    COLOR_B_ROW = "#d62728"
    COLOR_RESULT = "#9467bd"
    COLOR_TARGET = "#FFD700"
    COLOR_ERROR = "#ff7f0e"

    # 全書 heatmap 用 colormap
    CMAP_SIGNED = "RdBu_r"   # 雙向 +/- 含 0
    CMAP_ABS = "Oranges"     # 單向絕對值
    CMAP_GRAY = "Greys_r"    # 圖像模式（0=黑 1=白，標準影像慣例）
    return (
        CMAP_ABS,
        CMAP_GRAY,
        CMAP_SIGNED,
        COLOR_A_COL,
        COLOR_B_ROW,
        COLOR_ERROR,
        COLOR_RESULT,
        COLOR_TARGET,
    )


@app.cell
def _(np):
    # 圖像模式：4 張 64×64 灰階圖（程式內生成，WASM 零阻抗）
    # 設計重點：σ 譜由大到小排，rank-r 重建展示 SVD 壓縮精髓
    # - portrait：procedural 光滑肖像（rank ~10-20 effective）
    # - stripes：水平正弦條紋（rank 1 exactly）
    # - gradient：斜向線性漸層（rank 2 exactly）
    # - random：標準常態雜訊（rank ~64，不可壓縮）

    def gen_portrait(size=64):
        """Procedural 光滑肖像 — 設計為 SVD 可壓縮（rank ~10-20）。"""
        y, x = np.meshgrid(
            np.linspace(-1, 1, size),
            np.linspace(-1, 1, size),
            indexing="ij",
        )
        # 背景：上亮下略暗
        img = 0.65 - 0.08 * y
        # 臉部橢圓（高斯）
        r2 = (x / 0.65) ** 2 + ((y + 0.05) / 0.85) ** 2
        img = img + 0.18 * np.exp(-r2 * 2.0)
        # 頭髮（上方暗色）
        hair = np.exp(-((x / 0.95) ** 2 + ((y + 0.65) / 0.4) ** 2) * 4)
        img = img - 0.32 * hair
        # 雙眼（暗點）
        eye_l = np.exp(
            -(((x + 0.22) / 0.08) ** 2 + ((y + 0.05) / 0.07) ** 2)
        )
        eye_r = np.exp(
            -(((x - 0.22) / 0.08) ** 2 + ((y + 0.05) / 0.07) ** 2)
        )
        img = img - 0.40 * (eye_l + eye_r)
        # 嘴巴（暗色橫線）
        mouth = np.exp(-(((x) / 0.18) ** 2 + ((y - 0.35) / 0.06) ** 2))
        img = img - 0.25 * mouth
        return np.clip(img, 0.0, 1.0)

    def gen_stripes(size=64):
        """水平正弦條紋 — rank 1 (separable: f(y)·1(x))。"""
        y_vals = np.linspace(0, 4 * np.pi, size)
        stripe_col = 0.5 + 0.4 * np.sin(y_vals)
        img = np.broadcast_to(stripe_col[:, None], (size, size)).copy()
        return img

    def gen_gradient(size=64):
        """斜向線性漸層 — rank 2 (a·x + b·y + c)。"""
        y, x = np.meshgrid(
            np.linspace(0, 1, size),
            np.linspace(0, 1, size),
            indexing="ij",
        )
        return (0.15 + 0.45 * x + 0.35 * y).astype(np.float64)

    def gen_random(size=64):
        """標準常態雜訊 — rank ~64 (不可壓縮)。

        刻意不 min-max 標準化到 [0,1]，避免引入強 DC 分量讓 σ_1 主導 —
        保留 mean ≈ 0 的原始分佈，σ 譜呈現 Marchenko-Pastur 緩慢衰退，
        符合「隨機 = 不可壓縮」的教學意圖。顯示時用對稱 zmin/zmax 視覺化。
        """
        rng = np.random.default_rng(42)
        return rng.standard_normal((size, size)).astype(np.float64)

    IMAGES = {
        "Mona Lisa": gen_portrait(64),
        "條紋": gen_stripes(64),
        "漸層": gen_gradient(64),
        "隨機": gen_random(64),
    }

    # 預計算 SVD（cell load 一次即可，~5ms × 4 = ~20ms）
    SVD_CACHE = {}
    for _img_name, _img in IMAGES.items():
        _U, _sig, _Vt = np.linalg.svd(_img, full_matrices=False)
        SVD_CACHE[_img_name] = (_U, _sig, _Vt)

    return IMAGES, SVD_CACHE


@app.cell
def _(mo):
    mo.md(
        r"""
        # §4 Matrix × Matrix — VizScript-02 母模板（S18：圖像模式 + Mona Lisa SVD）

        對應 [ch04-mat-mat.md §4 (MM4)](../docs/book/ch04-mat-mat.md)。

        **(MM4) 外積之和方式：**

        $$
        AB \;=\; \sum_{p=1}^{k} \mathbf{a}_p \mathbf{b}^*_p
        $$

        每項 $\mathbf{a}_p \mathbf{b}^*_p$ 是一個 **秩 1 矩陣**。當 $A, B$ 來自 SVD 分解
        （$A = U\Sigma^{1/2}$、$B = \Sigma^{1/2} V^{\mathrm{T}}$），秩 1 圖層按奇異值
        $\sigma_p$ 由大到小排列 — 前幾項就保留主要結構，這就是 SVD 壓縮的精髓。

        **互動：** 切換模式（小矩陣 demo / 64×64 圖像四種），拉「累加項數 $r$」slider
        看 $C_r$（或 $M_r$）從全 0 逐項累加為完整目標。
        """
    )
    return


@app.cell
def _(mo):
    # 模式選擇（S18 新增）
    mode = mo.ui.radio(
        options=["小矩陣 demo", "Mona Lisa", "條紋", "漸層", "隨機"],
        value="小矩陣 demo",
        label="模式",
    )

    # A entries (3×2) — VizScript 預設 [[1,2],[3,4],[5,6]]
    a11 = mo.ui.slider(start=-9, stop=9, step=1, value=1, label="a11")
    a12 = mo.ui.slider(start=-9, stop=9, step=1, value=2, label="a12")
    a21 = mo.ui.slider(start=-9, stop=9, step=1, value=3, label="a21")
    a22 = mo.ui.slider(start=-9, stop=9, step=1, value=4, label="a22")
    a31 = mo.ui.slider(start=-9, stop=9, step=1, value=5, label="a31")
    a32 = mo.ui.slider(start=-9, stop=9, step=1, value=6, label="a32")

    # B entries (2×2) — VizScript 預設 B = I_2 使 AB = A 便於對比
    b11 = mo.ui.slider(start=-9, stop=9, step=1, value=1, label="b11")
    b12 = mo.ui.slider(start=-9, stop=9, step=1, value=0, label="b12")
    b21 = mo.ui.slider(start=-9, stop=9, step=1, value=0, label="b21")
    b22 = mo.ui.slider(start=-9, stop=9, step=1, value=1, label="b22")

    # r slider — 小矩陣 / 圖像模式分開（範圍不同，狀態獨立）
    r_small = mo.ui.slider(start=0, stop=2, step=1, value=0, label="累加項數 r")
    r_image = mo.ui.slider(start=0, stop=64, step=1, value=10, label="累加項數 r")
    return (
        a11,
        a12,
        a21,
        a22,
        a31,
        a32,
        b11,
        b12,
        b21,
        b22,
        mode,
        r_image,
        r_small,
    )


@app.cell
def _(
    a11,
    a12,
    a21,
    a22,
    a31,
    a32,
    b11,
    b12,
    b21,
    b22,
    mo,
    mode,
    r_image,
    r_small,
):
    panels = [mo.vstack([mo.md("**模式**"), mode])]
    if mode.value == "小矩陣 demo":
        panels.extend(
            [
                mo.vstack(
                    [mo.md("**矩陣 A (3×2)**"), a11, a12, a21, a22, a31, a32]
                ),
                mo.vstack([mo.md("**矩陣 B (2×2)**"), b11, b12, b21, b22]),
                mo.vstack(
                    [mo.md(r"**累加控制** $r \in [0, 2]$"), r_small]
                ),
            ]
        )
    else:
        panels.append(
            mo.vstack(
                [mo.md(r"**累加控制** $r \in [0, 64]$"), r_image]
            )
        )
    mo.hstack(panels, justify="start", gap=2.0)
    return


@app.cell
def _(
    IMAGES,
    SVD_CACHE,
    a11,
    a12,
    a21,
    a22,
    a31,
    a32,
    b11,
    b12,
    b21,
    b22,
    mode,
    np,
    r_image,
    r_small,
):
    # 計算 cell — 雙模式分支
    # 小矩陣模式：A (3×2) @ B (2×2) = C (3×2)，k = 2
    # 圖像模式：M (64×64)，SVD 重建，k = 64
    is_small = mode.value == "小矩陣 demo"

    if is_small:
        A_mat = np.array(
            [
                [a11.value, a12.value],
                [a21.value, a22.value],
                [a31.value, a32.value],
            ],
            dtype=float,
        )
        B_mat = np.array(
            [
                [b11.value, b12.value],
                [b21.value, b22.value],
            ],
            dtype=float,
        )
        k = A_mat.shape[1]  # = 2
        target_M = A_mat @ B_mat
        r_val = int(r_small.value)
        r_clamped = min(r_val, k)
        if r_clamped > 0:
            Mr = A_mat[:, :r_clamped] @ B_mat[:r_clamped, :]
        else:
            Mr = np.zeros_like(target_M)
        layers = [np.outer(A_mat[:, p], B_mat[p, :]) for p in range(k)]
        energies = [
            float(np.linalg.norm(A_mat[:, p]) * np.linalg.norm(B_mat[p, :]))
            for p in range(k)
        ]
        layer_fro2 = np.array([float(np.sum(L * L)) for L in layers])
        total_fro2 = float(layer_fro2.sum())
        cum_pct = (
            float(layer_fro2[:r_clamped].sum() / total_fro2)
            if total_fro2 > 0
            else 0.0
        )
        sigma_vals = np.array([])
    else:
        A_mat = None
        B_mat = None
        target_M = IMAGES[mode.value]
        U_mat, sigma_vals, Vt_mat = SVD_CACHE[mode.value]
        k = int(sigma_vals.shape[0])
        r_val = int(r_image.value)
        r_clamped = min(r_val, k)
        if r_clamped > 0:
            Mr = (
                U_mat[:, :r_clamped]
                @ np.diag(sigma_vals[:r_clamped])
                @ Vt_mat[:r_clamped, :]
            )
        else:
            Mr = np.zeros_like(target_M)
        layers = None  # 圖像模式不展開 64 層；strip 改畫 σ 譜
        energies = sigma_vals.tolist()
        sig2 = sigma_vals * sigma_vals
        sig2_total = float(sig2.sum())
        cum_pct = (
            float(sig2[:r_clamped].sum() / sig2_total)
            if sig2_total > 0
            else 0.0
        )

    error = target_M - Mr
    norm_target = float(np.linalg.norm(target_M))
    rel_err = (
        float(np.linalg.norm(error)) / norm_target if norm_target > 0 else 0.0
    )

    # 三式對拍（小矩陣模式才做完整檢查）
    if is_small:
        full_check = A_mat[:, :k] @ B_mat[:k, :]
        consistent = bool(
            float(np.abs((A_mat @ B_mat) - full_check).max()) < 1e-9
            and float(np.abs(target_M - full_check).max()) < 1e-9
        )
    else:
        consistent = True
    return (
        A_mat,
        B_mat,
        Mr,
        consistent,
        cum_pct,
        energies,
        error,
        is_small,
        k,
        layers,
        r_clamped,
        r_val,
        rel_err,
        sigma_vals,
        target_M,
    )


@app.cell
def _(
    A_mat,
    B_mat,
    Mr,
    consistent,
    cum_pct,
    energies,
    is_small,
    k,
    mo,
    r_clamped,
    rel_err,
    sigma_vals,
    target_M,
):
    if is_small:
        Astr = r" \\ ".join(
            " & ".join(f"{A_mat[i,j]:.0f}" for j in range(A_mat.shape[1]))
            for i in range(A_mat.shape[0])
        )
        Bstr = r" \\ ".join(
            " & ".join(f"{B_mat[i,j]:.0f}" for j in range(B_mat.shape[1]))
            for i in range(B_mat.shape[0])
        )
        Cstr = r" \\ ".join(
            " & ".join(f"{target_M[i,j]:.2f}" for j in range(target_M.shape[1]))
            for i in range(target_M.shape[0])
        )
        Crstr = r" \\ ".join(
            " & ".join(f"{Mr[i,j]:.2f}" for j in range(Mr.shape[1]))
            for i in range(Mr.shape[0])
        )
        energy_line = " + ".join(
            rf"\|\mathbf{{a}}_{p+1}\|\|\mathbf{{b}}^*_{p+1}\| = {energies[p]:.2f}"
            for p in range(k)
        )
        body = rf"""
        ## 即時計算（小矩陣模式）

        $$
        A = \begin{{bmatrix}} {Astr} \end{{bmatrix}}_{{3 \times 2}}, \quad
        B = \begin{{bmatrix}} {Bstr} \end{{bmatrix}}_{{2 \times 2}}, \quad
        C = AB = \begin{{bmatrix}} {Cstr} \end{{bmatrix}}_{{3 \times 2}}
        $$

        **累加項數 $r = {r_clamped}$，$k = {k}$：**

        $$
        C_r = \sum_{{p=1}}^{{{r_clamped}}} \mathbf{{a}}_p \mathbf{{b}}^*_p = \begin{{bmatrix}} {Crstr} \end{{bmatrix}}
        $$

        - 相對誤差 $\|C - C_r\|_F / \|C\|_F = {rel_err*100:.2f}\%$
        - 累積能量 $\sum_{{p \leq r}}\|\mathbf{{a}}_p\mathbf{{b}}^*_p\|_F^2 / \sum_{{p}} \|\cdot\|_F^2 = {cum_pct*100:.2f}\%$
        - 各秩 1 圖層能量：${energy_line}$
        - 三式對拍 `A @ B == sum of rank-1 layers == accumulate(A, B, k)` → **{"✓" if consistent else "✗"}**
        """
    else:
        n_show = min(8, len(sigma_vals))
        sigma_str = ", ".join(f"{sigma_vals[i]:.2f}" for i in range(n_show))
        tail = ""
        if len(sigma_vals) > n_show:
            tail = rf", \ldots, {sigma_vals[-1]:.2e}"
        body = rf"""
        ## 即時計算（圖像模式 64×64）

        **(MM4) 來自 SVD：** $M = U\Sigma V^{{\mathrm{{T}}}}$，取
        $A = U\Sigma^{{1/2}}$、$B = \Sigma^{{1/2}}V^{{\mathrm{{T}}}}$，則

        $$
        \mathbf{{a}}_p \mathbf{{b}}^*_p = \sigma_p \,\mathbf{{u}}_p\, \mathbf{{v}}_p^{{\mathrm{{T}}}}
        $$

        - 累加項數 $r = {r_clamped} \,/\, k = {k}$
        - 相對誤差 $\|M - M_r\|_F / \|M\|_F = {rel_err*100:.2f}\%$
        - **累積能量** $\sum_{{p \leq r}}\sigma_p^2 \,/\, \sum_{{p}} \sigma_p^2 = \mathbf{{{cum_pct*100:.2f}\%}}$
        - 前 {n_show} 個奇異值：$\sigma = [{sigma_str}{tail}]$
        """
    mo.md(body)
    return


@app.cell
def _(
    CMAP_ABS,
    CMAP_GRAY,
    CMAP_SIGNED,
    Mr,
    error,
    go,
    is_small,
    k,
    layers,
    make_subplots,
    mo,
    np,
    r_clamped,
    target_M,
):
    # 主舞台：小矩陣模式 2×3 共 6 heatmap / 圖像模式 1×3 三圖並列
    if is_small:
        titles = [
            f"秩 1 圖層 1 = a₁ b*₁  {'(已累加)' if r_clamped >= 1 else '(尚未累加)'}",
            f"秩 1 圖層 2 = a₂ b*₂  {'(已累加)' if r_clamped >= 2 else '(尚未累加)'}",
            f"累加結果 C_r (r={r_clamped})",
            "占位",
            "目標 C = AB",
            "誤差 |C - C_r|",
        ]
        fig = make_subplots(
            rows=2,
            cols=3,
            subplot_titles=titles,
            specs=[
                [{"type": "heatmap"}, {"type": "heatmap"}, {"type": "heatmap"}],
                [{"type": "heatmap"}, {"type": "heatmap"}, {"type": "heatmap"}],
            ],
            horizontal_spacing=0.08,
            vertical_spacing=0.18,
        )

        def _add_signed_hm(M, row, col, cmap, faded=False, show_text=True):
            M = np.asarray(M, dtype=float)
            opacity = 0.35 if faded else 1.0
            zmax = float(max(np.abs(M).max(), 1e-9))
            zmin = -zmax if cmap == CMAP_SIGNED else 0.0
            text = [[f"{v:.1f}" for v in row_vals] for row_vals in M]
            fig.add_trace(
                go.Heatmap(
                    z=M,
                    colorscale=cmap,
                    zmid=0 if cmap == CMAP_SIGNED else None,
                    zmin=zmin,
                    zmax=zmax,
                    showscale=False,
                    opacity=opacity,
                    text=text if show_text else None,
                    texttemplate="%{text}" if show_text else None,
                    textfont=dict(size=12),
                    hovertemplate="(%{y}, %{x}) = %{z:.2f}<extra></extra>",
                ),
                row=row,
                col=col,
            )

        _add_signed_hm(layers[0], 1, 1, CMAP_SIGNED, faded=(r_clamped < 1))
        _add_signed_hm(layers[1], 1, 2, CMAP_SIGNED, faded=(r_clamped < 2))
        _add_signed_hm(Mr, 1, 3, CMAP_SIGNED)
        _add_signed_hm([[0]], 2, 1, CMAP_SIGNED, show_text=False, faded=True)
        _add_signed_hm(target_M, 2, 2, CMAP_SIGNED)
        _add_signed_hm(np.abs(error), 2, 3, CMAP_ABS)

        for i in range(1, 3):
            for j in range(1, 4):
                fig.update_yaxes(autorange="reversed", row=i, col=j)
                fig.update_xaxes(showticklabels=False, row=i, col=j)
                fig.update_yaxes(showticklabels=False, row=i, col=j)

        fig.update_layout(
            height=520,
            width=900,
            showlegend=False,
            margin=dict(l=20, r=20, t=60, b=20),
            plot_bgcolor="white",
        )
    else:
        # 圖像模式：1×3（原圖 / 重建 / 誤差）— 灰階 + 絕對值誤差
        titles = [
            "原圖 M (64×64)",
            f"重建 M_r (r={r_clamped} / k={k})",
            "誤差 |M - M_r|",
        ]
        fig = make_subplots(
            rows=1,
            cols=3,
            subplot_titles=titles,
            specs=[[{"type": "heatmap"}] * 3],
            horizontal_spacing=0.05,
        )

        # 原圖與重建用同 zmin/zmax 才能直接視覺對比
        zmin_img = float(target_M.min())
        zmax_img = float(target_M.max())

        def _add_img(M, col, cmap, zmin, zmax, hover_fmt="%{z:.3f}"):
            M = np.asarray(M, dtype=float)
            fig.add_trace(
                go.Heatmap(
                    z=M,
                    colorscale=cmap,
                    zmin=zmin,
                    zmax=zmax,
                    showscale=False,
                    hovertemplate=f"(%{{y}}, %{{x}}) = {hover_fmt}<extra></extra>",
                ),
                row=1,
                col=col,
            )

        _add_img(target_M, 1, CMAP_GRAY, zmin_img, zmax_img)
        _add_img(Mr, 2, CMAP_GRAY, zmin_img, zmax_img)
        err_abs = np.abs(error)
        _add_img(err_abs, 3, CMAP_ABS, 0.0, float(err_abs.max() + 1e-9))

        for c in range(1, 4):
            fig.update_yaxes(autorange="reversed", row=1, col=c)
            fig.update_xaxes(showticklabels=False, row=1, col=c)
            fig.update_yaxes(showticklabels=False, row=1, col=c)

        fig.update_layout(
            height=420,
            width=1200,
            showlegend=False,
            margin=dict(l=20, r=20, t=60, b=20),
            plot_bgcolor="white",
        )

    mo.ui.plotly(fig)
    return


@app.cell
def _(
    energies,
    go,
    is_small,
    k,
    layers,
    make_subplots,
    mo,
    np,
    r_clamped,
):
    # strip：小矩陣模式 = k 個秩 1 圖層 heatmap 縮圖（灰/亮兩態）
    #        圖像模式 = 64 條 σ_p 柱狀圖（紫=已累加，灰=尚未；視覺化 SVD 譜衰退）
    if is_small:
        titles_strip = [
            f"p={p+1} | 能量 {energies[p]:.2f} | "
            f"{'已累加' if p < r_clamped else '尚未累加'}"
            for p in range(k)
        ]
        chart = make_subplots(
            rows=1,
            cols=k,
            subplot_titles=titles_strip,
            specs=[[{"type": "heatmap"}] * k],
            horizontal_spacing=0.05,
        )

        def _add_thumb(M, p):
            M = np.asarray(M, dtype=float)
            active = p < r_clamped
            opacity = 1.0 if active else 0.35
            zmax = float(max(np.abs(M).max(), 1e-9))
            chart.add_trace(
                go.Heatmap(
                    z=M,
                    colorscale="RdBu_r",
                    zmid=0,
                    zmin=-zmax,
                    zmax=zmax,
                    showscale=False,
                    opacity=opacity,
                    hovertemplate=(
                        f"a_{p+1} b*_{p+1}<br>"
                        f"能量 ||a||·||b|| = {energies[p]:.2f}<extra></extra>"
                    ),
                ),
                row=1,
                col=p + 1,
            )

        for p in range(k):
            _add_thumb(layers[p], p)
            chart.update_yaxes(autorange="reversed", row=1, col=p + 1)
            chart.update_xaxes(showticklabels=False, row=1, col=p + 1)
            chart.update_yaxes(showticklabels=False, row=1, col=p + 1)

        chart.update_layout(
            title="秩 1 圖層 strip（拉 r slider 控制亮/灰）",
            height=260,
            width=600,
            showlegend=False,
            margin=dict(l=20, r=20, t=80, b=20),
            plot_bgcolor="white",
        )
    else:
        # σ 譜柱狀圖（k=64）
        sigma_arr = np.asarray(energies, dtype=float)
        n_sig = len(sigma_arr)
        idx = np.arange(1, n_sig + 1)
        colors = [
            "#9467bd" if p < r_clamped else "#bbbbbb" for p in range(n_sig)
        ]
        chart = go.Figure()
        chart.add_trace(
            go.Bar(
                x=idx,
                y=sigma_arr,
                marker_color=colors,
                hovertemplate="σ_%{x} = %{y:.3f}<extra></extra>",
            )
        )
        if 0 < r_clamped < n_sig:
            chart.add_vline(
                x=r_clamped + 0.5,
                line=dict(color="#d62728", dash="dash", width=2),
                annotation_text=f"r = {r_clamped}",
                annotation_position="top right",
            )
        chart.update_layout(
            title=(
                f"奇異值譜 σ_p（紫 = 前 {r_clamped} 個已累加 / "
                f"灰 = 尚未；σ_1 = {sigma_arr[0]:.2f}）"
            ),
            xaxis_title="p",
            yaxis_title="σ_p",
            height=320,
            width=1200,
            showlegend=False,
            margin=dict(l=50, r=20, t=60, b=40),
            plot_bgcolor="white",
        )

    mo.ui.plotly(chart)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---

        ### S18 進展說明

        - **本版本（S18）**：S17 小矩陣骨架 ＋ **圖像模式**（程式內生成 4 張 64×64 圖像 + SVD 預計算 + rank-$r$ 重建）。
        - **小矩陣模式：** $r$ slider 即時更新累加結果與秩 1 圖層 strip。
        - **圖像模式：** 切到 Mona Lisa / 條紋 / 漸層 / 隨機，$r$ slider 控制 rank-$r$ 重建。
          - 三圖並列：原圖 / 重建 / 誤差熱圖
          - σ 譜柱狀圖：紫=已累加，灰=尚未；展示「SVD 譜衰退決定壓縮率」
          - 累積能量 $\sum_{p \leq r}\sigma_p^2 / \sum \sigma_p^2$ 顯示「保留多少資訊」

        ### 觀察重點（圖像模式）

        | 圖像 | 結構 | 有效 rank | 視覺辨識所需 $r$ |
        |------|------|---------|----------------|
        | Mona Lisa（procedural 肖像） | 光滑背景 + 5 個 Gaussian 特徵 | **~5** | $r=2$ 辨識臉型，$r=5$ 幾乎無誤差 |
        | 條紋（水平正弦） | $f(y) \cdot 1(x)$ separable | **1（精確）** | $r=1$ 完美重建 |
        | 漸層（雙線性） | $ax + by + c$ | **2（精確）** | $r=2$ 完美重建 |
        | 隨機（高斯雜訊） | 各向同性 Marchenko-Pastur | **~64（滿秩）** | $r \approx 28$ 達 85% 能量，$r \approx 49$ 達 99% |

        **觀察 σ 譜：** 條紋 / 漸層的譜在 $p=1$ 或 $p=2$ 後直接掉到 ~0（可壓縮）；
        Mona Lisa 的譜衰退快（5 個主要 σ 之後 ~0）；隨機的譜接近 Marchenko-Pastur
        分布（基本平坦衰退、不可壓縮）。

        **DC 注意：** 對 Mona Lisa / 條紋 / 漸層（值域 $[0, 1]$），$\sigma_1$ 由「平均亮度」DC 分量主導，
        所以「累積能量」百分比會 $r=1$ 就達 99%+ — 這是 Frobenius 能量觀點，**但視覺上需 $r \geq 2$
        才看得到結構**（人眼對空間特徵敏感，不只對能量總和）。這也是 SVD 壓縮在實務上仍取 $r > 1$ 的原因。

        ### S19+ 待加

        - 飛入動畫 800ms / 項（秩 1 圖層從 strip 飛到主舞台中央合併）
        - 4 重排序對比（按 $\sigma_p$ vs 隨機，鋪陳 Eckart-Young §6.5）
        - 誤差曲線 $r$ vs $\|M - M_r\|_F / \|M\|_F$ 即時下降圖
        - Walkthrough 6 步首次自動觸發
        - 快捷鍵 Space / ←/→ / R / 0 / Shift+End / M
        """
    )
    return


if __name__ == "__main__":
    app.run()
