class Calculator:
    def __init__(self, num):
        self.num = num
        print("The result is given below:")

    def getResult(self):
        print(f"The sqaure of {self.num} is {self.num ** 2}")
        print(f"The cube of {self.num} is {self.num  ** 3}")
        print(f"The sqaure root of {self.num} is {self.num ** 0.5}")

binod = Calculator(16)
binod.getResult()
        