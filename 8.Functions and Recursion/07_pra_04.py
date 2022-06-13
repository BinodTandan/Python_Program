def sum_natural(num):
    if(num>0):
        return num*(num+1)/2
    else:
        print("Enter positive value")
num1 = int(input("Enter the number: "))
result = sum_natural(num1)
print(f"sum of first {num1} numbers is {result}")