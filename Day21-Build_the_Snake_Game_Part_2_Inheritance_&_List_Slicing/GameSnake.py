import time
from turtle import Screen
from Food import Food
from Snake import Snake
from ScoreBroad import ScoreBroad
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Game Snake")
screen.tracer(0)
#  Create a snake body
snake = Snake()

food = Food()
#  Create a scoreboard
score_broad = ScoreBroad()
# Control the snake
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_broad.increase_score()
    #  Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_broad.game_over()
        game_is_on = False
        print("Detect collision with wall")
    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score_broad.game_over()
            print("Detect collision with tail")
screen.exitonclick()





