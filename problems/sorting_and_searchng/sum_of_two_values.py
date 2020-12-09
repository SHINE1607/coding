from bisect import bisect_right
def find_sum(n, x, arr):
    temp = arr.copy()
    arr.sort()
    left = 0
    right = n - 1
    while(left < right):
        if arr[left] + arr[right] < x:
            left = left + 1
        elif arr[left] + arr[right] > x:
            right -= 1
        else:
            left_index = temp.index(arr[left])
            right_index = n - temp[::-1].index(arr[right])
            print(left_index + 1, right_index)
            return
    print("IMPOSSIBLE")






[n, x] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

find_sum(n,x, arr)