from unicodedata import name


class Employee:
    company = "Google"
    

    def __init__(self, name, salary, subunit): # Constructors
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f"The name of employee is {self.name}")
        print(f"The salary of employee is {self.salary}")
        print(f"The name of employee is {self.subunit}")
        
        
        

    def getSalary(self, signature):
        print(f"Salary for this employee woking in {self.company} is {self.salary} \n {signature} ")
    @staticmethod
    def greet():
        print("good morning")


binod = Employee("Binod", 100030, "Youtube")
binod.getDetails()
# binod.salary = 10000
# binod.getSalary("Hello")
# binod.greet()