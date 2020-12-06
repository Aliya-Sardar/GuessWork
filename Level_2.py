import turtle
import random

def random_function(screen):
    lists=['mobile','panda']
    num = random.randint(0,1)
    
    func = lists[num]
    if func == 'mobile' :
        registering_Ans(func)
        mobile(screen)

    elif func == 'panda' :
        registering_Ans(func)
        panda(screen)
    else:
        return
            

## writing answer function
def registering_Ans(art_name):
    Answers = open("level_2Answers.txt",'w')
    Answers.write(art_name)
    Answers.close()

def text(brush):
    brush.speed(0)
    brush.up()
    brush.goto(-250,200)
    brush.down()
    brush.write('Level 2',font='Arial 12')


def mobile(canvas):
    mobile = turtle.TurtleScreen(canvas)
    mobile.bgcolor('white')
    brush = turtle.RawTurtle(mobile)
    brush.ht()

    text(brush)

    # mobile
    brush.speed(2)
    brush.up()
    brush.goto(-100,100)
    brush.down()

    #outer lines
    brush.fd(130)
    brush.seth(270)
    brush.fd(240)
    brush.seth(180)
    brush.fd(130)
    brush.seth(90)
    brush.fd(240)

    #GOTO
    brush.up()
    brush.goto(-85,80)
    brush.down()

    # inner screen
    brush.fillcolor('black')
    brush.begin_fill()
    brush.seth(0)
    brush.fd(100)
    brush.seth(270)
    brush.fd(180)
    brush.seth(180)
    brush.fd(100)
    brush.seth(90)
    brush.fd(180)
    brush.end_fill()

    #GOTO
    brush.up()
    brush.goto(-25,-120)
    brush.down()

    #button
    brush.pensize(2)
    brush.circle(12)

    #GOTO
    brush.up()
    brush.goto(-50,90)
    brush.down()

    #top line
    brush.seth(0)
    brush.fd(30)



def panda(canvas):
    panda = turtle.TurtleScreen(canvas)
    panda.bgcolor('white')
    brush = turtle.RawTurtle(panda)
    brush.ht()

    text(brush)


    brush.speed(10)
    brush.pensize(3)
    brush.up()
    brush.goto(0,0)
    brush.down()


    #Draw face

    brush.color('black', 'black')
    brush.pendown()
    brush.circle(100)


    #Draw right ear

    brush.penup()
    brush.setx(50)
    brush.sety(185)
    brush.pendown()

    brush.begin_fill()
    brush.right(90)
    brush.circle(30, -260)
    brush.end_fill()


    #Draw left ear

    brush.penup()
    brush.setx(-50)
    brush.sety(185)
    brush.pendown()

    brush.left(170)
    brush.begin_fill()
    brush.right(90)
    brush.circle(30, 260)
    brush.end_fill()


    #Draw left eye

    brush.penup()
    brush.setx(-40)
    brush.sety(90)
    brush.pendown()

    brush.begin_fill()
    brush.circle(30)
    brush.end_fill()

    brush.left(10)
    brush.penup()
    brush.setx(-30)
    brush.sety(110)
    brush.pendown()

    brush.color('white', 'white')
    brush.begin_fill()
    brush.circle(15)
    brush.end_fill()

    brush.penup()
    brush.setx(-30)
    brush.sety(115)
    brush.pendown()

    brush.color('black', 'black')
    brush.begin_fill()
    brush.circle(5)
    brush.end_fill()


    #Draw right eye

    brush.penup()
    brush.setx(40)
    brush.sety(90)
    brush.pendown()

    brush.color('black', 'black')
    brush.begin_fill()
    brush.circle(30)
    brush.end_fill()

    brush.penup()
    brush.setx(30)
    brush.sety(110)
    brush.pendown()

    brush.color('white', 'white')
    brush.begin_fill()
    brush.circle(15)
    brush.end_fill()

    brush.penup()
    brush.setx(30)
    brush.sety(115)
    brush.pendown()

    brush.color('black', 'black')
    brush.begin_fill()
    brush.circle(5)
    brush.end_fill()


    #Draw mouth and nose

    brush.color('black', 'black')
    brush.penup()
    brush.setx(0)
    brush.sety(50)
    brush.pendown()

    brush.begin_fill()
    brush.circle(10)
    brush.end_fill()

    brush.right(90)
    brush.circle(20, 180)

    brush.penup()
    brush.setx(0)
    brush.sety(50)
    brush.pendown()

    brush.circle(20, -180)



