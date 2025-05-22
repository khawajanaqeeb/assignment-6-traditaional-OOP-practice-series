
# custom exception.
class InvalidAgeError(Exception):
    pass

# function to check age
def check_age(age):
    if age <18 :
        raise InvalidAgeError("Age must be atleast 18.")
    else:
        print("Access granted.")
    
    
try:
    user_age=int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
        print("Custom exception caught:",e)


