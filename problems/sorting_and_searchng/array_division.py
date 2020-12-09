
def divide(n, k, arr):

    t = sum(arr)/k
    # print(t)
    curr_sum  = []
    i = 1
    largest = 0
    curr_sum = [arr[0]]
    if k == 1:
        print(int(t * k))
        return
    j = 0
    while i < n:
        curr_sum.append(curr_sum[-1] + arr[i])
        if i < n - 1:
            # print(arr[i])
            d1 = abs(t - curr_sum[-1])
            d2 = abs(t - (curr_sum[-1] + arr[i + 1]))
            
        
            if d1 < d2:
                j += 1
                # found a new group in the left group
                largest = max(curr_sum[-1], largest)
                curr_sum[-1] = 0
            # else:
            #     j += 1
            #     largest = max(curr_sum[-1] + arr[i + 1], largest)
            #     curr_sum[-1] = 0
            #     i += 1
            
        if j == k:
            largest = max(largest, sum(arr[i:]))
            break
        
        if i == n-1:
            largest  = max(largest, curr_sum[-1])
        i += 1
    
    print(largest)
[n, k] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
divide(n,k,  arr)