from problems.hanoiTower.balducci import *
from path_search.strategies import *
from path_search.search import Search

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem = HanoiProblem((1, 2, 3, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 2, 3))
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
