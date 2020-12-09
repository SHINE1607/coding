import random







def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    res = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            res.append(left[left_pointer])
            left_pointer += 1
        else:
            res.append(right[right_pointer])
            right_pointer += 1

    if left_pointer < len(left):
        res += left[left_pointer:]
    
    if right_pointer < len(right):
        res += right[right_pointer:]

def  merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr)//2
        left  = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

arr = []
for i in range(100):
    arr.append(random.randint(1, 10))

print(merge_sort(arr))




