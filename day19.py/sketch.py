from turtle import Turtle , Screen
tim = Turtle()
my_screen = Screen()

def move_forw():
    tim.forward(10)
def move_back():
    tim.backward(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen.onkey(move_forw , "w")
my_screen.onkey(move_back, "s")
my_screen.onkey(turn_left, "a")
my_screen.onkey(turn_right, "d")
my_screen.onkey(clear, "e")



my_screen.listen()
my_screen.exitonclick()