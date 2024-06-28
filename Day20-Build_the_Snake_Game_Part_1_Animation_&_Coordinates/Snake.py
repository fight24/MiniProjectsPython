from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        self.segments = [self.create_square(x_pos, y_pos) for x_pos, y_pos in START_POS]

    @staticmethod
    def create_square(x, y):
        new_square = Turtle(shape="square")
        new_square.shapesize(1)
        new_square.penup()
        new_square.color("white")
        new_square.goto(x, y)
        return new_square

    def move(self, angle):
        for seg_num in range(2, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.setheading(angle)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.move(UP)

    def down(self):
        if self.head.heading() != UP:
            self.move(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.move(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.move(RIGHT)
