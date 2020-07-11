#1
totalbug=0
for day in range(5):
    bug=int(input("How many bugs you had collected today?"))
    totalbug+=bug
print("You had collected",totalbug,"bugs.")
#2
AMINCAL=4.2
for min in [10,15,20,25,30]:
    TOTAL=AMINCAL*min
    print("In",min,"minutes,",TOTAL,"calories consumed.")
#3
budget=float(input("Please enter the budget of this month:"))
tc=0
consume=float(input("Please enter the consume of this month by every time:"))
while consume!=0:
    tc+=consume
    consume = float(input("Please enter the consume of this month by every time(enter 0 to quit):"))
if tc<budget:
    print("Budget is sufficient.The rest is",budget-tc,"dollars.")
elif tc>budget:
    print("Budget is insufficient.The deficit is", tc - budget, "dollars.")
else:
    print("No money rest.")
#4
sp=float(input("What is the speed of the vehicle in mph?"))
hrs=int(input("How many hours it traveled?"))
print("Hour\t             Distance Traveled\t\n"
      "___________________________________________")
for h in range(1,hrs+1):
    dst=sp*h
    print(h,'\t                 ',dst,'\t',sep="")
#5
MONTH=12
totam=[0,0,0,0,0,0,0,0,0,0,0,0]
avem=[0,0,0,0,0,0,0,0,0,0,0,0]
totay=[0,0,0,0,0]
appe=['st','nd','rd','th','th']
mnn=['January','February','March','April','May','June','July','August','September','October','November','December']
YEAR=5
total=0
for yr in range(YEAR):
    print("The ",yr+1,appe[yr]," year:\n",end="",sep="")
    print("Please enter the precipitation of every month:")
    for mn in range(MONTH):
        pre=float(input(""))
        while pre<0:
            pre=float(input("An minus is invalid.Please try again:"))
        totam[mn]+=pre
        totay[yr]+=pre
for mn in range(MONTH):
    avem[mn]=totam[mn]/YEAR
for yr in range(YEAR):
    total+=totay[yr]
avey=total/YEAR
print("JAN\tFEB\tMAR\tAPR\tMAY\tJUN\tJUL\tAUG\tSEP\tOCT\tNOV\tDEC\tPERYEAR\n")
for mn in range(MONTH):
    print(format(avem[mn],'.1f'),'\t',sep="",end="")
print(avey,'\n',sep="")
#6
def Conv(cel):
    return 6*cel/5+32
print("Celcius\tFahrenheit\t")
for cel in range(0,21):
    f=Conv(cel)
    print(cel,'\t',f,'\t',sep="")
#7
base=2**(-1)
day=int(input("Please enter the number of days after the base:"))
total=0
#sum of 2*(n-1)
for d in range(day):
    base*=2
    total+=base
print("After",day,"days,he received",total,"dollars.")
#8
sum=0
pstn=float(input("Please enter a positive number:"))
while pstn>0:
    sum+=pstn
    pstn = float(input("Please enter a positive number,a negative to quit:"))
print("The sum is",sum)
#9
SPEED=1.6
print("YEAR AFTER\tRISING\t")
for yr in range(1,26):
    above=SPEED*yr
    print(yr,'\t',format(above,'.1f'),'\t',sep="")
#10
SPEED=0.03
tuition=8000
print("YEAR AFTER\tTUITION\t")
for yr in range(1,6):
    tuition=tuition*(1+SPEED)
    print(yr,'\t',format(tuition,'.1f'),'\t',sep="")
#11
DECLINE=4
w=float(input("Enter your initial weight before diet:"))
print("MONTHS AFTER\tWEIGHT\t")
for mn in range(1,7):
    w-=4
    print(mn,'\t',format(w,'.1f'),'\t',sep="")
#12
mul=1
n=int(input("Please enter a non-negative number:"))
while n<0:
    n = int(input("Please enter a non-negative number:"))
if n==0:
    print(n,'!=1.',sep='')
else:
    for a in range(1,n+1):
        mul*=a
    print(n,'!=',mul,'.',sep='')
#13
stn=int(input("Starting number of organisms:"))
str=input("Average daily increase:")
#切片法去除最后一个字符‘%’再转换成数字
dyic=int(str[:-1])/100
mtp=int(input("Number of days to multiply:"))
print("Day Approximate\tPopulation\t")
print("1\t",stn,sep="")
for d in range(2,mtp+1):
    stn*=(1+dyic)
    print(d,'\t',format(stn,'.1f'),sep="")
#14
for i in range(7,0,-1):
    for j in range(i):
        print('*',end='')
    print()
#15
for i in range(6):
    print('#',end='')
    for j in range(i):
        print(' ',end='')
    print('#')
#16
import turtle as t
t.speed(0)
#最小的正方形边长10，相邻两个正方形间隔是5
base=10
for i in range(100):
    width=base+5*i
    t.penup()
    t.goto(250, -250)
    t.setheading(90)
    t.forward(i*5)
    t.pendown()
    for j in range(2):
        t.left(90)
        t.forward(width)
#17
import turtle as t
LINELEN=300
NORTH=90
A_TURN=135
t.hideturtle()
t.penup()
t.goto(150,-150)
t.pendown()
t.setheading(NORTH)
for i in range(8):
    t.forward(LINELEN)
    t.left(A_TURN)
t.done()
#18
NORTH=90
BASE=2.5
INCREASE=4
A_TURN=90
import turtle as t
t.speed(0)
t.hideturtle()
t.setheading(NORTH)
for i in range(200):
    dst=BASE+i*INCREASE
    t.forward(dst)
    t.left(A_TURN)
#19
import turtle as t
import math as m
for i in range(8):
    t.forward(100)
    t.left(45)
t.hideturtle()
t.penup()
t.forward(50)
t.left(90)
t.forward(50*m.tan(67.5*2*3.14159265358979323/360))
t.pendown()
t.write('STOP')
t.done()