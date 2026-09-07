import random

class sudoku:
    def __init__(self):
        self.initial_state = self.random_state()

    def random_state(self):
        stato= []
        for _ in range(4):
            cella= [[random.randint(1,9) for _ in range(2)], [random.randint(1,9) for _ in range(2)]]
            stato.append(cella)

        return stato

    def actions(self, state):
        act= []
        for _ in range(10):
            i= random.choice(range(4))
            j= random.choice(range(2))
            k= random.randint(1,9)
            act.append([i, j, k])
        return act

    def results(self, state, action):
        state= list(state)
        i, j, k= action
        state[i][j][j]= k
        return tuple(state)


    def evaluate(self, state):
        conf= 0

        righe= ([[state[0][0][0], state[0][0][1], state[1][0][0], state[1][0][1]],
                    [state[0][1][0], state[0][1][1], state[1][1][0], state[1][1][1]],
                    [state[2][0][0], state[2][0][1], state[3][0][0], state[3][0][1]],
                    [state[2][1][0], state[2][1][1], state[3][1][0], state[3][1][1]]])

        colonne = ([[state[0][0][0], state[0][1][0], state[2][0][0], state[2][1][0]],
                    [state[0][0][1], state[0][1][1], state[2][0][1], state[2][1][1]],
                    [state[1][0][0], state[1][1][0], state[3][0][0], state[3][1][0]],
                    [state[1][0][1], state[1][1][1], state[3][0][1], state[3][1][1]]])

        for riga in righe:
            for j in range(4):
                for i in range(j+1, 4):
                    if riga[j]== riga[i]:
                        conf +=1

        for c in colonne:
            for j in range(4):
                for i in range(j+1, 4):
                    if c[j]==c[i]:
                        conf +=1

        for k in range(1,10):
            for j in range(4):
                lun = 0
                for i in range(2):
                    for r in range(2):
                       if state[j][i][r] == k:
                           lun +=1

                if lun>=2:
                    conf = conf + lun-1

        return -conf