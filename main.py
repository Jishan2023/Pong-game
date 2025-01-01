from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# paddle & ball & scoreboard
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# instruction of paddle
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "u")
screen.onkey(left_paddle.go_down, "d")

# game on
game_start = True
while game_start:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     detect with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#         detect with paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 300 or ball.distance(left_paddle) < 50 and ball.xcor() < - 300:
        ball.bounce_x()

#       detect right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

#       detect left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()