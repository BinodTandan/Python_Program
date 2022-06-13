# Use Open function to read the content of the text file

# f = open("sample.txt", 'r')
f = open("sample.txt") # By default it select the read mode
data= f.read(9)
# data= f.read()

print(data)
f.close()
