#Abstract Base Class & @abstractmethod Python Test

from  abc import ABC,abstractmethod

class C(ABC):
    @abstractmethod
    def raj(self):
        return 0

class A():
    def __init__(self):
        self.height = 20
        self.weight = 30

    def raj(self):
        return  self.height + self.weight

class B(C):
    def __init__(self):
        self.a = 54
        self.b = 6
    def raj(self):
        return self.a + self.b

nill = A()
print(nill.raj())

ridita = B()
print("Your Class Name is : ",ridita.raj())

