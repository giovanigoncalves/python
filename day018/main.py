import turtle
from turtle import Turtle, Screen
import random

color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86),
              (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219),
              (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49),
              (142, 208, 227), (119, 191, 139), (5, 185, 177), (106, 108, 198),
              (137, 29, 72), (4, 162, 86), (98, 51, 36), (24, 155, 210),
              (229, 168, 185), (173, 185, 221), (29, 90, 95), (233, 173, 162),
              (156, 212, 190), (87, 46, 33), (37, 45, 83), (245, 205, 7),
              (35, 88, 88), (103, 24, 56)]

turtle.colormode(255)
rafa = Turtle()
rafa.color("red")
rafa.speed(0)
rafa.penup()
# rafa.shape("turtle")
rafa.hideturtle()
x_origin = -200
y_origin = -200
origin = (x_origin, y_origin)
rafa.setposition(origin)


for _ in range(10):
    for _ in range(10):
        rafa.dot(20, random.choice(color_list))
        rafa.forward(50)
    y_origin += 50
    rafa.setposition(x_origin, y_origin)

screen = Screen()
screen.exitonclick()
