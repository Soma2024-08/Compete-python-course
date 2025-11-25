# Type of arguments:
# 1. Positional Arguments: order matters
# 2. Keyword Arguments: order does not matter
# 3. Default Arguments: if no argument is passed, default value is used
# 4. Arbitrary Arguments: *args and **kwargs 
# first *args then **kwargs
# first normal arguments, then *args, then **kwargs

def greet(name, dept):
    print(f"Hello {name}")
    print(f"Are you from {dept} department?")
greet("Soma","Math")  
greet("Math","Soma")  # makes no sense

greet(dept="Math",name="Soma")  # now it make sense, because we are using keyword arguments 

greet("Soma", dept="Math") # valid: positional argument followed by keyword argument

# greet(name="Soma", "Math") # this will give error


def greet2(name, dept="CSE"):  # dept has default value "CSE"
    print(f"Hello {name}")
    print(f"Are you from {dept} department?")
greet2("Soma")  # dept will take default value "CSE"
greet2("Soma", "Math")  # dept will take value "Math"


def greet2(name,subject, dept="CSE"):  # dept has default value "CSE"
    print(f"Hello {name}")
    print(f"You study {subject}")
    print(f"Are you from {dept} department?")
#greet2("Soma")  # missing required positional argument 'subject'

greet2("Soma","Calculus")  # dept will take default value "CSE"

#def greet3(name, dept="math",subject):  # a non-default argument cannot come after a default argument
    

def add(*numbers):  # arbitrary positional arguments
    total = 0
    for num in numbers:
        total += num
    return total
print(add(1, 2, 3))  
print(add(5, 10, 15, 20, 25))

def student_info(**info):  # arbitrary keyword arguments
    for key, value in info.items():
        print(f"{key}: {value}")
student_info(name="Soma", age=20, dept="Math")
student_info(name="Alex", grade="A", city="New York", hobby="Painting") 
# student_info("Soma", 20)  # this will give error
    
def add(*numbers,name):
    total = 0
    for num in numbers:
        total += num
    print(f"Total added by {name} is {total}")

add(1, 2, 3, name="Soma")