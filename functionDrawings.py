import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square with sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0,0)

alex = turtle.Turtle()
alex.color("pink")
for i in range(6):
    alex.penup()
    alex.forward(40)
    alex.pendown()
    drawSquare(alex,20)

wn.exitonclick()
