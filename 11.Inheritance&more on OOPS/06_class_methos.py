class Employee:
    company = "Apple"
    salary = 1000
    @classmethod
    def changeSalary(cls, sla):
        cls.salary = sla


e = Employee()
print(e.salary)
e.changeSalary(2000)
print(e.salary)
print(Employee.salary)
