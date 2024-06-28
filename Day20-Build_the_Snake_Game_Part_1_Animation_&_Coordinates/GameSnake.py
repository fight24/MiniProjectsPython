import time
from turtle import Screen

from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Game Snake")
screen.tracer(0)
#  Create a snake body
snake = Snake()
# Control the snake
screen.listen()
screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Move the snake
screen.exitonclick()

# TODO Control the snake
# TODO Detect collision with food
# TODO Create a scoreboard
# TODO Detect collision with wall
# TODO Detect collision with tail
