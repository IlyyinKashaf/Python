import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=500)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.go_up , "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create()
    cars.move()

    for car in cars.cars:
        if car.distance(player) < 20:
            game_is_on = False
            player.game_over()

    if player.finish():
        player.origin()
        cars.levelup()
        score.inc_level()





screen.exitonclick()

    
