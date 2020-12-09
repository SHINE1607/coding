# given an array of integers we need to find the longest binary subseuqnce 
# binary sequence are the one which first incareses then decreases
# longest binary sequence if calculafed by finding the longest increases subsequnec of the forward array and 
# reverse array and addinf there dps
from bisect import bisect_left


def longest_subsequence(arr):

    n = len(arr)
    dp = [0]
    dp[0] = arr[0]
    dp_longest = [1]*n
    for i in range(1, n):
        
        if arr[i] > dp[- 1]:
            dp.append(arr[i])
            dp_longest[i] = len(dp)
            continue
        pos = bisect_left(dp, arr[i])
        if pos < len(dp):
            dp[pos] = arr[i]
            dp_longest[i] = len(dp)

    return dp_longest





arr = [int(x) for x in input().split()]
dp1 = longest_subsequence(arr)
dp2 = longest_subsequence(arr[::-1])
print(dp1)
print(dp2[::-1])
print(max([sum(x) for x in zip(dp1, dp2[::-1])]))
