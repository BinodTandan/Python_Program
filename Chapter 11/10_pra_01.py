class C2dvector:
    

    def __init__(self, i ,j):
        self.icap = i
        self.jcap= j
        
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dvector(C2dvector):
    def __init__(self, i ,j, k):
        super().__init__(i, j)
        self.kcap= k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


v0 = C2dvector(11,15)
v = C3dvector(12, 11, 10)
print(v0)
print(v)