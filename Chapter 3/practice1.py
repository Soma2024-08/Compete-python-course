# write a program that takes your favourite food name as input and prints:
# 1. The middle 3 characters
# 2. the last 2 characters

food_name = input("Enter your favourite food name: ")
length = len(food_name)
mid = length // 2  # remove decimal part
print("The middle 3 characters are", food_name[mid-1:mid+2])
print("The last 2 characters are", food_name[length-2:])

#another way to get last 2 characters
print("The last 2 characters are", food_name[-2:])