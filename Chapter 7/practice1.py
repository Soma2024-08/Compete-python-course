# write a function that return square of a number
def Square(num):
    return num * num
print(Square(5))

#-------Aother way to write the same function using lambda expression
Square = lambda x: x * x
print(Square(6))

# -----Another way-------------

def Square():
    num = int(input("Enter a number: "))
    return num * num
print(Square())
    