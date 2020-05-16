import numpy as np


def subgrid(grid: np.ndarray, row: int, col: int) -> np.ndarray:
    sg_row = int(row/3) * 3
    sg_col = int(col/3) * 3
    return grid[sg_row:sg_row+3, sg_col:sg_col+3]


def can_place(num: int, grid: np.ndarray, row: int, col: int) -> bool:
    if grid[row, col] or num in grid[row, :] or num in grid[:, col] or num in subgrid(grid, row, col):
        return False
    return True


def is_solved(grid: np.ndarray) -> bool:
    if not all(n in grid[row, :] for n in range(1, 10) for row in range(0, 9)):
        return False
    if not all(n in grid[:, col] for n in range(1, 10) for col in range(0, 9)):
        return False
    if not all(n in subgrid(grid, row=r, col=c) for r in [0,3,6] for c in [0,3,6] for n in range(1, 10)):
        return False
    return True
