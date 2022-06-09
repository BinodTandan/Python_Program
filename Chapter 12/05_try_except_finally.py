
try:
    a= int(input("Enter number: "))
    c = 1/a
except Exception as e:
    print(e)
    exit()

finally:
    print("we are sucessful")

print("Thanks for using program")