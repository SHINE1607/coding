
# rec fuction to find if the subset with targetsum can be found
def rec_sum(arr, i, s, target, ind):
    if s ==  target:
        return True
    if i == 0 and s != 0:
        return False
 
    return rec_sum(arr, i - 1, s, target, "kuntham") or rec_sum(arr, i - 1, s - arr[i], target, "remove")

def get_subset(n, arr):
    s = sum(arr)
    
    if s%2== 1:
        print(False)
        return
    target = s/2
    print(target)
    res = rec_sum(arr, n-1, s, target, "intial")
    print(res)


n = int(input())
arr = [int(x) for x in input().split()]
get_subset(n, arr)