# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
  #constrcutor
  def __init__(self, name, email, age):
    self.name = name 
    self.email = email
    self.age = age 

  def greetings(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age +=1

#init user object 
brad = User('Brad Traversy', 'brad@gmail.com', 37)

#edit property 
brad.age = 38

print(brad.name)

print(brad.age)

print(brad.greetings())

print(brad.has_birthday())

print(brad.greetings())

  
class Customer(User):
  def __init__(self, name, email, age):
    self.name = name
    self.email = email 
    self.age = age 
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance 

  def greetings(self):
    return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

#Init customer 
cust1 = Customer('Joh Doe', 'john@gmail.com', 40)

print(cust1.name)

cust1.set_balance(500)

print(cust1.greetings())