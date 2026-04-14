from problems.streetProblem.cities import *

class StreetProblem:

    def __init__(self, initial_state, goal_state):

        self.initial_state = initial_state
        self.goal_state = goal_state

        self.map = {
            CORATO: [TRANI, BISCEGLIE, RUVO, ALTAMURA, ANDRIA],
            BARLETTA: [TRANI, ANDRIA, MINERVINO],
            ANDRIA: [CORATO, BARLETTA, MINERVINO],
            MINERVINO: [BARLETTA, ANDRIA, ALTAMURA],
            TRANI: [CORATO, BISCEGLIE, BARLETTA],
            BISCEGLIE: [TRANI, MOLFETTA, CORATO],
            MOLFETTA: [BISCEGLIE, RUVO, MODUGNO, BARI],
            RUVO: [CORATO, MOLFETTA, MODUGNO, ALTAMURA],
            ALTAMURA: [MINERVINO, CORATO, RUVO, MODUGNO, BARI],
            MODUGNO: [MOLFETTA, RUVO, ALTAMURA, BARI],
            BARI: [MOLFETTA, MODUGNO, ALTAMURA]
        }

    def actions(self, state):
        return self.map[state]

    def result(self, state, action):
        for street in streets: 
            c1, c2, _ = street
            if (c1 == state and action == c2) or (c2 == state and action == c1):
                return action
        raise ValueError('Action not possible')

    def action_cost(self, state, action):
        for street in streets: 
            c1, c2, cost = street
            if (c1 == state and action == c2) or (c2 == state and action == c1):
                return cost
        print(state, action)
        raise ValueError('Action not allowed')
    
    def is_goal(self, state):
        return state == self.goal_state

