class A:
    def show(self):
        print("Showing method from class A")

class B(A):                 # inherit from A but orver-ride it
    def show(self):
        print("Showing method from class B")

class C(A):                 # inherit from A but over-ride it
    def show(self):
        print("Showing method from class C")    

class D(B,C):               # inherit from B first then C but not over-ride any of them.
    pass                    # if we change the order like (C,B then) D first check C.

# creating object of D.
d=D()
d.show()

# printing MRO of class D.(method resolution order)
print(D.__mro__)            

