#Largest Number
def largest():
    with open("numbers.txt") as new_file:
        largest = 0
        for number in new_file:
            if number > str(largest):
                largest = int(number)
    return largest

if __name__ == "__main__":
    print(largest())
            

#Fruit Market
def read_fruits():
    with open("fruits.csv") as new_file:
        fruit_dict = {}
        for line in new_file:
            words = line.split(";")
            fruit_name = words[0]
            fruit_price = float(words[1])
            fruit_dict[fruit_name] = fruit_price
        return fruit_dict

if __name__ == "__main__":
    print(read_fruits())


#Matrix
def matrix_sum():
    with open("matrix.txt") as new_file:
        matrix = []
        for line in new_file:
            row = []
            parts = line.strip().split(",")
            for element in parts:
                row.append(int(element))
            matrix.append(row)
        sum = 0
        for row in matrix:
            for column in row:
                sum += column
        return sum

def matrix_max():
    with open("matrix.txt") as new_file:
        matrix = []
        for line in new_file:
            row = []
            parts = line.strip().split(",")
            for element in parts:
                row.append(int(element))
            matrix.append(row)
        greatest = matrix[0][0]
        for row in matrix:
            largest = max(row)
            if largest > greatest:
                greatest = largest
    return greatest

def row_sums():
    with open("matrix.txt") as new_file:
        matrix = []
        for line in new_file:
            row = []
            parts = line.strip().split(",")
            for element in parts:
                row.append(int(element))
            matrix.append(row)
        sum_list = []
        for row in matrix:
            sum_rows = sum(row)
            sum_list.append(sum_rows)
    return sum_list

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())


#Course Grading: Part 1, 2 and 3
student_info = input("Student Information:")
exercises_comp = input("Exercises Completed:")
student_names = {}

with open(student_info) as student_file:
    for line in student_file:
        parts = line.strip().split(";")
        if parts[0] == 'id':
            continue
        student_names[parts[0]] = parts[1:]

exercises = {}

with open(exercises_comp) as exercises_file:
    for line in exercises_file:
        parts = line.strip().split(";")
        if parts[0] == 'id':
            continue
        exercises[parts[0]] = parts[1:]


for key, value in student_names.items():
    name = value[0] + " " + value[1]
    total = sum(int(x) for x in exercises[key])
    print(f"{name} {total}")

#Part 2
student_info = input("Student information:")
exercises_comp = input("Exercises completed:")
exam_point = input("Exam points:")

student_names = {}

with open(student_info) as student_file:
    for line in student_file:
        parts = line.strip().split(";")
        if parts[0] == 'id':
            continue
        student_names[parts[0]] = parts[1:]

exercises = {}

with open(exercises_comp) as exercises_file:
    for line in exercises_file:
        parts = line.strip().split(";")
        if parts[0] == 'id':
            continue
        exercises[parts[0]] = parts[1:]

exam_points = {}
with open(exam_point) as exam_file:
    for line in exam_file:
        parts = line.strip().split(";")
        if parts[0] == 'id':
            continue
        exam_points[parts[0]] = parts[1:]


for key, value in student_names.items():
    name = value[0] + " " + value[1]
    exam_total = sum(int(y) for y in exam_points[key])
    exercise_points = sum(int(x) for x in exercises[key]) // 4
    total = exam_total + exercise_points
    if total <= 14:
        grade = 0
    elif total >= 15 and total <= 17:
        grade = 1
    elif total >= 18 and total <= 20:
        grade = 2
    elif total >= 21 and total <= 23:
        grade = 3
    elif total >= 24 and total <= 27:
        grade = 4
    elif total >= 28:
        grade = 5
    print(f"{name} {grade}")

#Part 3
student_info = input("Student information:")
exercises_comp = input("Exercises completed:")
exam_point = input("Exam points:")

student_names = {}

with open(student_info) as student_file:
    for line in student_file:
        parts = line.strip().split(";")
        if parts[0] == 'id':
            continue
        student_names[parts[0]] = parts[1:]

exercises = {}

with open(exercises_comp) as exercises_file:
    for line in exercises_file:
        parts = line.strip().split(";")
        if parts[0] == 'id':
            continue
        exercises[parts[0]] = parts[1:]

exam_points = {}
with open(exam_point) as exam_file:
    for line in exam_file:
        parts = line.strip().split(";")
        if parts[0] == 'id':
            continue
        exam_points[parts[0]] = parts[1:]

print(f'{"name":<30}',end="")
print(f'{"exec_nbr":<10}',end="")
print(f'{"exec_pts.":<10}',end="")
print(f'{"exm_pts.":<10}',end="")
print(f'{"tot_pts.":<10}',end="")
print(f'{"grade":<10}')
for key, value in student_names.items():
    name = value[0] + " " + value[1]
    completed = sum(int(x) for x in exercises[key])
    exam_total = sum(int(y) for y in exam_points[key])
    exercise_points = completed // 4
    total = exam_total + exercise_points
    if total <= 14:
        grade = 0
    elif total >= 15 and total <= 17:
        grade = 1
    elif total >= 18 and total <= 20:
        grade = 2
    elif total >= 21 and total <= 23:
        grade = 3
    elif total >= 24 and total <= 27:
        grade = 4
    elif total >= 28:
        grade = 5
    print(f"{name:<30}",end="")
    print(f"{completed:<10}",end="")
    print(f"{exercise_points:<10}",end="")
    print(f"{exam_total:<10}",end="")
    print(f"{total:<10}",end="")
    print(f"{grade:<10}")


#Spell Checker
text = input("Write text:")
text_list = text.split(" ")
word_list = []
with open("wordlist.txt") as words_file:
    for line in words_file:
        word = line.strip()
        word_list.append(word)
counter = 0   
for word in text_list:
    if word.lower() in word_list:
        print(word + " ",end="")
    else:
        print("*" + word + "*",end="")


#Recipie Search
def search_by_name(filename: str, word: str):
    recipie_name = []
    list_of_recipie = list_of_recipies(filename)
    for recipie in list_of_recipie:
        if word.lower() in recipie[0].lower():
            recipie_name.append(recipie[0])

    return recipie_name

def list_of_recipies(filename: str):
    recipie_list = []
    recipie = []
    with open(filename) as recipie_file:
        for line in recipie_file:
            name = line.strip()
            if name == "":
                recipie_list.append(recipie)
                recipie = []
            else:
                recipie.append(name)
        recipie_list.append(recipie)
    return recipie_list

def search_by_time(filename: str, prep_time: int):
    recipie_time = []
    list_of_recipie = list_of_recipies(filename)

    for recipies in list_of_recipie:
        if int(recipies[1]) <= prep_time:
            sentence =f"{recipies[0]}, preparation time {recipies[1]} min"
            recipie_time.append(sentence)

    return recipie_time

def search_by_ingredient(filename: str, ingredient: str):
    ingredient_list = []
    list_of_recipie = list_of_recipies(filename)

    for recipies in list_of_recipie:
        if ingredient in recipies:
            sentence = f"{recipies[0]}, preparation time {recipies[1]} min"
            ingredient_list.append(sentence)
    return ingredient_list

if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)

    for recipe in found_recipes:
        print(recipe)
    
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
        print(recipe)


#City bikes
import math

def get_station_data(filename: str):
    station_data = {}
    station = list_of_stations(filename)
    for data in station:
        station_data[data[3]] = (float(data[0]), float(data[1]))
    return station_data


def list_of_stations(filename: str):
    stations_list = []
    with open(filename) as station_file:
        for line in station_file:
            data = line.strip().split(";")
            if data[0] == "Longitude":
                continue
            stations_list.append(data)
    return stations_list

def distance(stations: dict, station1: str, station2: str):
    coordinates_1 = stations[station1]
    coordinates_2 = stations[station2]
    x_km = (coordinates_1[0] - coordinates_2[0]) * 55.26
    y_km = (coordinates_1[1] - coordinates_2[1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    max_distance = 0
    station1 = ""
    station2 = ""
    for key1 in stations.keys():
       for key2 in stations.keys():
            d = distance(stations, key1, key2)
            if d > max_distance:
                station1 = key1
                station2 = key2
                max_distance = d
    return (station1, station2, max_distance)

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)



