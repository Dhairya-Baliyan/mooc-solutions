#emoticon: :-)
print(":-)")

#Fix the code: Seven Brothers
print("Aapo")
print("Eero")
print("Juhani")
print("Lauri")
print("Simeoni")
print("Timo")
print("Tuomas")

#Row, Row, Row Your Boat
print("Row, row, row your boat,")
print("Gently down the stream.")
print("Merrily, merrily, merrily, merrily,")
print("Life is but a dream.")

#Minutes in a year
day_minutes = 24 * 60
year_minutes = day_minutes * 365
print(year_minutes)

#Print some code
print('print("Hello there!")')

#Name twice
name = input("What is your name?")
print(name)
print(name)

#Name and exclamation marks
name = input("What is your name?")
print("!"+name+"!"+name+"!")

#Name and address
name = input("Given Name:")
family_name = input("Family Name:")
street_address = input("Street Address:")
city_and_postal_code = input("City and postal code:")

print(name+" "+ family_name)
print(street_address)
print(city_and_postal_code)

#Fix the code: Utterances
part1 = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(part1 + "-" + part2 + "-" + part3 + "!")

#Story
name = input("Please type in a name:")
year = input("Please type in a year:")

print(f"{name} is a valiant knight, born in the year {year}. One morning {name} woke up to an ")
print(f"awful racket: a dragon was approaching the village. Only {name} could save the ")
print("village's residents.")

#Extra space
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print(f"my name is {name}, I am {age} years old")
print()
print("my skills are")
print(f" - {skill1} ({level1})")
print(f" - {skill2} ({level2})")
print(f" - {skill3} ({level3})")
print()
print(f"I am looking for a job with a salary of {lower}-{upper} euros per month")

#Arithmetics
x = 27
y = 15
print(f"{x} + {y} = {x+y}")
print(f"{x} - {y} = {x-y}")
print(f"{x} * {y} = {x*y}")
print(f"{x} / {y} = {x/y}")

#Fix the code: Print a single line
print(5,end="")
print(" + ",end="")
print(8,end="")
print(" - ",end="")
print(4,end="")
print(" = ",end="")
print(5 + 8 - 4)

#Times five
num = int(input("Please type in a number:"))
print(f"{num} times 5 is {num * 5}")

#Name and age
name = input("What is your name?")
year = int(input("What year were you born?"))
print(f"Hi {name}, you will be {2021 - year} years old at the end of the year 2021")

#Seconds in a day
days = int(input("How many days?"))
print(f"Seconds in that many days: {days * 24 * 60 * 60}")

#Fix the code: Product
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)

#Sum and product
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
print(f"The sum of the numbers: {num1 + num2}")
print(f"The product of the numbers: {num1 * num2}")

#Sum and mean
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
num3 = int(input("Number 3:"))
num4 = int(input("Number 4:"))
print(f"The sum of the numbers is {num1 + num2+ num3 + num4} and the mean is {(num1 + num2 + num3 + num4)/4}")

#Food expenditure
times_eaten = int(input("How many times a week do you eat at the student cafeteria?"))
price = float(input("The price of a typical student lunch?"))
money_spent = float(input("How much money do you spend on groceries in a week?"))
print()
print(f"Average food expenditure:")
weekly = times_eaten * price + money_spent
daily = weekly/7
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")

#Students in groups
number_of_student = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
print(f"Number of groups formed: {(number_of_student+group_size-1)//group_size}")

#Orwell
num = input("Please type in a number:")
if num == "1984":
    print("Orwell")

#Absolute value
num = int(input("Please type in a number:"))
if num < 0:
    print(f"The absolute value of this number is {num * -1}")
print(f"The absolute value of this number is {num}")

#Soup or no soup
name = input("Please tell me your name:")
if name != "Jerry":
    portions = int(input("How many portions of soup?"))
    print(f"The total cost is {portions * 5.90}")
print("Next please!")

#Order of magnitude
num = int(input("Please type in a number:"))
if num < 1000:
    print("This number is smaller than 1000")
if num < 100:
    print("This number is smaller than 100")
if num < 10:
    print("This number is smaller than 10")
print("Thank you!")

#Calculator
num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
operation = input("Operation:")
print()
if operation == "add":
    print(f"{num1} + {num2} = {num1+num2}")
if operation == "subtract":
    print(f"{num1} - {num2} = {num1-num2}")
if operation == "multiply":
    print(f"{num1} * {num2} = {num1*num2}")

#Temperatures
temp = int(input("Please type in a temprature(F):"))
celsius = (temp - 32) * 5/9
print(f"{temp} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
    print("Brr! It's cold in here!")

#Daily wages
wage = float(input("Hourly wage:"))
work = int(input("Hours worked:"))
day = input("Day of the week:")
daily_wage = wage * work
if day == "Sunday":
    print(f"Daily wages: {daily_wage * 2} euros")
if day != "Sunday":
    print(f"Daily wages: {daily_wage} euros")

#Loyalty bonus
points = int(input("How many points are on your card? "))
if points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")

print("You now have", points, "points")

#What to wear tomorrow
print("What is the weather forecast for tomorrow?")
temp = int(input("Temprature:"))
rain = input("Will it rain(yes/no):")
if temp > 20 or temp <= 20:
    print("Wear jeans and a T-shirt")
if temp > 10 and temp <=20 or temp <= 10:
    print("I recommend a jumper as well")
if temp > 5 and temp <= 10 or temp <=5:
    print("Take a jacket with you")
if temp <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")

#Solving a quadratic equation
from math import sqrt
a = int(input("Value pf a:"))
b = int(input("Value of b:"))
c = int(input("Value of c:"))
x1 =(-b + sqrt((b * b) - (4 * a * c)))/(2 * a)
x2 =(-b - sqrt((b * b) - (4 * a * c)))/(2 * a)
print(f"The roots are {x1} and {x2}")

#End of the exercise of part 1 mooc.fi python course 2026