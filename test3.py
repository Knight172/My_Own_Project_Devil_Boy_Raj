class son:
    a = 9

class dad(son):
    def ridita(self,Name):
       self.Name = Name

class grandfather(dad):
     def __init__(self,Name):
        self.fname = Name


ab = grandfather("Raj Rahman")
ab.a
print(ab.a)
ab.Name = "Ridita Islam"
print(ab.Name)
print(ab.fname)
