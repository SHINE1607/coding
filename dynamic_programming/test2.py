
arr = [5, 1, 0, 1, 2, 2]


from collections import Counter
counter = Counter(arr)

q = [1, 5, 3]
values1 = list(counter.values())
values1.sort()
for i in range(len(q)):
    to_delete = q[i]
    i = 0
    values = values1.copy()
    while True:
        if values == []:
            break

        if values[0] < to_delete:
            to_delete -= values[0]
            values = values[1:]
            continue
        if values[0] == to_delete:
            to_delete = 0
            values = values[1:]
            break
        if values[0] > to_delete:
            values[i] = values[i] - to_delete
            break
    print(len(values))
            
