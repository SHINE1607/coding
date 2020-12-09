# Given an array of intergers find the subarray having the max sum 
# Kadanes algorithm
# time complexity: O(n)


# teh idea is we are tracking the largest possible sum till ith position in ans 
# the current_sum in curr_sum 
# foreach element we hav 2 choices, either we can add thatelement to the curr_sum or we start a new subarray from that element
from collections import defaultdict


def kadanes(arr):
    curr_sum = arr[0]
    ans = arr[0]    
    n = len(arr)

    for i in range(1, n):
        op1 = arr[i]
        op2 = curr_sum + arr[i]


        curr_sum = max(op2, op1) 
        ans = max(ans, curr_sum)
        
            

    ans = max(curr_sum, ans)

    print(ans)

            





arr = [int(x) for x in input().split()]
kadanes(arr)
