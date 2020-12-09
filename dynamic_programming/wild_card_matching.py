# we have a pattern and a string, we need to tell pattern matched string or not
# "*" ==> 0 or more sequence
# "?" ==> any one character

# test case:
# x?y*z
# xaylmz


from collections import defaultdict

def wild_card_match(string, pattern):
    string = " " + string
    pattern = " " + pattern
    s = len(string)
    p = len(pattern)
    dp = defaultdict(lambda:[False] * p)
    dp[0][0] = True
    for i in range(1, s):
        for j in range(1, p):
            # case 1: if the twwo strings match or "."
            if (string[i] == pattern[j] or pattern[j] == "?" ) and dp[i - 1][j - 1] == True:
                dp[i][j] = True
                
            # case2: if the pattern is "#"
            if pattern[j] == "*":
                if dp[i - 1][j] == True or dp[i][j - 1] == True:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

    print(dp[s - 1][-1])

    






pattern = input()
string = input()

wild_card_match(string, pattern)