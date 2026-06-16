#String multiplied
string = input("Please type in a string:")
amount = int(input("Please type in an amount:"))
print(string*amount)

#The longer string
string1 = input("Please type in string 1:")
string2 = input("Please type in string 2:")
len1 = len(string1)
len2 = len(string2)
if len1 > len2:
    print(f"{string1} is longer")
elif len2 > len1:
    print(f"{string2} is longer")
else:
    print("The strings are equally long")

#End to beginning
string = input("Please type in a string:")
length = len(string)
while length - 1 >= 0:
    print(string[length - 1])
    length -= 1
 
#Second and second to last characters
string = input("Please type in a string:")
sec_char = string[1]
last_sec_char = string[-2]
if sec_char != last_sec_char:
    print("The second and the second to last characters are different")
else:
    print(f"The second and the second to last characters are {sec_char}")

#A line of hashes
width = int(input("Width:"))
print("#"*width)

#A rectangle of hashes
width = int(input("Width:"))
height = int(input("Height:"))
while height > 0:
    print("#"*width)
    height -= 1 

#Underlining
while True:
    string = input("Please type in a string:")
    if string == "":
        break;
    print(string)
    print("-"*len(string))

#Right-aligned
string = input("Please type in a string:")
if len(string) < 20:
    print("*"*(20 - len(string)),end="")
    print(string)
else:
    print(string)

#A framed word
word = input("Word:")
print("*"*30)
if len(word) % 2 == 0:
    print("*",end="")
    space_len = (30//2 -len(word)//2) - 1
    print(" "*space_len,end="")
    print(word,end="")
    print(" "*space_len,end="")
    print("*")
else:
    print("*",end="")
    space_len = (30//2 -len(word)//2) - 1
    print(" "*(space_len - 1),end="")
    print(word,end="")
    print(" "*space_len,end="")
    print("*")
print("*"*30)

#Substrings, part 1
string = input("Please type in astring:")
length = len(string)
a = 1
while a <= length:
    print(string[:a])
    a += 1

#Substrings, part 2
string = input("Please type in a string:")
index = len(string) - 1
while index >= 0:
    print(string[index:])
    index -= 1

#Does it contain vowels
string = input("Please type in string:")
index = 0
if "a" in string:
    print("a found")
else:
    print("a not found")
if "e" in string:
    print("e found")
else:
    print("e not found")
if "o" in string:
    print("o found")
else:
    print("o not found")

#Find the first substring
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
index = word.find(character)
if index!=-1 and len(word)>=index+3:
    print(word[index:index+3])
 
#Find all the substrings
word = input("Please type in a word:")
character = input("Please type in a character:")
index = 0
while index < len(word):
    if len(word) >= index + 2 and word[index] == character:
        string = word[index:index+3]
        if len(string) > 2:
            print(string)
    index += 1

#The second occurrence
string = input("Please type in a string:")
substring = input("Please type in a substring:")
index = string.find(substring)
if index == -1:
    print("The substring does not occur twice in the string.")
else:
    position = index + len(substring)
    sliced_string = string[position:]
    if substring in sliced_string:
        index_2 = sliced_string.find(substring)
        print(f"The second occurrence of the substring is at index {position + index_2}.")
    else:
        print("The substring does not occur twice in the string.")

