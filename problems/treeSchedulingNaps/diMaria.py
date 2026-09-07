# Author: Di Maria Matteo

import random

PENALTY = 100 # Penalità per il vincolo "ogni albero almeno un nap"

class TreeSchedulingNapsProblem:
    def __init__(self):
        self.naps = ["Nap1", "Nap2", "Nap3", "Nap4"]
        self.incompatibilities = [
            ("Nap1", "Nap2"),
            ("Nap1", "Nap3"),
            ("Nap2", "Nap4")
        ]
        self.num_trees = 2

        # Stato iniziale casuale
        self.initial_state = self.random_state()

    def random_state(self):
        # Genera una tupla di 4 numeri (0 o 1) a caso
        return tuple(random.randint(0, self.num_trees - 1) for _ in range(len(self.naps)))

    def actions(self, state):
        """Sposta un nap su un albero diverso"""
        valid_actions = []
        for nap_idx in range(len(self.naps)):
            for tree_idx in range(self.num_trees):
                if state[nap_idx] != tree_idx:
                    valid_actions.append((nap_idx, tree_idx))
        return valid_actions

    def result(self, state, action):
        nap_idx, new_tree = action
        new_state = list(state)
        new_state[nap_idx] = new_tree
        return tuple(new_state)

    def get_conflicts(self, state):
        """Conta quanti conflitti ci sono tra naps incompatibili"""
        count = 0
        for (a, b) in self.incompatibilities:
            idx_a = self.naps.index(a)
            idx_b = self.naps.index(b)
            # Se nello stesso albero, c'è un conflitto
            if state[idx_a] == state[idx_b]:
                count += 1
        return count

    def evaluate(self, state):
        """Utility = - (Conflitti + Penalità per alberi vuoti)"""
        score = self.get_conflicts(state)

        # Vincolo: ogni albero deve avere almeno un nap
        # Si usa set(state) per vedere quanti alberi unici sono usati
        trees_used = len(set(state))
        if trees_used < self.num_trees:
            score += PENALTY # Se un albero è vuoto, il punteggio crolla

        return -score

    def print_state(self, state):
        print(f"Configurazione: {state}")
        print(f"Conflitti reali: {self.get_conflicts(state)}")
        for t in range(self.num_trees):
            naps_on_tree = [self.naps[i] for i, tree in enumerate(state) if tree == t]
            print(f"    Albero {t}: {naps_on_tree}")