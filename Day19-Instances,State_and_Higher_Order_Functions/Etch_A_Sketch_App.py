from turtle import Turtle, Screen

the_arrow = Turtle()


def move_forward():
    the_arrow.forward(10)


def move_back():
    the_arrow.back(10)


def turn_left():
    the_arrow.setheading(the_arrow.heading() + 10)


def turn_right():
    the_arrow.setheading(the_arrow.heading() - 10)


def clear_screen():
    the_arrow.clear()
    the_arrow.penup()
    # the_arrow.goto(0, 0)
    the_arrow.home()
    the_arrow.pendown()


screen = Screen()
screen.listen()
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="w", fun=move_forward)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
