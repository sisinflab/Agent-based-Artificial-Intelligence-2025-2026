# Author: Di Maria Matteo

import random

class SudokuChallengeProblem:
    def __init__(self):
        self.n = 16 #4x4 = 16 celle
        # Indici delle celle raggruppati per i 4 blocchi 2x2
        self.blocks = [
            (0, 1, 4, 5),  # Blocco in alto a sx
            (2, 3, 6, 7),  # Blocco in alto a dx
            (8, 9, 12, 13),  # Blocco in basso a sx
            (10, 11, 14, 15)  # Blocco in basso a dx
        ]
        self.initial_state = self.random_state()

    def random_state(self):
        """Genera uno stato dove ogni blocco 2x2 ha i numeri 1,2,3,4 mescolati."""
        state = [0] * 16
        for block in self.blocks:
            values = [1, 2, 3, 4]
            random.shuffle(values)
            for i, cell_idx in enumerate(block):
                state[cell_idx] = values[i]
        return tuple(state)

    def actions(self, state):
        """L'azione è scambiare due celle all'interno dello stesso blocco."""
        valid_actions = []
        for block in self.blocks:
            # Scegliamo due indici diversi all'interno del blocco (es. tra 0, 1, 4, 5)
            for i in range(len(block)):
                for j in range(i + 1, len(block)):
                    valid_actions.append((block[i], block[j]))
        return valid_actions

    def result(self, state, action):
        """Esegue lo scambio tra due celle."""
        idx1, idx2 = action
        new_state = list(state)
        new_state[idx1], new_state[idx2] = new_state[idx2], new_state[idx1]
        return tuple(new_state)

    def count_conflicts(self, state):
        """Conta quanti numeri sono duplicati in righe e colonne."""
        violations = 0

        # 1. Controlla Righe
        for r in range(4):
            row = [state[r*4 + c] for c in range(4)]
            # Conta quanti numeri mancano (se mancano, ci sono duplicati)
            violations += (4 - len(set(row)))

        # 2. Controlla Colonne
        for c in range(4):
            col = [state[r*4 + c] for r in range(4)]
            violations += (4 - len(set(col)))

        # Nota: Non controllo i blocchi perché le azioni
        # garantiscono che i blocchi siano sempre validi

        return violations

    def evaluate(self, state):
        """Si vuole minimizzare le violazioni -> Si massimizza il negativo"""
        return -self.count_conflicts(state)

    def print_state(self, state):
        """Stampa la griglia 4x4"""
        for r in range(4):
            if r % 2 == 0: print("-" * 13)
            row = [str(state[r*4 + c]) for c in range(4)]
            print(f"|{row[0]} {row[1]}|{row[2]} {row[3]}|")
        print("-" * 13)
        print(f"Violazioni: {self.count_conflicts(state)}")