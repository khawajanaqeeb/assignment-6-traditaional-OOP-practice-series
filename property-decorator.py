class Product:
    def __init__(self,price):
        self._price = price         # private attribute

    @property               # it's a decorator. it's a getter
    def price(self):
        print("Getting Price...")
        return self._price

    # creating price setter
    @price.setter
    def price(self,new_price):
        print("Setting Price...")
        if new_price < 0:
            raise ValueError("Price can not be negative!")
        self._price = new_price

    # price deleter
    @price.deleter
    def price(self):
        print("Deleting Price...")
        del self._price

# testing the class
p=Product(100)

# call getter
print(p.price)

# call setter
p.price=200
print(p.price)

# check negative value
try:
    p.price=-69
except ValueError as e:
    print(e)    

# price deleter
del p.price

