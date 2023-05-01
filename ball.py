from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def ball_move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        time.sleep(0.1)
        self.goto(x_cor,y_cor)

    def ball_bounce(self):
        self.y_move = self.y_move * -1

    def ball_hor(self):
        self.x_move *= -1

    def restart(self):
        self.color("blue")
        self.shape("circle")
        self.color("blue")
        self.home()
        self.x_move *= -1


