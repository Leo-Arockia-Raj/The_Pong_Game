from turtle import Screen
from divider import Divider
from paddle import Paddle
from ball import Ball
from score import Score
import time

#############################################################################################
#                                      SCREEN
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

##############################################################################################
#                                Players Ball Boundary Line
centre_divider = Divider()
#############################################################################################
#                                    Creating Paddles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

##########################################################################################
#                                   SCREEN LISTEN
screen.listen()

#                                   Paddle OnkeyPress
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")

#########################################################################################

game_is_on = True
l_score = Score(location=(-100, 200))
l_score.score_update()
r_score = Score(location=(30, 200))
r_score.score_update()

#############################################################################################
#                                  Ball

ball = Ball()
#############################################################################################
while game_is_on:
    screen.update()
    # Moving the Ball
    ball.move_ball()
    time.sleep(ball.ball_speed_value)    # Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 360:
        ball.reset_position()
        l_score.score_increment()

    if ball.xcor() < -360:
        ball.reset_position()
        r_score.score_increment()

screen.exitonclick()
