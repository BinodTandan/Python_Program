class Employee:
    company = "Microsoft"

class Freelancer:
    company = "Google"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = " BINOD"

p = Programmer()
print(p.company)
p.upgradeLevel()
print(p.level)
