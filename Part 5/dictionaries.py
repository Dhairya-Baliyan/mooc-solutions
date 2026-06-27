#Times ten
def times_ten(start_index: int, end_index: int):
    dictionary = {}
    for index in range(start_index, end_index + 1):
        dictionary[index] = index * 10
    return dictionary

if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d)


#Factorials
def factorials(n: int):
    factorial = {}
    for index in range(1, n+1):
        f = 1
        for number in range(1, index + 1):
            f *= number
        factorial[index] = f
    return factorial

if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])


#Histogram
def histogram(string: str):
    histogram = {}
    for character in string:
        if character in histogram:
            histogram[character] += "*"
        else:
            histogram[character] = "*"
    for key, value in histogram.items():
        print(f"{key} {value}")

if __name__ == "__main__":
    histogram("statistically")


#Phonebook:Version 1 and 2
def histogram(string: str):
    histogram = {}
    for character in string:
        if character in histogram:
            histogram[character] += "*"
        else:
            histogram[character] = "*"
    for key, value in histogram.items():
        print(f"{key} {value}")

if __name__ == "__main__":
    histogram("statistically")


phone_book = {}
while True:
    choice = int(input("1 search, 2 add, 3 quit:"))
    if choice == 1:
        search_name = input("name:")
        if search_name in phone_book:
            for key, value in phone_book.items():
                if key == search_name:
                    for num in value:
                        print(num)
        else:
            print("no number")
    elif choice == 2:
        name = input("name:")
        number = input("number:")
        if name not in phone_book:
            phone_book[name] = []
        phone_book[name].append(number)
        print("ok!")
    elif choice == 3:
        print("quitting...")
        break


#Invert a dictionary
def invert(dictionary: dict):
    inverted = {}
    for key, value in dictionary.items():
        inverted[value] = key
    dictionary.clear()
    dictionary.update(inverted)

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)


#Numbers spelled out
def dict_of_numbers():
    number_dict = {}
    dictionary1 = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    dictionary2 = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    for number in range(100):
        if number < 20:
            number_dict[number] = dictionary1[number]
        elif number % 10 == 0:
            number_dict[number] = dictionary2[number]
        else:
            division = number // 10
            remainder = number % 10
            number_dict[number] = f"{dictionary2[division * 10]}-{dictionary1[remainder]}"
    return number_dict

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])


#Movies database
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    movie_dict = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }
    database.append(movie_dict)

if __name__ == "__main__":
    database = []
    add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
    add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
    print(database)



#Find movies
def find_movies(database: list, search_term: str):
    new_database = []
    for movie in database:
        movie_name = movie["name"].lower()
        if search_term.lower() in movie_name:
            new_database.append(movie)
        else:
            continue
    return new_database

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]
    my_movies = find_movies(database, "python")
    print(my_movies)