# Author: Di Maria Matteo

import random

class KnapsackPotassiumProblem:
    def __init__(self, capacity):
        self.capacity = capacity
        # Dataset fornito dalla traccia
        self.bananas = [
            {"weight": 2, "potassium": 3},
            {"weight": 2, "potassium": 3},
            {"weight": 3, "potassium": 4},
            {"weight": 3, "potassium": 4},
            {"weight": 4, "potassium": 5},
            {"weight": 5, "potassium": 8}
        ]
        self.n = len(self.bananas)
        self.initial_state = self.random_state()

    def random_state(self):
        """Genera una tupla casuale di 0 e 1"""
        return tuple(random.randint(0, 1) for _ in range(self.n))

    def actions(self, state):
        """Si può scegliere di cambiare lo stato di qualunque banana"""
        actions = []
        for banana in range(self.n):
            actions.append(banana)
        return actions

    def result(self, state, action):
        """Inverte (0->1 o 1->0) la banana scelta"""
        new_state = list(state)
        idx = action
        new_state[idx] = 1 - state[idx]
        return tuple(new_state)

    def get_totals(self, state):
        """Calcola peso e potassio attuali"""
        total_weight = 0
        total_potassium = 0
        for i in range(self.n):
            total_weight += self.bananas[i]["weight"]
            total_potassium += self.bananas[i]["potassium"]
        return total_weight, total_potassium

    def evaluate(self, state):
        """
        Funzione di valutazione con PENALITÀ.
        Si vuole massimizzare il potassio, ma si punisce duramente il sovrappeso.
        """
        weight, potassium = self.get_totals(state)

        if weight <= self.capacity:
            return potassium # Stato legale: il valore è il potassio
        else:
            # Stato illegale: si tolgono 10 punti per ogni kg di troppo
            penalty = (weight - self.capacity) * 10
            return potassium - penalty

    def print_state(self, state):
        weight, potassium = self.get_totals(state)
        print(f"Stato: {state}")
        print(f"Peso totale: {weight}/{self.capacity} kg")
        print(f"Potassio totale: {potassium} K")
        if weight > self.capacity:
            print("ATTENZIONE: Zaino troppo pesante!")