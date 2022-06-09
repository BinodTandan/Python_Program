class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
        
    def __add__(self, vec2):
            if len(self.vec)==len(vec2.vec):
                print("Both dimensions have same lenght ")
                newList = []
                for i in range(len(self.vec)):
                    newList.append(self.vec[i] + vec2.vec[i])

                return Vector(newList)
            else:
                print("Both dimensions have different length")
        
    def __mul__(self, vec2):
        if len(self.vec)==len(vec2.vec):
                print("Both dimensions have same lenght ")
                sum = 0
                for i in range(len(self.vec)):
                    sum += self.vec[i] * vec2.vec[i]
                return sum
        else:
            print("Both dimensions have different length")

    def __len__(self):
        return len(self.vec)
    
v1 = Vector([1, 2, 4])
v2 = Vector([6,8, 6])
print(v1+v2)
print(v1*v2)
