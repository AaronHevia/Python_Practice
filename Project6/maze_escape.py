def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not is_facing_north():
    turn_left()

if front_is_clear():
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()