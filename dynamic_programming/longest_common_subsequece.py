
from collections import defaultdict

def longest(string1, string2):
    m = len(string1)
    n = len(string2)
    dp = defaultdict(lambda:[0]*(n+1))
    string1 = " " + string1
    string2 = " " + string2
    for i in range(m + 1):
        for j in range(n + 1):
            if string1[i] == string2[j]:
                if j == 0:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i - 1][j] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

            
    print(dp[m][-1])




string1 = input()
string2 = input()
longest(string1, string2)
