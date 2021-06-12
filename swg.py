import random

# Snake , Water , Gun game :--
def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 's':
            return True


print("Player-1 turn: Snake(s) Water(w) Gun(g)")
randNo = random.randint(1, 3)
print(randNo)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Player-2 turn: Snake(s) Water(w) Gun(g)")
a = gameWin(comp, you)
if a == None:
    print(" GAME IS A TIE")
elif a:
    print("You Win!")
else:
    print("You Lose!")
print(f"computer chose {comp}")
print(f"you chose {you}")