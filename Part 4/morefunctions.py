#Greatest number
def greatest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
    else:
        return a 

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)


#Same characters
def same_chars(text, index1, index2):
    if index1 >= len(text) or index2 >= len(text):
        return False
    if text[index1] == text[index2]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))


#first_second_last word
def first_word(sentence1):
    word =""
    index = 0
    while index < len(sentence1) and sentence1[index] != " ":
        word += sentence1[index]
        index += 1
    return word

def second_word(sentence2):
    index = 0

    while index < len(sentence2) and sentence2[index] != " ":
        index += 1 
    while index < len(sentence2) and sentence2[index] == " ":
        index += 1
    word = ""
    while index < len(sentence2) and sentence2[index] != " ":
        word += sentence2[index]
        index += 1
        
    return word

def last_word(sentence3):
    index = len(sentence3) - 1
    while index >= 0 and sentence3[index] != " ":
        index -= 1
    return sentence3[index + 1:]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))