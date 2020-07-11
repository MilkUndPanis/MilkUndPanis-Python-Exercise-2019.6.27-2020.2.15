import  math as m
EAST=0
SOUTH=270
WEST=180
NORTH=90
A_TURN=90
GLASS_WIDTH=40
HALF_WIDTH=20
GLASS_HEIGHT=30
HALF_HEIGHT=15
import turtle
turtle.hideturtle()
turtle.pensize(3)
turtle.speed(0)
turtle.penup()
turtle.goto(50,50)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(GLASS_WIDTH)
turtle.left(A_TURN)
turtle.forward(GLASS_HEIGHT)
turtle.left(A_TURN)
turtle.forward(GLASS_WIDTH)
turtle.left(A_TURN)
turtle.forward(GLASS_HEIGHT)
turtle.setheading(EAST)
turtle.penup()
turtle.goto(50,65)
turtle.pendown()
turtle.goto(-50,65)
turtle.setheading(SOUTH)
turtle.forward(HALF_HEIGHT)
turtle.right(A_TURN)
turtle.forward(GLASS_WIDTH)
turtle.right(A_TURN)
turtle.forward(GLASS_HEIGHT)
turtle.right(A_TURN)
turtle.forward(GLASS_WIDTH)
turtle.right(A_TURN)
turtle.forward(HALF_HEIGHT)
turtle.penup()
turtle.goto(-50-HALF_WIDTH,0)
turtle.setheading(SOUTH+30)
turtle.pendown()
turtle.circle(140/(m.sqrt(3)),120)
turtle.setheading(WEST)
turtle.forward(140)
turtle.penup()
turtle.goto(-220/(m.sqrt(3)),65)
turtle.pendown()
turtle.setheading(SOUTH)
turtle.circle(220/(m.sqrt(3)),180)
turtle.setheading(NORTH)
turtle.forward(120)
turtle.circle(80,90)
turtle.forward(440/(m.sqrt(3))-160)
turtle.circle(80,90)
turtle.penup()
turtle.goto(220/(m.sqrt(3)),185)
turtle.pendown()
radius=15+2420/9
the=(m.atan((2420/9-15)/(220/m.sqrt(3)))*360)/(2*3.1415926535897932)
turtle.setheading(NORTH+the)
turtle.circle(radius,180-2*the)
turtle.setheading(SOUTH)
turtle.forward(120)
turtle.penup()
turtle.goto(-70,155)
turtle.pendown()
turtle.goto(70,155)
turtle.penup()
turtle.goto(-70,135)
turtle.pendown()
turtle.goto(70,135)
turtle.penup()
turtle.goto(-70,115)
turtle.pendown()
turtle.goto(70,115)
turtle.penup()
turtle.goto(-50,90)
turtle.pendown()
turtle.setheading(NORTH+30)
turtle.circle(GLASS_WIDTH/m.sqrt(3),120)
turtle.penup()
turtle.goto(90,90)
turtle.pendown()
turtle.setheading(NORTH+30)
turtle.circle(GLASS_WIDTH/m.sqrt(3),120)
turtle.penup()
turtle.goto(-54,65)
turtle.pendown()
theta=(m.atan(7.8/16))*360/(2*3.1415926535897932)
turtle.setheading(theta+NORTH)
turtle.circle(17.8,180-2*theta)
turtle.setheading(SOUTH+theta)
turtle.circle(17.8,180-2*theta)
turtle.penup()
turtle.goto(-70,72)
turtle.pendown()
turtle.setheading(WEST)
turtle.circle(7)
turtle.goto(-70,68)
turtle.setheading(WEST)
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()
turtle.penup()
turtle.goto(86,65)
turtle.pendown()
turtle.setheading(theta+NORTH)
turtle.circle(17.8,180-2*theta)
turtle.setheading(SOUTH+theta)
turtle.circle(17.8,180-2*theta)
turtle.penup()
turtle.goto(70,72)
turtle.pendown()
turtle.setheading(WEST)
turtle.circle(7)
turtle.goto(70,68)
turtle.setheading(WEST)
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(3)
turtle.end_fill()
turtle.penup()
turtle.goto(-51,0)
turtle.pendown()
turtle.setheading(SOUTH)
turtle.forward(22)
turtle.penup()
turtle.goto(-32,0)
turtle.pendown()
turtle.forward(33.7)
turtle.penup()
turtle.goto(-13,0)
turtle.pendown()
turtle.forward(38)
turtle.penup()
turtle.goto(6,0)
turtle.pendown()
turtle.forward(38)
turtle.penup()
turtle.goto(25,0)
turtle.pendown()
turtle.forward(36.8)
turtle.penup()
turtle.goto(44,0)
turtle.pendown()
turtle.forward(27)
turtle.penup()
turtle.goto(63,0)
turtle.pendown()
turtle.forward(8)
turtle.penup()
turtle.goto(-70,0)
turtle.pendown()
turtle.setheading(SOUTH+60)
turtle.circle(140,20)
x=turtle.xcor()
t=turtle.heading()
turtle.setheading(EAST)
turtle.forward(-2*x)
turtle.setheading(-t)
turtle.circle(140,20)
pro=220/m.sqrt(3)
turtle.penup()
turtle.goto(-pro,110)
turtle.pendown()
turtle.setheading(WEST)
turtle.forward(14)
turtle.circle(15,167)
k=turtle.ycor()
turtle.setheading(WEST+13)
turtle.circle(15,227)
y=turtle.ycor()
turtle.penup()
turtle.goto(pro,y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(14)
turtle.circle(15,167)
turtle.setheading(EAST+13)
turtle.circle(15,227)
turtle.setheading(EAST)
turtle.penup()
turtle.goto(-30,90)
turtle.pendown()
turtle.goto(30,90)
turtle.penup()
turtle.setheading(NORTH+30)
turtle.goto(-7.5,90)
turtle.pendown()
turtle.forward(15)
turtle.penup()
turtle.goto(0,90)
turtle.setheading(NORTH)
turtle.pendown()
turtle.forward(30/m.sqrt(3))
turtle.penup()
turtle.setheading(NORTH-30)
turtle.goto(7.5,90)
turtle.pendown()
turtle.forward(15)
turtle.penup()
turtle.goto(30,90)
turtle.pendown()
turtle.setheading(SOUTH-30)
turtle.circle(120,30)
turtle.penup()
turtle.setheading(315)
turtle.forward(15*m.sqrt(2))
turtle.setheading(EAST)
turtle.pendown()
turtle.circle(15,270)
turtle.penup()
turtle.setheading(315)
turtle.forward(15*m.sqrt(2))
turtle.setheading(NORTH)
turtle.pendown()
turtle.circle(13,180)
x=turtle.xcor()
turtle.setheading(WEST)
turtle.forward(2*x)
turtle.setheading(NORTH)
turtle.circle(13,180)
turtle.setheading(45)
turtle.penup()
turtle.forward(15*m.sqrt(2))
turtle.pendown()
turtle.setheading(NORTH)
turtle.circle(15,270)
turtle.penup()
turtle.setheading(45)
turtle.forward(15*m.sqrt(2))
turtle.pendown()
turtle.setheading(NORTH)
turtle.circle(120,30)
turtle.setheading(EAST)
turtle.penup()
turtle.goto(-50,90)
turtle.pendown()
turtle.forward(100)
turtle.penup()
turtle.goto(90,65)
turtle.pendown()
turtle.forward(20)
turtle.goto(pro,k)
turtle.left(2*A_TURN)
turtle.penup()
turtle.goto(-90,65)
turtle.pendown()
turtle.forward(20)
turtle.goto(-pro,k)
turtle.done()
