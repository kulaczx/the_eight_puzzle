from puzzle import puzzle
from node import mynode
from tree import tree

alist = [1, 2, 3, 4, 0, 5, 6, 7, 8]
newP = puzzle(alist)
if not newP.move_blank_right():
    print("not")
print(newP.compare_state())
newP.show_puzzle()

atree = tree(alist)
a, b, c = atree.uniform_cost_search()
print(a)
b.show_puzzle()
print(c)
