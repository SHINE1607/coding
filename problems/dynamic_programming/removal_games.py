import time
start_time = time.time()
from collections import defaultdict 
import sys
sys.setrecursionlimit(500000000)
ans = 0


dp = defaultdict(lambda:[None, None])
def rec(i, j, arr): 
    # print(i , j)
    global dp
    # filling the dp if there is omnly one ele
    if i == j:
        dp[i, j] = [arr[i], 0]
        return 
    
    if i > j:
        return

    #if the player selecting the first coin
    if dp[i + 1, j] == [None, None]: 
        rec(i + 1, j, arr)
    op1 = arr[i] + dp[i + 1, j][1]

    # if the palyer selecting the last coin
    if dp[i, j - 1] == [None, None]:
        rec(i, j - 1, arr)
    op2 = arr[j] + dp[i, j - 1][1]

    dp[i, j] = [max(op1, op2), sum(arr[i:j+1]) - max(op1, op2)]

def max_score(n, scores):
    global dp
    rec(0, n - 1, scores)
    print(dp[0, n - 1][0])


# n = int(input())
# scores = [int(x) for x in input().split()]
with open('test_input.txt', 'r') as file:
   lines = file.readlines()

# lines.split()
lines = lines[0].split()
scores = [int(x) for x in lines]
# print(type(scores[0]))
n = 5000
max_score(n, scores)
print("--- %s seconds ---" % (time.time() - start_time))
