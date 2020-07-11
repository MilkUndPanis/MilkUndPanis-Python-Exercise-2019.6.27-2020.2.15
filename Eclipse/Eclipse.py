import turtle
import math
def eclipse(a,b,angle,steps):
    minAngle = (2*math.pi/360) * angle / steps
    turtle.penup()
    turtle.setpos(0,-b)
    turtle.pendown()
    for i in range(steps):
        nextPoint = [a*math.sin((i+1)*minAngle),-b*math.cos((i+1)*minAngle)]
        turtle.setpos(nextPoint)
def eclipseR(a,b,angle,steps,rotateAngle):
    minAngle = (2*math.pi/360) * angle / steps
    rotateAngle = rotateAngle/360*2*math.pi
    turtle.penup()
    turtle.setpos(b*math.sin(rotateAngle),-b*math.cos(rotateAngle))
    turtle.pendown()
    for i in range(steps):
        nextPoint = [a*math.sin((i+1)*minAngle),-b*math.cos((i+1)*minAngle)]
        nextPoint = [nextPoint[0]*math.cos(rotateAngle)-nextPoint[1]*math.sin(rotateAngle),
                     nextPoint[0]*math.sin(rotateAngle)+nextPoint[1]*math.cos(rotateAngle)]
        turtle.setpos(nextPoint)
turtle.hideturtle()
turtle.begin_fill()
turtle.fillcolor('dark sea green')
eclipseR(200,150,360,50,30)
turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor('bisque')
eclipseR(200,150,360,50,60)
turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor('lavender')
eclipseR(200,150,360,50,90)
turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor('gold')
eclipseR(200,150,360,50,120)
turtle.end_fill()
turtle.begin_fill()
turtle.fillcolor('cyan')
eclipseR(200,150,360,50,150)
turtle.end_fill()
turtle.penup()
turtle.right(135)
turtle.forward(100)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('SeaGreen3')
turtle.circle(50)
turtle.end_fill()
turtle.penup()
turtle.forward(120)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('SeaGreen3')
turtle.circle(50)
turtle.end_fill()
turtle.right(180)
turtle.penup()
turtle.forward(60)
turtle.right(90)
turtle.forward(100)
turtle.pendown()
turtle.right(90)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.left(90)
turtle.circle(100,180)
turtle.done()

