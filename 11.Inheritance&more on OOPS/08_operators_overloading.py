

class Number:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, num2):
        print("lets add")
        return self.num + num2.num

    def __mul__(self, num2):
        print("lets multiply")
        return self.num * num2.num
# For addition
n1 = Number(19)
n2 = Number(10)
sum = n1 + n2
print(sum)
mul = n1*n2
print(mul)