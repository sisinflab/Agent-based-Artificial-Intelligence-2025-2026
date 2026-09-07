# Author: Di Maria Matteo

from path_search.search import Search
from path_search.strategies import UniformCostStrategy
from problems.networkRouting.diMaria import NetworkRoutingProblem, A, G

problem = NetworkRoutingProblem(initial_state=A, goal_state=G)

strategy = UniformCostStrategy()

search = Search(problem=problem, strategy=strategy)

result = search.run()

if result:
    path = result.path()
    print(f"Percorso trovato: {problem.initial_state} -> {' -> '.join(path)}")
    print(f"Latenza totale calcolata: {result.path_cost}")
else:
    print("Nessun percorso trovato.")
