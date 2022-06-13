class Brands:
    product = "Shoes"

    def __init__(self):
        print("I am a brand")

    def shoeName(self):
        
        print("The name of popular shoe brand of our country is Goldstar")

class Branch(Brands):
    country = "Nepal"
    def __init__(self):
        super().__init__()
        print("I am a branch")
    def shoeName(self):
        super().shoeName()
        print(f"The name of popular shoe is Goldstar")



class Salesman(Branch):
    def personDetials(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of salesman is {self.name} having salary {self.salary}")
        
    def shoeName(self):
        super().shoeName()
        print("The name of popular is Goldstar")

# b = Brands()
# b.shoeName()
# bn = Branch()
# bn.shoeName()
# s = Salesman()
# s.shoeName()
s = Salesman()

