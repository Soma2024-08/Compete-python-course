# Write a program to check grade based on marks ( A/B/C/D) using if-elif-else

marks= float(input("Enter your marks : "))
if marks > 85:
    print("Your grade is A")
elif marks<=85 and marks >70 :
    print("Your grade is B")
elif marks<=70 and marks >50:
    print("Your grade is C")
else:
    print("Your grade is D")