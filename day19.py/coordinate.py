from turtle import Turtle , Screen
import random
my_screen = Screen()
my_screen.setup(width = 500, height=400)
user_bet = my_screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange","yellow","green","blue","purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    

if user_bet:
    is_race_on = True


while is_race_on:
    rand_distance = random.randint(0, 10)
    tim.forword(rand_distance)
    tim.forward(rand_distance)


my_screen.exitonclick()