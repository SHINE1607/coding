def binary_search_rec(arr, n, left, right):
    if left > right:
        print("the alement cant be found")
        return
    middle = (left + right) // 2 
    if arr[middle] == n:
        print("the element is found at {}".format(middle))
        return 
    elif n <= arr[middle]:
        
        binary_search_rec(arr, n, left, middle)
    else:
        binary_search_rec(arr, n , middle + 1, right)


arr = [1, 4, 5, 2, 3]
def binary_search(arr, find):
    arr.sort()
    print(arr)
    
    binary_search_rec(arr, find, 0, len(arr) - 1)

binary_search(arr,4)


[['b', 'd'], ['a', 'c'], ['a', 'b'], ['c'], ['b', 'd'], ['d'], ['a', 'c'], ['']]
[['a', 'b'], ['c', 'd'], ['b', 'd'], ['a'], ['b', 'c'], ['d'], ['a', 'c'], ['']]
 
