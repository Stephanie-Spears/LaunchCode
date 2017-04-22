import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

def flagGirl():
    flagGirl = turtle.Turtle()
    flagGirl.speed(10)
    flagGirl.shape("turtle")
    flagGirl.color("hotpink")
    flagGirl.pensize(4)
    flagGirl.pencolor("red")

    flagGirl.penup()
    flagGirl.goto(125,-210)
    flagGirl.left(90)

    for i in range(20):
        flagGirl.forward(15)
        flagGirl.penup()
        flagGirl.forward(5)
        flagGirl.pendown()


def createTurtle(startPoint, numOfTurtles):
    
    aTurtle = turtle.Turtle()

    colors = ["red", "blue", "green", "yellow", "purple", "violet", "maroon", "black", "white"]
    aTurtle.shape("turtle")
    aTurtle.speed(random.randrange(4,10))
    aTurtle.color(colors[random.randrange(0,(len(colors)))])

    aTurtle.penup()  
    aTurtle.goto(-200, startPoint) 
    aTurtle.pendown()

    return aTurtle

flagGirl()

numOfTurtles = random.randint(2,9)
turtleIndex = list(range(0, numOfTurtles))

a = {}
startPoint = 175
for i in range(0, numOfTurtles):
    key = "Turtle" + str(i)
    a[key] = createTurtle(startPoint, numOfTurtles)
    startPoint = startPoint - (400/(numOfTurtles))
    print("{}'s speed is: {}".format(key, a[key].speed()))

dist = 2
for i in range(0, 200):
    a[key].tracer((8),(25))

    a[key].forward(dist)
    dist+=2

    
#wn.ontimer((a["Turtle0"].forward(400), a["Turtle2"].forward(400)), 10*numOfTurtles)

   # turtle.forward(300)
    
    
wn.exitonclick()
