class Brands:
    product = "Shoes"

    def shoeName(self, name):
        self.name = name
        print(f"The name of popular shoe brand of our country is {self.name}")

class Branch(Brands):
    country = "Nepal"


class Salesman(Branch):
    def personDetials(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"The name of salesman is {self.name} having salary {self.salary}")

s = Salesman()
s.shoeName("Goldstar")
s.personDetials("Ram", 16000)
print(s.country)