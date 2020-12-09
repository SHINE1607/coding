from collections import defaultdict
 
def playlist(n, arr):
    s = set()
    j = 0   # loop variable for curr arr 
    ans = 0
    for i in range(n):
        while arr[i] in s:
            s.remove(arr[j])
            
            j += 1

        s.add(arr[i])
        ans = max(ans, len(s))    
    print(ans)


n = int(input())
arr = [int(x) for x in input().split()]
playlist(n, arr)