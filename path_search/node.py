class Node:

    def __init__(self, state, action, parent, path_cost, depth=None):
        self.state = state
        self.action = action
        self.parent = parent
        self.path_cost = path_cost
        if depth is None:
            self.depth = self.parent.depth + 1
        else:
            self.depth = depth

    def __repr__(self):
        if self.parent is None:
            return f"([ROOT NODE] State: {self.state}, Action: {self.action}, Cost: {self.path_cost})"
        return f"([NODE] State: {self.state}, Action: {self.action}, Parent: {self.parent.state}, Cost: {self.path_cost})"


