#the game
class maen():
    def __init__(self,Name,Roll):
        self.Name = Name
        self.Roll = Roll

    def r1(self):
        return f"Hello Facebook Team My Name is {self.Name} And My Roll is {self.Roll} Please verified my account as soon as possible \nThank You \n{self.Name}\n{self.Roll}"




class lpi(maen):
    raj = maen("Raj Rahman",12)
    ridita = maen("Obsora Sultana Ridita",13)
    m = ridita.r1()
    #print all the detils
    print(raj.Name,raj.Roll)
    print(ridita.Name,ridita.Roll)
    print("\n")
    print(m)

class lip:
    ar = "Dhaka,Bangladesh"
    def __init__(self,Name,Register):
        self.Name = Name
        self.Register = Register

    def ra(self):
        return f"Hello My Dear {self.Name} How Are You. What is your {self.Register} Thank you\n{self.Name}\n{self.Register}"

    @classmethod
    def world(cls,Name):
        cls.ar = Name

    @staticmethod
    def finish():
        print("---------------------------------------")
        return "Finish Now Thank You So Much Guys"

raj = lip("Nill Pori Odhora",145263)
ridita = lip("Obsora Sultana Ridita",14512)
print("\n")
print("<--------------------->")
print("Name: ",raj.Name,"\nRegister",raj.Register)
print("\t")
print("Name: ",ridita.Name,"\nRegister",ridita.Register)

print("<--------------->")
taka = raj.ra()
print(taka)
class lap(lip):
    # raj.ar = "Noakhali, Bangladesh"
    # print(raj.__dict__)
    # print(lip.ar)
    raj.world("Noakhali,Bangladesh")
    print(lip.ar)
    print(lip.finish())



