import random
from collections import Counter
arr = []
for i in range(10):
    arr.append(random.randint(1, 100))
binary = []
ones = []
for num in arr:
    binary.append(bin(num)[2:])
    ones.append(binary[-1].count("1"))
data = list(zip(ones, arr))
data.sort()
ans = [x[1] for x in data]
print(ans)
temp = [bin(x)[2:].count("1") for x in ans]
print(temp)