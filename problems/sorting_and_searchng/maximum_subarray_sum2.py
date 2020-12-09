
def find_sum(n, a, b, arr):
    start = 0
    end = a - 1
    curr_sum = sum(arr[:a])
    prev = curr_sum
    max_sum = sum(arr[:a])
    while end < n:
        # we are  adding ele at indx end
        max_sum = max(curr_sum, max_sum)
        end += 1  
        #  if end reaching end of the list, LOL
        if end < n:
            curr_sum += arr[end]
        

        # new group condition
        if (end - start >= b or end > n - 1) and start + a - 1 < n - 1:
            start += 1
            end = start + a - 1
            curr_sum = prev - arr[start - 1] + arr[end]
            prev = curr_sum
    print(max_sum)

[n, a, b] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
find_sum(n, a, b, arr)