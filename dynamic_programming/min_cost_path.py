# Givan a matrix of cost (integers), fidn min cost to reach bottom right from top left 

from collections import defaultdict



def min_cost_path(r, c, matrix):

    dp = defaultdict(int)
    dp[0, 0] = matrix[0][0]
    for i in range(r):
        for j in range(c):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i, j] = dp[i, j - 1] + matrix[i][j]
                continue
            if j == 0:
                dp[i, j] = dp[i - 1, j] + matrix[i][j]
                continue
            # coming from top cell
            op1 = dp[i - 1, j] + matrix[i][j]
            # coming from the left cell
            op2 = dp[i, j - 1] + matrix[i][j]
            dp[i, j] = min(op1, op2)

    print(dp[r - 1, c - 1])

            



[rows, cols] = [int(x) for x in input().split()]
matrix = [None]*rows
for i in range(rows):
    matrix[i] = [int(x) for x in input().split()] 

min_cost_path(rows, cols, matrix)
    