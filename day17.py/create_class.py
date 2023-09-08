''' Class :- for creating class we have a class keyword followed by the name of the class and then a colon and then 
all of the code in your class follow this and will be indented. in class all the first letter with capital letter without any space. '''
''' in python whenever we use the colon in function then python want identation if we want nothing to write then 
we have to simply write (pass) at the indentation  '''

class user:
    
    
    def __init__(self):
        print("new user being created...")

user_1 = user()
# how to create an attribute
user_1.id = "001"
user_1.username = "angela_madam"
print(user_1.username)
# Attribute is a variable associated with an object. here user_1 is an object

user_2 = user()
user_2.id = "002"
user_2.username = "jack"
print(user_2.username)