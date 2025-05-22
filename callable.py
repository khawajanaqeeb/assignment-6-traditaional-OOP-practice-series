class Multiplier:
    def __init__(self,factor):
        self.factor=factor          # storation of multiplication factor

    def __call__(self,number):
        return number * self.factor

# creating instance with factor
m=Multiplier(6)


# using callable() to check it is callable.
print("Is m callable",callable(m))

# now call it like a function
result=m(30)
print("Resutl of m(30)",result)
