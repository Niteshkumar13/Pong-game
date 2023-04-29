import turtle

class  Score_board(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score is {self.score}", align="center", font=("Arial", 20, "normal"))





    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over \n Score is {self.score}", align="center", font=("Arial", 20, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score is {self.score}", align="center", font=("Arial", 24, "normal"))