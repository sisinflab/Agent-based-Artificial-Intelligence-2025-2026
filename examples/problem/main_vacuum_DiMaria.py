# Author: Di Maria Matteo

from path_search.search import Search
from path_search.strategies import AStarStrategy
from problems.vacuumCleaner.diMaria import VacuumProblem

# STRUTTURA DELLO STATO INIZIALE: ( Posizione_Robot, (Tupla_Sporco) )
dirt = ((0, 0), (2, 0), (2, 2))
initial_state = ((1, 1), dirt)

# OBIETTIVO: Una tupla di sporco completamente vuota
goal_state = ()

# Inizializziamo il problema rispettando le variabili standard
problem = VacuumProblem(initial_state=initial_state, goal_state=goal_state, grid_size=(3, 3))

print("Ricerca del percorso ottimale di pulizia in corso...")

strategy = AStarStrategy(problem=problem)
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result is not None:
    print(f"\n--- AMBIENTE PULITO IN {result.path_cost} AZIONI ---")
    path = result.path()
    curr = problem.initial_state

    print(f"Stato iniziale: Robot in {curr[0]}, Sporco in {curr[1]}")
    for i, move in enumerate(path):
        curr = problem.result(curr, move)
        if move == 'CLEAN':
            print(f"Passo {i+1}: >>> PULISCO LA CELLA! <<< Sporco rimasto: {curr[1]}")
        else:
            print(f"Passo {i+1}: Mi muovo {move} -> Posizione attuale: {curr[0]}")
else:
    print("Nessuna soluzione trovata.")
