#Multiplication
num = int(input("Please type in a number:"))
a = 1
while a <= num:
    b = 1
    while b <= num:
          print(f"{a} x {b} = {a*b}")
          b += 1
    a += 1

#First letter of words
sentence = input("Please type in a sentence:")
sentence = " " + sentence
counter = 0
while counter < len(sentence):
    if sentence[counter] == " ":
        print(sentence[counter + 1])
    counter += 1

#Factorial
while True:
    number = int(input("Please type in a number:"))
    if number <= 0:
        print("Thanks and bye!")
        break;
    factorial = 1
    counter = 1
    while counter <= number:
        factorial *= counter
        counter += 1
    print(f"The factorial of the number {number} is {factorial}")

#Flip the pairs
number = int(input("Please type in a number:"))
counter1 = 1
counter2 = 2
while counter1 <= number:
    if counter2 <= number:
            print(counter2)
    print(counter1)
    counter1 += 2
    counter2 += 2

#Taking turns
number = int(input("Please type in a number:"))
index1 = 1
index2 = number
while index1 < index2:
    print(index1)
    print(index2)
    index1 += 1
    index2 -= 1
if index1 == index2:
    print(index1)
