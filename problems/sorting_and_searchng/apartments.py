

from collections import Counter

def apartments(n, m , k, need, size):
    need.sort()
    size.sort()
    ans = 0
    j = 0 
    j_next = 0
    for i in range(n): 

        while(j < m and abs(need[i] - size[j]) > k):
            j += 1
        if j < m and abs(need[i] - size[j]) <= k:
            j += 1
            ans += 1 
            j_next = j
        if j == m:
            j = j_next
    print(ans)


[n, m, k] = [int(x) for x in input().split()]
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
apartments(n, m, k, arr1, arr2)