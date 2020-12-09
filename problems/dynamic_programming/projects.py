from collections import defaultdict

# dp[i] is the maximum rewrd that can be achieved until the ith job 
def max_reward(n, projects, times):
    dp = defaultdict(int)
    ans = 0
    dp[0] = projects[0]
    for i in range(1, n):
        curr_job = times[i][::-1]
        dp[i] = projects[i]
        j = 0
        while j < i:
            
            job = times[j][::-1]
            if curr_job[0] > job[1]:
                dp[i]  = max(projects[i] + dp[j], dp[i])
                ans = max(ans, dp[i])
                
            j += 1


    print(ans)

n = int(input())
projects = defaultdict(list)
times = []
for i in range(n):
    curr = [int(x) for x in input().split()]
    times.append((curr[1], curr[0], curr[2])) 


times.sort()
for i in range(n):
    projects[i] = times[i][2]
    times[i]  = tuple([times[i][1], times[i][0]])


max_reward(n, projects, times)