
def max_rewards(n, tasks):
    
    ans = 0
    time = 0
    for i in range(n):
        time += tasks[i][0]
        ans += (tasks[i][1] - time)
    print(ans)
    
        



n = int(input())
tasks = []
for i in range(n):
    temp = input().split()
    tasks.append((int(temp[0]), int(temp[1])))
tasks.sort()
max_rewards(n, tasks)

