# Write a program that takes any word or sentences as input and prints:
# 1. The first character
# 2. The last character
# 3. the total number of characters

input_string = input("Enter a word or sentence: ")
length = len(input_string)
print("The first character is:", input_string[0])
print("The last character is:", input_string[-1])
print("The total number of characters is:", length)