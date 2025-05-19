class Car:                      # this is the class body
    def __init__(self,brand):   # constructor of the class , which construc object
        self.brand=brand        # public variable

    def start(self):            # public method
        print(f"{self.brand} car is starting...")

c1=Car("Toyota")                # instantiate the class, create an object(an istance of the class)
 
# access the variable and method

print(c1.brand)                 # access public variable
c1.start()                      # access public method

            
