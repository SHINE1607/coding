
from collections import defaultdict
import math
dp = defaultdict(lambda:None)
# dp[(a, b)] = min number of cuts needed to make sqares from rectangle of size a*b
     
def rectangle(a, b):
    dp = defaultdict(lambda: None)


    for height in range(1, a + 1):
        for width in range(1, b + 1):
            if height == width:
                dp[height, width] = 0
                continue
            else:
                ans = 1e9 + 7

                #  taking the minimum of all the horizonal amnd vertical cut combinations

                # horizontal cuts
                for k in range(1, height):
                    ans = min(ans, 1 + dp[k, width]  + dp[height  - k, width])

                # vertical cuts
                for k in range(1, width):
                    ans = min(ans, 1 + dp[height, k] + dp[height, width - k])
     
                dp[height, width] = ans
    print(dp[height, width])

[a, b] = [int(x) for  x in input().split()]
rectangle(min(a, b), max(a,b))
