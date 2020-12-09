from bisect import insort_right
def slide(n, k, arr):

    if len(list(set(arr))) == 1:
        print(*([arr[0]]*(n-k+1)))
        return
    curr = arr[:k]
    curr.sort()
    if k%2 == 0:
        s = k//2 - 1
        d = 0
    else:
        s = k//2
        d = 1

    l_heap, u_heap = set(curr[:s+1]), set(curr[s+1:]) # to store the upper heap and lower heap
    
    try:
        l_max = max(l_heap)
    except:
        l_max = 0
    try:
        u_min = min(u_heap)
    except:
        u_min = 0
    l, u = s + 1, k - s - 1 # to store thesize of the 2 heaps
    i = k
    prev = curr[s]
    print(prev, end = " ")

    print(l_heap, u_heap )
    while i < n:
        print(l_heap, u_heap,l, u,  "initial")
        # removing the first element of the prev window 
        rem = arr[i - k]
        if rem < prev:
            l_heap.remove(rem)
            l -= 1
            try:
                l_max = max(l_heap)
            except:
                l_max = 0
        elif rem > prev:
            u_heap.remove(rem)
            u -= 1
            try:
                u_min = min(u_heap)
            except:
                u_min = 0
        else:
            if u > l:
                u_heap.remove(rem)
                u -= 1
                try:
                    u_min = min(u_heap)
                except:
                    u_min = 0
            else:
                l_heap.remove(rem)
                l -= 1
                try:
                    l_max = max(l_heap)
                except:
                    l_max = 0
        # making both heaps of same size
        if u - l > d and u_min < prev:
            l_heap.add(u_min)
            l += 1
            u -= 1
            u_heap.remove(u_min)

        elif l - u > d and l_max >= prev:
            u_heap.add(l_max)
            l -= 1
            u += 1
            l_heap.remove(l_max)
        try:
            u_min = min(u_heap)
        except:
            u_min = 0

        try:
            l_max = max(l_heap)
        except:
            l_max = 0
        # print(l_heap, u_heap, "after first equali ")

        # adding the element to the upper heap
        if arr[i] > prev:
            u_heap.add(arr[i]) 
            u += 1
            u_min = min(u_min, arr[i])

        # adding the element to the  lower heap
        else:
            l_heap.add(arr[i])
            l += 1
            l_max = max(l_max, arr[i])
            
        # print(l_heap, u_heap, "afterAdding the new ele")
        # making both heaps of same size
        if u - l > d:
            l_heap.add(u_min)
            l += 1
            u -= 1
            u_heap.remove(u_min)
            

        elif l - u > d:
            u_heap.add(l_max)
            l -= 1
            u += 1
            l_heap.remove(l_max)
        try:
            u_min = min(u_heap)
        except:
            u_min = 0

        try:
            l_max = max(l_heap)
        except:
            l_max = 0
        # print(l_heap, u_heap, "after equalizing final")
        # finding the median
        if u > l:
            prev = u_min
        else:
            prev = l_max
        print(prev, end = " ")
        i += 1


 
 
[n, k] = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
slide(n, k, arr)