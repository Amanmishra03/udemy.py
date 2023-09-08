'''NOTE_1 :- In Python, an object is an instance of a class. A class is a blueprint or template
             that defines the attributes and methods of an object.
             To create an object, you first define a class. Here is an example of a simple class definition:'''
class MyClass:
    pass

# This class doesn't do anything yet. To create an object of this class, you simply call the class like a function:
my_object = MyClass()
# Now my_object is an instance of the MyClass class. You can access its attributes and methods using dot notation:
my_object.some_attribute = 42
print(my_object.some_attribute)
# You can also define methods in a class. Here is an example:
class MyClass:
    def __init__(self):
        self.some_attribute = 42
    
    def some_method(self):
        print("Hello, world!")
''' The __init__ method is a special method that is called when an object is created. 
It is used to initialize the object's attributes. The some_method method just prints a message.'''

# To create an object of this class and call its methods:




# suppose a waiter  what the waiter has is its Attribute and what waiter does is his Method
''' Attribute :- attribute is basically a variable.
                 attribute is a just a fancy word for a variable 
                 which is associated with a modeled object.'''
# Method :- it is just a function of modeled object
my_object = MyClass()
my_object.some_method()  # prints "Hello, world!"



class Employee:
    id = 10
    name = "john"
    def display (self):
        print("id : " ,self.id)
        print("name : " , self.name)
# create object of class employee
emp = Employee()
emp.display()