import random

randNumber = random.randint(1, 100)
# print(randNumber)  LET YOU KNOW THE NUMBER ,DELETE IT BEFORE PLAYING THE GAME
userGUESS = None
guesses = 0

while userGUESS != randNumber:
    userGUESS = int(input("Enter your guess: "))
    guesses += 1
    if userGUESS == randNumber:
        print("You guessed it right!!")
    else:
        if userGUESS > randNumber:
            print("ENTER A SMALLER NUMBER")
        else:
            print("ENTER A LARGER NUMBER ")

print(f"You guessed the number in {guesses} guesses")
