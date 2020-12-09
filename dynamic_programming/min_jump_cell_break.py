
import math
def min_jumps(cell, n):

    if cell[0] == "*" or cell[-1] == "*":
        print("No way!")
        return

    primes = []
    max_jumps = [0]*n
    
    


    dp = [10e7 + 9] * n
    if cell[0] == "#":
        dp[0] = 1
        max_jumps[0] = 2
    if cell[1] == "#":
        dp[1] =  1
        max_jumps[1] = 3

    for i in range(2, n):
        # checking for prime
        prime, special = True, False
        for p in primes:
            if p > math.sqrt(i):
                break
            if i % p == 0:
                prime = False
                continue
        # adding the prime numbers
        if prime == True:
            primes.append(i)


        # checking for special 
        if len(primes)/(i + 1) >= r1/r2:
            special = True

    

        # normal case: adding the max jump from theree
        if special == False and cell[i] == "#":
            max_jumps[i] = i + 2
            
        # special case : adding the max junmp from special cell
        if special == True and cell[i] == "#":
            max_jumps[i] = i + len(primes)



        # finding the min number of jumps needed to reach the current cell 
        if cell[i] == "#":  
            j = i - 1
            while j >= 0:
                if cell[j] is "#":
                    if max_jumps[j] + j < i:
                        break
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)

                j -= 1

        
    if dp[-1] == 10e7 + 9:
        print("No way!")
    else:
        print(dp[-1])






r1, r2 = 1, 2
cell = input()
min_jumps(cell, len(cell))