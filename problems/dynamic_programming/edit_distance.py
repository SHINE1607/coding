from collections import defaultdict
import sys
sys.setrecursionlimit(600000000)
dp = defaultdict(lambda:None)


def editDistance(str1, str2, m, n): 
  
    global dp
    if m == 0: 
         return n 
  
    if n == 0: 
        return m 
    if str1[m-1]== str2[n-1]: 
        if dp[(m - 1, n - 1)] == None:
            dp[(m - 1, n - 1)] = editDistance(str1, str2, m-1, n-1)
            return dp[(m - 1, n - 1)]


    if dp[(m, n - 1)] == None:
        dp[(m , n - 1)] = editDistance(str1, str2, m, n - 1)
    if dp[(m -1, n)] == None:
        dp[(m -1, n)] = editDistance(str1, str2, m-1, n)
    if dp[(m - 1, n - 1)] == None:
        dp[(m - 1, n - 1)] = editDistance(str1, str2, m- 1, n - 1)
    return 1 + min(dp[(m, n - 1)],    # Insert 
                   dp[(m -1, n)],    # Remove 
                   dp[(m - 1, n - 1)])    # Replace ) 


string1 = input()
string2 = input()

print(editDistance(string1, string2, len(string1), len(string2)))# find_distance(string1, string2)  
# print(dp[len(string1), len(string2)])
# print("buls")