from collections import Counter


def min_time(n, arr):
    arr.sort()
    ans = max(sum(arr), 2*arr[-1])
    print(ans)



n = int(input())
arr = [int(x) for x in input().split()]
min_time(n, arr)
