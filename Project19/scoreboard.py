from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, y_coordinate):
        super(Scoreboard, self).__init__()
        self.y_coordinate = y_coordinate
        self.hideturtle()
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.p1_points = 0
        self.p2_points = 0

    def game_over(self):
        """Creates Game Over message."""
        self.goto(0, 0)
        self.write(arg="Game Over", font=('Arial', 30, 'bold'), align="center")

    def p2_score(self):
        """Calculates player 2 score."""
        self.p2_points += 1
        self.update_scoreboard()

    def p1_score(self):
        """Calculates player 1 score."""
        self.p1_points += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """Writes the score along the upper edge of the screen.  Color changes depending on the amount of points."""
        self.clear()
        self.goto(-100, self.y_coordinate)
        self.write(arg=f"{self.p1_points}", font=('Arial', 20, 'bold'), align="center")
        self.goto(100, self.y_coordinate)
        self.write(arg=f"{self.p2_points}", font=('Arial', 20, 'bold'), align="center")

    def draw_boundaries(self):
        self.draw_half_court()
        self.draw_top_border()

    def draw_top_border(self):
        """Draws the uppermost border of playing field."""
        self.penup()
        self.goto(-960, 500)
        self.pendown()
        self.goto(960, 500)
        self.penup()

    def draw_half_court(self):
        """Draws the half court line."""
        self.goto(0, self.y_coordinate)
        self.pendown()
        self.setheading(90)
        while self.ycor() < 495:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

