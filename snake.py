import turtle
import random
import time


# Setup Screen

win = turtle.Screen()
win.title("Snake")
win.setup(600, 600)
win.bgcolor("black")
win.tracer(0)




# Score
score = 0

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(-290,270)
scoreboard.write("Score: 0", font = ("Courier", 20, "normal"))

def score_update():
    # global scoreboard, score
    scoreboard.clear()
    scoreboard.write("Score: {}".format(score), font = ("Courier", 20, "normal"))


def Grid():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    for i in range(-300, 300, 20):
            pen.goto(-300, i)
            pen.pendown()
            pen.goto(300, i)
            pen.penup()
    for j in range(-300, 300, 20):
        pen.goto(j, 300)
        pen.pendown()
        pen.goto(j, -300)
        pen.penup()



# Snake

snake = turtle.Turtle()
snake.speed(0)
snake.color("green")
snake.penup()
snake.shape("square")
dir = "up"

body = [snake]




# Food

food = turtle.Turtle()
food.speed(0)
food.color("red")
food.penup()
food.shape("circle")
randompos = []
for i in range(-280, 280, 20):
    randompos.append(i)
    


food.goto(random.choice(randompos), random.choice(randompos))



def grow():
    tail = turtle.Turtle()
    tail.speed(0)
    tail.color("green")
    tail.penup()
    tail.shape("square")
    # tail.goto(body[-1].xcor(), body[-1].ycor())
    
    body.append(tail)

    



def Eat():
    if ((food.xcor() + 15) >= snake.xcor() and (food.xcor() - 15) <= snake.xcor()) and ((food.ycor() + 15) >= snake.ycor() and (food.ycor() - 15) <= snake.ycor()):
        global score
        score += 10
        score_update()
        grow()
        food.goto(random.choice(randompos), random.choice(randompos))


        # food.goto(random.randint(-280, 280), random.randint(-280, 280))


    
    
        



def gameover():
    gameover = turtle.Turtle()
    gameover.speed(0)
    gameover.hideturtle()
    gameover.penup()
    gameover.color("white")
    gameover.write("Game Over", align = "center", font = ("Courier", 30, "normal"))
    time.sleep(10)
    quit()


# def selfcollision():
#     for index in range(len(body)):
        
#         if dir == "up" or dir == "down":
#             if abs(snake.ycor() - body[index].ycor()) < 20 and abs(snake.xcor() - body[index].xcor()) == 0:
#                 gameover()
        
#         # if dir == "down":
#         #     if abs(snake.ycor() - body[index].ycor()) < 20 and abs(snake.xcor() - body[index].xcor()) == 0:
#         #         gameover()

#         if dir == "left" or dir == "right":
#             if abs(snake.xcor() - body[index].xcor()) < 20 and abs(snake.ycor() - body[index].ycor()) == 0:
#                 gameover()

#         # if dir == "right":
#         #     if abs(snake.ycor() - body[index].ycor()) < 20 and abs(snake.xcor() - body[index].xcor()) == 0:
#         #         gameover()
    


def border():
    if (snake.xcor() > 290 or snake.xcor() < -290) or (snake.ycor() > 290 or snake.ycor() < -290):
        gameover()
        




# Moving the snake

def movement():
    for index in range(len(body) - 1, 0, -1):
        body[index].goto(body[index -1].xcor(), body[index - 1].ycor())

        if len(body) > 0:
            body[1].goto(snake.xcor(), snake.ycor())
            # selfcollision()


    if dir == "up":
        snake.sety(snake.ycor() + 20)
    
    if dir == "down":
        snake.sety(snake.ycor() - 20)

    if dir == "left":
        snake.setx(snake.xcor() - 20)

    if dir == "right":
        snake.setx(snake.xcor() + 20)

    


def up():
    global dir
    if dir != "down":
        dir = "up"
    

def down():
    global dir
    if dir != "up":
        dir = "down"


def left():
    global dir
    if dir != "right":
        dir = "left"
    

def right():
    global dir
    if dir != "left":
        dir = "right"



# Keyboard binding

win.listen()
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")
win.onkeypress(right, "Right")
win.onkeypress(left, "Left")




while True:
    time.sleep(0.1)
    # Grid()
    movement()
    Eat()
    border()
    # selfcollision()
    win.update()
