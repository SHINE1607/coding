
arr = [10, 2, 3, 6, 5, 1, 2, 4]

def counting_sort(arr, d):
    counter = [0]*(d+1)
    global values
    values = arr.copy()
    arr_2 = arr.copy()
    #updating the counter array
    for i in arr:
        counter[i] += 1
    
   
    #taking cumulative sum of coynter array
    for j in range(len(counter)):
        if(j > 0):
            counter[j] = counter[j] + counter[j - 1]
    #shifting the counter to right
    #shifting is done to make the cumulative counter values within range
    counter = [counter[-1]] + counter[0 : len(counter) - 1]
    
    for i in arr:
        print(i)
        arr_2[counter[i]] = i
        counter[i] += 1

    return(arr_2)
print(counting_sort(arr, 10))
        
        
    
    



