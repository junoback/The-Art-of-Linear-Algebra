"""共用：秩 1 圖層相關工具（S17 架構階段先放最小骨架）。

對應 [ch04-mat-mat.md VizScript-02](../../docs/book/ch04-mat-mat.md#vizscript-02) 的 (MM4) 視覺化。

主要函數：
- `rank1_layer(a, b)`        — 給直立列 a (m,) 與橫躺行 b (n,)，回傳秩 1 矩陣 a b^T (m, n)
- `accumulate(A, B, r)`      — 依 (MM4) 把 A (m, k) × B (k, n) 累加前 r 個秩 1 圖層
- `layers_of(A, B)`          — 列出 A (m, k) × B (k, n) 的全部 k 個秩 1 圖層 list of (m, n)
- `layer_energy(a, b)`       — 該秩 1 圖層的「能量」= ||a|| * ||b||（小矩陣模式用；圖像模式由 SVD σ_p 替代）

S17 不含 SVD demo / 圖像 / cache（留 S18）。
"""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


def rank1_layer(a: NDArray[np.floating], b: NDArray[np.floating]) -> NDArray[np.floating]:
    """秩 1 矩陣 a b^T，形狀 (len(a), len(b))。"""
    return np.outer(a, b)


def layers_of(A: NDArray[np.floating], B: NDArray[np.floating]) -> list[NDArray[np.floating]]:
    """A (m, k) × B (k, n) 全部 k 個秩 1 圖層；第 p 個 = A[:, p] outer B[p, :]。"""
    k = A.shape[1]
    return [rank1_layer(A[:, p], B[p, :]) for p in range(k)]


def accumulate(
    A: NDArray[np.floating], B: NDArray[np.floating], r: int
) -> NDArray[np.floating]:
    """C_r = sum_{p=1..r} a_p b^*_p。r=0 → 全 0；r=k → 完整 AB。"""
    m, k = A.shape
    n = B.shape[1]
    if r <= 0:
        return np.zeros((m, n))
    r = min(r, k)
    return A[:, :r] @ B[:r, :]


def layer_energy(a: NDArray[np.floating], b: NDArray[np.floating]) -> float:
    """秩 1 圖層能量 ||a|| * ||b||（小矩陣模式）。"""
    return float(np.linalg.norm(a) * np.linalg.norm(b))
