log = True
i = 1

with open("logfile.txt", 'r') as f:
    while log:
        log = f.readline()

        if 'python' in log.lower():
            print(log)
            print(f"yes python is in line {i}")
        i +=1