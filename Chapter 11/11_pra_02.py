
class Animals:

    def __init__(self):
        print("There are different types of animals")


class Pets(Animals):
    type = "Domestic"

    def __init__(self):
        super().__init__()
        print("There are varities of pets")

    

class Dogs(Pets):


    def __init__(self):
        super().__init__()
        print("There are varities of dogs")
    
    def barkDog(self, type):
        self.type = type
        return f"{self.type} dog barks at night"


d = Dogs()
d.type = "German shepard"
print(d.type)
print(d.barkDog("Black"))
