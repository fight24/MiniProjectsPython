from turtle import Turtle, Screen

the_turtle = Turtle()
screen = Screen()


def move_forwards(s):
    the_turtle.forward(s)


screen.listen()
screen.onkey(key="space", fun=move_forwards(10))
screen.exitonclick()