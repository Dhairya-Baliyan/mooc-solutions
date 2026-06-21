#The longest string
def longest(word_string: list):
    long = len(word_string[0])
    string = ""
    for words in word_string:
        if len(words) > long:
            long = len(words)
            string = words
    return string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))


#Number of matching elements
def count_matching_elements(matrix: list, number: int):
    counter = 0
    for element in matrix:
        for num in element:
            if number == num:
                counter += 1
    return counter

if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))


#Go
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
        for element in row:
            if element == 1:
                player1 += 1
            elif element == 2:
                player2 += 1
            else:
                continue
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    board_game = [[1, 2, 0, 1], [0, 1, 2, 1], [2, 2, 0, 1]]
    print(who_won(board_game))
