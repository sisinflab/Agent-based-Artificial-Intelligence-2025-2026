# Author: Di Maria Matteo

class RobotNavigationProblem:
    def __init__(self, initial_state, goal_state, width, height, obstacles):
        """
        :param initial_state: tupla (x, y) di partenza
        :param goal_state: tupla (x, y) di arrivo
        :param width: larghezza della griglia (asse x)
        :param height: altezza della griglia (asse y)
        :param obstacles: lista di tuple (x, y) che rappresentano i muri
        """

        self.initial_state = initial_state
        self.goal_state = goal_state
        self.width = width
        self.height = height

        # Convertiamo in un set per fare i controlli molto più veloci in Python
        self.obstacles = set(obstacles)

    def actions(self, state):
        """Restituisce le azioni legali possibili dallo stato corrente"""
        x, y = state
        possible_actions = []

        # Controlliamo UP (saliamo sull'asse y)
        if y + 1 < self.height and (x, y + 1) not in self.obstacles:
            possible_actions.append('UP')

        # Controlliamo DOWN (scendiamo sull'asse y)
        if y - 1 >= 0 and (x, y - 1) not in self.obstacles:
            possible_actions.append('DOWN')

        # Controlliamo RIGHT (avanziamo sull'asse x)
        if x + 1 < self.width and (x + 1, y) not in self.obstacles:
            possible_actions.append('RIGHT')

        # Controlliamo LEFT (indietreggiamo sull'asse x)
        if x - 1 >= 0 and (x - 1, y) not in self.obstacles:
            possible_actions.append('LEFT')

        return possible_actions

    def result(self, state, action):
        """Restituisce il nuovo stato dopo aver applicato l'azione"""
        x, y = state
        if action == 'UP':
            return (x, y + 1)
        elif action == 'DOWN':
            return (x, y - 1)
        elif action == 'RIGHT':
            return (x + 1, y)
        elif action == 'LEFT':
            return (x - 1, y)
        else:
            raise ValueError(f"Azione: {action} non valida!")

    def action_cost(self, state, action):
        """Il costo di ogni passo elementare è sempre 1"""
        return 1

    def is_goal(self, state):
        """Verifica se abbiamo raggiunto il target"""
        return state == self.goal_state

    def mahattan_distance(self, state):
        x, y = state
        gs_x, gs_y = self.goal_state

        # La Distanza di Manhattan è la somma delle distanze assolute sugli assi
        return abs(x - gs_x) + abs(y - gs_y)

    def heuristic(self, state):
        """
        Calcola l'euristica (Distanza di Manhattan) tra lo stato attuale e il goal.
        """
        return self.mahattan_distance(state)