# Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
# The problem is not actually to perform the multiplications, but merely to decide in which order 
# to perform the multiplications.

# We have many options to multiply a chain of matrices because matrix multiplication is associative. 
# In other words, no matter how we parenthesize the product, the result will be the same.

from collections import defaultdict
def min_cost(n, size):
    # dp[i][j] is the minimum cost to multiply matrices from index i to j 
    dp = defaultdict(lambda:[0]*n)
    index_map = defaultdict(lambda:(0, 0))
    for length in range(n):
        i = 0
        while i + length < n:
            if i == i + length:
                dp[i][i + length] = 0
                index_map[i, i + length] = (size[i][0], size[i][1])
                i += 1
                continue
            # option 1 :taking the left element
            # multiplying the i th element to right
            op1 = dp[i][i + length - 1] + index_map[i, i + length - 1][0] * index_map[i, i + length - 1][1] * size[i + length][1]


            # option 2: taking the bottom element
            # multiplying the current i + diff th element to the left 
            op2 = dp[i + 1][i + length] + size[i][0] * index_map[i + 1, i + length][0] * index_map[i + 1, i + length][1]
            # selecting the best option from the two
            dp[i][i + length] = min(op1, op2)
            if op1 < op2:
                index_map[i, i + length] = (index_map[i, i + length - 1][0], size[i + length][1])
            else:
                index_map[i, i + length] = (size[i][0], index_map[i + 1, i + length][1])
            i += 1

    print(dp[0][-1])
    for i in dp.keys():
        print(dp[i])

n = int(input())
size = []
for i in range(n):
    size.append([int(x) for x in input().split()])
min_cost(n, size)

    


