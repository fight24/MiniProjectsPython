import time
from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from ScoreBroad import ScoreBroad
# TODO crete screen
WIDTH = 800
HEIGHT = 600
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Game Pong")
screen.tracer(0)
# TODO create and move paddle
paddle_l = Paddle((-350, 0))
screen.listen()
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")
# TODO create other paddle
paddle_r = Paddle((350, 0))
screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
# TODO create ball and make it move
ball = Ball()
# TODO keep score broad
score_broad = ScoreBroad()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.speed_move)
    ball.move()
    # TODO detect collision with wall and bounce: phát hiện va chạm với tường và nảy
    if ball.ycor() > 270 or ball.ycor() < -270:
        # need to bounce
        ball.bounce_y()
    # TODO detect collision with paddle : phát hiện va chạm với mái chèo
    if (ball.distance(paddle_r) < 40 and ball.xcor() > 320) or (ball.distance(paddle_l) < 40 and ball.xcor() < -320):
        ball.bounce_x()
        print("contact")
    # TODO detect when paddle misses
    if ball.xcor() > 420:
        print("paddle right miss")
        ball.refresh_ball()
        score_broad.l_score_update()
    if ball.xcor() < -420:
        print("paddle left miss")
        ball.refresh_ball()
        score_broad.r_score_update()
screen.mainloop()


