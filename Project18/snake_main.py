from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time
import keyboard

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SLEEP_TIME = 0.11
# Set playing area.
screen = Screen()
screen.setup(SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('My snake game.  Press "X" to exit or ARROWS to control the snake.')
# Animation setting.
screen.tracer(0)
# Create starting snake.
snake = Snake()
food = Food()
# Create scoreboard and boundaries.
border = Scoreboard()
border.draw_border()
scoreboard = Scoreboard()
scoreboard.score()

# Get input from user
screen.listen()


# Create snake control function
def on_key_move():
    """Triggers associated movement when the respective key is pushed."""
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")


on_key_move()

playing = True


def exit_game():
    global playing
    playing = False
    scoreboard.game_over()


while playing:
    screen.update()
    time.sleep(SLEEP_TIME)
    # Move the snake
    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.place_food()
        snake.grow()
        scoreboard.score()
# Determine game over:
    # Collision with wall.
    if snake.head.xcor() > 485 or snake.head.xcor() < -485 or snake.head.ycor() > 451 or snake.head.ycor() < -481:
        scoreboard.reset_score()
        snake.reset_snake()
    # Collision with body.
    for part in snake.body[1:]:
        if part == snake.head:
            pass
        elif snake.head.distance(part) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

    screen.onkey(exit_game, 'x')

screen.exitonclick()
