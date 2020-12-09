#  insertion sort concept is simple as inserting a new elemenst to the already sorted array
# we iterate through the gievn array and place them in the crrct position
# so theer woll be a sorted part and unosrted part iterativel  we insert element from unsorted array to the sorted one
# time complexity O(n^2) for the worst case scenario
# ########################################################
# idea is to insert the new eleet in the sorted array 
# ########################################################


# the difference between insrtion sort and selection sort is that, in insertion sort, we inserting the curr arr element ans inerting into the sorted part
from bisect import insort_right

import time
def insertion_sort(arr):

    


    for i in range(1, len(arr)):
        sorted = arr[:i]

        curr = arr[i]
        for j in range(len(sorted)):
            if curr < sorted[j]:
                sorted = sorted[:j] + [curr] + sorted[j:]
                print(sorted)
                break
        arr = sorted + arr[i + 1:]
    print(arr)




        
start = time.time()
arr = [int(x) for x in input().split()]
end = time.time()
insertion_sort(arr)
print ("time: ", end - start)
