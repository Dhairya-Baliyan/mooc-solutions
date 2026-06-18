#Seven brothers
def seven_brothers():
    print("Aapo")
    print("Eero")
    print("Juhani")
    print("Lauri")
    print("Simeoni")
    print("Timo")
    print("Tuomas")

if __name__ == "__main__":
    seven_brothers()

#The first character
def first_character(text):
    print(text[0])

if __name__ == "__main__":
    first_character('python')
    first_character('yellow')
    first_character('tomorrow')
    first_character('heliotrope')
    first_character('open')
    first_character('night')

#Mean
def mean(x, y, z):
    mean = (x + y + z)/3
    print(mean)
# Testing the function
if __name__ == "__main__":
    mean(1, 2, 3)

#Print Many Times
def print_many_times(text, times):
    while times > 0:
        print(text)
        times -= 1
if __name__ == "__main__":
    print_many_times("python", 5)

#Square of hashes
def hash_square(length):
    a= length
    while length > 0:
        print("#"*a)
        length -= 1

if __name__ == "__main__":
    hash_square(5)

#Chessboard
def chessboard(length):
    a = 1
    b = 1
    while b <= length:
        if b % 2 == 0:
            a = 0;
        else:
            a = 1
        c = 1
        while c <= length:
            print(a, end="")
            if a == 0:
                a = 1;
            else:
                a = 0
            c += 1
        print()
        b += 1

# Testing the function
if __name__ == "__main__":
    chessboard(4)

#A word squared
def squared(text, length):
    counter = 0
    b = 1
    length1 = len(text)
    while b <= length:
        c = 1
        while c <= length:
            print(text[counter],end="")
            counter = (counter + 1) % length1
            c += 1
        print()
        b += 1

if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)

