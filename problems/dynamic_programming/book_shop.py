from collections import defaultdict
import sys
ans = 0
dp = defaultdict(list)

def find_pages(n, x, prices, pages):
    dp = [[0] * (x + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for money in range(x + 1):

            # case when we exactlu
            if money == prices[i - 1]:
                dp[i][money] = max(dp[i - 1][money], pages[i - 1])
                continue
            
            if money < prices[i - 1]:
                dp[i][money] = dp[i - 1][money]
                continue

            if money > prices[i - 1]:
                # taking the rest of money from the last row to remove the case of the adding the book more than one time
                dp[i][money] = max(dp[i - 1][money], pages[i - 1] + dp[i - 1][money - prices[i - 1]])
                continue
    print(dp[-1][-1])
    # print(dp)

[n, x] = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]
pages = [int(x) for x in input().split()]
# data = dict(zip(prices, pages))
find_pages(n, x, prices, pages)

