

def time(n, arr, t):
    temp = t*arr[0]
    final = temp
    # print(ans,"initial")
    for i in range(1, n):
        count = final/(arr[0] + arr[i])
        # print(arr[i],final, arr[0], count)
        if count <= 1:
            break
        else:
            count = int(count)
        temp -= (count * arr[0])
        final = temp
        print(final)
    print(final)
        




[n, t] = [int(x) for x  in input().split()]
arr = [int(x) for x  in input().split()]
arr.sort()
# print(arr)
time(n, arr, t)