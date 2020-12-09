


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
    

arr = [2, 4, 11, 13, 45, 52, 79]
print(binary_search(arr, 100, 0, len(arr) - 1))




