
class Programmer:
    company = "Microsoft"
    salary = 199909
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def getDetials(self):
        print(f"The name of programmer is {self.name} of age {self.age} having salary {self.salary} \n woring for a {self.company} ")
        


binod = Programmer("Binod", 24, 5000000)

binod.getDetials()

ha = Programmer("Hari", 34, 50599959)
ha.getDetials()




