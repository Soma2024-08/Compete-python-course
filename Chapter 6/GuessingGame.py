import random
Jackpot=random.randint(1,100)
guess= int(input("Guess the number: "))
counter=1
while guess != Jackpot:
    if guess>Jackpot:
        guess=int(input("Guess lower value: "))
    elif guess<Jackpot:
        guess=int(input("Guess higher number: "))
    counter +=1
print("Wohooo! You won the game🎊")
print(f"You take {counter} attempts to guess the number.")
