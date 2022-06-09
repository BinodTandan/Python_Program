# class Vector:
#     dimension1 = (2, 4)
#     dimension2 = (4, 6)

#     def __add__(self):
        
#         d1 = self.dimension1[0] + self.dimension2[0]
#         d2 = self.dimension1[1] + self.dimension2[1]
#         print(f"The sum of two dimensions of vectors is ({d1}, {d2})")
    
    
#     def __mul__(self):
        
#         d1 = self.dimension1[0] * self.dimension2[0]
#         d2 = self.dimension1[1] * self.dimension2[1]
#         print(f"The dot product of two dimensions of vectors is ({d1}, {d2})")

# v = Vector()
# v.__add__()
# v.__mul__()

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"
        
    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])

        return Vector(newList)
    def __mul__(self, vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] * vec2.vec[i]

        return sum
    

v1 = Vector([1, 2, 4])
v2 = Vector([6,7,8])
print(v1+v2)
print(v1*v2)