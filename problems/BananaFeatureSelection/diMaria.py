# Author: Di Maria Matteo

import random

PENALTY = 1.0

class BananaFeatureSelectionProblem:
    def __init__(self):
        # Dati dalla slide
        self.features = {
            "Color": 5,
            "Size": 3,
            "Ripeness": 8,
            "Texture": 2,
            "Sweetness": 6
        }
        self.feat_names = list(self.features.keys())
        self.revelance_values = list(self.features.values())

        self.n = len(self.feat_names)
        self.initial_state = self.random_state()

    def random_state(self):
        """Genera una tupla casuale di 0 e 1."""
        return tuple(random.randint(0, 1) for _ in range(self.n))

    def actions(self, state):
        """Si può scegliere di invertire qualunque feature."""
        valid_actions = []
        for i in range(self.n):
            valid_actions.append(i)
        return valid_actions

    def result(self, state, action):
        """Inverto lo stato della feature all'indice 'action'."""
        new_state = list(state)
        new_state[action] = 1 - state[action]
        return tuple(new_state)

    def evaluate(self, state):
        """
        Calcola l'utilità totale:
        Total Relevance - (Penalty * Numero di feature scelte)
        """
        total_relevance = 0
        num_selected = 0

        for i in range(self.n):
            if state[i] == 1:
                total_relevance += self.revelance_values[i]
                num_selected += 1

        # Sottraiamo la penalità per ogni feature scelta per premiare la semplicità
        score = total_relevance - (PENALTY * num_selected)
        return score

    def print_state(self, state):
        print(f"Configurazione (0=No, 1=Sì): {state}")
        print("Feature selezionate:")
        for i in range(self.n):
            if state[i] == 1:
                print(f" - {self.feat_names[i]} (Relevance: {self.revelance_values[i]})")
        print(f"Score Finale (Relevance - Penalty): {self.evaluate(state)}")