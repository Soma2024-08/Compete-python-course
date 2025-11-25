# Write a Python function named to_upper() that:
#Takes no arguments.
#Asks the user to enter a sentence.
#Converts the entire sentence to uppercase without using .upper() method.
#Prints the converted uppercase sentence.
#In ASCII, uppercase letters are 32 positions before lowercase letters.

#Example:
#'a' (97) – 32 → 65 (which is 'A')
#'b' (98) – 32 → 66 (which is 'B')

#chr(...): Converts the ASCII number back into a character.

def convert_to_upper():
    userInput = input("Enter a sentence: ")
    upper_sentence = ""
    for char in userInput:
        if 'a' <= char <= 'z':
            upper_char = chr(ord(char) - 32)
            upper_sentence += upper_char
        else:
            upper_sentence += char
    return upper_sentence
result = convert_to_upper()
print("Uppercase Sentence:", result)

#---------------------------------------------------------------

# Another way to solve the same problem

def to_upper(text):
    return text.upper()
to_upper("hello worLd!")