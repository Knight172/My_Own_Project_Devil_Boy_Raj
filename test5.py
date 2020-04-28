#super veriable test python project 05

class A:
    mane = "I am in class A"
    def __init__(self):
        self.Name = "Hello World I am in class A"
        self.ab = "Hey Guy How Are You A"
        self.nahid = "I am a nahid"

class B(A):
    ab = "I am in class B"
    def __init__(self):
        self.Name = "Hello World I am in class B"
        self.ab = "Hey Guy How Are You B"
        super().__init__()

C = B()
print(C.nahid)
