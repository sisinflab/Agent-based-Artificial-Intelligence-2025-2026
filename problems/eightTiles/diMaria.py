# Author: Di Maria Matteo

UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

class PuzzleProblem:

    def __init__(self, initial_state, goal_state):
        # Gli stati devono essere tuple, es: (1, 2, 3, 4, 5, 6, 7, 8, 0)
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.size = 3 # Griglia 3x3

    def actions(self, state):
        """Trova lo 0 e restituisce le mosse legali che può fare"""
        possible_actions = []
        zero_index = state.index(0)

        # Calcoliamo la riga e colonna dello 0 (da 0 a 2)
        row = zero_index // self.size
        column = zero_index % self.size

        # Se non siamo sulla prima riga in alto, possiamo andare SU
        if row > 0:
            possible_actions.append(UP)
        # Se non siamo sull'ultima riga in basso, possiamo andare GIÙ
        if row < self.size - 1:
            possible_actions.append(DOWN)
        # Se non siamo sulla primissima colonna a sx, possiamo andare a SINISTRA
        if column > 0:
            possible_actions.append(LEFT)
        # Se non siamo sull'ultima colonna a dx, possiamo andare a DESTRA
        if column < self.size - 1:
            possible_actions.append(RIGHT)

        return possible_actions

    def result(self, state, action):
        """Scambia lo 0 con la tessera nella direzione scelta"""
        # Trasformiamo la tupla in lista per poterla modificare
        state_list = list(state)
        zero_idx = state_list.index(0)

        # Calcoliamo l'indice della tessera da scambiare con lo 0
        if action == UP:
            swap_idx = zero_idx - self.size
        elif action == DOWN:
            swap_idx = zero_idx + self.size
        elif action == LEFT:
            swap_idx = zero_idx - 1
        elif action == RIGHT:
            swap_idx = zero_idx + 1
        else:
            raise ValueError("Azione non valida")

        # Eseguiamo lo scambio (swap)
        state_list[zero_idx], state_list[swap_idx] = state_list[swap_idx], state_list[zero_idx]

        # Restituiamo il nuovo stato come tupla
        return tuple(state_list)

    def action_cost(self, state, action):
        return 1

    def is_goal(self, state):
        return state == self.goal_state

    def heuristic(self, state):
        """
        Distanza di Manhattan.
        Calcola la somma delle distanze orizzontali e verticali di ogni
        tessera dalla sua posizione corretta nel goal.
        """
        distance = 0

        # Calcoliamo la distanza per ogni numero da 1 a 8 (ignoriamo lo 0)
        for tile in range(1, 9):
            # Posizione corrente del numero
            current_idx = state.index(tile)
            curr_row, curr_col = current_idx // self.size, current_idx % self.size

            # Posizione in cui dovrebbe stare (guardando il goal)
            goal_idx = self.goal_state.index(tile)
            goal_row, goal_col = goal_idx // self.size, goal_idx % self.size

            # Somma delle distanze assolute
            distance += abs(curr_row - goal_row) + abs(curr_col - goal_col)

        return distance