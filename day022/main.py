from turtle import Screen
from padders import Paddler
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddler((350, 0))
l_paddle = Paddler((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
hit = .1
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.move_speed *= 0.9

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()



screen.exitonclick()
