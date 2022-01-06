from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
# Set playing area.
screen = Screen()
screen.setup(SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('My snake game.')
# Animation setting.
screen.tracer(0)
# Get input from user
screen.listen()
# Create starting snake.
snake = Snake()
food = Food()
border = Scoreboard()
scoreboard = Scoreboard()
scoreboard.score()


# Create snake control function
def on_key_move():
    """Triggers associated movement when the respective key is pushed."""
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")

    # Testing snake growth
    screen.onkey(snake.grow, "a")


playing = True
sleep_time = 0.11

while playing:
    screen.update()
    time.sleep(sleep_time)

    # Move the snake
    snake.move()
    # TODO:  Create a timer which will not conduct the move at least until the next frame (sleep_time).
    # Control the snake with key presses.
    on_key_move()
    # Detect food collision
    if snake.head.distance(food) < 15:
        food.place_food()
        snake.grow()
        scoreboard.score()
# Determine game over:
    # Collision with wall.
    if snake.head.xcor() > 485 or snake.head.xcor() < -485 or snake.head.ycor() > 451 or snake.head.ycor() < -481:
        playing = False
        scoreboard.game_over()
    # Collision with body.
    for part in snake.body[1:len(snake.body)]:
        if snake.head.distance(part) < 10:
            playing = False
            scoreboard.game_over()

screen.listen()
screen.exitonclick()
