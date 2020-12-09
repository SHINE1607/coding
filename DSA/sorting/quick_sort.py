import random




def partition(arr, low, high):
    
    pivot = arr[low]

    i = low
    j = high
    while(i < j):
        while i <= high:
            if arr[i] > pivot:
                break
            else:
                i += 1
        while j >= low:
            if arr[j] <= pivot:
                break
            else:
                j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
    
        

def quick_sort(arr, low, high):
    if low < high:
        # by calling partition the first element is kept at the correct position
        index = partition(arr, low, high)

        quick_sort(arr, low, index - 1)
        quick_sort(arr, index + 1, high)
    
    
arr = []
for i in range(20):
    arr.append(random.randint(1, 100))
print(arr)
# arr = [int(x) for x in "20 3 11 5 7 2".split()]
quick_sort(arr, 0, len(arr) - 1)
print(arr)