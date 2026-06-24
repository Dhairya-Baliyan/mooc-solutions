#Items multiplied by 2
def double_items(numbers: list):
    doubled_list = []
    for number in numbers:
        doubled_list.append(number*2)
    return doubled_list

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)


#Remove the smallest
def remove_smallest(numbers: list):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    numbers.remove(smallest)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)


#Sudoku:print out the grid
def print_sudoku(sudoku: list):
    counter = 0
    for row in sudoku:
        space = 0
        for element in row:
            if element == 0:
                print("_",end="")
            else:
                print(element,end="")
            if space == 2 or space == 5:
                print(" ",end="")
            print(" ",end="")
            space += 1
        if counter == 2 or counter == 5:
            print()
        print()
        counter += 1

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)


#Sudoku:add number to a copy of the grid
def print_sudoku(sudoku: list):
    counter = 0
    for row in sudoku:
        space = 0
        for element in row:
            if element == 0:
                print("_",end="")
            else:
                print(element,end="")
            if space == 2 or space == 5:
                print(" ",end="")
            print(" ",end="")
            space += 1
        if counter == 2 or counter == 5:
            print()
        print()
        counter += 1

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = []
    for row in sudoku:
        sudoku_copy.append(row[:])
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)


#Tic-Tac-Toe
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x > 2 or y > 2 or x < 0 or y < 0:
        return False
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False

if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)


#Transpose a matrix
def transpose(matrix: list):
    n = len(matrix)
    print(n)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Orignal Matrix:")
    print(matrix)
    transpose(matrix)
    print("Transpose Matrix:")
    print(matrix)