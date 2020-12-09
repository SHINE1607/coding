from collections import defaultdict



def longest(n, string):
    dp = defaultdict(lambda: [0]*(n))

    i = 0
    for diff in range(0, n):
        
        i = 0
        while i + diff < n:
            
            if i == i + diff:
                dp[i][i + diff] = 1
                i += 1
                continue
                
            if string[i] == string[i + diff]:
                
                dp[i][i + diff] = dp[i + 1][i + diff - 1] + 2
            else:
                dp[i][i + diff] = max(dp[i + 1][i + diff], dp[i][i + diff - 1])
            
            i += 1
                
    print(dp[0][-1])

string = input()
longest(len(string), string)
