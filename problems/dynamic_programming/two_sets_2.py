from collections import defaultdict

def function(n):
    mod = 1e9 + 7
    # dp[i, j] =  number of ways from 1 to i can make uop the sum j
    dp = defaultdict(int)

    total_sum = int((n * (n + 1))/2)
    if total_sum %2 != 0:
        print(0)
        return
    else:
        total_sum = int(total_sum/2)
    
    for i in range(0, n):
        for curr_sum in range(0, total_sum + 1):
            if curr_sum == 0:
                dp[i, curr_sum] = 1
                continue
            if i > curr_sum:
                dp[i, curr_sum] = (dp[i - 1, curr_sum])%mod
            else:
                dp[i, curr_sum] = (dp[i - 1, curr_sum] + dp[i - 1, curr_sum - i])%mod   

    print(int(dp[n - 1, total_sum]))

    








n = int(input())
function(n)
