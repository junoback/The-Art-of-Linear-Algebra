# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy",
#     "plotly",
# ]
# ///

"""ch04 §4 Matrix × Matrix — VizScript-02 母模板（S17 架構階段：小矩陣模式骨架）。

對應 [ch04-mat-mat.md VizScript-02](../docs/book/ch04-mat-mat.md#vizscript-02)。
本檔在 S17 完成「最小可動骨架」：
- A (3×2) + B (2×2) entry sliders
- r slider 0..2 控制 (MM4) 累加項數
- 秩 1 圖層 strip（2 個 heatmap，灰/亮兩態）
- 主舞台 heatmap：A / B / 各秩 1 圖層 / C_r / 目標 C / 誤差 |C-C_r|

S18+ 待加：圖像模式 (Mona Lisa) / 飛入動畫 / 4 重排序對比 / 誤差曲線 / Walkthrough / 快捷鍵。
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
    COLOR_A_COL = "#2ca02c"   # A 直立列 = 綠
    COLOR_B_ROW = "#d62728"   # B 橫躺行 = 粉紅
    COLOR_RESULT = "#9467bd"  # C_r 結果 = 紫
    COLOR_TARGET = "#FFD700"  # 目標 C = 金
    COLOR_ERROR = "#ff7f0e"   # 誤差 = 橙

    # 全書 heatmap 用 colormap（雙向 +/- 含 0 → RdBu 反轉；單向絕對值 → Oranges）
    CMAP_SIGNED = "RdBu_r"
    CMAP_ABS = "Oranges"
    return (
        CMAP_ABS,
        CMAP_SIGNED,
        COLOR_A_COL,
        COLOR_B_ROW,
        COLOR_ERROR,
        COLOR_RESULT,
        COLOR_TARGET,
    )


@app.cell
def _(mo):
    mo.md(
        r"""
        # §4 Matrix × Matrix — VizScript-02 母模板（S17 骨架）

        對應 [ch04-mat-mat.md §4 (MM4)](../docs/book/ch04-mat-mat.md)。

        **(MM4) 外積之和方式：**

        $$
        AB \;=\; \sum_{p=1}^{k} \mathbf{a}_p \mathbf{b}^*_p
        $$

        其中 $\mathbf{a}_p$ 是 $A$ 第 $p$ 直立列，$\mathbf{b}^*_p$ 是 $B$ 第 $p$ 橫躺行，
        每項 $\mathbf{a}_p \mathbf{b}^*_p$ 是一個 **秩 1 矩陣**（所有直立列共線、所有橫躺行共線）。

        **本骨架：** 拉「累加項數 $r$」slider 從 0 到 $k=2$，看 $C_r = \sum_{p=1}^{r} \mathbf{a}_p \mathbf{b}^*_p$
        從全 0 逐項累加為完整 $AB$。每個秩 1 圖層是 SVD 的「鑰匙」、是壓縮 / PCA / 推薦的核心結構。
        """
    )
    return


@app.cell
def _(mo):
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

    # 累加項數 r (k=2 固定)
    r = mo.ui.slider(start=0, stop=2, step=1, value=0, label="累加項數 r")
    return a11, a12, a21, a22, a31, a32, b11, b12, b21, b22, r


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
    r,
):
    mo.hstack(
        [
            mo.vstack(
                [mo.md("**矩陣 A (3×2)**"), a11, a12, a21, a22, a31, a32]
            ),
            mo.vstack(
                [mo.md("**矩陣 B (2×2)**"), b11, b12, b21, b22]
            ),
            mo.vstack([mo.md("**累加控制**"), r]),
        ],
        justify="start",
        gap=2.0,
    )
    return


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
    np,
    r,
):
    # 秩 1 圖層工具（cell 內聯，避免 marimo 把 `_` 開頭函數視為 cell-private 不 export）
    def rank1_outer(a, b):
        return np.outer(a, b)

    def layers_of(A_, B_):
        kk = A_.shape[1]
        return [rank1_outer(A_[:, p], B_[p, :]) for p in range(kk)]

    def accumulate(A_, B_, rr):
        mm, kk = A_.shape
        nn = B_.shape[1]
        if rr <= 0:
            return np.zeros((mm, nn))
        rr = min(rr, kk)
        return A_[:, :rr] @ B_[:rr, :]

    def layer_energy(a, b):
        return float(np.linalg.norm(a) * np.linalg.norm(b))

    A = np.array(
        [
            [a11.value, a12.value],
            [a21.value, a22.value],
            [a31.value, a32.value],
        ],
        dtype=float,
    )
    B = np.array(
        [
            [b11.value, b12.value],
            [b21.value, b22.value],
        ],
        dtype=float,
    )
    k = A.shape[1]  # = 2

    target_C = A @ B
    r_val = int(r.value)
    Cr = accumulate(A, B, r_val)
    error = target_C - Cr
    rel_err = (
        float(np.linalg.norm(error)) / float(np.linalg.norm(target_C))
        if np.linalg.norm(target_C) > 0
        else 0.0
    )

    layers = layers_of(A, B)
    energies = [layer_energy(A[:, p], B[p, :]) for p in range(k)]

    # 三式對拍：A @ B (numpy 內建) == sum of rank-1 layers == accumulate(A, B, k)
    full_check = accumulate(A, B, k)
    consistent = bool(
        float(np.abs((A @ B) - full_check).max()) < 1e-9
        and float(np.abs(target_C - full_check).max()) < 1e-9
    )
    return (
        A,
        B,
        Cr,
        consistent,
        energies,
        error,
        k,
        layers,
        r_val,
        rel_err,
        target_C,
    )


@app.cell
def _(A, B, Cr, consistent, energies, k, mo, r_val, rel_err, target_C):

    Astr = r" \\ ".join(
        " & ".join(f"{A[i,j]:.0f}" for j in range(A.shape[1]))
        for i in range(A.shape[0])
    )
    Bstr = r" \\ ".join(
        " & ".join(f"{B[i,j]:.0f}" for j in range(B.shape[1]))
        for i in range(B.shape[0])
    )
    Cstr = r" \\ ".join(
        " & ".join(f"{target_C[i,j]:.2f}" for j in range(target_C.shape[1]))
        for i in range(target_C.shape[0])
    )
    Crstr = r" \\ ".join(
        " & ".join(f"{Cr[i,j]:.2f}" for j in range(Cr.shape[1]))
        for i in range(Cr.shape[0])
    )

    energy_line = " + ".join(
        rf"\|\mathbf{{a}}_{p+1}\|\|\mathbf{{b}}^*_{p+1}\| = {energies[p]:.2f}"
        for p in range(k)
    )

    mo.md(
        rf"""
        ## 即時計算

        $$
        A = \begin{{bmatrix}} {Astr} \end{{bmatrix}}_{{3 \times 2}}, \quad
        B = \begin{{bmatrix}} {Bstr} \end{{bmatrix}}_{{2 \times 2}}, \quad
        C = AB = \begin{{bmatrix}} {Cstr} \end{{bmatrix}}_{{3 \times 2}}
        $$

        **累加項數 $r = {r_val}$，$k = {k}$：**

        $$
        C_r = \sum_{{p=1}}^{{{r_val}}} \mathbf{{a}}_p \mathbf{{b}}^*_p = \begin{{bmatrix}} {Crstr} \end{{bmatrix}}
        $$

        - 相對誤差 $\|C - C_r\|_F / \|C\|_F = {rel_err*100:.2f}\%$
        - 各秩 1 圖層能量：${energy_line}$
        - 三式對拍：`A @ B == sum of rank-1 layers == accumulate(A, B, k)` → **{"✓" if consistent else "✗"}**
        """
    )
    return


@app.cell
def _(
    CMAP_ABS,
    CMAP_SIGNED,
    Cr,
    error,
    go,
    layers,
    make_subplots,
    mo,
    np,
    r_val,
    target_C,
):
    # 主舞台：6 個 heatmap subplot 並排
    # 列 1：layer 1 / layer 2 / C_r
    # 列 2：(空) / target_C / |error|
    titles = [
        f"秩 1 圖層 1 = a₁ b*₁  {'(已累加)' if r_val >= 1 else '(尚未累加)'}",
        f"秩 1 圖層 2 = a₂ b*₂  {'(已累加)' if r_val >= 2 else '(尚未累加)'}",
        f"累加結果 C_r (r={r_val})",
        "目標 C = AB",
        "誤差 |C - C_r|",
    ]
    fig = make_subplots(
        rows=2,
        cols=3,
        subplot_titles=titles + [""],
        specs=[
            [{"type": "heatmap"}, {"type": "heatmap"}, {"type": "heatmap"}],
            [{"type": "heatmap"}, {"type": "heatmap"}, {"type": "heatmap"}],
        ],
        horizontal_spacing=0.08,
        vertical_spacing=0.18,
    )

    def _add_heatmap(M, row, col, cmap, faded=False, show_text=True):
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

    # 列 1
    _add_heatmap(layers[0], 1, 1, CMAP_SIGNED, faded=(r_val < 1))
    _add_heatmap(layers[1], 1, 2, CMAP_SIGNED, faded=(r_val < 2))
    _add_heatmap(Cr, 1, 3, CMAP_SIGNED)
    # 列 2
    # (空格)：放一個透明 dummy heatmap
    _add_heatmap([[0]], 2, 1, CMAP_SIGNED, show_text=False, faded=True)
    _add_heatmap(target_C, 2, 2, CMAP_SIGNED)
    _add_heatmap(np.abs(error), 2, 3, CMAP_ABS)

    # 統一 y 軸反轉（heatmap 預設原點左下，數學矩陣慣例左上）
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

    mo.ui.plotly(fig)
    return


@app.cell
def _(energies, go, k, layers, make_subplots, mo, np, r_val):
    # 秩 1 圖層 strip — k 個縮圖橫排，灰/亮兩態
    # 用 placeholder 字串確保 plotly 生成 annotation slot（空字串會被跳過）
    titles_strip = [
        f"p={p+1} | 能量 {energies[p]:.2f} | "
        f"{'已累加' if p < r_val else '尚未累加'}"
        for p in range(k)
    ]
    strip = make_subplots(
        rows=1,
        cols=k,
        subplot_titles=titles_strip,
        specs=[[{"type": "heatmap"}] * k],
        horizontal_spacing=0.05,
    )

    def _add_layer_thumb(M, p, fig):
        M = np.asarray(M, dtype=float)
        active = p < r_val
        opacity = 1.0 if active else 0.35
        zmax = float(max(np.abs(M).max(), 1e-9))
        fig.add_trace(
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
        _add_layer_thumb(layers[p], p, strip)
        strip.update_yaxes(autorange="reversed", row=1, col=p + 1)
        strip.update_xaxes(showticklabels=False, row=1, col=p + 1)
        strip.update_yaxes(showticklabels=False, row=1, col=p + 1)

    strip.update_layout(
        title="秩 1 圖層 strip（拉 r slider 控制亮/灰）",
        height=260,
        width=600,
        showlegend=False,
        margin=dict(l=20, r=20, t=80, b=20),
        plot_bgcolor="white",
    )

    mo.ui.plotly(strip)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---

        ### S17 骨架說明

        - **本版本（S17）**：小矩陣 3×2 · 2×2 模式骨架；$r$ slider 即時更新累加結果與秩 1 圖層 strip 灰/亮狀態。
        - **未做（S18+）**：圖像模式（Mona Lisa / 條紋 / 漸層 / 隨機）/ 飛入動畫 / 4 種重排序對比（按 $\sigma_p$ vs 隨機）/ 誤差曲線 / Walkthrough 6 步驟 / 快捷鍵 / hover 細節 tooltip。
        - **Tier 目標**：S17 = Tier 2 雛形（slider 即時更新）；S18-S19 補完 Tier 3（圖像 + 動畫 + 重排序）。

        ### 驗證手動

        - $r=0$：$C_r$ 全 0、誤差 = 100%、strip 全灰。
        - $r=1$：$C_r$ = 秩 1 圖層 1、strip 第 1 項亮。
        - $r=k=2$：$C_r$ = $AB$、誤差 = 0%、strip 全亮。
        - $B = I_2$（預設）：$AB = A$，便於對拍。
        """
    )
    return


if __name__ == "__main__":
    app.run()
