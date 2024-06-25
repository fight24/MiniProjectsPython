# ####Turtle Intro######


# import turtle as t
# timmy_the_turtle = t.Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.backward(200)
# timmy_the_turtle.right(90)
# timmy_the_turtle.left(180)
# timmy_the_turtle.setheading(0)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, b, g
# # ####### Challenge 1 - Draw a Square ############

# tim.shape("arrow")
# tim.color("black", "red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# screen = tim.Screen()
# screen.exitonclick()


# ########## Challenge 2 - Draw a Dashed Line ########
# for _ in range(10):
#     tim.color("black")
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
# tim.shape("arrow")
# tim.color("black")
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# screen = t.Screen()
# screen.exitonclick()

# Turtle Challenge 3 - Drawing Different Shapes
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
#            "SeaGreen"]
#
# for i in range(3, 11):
#     tim.color(random.choice(colours))
#     angle = 360 / i
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(angle=angle)
# screen = t.Screen()
# screen.exitonclick()

# ########## Challenge 4 - Random Walk ########
# directions = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(0)
# for _ in range(200):
#     tim.pencolor((random_color()))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#
# screen = t.Screen()
# screen.exitonclick()
# ########## Challenge 5 - Spirograph ########
tim.speed(0)
# current_heading = tim.heading()
# while current_heading <= 360:
#     tim.color((random_color()))
#     tim.circle(100)
#     current_heading += 10
#     tim.setheading(current_heading)


def draw_spirograph(size_of_gap):
    # for _ in range(int(360/size_of_gap)):
    #     tim.color((random_color()))
    #     tim.circle(100)
    #     tim.setheading(tim.heading() + size_of_gap)
    current_heading = tim.heading()
    while current_heading <= 360:
        tim.color((random_color()))
        tim.circle(100)
        current_heading += size_of_gap
        tim.setheading(current_heading)


draw_spirograph(5)
screen = t.Screen()
screen.exitonclick()

# # Di chuyển rùa đến vị trí bắt đầu
# t.penup()
# t.goto(0, 0)  # Vị trí bắt đầu tại tọa độ (0, 0)
# t.pendown()
#
# # Đổi hướng rùa xuống dưới
# t.setheading(270)  # 270 độ là hướng xuống dưới
#
# # Vẽ đường tròn với bán kính 50
# t.circle(50)
#
# # Kết thúc chương trình khi nhấn vào cửa sổ

