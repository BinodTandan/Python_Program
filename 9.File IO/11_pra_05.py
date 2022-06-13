words = ["murkha", "alxi","kattu"]
with open("list.txt",'r') as f:
    le= f.read()

for word in words:
        le = le.replace(word, "*$%##***")
        with open("list.txt", 'w') as f:
            f.write(le)
