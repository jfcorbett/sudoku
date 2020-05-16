import numpy as np
from ..solver import subgrid, can_place, is_solved
import pytest
from pathlib import Path


def test_subgrid():
    g = np.genfromtxt(Path(__file__).parent / "grid.csv", delimiter=" ", dtype=int)
    np.testing.assert_array_equal(subgrid(g, row=0, col=0), np.array([[1,2,3],[4,5,6],[7,8,9]]))
    np.testing.assert_array_equal(subgrid(g, row=8, col=0), np.array([[0,0,0],[0,0,0],[0,0,0]]))


def test_can_place():
    g = np.genfromtxt(Path(__file__).parent / "grid.csv", delimiter=" ", dtype=int)
    
    assert can_place(7, g, row=0, col=8)  # legal

    assert ~can_place(7, g, row=0, col=6)  # bad col
    assert ~can_place(7, g, row=2, col=8)  # bad row
    assert ~can_place(7, g, row=4, col=4)  # bad subgrid
    assert ~can_place(2, g, row=3, col=3)  # no vacancy


def test_is_solved():
    assert is_solved(np.genfromtxt(Path(__file__).parent / "grid_solved.csv", delimiter=" ", dtype=int))
    
    # incomplete
    assert ~is_solved(np.genfromtxt(Path(__file__).parent / "grid.csv", delimiter=" ", dtype=int))

    # illegal duplicate 1 in top left subgrid
    assert ~is_solved(np.genfromtxt(Path(__file__).parent / "grid_solved_wrong.csv", delimiter=" ", dtype=int))