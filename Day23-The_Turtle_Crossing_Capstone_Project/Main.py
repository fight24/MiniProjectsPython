from turtle import Screen
from Player import Player
from ScoreBroad import ScoreBroad
from CarManager import CarManager

import time
WIDTH = 600
HEIGHT = 600
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
player = Player()
score_broad = ScoreBroad()
car_manager = CarManager()
screen.listen()
screen.onkeypress(player.move_up, "w")
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if player.distance(car) < 22:
            is_game_on = False
            print("collides")
            score_broad.game_over()
    if player.is_finish_y():
        player.refresh()
        score_broad.level_increase()
        car_manager.level_up()
screen.exitonclick()
