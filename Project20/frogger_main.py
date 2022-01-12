import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


def on_key_move():
    """Triggers associated movement when the respective key is pushed."""
    screen.onkeypress(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")
    screen.onkeypress(player.move_left, "Left")
    screen.onkeypress(player.move_right, "Right")


playing = True
while playing:
    time.sleep(0.1)
    screen.update()
    on_key_move()
    car_manager.create_car()
    car_manager.move()

    if player.ycor() > 280:
        player.clear()
        player.create_turtle()
        scoreboard.level_up()
        car_manager.increase_speed()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            playing = False
            scoreboard.game_over()

screen.exitonclick()
