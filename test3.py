#Multilevel Inheritance The Test of my python 
#writer: Raj Rahman

class GrandFather:
    a = 100
    b = 101

class Father(GrandFather):
    def r1(self):
        return f"The Name is a {self.Name} And The Roll is {self.Roll}"

class Son(Father):
    def __init__(self,Name,Roll):
        self.Name = Name
        self.Roll = Roll


ab = Son("Raj Rahman",132)
bc = Father()
ab.a
ab.b

bc.Name = "Nill Pori Odhora"
bc.Roll = 101
ib = bc.r1()
print(ib)

print(ab.a,ab.b)
print(ab.Name,ab.Roll)






