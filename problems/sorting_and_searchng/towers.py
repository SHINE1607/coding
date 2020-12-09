from bisect import bisect_right
from collections import defaultdict
def towers(n, arr):
    # towers[arr[0]] = [arr[0]]
    rep = [arr[0]] 
    ans = 1
    for i in range(1, n):
        index = bisect_right(rep, arr[i])
        if index >= ans:
            rep.append(arr[i])
            ans += 1
        else:
            old = rep[index]
            new = arr[i]
            rep[index] = new
    print(ans)
        
    






n = int(input())
arr = [int(x) for x in input().split()]
towers(n, arr)