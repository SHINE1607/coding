#  given number of steps as an interger, find the number of ways to climb the steps if we can skip 1 or 2 steps ata atime 


from collections import defaultdict

def staircase(n):

    dp = defaultdict(int)
    dp[0] = 1
    dp[1] = 1


    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]



    print(dp[n])



n =  int(input())
staircase(n)