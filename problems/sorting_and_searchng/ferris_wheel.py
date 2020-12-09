ans = 0

def ferris_wheel(n, m, arr):
    arr.sort()
    global ans
    left = 0
    right = n - 1
    
    while left <= right:
        if arr[left] + arr[right] > m:
            ans += 1
            right -= 1
        elif arr[left] + arr[right] <= m:
            left += 1
            right -= 1
            ans += 1
    print(ans)


[n, m] = [int(x) for x in input().split()]
string = input().split()
arr = []

for i in string:
    if int(i) >= m:
        ans += 1
        n -= 1
    else:
        arr.append(int(i))


ferris_wheel(n, m , arr)