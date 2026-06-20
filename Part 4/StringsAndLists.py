#Everything reversed
def everything_reversed(list):
    new_list = []
    for item in list:
        new_list.append(item[::-1])
    return new_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)


#Most common character
def most_common_character(string):
    best_character = string[0]
    best_value = string.count(best_character)
    for char in string:
        if string.count(char) > best_value:
            best_character = char
            best_value = string.count(char)
    return best_character

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))


#No vowels allowed
def no_vowels(string):
    new_string = ""
    for char in string:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            continue
        else:
            new_string += char
    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))


#No shouting allowed
def no_shouting(list):
    new_list = []
    for word in list:
        if not word.isupper():
            new_list.append(word)
    return new_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)


#Neighbours in a list
def longest_series_of_neighbours(list):
    new_list = []
    counter = 0
    counter1 = 1
    counter2 = 1
    while counter < len(list) - 1:
        differnce = list[counter] - list[counter + 1]
        if differnce == 1 or differnce == -1:
            counter1 += 1
            if counter1 > counter2:
                counter2 = counter1
        else:
            counter1 = 1
        counter += 1
    return counter2


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))