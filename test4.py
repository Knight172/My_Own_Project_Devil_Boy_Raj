#Public, Private & Protected Access test python project 04

class raj: #public
    r1 = 10
    def __init__(self,Name):
        self.Name = Name

class ridita: #protected
    _r2 = 20
    def s1(self):
        return f"My Name is {self.Name}"

class nill: #Private
    __r3 = 30
    def s2(self):
        return  f"Your Name is{self.Name}"



#Print All Details
i1 = raj("Raj Rahman")#public print
print("Your Name: ",i1.Name)
ah1 = raj.r1 #public veriable
print("Public Veriable: ",ah1)



i2 = ridita()#protected print
i2.Name = "Ridita Islam"
print("My Name Is: ",i2.s1())
print("Protected Veriable: ",ridita._r2)


i3 = nill()#private print
i3.Name = "Nill Pori Odhora"
print(i3.Name)
print(i3._nill__r3)


