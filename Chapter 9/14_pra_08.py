with open("this.txt", 'r') as f:
    content = f.read()

with open("copy.text", 'w') as f:
    f.write(content)