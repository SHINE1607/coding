from collections import defaultdict
import sys 
sys.setrecursionlimit(50000)
dp = defaultdict(int)
flag = False


def remove(n, k):
    global dp
    curr, k = n, 0

    while curr >= 0:
        for i in sorted(str(curr))[::-1]:
            if curr - int(i) < 0:
                continue 
            if curr - int(i) == 0:
                print(k + 1)
                return
            else:
                k += 1
                curr = curr - int(i)
                break
    print(k)
                
            



    # global dp, flag

    # if n == 0:
    #     flag = True
    #     print(k)
    #     return
    # for i in sorted(str(n))[::-1]:
    #     if dp[n - int(i)] == False and flag == False:
    #         dp[n - int(i)] = True
    #         remove(n - int(i), k + 1)
    #         if flag == True:
    #             break
    


n = int(input())
remove(n, 0)