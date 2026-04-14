from local_search.simulated_annealing import SimulatedAnnealing, Scheduler
from problems.chessQueens.chessQueens import ChessQueensProblem
import random

if __name__ == "__main__":
    problem = ChessQueensProblem(8)
    scheduler = Scheduler(iterations=10000, alpha=0.01, scheduler='basic')
    search = SimulatedAnnealing(problem, scheduler=scheduler)
    result = search.search()
    problem.print_state(result)