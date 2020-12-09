from collections import defaultdict
from bisect import bisect_right

def movies(n, k, arr):
    if n == k:
        print(n)
        return 
    # mapping of ending time to person watching it 
    end_map = defaultdict(list)
    ans = 0
    member = 0
    for i, el in enumerate(arr):
        
        el = el[::-1]
        if i == 0:
            member += 1
            end_map[el[1]].append(member)
            ans += 1
            print(end_map)
            continue
        # print(end_map, el)
        if list(end_map.keys())[0] > el[0]:
            # new member to be added
            if member + 1 <= k:
                member += 1
                end_map[el[1]].append(member)
                ans += 1
            else:
                # /movie acnnot be watched 
                continue

        else:
            end_map[el[1]].append(end_map[list(end_map.keys())[0]][0])
            end_map[list(end_map.keys())[0]].pop(0)
            if end_map[list(end_map.keys())[0]] == []:
                end_map.pop(list(end_map.keys())[0])
            ans += 1
        print(end_map)
    print(ans)



[n, k] = [int(x) for x in input().split()]
arr = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    arr.append((temp[1], temp[0]))

arr.sort()
print(arr)
movies(n, k, arr)