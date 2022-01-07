import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

# Constants created based on screen size.
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
POSITIONS = {
    "left_paddle": (-940, -40),
    "right_paddle": (935, -40),
    "boundary": -540,
    "scoreboard": 500

}
BOUNDS = {
    "upper": 490,
    "lower": -520,
    "left": -950,
    "right": 950
}

# Screen setup.
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('PONG')
boundaries = Scoreboard(POSITIONS["boundary"]).draw_boundaries()
# Animation setting.
screen.tracer(0)
# Get input from user
screen.listen()
# Scoreboard setup.
scoreboard = Scoreboard(POSITIONS["scoreboard"])
scoreboard.update_scoreboard()
# Create Paddles
p1_paddle = Paddle(POSITIONS["left_paddle"], BOUNDS["upper"], BOUNDS["lower"])
p2_paddle = Paddle(POSITIONS["right_paddle"], BOUNDS["upper"], BOUNDS["lower"])
# Create Ball
ball = Ball()


# Create paddle control function
def on_key_move():
    """Triggers associated movement when the respective key is pushed."""
    screen.onkeypress(p1_paddle.move_up, "w")
    screen.onkeypress(p1_paddle.move_down, "s")
    screen.onkeypress(p2_paddle.move_up, "Up")
    screen.onkeypress(p2_paddle.move_down, "Down")


playing = True
while playing:
    time.sleep(ball.move_speed)
    screen.update()
    on_key_move()
    ball.move()

    # Collisions against top or bottom walls.
    if ball.ycor() > BOUNDS["upper"] or ball.ycor() < BOUNDS["lower"]:
        ball.bounce_y()

    # TODO:  Create Speed adjustment depending on which portion of the paddle it hit.
    # Collisions against right paddle.
    if ball.x_move > 0:
        for part in p2_paddle.body:
            if ball.distance(part) < 20:
                ball.bounce_x()
                print(ball.move_speed)
    # Collisions against left paddle.
    elif ball.x_move < 0:
        for part in p1_paddle.body:
            if ball.distance(part) < 20:
                ball.bounce_x()
                print(ball.move_speed)

    if ball.xcor() > BOUNDS["right"]:
        ball.reset_ball()
        scoreboard.p1_score()
    elif ball.xcor() < BOUNDS["left"]:
        ball.reset_ball()
        scoreboard.p2_score()

    if scoreboard.p1_points == 7 or scoreboard.p2_points == 7:
        playing = False
        scoreboard.game_over()

screen.exitonclick()
