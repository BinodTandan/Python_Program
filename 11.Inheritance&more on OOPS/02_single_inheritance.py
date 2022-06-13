#Base Class
class Employee:
    company = "Youtube"

    def showDetials(self):
        print("This is an employee")
#Child class
class Programmer(Employee):
    language = "Python"
    def getName(self):
        print(f"He is a {self.language} programmer")

# Method Over ridding
    def showDetials(self):
        print("This is python program")


emp = Employee()
emp.showDetials()
pro = Programmer()
pro.showDetials()
pro.getName()