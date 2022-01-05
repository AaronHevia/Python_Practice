from turtle import Screen, Turtle
from snake import Snake
import scoreboard
import food
import time

# Set playing area.
screen = Screen()
screen.setup(width=1000, height=900)
screen.bgcolor('black')
screen.title('My snake game.')
# Animation setting.
screen.tracer(0)
# Get input from user
screen.listen()
# Create starting snake.
snake = Snake()


# Create snake control function
def on_key_move():
    """Triggers associated movement when the respective key is pushed."""
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.25)
    # Move the snake
    snake.move()
    # Control the snake with key presses.
    on_key_move()


# TODO:  Detect collision with food.

# TODO:  Grow the snake.
def add_body(snake_list):
    """
    Adds a body part to the snake.
    @param snake_list: An array of turtle objects.
    @return: Returns the modified snake_list.
    """

    body = Turtle()
    body.penup()
    body.shape("square")
    snake.append(body)
    return snake


# TODO:  Create a scoreboard.

# TODO:  Determine game over:
# TODO:  Detect collision with wall.
# TODO:  Detect collision with tail.

screen.listen()
screen.exitonclick()
