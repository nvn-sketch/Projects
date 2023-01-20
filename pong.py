import turtle
import random

win = turtle.Screen()
win.title("Pong")
win.setup(800, 600)
win.bgcolor("cyan")
win.tracer(0)


paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)



paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)



ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5


def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

# Keyboard binding
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

while True:
    win.update()

    # Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1


    # Paddle and ball collision

    if ball.xcor() > 330 and ball.xcor() < 340 and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60):
        ball.dx *= -1
    
    if ball.xcor() > 340 and ball.xcor() < 360:
        if ball.ycor() < (paddle_b.ycor() + 60) and not (ball.ycor() < (paddle_b.ycor() - 60)):
            ball.dy *= -1

        if ball.ycor() > (paddle_b.ycor() - 60) and not (ball.ycor() > (paddle_b.ycor() + 60)):
            ball.dy *= -1

    
    
    if ball.xcor() < -330 and ball.xcor() > -340 and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60):
        ball.dx *= -1
    
    if ball.xcor() < -340 and ball.xcor() > -360:
        if ball.ycor() < (paddle_a.ycor() + 60) and not (ball.ycor() < (paddle_a.ycor() - 60)):
            ball.dy *= -1

        if ball.ycor() > (paddle_a.ycor() - 60) and not (ball.ycor() > (paddle_a.ycor() + 60)):
            ball.dy *= -1


    # Border checking
    # Paddle A

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    # Paddle B

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    



    




