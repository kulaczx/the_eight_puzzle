from puzzle import puzzle
class mynode:
    def __init__(self, new_data):
        self.data = new_data
        self.leaves = []
        self.cost = 1
        self.depth = 0

    def __lt__(self, other):
        return True

    def get_data(self):
        return self.data

    def insert_leaf(self, node):
        self.leaves.append(node)