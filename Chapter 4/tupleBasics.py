# Tuples: Immutable lists
# Tuples are similar to lists, but they cannot be changed after creation.
# They are defined using parentheses () instead of square brackets [].


myTuple = (78,90,75,88,92,88,78,75)
studentTuple=("John",21,"A")

#studentTuple[0] = "Doe"  
#print(studentTuple)

print("Student Name:", studentTuple[0])
print("Student Age:", studentTuple[1])

# empty tuple
emptyTuple = ()
print("type of epmtyTuple is:", type(emptyTuple))

print(type(myTuple))

# tuple with one item
oneItemTuple = (5,)  # Note the comma
print("type of oneItemTuple is:", type(oneItemTuple))

print(myTuple.index(88))  # returns the index of first occurrence of 88
print(myTuple.count(75))  # returns the count of 75 in the tuple


fruit_list=("apple","banana","mango","orange","grapes")
print("length of fruit_list is:", len(fruit_list))
print(fruit_list.index("mango"))