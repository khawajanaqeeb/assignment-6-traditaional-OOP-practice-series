class Person:
    def __init__(self,name):
        self.name=name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)          # calling base (parent)class constructor
        self.subject= subject           # own class subject field added

# creating Teacher class object

t1= Teacher("Khalid","Physic")

# accessing both fields

print("name:",t1.name)
print("subject:",t1.subject)
