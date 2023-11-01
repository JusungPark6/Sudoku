# Sudoku
## Jusung Park 
### COSC 76 Fall 2023
___

Sudoku, a popular logic-based puzzle, can be effectively translated into SAT, enabling us to employ a host of SAT solvers for its solutions. Two such heuristic-based SAT solvers are GSAT and WalkSAT. Their stochastic nature provides an edge in tackling instances that deter deterministic algorithms.

## GSAT

The GSAT algorithm is a local search method that attempts to maximize the number of satisfied clauses in a given Boolean formula. The steps are as follows:

1. Choose a random assignment (a model). 
2. If the assignment satisfies all the clauses, stop. 
3. Pick a number between 0 and 1. If the number is greater than some threshold h, choose a variable uniformly at random and flip it; go back to step 2. 
4. Otherwise, for each variable, score how many clauses would be satisfied if the variable value were flipped. 
5. Uniformly at random choose one of the variables with the highest score. (There may be many tied variables.) Flip that variable. Go back to step 2.

- `read_cnf`: Parses the CNF file, generating a standardized representation for clauses and a mapping between variables and their indices.
- `evaluate`: For the current variable assignment, this method checks if all the clauses are satisfied. 
- `score_variable`: By hypothetically flipping a variable's truth value, this method calculates the potential impact on the overall formula satisfaction. It serves as a heuristic to guide the search. 
- `gsat`: This is the core GSAT algorithm. It iteratively refines the variable assignments to increase the number of satisfied clauses. To avoid local optima, the algorithm occasionally flips random variables. Otherwise, it opts to flip the variable that leads to the maximum increase in satisfied clauses.


## WalkSAT

I created a new file `SAT2.py` to implement the WalkSAT algorithm.

- `Clauses`: A SAT problem is defined by its clauses, which are parsed from a CNF file. Each clause is a list of integers, where positive integers represent literals, and negative integers denote the negation of the corresponding literal. 
- `Variable Assignments`: Every variable from the clauses is initialized with a random truth value.

- `read_clauses`: This method parses the CNF file into a standardized representation for clauses. 
- `initialize_variables`: Constructs a dictionary of variables from the clauses and assigns random initial truth values. 
- `is_clause_satisfied`: Determines if a clause is satisfied for the current assignment of truth values. 
- `get_score`: For a given variable, it calculates the potential impact on the overall formula satisfaction if its truth value is flipped. It serves as a heuristic to guide the search.

- `walksat`: This embodies the WalkSAT algorithm, refining variable assignments in an iterative process aiming to find a satisfying assignment for the formula.

The WalkSAT algorithm was significantly faster than the GSAT when solving the sudoku test .cnf files.

## Results

one_cell.cnf 
output:
```python
3 0 0 | 0 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 0 
---------------------
0 0 0 | 0 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 0 
---------------------
0 0 0 | 0 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 0 
0 0 0 | 0 0 0 | 0 0 0 

```

all_cells.cnf 
output:
```python
6 2 6 | 3 5 4 | 4 1 5 
3 6 4 | 6 6 3 | 2 1 4 
5 5 2 | 3 2 7 | 8 2 6 
---------------------
7 1 4 | 4 7 6 | 2 6 1 
7 3 7 | 4 3 8 | 9 8 1 
8 7 4 | 9 6 6 | 3 8 2 
---------------------
6 9 3 | 6 8 6 | 9 9 3 
7 1 8 | 4 1 5 | 8 3 2 
3 4 9 | 2 8 2 | 1 4 9 
```

rows.cnf
output:
```python
7 6 1 | 8 4 3 | 5 9 2 
4 6 1 | 7 5 3 | 2 9 8 
5 7 8 | 1 6 2 | 4 9 3 
---------------------
7 6 8 | 5 9 4 | 1 3 2 
7 1 8 | 6 9 5 | 4 2 3 
5 2 9 | 6 1 7 | 8 3 4 
---------------------
7 5 6 | 2 9 4 | 3 8 1 
2 4 9 | 3 8 1 | 7 5 6 
3 7 9 | 8 4 5 | 1 6 2
```
rows_and_cols.cnf
output:
```python
5 3 8 | 7 2 6 | 1 9 4 
4 9 7 | 3 5 1 | 8 2 6 
7 6 1 | 5 9 8 | 3 4 2 
---------------------
3 4 2 | 6 8 7 | 9 5 1 
9 2 4 | 8 6 3 | 7 1 5 
8 1 6 | 9 4 2 | 5 7 3 
---------------------
2 5 9 | 1 7 4 | 6 3 8 
1 8 5 | 2 3 9 | 4 6 7 
6 7 3 | 4 1 5 | 2 8 9
```
rules.cnf
output:
```python
1 7 6 | 2 4 8 | 9 5 3 
9 4 3 | 1 5 6 | 2 8 7 
5 2 8 | 9 7 3 | 6 4 1 
---------------------
4 9 7 | 3 6 1 | 8 2 5 
6 8 1 | 5 2 9 | 7 3 4 
3 5 2 | 7 8 4 | 1 9 6 
---------------------
2 1 4 | 8 3 7 | 5 6 9 
7 6 5 | 4 9 2 | 3 1 8 
8 3 9 | 6 1 5 | 4 7 2
```
puzzle1.cnf
output:
```python
5 9 6 | 4 2 8 | 1 7 3 
2 7 3 | 6 9 1 | 5 8 4 
4 1 8 | 5 3 7 | 9 6 2 
---------------------
8 4 1 | 3 6 5 | 7 2 9 
6 5 2 | 8 7 9 | 3 4 1 
7 3 9 | 1 4 2 | 6 5 8 
---------------------
3 6 5 | 9 8 4 | 2 1 7 
9 8 7 | 2 1 6 | 4 3 5 
1 2 4 | 7 5 3 | 8 9 6 
```

puzzle2.cnf
output:
```python
1 3 8 | 4 5 6 | 2 9 7 
2 6 7 | 1 9 8 | 5 3 4 
5 9 4 | 7 3 2 | 6 1 8 
---------------------
8 2 5 | 9 6 1 | 4 7 3 
6 4 3 | 8 7 5 | 9 2 1 
7 1 9 | 3 2 4 | 8 5 6 
---------------------
4 7 2 | 5 8 3 | 1 6 9 
3 8 6 | 2 1 9 | 7 4 5 
9 5 1 | 6 4 7 | 3 8 2 
```

puzzle_bonus.cnf
output:
```python
5 3 4 | 6 7 8 | 1 9 2 
6 7 2 | 1 9 5 | 3 4 8 
1 9 8 | 3 4 2 | 5 6 7 
---------------------
8 5 9 | 7 6 1 | 4 2 3 
4 2 6 | 8 5 3 | 9 7 1 
7 1 3 | 9 2 4 | 8 5 6 
---------------------
9 6 1 | 5 3 7 | 2 8 4 
2 8 7 | 4 1 9 | 6 3 5 
3 4 5 | 2 8 6 | 7 1 9
```



## Bonus: Minesweeper

My Minesweeper Solver reads a Minesweeper map file and then creates clauses based on the rules of Minesweeper. This leverages the SAT-2 solver and converts Minesweeper grids into SAT-2 problems.

- `read_minesweeper_map`: Reads the Minesweeper map from a given file. 
- `generate_clauses_from_grid`: Converts the Minesweeper grid into a series of SAT-2 clauses. 
- `get_var`: Gets the variable number for a particular cell in the Minesweeper grid. 
- `generate_combinations`: Generates possible combinations of mine locations around a cell. 
- `print_solution`: Prints out the solved Minesweeper grid.

The primary challenge in this implementation was converting Minesweeper puzzles into SAT-2 problems. Each cell in the Minesweeper grid can either contain a mine or not. These states are translated into boolean variables. The number in a cell indicates how many surrounding cells contain mines. This information is used to generate clauses that must be satisfied.
For example, if a cell contains the number '2', then two of its surrounding cells must contain mines. This can be translated into multiple clauses that represent the various combinations of two mines in the neighboring cells.

sample map used:
```python
11..
..22
.3..
2...
```