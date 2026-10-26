import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

h = 0

for i in range(400):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    pen.pencolor(c)

    pen.forward(i * 0.8)
    pen.left(91)

    h += 0.004

pen.hideturtle()
turtle.done()