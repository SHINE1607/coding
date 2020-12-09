ans  = 0


def queens_rec(q_no, taken, taken_clone,  diff_arr, main_board):
    global ans
    # print(taken_clone)
    if q_no == 2:
        ans += 1
    
    # print(taken , taken_clone)
            
    
    for i in range(8):  # loop for the chess board
        for j in range(8):
            if main_board[i][j] !=  ".":
                continue
            else:
                if i in taken_clone[0]:
                    break
                if j in taken_clone[1]:
                    
                    continue
                diff = i - j
                if diff in diff_arr or -1*diff in diff_arr:
                   
                    continue
                else:
                    print(i, j)
                    temp1 = taken_clone.copy()
                    temp1[0].append(i)
                    temp1[1].append(j)
                    main_board[i][j] = "#"
                    # if i == 1 and j==3 and q_no == 1:
                    #     print("shit")
                    #     print(temp2)
                    queens_rec(q_no + 1, taken + [[i, j]], temp1, diff_arr + [i - j], main_board)
                    temp1[0].append(j)
                    temp1[1].append(i)
                    if q_no == 1:
                        print(temp1)
                    queens_rec(q_no + 1, taken + [[j, i]], temp1, diff_arr + [j - i], main_board)
                    main_board[i][j] = "."

# board = []
# for i in range(8):
# board.append(list(input()))
fixed_pos = [[], []]
# print(board)
board = [['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '*', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '*', '*', '.'], ['.', '.', 
'.', '*', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']]
main_board = [["." for i in range(8)] for j in range(8)]

main_board[0][0] = "#"
queens_rec(1, [[0, 0]], [[0], [0]], [0], main_board)


# fixing the first queeen
# for i in range(8):
#     for j in range(8):
#         main_board = [["." for i in range(8)] for j in range(8)]
#         main_board[i][j] = "#"
#         queens_rec(1, [[i, j]], [[i], [j]], [i - j], main_board)
#         main_board = [["." for i in range(8)] for j in range(8)]
# print(ans)
print(ans)

