# possibly the themost brute force approoach we can think of
# steps
# > we select the last element as i 
# > we iterate j from to i - 1
# > replace the largest element with ith position
# like that imoves from n -1 to 1


# 20 3 11 5 7 2
# first iteration for i
# j           i
# 20 3 11 5 7 2

#    j        i
# 3 20 11 5 7 2

#       j     i
# 3 11 20 5 7 2

#         j   i
# 3 11 5 20 7 2

#          j  i
# 3 11 5 7 20 2

#            ji
# 3 11 5 7 2 20

# time complexity: O(n^2)


import time
def bubble_sort(arr):
    
    n = len(arr)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    print(arr)
    

arr = [int(x) for x in input().split()]
arr1 = arr.copy()
start = time.time()
bubble_sort(arr1)
end   = time.time()
print("time for bubble sort: ", end - start)


def bubble_sort_linear(arr):
    start = time.time()
    n = len(arr)
    i = n - 1
    t = 0
    while i > 0:
        print(arr, i)
        for  j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr [j]
                t = j
        i = t
    print(arr)

start = time.time()
bubble_sort_linear(arr)
end   = time.time()
print("time for bubble sort linear: ", float(end - start))