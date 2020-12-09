# code to find the cnumber of the special subatring in the given  string 


from collections import Counter 
from itertools import combinations
from math import factorial

def substrCount(n, s):
    special = 0
    comb = get_sub_strings(s)
    print(comb)
    for curr in comb:
        
        if(len(curr)%2 == 0):
            if(len(curr) == 2):
                length = 1
            else:
                length = int(len(curr) / 2) - 1

            for j in range(0, length):
                
                if(curr[j] == curr[len(curr) - j - 1]):
                    pass
                else:
                    flag = 0
                    break
                if(flag == 1):
                    special += 1
        else:
            if(len(curr) == 1):
                special += 1
                pass
            flag = 1

            for j in range(0, int(len(curr)/ 2)):
                if(curr[j] == curr[len(curr) - j - 1]):
                    pass
                else:
                    flag = 0
                    break
                if(flag == 1):
                    special += 1
    print(special)

def get_sub_strings(string):
    length = len(string) + 1
    return [string[x:y] for x, y in combinations(range(length), r=2)]



print(substrCount(4, "abcbaba"))







