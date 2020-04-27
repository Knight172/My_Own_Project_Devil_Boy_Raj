#project 2 Multiple Inheritance

class raj:
    tomar = 4
    def __init__(self,Name,Roll,Address):
        self.Name = Name
        self.Roll = Roll
        self.Address = Address

    def ra1(self):
        return f"My Name is {self.Name} And My Roll is {self.Roll} And My Address Is {self.Address}"


raj_rahman = raj("Raj Rahman",14,"Dhaka,Bangladesh")
print(raj_rahman.Name,raj_rahman.Roll,raj_rahman.Address)

a = raj_rahman.ra1()
print(a)

class nill:
    tomar = 5
    nul = "Hello world"
    def prem(self):
        return (self.nul)

class nann(nill,raj):
  # tomar = 6
  pass

null = nill()
print(null.prem())

Durjoy = nann("Nill Pori Odhora",120,"Dhaka Bangladesh")
Durjoy.prem()


print(Durjoy.Name,Durjoy.Roll,Durjoy.Address)
print(Durjoy.prem())

detta = Durjoy.tomar
print(detta)
