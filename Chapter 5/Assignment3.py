# try to add both integer 9 and float 9.0 to a set and observe what happen.
#(hint: you can convert one into a string to make both unique.)

set={1,2,3,"1.0",3.0,4.0}

print(set)
set.add(9)
set.add(9.0)
print(set)
set.add("9.0")
print(set)

set.pop()
set.pop()
print(set)

set.remove("1.0")
print(set)


