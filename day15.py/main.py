from turtle import Turtle , Screen
''' here turtle is a module and from turtle module we take a class Turtle and another class Screen 
    but jab tak ham object define nhi krte tab tak class kaam nhi karega isliye hmko object define krna padega'''
# the object for class Turtle is 
timmy = Turtle()
print(timmy)
# the code written below is called method timmy is object .shape is method
timmy.shape("turtle")
timmy.color("red")


'''for class Screen we have to create object of class screen taki class work kr ske
 kyoki class object ke bina work nhi krta '''
my_screen = Screen()

# for create attribute write object. and then attribute for example
print(my_screen.canvheight)
# here my_screen.canvheight is an attribute

# for method 
my_screen.exitonclick()
# this is a method 

