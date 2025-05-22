class TemperatureConverter:


    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9 /5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (5/9)*(f-32)
    
c=float(input("Enter degree of celsius to be converted to Fahrenheit: "))
f=float(input("Enter degree of Fahrenheit to be converted to Calsius: "))
    
print(f"{TemperatureConverter.celsius_to_fahrenheit(c):.2f}")
print(f"{TemperatureConverter.celsius_to_fahrenheit(120):.2f}")

print(f"{TemperatureConverter.fahrenheit_to_celsius(f):.2f}")
print(f"{TemperatureConverter.fahrenheit_to_celsius(110):.2f}")

