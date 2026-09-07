import random

features= {
    'color' : 5,
    'size' : 3,
    'ripeness' : 8,
    'texture' : 2,
    'swetnesss' : 6,
}

class Banana:

    def __init__(self):
        self.initial_state= self.random_state()


    def random_state(self):
        return [random.randint(0,1) for _ in range(5)]

    def actions(self, state):
        azioni= []
        for i in range(5):
            if state[i] == 0:
                azioni.append((i, 1))
            if state[i]== 1:
                azioni.append((i, -1))

        return azioni

    def results(self, state,azione):
        features, azione= azione
        new_state= list(state)
        new_state[features] += azione
        return tuple(new_state)

    def evaluate(self, state):
        valore= 0
        penalty= 0
        for f in range(5):
            valore += state[f] * features[list(features)[f]]
            penalty += state[f]*2

        return valore-penalty