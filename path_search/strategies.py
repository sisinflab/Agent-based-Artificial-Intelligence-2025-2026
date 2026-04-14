import random

class RandomStrategy:
    def select(self, fringe):
        random.shuffle(fringe)
        selected_node = fringe.pop(0)
        return fringe, selected_node