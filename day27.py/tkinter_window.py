import tkinter

window = tkinter.Tk()

window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.pack(expand=True)
# my_label.pack(side="bottom")


import turtle
tim = turtle.Turtle()
tim.write("Some text", align="center", font=("Arial", 24, "normal"))



window.mainloop()