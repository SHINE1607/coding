# given a matrix of 1 and 0, find the largest recatngle haviong only 1

def max_size(matrix):
    r = len(matrix)
    c = len(matrix[0])
    dp_arr = matrix[0].copy()
    print(dp_arr)
    non_zero = []
    area = 0

    for i in dp_arr:
        if i == 0:
            if len(non_zero) != 0:
                area = max(area, min(non_zero) * len(non_zero))
                non_zero = []
        else:
            non_zero.append(i)
            
        
    if len(non_zero) != 0:
        area = max(area, min(non_zero) * len(non_zero))
            

    for i in range(1, r):
        for j in range(c):
            if matrix[i][j] == 0:
                dp_arr[j] = 0
                if len(non_zero) != 0:
                    area = max(area, min(non_zero) * len(non_zero))
                    non_zero = []
                
            else:
                dp_arr[j] += 1
                non_zero.append(dp_arr[j])
                

        

    if len(non_zero) != 0:
        area = max(area, min(non_zero) * len(non_zero))
    print(area)

import random
[rows, cols] = [int(x) for x in input().split()]
# matrix = []
# for i in range(rows):
#     matrix.append([int(x) for x in input().split()])
matrix  = [[0]*cols for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = random.randint(0, 1)
    print(matrix[i])
max_size(matrix)
    