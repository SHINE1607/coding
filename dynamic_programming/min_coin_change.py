#  Given infinte supply of coins with some denominations  and a target value, find minimum number of coins to
# make the target

# smaple tvest case
# target:13
# coins 7 2 3 6



# dp[i][j] = minimum number of coins needed to nake the sum j with i coins
from collections import defaultdict

def min_coins(target, coins):
    mod = 1e7 + 9
    coins = [0] + coins
    dp = defaultdict(lambda:([0] + [mod]*(target)))
    dp[0][0] = 0
    for i in range(1, len(coins)):
        if coins[i] > target:
            continue
        dp[i][:coins[i]] = dp[i - 1][:coins[i]]
        for j in range(coins[i], target + 1):
            
            op1 = dp[i - 1][j]
            op2 = dp[i][j - coins[i]] + 1
            
            dp[i][j] = min(op1, op2)
            
        
    
    if dp[list(dp.keys())[-1]][-1] == mod:
        print("The given sum cannnot be made")
    else:
        print(dp[list(dp.keys())[-1]][-1])
            




target = int(input())
coins = [int(x) for x in input().split()]
min_coins(target, coins)




