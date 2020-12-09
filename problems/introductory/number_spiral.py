def number_spiral(ind1, ind2):
    diagnol = 0
    
    if ind1 == ind2:
        print(ind2*(ind2-1) + 1)
        return
    if ind1 < ind2:
        diagnol = ind2*(ind2-1) + 1
        if ind2%2 == 0:
            print(diagnol - (ind2 - ind1))
        else:
            print(diagnol + (ind2 - ind1))
    elif  ind1 >  ind2:
        diagnol = ind1*(ind1-1) + 1
        if ind1%2 == 0:
            print(diagnol + (ind1 - ind2))
        else:
            print(diagnol - (ind1 - ind2))


n = int(input())
for i in range(n):
    index_arr = input().split()
    
    ind1 = int(index_arr[0])
    ind2 = int(index_arr[1])
    number_spiral(ind1, ind2)
