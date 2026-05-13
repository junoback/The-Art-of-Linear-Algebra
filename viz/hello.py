import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell
def _(mo):
    mo.md(
        r"""
        # Hello Marimo — S16 PoC Stage 1

        本 notebook 驗證:
        1. Marimo 反應式 cell 機制（slider 一動，下游 cell 自動重算）
        2. NumPy + Marimo UI 整合
        3. LaTeX 數學渲染

        > **目的：** 把 Strang / Hiranabe《The Art of Linear Algebra》轉成「app 式書籍」的技術棧 PoC。
        """
    )
    return


@app.cell
def _(mo):
    n = mo.ui.slider(start=1, stop=12, step=1, value=5, label="向量長度 n")
    n
    return (n,)


@app.cell
def _(mo, n, np):
    vec = np.arange(1, n.value + 1)
    mo.md(
        f"""
        ## 觀察反應式行為

        $$\\mathbf{{v}}_n = (1, 2, \\ldots, n) \\quad \\text{{當前 }} n = {n.value}$$

        - 向量：`{vec.tolist()}`
        - 範數 $\\|\\mathbf{{v}}\\|_2 = {np.linalg.norm(vec):.4f}$
        - 元素總和 $\\sum v_i = {int(vec.sum())}$
        """
    )
    return


if __name__ == "__main__":
    app.run()
