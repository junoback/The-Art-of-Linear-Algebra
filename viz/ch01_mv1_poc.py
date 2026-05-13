# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy",
#     "plotly",
# ]
# ///

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    return go, mo, np


@app.cell
def _(mo):
    mo.md(
        r"""
        # S16 PoC Stage 2 — (Mv1) 點積觀點 + (Mv2) 線性組合觀點

        本 notebook 對應 [ch01-viewing-matrix.md](../docs/book/ch01-viewing-matrix.md) 的最小可互動版本：

        - 4 個 slider 控制矩陣 $A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}$
        - 2 個 slider 控制向量 $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$
        - 同時呈現:
          - **(Mv1) 點積觀點：** $A\mathbf{x}$ 第 $i$ 列 = $A$ 第 $i$ 橫躺行 $\cdot \mathbf{x}$
          - **(Mv2) 線性組合觀點：** $A\mathbf{x} = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2$
        """
    )
    return


@app.cell
def _(mo):
    a11 = mo.ui.slider(start=-3.0, stop=3.0, step=0.1, value=2.0, label="a11")
    a12 = mo.ui.slider(start=-3.0, stop=3.0, step=0.1, value=1.0, label="a12")
    a21 = mo.ui.slider(start=-3.0, stop=3.0, step=0.1, value=0.5, label="a21")
    a22 = mo.ui.slider(start=-3.0, stop=3.0, step=0.1, value=1.5, label="a22")
    x1 = mo.ui.slider(start=-3.0, stop=3.0, step=0.1, value=1.0, label="x1")
    x2 = mo.ui.slider(start=-3.0, stop=3.0, step=0.1, value=1.0, label="x2")
    return a11, a12, a21, a22, x1, x2


@app.cell
def _(a11, a12, a21, a22, mo, x1, x2):
    mo.hstack(
        [
            mo.vstack([mo.md("**矩陣 A**"), a11, a12, a21, a22]),
            mo.vstack([mo.md("**向量 x**"), x1, x2]),
        ],
        justify="start",
        gap=2.0,
    )
    return


@app.cell
def _(a11, a12, a21, a22, np, x1, x2):
    A = np.array([[a11.value, a12.value], [a21.value, a22.value]])
    x = np.array([x1.value, x2.value])
    Ax = A @ x
    col1 = A[:, 0]
    col2 = A[:, 1]
    row1_dot_x = float(A[0] @ x)
    row2_dot_x = float(A[1] @ x)
    return A, Ax, col1, col2, row1_dot_x, row2_dot_x, x


@app.cell
def _(A, Ax, col1, col2, mo, row1_dot_x, row2_dot_x, x):
    mo.md(
        rf"""
        ## 即時計算

        $$
        A = \begin{{bmatrix}} {A[0,0]:.2f} & {A[0,1]:.2f} \\ {A[1,0]:.2f} & {A[1,1]:.2f} \end{{bmatrix}}, \quad
        \mathbf{{x}} = \begin{{bmatrix}} {x[0]:.2f} \\ {x[1]:.2f} \end{{bmatrix}}, \quad
        A\mathbf{{x}} = \begin{{bmatrix}} {Ax[0]:.3f} \\ {Ax[1]:.3f} \end{{bmatrix}}
        $$

        ### (Mv1) 點積觀點

        - 第 1 列 = $({A[0,0]:.2f})({x[0]:.2f}) + ({A[0,1]:.2f})({x[1]:.2f}) = {row1_dot_x:.3f}$
        - 第 2 列 = $({A[1,0]:.2f})({x[0]:.2f}) + ({A[1,1]:.2f})({x[1]:.2f}) = {row2_dot_x:.3f}$

        ### (Mv2) 線性組合觀點

        $$A\mathbf{{x}} = {x[0]:.2f} \begin{{bmatrix}} {col1[0]:.2f} \\ {col1[1]:.2f} \end{{bmatrix}} + {x[1]:.2f} \begin{{bmatrix}} {col2[0]:.2f} \\ {col2[1]:.2f} \end{{bmatrix}} = \begin{{bmatrix}} {Ax[0]:.3f} \\ {Ax[1]:.3f} \end{{bmatrix}}$$
        """
    )
    return


@app.cell
def _(Ax, col1, col2, go, mo, x):
    def _arrow(fig, vec, color, name, dash="solid"):
        fig.add_annotation(
            ax=0,
            ay=0,
            axref="x",
            ayref="y",
            x=float(vec[0]),
            y=float(vec[1]),
            xref="x",
            yref="y",
            showarrow=True,
            arrowhead=3,
            arrowsize=1.5,
            arrowwidth=2,
            arrowcolor=color,
        )
        fig.add_trace(
            go.Scatter(
                x=[0, float(vec[0])],
                y=[0, float(vec[1])],
                mode="lines",
                line=dict(color=color, width=3, dash=dash),
                name=name,
                showlegend=True,
                hovertemplate=f"{name}: (%{{x:.2f}}, %{{y:.2f}})<extra></extra>",
            )
        )

    pts = [x, col1, col2, Ax]
    extent = max(3.0, max(max(abs(float(p[0])), abs(float(p[1]))) for p in pts)) + 0.5

    fig = go.Figure()

    # (Mv2) parallelogram of x1*col1 + x2*col2
    p1 = (x[0] * col1).tolist()
    p2 = Ax.tolist()
    p3 = (x[1] * col2).tolist()
    fig.add_trace(
        go.Scatter(
            x=[0.0, p1[0], p2[0], p3[0], 0.0],
            y=[0.0, p1[1], p2[1], p3[1], 0.0],
            mode="lines",
            line=dict(color="rgba(255, 200, 100, 0.6)", width=1, dash="dot"),
            fill="toself",
            fillcolor="rgba(255, 200, 100, 0.15)",
            name="(Mv2) 平行四邊形",
            showlegend=True,
            hoverinfo="skip",
        )
    )

    _arrow(fig, x, "#1f77b4", "x")
    _arrow(fig, col1, "#2ca02c", "a1 (A 第 1 column)")
    _arrow(fig, col2, "#d62728", "a2 (A 第 2 column)")
    _arrow(fig, Ax, "#9467bd", "Ax", dash="dash")

    fig.update_layout(
        title="(Mv2) 線性組合視覺化：Ax = x1·a1 + x2·a2",
        xaxis=dict(
            range=[-extent, extent],
            scaleanchor="y",
            scaleratio=1,
            zeroline=True,
            zerolinecolor="lightgray",
        ),
        yaxis=dict(range=[-extent, extent], zeroline=True, zerolinecolor="lightgray"),
        width=600,
        height=600,
        showlegend=True,
        legend=dict(x=0.02, y=0.98),
        plot_bgcolor="white",
    )

    mo.ui.plotly(fig)
    return


if __name__ == "__main__":
    app.run()
