# Difference between parameter and argument:
# A parameter is a variable in the declaration of a function.
# An argument is the actual value of this variable that gets passed to function.
#======================================================================================
# difference between return statement and print statement:
# The return statement is used to exit a function and go back to the place where it was called. 
# It can return a value to the caller using the function but it does not display anything on the screen.
# The print statement is used to output data to the standard output device (screen).


def add(a, b):  # a and b are parameters
    return a + b
result = add(5, 3)  # 5 and 3 are arguments
print("Sum:", result)

# Example of function with parameters and arguments
def greet(name):  # 'name' is a parameter
    print("Hello,", name)   
greet("Soma")  # "Soma" is an argument
