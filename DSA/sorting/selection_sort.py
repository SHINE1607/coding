
# selection sort too have a sorted part and an unsorted part
# but instead of inserting the curr element to the correct pos
# we sleect the least element in the remaining arr and append it  to the rest of the array
import random 



def selection_sort(arr):
    

    pos  = 0
    while True:
        if pos == len(arr):
            break
        # finding the least element index
        min_pos = arr[pos:].index(min(arr[pos:])) + pos
        arr[pos], arr[min_pos] = arr[min_pos], arr[pos]
        pos += 1

    print(arr)

arr = []
for i in range(10):
    arr.append(random.randint(1, 1000))
print(arr)
selection_sort(arr)


