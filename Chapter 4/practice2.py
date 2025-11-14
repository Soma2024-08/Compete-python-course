# take 3 food and store in list, print list and print length
food_list = []
for i in range(1,4):
    food = input(f"Enter food item: ")
    food_list.append(food)
print("length of the food list is:", len(food_list))
print("Food items:", food_list)
