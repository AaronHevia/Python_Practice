import random
import turtle
import colorgram


def extract_color(image, colors):
    extracted_colors = colorgram.extract(image, colors)
    temp_list = []
    for color in extracted_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        extracted_color = (r, g, b)
        temp_list.append(extracted_color)
    return temp_list


def random_color():
    """Returns a random color based on R, G, B values."""
    turtle.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def make_shape(sides):
    """Makes an equilateral shape based on the number of sides given."""
    angle = 360 / sides

    for _ in range(sides):
        turtle.pencolor(random_color())
        turtle.right(angle)
        turtle.forward(100)


def random_walk(steps):
    """Creates a random walking pattern north, south, east, or west based on the number of steps given."""
    angles = [0, 90, 180, 270]

    for _ in range(steps + 1):
        turtle.pencolor(random.choice(color_list))
        turtle.setheading(random.choice(angles))
        turtle.forward(30)


def spirograph(circles):
    """Creates a spirograph based on the number of circles given."""
    angle = 360 / circles

    for circle in range(circles + 1):
        radius = 100
        turtle.pencolor(random_color())
        turtle.circle(radius)
        turtle.right(angle)


def paint_like_hirst(radius, spacing, dots):
    turtle.penup()
    turtle.hideturtle()
    turtle.setheading(225)
    turtle.forward(250)
    turtle.setheading(0)

    for v in range(dots):
        for dot in range(dots):
            turtle.dot(radius, random.choice(color_list))
            turtle.forward(spacing)
        if v % 2 != 0:
            turtle.right(90)
            turtle.forward(spacing)
            turtle.right(90)
            turtle.forward(spacing)
        else:
            turtle.left(90)
            turtle.forward(spacing)
            turtle.left(90)
            turtle.forward(spacing)


color_list = extract_color('image.jpg', 30)
color_list.remove((249, 248, 244))
color_list.remove((247, 252, 251))
color_list.remove((251, 246, 249))
turtle.colormode(255)
turtle.shape("turtle")
turtle.color("green")
turtle.pensize(1)
turtle.speed(0)

# for _ in range(3, 11):
#     make_shape(_)

# random_walk(100)

# spirograph(9)

paint_like_hirst(20, 50, 10)

turtle.exitonclick()
