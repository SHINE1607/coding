from collections import defaultdict
import sys
sys.setrecursionlimit(500000)
dp = defaultdict(list)
ans = 0
temp = []

def combinations(n, x, arr):
    dp = defaultdict(list)

    for i in range(0, n):
        j = 0
        while j < x + 1:
        
            if i == 0:
                if j%arr[i] == 0:
                    dp[arr[i]].append(1)
                else:
                    dp[arr[i]].append(0)
            else:

                if j < arr[i]:
                    dp[arr[i]] = dp[arr[i - 1]][:arr[i]]
                    j = arr[i]
                    continue
                else:
                     
                    dp[arr[i]].append((dp[arr[i - 1]][j] + dp[arr[i]][j - arr[i]])%(1e9 + 7))
            j += 1

    print(int(dp[arr[-1]][-1]))
            





 

[n, x] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()
combinations(n, x, arr)
