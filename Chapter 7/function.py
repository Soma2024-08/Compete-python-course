# Function: instead of writing the same code multiple times,
# we can define a function and call it whenever needed.

def greet(name):
    print(f"Hello, {name}!")
greet("Samanta")
#=============================================================

def Average():
    n = int(input("Enter number of elements: "))
    total = 0
    for _ in range(n):
        num = float(input("Enter number: "))
        total += num
    avg = total / n
    print(f"The average is: {avg}")
Average()

#=============================================================

def Average():
    numbers=input("Enter numbers separated by space: ")
    numbers=[float(num) for num in numbers.split()]
    total=0
    for num in numbers:
        total+= num
    avg=total/len(numbers)
    print(f"The average is: {avg}")
Average()