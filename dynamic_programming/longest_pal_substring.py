
from collections import defaultdict

ans = 1
def find_longest(n, string):
    global ans
    dp = defaultdict(lambda:[0]*n)


    for diff in range(0, n):
        # print(i)
        i = 0
        while i + diff < n:
            if i == i + diff:
                dp[i][i + diff] = 1
                i += 1
                continue
            
            if string[i] == string[i + diff]:
                if diff == 1:
                    dp[i][i + diff] = 1
                    ans = max(ans, diff + 1)
                else:
                    if dp[i + 1][i + diff - 1] == 1:
                        dp[i][i + diff] = 1
                        ans = max(ans, diff + 1)
                        

    

            i += 1
    for i in dp.keys():
        print(dp[i])
    print(ans)




string = input()
find_longest(len(string), string)
