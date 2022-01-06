from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("red")
        self.speed(0)
        self.place_food()

    def place_food(self):
        """Puts food on a random position of the playable screen."""
        random_x = random.randint(-480, 480)
        random_y = random.randint(-480, 450)
        self.goto(random_x, random_y)
