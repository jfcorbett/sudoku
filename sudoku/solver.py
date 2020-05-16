import numpy as np

ROWS = COLS = range(9)
NUMS = range(1, 10)


def subgrid(grid: np.ndarray, row: int, col: int) -> np.ndarray:
    """Returns the 3x3 square to which cell (row,col) belongs"""
    sg_row = int(row/3) * 3
    sg_col = int(col/3) * 3
    return grid[sg_row:sg_row+3, sg_col:sg_col+3]


def can_place(num: int, grid: np.ndarray, row: int, col: int) -> bool:
    return ~grid[row, col] \
        and num not in grid[row, :] \
        and num not in grid[:, col] \
        and num not in subgrid(grid, row, col)


def is_solved(grid: np.ndarray) -> bool:
    if not all(n in grid[row, :] for n in NUMS for row in ROWS):
        return False
    if not all(n in grid[:, col] for n in NUMS for col in COLS):
        return False
    if not all(n in subgrid(grid, row=r, col=c) for r in [0,3,6] for c in [0,3,6] for n in NUMS):
        return False
    return True


def solve(grid: np.ndarray):

    for row in ROWS:
        for col in COLS:
            if grid[row, col]:
                continue  # cell already filled, go to next cell
            for num in NUMS:
                if can_place(num, grid, row, col):
                    grid[row, col] = num  # write num in cell
                    solve(grid)
                    if is_solved(grid):
                        # print(grid_to_str(grid) + "\n")
                        return
                    grid[row, col] = 0  # backtrack



def grid_to_str(grid: np.ndarray) -> str:
    return "\n".join("".join(str(num) for num in row) for row in grid)
    # or, equivalently:
    # nr, nc = grid.shape
    # return "\n".join("".join(str(grid[r, c]) for c in range(nc)) for r in range(nr))


def grid_from_str(s: str) -> np.ndarray:
    return np.array([[int(n) for n in sp] for sp in s.strip().split('\n')])


def read_txt(f, sep: str="") -> np.ndarray:
    return grid_from_str(open(f).read().replace(sep,""))
