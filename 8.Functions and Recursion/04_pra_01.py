def greatest_number(num1, num2, num3):
    if(num1> num2 and num1> num3):
        return num1
    elif(num2> num1 and num2> num3):
        return num2
    else:
        return num3

num = greatest_number(11, 1000, 124)
print("The greatest value among them is  "+ str(num))