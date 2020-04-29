# Setters & Property Decorators python test project

#first Your print details
#2nd First Email
#3rd change email first name value
#4th function remove using property
#5th setter using and set the email
#6th setter delete


class A:
    def __init__(self,Name,LName):
        self.Name = Name
        self.LName = LName
        # self.email = f"{Name}{LName}@rajrahman.com"

    def snack(self):
        return  f"The Name is {self.Name} And The Roll is {self.LName}"

    @property
    def email(self):
        if self.Name == None or self.LName == None:
            return  "Deleted Successfully"
        return  f"{self.Name}{self.LName}@rajrahman.com"

    @email.setter
    def email(self,abc):
        fed = abc.split("@")[0]
        self.Name = fed.split(".")[0]
        self.LName = fed.split(".")[1]

    @email.deleter
    def email(self):
        self.Name = None
        self.LName = None

B = A("facebook","youtube")
print(B.Name,B.LName)
print(B.snack())

#2nd work
# print(B.email)

#3rd work
B.Name = "google"
B.LName = "twitter"
print(B.email)

#4th work
#done

#5th work
B.email = "nill.poriodhora@rajrahman.com"
print(B.email)

#6th work
del B.email
print(B.email)
