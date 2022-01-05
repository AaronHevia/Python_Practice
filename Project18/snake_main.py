from turtle import Screen, Turtle
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


# Create starting snake body.
def create_body():
    """
    Creates the starting body for the snake.
    @return:  Returns the starting body.
    """
    x_position = [0, -20, -40]
    body = []
    for x in x_position:
        segment = Turtle('square')
        segment.penup()
        segment.color("white")
        segment.setx(x)
        body.append(segment)
    return body


snake = create_body()


# TODO:  Control the snake with key presses.
def on_key_move(element):
    def move_right(head):
        head.setheading(0)

    def move_up(head):
        head.setheading(90)

    def move_left(head):
        head.setheading(180)

    def move_down(head):
        head.setheading(270)

    screen.onkey(move_up, "w")
    screen.onkey(move_down, "s")
    screen.onkey(move_left, "a")
    screen.onkey(move_right, "d")


# TODO:  Move the snake.
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.25)

    for part in range(len(snake) - 1, 0, -1):
        # if part == snake[0]:
        #     on_key_move(snake[part])
        #     snake[part].forward(10)
        # else:
        front_x = snake[part - 1].xcor()
        front_y = snake[part - 1].ycor()
        snake[part].goto(front_x, front_y)

    snake[0].forward(20)




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
