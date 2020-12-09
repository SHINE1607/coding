

def repititions(n, arr):
    cur_largest = arr[0]
    turns = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            turns += (arr[i - 1] - arr[i])
            arr[i] = arr[i - 1]
        elif arr[i] >= arr[i - 1]:
            curr_largest = arr[i]
    print(turns)
    








n = int(input())
arr = [int(x) for x in input().split()]
repititions(n, arr)


