from collections import defaultdict 
def get_sum(n, x ,arr, org):
    left = 0
    right  = n -1
    while left < right:
        diff = x- (int(arr[left]) + int(arr[right]))
        if str(diff) in set(arr[left + 1: right]):
            i1 = org.index(str(arr[left]) , 0)
            i2 = org.index(str(diff) , i1 + 1)
            try:
                i3 = org.index(str(arr[right]), i2 + 1)
            except:
                i3 = org.index(str(arr[right]))
            print(i1 + 1, i2 + 1, i3 + 1)
            return
        if diff == 0:
            right -= 1
            continue

        if diff <= int(arr[left]):
            right -=  1
            continue
        
        if diff >= int(arr[right]):
            left += 1
            continue
        
    print("IMPOSSIBLE")
    

        

    




[n, x] = [int(x) for x in input().split()]
arr = input().split()
org = arr.copy()
arr.sort()
get_sum(n, x, arr, org)