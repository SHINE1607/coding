#  0/1 knap sack problem 
#  Given weights and values of n items, put these items in a knapsack of 
# capacity W to get the maximum total value in the knapsack. In other words, 
# given two integer arrays val[0..n-1] and wt[0..n-1] which represent values 
# and weights associated with n items respectively. Also given an integer W 
# which represents knapsack capacity, find out the maximum value subset of 
# al[] such that sum of the weights of this subset is smaller than or equal 
# to W. You cannot break an item, either pick the complete item or don’t pick 
# it (0-1 property).



from collections import defaultdict

def knapsack(n, weights, values, target):
    values = [0] + values
    weights = [0] + weights

    dp = defaultdict(lambda: [0]*(target + 1))
    dp[0] = [0]*(target + 1)
    for i in range(1, n + 1):
        for j in range(0, target + 1):
            if j == 0:
                dp[i][j] = 0
                continue
            
            if weights[i] > j:
                dp[i][j] = dp[i - 1][j]
                continue
            
            op1 = dp[i - 1][j]
            op2 = values[i] + dp[i - 1][j - weights[i]]
            
            dp[i][j] = max(op1, op2)
        

    print(dp[n][-1])
            
            

n = int(input())
weights = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]
target = int(input())
knapsack(n, weights, values, target)

