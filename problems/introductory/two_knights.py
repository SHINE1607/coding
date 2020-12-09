def  two_knights(k):
    a1 = k * k
    a2 = a1*(a1 - 1)/2

    if k > 2:
        a2 -= 4*(k-1)*(k-2)
    print(int(a2))


    


k = int(input())
for i in range(1, k+1):
    two_knights(i)