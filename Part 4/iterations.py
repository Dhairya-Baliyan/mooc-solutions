#Star studded
string = input("Please type in a string:")
for character in string:
    print(character)
    print("*")


#From negative to positive
number = int(input("Please type in a positive integer:"))
for counter in range(-number, number + 1):
    if counter == 0:
        continue
    print(counter)


#List of stars
number = int(input("Please type in a positive integer:"))
for counter in range(-number, number + 1):
    if counter == 0:
        continue
    print(counter)


#Anagrams
def anagrams(text1, text2):
    if sorted(text1) == sorted(text2):
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams("tame", "mate"))


#Palindromes
def palindromes(word: str):
    word1 = word[::-1]
    if word == word1:
        print(f"{word} is a palindrome!")
        return True
    else:
        print("that wasn't a palindrome")
        return False

while True:
    string = input("Please type in a word:")
    value = palindromes(string)
    if value == True:
        break


#The sum of positive numbers
def sum_of_positives(list):
    sum = 0
    for item in list:
        if item > 0:
            sum += item
    return sum

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, -5]
    result = sum_of_positives(my_list)
    print("The result is", result)


#Even numbers
def even_numbers(list):
    new_list = []
    for item in list:
        if item % 2 == 0:
            new_list.append(item)
    return new_list

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)


#The sum of lists
def list_sum(list1, list2):
    sum_list = []
    counter = 0
    while counter < len(list1):
        sum_list.append(list1[counter] + list2[counter])
        counter += 1
    return sum_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))


#Distinct numbers
def distinct_numbers(list):
    new_list = []
    for item in list:
        if item in new_list:
            continue
        new_list.append(item)
    return sorted(new_list)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))


#The length of the longest in the list
def length_of_longest(list):
    best = list[0]
    for item in list:
        if len(item) > len(best):
            best = item
    return len(best)

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(result)


#The shortest in the list
def shortest(list):
    best = list[0]
    for item in list:
        if len(item) < len(best):
            best = item
    return best

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)


#All the longest in the list
def all_the_longest(list):
    best = list[0]
    new_list = []
    counter = 0
    index = 0
    for item in list:
        if len(item) > len(best):
            best = item
            index = counter
        counter += 1
    new_list.append(best)
    for item in range(index + 1, len(list)):
        if len(list[item]) == len(best):
            new_list.append(list[item])
    return new_list
     
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']

#end of the exercises