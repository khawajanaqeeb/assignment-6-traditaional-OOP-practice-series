class Employee:
    def __init__(self, name, salary, ssn):
        self.name=name                  # public
        self._salary=salary             # private
        self.__ssn=ssn                  # protected 

# creating an object
emp1= Employee("Zahid",50000,"123-45-678")

# trring accessing each vaiable
print("Name:",emp1.name)
print("Salary:", emp1._salary)
print("SSN:",emp1.__ssn)



