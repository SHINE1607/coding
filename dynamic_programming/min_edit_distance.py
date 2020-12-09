from collections import defaultdict


def min_dist(string1, string2):
    string1 = " " + string1
    string2 = " " + string2
    m = len(string1)
    n = len(string2)
    dp = defaultdict(lambda:[0]*(n))
    dp[0] = list(range(0, n))
    for i in range(1, m):
        for j in range(0, n):
            if j == 0:
                dp[i][j] = i
                continue
            if string1[i] == string2[j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

    print(dp[m - 1][-1])


string1 = input()
string2 = input()
min_dist(string1, string2)

