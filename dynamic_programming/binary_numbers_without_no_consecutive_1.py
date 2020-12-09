# Given an integer n we have to fin dthe number of binary number with n digitys having no cosecutive 1s



def function(n):
    dp = [0]*(n+1)

    dp[1], dp[2] = 2, 3

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]


    print(dp)
    print (dp[-1])


n = int(input())
function(n)
