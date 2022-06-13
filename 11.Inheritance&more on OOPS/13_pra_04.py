class Complex:
    def __init__(self, num1, num2):
        self.real = num1
        self.imag = num2

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __mul__(self, c):
        return Complex((self.real*c.real - self.imag*c.imag), (self.real*c.imag + self.imag*c.real))

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = Complex(11,22)
c2 = Complex(10,20)
print(c1+c2)
print(c1*c2)
