from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.points = -1
        self.draw_border()

    def draw_border(self):
        """Draws the uppermost border of playing field."""
        self.speed('fastest')
        self.goto(-500, 455)
        self.pendown()
        self.goto(500, 455)
        self.penup()

    def score(self):
        """Writes the score along the upper edge of the screen.  Color changes depending on the amount of points"""
        self.points += 1

        if self.points > 10:
            self.pencolor('cyan')
        if self.points > 20:
            self.pencolor('lime')
        if self.points > 30:
            self.pencolor('yellow')
        if self.points > 40:
            self.pencolor('orange')
        if self.points > 50:
            self.pencolor('red')

        self.clear()
        self.goto(0, 460)
        self.write(arg=f"Score:  {self.points}", font=('Arial', 20, 'bold'), align="center")

    def game_over(self):
        """Creates Game Over message."""
        self.goto(0, 0)
        self.write(arg="Game Over", font=('Arial', 30, 'bold'), align="center")
