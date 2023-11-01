from display import display_sudoku_solution
import random, sys
from SAT import SAT
from SAT2 import SAT2

if __name__ == "__main__":
    # for testing, always initialize the pseudorandom number generator to output the same sequence
    #  of values:
    random.seed(1)

    puzzle_name = str(sys.argv[1][:-4])
    sol_filename = puzzle_name + ".sol"

    #If Using WalkSAT
    sat = SAT2(sys.argv[1])
    result = sat.walksat()

    # If Using GSAT
    # sat = SAT(sys.argv[1])
    # result = sat.gsat()

    if result:
        sat.write_solution(sol_filename)
        display_sudoku_solution(sol_filename)
