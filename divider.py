from turtle import Turtle


class Divider:
    def __init__(self):
        divider_line = Turtle("turtle")
        divider_line.color("white")
        divider_line.penup()
        divider_line.goto(0, 300)
        divider_line.setheading(270)
        divider_line.pencolor("white")
        divider_line.pensize(10)
        while divider_line.ycor() > -300:
            divider_line.pendown()
            divider_line.forward(20)
            divider_line.penup()
            divider_line.forward(20)
        divider_line.hideturtle()
