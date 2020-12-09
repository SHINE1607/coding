
diff = 0
final_ans = 0
def division_rec(arr, i,  s, target):
    
    global diff 
    global final_ans
    if i == -1:
        return
    if abs(s - target) < abs(diff):
        
        final_ans = s
        diff = s - target
        # print(s, diff, i, "check")
    return division_rec(arr, i - 1, s, target) or division_rec(arr, i - 1, s - arr[i], target)

def apple_division(n, arr):
    s = sum(arr)
    target = s/2
    global diff
    global final_ans
    
    diff = abs(s - min(arr))
    division_rec(arr, n - 1, s, target)
    left_sum = final_ans
    right_sum =  s - final_ans
    print(abs(right_sum- left_sum))







n = int(input())
weights = [int(x) for x in input().split()]
apple_division(n, weights)