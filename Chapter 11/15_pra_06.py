class Vector:

    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i^+{self.vec[1]}j^+{self.vec[2]}k^"

v = Vector([22,33,44])
print(v)
