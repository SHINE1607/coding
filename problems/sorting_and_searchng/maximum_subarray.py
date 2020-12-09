

def  find_sum(n, arr):
    curr, ans = 0, 0 
    neg = None
    for i in arr:
        if  i < 0:
            if neg == None:
                neg = i
            elif i > neg:
                neg = i
        curr += i
        if curr < 0:
            curr = 0   # maling the curr sum = 0 cuz 0 is better than negatiue
        if ans < curr:
            ans = curr
    if ans == 0:
        ans = neg
        print(ans)
    else:
        print(ans)
    



n = int(input())
arr = [int(x) for x in input().split()]
find_sum(n, arr)