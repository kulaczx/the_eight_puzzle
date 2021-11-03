from puzzle import puzzle
from node import mynode
from tree import tree
import os
import xlsxwriter

alist = [1, 2, 3, 4, 0, 5, 6, 7, 8]
atree = tree(alist)
p, t= atree.uniform_cost_search()
print("done searching")
for item in p:
    item.get_data().show_puzzle()

workbook = xlsxwriter.Workbook(r'C:\Users\asuka\PycharmProjects\170P1\the_eight_puzzle\time.xlsx')
worksheet = workbook.add_worksheet()
row = 0
for x in t:
    worksheet.write(row, 0, x[0])
    worksheet.write(row, 1, x[1])
    row += 1

workbook.close()