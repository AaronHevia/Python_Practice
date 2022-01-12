from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.hideturtle()
        self.penup()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        """Creates the turtle at a starting position."""
        spawn_rate = random.randint(1, 6)
        if spawn_rate == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move(self):
        """Moves the car a certain distance."""
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        """Increases speed of cars."""
        self.speed += MOVE_INCREMENT
