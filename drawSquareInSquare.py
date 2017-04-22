import turtle

def drawSquare(myTurt, sideLength):
    for i in range(4):
        myTurt.forward(sideLength)
        myTurt.left(90)
    

wn = turtle.Screen()
wn.bgcolor("lightgreen")

fabio = turtle.Turtle()
fabio.pensize(3)
fabio.color("hotpink")
sideLen = 20
for i in range(5):
    drawSquare(fabio, sideLen)
    fabio.forward(sideLen)
    sideLen += 20
