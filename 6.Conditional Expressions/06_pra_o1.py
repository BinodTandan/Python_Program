# Program to find the greatest of four number entered by user
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Fourth Number: "))

if(a>b):
    f1 = a
else:
    f2= b

if(c>d):
    f1 = c
else:
    f2= d

if(f1>f2):
    print(f1," is the greatest number")
else:
    print(f2, " is the greatest number")
