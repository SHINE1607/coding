
from bisect  import bisect_left
from collections import defaultdict
def find_pos(n, arr):
    S= []
    for i in range(n): 
      
        print(arr[i], S)
        while (len(S) > 0 and S[-1] >= arr[i]): 
            S.pop() 
  
        
        if (len(S) == 0): 
            print("")
            # print(0, end = " ") 
        else:   
            print("")
            # print(S[-1], end = " ") 
  
        S.append(arr[i]) 





n = int(input())
arr = input().split()
find_pos(n, arr)