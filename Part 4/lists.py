#Change value of item
list = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index:"))
    if index == -1:
        break;
    new_value = int(input("New Value:"))
    list[index] = new_value
    print(list)


#Add item to the list
list = []
items = int(input("How many items:"))
counter = 1
while counter <= items:
    number = int(input(f"Item {counter}"))
    list.append(number)
    counter += 1
print(list)


#addition and removal
list = []
print(f"The list is now {list}")
counter = 1
while True:
    option = input("a(d)d, (r)emove or e(x)it:")
    if option == "d":
        list.append(counter)
        counter += 1
    elif option == "r":
        list.remove(counter-1)
        counter -= 1
    elif option == "x":
        print("Bye!")
        break;
    print(f"The list is now {list}")


#Same word twice
list = []
counter = 0
while True:
    word = input("Word:")
    list.append(word)
    counter += 1
    list.pop(counter - 1)
    if word in list:
        print(f"You typed in {counter - 1} different words")
        break;
    else:
        list.append(word)


#List twice
list = []
while True:
    item = int(input("New item:"))
    if item == 0:
        print("Bye!")
        break;
    list.append(item)
    print(f"The list now: {list}")
    print(f"The list in order: {sorted(list)}")


#Length of list
def length(list):
    return len(list)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = length(my_list)
    print(result)


#Mean
def mean(list):
    list_sum  = sum(list)
    return list_sum/len(list)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)


#Range of list
def range_of_list(list):
    largest = max(list)
    smallest = min(list)
    return largest - smallest

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)
