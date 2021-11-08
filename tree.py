from node import mynode
from puzzle import puzzle
import time
import queue
import sys


def get_next_level(anode):
    getNext = anode.get_data()
    temp = getNext.cpy_puzzle()
    temp.set_parent_move(getNext.move)
    node_created = 0
    if temp.move_blank_up():
        new_node = mynode(temp)
        new_node.depth = anode.depth + 1
        anode.insert_leaf(new_node)
        temp = getNext.cpy_puzzle()
        node_created += 1

    if temp.move_blank_right():
        new_node = mynode(temp)
        new_node.depth = anode.depth + 1
        anode.insert_leaf(new_node)
        temp = getNext.cpy_puzzle()
        node_created += 1

    if temp.move_blank_down():
        new_node = mynode(temp)
        new_node.depth = anode.depth + 1
        anode.insert_leaf(new_node)
        temp = getNext.cpy_puzzle()
        node_created += 1

    if temp.move_blank_left():
        new_node = mynode(temp)
        new_node.depth = anode.depth + 1
        anode.insert_leaf(new_node)
        node_created += 1

    return node_created

def puzzle_check(lists, target):
    for item in lists:
        if item == target:
            return True
    return False


class tree:
    def __init__(self, data):
        pzl = puzzle(data)
        self.root = mynode(pzl)
        self.head = self.root
        self.depth = 0

    def uniform_cost_search(self):
        q = queue.PriorityQueue()
        visited_node = set()
        visited_node.add(self.root)
        q.put((0, self.root, [self.root]))
        timer = time.time()
        total_nodes = 0
        while not q.empty():
            current_node_priority, current_node, path = q.get()
            current_puzzle = current_node.get_data()
            visited_node.add(current_node)
            total_nodes += get_next_level(current_node)
            current_time = time.time() - timer
            if current_puzzle.compare_state() == 0:
                print("find goal")
                return path, current_time, total_nodes
            else:
                for children in current_node.leaves:
                    if children not in visited_node:
                        q.put((current_node_priority + children.cost, children, path + [children]))

        print("q is empty")
        sys.exit(0)

    def misplaced_tile_heuristic(self):
        q = queue.PriorityQueue()
        visited_node = set()
        temp_puzzle = self.root.get_data()
        q.put((temp_puzzle.compare_state(), self.root, [self.root]))
        visited_puzzled = []
        timer = time.time()
        total_nodes = 0
        while not q.empty():
            current_node_priority, current_node, path = q.get()
            current_puzzle = current_node.get_data()
            visited_puzzled.append(current_puzzle.state)
            visited_node.add(current_node)
            total_nodes += get_next_level(current_node)
            current_time = time.time() - timer
            if current_puzzle.compare_state() == 0:
                print("find goal")
                return path, current_time, total_nodes
            else:
                for children in current_node.leaves:
                    temp = children.get_data()
                    misplaced = temp.compare_state()
                    if not puzzle_check(visited_puzzled, temp.state):
                        q.put((misplaced, children, path + [children]))
        print("q is empty")
        sys.exit(0)

    def manhattan_distance_heuristic(self):
        q = queue.PriorityQueue()
        visited_node = set()
        temp_puzzle = self.root.get_data()
        q.put((temp_puzzle.compare_state(), self.root, [self.root]))
        timer = time.time()
        total_nodes = 0
        visited_puzzle = []
        while not q.empty():
            current_node_priority, current_node, path = q.get()
            current_puzzle = current_node.get_data()
            visited_node.add(current_node)
            visited_puzzle.append(current_puzzle.state)
            total_nodes += get_next_level(current_node)
            current_time = time.time() - timer
            if current_puzzle.compare_state() == 0:
                print("find goal")
                return path, current_time, total_nodes
            else:
                for children in current_node.leaves:
                    temp = children.get_data()
                    mdh = temp.distance_to_goal()
                    if not puzzle_check(visited_puzzle, temp.state):
                        q.put((mdh, children, path + [children]))
        print("q is empty")
        sys.exit(0)
