from problems.streetProblem.v1 import StreetProblem
from problems.streetProblem.cities import * 
from path_search.search import Search
from path_search.strategies import RandomStrategy

problem = StreetProblem(TRANI, MODUGNO)

strategy = RandomStrategy()
search = Search(problem=problem, strategy=strategy)
result = search.run()
if result is None:
    print('No solution found')
else:    
    print(f'Solution found with path cost {result.path_cost}')