# Write a program to print a multiplication table of any number using a while loop

number=int(input("enter a number: "))
i=1
while i<=10:
    mul=number * i 
    print(f"{number}*{i}={mul}")
    i +=1
