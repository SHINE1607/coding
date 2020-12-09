# Given array of permissible jumps from theat position, find min number of jumps needed to
# reach the last position

from collections import defaultdict 


# dp[i] = min number of steps needed to reach ith pos

def min_jumps(n, jumps):
    dp_jumps = [1e7 + 9]*n
    dp_jumps[0] = 0
    for i in range(1, n):
        j = 0
        while j < i:
            if i - j <= jumps[j]: # condition that we can jump from the curr element
                dp_jumps[i] = min(dp_jumps[j] + 1, dp_jumps[i])
            j += 1

    print(dp_jumps[-1])




n =  int(input())
jumps = [int(x) for x in input().split()]


min_jumps(n, jumps)
