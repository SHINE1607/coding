from collections import Counter, defaultdict
from bisect import bisect_left
def rooms(n, arr):
    
    end_map = defaultdict(list)
    ans = 0
    member = 0
    for i, el in enumerate(arr):
        el = el[::-1]
        if i == 0:
            member += 1
            end_map[el[1]].append(member)
            ans += 1
            continue
    
        index = bisect_left(list(end_map.keys()), el[0])
        free_gooys = list(end_map.keys())
        
        # found a free guy
        if end_map[free_gooys[index - 1]] != [] and index > 0:
            # found a free guy to see the movue
            end_map[el[1]].append(end_map[free_gooys[index -1]][0])
            # removing the guy from that above bucket
            end_map[list(end_map.keys())[index - 1]] = end_map[free_gooys[index - 1]][1:]
            if end_map[list(end_map.keys())[index - 1]] == []:
                end_map.pop(list(end_map.keys())[index - 1])
            ans += 1

        # time to invite a new momeber 
        if index == 0:
            member += 1
            
            end_map[el[1]].append(member)
            ans += 1
        print(end_map)
    print(ans)
    
    
    
    
    
    
    
    
    # total = 1
    # leaving_time = [clone[0][1]]
    # room_mapping = defaultdict(int)
    # room_mapping[clone[0][1]] = total
    # ans = [(clone[0][0], 1)]

    # for el in clone[1:]:
    #     index = bisect_left(leaving_time, el[0])

    #     if index == 0: # new room alloted
    #         leaving_time.append(el[1])
    #         total += 1
    #         room_mapping[el[1]] = total
    #     else:   # no room to be added 

    #         room_mapping[el[1]] = room_mapping[leaving_time[index - 1]]
    #         leaving_time[index - 1] = el[1]
    #     ans.append((el[0], room_mapping[el[1]]))
    # print(total)
    
    # print(ans)
n = int(input())
times = []
for i in range(n):
    temp = [int(x) for x in input().split()]
    times.append((temp[0], temp[1]))
    # times.append((temp[0], "start"))
    # times.append((temp[1] + 1,  "end"))
    

# print(clone)
rooms(n, times)