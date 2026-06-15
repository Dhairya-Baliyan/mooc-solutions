#Fix the syntax
number = int(input("Please type in a number: "))
if number>100:
    print("The number was greater than one hundred")
    number = number - 100
    print("Now its value has decreased by one hundred")
    print("Its value is now",number)
print(number,"must be my lucky number!")
print("Have a nice day!")

#Number of characters
word = input("Please type in a word:")
if len(word) > 1:
    print(F"There are {len(word)} letter in the word {word}")
print("Thank you!")

#Typecasting
num = float(input("Please typr in a number:"))
int_part = int(num)
decimal_part = num - int_part
print(f"Integer part: {int_part}")
print(f"Decimal part: {decimal_part}")

#Age of maturity
age = int(input("How old are you?"))
if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")

#Greater than or equal to
num1 = int(input("Please type in the first number:"))
num2 = int(input("Please type in the second number:"))
if num1 > num2:
    print(f"The greater number was: {num1}")
elif num2 > num1:
    print(f"The greater number was: {num2}")
else:
    print("The numbers are equal")

#The elder
print("Person 1:")
name1 = input("Name:")
age1 = int(input("Age:"))
print("Person 2:")
name2 = input("Name:")
age2 = int(input("Age:"))
if age1 > age2:
    print(f"The elder is {name1}")
elif age2 > age1:
    print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are of the same age")

#Alphabetically last
word1 = input("Please type in the 1st word:")
word2 = input("Please type in the 2nd word:")
if word1 > word2:
    print(f"{word1} comes alphabetically last.")
elif word2 > word1:
    print(f"{word2} comes alphabetically last.")
else:
    print("You gave the same word twice.")

#Age check
age = int(input("What is your age?"))
if age > 4:
    print(f"Ok, you're {age} years old")
elif age < 5 and age >= 0:
    print("I suspect you can't write quite yet...")
elif age < 0:
    print("That must be a mistake")

#Nephews
name = input("Please type in your name:")
if name == "Huey" or name == "Dewey" or name == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
elif name == "Morty" or name == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

#Grades and points
points = int(input("How many points[0-100]:"))
if points < 0:
    print("Grade: impossible!")
elif points >= 0 and points < 50:
    print("Grade: fail")
elif points >= 50 and points < 60:
    print("Grade: 1")
elif points >= 60 and points < 70:
    print("Grade: 2")
elif points >= 70 and points < 80:
    print("Grade: 3")
elif points >= 80 and points < 90:
    print("Grade: 4")
elif points >=90 and points <= 100:
    print("Grade: 5")
else:
    print("grade: impossible!")

#FizzBuzz
num = int(input("Number:"))
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")

#Leap year
year = int(input("Please type in a year:"))
if year % 400 == 0:
    print("That year is a leap year.")
elif year % 100 == 0:
    print("That year is not a leap year.")
elif year % 4 == 0:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")

#Alphabetically in the middle
letter1 = input("1st Letter:")
letter2 = input("2nd Letter:")
letter3 = input("3rd Letter:")

if letter1 > letter2 and letter1 < letter3:
    print(f"The letter in the middle is {letter1}")
elif letter1 > letter3 and letter1 < letter2:
     print(f"The letter in the middle is {letter1}")
elif letter2 > letter1 and letter2 < letter3:
    print(f"The letter in the middle is {letter2}")
elif letter2 > letter3 and letter2 < letter1:
    print(f"The letter in the middle is {letter2}")
elif letter3 > letter1 and letter3 < letter2:
    print(f"The letter in the middle is {letter3}")
elif letter3 > letter2 and letter3 < letter1:
    print(f"The letter in the middle is {letter3}")

#Gift tax calculator
tax = 0.0
value = int(input("Value of gift:"))
if value >= 5000 and value < 25000:
    tax = 100 + (value - 5000) * 0.08
elif value >= 25000 and value < 55000:
    tax = 1700 + (value - 25000) * 0.1
elif value >= 55000 and value < 200000:
    tax = 4700 + (value - 55000) * 0.12
elif value >= 200000 and value < 1000000:
    tax = 22100 + (value - 200000) * 0.15
elif value >= 1000000:
    tax = 142100 + (value - 1000000) * 0.17
elif value < 5000:
    tax = 0
if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")

#Shall we continue?
print("hi")
while True:
    hi = input("Shall we continue?")
    if hi == "no":
        print("okay then")
        break;
    print("hi")
    
#Input validation
from math import sqrt

while True:
    num =int(input("Please type in a number:"))
    if num == 0:
        print("Exiting...")
        break;
    elif num < 0:
        print("Invalid number")
        continue;
    print(sqrt(num))

#Fix the code: Countdown
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number == 0:
    break;
print("Now!")

#Repeat password
password = input("Password:")
while True:
    rep_password = input("Repeat Password:")
    if password != rep_password:
        print("They do not match!")
        continue;
    else:
        print("User account created!")
        break;

#PIN and number of attempts
correct_pin = 4321
attempts = 0
while True:
    pin = int(input("PIN:"))
    attempts+=1
    if pin == correct_pin:
        if attempts == 1:
            print("Correct! It only took you one single attempt!")
            break;
        print(f"Correct! It took you {attempts} attempts")
        break;
    else:
        print("Wrong")

#The next leap year
year = int(input("Year:"))
leap_year = year
while True:
    leap_year += 1
    if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
        break;
print(f"The next leap year after {year} is {leap_year}")

#Story
code = ""
repeat = ""
while True:
    word = input("Please type in a word:")
    if word == repeat:
        print(code)
        break;
    elif word == "end":
        print(code)
        break;
    else:
        code += word + " "
        repeat = word

#Working with numbers
count = 0
positive = 0
negative = 0
sum = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    num = int(input("Number:"))
    if num == 0:
        break;
    elif num >= 0:
        positive += 1
    elif num < 0:
        negative += 1
    count += 1
    sum += num
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
mean = sum/count
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")

#Part 2 solutions 