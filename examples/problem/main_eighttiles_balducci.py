from problems.eightTiles.balducci import *
from path_search.strategies import *
from path_search.search import Search

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem = EightGame((1,0,2,4,5,3,7,8,6),(1,2,3,4,5,6,7,8,0))
    strategy = DepthFirstStrategy()
    search = Search(problem, strategy)
    result = search.run()
    if result is not None:
        path = result.path()
        state = problem.initial_state
        for action in path:
            print(f'[{state}] --{action}--> ', end='')
            state = problem.result(state, action)
        print(f'[{state}]')
        print(f'Path cost: {result.path_cost}')
