class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self,name,employee):
        self.name=name
        self.employee=employee          # this is aggregation , just a refrence

    def show_department(self):
        print(f"Department Name: {self.name}")  
        self.employee.show()            # accessing employee method

# creating an employee
emp1=Employee("Jawaid")
emp2=Employee("Imran")


# creating department with the existing employee
dep1=Department("Sales",emp1)

dep2=Department("Accounts",emp2)

# showing department details including employee
dep1.show_department()
dep2.show_department()
