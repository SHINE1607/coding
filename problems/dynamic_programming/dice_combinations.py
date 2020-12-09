
from collections import defaultdict
dp = defaultdict(int)
    

def combinations(n):
    global dp
    dp[0] = 1
    total = 0
    for i in range(1, n + 1):
        j = 1


        if i < 7:
            for j in range(1, i):
                dp[i] += dp[j]
            dp[i] += 1
        
        if i == 7:
            for j in range(1, 7):
                total += dp[7 - j]
            dp[7] = total
        
        if i > 7:
            dp[i] = int((total + dp[i - 1] - dp[i - 7])%(1e9+7))
            total = dp[i]

    
    print(dp[n])

from collections import Counter


def main(lines):
    lines = lines[1]
    lines = lines.split()

    counter = Counter(lines)
    values  = list[counter.values()]


    values.sort()
    if values[-1] >= 4:
        print("YES")
    else:
        print("NO")