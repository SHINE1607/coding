from collections import defaultdict
def customers(mapping):
    start = list(mapping.keys())
    start.sort()
    ans = 0
    curr = 0
    for i in  start:
        if mapping[i] == "start":
            curr += 1
            if curr > ans:
                ans = curr
        else:
            curr -= 1
    print(ans)

    


n = int(input())
mapping = defaultdict(str)
for i in range(n):
    temp = [int(x) for x in input().split()]
    mapping[temp[0]] = "start"
    mapping[temp[1]] = "end"
# customer(n, mapping)

customers(mapping)
