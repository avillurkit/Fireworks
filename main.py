bgcolor("dark blue")
speed(0)
penup()

#creating first firework
setposition(-100,100)
pendown()

def drawLargeCurve():
    for i in range(2):
        forward(70)
        right(90)
        forward(10)
        right(90)
    forward(70)
    right(30)
    for i in range(2):
        forward(45)
        right(90)
        forward(10)
        right(90)
    left(30)
    backward(70)
def drawSmallCurve():
    for i in range(2):
        forward(50)
        right(90)
        forward(5)
        right(90)
    forward(50)
    left(20)
    for i in range(2):
        forward(25)
        right(90)
        forward(5)
        right(90)
    right(20)
    backward(50)
for i in range(6):
    begin_fill()
    color("red")
    drawLargeCurve()
    end_fill()
    right(30)
    begin_fill()
    color("blue")
    drawSmallCurve()
    end_fill()
    right(30)

#creating second firework
penup()
setposition(80,70)
pendown()

for i in range(10):
    color("gold")
    penup()
    forward(45)
    pendown()
    forward(45)
    penup()
    backward(90)
    
    right(20)
    color("magenta")
    forward(20)
    pendown()
    forward(40)
    penup()
    backward(60)
    right(20)
left(90)
backward(10)
right(90)
color("yellow")
pendown()
begin_fill()
circle(10)
end_fill()
#creating third firework
penup()
setposition(-25,-75)
pendown()

def drawSquare(side):
    for i in range(4):
        forward(side)
        right(30)

for i in range(14):
    color("green")
    drawSquare(20)
    right(20)
    color("cyan")
    drawSquare(30)
    right(15)
    color("orange")
    drawSquare(20)
    right(15)
    
penup()
setposition(1000,1000)