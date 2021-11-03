from node import mynode
from puzzle import puzzle
import time
import queue


class tree:
    def __init__(self, data):
        pzl = puzzle(data)
        self.root = mynode(pzl)
        self.head = self.root
        self.depth = 0

    def get_next_level(self, anode):
        getNext = anode.get_data()
        temp = getNext.cpy_puzzle()
        if temp.move_blank_up():
            new_node = mynode(temp)
            new_node.depth = anode.depth + 1
            anode.insert_leaf(new_node)
            temp = getNext.cpy_puzzle()
        if temp.move_blank_down():
            new_node = mynode(temp)
            new_node.depth = anode.depth + 1
            anode.insert_leaf(new_node)
            temp = getNext.cpy_puzzle()
        if temp.move_blank_right():
            new_node = mynode(temp)
            new_node.depth = anode.depth + 1
            anode.insert_leaf(new_node)
            temp = getNext.cpy_puzzle()
        if temp.move_blank_left():
            new_node = mynode(temp)
            new_node.depth = anode.depth + 1
            anode.insert_leaf(new_node)

    def uniform_cost_search(self):
        q = queue.PriorityQueue()
        visited_node = set()
        visited_node.add(self.root)
        q.put((0, self.root, [self.root]))
        timer = time.time()
        time_lst = []
        while not q.empty():
            current_node_priority, current_node, path = q.get()
            current_puzzle = current_node.get_data()
            visited_node.add(current_node)
            if current_node.depth <= 80:
                self.get_next_level(current_node)
                current_time = time.time() - timer
                time_lst.append((current_node.depth, current_time))
                if current_puzzle.compare_state() == 0:
                    print("find goal")
                    return path, time_lst
                else:
                    for children in current_node.leaves:
                        if children not in visited_node:
                            q.put((current_node_priority + children.cost, children, path + [children]))

    def misplaced_tile_heuristic(self):
        q = queue.PriorityQueue()
        visited_node = set()
        temp_puzzle = self.root.get_data()
        q.put((temp_puzzle.compare_state(), self.root, [self.root]))
        timer = time.time()
        time_lst = []
        while not q.empty():
            current_node_priority, current_node, path = q.get()
            current_puzzle = current_node.get_data()
            visited_node.add(current_node)
            if current_node.depth <= 80:
                self.get_next_level(current_node)
                current_time = time.time() - timer
                time_lst.append((current_node.depth, current_time))
                if current_puzzle.compare_state() == 0:
                    print("find goal")
                    return path, time_lst
                else:
                    i = 0
                    child_index = 0
                    least_misplaced = 100
                    for children in current_node.leaves:
                        temp_puzzle = children.get_data()
                        misplaced = temp_puzzle.compare_state()
                        if misplaced < least_misplaced:
                            least_misplaced = misplaced
                            child_index = i
                        i += 1
                    if current_node.leaves[child_index] not in visited_node:
                        q.put((least_misplaced, current_node.leaves[child_index],
                               path + [current_node.leaves[child_index]]))

