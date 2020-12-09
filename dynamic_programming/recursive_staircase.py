# given the number of steps we can take at a time howe mkany tyital number of ways to climb given number of steps
from collections import defaultdict
def find_climb(n, steps):
    dp = defaultdict(lambda:[0] * (n + 1))
    steps = [0] + steps
    dp[0][0] = 1
    for i in range(1, len(steps)):
        if steps[i] > n:
            continue
        dp[i][:steps[i]]  = dp[i - 1][:steps[i]]
        
        for j in range(steps[i], n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - steps[i]]


    print(dp[i][-1])
    




n = int(input())
steps = [int(x) for x in input().split()]
find_climb(n, steps)