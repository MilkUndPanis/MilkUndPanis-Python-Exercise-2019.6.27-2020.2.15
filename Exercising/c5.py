#1
def miles_conversion(kilo):
    return kilo*0.6214
def main():
    kilo=float(input("Enter a distance(by kilometers):"))
    print(kilo,"km=",miles_conversion(kilo),"miles.",sep="")
main()
#2
def country(p):
    return p*0.025
def state(p):
    return p*0.05
def main():
    p=float(input("Please enter your spending:"))
    print("Spending\tState tax\tCountry tax\tTotal tax\tTotal spending")
    print(p,'\t',state(p),'\t',country(p),'\t',state(p)+country(p),'\t',p+state(p)+country(p),sep='')
main()
#3
def ShowMinMoney(cost):
    print("The minimum insure cost is:",cost*0.8,sep="")
def main():
    cost=float(input("Please enter your cost:"))
    ShowMinMoney(cost)
main()
#4
def MonthCost():
    loan=float(input("Enter the amount of loan per month:"))
    insu=float(input("Enter the amount of insurance per month:"))
    gas=float(input("Enter the cost of gas per month:"))
    oil=float(input("Enter the cost of oil per month:"))
    return loan+insu+gas+oil
def YearCost(mn):
    return mn*12
def main():
    mn=MonthCost()
    print("Your cost per month is:",mn)
    print(YearCost(mn),"per year.")
main()
#5
def Assess(estate):
    return estate*0.6
def Tax(assess):
    return assess*0.0072
def main():
    estate=float(input("Enter your total estate:"))
    print("Assessment price:$",Assess(estate),sep='')
    print("Tax:$",format(Tax(Assess(estate)),'.1f'),sep='')
main()
#6
def CountingCFF():
    fat=float(input("Please enter your take-in of fat(by gram):"))
    return fat*9
def CountingCFC():
    carb=float(input("Please enter your take_in of carbohydrate(by gram)"))
    return carb*4
def CountingTotal(a,b):
    return a+b
def main():
    cff=CountingCFF()
    cfc=CountingCFC()
    tfc=CountingTotal(cff,cfc)
    print("Your calories from fat:",format(cff,'.2f'),sep='')
    print("Your calories from carbohydrate:", format(cfc, '.2f'), sep='')
    print("Total calories:",format(tfc,'.2f'),sep='')
main()
#7
def A_Income():
    a=int(input("Please enter the amount of sold A ticket:"))
    return a*20
def B_Income():
    b=int(input("Please enter the amount of sold B ticket:"))
    return b*15
def C_Income():
    c=int(input("Please enter the amount of sold C ticket:"))
    return c*10
def Total_Income(a,b,c):
    return a+b+c
def main():
    ai=A_Income()
    bi=B_Income()
    ci=C_Income()
    ti=Total_Income(ai,bi,ci)
    print("A\tB\tC\tTotal")
    print(ai,'\t',bi,'\t',ci,'\t',ti,sep='')
main()
#8
def Get():
    area=float(input("Please enter the area of wall you want to brush:"))
    price=float(input("Please enter the cost of brushing per square inch:"))
    return area,price
def Paint(area):
    return area/112
def WorkingTime(area):
    return area/14
def PaintingFee(paint,price):
    return paint*price
def WorkingFee(time):
    return time*35.00
def TotalCost(paintingfee,workingfee):
    return paintingfee+workingfee
def main():
    a,p=Get()
    pa=Paint(a)
    wt=WorkingTime(a)
    pf=PaintingFee(pa,p)
    wf=WorkingFee(wt)
    tc=TotalCost(pf,wf)
    print("Need Paint:",format(pa,'.2f')," gallon",sep='')
    print("Working time:",format(wt,'.2f')," hours",sep='')
    print("Painting fee:",format(pf,'.2f')," dollars",sep='')
    print("Working fee:",format(wf,'.2f')," dollars",sep='')
    print("Total fee:",format(tc,'.2f')," dollars",sep='')
main()
#11
import random as r
def main():
    y='q'
    while y=='q':
        a=r.randint(1,300)
        b=r.randint(1,300)
        correct=a+b
        print(a,'\n+',b,'\n=?',sep='')
        test=int(input("Please enter an answer:"))
        while test!=correct:
            test=int(input("Wrong!Please enter a new answer:"))
        print("Correct.")
        y=input("Do you want to quit?(Press y to quit)")
main()
#12
def Getnum():
    a=int(input("Please enter the first number:"))
    b=int(input("Please enter the last number:"))
    return a,b
def max(a,b):
    if b>a:
        return b
    else:
        return a
def main():
    a,b=Getnum()
    m=max(a,b)
    print(m,"is larger.")
main()
#13
def falling_distance(t):
    return 4.9*(t**2)
def main():
    print("Time\tDistance\t")
    for t in range(1,11,1):
        print(t,'\t',format(falling_distance(t),'.2f'),'\t',sep='')
main()
#14
def Getnum():
    mass=float(input("Please enter the mass(kg):"))
    velocity=int(input("Please enter the speed(m/s):"))
    return mass,velocity
def kinetic_energy(mass,velocity):
    return 0.5*mass*(velocity**2)
def main():
    m,v=Getnum()
    ke=kinetic_energy(m,v)
    print("The object's kinetic energy is:",format(ke,'.2f'),sep='')
main()
#15
def Getnum():
    print("Please enter the score of five course:")
    a=float(input(""))
    b=float(input(""))
    c=float(input(""))
    d=float(input(""))
    e=float(input(""))
    return a,b,c,d,e
def calc_average(a,b,c,d,e):
    return (a+b+c+d+e)/5
def determine_grade(a):
    if a>=89.5 and a<=100:
        return 'A'
    elif a>=79.5 and a<89.5:
        return 'B'
    elif a>=69.5 and a<79.5:
        return 'C'
    elif a>=59.5 and a<69.5:
        return 'D'
    else:
        return 'F'
def main():
    a,b,c,d,e=Getnum()
    av=calc_average(a,b,c,d,e)
    gr=determine_grade(av)
    print("The five course's grades are:")
    print(determine_grade(a),'\t',determine_grade(b),'\t',determine_grade(c),'\t',determine_grade(d),'\t',determine_grade(e),'\t')
    print("Average score:",format(av,'.2f'),",grade ",gr,sep='')
main()
#16
import random as r
#1 refers to odd number,0 refers to even number
def determine(a):
    if a%2:
        return 1
    else:
        return 0
def main():
    odd=0
    even=0
    for i in range(100):
        nr=r.randint(1,600)
        tr=determine(nr)
        if tr==1:
            odd+=1
        else:
            even+=1
    print("There is",odd,"odd numbers,",even,"even numbers.")
main()
#17#18
import math as m
def is_prime(a):
    i=2
    while i*i<=a:
        if not(a%i):
            return False
        i+=1
    return True
def main():
    a=int(input("Please enter an interger:"))
    if is_prime(a):
        print(a,'is a prime.')
    else:
        print(a,'is not a prime.')
    print('Here is all of prime numbers from 1 to 100:')
    for i in range(2,101):
        if is_prime(i):
            print(i,end=' ')
main()
#19
def Future(p,i,t):
    return p*((1+i)**t)
def main():
    p=float(input("Please enter the value in your account now:"))
    i=float(input("Please enter the interest rate per month:"))
    t=int(input("Please enter the months:"))
    print("The future value is:",format(Future(p,i,t),'.2f'),"dollars.")
main()
#20
import random as r
def main():
    ch='y'
    while ch=='y':
        rn=r.randint(1,100)
        ts=int(input("A random number in the range from 1 to 100 produced.Guess how many:"))
        while ts!=rn:
            if ts>rn:
                ts=int(input("Too high,try again:"))
            elif ts<rn:
                ts=int(input("Too low,try again:"))
        print("Right!You are win.")
        ch=input("Press y to continue.")
main()
#21
#1 refers to STONE,2 refers to CLOTH,3 refers to SCISSORS
#RULES:STONE1 beats SCISSORS3
#SCISSORS3 beats CLOTH2
#CLOTH2 beats STONE1
#if computer and player choose the same choice,replay
STONE=1
CLOTH=2
SCISSORS=3
def Transverse(n):
    if n==STONE:
        return 'STONE'
    elif n==CLOTH:
        return 'CLOTH'
    elif n==SCISSORS:
        return 'SCISSORS'
    else:
        return 'NOUGHT'
def Deduce(a,b):
    #0 refers lose and 1 refers win,return two equal values refers a draw
    global STONE,CLOTH,SCISSORS
    if (a==STONE and b==STONE) or (a==CLOTH and b==CLOTH) or (a==SCISSORS and b==SCISSORS):
        return 1,1
    elif (a==STONE and b==SCISSORS) or (a==SCISSORS and b==CLOTH) or (a==CLOTH and b==STONE):
        return 1,0
    else:return 0,1
import random as r
def main():
    ch='y'
    while ch=='y':
        rn=r.randint(1,3)
        cs=int(input("Please give you choice.Stone,Cloth,or Scissors?\n1.Stone\t2.Cloth\t3.Scissors:"))
        while cs<STONE or cs>SCISSORS:
            cs=int(input("It is invalid.Try again:"))
        print("Now computer's choice is:",Transverse(rn))
        m1,m2=Deduce(rn,cs)
        if m1==0 and m2==1:
            print("You are win.")
        elif m1==1 and m2==0:
            print("You are lose.")
        else:
            print("A draw.")
        ch = input("Press y to continue.")
    print("That's all.")
main()
#22
import turtle as t
def triangle(X,Y,color):
    t.penup()
    t.goto(X,Y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(-60)
    t.forward(100)
    for i in range(2):
        t.right(120)
        t.forward(100)
    t.end_fill()
def main():
    triangle(50,50,'blue')
main()
#23
import turtle as t
def drawBase():
    t.hideturtle()
    t.penup()
    t.goto(0,-250)
    t.pendown()
    t.circle(100)
def drawMidSection():
    t.penup()
    t.goto(0,-50)
    t.pendown()
    t.circle(75)
def drawArms():
    for i in [75,-75]:
        t.penup()
        t.goto(i,25)
        t.pendown()
        if i==75:
            t.setheading(30)
        else:
            t.setheading(150)
        t.forward(75)
        t.left(35)
        t.forward(10)
        t.penup()
        t.left(180)
        t.forward(10)
        if i == 75:
            t.setheading(30)
        else:
            t.setheading(150)
        t.right(35)
        t.pendown()
        t.forward(10)
def drawHead():
    t.penup()
    t.goto(0,100)
    t.pendown()
    t.setheading(0)
    t.circle(35)
    t.setheading(90)
    t.penup()
    t.goto(20,120)
    t.setheading(-180)
    t.pendown()
    t.forward(40)
    for i in [15,-15]:
        t.penup()
        t.goto(i,140)
        t.pendown()
        t.setheading(0)
        t.circle(5)
def drawHat():
    t.fillcolor('black')
    t.penup()
    t.goto(65,170)
    t.pendown()
    t.begin_fill()
    t.setheading(-180)
    t.forward(130)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(20)
    t.end_fill()
def main():
    drawBase()
    drawMidSection()
    drawArms()
    drawHead()
    drawHat()
    t.done()
main()
#24
import turtle as t
def drawPattern(w,h):
    t.hideturtle()
    t.penup()
    t.goto(-w/2,-h/2)
    t.pendown()
    t.setheading(0)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
def drawFillPattern(w,h):
    t.fillcolor('black')
    t.begin_fill()
    drawPattern(w,h)
    t.end_fill()
def GOTO(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def main():
    drawFillPattern(100,100)
    drawPattern(150,150)
    drawPattern(200,200)
    GOTO(50,50)
    t.goto(100,100)
    GOTO(-50,50)
    t.goto(-100,100)
    GOTO(-50,-50)
    t.goto(-100,-100)
    GOTO(50,-50)
    t.goto(100,-100)
    GOTO(0,50)
    t.goto(0,100)
    GOTO(50,0)
    t.goto(100,0)
    GOTO(-50,0)
    t.goto(-100,0)
    GOTO(0,-50)
    t.goto(0,-100)
    t.done()
main()
#25
import turtle as t
def GOTO(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def square(x,y,width,color):
    t.hideturtle()
    GOTO(x,y)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()
def main():
    t.speed(0)
    for i in range(5):
        if i%2:
            square(-250+i*100,-250,100,'white')
        else: square(-250+i*100,-250,100,'black')
    t.left(90)
    for i in range(4):
        if i%2:
            square(250,-150+i*100,100,'black')
        else: square(250,-150+i*100,100,'white')
    t.left(90)
    for i in range(4):
         if i%2:
            square(150-100*i,250,100,'black')
         else: square(150-100*i,250,100,'white')
    t.left(90)
    for i in range(4):
         if i%2:
            square(-250,150-100*i,100,'black')
         else: square(-250,150-100*i,100,'white')
    t.setheading(0)
    GOTO(-150,-150)
    for i in range(3):
        if i%2:
            square(-150+i*100,-150,100,'white')
        else: square(-150+i*100,-150,100,'black')
    t.left(90)
    for i in range(2):
        if i%2:
            square(150,-50+i*100,100,'black')
        else: square(150,-50+i*100,100,'white')
    t.left(90)
    for i in range(2):
         if i%2:
            square(50-100*i,150,100,'black')
         else: square(50-100*i,150,100,'white')
    t.left(90)
    for i in range(2):
         if i%2:
            square(-150,50-100*i,100,'black')
         else: square(-150,50-100*i,100,'white')
    t.setheading(0)
    square(-50,-50,100,'black')
    t.done()
main()
#26
import turtle as t
import random as r
def S(a):
    t.setheading(a)
def F(a):
    t.forward(a)
def GOTO(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def square(x,y,width,color):
    t.hideturtle()
    GOTO(x,y)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(width)
        t.left(90)
    t.end_fill()
def drawCity():
    GOTO(-200,-80)
    S(0)
    F(50)
    S(90)
    F(80)
    S(0)
    F(60)
    S(90)
    F(140)
    S(0)
    F(110)
    S(-90)
    F(170)
    S(0)
    F(50)
    S(90)
    F(80)
    S(0)
    F(70)
    S(-90)
    F(40)
    S(0)
    F(20)
    S(-90)
    F(90)
    S(0)
    F(40)
    S(-90)
    F(120)
    S(180)
    F(400)
    S(90)
    F(120)
def drawWindow():
    square(-40,-60,10,'white')
    square(-135,-40,10,'white')
    square(-75,100,10,'white')
    square(-75,120,10,'white')
    square(95,10,10,'white')
    square(-10,40,10,'white')
def drawStar():
    for i in range(10):
        x=r.uniform(-200,200)
        if x>-200 and x<-150:
            y=r.uniform(-80,200)
        elif x>=-150 and x<-90:
            y=r.uniform(0,200)
        elif x>=-90 and x<20:
            y=r.uniform(140,200)
        elif x>=20 and x<70:
            y=r.uniform(-30,200)
        elif x>=70 and x<140:
            y=r.uniform(50,200)
        elif x>=140 and x<160:
            y=r.uniform(10,200)
        elif x>=160 and x<200:
            y=r.uniform(-80,200)
        else:y=-5000
        GOTO(x,y)
        t.dot()
def main():
    t.speed(0)
    square(-200,-200,400,'gray')
    t.fillcolor('black')
    t.begin_fill()
    drawCity()
    t.end_fill()
    drawWindow()
    drawStar()
    t.done()
main()
