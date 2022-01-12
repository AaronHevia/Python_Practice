from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.speed('fastest')
        self.penup()
        self.level = 1
        self.display_level()

    def game_over(self):
        """Creates Game Over message."""
        self.goto(0, 0)
        self.write(arg="Game Over", font=FONT, align="center")

    def level_up(self):
        """Calculates level player is on."""
        self.level += 1
        self.display_level()

    def display_level(self):
        """Writes the score along the upper edge of the screen."""
        self.clear()
        self.goto(-220, 265)
        self.write(arg=f"Level: {self.level}", font=FONT, align="center")