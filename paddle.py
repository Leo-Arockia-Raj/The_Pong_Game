from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xy):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(xy)

    def move_up(self):
        y = self.ycor()
        if self.ycor() < 240:
            self.goto(self.xcor(), y+20)

    def move_down(self):
        y = self.ycor()
        if self.ycor() > -240:
            self.goto(self.xcor(), y-20)
