#Reading Input
def read_input(sentence: str, start: int, end: int):
    while True:
        try:
            number = int(input(sentence))
            if number >= start and number <= end:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {start} and {end}")

if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)


#Parameter validation
def new_person(name: str, age: int):
    words = name.split(" ")
    if name == "" or len(words) < 2 or len(name) > 40:
        raise ValueError
    else:
        full_name = name
    if age < 0 or age > 150:
        raise ValueError
    else:
        real_age = age
    return(full_name, real_age)

if __name__ == "__main__":
    info = new_person("peter parker", 20)


#Incorrect lottery numbers
def filter_incorrect():
    with open("lottery_numbers.csv", "r") as read_file, open("correct_numbers.csv", "w") as write_file:
        
        for line in read_file:
            parts = line.strip().split(";")
            header = parts[0]
            numbers_str = parts[1]
            
            header_parts = header.split(" ")
            if len(header_parts) != 2 or header_parts[0] != "week":
                continue
                
            try:
                int(header_parts[1]) 
            except ValueError:
                continue

            numbers_list = numbers_str.split(",")
            if len(numbers_list) != 7: 
                continue
                
            valid_row = True
            seen = []
            
            for num_str in numbers_list:
                try:
                    num = int(num_str)
                    if num < 1 or num > 39 or num in seen:
                        valid_row = False
                        break
                    seen.append(num)
                except ValueError:
                    valid_row = False
                    break
            
            if valid_row:
                write_file.write(line)