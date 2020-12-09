import sympy 

for i in range(3, 1000):
    res = sympy.isprime(i)
    if i > 3 and (i**2 - 1)%24 == 0 and i%5 != 0 and i%7!= 0:
        res2 = True
    else:
        res2 = False
    if res != res2:
        print(i, res, res2)