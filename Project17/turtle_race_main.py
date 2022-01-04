import turtle
import random

screen = turtle.Screen()
screen.setup(width=820, height=520)


def set_turtle(turtle_object, color, y, x=-400):
    turtle_object.speed(0)
    turtle_object.shape("turtle")
    turtle_object.penup()
    turtle_object.color(color)
    turtle_object.goto(x, y)


def race(turtle_object_list, colors):
    index = random.randrange(0, len(turtle_object_list))
    turtle_object = turtle_object_list[index]
    color = colors[index]
    move_pace = random.randint(1, 10)

    if turtle_object.xcor() >= 390:
        return False, color
    else:
        turtle_object.forward(move_pace)
        return True, None


def race_result(winning_turtle, bet):
    turtle.hideturtle()
    if winning_turtle == bet:
        turtle.write("You picked the winning turtle.  You win!")
    else:
        turtle.write(f"The winning turtle was {winning_turtle}.  You lose.")


leonardo = turtle.Turtle()
set_turtle(leonardo, "blue", -200)

rafael = turtle.Turtle()
set_turtle(rafael, "red", -100)

donatello = turtle.Turtle()
set_turtle(donatello, "purple", 0)

michelangelo = turtle.Turtle()
set_turtle(michelangelo, "orange", 100)

splinter = turtle.Turtle()
set_turtle(splinter, "yellow", 200)

colors_list = ["blue", "red", "purple", "orange", "yellow"]
turtle_list = [leonardo, rafael, donatello, michelangelo, splinter]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")

keep_racing = True
winner = ""

while keep_racing:
    result = race(turtle_list, colors_list)
    keep_racing = result[0]
    winner = result[1]

race_result(winner, user_bet)

screen.exitonclick()

# def on_key_move():
#     screen.onkey(move_forward, "w")
#     screen.onkey(move_backward, "s")
# screen.listen()
# on_key_move()
