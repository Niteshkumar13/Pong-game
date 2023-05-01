from turtle import Turtle,Screen
xx = Screen()

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        # self.x = Turtle()
        self.shapesize(5,1)

        self.shape("square")
        self.color("red")
        self.penup()
        self.goto(position)


    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(),y_cor)

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)







