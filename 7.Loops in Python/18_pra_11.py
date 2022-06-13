for row in range(3):
    for col in range(5):
        if(row==0 and col%2==0) or (row ==1 and col%4==0) or (row==2 and col%2==0):
            print("*", end="")
        else:
            print(" ", end="")

    print()