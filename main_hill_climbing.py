from local_search.hill_climbing import HillClimbing
from problems.chessQueens.chessQueens import ChessQueensProblem
import random

if __name__ == "__main__":
    problem = ChessQueensProblem(8)
    search = HillClimbing(problem)
    result = search.search()
    problem.print_state(result)