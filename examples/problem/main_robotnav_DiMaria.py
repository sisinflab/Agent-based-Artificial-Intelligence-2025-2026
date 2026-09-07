# Author: Di Maria Matteo

from path_search.search import Search
from path_search.strategies import GreedStrategy
from problems.robotNavigation.diMaria import RobotNavigationProblem

# Definiamo una griglia 5x5
# Mettiamo un muro di osticali in mezzo
obstacles = [(1, 0), (1, 1), (2, 1), (3, 1), (3, 0)]

# Il robot parte da (0, 0) in basso a sinistra e deve arrivare a (4,4) in alto a destra
problem = RobotNavigationProblem(initial_state=(0, 0), goal_state=(4, 0), width=5, height=5, obstacles=obstacles)

strategy = GreedStrategy(problem=problem)
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result is not None:
    print("\n--- SOLUZIONE TROVATA! ---")
    path = result.path()
    state = problem.initial_state

    print(f"Start: {state}")
    for action in path:
        print(f"Mossa: {action} ->", end="")
        state = problem.result(state, action)
        print(f"Arrivato in {state}")

    print(f"\nCosto totale del percorso: {result.path_cost}")
else:
    print("\nNessuna soluzione trovata. Il robot è bloccato!")
