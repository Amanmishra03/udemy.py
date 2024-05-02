from tkinter import *

window = Tk()

window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.place(x=100, y=200)


# Button
button = Button(text="Click me", command="button_clicked")
button.pack(side="left")

# Entry
input = Entry(width=10)
print(input.get())
input.pack(side="left")

window.mainloop()