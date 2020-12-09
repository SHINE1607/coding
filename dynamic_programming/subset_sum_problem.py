# Given an array of integers and a tragert sum, we need find whether the array elements can make up the target sum

# Case 1
# input line 1: 6 9
# input line 2: 3 34 4 12 5 2 
# ans: True

# Case : 2
# input line 1 : 6 30
# input line2 : 3 34 4 12 5 2 
# ans: False

from collections import defaultdict

def find_subset(n, arr, target):
    arr = [0] + arr
    dp = defaultdict(lambda: [False]*(target + 1))
    dp[0][0] = True
    for i in range(1, n + 1):
        if arr[i] > target:
            dp[i] = dp[i - 1]
            continue
        dp[i][:arr[i]] = dp[i - 1][:arr[i]]
        curr = arr[i]
        while curr < target + 1:
            if dp[i - 1][curr - arr[i]]:
                dp[i][curr] = True
                if curr == target:
                    print(True)
                    return





            curr += 1
    print(False)

    



[n, target]= [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

find_subset(n, arr, target)