# Author: Di Maria Matteo

FILL = 'FILL'
EMPTY = 'EMPTY'
POUR = 'POUR'

class WaterJugProblem:
    def __init__(self, initial_state=(0, 0, 0), goal_state=4):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.capacities = (8, 5, 3) # Capacità delle tre brocche

    def actions(self, state):
        valid_actions = []

        for i in range(3):
            # 1. Azione: RIEMPI la brocca i (se non è già piena)
            if state[i] < self.capacities[i]:
                valid_actions.append((FILL, i))

            # 2. Azione: SVUOTA la brocca i (se non è già vuota)
            if state[i] > 0:
                valid_actions.append((EMPTY, i))

            # 3. Azione: TRAVASA dalla brocca i alla brocca j
            for j in range(3):
                if i != j:
                    # Posso travasare se i ha acqua e j non è piena
                    if state[i] > 0 and state[j] < self.capacities[j]:
                        valid_actions.append((POUR, i, j))

        return valid_actions

    def result(self, state, action):
        new_state = list(state)
        act_type = action[0]
        idx_i = action[1]

        if act_type == FILL:
            new_state[idx_i] = self.capacities[idx_i]
        elif act_type == EMPTY:
            new_state[idx_i] = 0
        elif act_type == POUR:
            idx_j = action[2]
            # Quanto posso effettivamente versare?
            # È il minimo tra l'acqua che ho in i e lo spazio che resta in j
            amount = min(state[idx_i], self.capacities[idx_j] - state[idx_j])
            new_state[idx_i] -= amount
            new_state[idx_j] += amount

        return tuple(new_state)

    def is_goal(self, state):
        # Il goal è raggiunto se una qualsiasi brocca ha 4 litri
        return any(liters == self.goal_state for liters in state)

    def action_cost(self, state, action):
        return 1