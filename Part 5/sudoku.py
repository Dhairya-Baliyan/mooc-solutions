#Sudoku: check row, column, block, grid
def row_correct(sudoku_row: list, row_no):
    row_sudoku = sudoku_row[row_no]
    seen_elements = []
    for element in row_sudoku:
        if element != 0:
            if element in seen_elements:
                return False
            else:
                seen_elements.append(element)
    return True

def column_correct(sudoku_column: list, column_no: int):
    seen_elements = []
    for row in sudoku_column:
        if row[column_no] != 0:
            if row[column_no] in seen_elements:
                return False
            else:
                seen_elements.append(row[column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    seen_elements = []
    row_index = row_no + 3
    column_index = column_no + 3
    for row in range(row_no, row_index):
        for column in range(column_no, column_index):
            element = sudoku[row][column]
            if element != 0:
                if element in seen_elements:
                    return False
                else:
                    seen_elements.append(element)
    return True

def sudoku_grid_correct(sudoku: list):
    grid_indexes = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    for index in range(0, 9):
        row = row_correct(sudoku, index)
        column = column_correct(sudoku, index)
        grid = block_correct(sudoku, grid_indexes[index])
        if row == True and column == True and grid == True:
            continue
        elif row == False or column == False or grid == False:
            return False
    return True

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_grid_correct(sudoku1))   
    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(row_correct(sudoku1, 0))
    print(row_correct(sudoku1, 1))
    print(column_correct(sudoku1, 0))
    print(column_correct(sudoku1, 1))
    print(block_correct(sudoku1, 0, 0))
    print(block_correct(sudoku1, 1, 2))
    print(sudoku_grid_correct(sudoku2))


