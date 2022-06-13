class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee woking in {self.company} is {self.salary} ")

bnod = Employee()
bnod.salary= 10000
bnod.getSalary()
