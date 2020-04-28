#Operator Overloading & Dunder Methods test in python

class A:
    def __init__(self,Name,Seleary,Subject):
        self.Name = Name
        self.Seleary = Seleary
        self.Subject = Subject

    def raj(self):
        return f"The Name is {self.Name} And The Seleary Is {self.Seleary}  And The Subject is {self.Subject}"

    def __add__(self, other):
       return self.Seleary + other.Seleary

    def __truediv__(self, other):
        return self.Seleary / other.Seleary

    def __floordiv__(self, other):
       return self.Seleary // other.Seleary

    def __or__(self, other):
        return other.Seleary | self.Seleary

    def __pow__(self, power, modulo=None):
        return self.Seleary ** power.Seleary

    def __lshift__(self, other):    # akane sob golo 2 ar sate jok hoy jemon 2*2 = 4  and 2*2*2 = 8
        return  self.Seleary << other.Seleary

    def __rshift__(self, other):
        return  self.Seleary >> other.Seleary

    def __mod__(self, other):
        return  self.Seleary % other.Seleary

    def __mul__(self, other):
        return  self.Seleary * other.Seleary

    def __matmul__(self, other):
        return  self.Name @ other.Name

    def __pos__(self):
        return self.Seleary

    def __sub__(self, other):
       return self.Seleary - other.Seleary

    def __lt__(self, other):
        return  self.Seleary < other.Seleary

    def __le__(self, other):
        return  self.Seleary<= other.Seleary

    def __eq__(self, other):
        return  self.Seleary==other.Seleary

    def __ne__(self, other):
        return  self.Seleary != other.Seleary

C = A("Raj Rahman",150,"Computer")
D = A("Ridia Islam",15,"Computer")
print(C != D)

