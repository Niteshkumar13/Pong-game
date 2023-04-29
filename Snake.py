from turtle import Turtle,Screen
import score
import time
import anshu

food = anshu.Food()
score_board = score.Score_board()
screen1 = Screen()
screen1.setup(600,600)

screen1.tracer(0)
position = [(0,0),(-20,0),(-40,0)]
move_dist = 20
list = []
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
for i in position:
    turtle1 = Turtle("square")
    turtle1.penup()
    turtle1.goto(i)
    list.append(turtle1)
head = list[0]

def up():
    if head.heading() != DOWN:
       head.setheading(UP)


def down():
    if head.heading() != UP:
       head.setheading(DOWN)


def left():
    if head.heading() != RIGHT:
       head.setheading(LEFT)


def right():
    if head.heading() != LEFT:
       head.setheading(RIGHT)
screen1.listen()
screen1.onkey(up,"Up")
screen1.onkey(down,"Down")
screen1.onkey(left,"Left")
screen1.onkey(right,"Right")
game_is_on = True
while game_is_on:
    screen1.update()
    time.sleep(0.1)
    if head.xcor()  >267 or head.xcor() < -267 or head.ycor()  >267 or head.ycor() < -267:
       game_is_on = False
       score_board.game_over()

    for i in list:
        if i == head:
            pass
        elif head.distance(i) < 10:
            game_is_on = False
            score_board.game_over()

    if head.distance(food) <15:
        food.refresh()
        score_board.increase_score()


        for i in range(1):
            turtle1 = Turtle("square")
            turtle1.penup()
            turtle1.color("red")
            list.append(turtle1)



    for i in range(len(list)-1,0, -1):
        x = list[i - 1].xcor()
        y = list[i - 1].ycor()
        list[i].goto(x, y)

    head.fd(move_dist)
screen1.exitonclick()