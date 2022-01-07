from turtle import Turtle

UP = 90
DOWN = 270
MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, starting_position, upper_bound, lower_bound):
        super(Paddle, self).__init__()
        self.starting_position = starting_position
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.body = []
        self.create_paddle(starting_position)

    def create_paddle(self, position):
        """Creates a paddle at a starting position."""
        x = position[0]
        y = position[1]
        for i in range(5):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(x, y)
            self.body.append(segment)
            y += 20

    def move(self):
        """Sets the move speed of the paddle"""
        for part in self.body:
            part.forward(MOVE_DISTANCE)

    def move_up(self):
        """Moves the paddle up."""
        if self.body[-1].ycor() < self.upper_bound:
            if self.body[0].heading() != UP:
                for part in self.body:
                    part.setheading(UP)
            self.move()

    def move_down(self):
        """Moves the paddle down."""
        if self.body[0].ycor() > self.lower_bound:
            if self.body[0].heading != DOWN:
                for part in self.body:
                    part.setheading(DOWN)
            self.move()
