#Diamond Shape Problem In Multiple Inheritance test in python

class A:
    def raj(self):
        print("How Are You")

class B(A):
   def raj(self):
       print("I am a good")

class C(A):
    def raj(self):
        print("I am a good C")

class D(C,B):
    def raj(self):
        print("I am a good D")

a = A()
b = B()
c = C()
d = D()

d.raj()

