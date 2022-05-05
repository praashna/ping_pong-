 
 #part 1: getting started
 
import turtle
import winsound

wn = turtle.Screen()
wn.title("pong by @Praash")
wn.bgcolor("black")
wn.setup(width=800, height=600) #800 600 pixels
wn.tracer(0) #stops window automatically updating

#score
score_a=0
score_b=0

#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(+350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

#mark_line to mark the line between two players

mark_line = turtle.Turtle()
mark_line.speed(0)
mark_line.color("white")
mark_line.penup()
mark_line.hideturtle()
mark_line.goto(0, 260)
mark_line.write("Player A: 0 Player B: 0", align="center", font=('courier', 24, ))

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20 #add by 20 while moving up
    paddle_a.sety(y) #set y to the new y ie +20 y

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)    

# keyboard binding
wn.listen() 
wn.onkeypress(paddle_a_up, "w") #when user press w, call fun paddle up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

 #main game loop
while True:
    wn.update()

#move the ball

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

#border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('pong.wav',winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1   
        winsound.PlaySound('pong.wav',winsound.SND_ASYNC)


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        mark_line.clear()
        mark_line.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=('courier', 24, ))
        

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        mark_line.clear()
        mark_line.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=('courier', 24, ))
        

#paddle and ball collisoion
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor()> paddle_b.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('pong.wav',winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor()> paddle_a.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('pong.wav',winsound.SND_ASYNC)



    



    



 



             
