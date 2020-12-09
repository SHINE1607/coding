from collections import defaultdict 
def longest(n, arr):
    dp = defaultdict(lambda:1)
    largest = 1
    for i in range(n - 1):
        
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                dp[j] = dp[i] + 1
            largest = max(dp[j], largest)
            
 
    print(largest)
 
 
n = int(input())
arr = [int(x) for x in input().split()]


longest(n, arr)
