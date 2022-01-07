from turtle import Turtle

X_START = 10
Y_START = 10
MOVE_SPEED = 0.05


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.x_move = X_START
        self.y_move = Y_START
        self.penup()
        self.shape('circle')
        self.color('cyan')
        self.move_speed = MOVE_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .9

    def reset_ball(self):
        self.move_speed = MOVE_SPEED
        self.x_move *= -1

        self.goto(0, 0)
