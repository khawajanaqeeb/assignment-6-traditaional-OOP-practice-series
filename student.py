class Student:
    def __init__(self, name, age, grade):
        self.name=name
        self.age=age
        self.grade=grade

    def display_info(self):
        print(f"Student Name:{self.name}, Student Age: {self.age} , Student Grade: {self.grade}")

student1=Student("Danish",14 ,"A")
student2=Student("Kamran",15 ,"B")

student1.display_info()
student2.display_info()

