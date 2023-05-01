from turtle import Turtle,Screen
screen = Screen()
screen.setup(800,600)
class Score_board(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.scores()
    def scores(self):
        self.clear()
        self.goto(-200,250)
        self.write(self.l_score,align="center",font=("Algerian", 20, "normal"))
        self.goto(200, 250)
        self.write(self.r_score, align="center", font=("Algerian", 20, "normal"))



    def lscore(self):
        self.l_score += 1
        self.scores()

    def rscore(self):
        self.r_score += 1
        self.scores()





