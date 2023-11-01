import random, sys
from SAT2 import SAT2

class MinesweeperSolver(SAT2):
    def __init__(self, filename):
        self.grid = self.read_minesweeper_map(filename)
        self.clauses = self.generate_clauses_from_grid()
        self.variables = self.initialize_variables(self.clauses)

    def read_minesweeper_map(self, filename):
        with open(filename, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]

    def generate_clauses_from_grid(self):
        clauses = []
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == '*':
                    continue
                elif cell == '.':
                    # This cell should not contain a mine and has no mines around it
                    clauses.append([-self.get_var(i, j)])
                else:
                    # Generate clauses based on the count of adjacent mines
                    num = int(cell)
                    neighbors = [(x, y) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2) if
                                 0 <= x < len(self.grid) and 0 <= y < len(row) and (x, y) != (i, j)]
                    possible_mine_combinations = self.generate_combinations(neighbors, num)
                    for combination in possible_mine_combinations:
                        clause = []
                        for n in neighbors:
                            if n in combination:
                                clause.append(self.get_var(n[0], n[1]))
                            else:
                                clause.append(-self.get_var(n[0], n[1]))
                        clauses.append(clause)
        return clauses

    def get_var(self, i, j):
        # This function gives a unique number for each cell in the grid
        return i * len(self.grid[0]) + j + 1

    def generate_combinations(self, neighbors, num):
        # This function returns all possible combinations of 'num' neighbors from the list of neighbors
        if num == 0:
            return [()]
        if not neighbors:
            return []
        return self.generate_combinations(neighbors[1:], num) + [tuple([neighbors[0]] + list(item)) for item in
                                                                 self.generate_combinations(neighbors[1:], num - 1)]

    def print_solution(self):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == '.':
                    count_mines_around = sum(
                        [self.variables[self.get_var(x, y)] for x in range(i - 1, i + 2) for y in range(j - 1, j + 2) if
                         0 <= x < len(self.grid) and 0 <= y < len(row) and (x, y) != (i, j)])
                    if count_mines_around == 0:
                        print('.', end='')
                    else:
                        print(count_mines_around, end='')
                elif cell == ' ':
                    if self.variables[self.get_var(i, j)]:
                        print('*', end='')
                    else:
                        print(' ', end='')
                else:
                    print(cell, end='')
            print()

if __name__ == "__main__":
    map_file = sys.argv[1]
    solver = MinesweeperSolver(map_file)
    if solver.walksat():
        solver.print_solution()
    else:
        print("No solution found.")