#Box of hashes
# ##########
# #########
# #########
# #########
# #########

def line(length, text):
        print(text*length)

def box_of_hashes(height):
    counter = 1
    while counter <= height: 
        line(10, "#")
        counter += 1
        
if __name__ == "__main__":
    box_of_hashes(5)


#Square of hashes
# #####
# ####
# ####
# ####
# ####

def line(length, text):
    print(text*length)

def square_of_hashes(size):
    counter = 1
    while counter <= size:
        line(size, "#")
        counter += 1

if __name__ == "__main__":
    square_of_hashes(5)


#Square
#*****
#*****
#*****
#*****
#*****

def line(length, text):
    print(text*length)

def square(size, character):
    counter = 1
    while counter <= size:
        line(size, character)
        counter += 1
        
if __name__ == "__main__":
    square(5, "x")

#Triangle
# #
# #
# ##
# ###
# ####
# #####
def line(length, text):
    print(text*length)

def triangle(size):
    counter = 1
    while counter <= size:
        line(counter, "#")
        counter += 1

if __name__ == "__main__":
    triangle(5)


#Shape
# X
# XX
# XXX
# XXXX
# XXXXX
# *****
# *****
# *****
def line(length, text):
    print(text*length)
def shape(size1, character1, size2, character2):
    counter = 1
    while counter <= size1:
        line(counter, character1)
        counter += 1
    counter1 = 1
    while counter1 <= size2:
        line(size1, character2)
        counter1 += 1
    
if __name__ == "__main__":
    shape(5, "x", 2, "o")

#Spruce
#    *
#   ***
#  *****
# *******
#*********
#    *
def spruce(size):
    print("a spruce!")
    counter1 = 1
    counter2 = 1
    space = size - 1
    while counter1 <= size:
        print(" "*space,end="")
        print("*"*counter2)
        space -= 1
        counter1 += 1
        counter2 += 2
        print()
    counter3 = (counter2 - 2)//2
    print(" "*counter3, end="")
    print("*")

if __name__ == "__main__":
    spruce(3)