class HillClimbing():

    def __init__(self, problem):
        self.problem = problem
    
    def get_neighbors(self, state):
        return [self.problem.result(state, action) for action in self.problem.actions(state)]

    def search(self):
        
        state = self.problem.initial_state
        score = self.problem.evaluate(state)

        while True:
            neighbors = self.get_neighbors(state)
            if not neighbors:
                break
            
            best_neighbor = max(neighbors, key=lambda x: self.problem.evaluate(x))
            new_score = self.problem.evaluate(best_neighbor)
            if new_score <= score:
                break
            state = best_neighbor
            score = new_score
            print(f"Utility {score}")

        return state

