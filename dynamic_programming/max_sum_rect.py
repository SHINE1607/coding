from collections import defaultdict


# its kind of the basic method we do in max_sum _subarray problem for each top rows moving from 0 to last row, 
# we select lst row moving from the top to bottom row
# we sum columnwise of each top to bottom submatrix  and stored in curr_sub_matrix_sum
# we find the max of that curr_sub_matrix_sum using kadanes alagorithm

# for example if our top row is 2 and bottom row is 4
# and oput curr_sub_matrix_sum is [-18, 13, 4, -3, -4], so using kadanes we get max is 17
# and dis will our curr max and if it if larger than out largest we update the largest 
# and th largest occur in in rect (2, 2) to (4, 3)  cool right!

def find_max(matrix):
    r = len(matrix)
    c = len(matrix[0])
    curr_sub_matrix_sum  = [0]*c
    largest = 0
    for t in range(r):
        curr_sub_matrix_sum = matrix[t]
        largest = kadanes(curr_sub_matrix_sum)
        for b in range(t+1, r):
            curr_sub_matrix_sum = [(curr_sub_matrix_sum[i] + matrix[b][i]) for i in range(c)]
            
            curr_max = kadanes(curr_sub_matrix_sum)
            largest = max(largest, curr_max)
        largest = max(largest, curr_max)
    print(largest)



def kadanes(arr):
    curr_sum = arr[0]
    ans = arr[0]


    for i in range(1, len(arr)):
        op1 = arr[i]
        op2 = curr_sum + arr[i]

        curr_sum = max(op1, op2)
        ans = max(ans, curr_sum)

    return max(ans, curr_sum)
    

[r, c] = [int(x) for x in input().split()]
matrix = []
for i in range(r):
    matrix.append([int(x) for x in input().split()]) 
find_max(matrix)