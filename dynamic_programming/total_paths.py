# given a matrxi of size m x n, finf number of ways to reach bottom right starting top left , if you can 
# go either only right or bottom

from collections import defaultdict



def total_paths(m,n):
    dp = defaultdict(lambda: [0]*n)
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if j == 0:
                dp[i][j] = 1
                continue 
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    for i in dp.keys():
        print(dp[i])
        
            
            





[m, n] = [int(x) for x in input().split()]
total_paths(m, n)

