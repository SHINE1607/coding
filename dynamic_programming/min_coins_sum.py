# given a number of coins with infinte supply with  certian denominations, 
# find the min number of coins to make the given sum

from collections import defaultdict

def min_coins(coins, target):
    dp = defaultdict(lambda:[10e9 + 7]*(target + 1))
    n = len(coins)

    for i in range(n):
        for change in range(target + 1):
            if change == 0:
                dp[i][change] = 0
                continue
        

            op1 = dp[i - 1][change]
            op2 = dp[i][change - coins[i]] + 1


            dp[i][change] = min(op1, op2)


            
    
    print(dp[n - 1][-1])





coins = [int(x) for x in input().split()]
target = int(input())
min_coins(coins, target)