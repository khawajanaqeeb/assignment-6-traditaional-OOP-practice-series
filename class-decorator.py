# first define class decorator

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"

    cls.greet=greet             # adding greeting method to the class
    return cls

# applying decorator to a class.

@add_greeting
class Person:
    def __init__(self,name):
        self.name=name

# now using class
p =Person("Mujtuba")
print(p.greet())    # it will print Hello from decorator!.

