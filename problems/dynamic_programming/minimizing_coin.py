import sys
sys.setrecursionlimit(500000)
#  UNBOUNDED KNAPSACK PROBLEM

from collections import defaultdict
# dp  = defaultdict(bool)
# coins = 0
# ans = None





# def rec(arr1, arr2, coins, x):
#     global dp
#     # print(dp)
#     temp = []
#     for i in range(len(arr2)):
#         for j in range(len(arr1)):
#             # terminating condition for overflow
#             curr = arr2[i] + arr1[j]
#             if i == 0 and j == 0 and curr > x:
#                 ans = -1
#                 print(ans)
#                 return 
#             # terminating condition if we founf the perffect match
#             if curr == x:
#                 ans = coins
#                 print(ans)
#                 return
#             if curr > x:
#                 break
#             if curr < x:
#                 if dp[curr] == False:
#                     dp[curr] = True
#                     temp.append(curr)
               
#     temp = list(set(temp))
#     rec(arr1, temp, coins + 1, x)
 



 
def min_coins(n, x , arr):
    dp = defaultdict(list)
    dp[0] = 0



    for i in range(0, n):
        print(dp)
        for j in range(0, x + 1):
            if i == 0:
                if j%arr[i] == 0:
                    dp[arr[i]].append(1)
                else:
                    dp[arr[i]].append(0)
            else:
                if j < arr[i]:
                    dp[arr[i]].append(dp[arr[i - 1]][j])
                else:
                    
                    dp[arr[i]].append(dp[arr[i - 1]][j] + dp[arr[i]][j - arr[i]])

    print(dp)
            
 


[n, x] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
arr.sort()
min_coins(n, x, arr)