class Bank:
    bank_name= "ABC Bank"   # class varible, all bank object will use this name

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name= name         # cls is like self but it refer class not an object

bank1=Bank()
bank2=Bank()

print("Before change")
print(bank1.bank_name)
print(bank2.bank_name)


# change bank name using class method
print("\nAfter change:")
Bank.change_bank_name("Meezan Bank")
print(bank1.bank_name)
print(bank2.bank_name)  # both instance reflect the change bank name because they share class variable

