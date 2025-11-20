# Write a program to print numbers from 1 to 50, but print "Soma Samanta" instead of numbers that are multiple of 5

for i in range(1,51):
    if i%5 ==0:
        print("Soma Samanta")
    print(i)

print("using for loop execution done")
print("\n")

j=1
while j<=50:
    if j%5 ==0:
        print("Soma Samanta")
        j+=1
    else:
        print(j)
        j +=1
print("Using while loop execution done")