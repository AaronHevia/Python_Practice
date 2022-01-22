import turtle
import pandas

TOTAL_STATES = 50
correct_states = 0
known_states = []

# Set up game environment
screen = turtle.Screen()
screen.title('U.S. States Game')

# Load image to turtle
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)
turtle.penup()

# Create stamping turtle
stamp = turtle.Turtle()
stamp.hideturtle()
stamp.penup()

# Import state data
data = pandas.read_csv('50_states.csv')
states = data.state.to_list()

while correct_states < TOTAL_STATES:
    # Get a state from the user
    answer_state = screen.textinput(title=f'{correct_states}/{TOTAL_STATES} states',
                                    prompt='Guess a state in the U.S. or "X" to Exit:  ').title()

    if answer_state == 'X':
        states_to_learn = [state for state in states if state not in known_states]  # List Comprehension.
        df = pandas.DataFrame(states_to_learn)
        df.to_csv('states_to_learn.csv')
        break

    if answer_state in states and answer_state not in known_states:
        known_states.append(answer_state)
        row = data[data.state == answer_state]
        stamp.goto(int(row.x), int(row.y))
        stamp.write(answer_state)
        correct_states += 1
