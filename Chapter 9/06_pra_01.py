f = open("poem.txt","r")
t = f.read()
if 'twinkle 'in t:
    print("twinkle is present")
else:
    print("twinkle is not present in poem")
print(t)
f.close()
