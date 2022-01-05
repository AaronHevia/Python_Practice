from turtle import Turtle

STARTING_X_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        """Creates the starting body for the snake."""
        for x in STARTING_X_POSITIONS:
            segment = Turtle('square')
            segment.penup()
            segment.color("white")
            segment.setx(x)
            self.body.append(segment)

    def move(self):
        """Moves the snake towards the direction of the head."""
        for part in range(len(self.body) - 1, 0, -1):
            front_x = self.body[part - 1].xcor()
            front_y = self.body[part - 1].ycor()
            self.body[part].goto(front_x, front_y)
        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        """Moves the head of the snake right if it is not facing left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        """Moves the head of the snake up if it is not facing down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_left(self):
        """Moves the head of the snake left if it is not facing right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_down(self):
        """Moves the head of the snake down if it is not facing up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Grow the snake.
    def grow(self):
        """Adds a body part to the snake."""
        x = self.body[-1].xcor()
        y = self.body[-1].ycor()
        body = Turtle()
        body.penup()
        body.shape("square")
        body.setposition(x, y)
        body.color("white")
        self.body.append(body)
