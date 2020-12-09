def two_sets(n):
    if (n*(n+1)/2) % 2 == 1:
        print("NO")
        return 
    print("YES")
    left_arr = ["1", "2"]
    right_arr = ["3"]
    for i in range(1, int((n-3)/4 + 1)):
        curr = i * 4
        left_arr += [str(curr), str(curr + 3)]
        right_arr += [str(curr + 1), str(curr + 2)]
    print(len(left_arr))
    print(" ".join(left_arr))
    print(len(right_arr))
    print(" ".join(right_arr))
        
        







n =  int(input())
two_sets(n)