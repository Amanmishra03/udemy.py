from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
    
    def move(self):
        new_x = self.xcor() + 10