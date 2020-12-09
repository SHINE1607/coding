


def permutations(n):
    
    if n < 4 and n > 1:
        print("NO SOLUTION")
        return 
    if n == 4:
        print("2 4 1 3")
        return
    if n == 1:
        print(1)
        return


    even_index = 0
    odd_index = 0
    arr = [0] * n
    if n %2 == 1:
        even_index = n//2 + 1
    else:
        even_index = n//2
    for i in range(n):
        if (i + 1)%2== 1:
            arr[odd_index] = str(i + 1)
            odd_index  += 1 
        else:
            arr[even_index] = str(i + 1)
            even_index += 1
    print(" ".join(arr))



n = int(input())
permutations(n)