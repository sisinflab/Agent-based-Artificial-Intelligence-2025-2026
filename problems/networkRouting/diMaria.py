# Author: Di Maria Matteo

A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'

class NetworkRoutingProblem:

    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

        # Latenza dei nodi (node latency)
        self.node_latency = {
            A: 1,
            B: 2,
            C: 1,
            D: 3,
            E: 2,
            F: 1,
            G: 2
        }

        # Latenza degli archi (edge latency)
        self.network = {
            A: {B: 2, C: 5},
            B: {D: 4, E: 1},
            C: {F: 3},
            D: {G: 6},
            E: {D: 2, G: 3},
            F: {E: 4, G: 2},
            G: {}
        }

        # Tabella Euristica h(n)
        # Rappresenta una stima della latenza mancante per arrivare a G
        # Deve essere ottimista (h <= costo reale)
        self.h_table = {
            "A": 6,  # Stima molto bassa
            "B": 4,
            "C": 4,
            "D": 2,
            "E": 2,
            "F": 2,
            "G": 0  # L'euristica sul goal è sempre 0
        }

    def actions(self, state):
        """Restituisce i nodi vicini raggiungibili"""
        return list(self.network[state].keys())

    def result(self, state, action):
        """L'azione coincide con il nome del nodo di destinazione"""
        if action not in self.network[state]:
            raise ValueError(f"Connessione {state} -> {action} non esistente")
        return action

    def action_cost(self, state, action):
        """
        Calcola il costo: Latenza Arco + Latenza del nodo di arrivo.
        """

        return self.network[state][action] + self.node_latency[action]

    def is_goal(self, state):
        return state == self.goal_state

    def heuristic(self, state):
        return self.h_table[state]