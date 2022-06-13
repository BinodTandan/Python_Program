while(True):
    a = input("Enter a number:")
    if(a == "q"):
        break
    
    try:
        a = int(a)
        if (a >  10):
            print("You entered a number greater than 10")

        elif (a < 10):
            print("You entered a number less than 10")

    except Exception as e:
        print(f"The exception occurs is {e}")

print("Thanks!!")
