
# given an array of integers we need to find the subsequnec with max sum which are not adjacent to each other


def find_max(arr):
    dp = [0]*len(arr)

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        dp[i] = dp[i - 2] + arr[i]
        
    print (dp)
    print(max(dp[- 1], dp[-2]))



arr = [int(x) for x in input().split()]
find_max(arr)