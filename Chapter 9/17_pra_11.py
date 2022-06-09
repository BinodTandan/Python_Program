import os
file1 = "that.txt"
newname = "renamed_by_python.txt"

with open(file1, 'r') as f:
    content = f.read()

with open(newname, 'w') as f:
     f.write(content)

os.remove(file1)

