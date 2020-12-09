from collections import Counter


s = [2, 4, 6, 8, 10]
a = 25

left = 0
right = len(s) - 1

ans = 0
while left < right:
    if s[left] * s[right] < a:
        ans += (right - left)*2 + 1
        left += 1
        continue
    
    if s[left] *  s[right] >= a:
        right = right - 1 
        continue  

print(ans)
    




        
