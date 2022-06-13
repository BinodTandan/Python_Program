file1 = "logfile.txt"
file2 = "this.txt"

with open(file1,'r') as f:
    f1 = f.read()

with open(file2,'r') as f:
    f2 = f.read()

if(f1 == f2):
    print("files are identical")
else:
    print("fileS aren't identical")