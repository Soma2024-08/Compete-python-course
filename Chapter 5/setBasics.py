# Sets: it is unordered and store unique items, mulatable(add , remove)
# written using curly braces {}

food={} # create set
food={"paneer","chole bhature","golgappa","sandwitch","paneer"}
print(type(food))
print(food)

# create an empty set
empty_set= set()
print(type(empty_set))

# methods
food.add("Biriyani")
food.remove("paneer")
print(food)



