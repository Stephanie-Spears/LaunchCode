import turtle              # 1. import the modules
import random
wn = turtle.Screen()       # 2. Create a screen
wn.bgcolor('lightblue')

def createTurtle(startPoint, numOfTurtles):
    
    
    aTurtle = turtle.Turtle()

    colors = ["red", "blue", "green", "yellow", "purple", "violet", "maroon", "black", "white"]
    randIntColor = random.randrange(0,(len(colors)))
    randIntSpeed = random.randrange(4,10)
    aTurtle.shape("turtle")
    aTurtle.speed(randIntSpeed)
    aTurtle.color(colors[randIntColor])
    
   # for i in range(0, numOfTurtles):
    aTurtle.penup()  
    aTurtle.goto(-200, startPoint) 
    aTurtle.pendown()
        
    return aTurtle


numOfTurtles = random.randint(2,9)
turtleIndex = list(range(0, numOfTurtles))
print("number of turtles:", numOfTurtles)


startPoint = 175
for i in range(0, numOfTurtles):
    turtleIndex[i] = createTurtle(startPoint, numOfTurtles)
    startPoint = startPoint - (400/(numOfTurtles))
    
    
flagGirl = turtle.Turtle()
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
    
fastTurtle=turtleIndex[0]

print(fastTurtle.speed())
for i in range(0, numOfTurtles):
    if turtleIndex[i].speed() > fastTurtle.speed():
        fastTurtle = turtleIndex[i]

        
#wn.onscreenclick(turtleIndex.goto(200, (startPoint*-1)))        
#def makeRace(numOfTurtles, turtleIndex):
#    for i in numOfTurtles:
#        turtleIndex[i] & turtleIndex[i+1]
        
        
#makeRace(numOfTurtles, turtleIndex)        


#flagGirl.pendown()

#flagGirl.left(90)
#flagGirl.forward(400)
#flagGirl.left(140)

    

#andy.up()                  # 4. Move the turtles to their starting point
#lance.up()
#andy.goto(-100,20)
#lance.goto(-100,-20)

# your code goes here

wn.exitonclick()

wn.exitonclick()
