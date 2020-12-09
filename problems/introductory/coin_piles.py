def coin_piles(arr):
    minimum =  min(arr)
    maximum = max(arr)
    if (minimum + maximum) % 3 ==0 and maximum <= 2*minimum:
        print("YES")
    else:
        print("NO")


n = int(input())
for i in range(n):
    arr = [int(x) for x in input().split()]
    coin_piles(arr)