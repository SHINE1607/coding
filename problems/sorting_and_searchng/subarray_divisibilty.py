from collections import defaultdict
def subarray(n, arr):
    prefix_sum = [arr[0]]
    ans = 0
    if arr[0]%n == 0:
        ans += 1
    mapping = defaultdict(int)
    mapping[arr[0]%n] += 1
    for i in range(1, n):
        prefix_sum.append(prefix_sum[-1] + arr[i])
        mapping[prefix_sum[-1]%n] += 1
        count = mapping[prefix_sum[-1]%n]
        # print(i, count)
        if prefix_sum[-1]%n == 0:
            ans += 1
        if count > 1:
            ans += count - 1
        

        
        
        
    print(ans)
    # print(prefix_sum)






        
    # print(prefix_sum)
    # print(mapping)
    # print(ans)
        
        

n = int(input())
arr = [int(x) for x in input().split()]
# arr.sort()
subarray(n,  arr)