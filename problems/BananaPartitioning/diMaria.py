# Author: Di Maria Matteo

import random

class BananaPartitioningProblem:
    def __init__(self, n_bananas):
        self.n_bananas = n_bananas
        # Stato iniziale: una tupla di n zeri o uni scelti casualmente
        self.initial_state = self.random_state()

    def random_state(self):
        """Crea una configurazione iniziale completa ma casuale."""
        return tuple(random.randint(0, 1) for _ in range(self.n_bananas))

    def actions(self, state):
        """
        Restituisce gli indici di tutte le banane (da 0 a n-1).
        """
        actions = []
        for banana in range(self.n_bananas):
            actions.append(banana)
        return actions

    def result(self, state, action):
        """
        Crea un nuovo stato invertendo la scimmia per la banana scelta.
        """
        new_state = list(state)
        banana_index = action
        # Se era 0 diventa 1, se era 1 diventa 0
        new_state[banana_index] = 1 - state[banana_index]
        return tuple(new_state)

    def get_differences(self, state):
        """
        Calcola la differenza pura (valore assoluto) tra i due gruppi.
        """
        n_first_monkey = 0
        n_second_monkey = 0
        for banana in range(self.n_bananas):
            if state[banana] == 0:
                n_first_monkey += 1
            else:
                n_second_monkey += 1
        return abs(n_first_monkey - n_second_monkey)

    def evaluate(self, state):
        """
        Restituisce il valore negativo perché l'algoritmo vuole massimizzare.
        """
        return - self.get_differences(state)

    def print_state(self, state):
        """Stampa i dettagli per l'utente."""
        diff = self.get_differences(state)
        print(f"Stato: {state}")
        print(f"Differenza tra le scimmie: {diff}")