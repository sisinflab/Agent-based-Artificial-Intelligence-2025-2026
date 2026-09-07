# Author: Di Maria Matteo

class HanoiProblem:

    def __init__(self, initial_state, goal_state):
        """
        Lo stato deve essere una tupla di 3 tuple.
        Esempio: ((3, 2, 1), (), ())
        """
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        """
        Restituisce le mosse legali come tuple (origine, destinazione).
        Esempio: (0, 2) significa sposta dal primo al terzo piolo.
        """
        valid_actions = []

        # i = indice piolo di origine, j = indice piolo di destinazione
        for i in range(3):
            for j in range(3):
                if i != j: # Non ci si muove sullo stesso piolo
                    # Regola 1: Il piolo di origine non deve essere vuoto
                    if len(state[i]) > 0:
                        # Regola 2: Muovo se la destinazione è vuota
                        # OPPURE se il disco mosso è più piccolo di quello in cima alla destinazione
                        if len(state[j]) == 0 or state[j][-1] > state[i][-1]:
                            valid_actions.append((i, j))
        return valid_actions

    def result(self, state, action):
        """
        Applica lo spostamento usando lo slicing delle tuple.
        """
        i, j = action

        # Prendiamo il disco in cima al piolo di origine
        disk = state[i][-1]

        # Creiamo una nuova lista di pioli (che sono tuple)
        new_pegs = list(state)

        # 1. Togliamo il disco dall'origine: prendiamo tutto tranne l'ultimo elemento
        new_pegs[i] = state[i][:-1]

        # 2. Aggiungiamo il disco alla destinazione: concatenazione di tuple
        new_pegs[j] = state[j] + (disk,)

        return tuple(new_pegs)

    def action_cost(self, state, action):
        return 1

    def is_goal(self, state):
        return state == self.goal_state

    def heuristic(self, state):
        """
        Euristica: quanti dischi non sono ancora sul piolo di destinazione?
        (Assumendo che il goal sia tutto sul piolo 2)
        """
        return len(state[0]) + len(state[1])