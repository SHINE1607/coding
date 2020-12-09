def rotation(matrix):
    res_matrix  = [[None]*len(matrix[0]) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res_matrix[j][len(matrix[0]) - 1 - i] =  matrix[i][j]



    return res_matrix 


matrix = [[1, 2, 3, 4], [4, 5, 6, 1], [7, 8, 9, 6]]
res_matrix =  rotation(matrix)
for i in matrix:
    print(i)
for i in res_matrix:
    print(i)