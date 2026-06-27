def isComposite(number: int):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(f"{number} is a composite number")
                return True

start_index = int(input("Enter starting index:"))
number = int(input("Enter the number of composite number to print:"))
counter = 0
while counter < number:
    composite = isComposite(start_index)
    start_index += 1
    if composite:
        counter += 1
