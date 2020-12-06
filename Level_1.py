## Guess Work Level_1

import turtle
import random


#random function to randomly choose drawings
def random_function(screen):
    lists=['leaf','hand','book','table']
    num = random.randint(0,3)
    
    func = lists[num]
    if func == 'leaf' :
        registering_Ans(func)
        leaf(screen)

    elif func == 'hand' :
        registering_Ans(func)
        hand(screen)

    elif func == 'book' :
        registering_Ans(func)
        book(screen)

    elif func == 'table' :
        registering_Ans(func)
        table(screen)
        
    else:
        return
    
    

## writing answer function
def registering_Ans(art_name):
    Answers = open("level_1Answers.txt",'w')
    Answers.write(art_name)
    Answers.close()

def text(brush):
    brush.speed(0)
    brush.up()
    brush.goto(-250,200)
    brush.down()
    brush.write('Level 1',font='Arial 12')


# functions for drawings
def leaf(canvas):
    leaf = turtle.TurtleScreen(canvas)
    leaf.bgcolor('white')
    brush = turtle.RawTurtle(leaf)
    brush.ht()
    
    brush.up()
    brush.goto(0,0)
    brush.down()
    brush.speed(1)
    
    brush.fillcolor('green')
    brush.begin_fill()
    brush.forward(100)
    brush.setheading(45)
    brush.fd(100)
    brush.setheading(180)
    brush.fd(100)
    brush.setheading(225)
    brush.fd(100)
    brush.setheading(23)
    brush.fd(190)
    brush.up()
    brush.bk(190)
    brush.down()
    brush.pen(pencolor ='Brown',pensize =5)
    brush.setheading(250)
    brush.fd(100)

    brush.up()
    brush.pen(pencolor ='Black',pensize =1)
    brush.bk(100)
    brush.setheading(23)
    brush.fd(80)
    brush.setheading(-20)
    brush.down()
    brush.fd(45)
    brush.up()
    brush.bk(50)
    brush.setheading(75)
    brush.down()
    brush.fd(45)
    brush.end_fill()


def hand(canvas):
    hand = turtle.TurtleScreen(canvas)
    hand.bgcolor('white')
    brush = turtle.RawTurtle(hand)
    brush.ht()

    text(brush)

    brush.up()
    brush.goto(-40,-70)
    brush.down()
    
    brush.speed(2)
    brush.fillcolor('PapayaWhip')
    brush.begin_fill()
    # left side wrist
    brush.seth(100)
    brush.fd(50)

    #thumb
    brush.seth(120)
    brush.fd(100)
    brush.circle(-10,180)
    brush.seth(305)
    brush.fd(50)

    #index
    brush.setheading(93)
    brush.fd(100)
    brush.circle(-10,180)
    brush.setheading(272)
    brush.fd(80)

    #middle finger
    brush.setheading(88)
    brush.fd(110)
    brush.circle(-10,180)
    brush.setheading(272)
    brush.fd(100)

    #ring finger
    brush.setheading(88)
    brush.fd(80)
    brush.circle(-10,180)
    brush.setheading(270)
    brush.fd(80)

    #pinky finger
    brush.setheading(88)
    brush.fd(60)
    brush.circle(-8,180)
    brush.setheading(268)
    brush.fd(200)

    brush.end_fill()

def book(canvas):
    book = turtle.TurtleScreen(canvas)
    book.bgcolor('white')
    brush = turtle.RawTurtle(book)
    brush.ht()

    text(brush)
    
    #starting point
    brush.up()
    brush.goto(-160,-40)
    brush.down()
    brush.speed(3)

    #upper cover
    brush.pensize(5)
    brush.seth(45)
    brush.fd(200)
    brush.seth(340)
    brush.fd(200)
    brush.seth(225)
    brush.fd(200)
    brush.seth(160)
    brush.fd(200)

    #lower cover
    brush.seth(270)
    brush.fd(40)
    brush.seth(340)
    brush.fd(200)
    brush.seth(45)
    brush.fd(200)

    #pages
    brush.pensize(1)
    brush.bk(5)
    brush.seth(90)
    brush.fd(40)
    for i in range(-40,-80,-8):
        brush.up()
        brush.goto(-160,i)
        brush.down()
        brush.seth(340)
        brush.fd(200)
        brush.seth(45)
        brush.fd(195)

def table(canvas):
    table = turtle.TurtleScreen(canvas)
    table.bgcolor('white')
    brush = turtle.RawTurtle(table)
    brush.ht()

    text(brush)

    #starting position
    brush.up()
    brush.goto(-200,20)
    brush.down()
    brush.speed(3)

    brush.fillcolor('brown')
    brush.begin_fill()

    #table top
    brush.seth(40)
    brush.fd(100)
    brush.seth(0)
    brush.fd(300)
    brush.seth(220)
    brush.fd(100)
    brush.seth(180)
    brush.fd(300)

    #table sides
    brush.seth(270)
    brush.fd(20)
    brush.seth(0)
    brush.fd(300)
    brush.seth(90)
    brush.fd(20)
    brush.up()
    brush.bk(20)
    brush.down()
    brush.seth(40)
    brush.fd(100)
    brush.seth(90)
    brush.fd(20)

    #table legs

    brush.up()
    brush.goto(-180,0)
    brush.down()

    #left front leg
    brush.seth(270)
    brush.fd(150)
    brush.seth(0)
    brush.fd(15)
    brush.seth(90)
    brush.fd(150)
    brush.up()
    brush.bk(150)
    brush.down()
    brush.seth(45)
    brush.fd(10)
    brush.seth(90)
    brush.fd(145)

    #right front leg
    brush.up()
    brush.goto(85,0)
    brush.down()

    brush.seth(270)
    brush.fd(150)
    brush.seth(0)
    brush.fd(15)
    brush.seth(90)
    brush.fd(150)
    brush.up()
    brush.bk(150)
    brush.down()
    brush.seth(45)
    brush.fd(10)
    brush.seth(90)
    brush.fd(149)

    #right back leg
    brush.up()
    brush.goto(150,40)
    brush.down()

    brush.seth(270)
    brush.fd(110)
    brush.seth(0)
    brush.fd(15)
    brush.seth(90)
    brush.fd(125)
    brush.up()
    brush.bk(125)
    brush.down()
    brush.seth(45)
    brush.fd(10)
    brush.seth(90)
    brush.fd(125)

    #left back leg
    brush.up()
    brush.goto(-120,0)
    brush.down()

    brush.seth(270)
    brush.fd(80)
    brush.seth(0)
    brush.fd(15)
    brush.seth(90)
    brush.fd(80)
    brush.up()
    brush.bk(80)
    brush.down()
    brush.seth(45)
    brush.fd(10)
    brush.seth(90)
    brush.fd(75)

    brush.end_fill()
