class Employee:
    company = "Tiptop"
    salary = 10000
    salarybonous = 2000


    @property
    def totalSalary(self):
        return  self.salary + self.salarybonous

    
    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonous = val - self.salary


    
    # @totalSalary.setter
    # def totalSalary(self, val):
    #     self.salarybonous = val -self.salary
e = Employee()
print(e.totalSalary)
e.totalSalary = 11500
print(e.totalSalary)
print(e.salarybonous)