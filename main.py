from puzzle import puzzle
from node import mynode
from tree import tree
import os
import xlsxwriter

cases = [[1, 2, 3, 4, 5, 6, 7, 8, 0],
         [1, 2, 3, 4, 5, 6, 0, 7, 8],
         [1, 2, 3, 5, 0, 6, 4, 7, 8],
         [1, 3, 6, 5, 0, 2, 4, 7, 8],
         [1, 3, 6, 5, 0, 7, 4, 8, 2],
         [1, 6, 7, 5, 0, 3, 4, 8, 2],
         [7, 1, 2, 4, 8, 5, 6, 3, 0],
         [0, 7, 2, 4, 6, 1, 3, 5, 8]]

uniformSearch = []
MTH = []
MDH = []

#for case in cases:
atree = tree(cases[2])
p, t, n = atree.uniform_cost_search()
print("Uniform Cost searching")

for item in p:
    item.get_data().show_puzzle()

print("time: ", t, " total nodes: ", n)
uniformSearch.append((t, n))

btree = tree(cases[2])
p, t, n = btree.misplaced_tile_heuristic()
print("Misplaced Tile Heuristic")
for item in p:
    item.get_data().show_puzzle()

print("time: ", t, " total nodes: ", n)
MTH.append((t, n))

ctree = tree(cases[2])
p, t, n = ctree.manhattan_distance_heuristic()
print("Manhattan Distance Heuristic")
for item in p:
    item.get_data().show_puzzle()

print("time: ", t, " total nodes: ", n)
MDH.append((t, n))

print("result summary")

print("Uniform Cost Search")
for i in uniformSearch:
    print("time: ", i[0], " expanded nodes: ", i[1])

print("Misplaced Tile Heuristic")
for i in MTH:
    print("time: ", i[0], " expanded nodes: ", i[1])

print("Manhattan Distance Heuristic")
for i in MDH:
    print("time: ", i[0], " expanded nodes: ", i[1])
