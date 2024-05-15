def is_valid(prob, row, col, num):
    for x in range(9):
        if prob[row][x] == num:
            return False
    for x in range(9):
        if prob[x][col] == num:
            return False
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if prob[i + start_row][j + start_col] == num:
                return False
    return True
def solve_sudoku(prob):
    for i in range(9):
        for j in range(9):
            if prob[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(prob, i, j, num):
                        prob[i][j] = num
                        if solve_sudoku(prob):
                            return True
                        prob[i][j] = 0
                return False
    return True
def print_board(prob):
     for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(prob[i][j])
            else:
                print(str(prob[i][j]) + " ", end="")
prob = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
if solve_sudoku(prob):
    print_board(prob)
    print("Sudoku puzzle solved successfully")
else:
    print("No solution exists")