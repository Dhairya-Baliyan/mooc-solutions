#Print numbers
num = 2
while num <= 30:
    print(num)
    num += 2

#Fix the code: Countdown
print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
        print(number)
        number -= 1
print("Now!")

#Numbers
upper_limit = int(input("Upper limit:"))
num = 1
while num > 0 and num < upper_limit:
    print(num)
    num += 1

#Powers of two
upper_limit = int(input("Upper limit:"))
power = 0
while 2 ** power <= upper_limit:
    print(2 ** power)
    power += 1

#Powers of base n
upper_limit = int(input("Upper limit:"))
base = int(input("Base:"))
number = 1
while number <= upper_limit:
    print(number)
    number = number * base

#The sum of consecutive numbers, version 1
limit = int(input("Limit:"))
sum = 0
number = 1
while sum < limit:
    sum += number
    number += 1
print(sum)

#The sum of consecutive numbers, version 2
limit = int(input("Limit:"))
sentence = "The consecutive sum: 1"
sum = 1
number = 1
while sum < limit:
    number += 1
    sentence += " + " + str(number)
    sum += number
sentence += " = " + str(sum)
print(sentence)

#