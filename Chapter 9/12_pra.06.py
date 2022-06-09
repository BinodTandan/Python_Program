with open("logfile.txt", 'r') as f:
    log = f.read().lower()

if 'python' in log:
    print("It contains python")

else:
    print("It dosen't contain python")