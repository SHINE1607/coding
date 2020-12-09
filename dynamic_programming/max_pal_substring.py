# given astring we need to find the minumum number  of splits needed to make all subatrings are palindroem


from collections import defaultdict


def max_pal(string):
    dp = defaultdict(lambda:[-1] * len(string))
    n = len(string)
    for diff in range(n + 1):
        
        i = 0
        while i + diff < n:
            if i == i + diff:
                dp[i][i + diff] = 0
                i += 1
                continue
            
            if (string[i] == string[i + diff] and dp[i + 1][i + diff - 1] == 0) or (string[i] == string[i + diff] and diff == 1):
                dp[i][i + diff] = 0
            else:
                dp[i][i + diff] = min(dp[i + 1][i + diff] + 1, dp[i][i + diff - 1] + 1)

            i += 1

    print(dp[0][-1])
    
    




string = input()
max_pal(string)