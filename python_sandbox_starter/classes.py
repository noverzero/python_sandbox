# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class

class User:
    #constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'Hello. My name is, {self.name} and I am {self.age} years old.'

    def has_birthday(self):
        self.age += 1

#Init user object
dustin = User('Dustin Huth', 'dustin@gmail.com', 40)

dustin.has_birthday()
print(dustin.greeting()) 

# Extend class

class Customer(User):
    def set_balance(self, balance):
        self.balance = balance

brent = Customer('Brent Ivanhoe', 'brent@gmail.com', 48)
brent.set_balance(100)
print(brent.greeting(), brent.balance)