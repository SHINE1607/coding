#  given some boxes of fixed lengthm, breadth and height with infite supply of them
# find the mx height we can make with them on a strict condition the lenth abd breadth of the subsequen tbox must be 
# less than the one preceeding it


from collections import defaultdict


def max_height(boxes):
    



n = int(input())
boxes = []
for i in range(n):
    boxes.append([int(x) for x in input().split())

max_height(boxes)