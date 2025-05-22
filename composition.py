class Engine:
    def start(self):
        print("Engine has started.")

class Car:
    def __init__(self,engine):
        self.engine=engine

    def start_car(self):
        self.engine.start()    # accessing engine method via Car class

# creating engine object
my_engine=Engine()

# now passing engine object to the Car
my_car=Car(my_engine)

# now start the Car using Engine start method.
my_car.start_car()
