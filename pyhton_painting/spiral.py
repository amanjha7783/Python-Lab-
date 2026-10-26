import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Mandala")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Generate rainbow colors
hue = 0

for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.pencolor(color)

    pen.forward(i)
    pen.left(59)
    pen.circle(50)

    hue += 0.005

turtle.done()