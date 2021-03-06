class Employee:
    salary = 120000
    increment = 1.5
    

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, val):
        self.increment = val/self.salary



e = Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement = 150000
print(e.salaryAfterIncrement)
print(e.increment)