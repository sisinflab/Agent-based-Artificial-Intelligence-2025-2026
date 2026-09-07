# Author: Di Maria Matteo

from path_search.search import Search
from path_search.strategies import BreadthFirstStrategy
from problems.hanoiTower.diMaria import HanoiProblem

# DEFINIZIONE STATI (Tupla di Tuple)
# Il numero più grande (3) rappresenta il disco alla base
initial_state=((3, 2, 1), (), ())
goal_state=((), (), (3, 2, 1))

problem = HanoiProblem(initial_state=initial_state, goal_state=goal_state)

strategy = BreadthFirstStrategy()
search = Search(problem=problem, strategy=strategy)
result = search.run()

if result is not None:
    print(f"Soluzione trovata in {result.path_cost} mosse!")
    path = result.path()
    curr_state = initial_state
    print(f"Inizio: {curr_state}")

    for move in path:
        curr_state = problem.result(curr_state, move)
        print(f"Muovo da {move[0]} a {move[1]} -> Nuovo stato: {curr_state}")
else:
    print("Nessuna soluzione trovata.")
