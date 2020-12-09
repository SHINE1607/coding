from collections import defaultdict 

def find_path(n, grid):
    global dp
    mod = 1e9 + 7
    if grid[n - 1][n - 1] == "*":
        print(0)
        return
    else:
        dp[n - 1][n - 1] = 1
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, - 1, -1):
            if i == n - 1 and j == n - 1:
                continue
            if grid[i][j] == "*":
                dp[i][j] = 0
                continue

            if i == n - 1 and j < n - 1:
                dp[i][j] = dp[i][j + 1]
                continue
            elif j == n - 1 and i  < n - 1:
                dp[i][j] = dp[i + 1][j]
                continue
            
            else:
                dp[i][j] = (dp[i + 1][j] + dp[i][j + 1])%mod
    print(int(dp[0][0]))
        
            


n = int(input())
arr = []
for i in range(n):
    arr.append(list(input()))
dp = defaultdict(lambda:([0]*n))
find_path(n, arr)