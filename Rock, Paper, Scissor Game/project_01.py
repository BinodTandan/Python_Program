# Snake Water and Gun Game

import random
def gameWin(comp, user):
    if comp==user:
        return None
    if comp=="s":
        if user == 'w':
            return False
        elif user=='g':
            return True
    if comp=="w":
        if user == 'g':
            return False
        elif user=='s':
            return True

    if comp=="g":
        if user == 's':
            return False
        elif user=='w':
            return True



print("Comp Turn:  Snake(s), Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
if randNo==1:
    comp = 's'
elif randNo==2:
    comp = 'w'
else:
    comp = 'g'


user = input("Your turn: Snake(s), Water(w) or Gun(g)?:")
print(f"comp choose {comp}")
print(f"you choose {user}")



a= gameWin(comp, user)
if(a==None):
    print("The game is tie!")

elif(a):
    print("you win!")

else:
    print("you lose!")


