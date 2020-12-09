
# GIven  n number of binary trees, find total number of binary search trees possible 
from math import factorial



def binary_trees_count(n):
    ans = factorial(2 * n)/(factorial(n) * (n + 1)* factorial(n))
    print(int(ans))


n = int(input())
binary_trees_count(n)