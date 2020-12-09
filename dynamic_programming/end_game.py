# GIven some denominations of coins arranged in an order, we have to play a game to optimally maximze the score
# if 2 playes alternatievely make the selection 
# the objective is to maximize the profit of player 1


from collections import defaultdict


def end_game(n, coins):
    dp = defaultdict(lambda : [(-1, -1)]*n)

    for diff in range(n + 1):
        
        i = 0
        while i + diff < n:
            if i == i + diff:
                dp[i][i + diff] = (coins[i], 0)
                i += 1
                continue

            curr = coins[i: i + diff + 1]
           
            # we can start with either the first element or the last
            op1 =  (curr[0] + dp[i + 1][i + diff][1], dp[i + 1][i + diff][0])
            op2 = (curr[-1] + dp[i][i + diff - 1][1], dp[i][i + diff - 1][0])
            dp[i][i + diff] = max(op1, op2)

            i += 1
    print(dp[0][-1][0])




            
            
            




n = int(input())
coins = [int(x) for x in input().split()]
end_game(n, coins)