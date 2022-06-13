class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for this employee woking in {self.company} is {self.salary} \n {signature} ")
    @staticmethod
    def greet():
        print("good morning")
bnod = Employee()
bnod.salary= 10000
bnod.getSalary("Thanks") #Employee.getSalary(bnod)
bnod.greet()   #Employee.greet()
 