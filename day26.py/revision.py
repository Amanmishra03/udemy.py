from turtle import Turtle, Screen
tim = Turtle()
my_screen = Screen()
num_sides = my_screen.numinput(title="No. of sides do you want", prompt="How many sides do you want")
num_sides = int(num_sides)
angle = 360/num_sides
for i in range(num_sides):
    tim.forward(100)
    tim.left(angle)


my_screen.exitonclick()