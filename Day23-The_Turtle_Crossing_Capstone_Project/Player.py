from turtle import Turtle
STARTING_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black", "red")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POS)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_finish_y(self):
        if self.ycor() > FINISH_Y:
            return True
        return False

    def refresh(self):
        self.goto(STARTING_POS)
