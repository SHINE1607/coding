from collections import defaultdict
def subarray(n, x, arr):
    mapping = defaultdict(int)
    
    curr_sum = 0
    ans = 0
    prefix_sum = [arr[0]]
    mapping[arr[0]] += 1
    if arr[0] == x:
        ans+= 1
    for i in range(1, n):
        prefix_sum.append(arr[i] + prefix_sum[-1])

        if prefix_sum[-1] == x:
            ans += 1
        
        if mapping[prefix_sum[-1] - x] > 0:
            ans += mapping[prefix_sum[-1] - x]
        
        mapping[prefix_sum[-1]] += 1


    print(ans)


           
        
[n, x] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
# arr.sort()
subarray(n, x, arr)