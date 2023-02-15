from turtle import Turtle
FONT = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self, location):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(location)

    def score_increment(self):
        self.score += 1
        self.clear()
        self.score_update()

    def score_update(self):
        self.write(arg=self.score, font=FONT)
