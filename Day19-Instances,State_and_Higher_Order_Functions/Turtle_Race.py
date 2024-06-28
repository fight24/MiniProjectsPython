from turtle import Turtle, Screen
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a colour:")


def create_turtle(c, position_y):
    new_turtle = Turtle(shape="turtle")
    new_turtle.hideturtle()
    new_turtle.color(c)
    new_turtle.penup()
    new_turtle.goto(x=-240, y=position_y)
    new_turtle.showturtle()
    return new_turtle


if guess:
    is_race_on = True
turtles = []
y = -70
for color in colors:
    turtles.append(create_turtle(color, y))
    y += 30
while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            if t.pencolor() == guess:
                print(f"You 've won! The {t.pencolor()} turtle is the winner!")
            else:
                print(f"You 've lost! The {t.pencolor()} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        t.forward(rand_distance)
screen.exitonclick()
