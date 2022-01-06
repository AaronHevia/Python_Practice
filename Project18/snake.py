from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
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
        self.head.color('dark green')

    def create_snake(self):
        """Creates the starting body for the snake."""
        for position in STARTING_POSITIONS:
            self.add_body_part(position)

    def add_body_part(self, position):
        """Builds a body part and places it in desired position."""
        segment = Turtle('square')
        segment.color('green')
        segment.penup()
        segment.goto(position)
        self.body.append(segment)

    # Grow the snake.
    def grow(self):
        """Adds a body part to the snake after eating food."""
        self.add_body_part(self.body[-1].position())

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


