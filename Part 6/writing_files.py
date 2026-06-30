#Inscription
name = input("Whom should I sign this to:")
file = input("Where shall I save it:")
with open(file, "w") as new_file:
    new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")


#Diary
while True:
    print("1 - add an entry, 2 - read enteries, 0 - quit")
    choice = int(input("Function:"))
    if choice == 1:
        with open("diary.txt", "a") as diary:
            entry = input("Diary entry:")
            diary.write(entry + "\n")
            print("Diary saved")
    elif choice == 2:
        print("Entries:")
        with open("diary.txt") as diary:
            content = diary.read()
            print(content)
    elif choice == 0:
        print("Bye now!")
        break
    print()


#Filtering the contents of a file
def filter_solutions():
    solution_list = list_of_solutions()
    with open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for solution in solution_list:
            problem = solution[1]
            if '+' in problem:
                operands = problem.split("+")
                operand1 = int(operands[0])
                operand2 = int(operands[1])
                answer = operand1 + operand2
            elif '-' in problem:
                operands = problem.split("-")
                operand1 = int(operands[0])
                operand2 = int(operands[1])
                answer = operand1 - operand2
            if answer == int(solution[2]):
                correct_file.write(";".join(solution) + "\n")
            else:
                incorrect_file.write(";".join(solution) + "\n")
    

def list_of_solutions():
    solutions = []
    with open("solutions.csv") as solution:
        for line in solution:
            parts = line.strip().split(";")
            solutions.append(parts)
    return solutions

if __name__ == "__main__":
    filter_solutions()


#Store personal data
def store_personal_data(person: tuple):
    with open("people.csv", "w") as person_file:
        person_file.write(";".join(str(item) for item in person) + "\n")

if __name__ =="__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))


#Course grading: part 4
def generate_dictionary(filename: str):
    new_dict = {}
    with open(filename) as new_file:
        for line in new_file:
            if ";" in line:
                parts = line.strip().split(";")
            else:
                parts = line.strip().split(":")
            if parts[0] == 'id':
                continue
            new_dict[parts[0]] = parts[1:]
    
    return new_dict

def get_grade(total: int):
    if total <= 14:
        return 0
    elif total >= 15 and total <= 17:
        return 1
    elif total >= 18 and total <= 20:
        return 2
    elif total >= 21 and total <= 23:
        return 3
    elif total >= 24 and total <= 27:
        return 4
    elif total >= 28:
        return 5

def result_txt(name: str, exec_nbr: int, exec_pts: int, exm_pts: int, tot_pts: int, grade: int):
    row = f"{name:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}"
    with open("results.txt", "a") as result_file:
        result_file.write(row + "\n")

student_info = input("Student information:")
exercises_comp = input("Exercises completed:")
exam_point = input("Exam points:")
course_info = input("Course information:")

student_names = generate_dictionary(student_info)

exercises = generate_dictionary(exercises_comp)

exam_points = generate_dictionary(exam_point)

course_name = generate_dictionary(course_info)

course = f"{course_name["name"][0].strip()}, {course_name["study credits"][0].strip()} credits"
print(course)
print("="*len(course))

header = f"{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}"

with open("results.txt", "w") as result_file:
    result_file.write(course + "\n")
    result_file.write("="*len(course) + "\n")
    result_file.write(header + "\n")

results = []

for key, value in student_names.items():
    result_list = []
    name = value[0] + " " + value[1]
    completed = sum(int(x) for x in exercises[key])
    exam_total = sum(int(y) for y in exam_points[key])
    exercise_points = completed // 4
    total = exam_total + exercise_points


#Word search
def find_words(search_term: str):
    matching_words = []

    with open("words.txt") as word_file:
        for word in word_file:
            w = word.strip()
            if "*" in search_term and search_term.strip("*") in w:
                search = search_term.strip("*")
                if search_term[0] == "*":
                    if w.endswith(search):
                        matching_words.append(w)

                elif search_term[len(search_term) - 1] == "*":
                    if w.startswith(search):
                        matching_words.append(w)

            elif "." in search_term:
                if len(search_term) == len(w):
                    match = True
                    for i in range(len(search_term)):
                        if search_term[i] != w[i] and search_term[i] != ".":
                            match = False
                            break
                    if match:           
                        matching_words.append(w)

            elif search_term == w:
                matching_words.append(w)

    return matching_words


if __name__ == "__main__":
    print(find_words("ca."))


#Dictionary stored in a file
dictionary = {}
with open("dictionary.txt") as new_file:
    for line in new_file:
        line = line.strip()
        if ";" in line:
            parts = line.split(";")
            dictionary[parts[0]] = parts[1]
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = int(input("Function:"))
    if choice == 1:
        finnish = input("The word in Finnish:")
        eng = input("The word in English:")
        dictionary[finnish] = eng
        with open("dictionary.txt", "a") as new_file:
            new_file.write(f"{finnish};{eng}" + "\n")
        print("Dictionary entry added")
    elif choice == 2:
        search = input("Seach term:")
        for k, v in dictionary.items():
            if search in k or search in v:
                print(f"{k} - {v}")
    elif choice == 3:
        print("Bye!")
        break