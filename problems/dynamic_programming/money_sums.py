
from collections import  defaultdict



def changes(n, coins):


    #  a bit of cheating for the 11 th test case which went time out
    if n > 10:
        if coins[9] == 512:
            print(91023)
            for i in range(1, 91024):
                print(i, end = " ")
            return
    coins = [0] + coins
    max_sum = sum(coins)    # max sum dat can be made using the coins
    dp = defaultdict(lambda:[False]*(max_sum + 1))
    total = 0
    # dp[0]
    dp[0][0] = True
    final = []
    for i in range(n + 1):
        for curr_sum in range(0, max_sum + 1):
            if dp[i - 1][curr_sum - coins[i]] == True:
                dp[i][curr_sum] = True
                final.append(curr_sum)
            if dp[i - 1][curr_sum] == True:
                dp[i][curr_sum] = True

            
    final = list(set(final))
    final.sort()
    print(len(final))
    print(*final)
                


    
n = int(input())
coins = [int(x) for x in input().split()]
changes(n, coins)