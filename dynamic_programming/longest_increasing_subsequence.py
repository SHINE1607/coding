# given a array of intergers ,we need to find the longest increasing subsequence in the array


# we are doing a binary search and dp approach
# So we have iterate through the array and keep a track of the longest increasiung subsequnec in another array
# At ith elemnt if greater the last element of longst subsequnce we simply appened it to it
# or if it is lesss than that we find a suitable position for it start a new parellel subsequenc for it 

# This approach has an O(nlogn) time complexity
from collections import defaultdict
from bisect import bisect_left

def find_longest(n, arr):
    # each element itself is a increasung subsequnce
    # dp_longest is not directly the longest increasing subsequence, the length of this is the ans
    # it simply like storing parellel subsequnce but just the current explicitly
    dp_longest = [arr[0]]
    ans = 1
     
    for i in range(1, n):
        # case 1: if the curr element is larger than last element if the longest subsequnec
        if arr[i] > dp_longest[-1]:
            dp_longest.append(arr[i])        
            ans = ans + 1

        else: 
            # finding the suitable position for the curr element
            pos = bisect_left(dp_longest, arr[i])  
            dp_longest[pos] = arr[i]
    print(ans)



n = int(input())
arr = [int(x) for x in input().split()]

find_longest(n, arr)
            
            
            
# bainry search function
def binary_search(arr, target,left, right):

    if left == right:
        if arr[left] == target:
            return left
        else:
            return  -1

    mid =  (left  + right)//2

    
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid)
    else: 
        return binary_search(arr, target, mid + 1, right)





