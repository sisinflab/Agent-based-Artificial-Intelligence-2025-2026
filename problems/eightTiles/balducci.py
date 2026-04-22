class EightGame:
    def __init__(self, inital_state, goal_state):
        self.initial_state = inital_state
        self.goal_state = goal_state

    def actions(self, state):
        possible_actions = []
        #print(state)
        zero_index = state.index(0)

        #trovo riga e colonna dove si trova lo zero
        row = zero_index // 3
        col = zero_index % 3

        if row > 0: possible_actions.append("UP")
        if row < 2: possible_actions.append("DOWN")
        if col > 0: possible_actions.append("LEFT")
        if col < 2: possible_actions.append("RIGHT")

        return possible_actions

    def result(self, state, action):
        state_copy = list(state)
        zero_index = state_copy.index(0)
        #row = zero_index // 3
        #col = zero_index % 3

        if action == "UP": target_index = zero_index - 3
        if action == "DOWN": target_index = zero_index + 3
        if action == "LEFT": target_index = zero_index - 1
        if action == "RIGHT": target_index = zero_index + 1

        state_copy[zero_index],state_copy[target_index] = state_copy[target_index],state_copy[zero_index]

        return tuple(state_copy)

    def is_goal(self, state):
        return state == self.goal_state

    def action_cost(self, state, action):
        return 1

    #def heuristic(self, node):
    #    node_state = node.state
    #    distance = 0

    #    return distance
