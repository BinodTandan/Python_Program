# with open("another.txt", 'r') as f:
#     a = f.read()
# print(a)
with open("another.txt", 'w') as f:
    a = f.write("Hello world")
print(a)