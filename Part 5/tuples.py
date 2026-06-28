#Create a tuple
def create_tuple(x: int, y: int, z: int):
    sum = x + y + z
    if x > y:
        if x > z:
            greatest = x
        else:
            greatest = z
    elif y > x:
        if y > z:
            greatest = y
        else:
            greatest = z
    
    if x < y:
        if x < z:
            smallest = x
        else:
            smallest = z
    elif y < x:
        if y < z:
            smallest = y
        else:
            smallest = z
    
    numbers = (smallest, greatest, sum)
    return numbers

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
    

#The oldest person
def oldest_person(people: list):
    oldest = people[0][1]
    name = people[0][0]
    for peep in people:
        if peep[1] < oldest:
            oldest = peep[1]
            name = peep[0]
    return name

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))


#Older people
def older_people(people: list, year: int):
    name = []
    for peep in people:
        if peep[1] < year:
            name.append(peep[0])
    
    return name

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    older = older_people(people, 1979)
    print(older)


#Student Database
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = {}

def add_course(students: dict, name: str, course: tuple):
    course_name, grade = course
    if grade == 0:
        return
    if course_name not in students[name]:
        students[name][course_name] = grade
    else:
        students[name][course_name] = max(students[name][course_name], grade)


def print_student(students: dict, name: str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return      
    print(f"{name}:")
    if not students[name]:
        print(" no completed courses")
    else:
        print(f" {len(students[name])} completed courses:")
        total_grade = 0
        for course_name, grade in students[name].items():
            print(f"  {course_name} {grade}")
            total_grade += grade
        
        print(f" average grade {total_grade / len(students[name])}")


def summary(students: dict):
    most_courses = 0
    most_courses_name = ""
    best_avg_grade = 0
    best_avg_grade_name = ""  
    for key, value in students.items():
        completed = len(value)
        if completed > most_courses:
            most_courses = completed
            most_courses_name = key
        if completed > 0:
            avg_grade = sum(value.values()) / completed
            if avg_grade > best_avg_grade:
                best_avg_grade = avg_grade
                best_avg_grade_name = key
                
    print(f"students {len(students)}")
    print(f"most courses completed {most_courses} {most_courses_name}")
    print(f"best average grade {best_avg_grade} {best_avg_grade_name}")

if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)


#A square of letters
layers = int(input("Layers:"))
n = layers * 2 - 1
for i in range(n):
    for j in range(n):
        distance = [i, n - 1 - i, j, n - 1 - j]
        ring_no = min(distance)
        ascii_code = (layers - 1) - ring_no + 65
        character = chr(ascii_code)
        print(character,end="")
    print()

