# continue Statement: skip the current iteration and moves to the next one


for i in range(1,10):
    if i ==5:
        continue
    print(i)
print("for loop execution done")
i=1
while(i<=10):
    if i==5:
        i +=1
        continue
    print(i)
    i+=1