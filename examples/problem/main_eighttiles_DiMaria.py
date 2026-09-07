# Author: Di Maria Matteo

from path_search.search import Search
from path_search.strategies import AStarStrategy
from problems.eightTiles.diMaria import PuzzleProblem

def print_grid(state):
    """Funzione di utility per stampare la tupla come una griglia 3x3"""
    for i in range(0, 9, 3):
        row = state[i:i+3]
        # Sostituiamo lo 0 con uno spazietto vuoto per renderlo più bello
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print("-" * 5)

# Puzzle
initial_state = (3, 5, 6, 1, 2, 7, 8, 0, 4)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

problem = PuzzleProblem(initial_state=initial_state, goal_state=goal_state)

print("Calcolo in corso (potrebbe richiedere qualche secondo)...")

strategy = AStarStrategy(problem=problem)
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result is not None:
    print("\n--- SOLUZIONE TROVATA! ---")
    path = result.path()

    state = problem.initial_state
    print("START:")
    print_grid(state)

    for i, action in enumerate(path):
        print(f"Passo {i+1} | Mossa dello spazio vuoto: {action}")
        state = problem.result(state, action)
        print_grid(state)

    print(f"Costo totale del percorso: {result.path_cost} mosse.")
else:
    print("Nessuna soluzione trovata.")
