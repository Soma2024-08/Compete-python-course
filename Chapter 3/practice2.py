# write a program that:
# 1. takes a sentence as input
# 2. converts it to lowercase
# 3. replaces all spaces with "_"
# 4. prints the modified string

sentence = input("Enter a sentence: ")
modified_sentence=sentence.lower()
modified_sentence=modified_sentence.replace(" ","_")
print("Modified string is:", modified_sentence)