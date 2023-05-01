from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score_board_ import  Score_board
import time
screen = Screen()
scored = Score_board()
screen.setup(800,600)
screen.tracer(0)
ball = Ball()
turtle = Turtle()
turtle.lt(90)
turtle.hideturtle()
turtle.penup()
turtle.goto(0,330)


turtle.pendown()
l_paddle = Paddle((-385,0))
r_paddle = Paddle((380,0))
screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
game_is_on = True
while game_is_on:
    screen.update()
    ball.ball_move()
    if ball.ycor() > 280 or  ball.ycor() < -280:
        ball.ball_bounce()

    elif (ball.distance(r_paddle) < 30 and ball.xcor() > 330) or (ball.distance(l_paddle) <30 and ball.xcor() < -350):
        ball.ball_hor()

    elif ball.xcor() > 380:
        ball.restart()
        scored.lscore()
    elif ball.xcor() < -380:
        ball.restart()
        scored.rscore()







screen.exitonclick()