# Author: Di Maria Matteo

CLEAN = 'CLEAN'
UP = 'UP'
DOWN = 'DOWN'
RIGHT = 'RIGHT'
LEFT = 'LEFT'

class VacuumProblem:
    def __init__(self, initial_state, goal_state, grid_size=(3, 3)):
        """
        :param initial_state: tupla strutturata come ((x, y), (dx1, dy1), (dx2, dy2)...)
        :param goal_state: tupla vuota () che rappresenta zero celle sporche rimaste.
        :param grid_size: dimensioni della griglia (di default 3x3)
        """
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.width, self.height = grid_size

    def actions(self, state):
        pos, dirt = state
        x, y = pos
        valid_actions = []

        if pos in dirt:
            return [CLEAN]

        # Se la cella è pulita, allora ci muoviamo
        if y + 1 < self.height: valid_actions.append(UP)
        if y - 1 >= 0:          valid_actions.append(DOWN)
        if x + 1 < self.width:  valid_actions.append(RIGHT)
        if x - 1 >= 0:          valid_actions.append(LEFT)

        return valid_actions

    def result(self, state, action):
        pos, dirt = state
        x, y = pos

        if action == CLEAN:
            # Rimuoviamo la cella appena pulita dalla tupla dello sporco
            new_dirt = tuple(d for d in dirt if d != pos)
            return (pos, new_dirt)

        # Aggiorniamo le coordinate in base al movimento
        if action == UP: y += 1
        elif action == DOWN: y -= 1
        elif action == RIGHT: x += 1
        elif action == LEFT: x -= 1

        return ((x, y), dirt)

    def is_goal(self, state):
        _, dirt = state
        # Il goal è raggiunto quando la tupla dello sporco è identica al goal_state (cioè vuota)
        return dirt == self.goal_state

    def action_cost(self, state, action):
        return 1

    def heuristic(self, state):
        """Distanza di Manhattan dallo sporco più vicino + numero di pulizia rimasta"""
        pos, dirt = state
        x, y = pos

        if not dirt:
            return 0

        min_dist = min(abs(x - dx) + abs(y - dy) for dx, dy in dirt)
        return len(dirt) + min_dist