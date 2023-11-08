import time
start_time = time.time()

sudoku = [[6, 0, 5, 0, 0, 0, 0, 9, 0],
         [0, 0, 0, 0, 0, 7, 0, 2, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 9, 0, 8, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 5, 0, 0],
         [4, 0, 0, 0, 0, 0, 1, 0, 6],
         [0, 8, 0, 0, 0, 3, 0, 0, 0],
         [0, 0, 0, 5, 1, 0, 0, 0, 0],
         [0, 2, 0, 0, 0, 0, 0, 0, 0]]

def check_for_number_row(row, grid, number):
    for i in range(9):
        if grid[row][i] == number:
            return False
    return True

def check_for_number_column(column, grid, number):
    for i in range(9):
        if grid[i][column] == number:
            return False
    return True

def check_for_number_zone(row, column, grid, number):
    row_zone = (row // 3) * 3
    column_zone = (column // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[i + row_zone][j + column_zone] == number:
                return False
    return True

def solve():
    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                for number in range(1, 10):
                    if (check_for_number_row(row, sudoku, number) and
                        check_for_number_column(column, sudoku, number) and
                        check_for_number_zone(row, column, sudoku, number)):
                        sudoku[row][column] = number  
                        if solve():
                            return True
                        sudoku[row][column] = 0
                return
    for row in sudoku:
        print(*row) # = print(*row,sep=' ')

    print('Solution found in', round((time.time() - start_time), 3), 'ms')

solve()
