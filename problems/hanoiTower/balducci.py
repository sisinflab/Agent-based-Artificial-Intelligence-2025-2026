class HanoiProblem:
    def __init__(self, inital_state, goal_state):
        self.initial_state = inital_state
        self.goal_state = goal_state

    def actions(self, state):
        possible_actions = []

        torri = [
            state[0:3],
            state[3:6],
            state[6:9]
        ]

        def top(t):
            for x in t:
                if x != 0:
                    return x
            return None

        for i in range(3):
            for j in range(3):
                if i==j:
                    continue

                if top(torri[i]) is None:
                    continue

                if top(torri[j]) is None or top(torri[j]) < top(torri[i]):
                    possible_actions.append((i,j))

        return possible_actions

    def result(self, state, action):
        i,j = action

        torri = [
            list(state[0:3]),
            list(state[3:6]),
            list(state[6:9])
        ]

        for k in range(3):
            if torri[i][k] != 0:
                disco = torri[i][k]
                torri[i][k] = 0
                break

        for k in range(3):
            if torri[j][k] == 0:
                torri[j][k] = disco
                break

        return tuple(torri[0] + torri[1] + torri[2])

    def is_goal(self, state):
        return state == self.goal_state

    def action_cost(self, state, action):
        return 1