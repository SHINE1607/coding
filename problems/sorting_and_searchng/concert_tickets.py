from bisect import bisect_right
def concert(n, m, arr1, arr2):
    arr1.sort()
    j = 0
    for i in range(m):
        index = bisect_right(arr1, arr2[i])
        if index > 0:
            print(arr1[index - 1])
            arr1.pop(index - 1)
        else:
            print(-1)

[n, m] = [int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]


concert(n, m, arr1, arr2)