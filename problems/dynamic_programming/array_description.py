

ans = 0
def rec(n, m, arr, index):
    global ans
    if arr[index] != 0 or index == n:
        return





def find_des(n, m , arr):
    rec(n, m, arr, 0)
    
                
              
[n, m] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

find_des(n, m, arr)

