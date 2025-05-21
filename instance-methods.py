class Dog:
    def __init__(self, name, breed):
        self.name= name
        self.breed= breed

    def bark(self):    #this is instance method because it uses instance object data(instance variable)
        print(f"My dog {self.name} says: bhao bhao.")   

my_dog = Dog("Tiger","German Shepherd")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()
