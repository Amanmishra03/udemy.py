import turtle
import pandas

screen = turtle.Screen()
screen.title("Bharat state game")
image = ("bharat_state.gif.gif")
screen.addshape(image)
turtle.shape(image)
# data = pandas.read_csv("state.csv")
# all_state = data.state.to_list()
# guessed_states = []

def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

# while len(guessed_states)<50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct ",
#                                     prompt="what's another state's name").title()
#
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_state:
#             if state not in guessed_states:
#                 missing_states.append(state)
#                 print(missing_states)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states to learn")
#         break
#     if answer_state in all_state:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         # t.write(state_data.state.item())
#         t.write(answer_state)




screen.exitonclick()

