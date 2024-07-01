from turtle import Turtle

DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)  # Height=100, Width=20
        self.color("white")
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + DISTANCE
        self.goto(self.xcor(), new_y)
        print(f"UP - new y:{new_y}")

    def down(self):
        new_y = self.ycor() - DISTANCE
        self.goto(self.xcor(), new_y)
        print(f"Down - new y:{new_y}")



