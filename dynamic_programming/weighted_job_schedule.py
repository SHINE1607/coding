# Given a set of jobs starting time and ending time and progfits made
# FInd max profit that can be made if only one guy is doing the work

from collections import defaultdict


# dp state
# dp[i] =  maxiumum profit that can be made with i jobs 

def max_profit(n, jobs):

    dp = defaultdict(int)
    dp[0] = jobs[0][2]
    ans = 0
    for i in range(1, n):
        
        curr_profit = jobs[i][2]
        start = jobs[i][1]
        end = jobs[i][0]
        dp[i] = curr_profit
        j = 0
        while j < i:
            temp_start = jobs[j][1]
            temp_end = jobs[j][0]
            if temp_end <= start:
                # option we can do the job
                op1 =  curr_profit + dp[j]
                op2 = dp[i]
                
                dp[i] = max(op1, op2)
                ans = max(dp[i], ans)

            j += 1
            
    print(ans)




n = int(input())
jobs = [0] * n
for i in range(n):
    curr = [int(x) for x in input().split()]
    jobs[i] = (curr[1], curr[0], curr[2])

jobs.sort()
max_profit(n, jobs)
 
    