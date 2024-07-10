from turtle import Turtle
FONT = ("Courier", 10, "normal")


class ShowState(Turtle):
    def __init__(self):
        super().__init__()

    def show_move(self, name, x, y):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(name, align="center", font=FONT)

