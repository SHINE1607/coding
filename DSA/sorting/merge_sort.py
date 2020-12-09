


import random



def merge(left, right):
    global swaps
    left_pointer = 0
    right_pointer = 0
    res = []
    if left == None:
        return right
    if right  == None:
        return left
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            res.append(left[left_pointer])
            left_pointer += 1
        else:
            swaps += 1
            res.append(right[right_pointer])
            right_pointer += 1

    if left_pointer < len(left):
        res += left[left_pointer:]
        # swaps += (len(left) - left_pointer)
    
    if right_pointer < len(right):
        res += right[right_pointer:]
    return res

def  merge_sort(arr):
    
    global swaps
    
    if len(arr) <= 1:
        return arr
    middle = len(arr)//2
    left  = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

arr = []
for i in range(20):
    arr.append(random.randint(1, 100))

swaps = 0
print(merge_sort(arr))
print("number ofswaps:", swaps)








# def partition(arr):
#     pivot = arr[0]

#     i = 0
#     j = len(arr) - 1
    
#     while True:
        
#         while pivot < arr[i] and i < len(arr):
#             i += 1
#         while pivot > arr[i] and j >= 0:
#             j -= 1

#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break
            




# def quick_sort(arr):
    

    
    