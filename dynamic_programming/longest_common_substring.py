# given 2 strings we need to fing the longest common substring


from collections import defaultdict


def longest(string1, string2):
    string1 = " " + string1
    string2 =  " " + string2 
    p = len(string1)
    q = len(string2)
    dp = defaultdict(lambda:[0]*(q))
    ans = 0
    for i in range(1, p):

        for j in range(1, q):
            if j == 0:
                dp[i][j] = 0
                continue
            if string1[i] == string2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                
                ans = max(dp[i][j], ans)
            else:
                dp[i][j] = 0
    print(ans)

   



string1 = input()
string2 = input()
longest(string1, string2)