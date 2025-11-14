# ask the user for their 3 favouriteb movies and store them in a list. print the list and print the length of the list
movie_list = []
for i in range(1,4):
    movie = input(f"Enter your favourite movie {i}: ")
    movie_list.append(movie)
print("You have", len(movie_list), "favourite movies.")
print("Your favourite movies are:", movie_list)
