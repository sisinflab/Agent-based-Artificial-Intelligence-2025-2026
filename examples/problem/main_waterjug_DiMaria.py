# Author: Di Maria Matteo

from path_search.search import Search
from path_search.strategies import BreadthFirstStrategy
from problems.waterJug.diMaria import WaterJugProblem

# Partiamo con le brocche vuote
problem = WaterJugProblem(initial_state=(0, 0, 0))

strategy = BreadthFirstStrategy()
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result:
    print(f"--- OBIETTIVO RAGGIUNTO IN {result.path_cost} MOSSE ---")
    path = result.path()
    curr = problem.initial_state
    print(f"Inizio {curr}")

    for move in path:
        curr = problem.result(curr, move)
        print(f"Azione {move} -> Stato: {curr}")
else:
    print("Nessuna soluzione trovata.")
