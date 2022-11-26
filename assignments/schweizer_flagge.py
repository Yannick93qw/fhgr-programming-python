import turtle
import random

"""
Erstellen Sie die Schweizer Flagge mit der turtle-Grafik und exakt folgendem Aussehen (400x400 Pixel), es darf kein Pfeil/Turtle sichtbar sein!
"""


def draw_rect(width, height, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.end_fill()


def draw_swiss_cross(width, height, background_color, cross_color):
    padding_percent = 0.2
    swiss_cross_side_percent = 0.2

    # Draw red background for swiss cross
    draw_rect(width, height, background_color)

    # Move to start position for horizontal part of swiss cross
    turtle.penup()
    turtle.forward(width * (2 * swiss_cross_side_percent))
    turtle.left(90)
    turtle.forward(height * padding_percent)
    turtle.right(90)
    turtle.pendown()

    # Draw horizontal part of swiss cross (consisting of 3 segments)
    draw_rect(int(width * swiss_cross_side_percent),
              int(height * swiss_cross_side_percent * 3), cross_color)

    # Move to start position of vertical part of swiss cross
    turtle.penup()
    turtle.left(90)
    turtle.forward(int(height * swiss_cross_side_percent))
    turtle.left(90)
    turtle.forward(int(width * swiss_cross_side_percent +
                   (width * padding_percent)))
    turtle.right(180)
    turtle.forward(int(width * padding_percent))
    turtle.pendown()

    # Draw vertical part of swiss cross (consisting of 3 segments)
    draw_rect(int(width * swiss_cross_side_percent * 3),
              int(height * swiss_cross_side_percent), cross_color)


turtle.reset()

turtle.speed("fastest")

background_colors = ["#F27457", "#BF665E", "red"]
cross_colors = ["#253659", "#03A696", "white"]

# Totally not necessary but kinda neat
for i in range(100):
    width = random.randrange(10, 200)
    height = width

    x = random.randint(-400, 400)
    y = random.randint(-400, 400)

    background_color = random.choice(background_colors)
    cross_color = random.choice(cross_colors)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_swiss_cross(width, height, background_color, cross_color)

turtle.exitonclick()
