# given a matrix of only 0 and 1, we need to find the largest submatrix having only ones

from collections import defaultdict

def find_max(rows, cols, matrix):
    # dp[i][j] = maximum susqaure matrix that can be formed until i, j
    # dp[i][j] = 0, if original matrix has 0 at that index

    # 0 can be considered as False here
    ans = 0
    dp = defaultdict(lambda:[0]*(cols + 1))
    dp[0] = [0]*(cols + 1)
    for i in range(rows):
        for j in range(cols):

            if matrix[i][j] == 0:
                dp[i + 1][j + 1] = 0
                continue

            if matrix[i][j] == 1:
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1], dp[i][j]) + 1
                ans = max(ans, dp[i + 1][j + 1])
            
    print(ans)




[rows, cols] = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split()])

find_max(rows, cols, matrix)