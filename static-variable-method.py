class MathUtils:
    # Doesn’t take self or cls
    # Doesn’t access instance (self) or class (cls) variables
    @staticmethod
    def add(a,b):
        return a + b       # its clean and independent no class or instance(object)
    
# now calling MathUtils function directly beacue not depent on object or class

result=MathUtils.add(8 , 9)
print("Sum of two numbers using static method is:", result)

