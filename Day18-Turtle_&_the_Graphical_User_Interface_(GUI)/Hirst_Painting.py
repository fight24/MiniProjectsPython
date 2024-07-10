from colorgram import colorgram
import turtle as t
import random
colors = colorgram.extract("image.jpg", 12*7)
rbg_color = []
for color in colors:
    rbg_color.append(color.rgb)
print(f"RBG: {rbg_color}")
# Challenge
result = [(i.r, i.g, i.b) for i in rbg_color]
print(f"result: {result}")


def draw_dot():
    color_random = random.choice(result)
    the_turtle.color(color_random)
    the_turtle.dot(20, color_random)
# size of picture: 10 x 10, radius of dot 20, distance 50


t.colormode(255)
the_turtle = t.Turtle()
the_turtle.penup()
the_turtle.hideturtle()
the_turtle.goto(-250, 250)

for i in range(10):
    for j in range(10):
        draw_dot()
        if j < 9:
            the_turtle.forward(50)
    if i < 9 and i % 2 == 0:
        the_turtle.right(90)
        the_turtle.forward(50)
        the_turtle.right(90)
    if i < 9 and i % 2 != 0:
        the_turtle.left(90)
        the_turtle.forward(50)
        the_turtle.left(90)

# the_turtle.setheading(225)
# the_turtle.forward(300)
# the_turtle.setheading(0)
# num_of_dot = 100
# for dot_count in range(1, num_of_dot + 1):
#     the_turtle.dot(20, random.choice(result))
#     the_turtle.forward(50)
#     if dot_count % 10 == 0:
#         the_turtle.setheading(90)
#         the_turtle.forward(50)
#         the_turtle.setheading(180)
#         the_turtle.forward(500)
#         the_turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()
