from turtle import Turtle, Screen
from player import Player
from cars import Cars
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Cars()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "Up")

# car.create_car()

game_is_on = True
while game_is_on:
    # cars.append(car.create_car())
    screen.update()
    time.sleep(.1)
    car.create_car()
    car.move_car()

    for i in car.all_cars:
        if i.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    if player.is_at_finish_line():
        player.go_origin()
        car.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

# cars = []
# for i in range(10):
#     cars.append(car.create_car())



screen.exitonclick()