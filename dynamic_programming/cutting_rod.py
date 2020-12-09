from collections import defaultdict

# dp state
# dp[i][j] = maximum profit thta can be achieved for a rod of length j 
# if we can cut in i ways


def max_profit(l, cuts, values):
    dp = defaultdict(lambda:[0]*(l + 1))
    cuts = [0] + cuts
    values = [0] + values
    dp[0] = [0]*(l+1)
    for i in range(1, len(cuts)):
        dp[i][:cuts[i]] = dp[i - 1][:cuts[i]]
        for length in range(cuts[i], l + 1):
            
            # op1: if we direclt take the previsou value
            op1 = dp[i-1][length]
            # op2: if we take the current cut intto action
            op2 = values[i] + dp[i][length - cuts[i]]

            dp[i][length] = max(op1, op2)


    print(dp[len(cuts) - 1][-1])





rod_length = int(input())
cuts = [int(x) for x in input().split()]
values = [int(x) for x in input().split()]
max_profit(rod_length, cuts, values)

