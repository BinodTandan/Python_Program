import random
randNo = random.randint(0,100)
count = 0
user = None
while(user != randNo):
    user = int(input("User Guess: "))
    count += 1
    if randNo == user:
        print("Your quess is right")
    else:
        if randNo > user:
            print("Higher Number please!")
        else:
            print("Lower Number please!")
print(f"You guess the number after {count} guesses")

with open("hiscore.txt", 'r') as f:
    hiscore = int(f.read())
if(count<hiscore or hiscore == None):
    print("You have just broke the high score")
    with open("hiscore.txt", 'w') as f:
        f.write(str(count))
