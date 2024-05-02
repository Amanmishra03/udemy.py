from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodoro")   
windows.config(padx=100, pady=50)

Canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
Canvas.create_image(100, 112, image="tomato.png")
Canvas.pack()   


windows.mainloop()
 