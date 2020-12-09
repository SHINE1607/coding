def trailing_zeros(n):
    ans  = 0
    i =  5
    while i <= n:
        ans += int(n/i)
        i *= 5
    print(ans)



n = int(input())
trailing_zeros(n)

