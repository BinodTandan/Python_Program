with open("word.txt", "r") as f:
    res = f.read()

res = res.replace("Donkey", "#$$%$#")

with open("word.txt", "w") as f:
    f.write(res)