
try:
    a = int(input("Enter a number:"))
    b = input("Enter a string :")
    c = 1/a
    d = a + b
    print(d)

except ValueError as e:
    print("Please entered a valid value!!!")
    print(f"Occured exception is {e}")

except ZeroDivisionError as e:
    print("Please entered non zero value")
    print(f"Occured exception is {e}")

except TypeError as e:
    print("Please entered the value of same type")
    print(f"Occured exception is {e}")

print("Thanks for using this code")


