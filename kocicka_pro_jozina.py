import turtle
mnau = turtle.Turtle()
turtle.bgcolor("dark orange")
turtle.title("Mnau<3")
strana = input("Vyber si stranu[boční(b), přední(p)]: ")
def noha():
    mnau.fillcolor("black")
    mnau.begin_fill()
    for i in range(2):
        mnau.fd(20)
        mnau.rt(90)
        mnau.fd(20)
        mnau.rt(90)
    mnau.end_fill()
    mnau.penup()
    mnau.rt(90)
    mnau.fd(20)
    mnau.lt(90)
    mnau.pendown()
    mnau.fillcolor("white")
    mnau.begin_fill()
    for i in range(2):
        mnau.fd(20)
        mnau.rt(90)
        mnau.fd(20)
        mnau.rt(90)
    mnau.end_fill()  
if strana == "b":
    mnau.pensize(3)
    mnau.fillcolor("black")
    mnau.begin_fill()
    for j in range(2):
        mnau.lt(90)
        mnau.fd(100)
        mnau.lt(90)
        mnau.fd(300)
    mnau.end_fill()
    mnau.penup()
    mnau.goto(-280, 0)
    mnau.pendown()
    noha()
    mnau.penup()
    mnau.goto(-40,0 )
    mnau.pendown()
    noha()
    mnau.penup()
    mnau.goto(0, 60)
    mnau.pendown()
    mnau.fillcolor("black")
    mnau.begin_fill()
    mnau.lt(90)
    mnau.fd(10)
    mnau.rt(120)
    mnau.fd(50)
    mnau.rt(90)
    mnau.fd(10)
    mnau.rt(90)
    mnau.fd(50)
    mnau.end_fill()
    mnau.begin_fill()
    mnau.bk(50)
    mnau.rt(130)
    mnau.fd(60)
    mnau.lt(90)
    mnau.fd(10)
    mnau.lt(90)
    mnau.fd(60)
    mnau.end_fill()
    mnau.bk(60)
    mnau.rt(180)
    mnau.fillcolor("white")
    mnau.begin_fill()
    for o in range(3):
        mnau.fd(10)
        mnau.rt(90)
    mnau.fd(10)
    mnau.end_fill()
    mnau.penup()
    mnau.goto(-300,60)
    mnau.pendown()
    mnau.fillcolor("black")
    mnau.begin_fill()
    mnau.rt(30)
    for t in range(3):
        mnau.fd(80)
        mnau.lt(90)
    mnau.fd(80)
    mnau.end_fill()
    mnau.penup()
    mnau.lt(90)
    mnau.fd(80)
    mnau.pendown()
    mnau.fillcolor("white")
    mnau.begin_fill()
    mnau.fd(10)
    mnau.lt(90)
    mnau.fd(30)
    mnau.lt(90)
    mnau.fd(10)
    mnau.end_fill()
    mnau.penup()
    mnau.rt(90)
    mnau.fd(50)
    mnau.lt(90)
    mnau.fd(60)
    mnau.pendown()
    mnau.fillcolor("black")
    mnau.begin_fill()
    mnau.rt(90)
    for h in range(2):
        mnau.fd(10)
        mnau.lt(90)
    mnau.fd(10)
    mnau.end_fill()
    mnau.fillcolor("white")
    mnau.begin_fill()
    mnau.rt(180)
    mnau.fd(10)
    for g in range(2):
        mnau.lt(90)
        mnau.fd(10)
    mnau.end_fill()
    mnau.penup()
    mnau.goto(-200, 0)
    mnau.pendown()
    mnau.fillcolor("white")
    mnau.begin_fill()
    mnau.lt(100)
    mnau.fd(20)
    mnau.rt(90)
    mnau.fd(100)
    mnau.rt(90)
    mnau.fd(20)
    mnau.end_fill()    
    mnau.hideturtle()
    turtle.done()
if strana == "p":
    def white_eye():
        mnau.fillcolor("white")
        mnau.begin_fill()
        for e in range(4):
            mnau.fd(40)
            mnau.rt(90)
        mnau.end_fill()
    def green_eye():
        mnau.fillcolor("green3")
        mnau.begin_fill()
        for ee in range(4):
            mnau.fd(40)
            mnau.rt(90)
        mnau.end_fill()
    def pusa():
        for v in range(4):
            mnau.fd(40)
            mnau.lt(90)
        mnau.lt(90)
        mnau.fd(40)
        mnau.rt(90)
    mnau.pensize(3)
    mnau.fillcolor("black")
    mnau.begin_fill()
    for v in range(4):
        mnau.lt(90)
        mnau.fd(200)
    mnau.end_fill()
    def ousko():
        mnau.fillcolor("white")
        mnau.begin_fill()
        mnau.lt(90)
        mnau.fd(20)
        mnau.lt(90)
        mnau.fd(40)
        mnau.lt(90)
        mnau.fd(20)
        mnau.end_fill()
    mnau.penup()
    mnau.goto(0, 200)
    mnau.pendown()
    ousko()
    mnau.penup()
    mnau.goto(-160,200)
    mnau.lt(90)
    mnau.pendown()
    ousko()
    mnau.penup()
    mnau.fd(40)
    mnau.pendown()
    mnau.pensize(1)
    mnau.lt(90)
    white_eye()
    mnau.fd(40)
    green_eye()
    mnau.penup()
    mnau.fd(80)
    mnau.pendown()
    green_eye()
    mnau.fd(40)
    white_eye()
    mnau.penup()
    mnau.fd(40)
    mnau.rt(90)
    mnau.fd(160)
    mnau.rt(90)
    mnau.fd(40)
    mnau.rt(90)
    mnau.pendown()
    mnau.begin_fill()
    for m in range(2):
        mnau.fd(40)
        mnau.lt(90)
        mnau.fd(120)
        mnau.lt(90)
    mnau.end_fill()
    mnau.fd(40)
    mnau.fillcolor("slate gray")
    mnau.begin_fill()
    pusa()
    mnau.end_fill()
    mnau.fillcolor("PaleVioletRed1")
    mnau.begin_fill()
    pusa()
    mnau.end_fill()
    mnau.fillcolor("slate gray")
    mnau.begin_fill()
    pusa()
    mnau.end_fill()
    mnau.hideturtle()
    turtle.done()