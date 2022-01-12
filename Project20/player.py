from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.create_turtle()

    def create_turtle(self):
        """Creates the turtle at a starting position."""
        self.shape('turtle')
        self.color('dark green')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(UP)

    def move(self):
        """Moves the turtle a certain distance."""
        self.forward(MOVE_DISTANCE)

    def move_up(self):
        """Moves the turtle up."""
        self.setheading(UP)
        self.move()

    def move_down(self):
        """Moves the turtle down."""
        self.setheading(DOWN)
        if self.ycor() > -280:
            self.move()

    def move_left(self):
        """Moves the turtle left."""
        self.setheading(LEFT)
        if self.xcor() > -280:
            self.move()

    def move_right(self):
        """Moves the turtle right."""
        self.setheading(RIGHT)
        if self.xcor() < 270:
            self.move()
