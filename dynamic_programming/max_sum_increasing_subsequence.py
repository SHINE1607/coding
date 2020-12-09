# given array of integers find the subsequnce of the array having the max sum and increasing 


def find_max(arr):
    curr_sum = 0
    ans = 0
    n = len(arr)
    dp = arr.copy()
    for i in range(1, n):
        curr_sum = 0
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
        ans = max(dp[i], ans)


    print(ans)
    print(dp)

                







arr = [int(x) for x in input().split()]
find_max(arr)



