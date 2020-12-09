from collections import defaultdict
def movies(n, arr):
    ans = 0
   

    for i in range(len(arr)):
        if i == 0:
            ans += 1
            last_end = arr[0][0]
            continue
        else:
            if arr[i][1] >= last_end:
                # new movie found to watch
                ans += 1
                last_end = arr[i][0]
                continue
            if arr[i][1] < arr[i - 1][0]:
                continue
            
        
                
    print(ans)



n  = int(input())
arr = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    arr.append((temp[1], temp[0]))

arr.sort()
movies(n,arr)