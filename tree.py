from node import mynode
from puzzle import puzzle
import time

class tree:
    def __init__(self, data):
        pzl = puzzle(data)
        self.root = mynode(pzl)
        print("init tree")
        print(data)
        self.root.get_data().show_puzzle()
        self.depth = 0


    def get_next_level(self):
        getNext = self.root.get_data()
        temp = getNext.cpy_puzzle()
        temp.show_puzzle()
        if temp.move_blank_up():
            new_node = mynode(temp)
            print("UP")
            temp.show_puzzle()
            self.root.insert_leaf(new_node)
            temp = getNext.cpy_puzzle()
        if temp.move_blank_down():
            new_node = mynode(temp)
            print("DOWN")
            temp.show_puzzle()
            self.root.insert_leaf(new_node)
            temp = getNext.cpy_puzzle()
        if temp.move_blank_right():
            new_node = mynode(temp)
            print("RIGHT")
            temp.show_puzzle()
            self.root.insert_leaf(new_node)
            temp = getNext.cpy_puzzle()
        if temp.move_blank_left():
            new_node = mynode(temp)
            print("LEFT")
            temp.show_puzzle()
            self.root.insert_leaf(new_node)

    def uniform_cost_search(self):
        # search
        steps = []
        timer = time.time()
        timers = []
        cost = 10000
        next_node_index = -1
        for i in range(80):
            print("state check",i)
            self.root.get_data().show_puzzle()
            print(self.root.get_data().compare_state())
            if self.root.get_data().compare_state() == 0:
                print(" reach goal ")
                break
            else:
                self.get_next_level()
            for j in range(len(self.root.leaves)):
                temp_puzzle = self.root.leaves[j].get_data()
                temp_cost = temp_puzzle.get_move_cost()
                if temp_cost <= cost:
                    cost = temp_cost
                    next_node_index = j
            if next_node_index >= 0:
                temp_puzzle = self.root.leaves[next_node_index].get_data()
                steps.append(temp_puzzle.get_move())
                self.root = self.root.leaves[next_node_index]

                self.depth += 1
                timers.append(time.time() - timer)
            else:
                break

            next_node_index = -1

        return steps, self.root.get_data(), timers
