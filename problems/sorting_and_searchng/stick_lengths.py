import math
def modify(n, arr):
    
    upper = arr[int(math.ceil(n/2))]
    lower = arr[int(n/2 - 1)]
    if upper == lower:
        ans = 0
        for i in arr:
            ans += abs(i - upper)
        print(ans)
    else:
        ans1, ans2 = 0, 0
        for i in arr:
            ans1 += abs(i - upper)
            ans2 += abs(i - lower)
        # print(ans1, ans2,"uppper", "lowr")
        print(min(ans1, ans2))





n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
modify(n, arr)