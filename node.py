from puzzle import puzzle
class mynode:
    def __init__(self, new_data):
        self.data = new_data

        self.leaves = []
        self.leaves_count = 0
        #self.previous = node(puzzle([0,0,0,0,0,0,0,0,0]))


    def get_data(self):
        return self.data

    def insert_leaf(self, node):
        self.leaves.append(node)
        self.leaves_count = len(self.leaves)
        #node.add_prev(self)

    #def add_prev(self, prev_node):
        #self.previous = prev_node
