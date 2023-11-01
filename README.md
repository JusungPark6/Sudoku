# Sudoku
## Jusung Park


### How to Use
Type in the terminal `python3 solve_sudoku.py [map name]` to test the sudoku solving programs. Within `solve_sudoku.py` use 
```python
sat = SAT2(sys.argv[1])
result = sat.walksat()
```
if testing WalkSAT, or 
```python
sat = SAT(sys.argv[1])
result = sat.gsat()
```
if testing GSAT. Make sure to comment out the other when using one.

To test the BONUS `MinesweeperSolver.py`, type in the terminal `python3 MinesweeperSolver.py [map name]`.
Currently the only file contained is `sample_map.txt`