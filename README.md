# sudoku

To entertain myself while watching a children's movie, I made this simple sudoku solver. Approach: backtracking. 

Possible improvements:

* Rather than naively go through all cells, first find the empty ones, and then sort them in increasing order of likely "freedom", e.g. start with cells whose col/row/square are most filled up. Then fill them up in that order. 
* Keep track of how much backtracking was done for each solution. I guess this can be an indicator of "difficulty"



## Example usage

```python
import numpy as np
import sudoku
from textwrap import dedent

# Conveniently enter sudoku grid as a string and convert it to a numpy array
g = sudoku.grid_from_str(dedent("""\
120006000
456000123
000123000
234560001
000091034
000200067
000608912
678000000
000000000"""))

# Solve, and print each solution as soon as it is found
# (Depending on your start sudoku grid, there can in principle be more than one solution)
for sol in sudoku.solve(g):
    print(sudoku.grid_to_str(sol))
    print('---------')    

```

