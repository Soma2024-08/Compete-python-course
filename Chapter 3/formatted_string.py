# f-String make it easy to include variavles inside strings

name="Soma"
age=25
# without f-string
print("My name is "+name+". I am "+str(age)+" years old.")

# with f-string
print(f"My name is {name}. I am {age} years old.")


# Escape sequences
print("Hello viewers, Welcome to the Python Course.")  # Normal print
print("Hello viewers,\nWelcome to the Python Course.")  # New line
print("Hello viewers,\tWelcome to the Python Course.")  # Tab space


# membership operator
str="GulabJamun"
print("Jamun" in str)  # True
print("Mango" not in str)  # True