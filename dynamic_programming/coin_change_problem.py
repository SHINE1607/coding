# if we have infite supply of coins of diffreer denominations,
# find then minium number of coins to make the target sum


from collections import defaultdict



def min_coins(n, coins,  target):
    dp = defaultdict(lambda:[0]*(target + 1))

    for i in range(n):
        if coins[i] > target:
            dp[i] = dp[i - 1]
            continue
        dp[i][:coins[i]] = dp[i - 1][:coins[i]]
        change = coins[i]
        while change < target + 1:
            if i == 0:
                if change%coins[i] == 0:
                    dp[i][change] = int(change/coins[i])
                change += 1
                continue
            # op1: to take the number of coins from the above denomination
            op1 = dp[i - 1][change]
            # op2:  add the current coin
            op2 = 1 + dp[i][change - coins[i]]

            dp[i][change] = min(op1, op2)
            change += 1


    print(dp[n - 1][-1])



[n, target] = [int(x) for x in input().split()]
coins = [int(x) for x in input().split()]
coins.sort()
min_coins(n, coins, target)