def game():
    user = int(input("Enter score:"))
    return user
score = game()
with open("Hiscore.txt", 'r') as f:
    hiscore = int(f.read())
if hiscore < score:
    with open("Hiscore.txt","w") as f:
        f.write(str(score))


