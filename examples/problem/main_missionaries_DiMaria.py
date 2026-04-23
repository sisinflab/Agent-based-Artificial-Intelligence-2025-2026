# Author: Di Maria Matteo

from path_search.search import Search
from path_search.strategies import BreadthFirstStrategy
from problems.missionariesAndCanniblesProblem.diMaria import MissionariesProblem

# Inizializzazione standard
problem = MissionariesProblem()

strategy = BreadthFirstStrategy()
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result:
    print(f"--- SOLUZIONE TROVATA IN {result.path_cost} PASSI ---")
    path = result.path()
    curr = problem.initial_state
    for i, move in enumerate(path):
        direction = "DESTRA" if i % 2 == 0 else "SINISTRA"
        print(f"Mossa {i+1}: Porto {move[0]}M e {move[1]}C verso {direction}")
        curr = problem.result(curr, move)
        print(f"    Stato sponda SX: {curr}")
else:
    print("Nessuna soluzione.")
