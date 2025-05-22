# first define decorator
def log_function_call(func):
    def wrapper():
        print("Function is being called.")
        func()
    return wrapper    

# now define the function to decorate
@log_function_call
def say_hello():
    print("Hello!")

# now call decoratored function
say_hello()
