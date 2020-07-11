#1
y=int(input("Enter a number in a week:"))
if y==1:
    print('Monday')
elif y==2:
    print('Tuesday')
elif y==3:
    print('Wednesday')
elif y==4:
    print('Thursday')
elif y==5:
    print('Friday')
elif y==6:
    print('Saturday')
elif y==7:
    print('Sunday')
else:
    print('Wrong')
#2
l_a=float(input("Enter the length of first rectangle:"))
w_a=float(input("Enter the width of first rectangle:"))
l_b=float(input("Enter the length of second rectangle:"))
w_b=float(input("Enter the width of second rectangle:"))
s_a=w_a*l_a
s_b=w_b*l_b
if s_a>s_b:
    print('First is larger.')
elif s_a<s_b:
    print('Second is larger.')
else:
    print('Their areas are equal.')
#3
age=int(input("Enter the age of a people:"))
if age<0 or age>120:
    print("A man at the age of such is not exist yet.")
elif age<=1:
    print("It is an infant.")
elif age<13:
    print("It is a child.")
elif age<20:
    print("It is a juvenile.")
else:
    print("It is an adult.")
#4
A_n=int(input("Enter an Arab number:"))
if A_n==1:
    print('I')
elif A_n==2:
    print('II')
elif A_n==3:
    print("III")
elif A_n==4:
    print("IV")
elif A_n==5:
    print("V")
elif A_n==6:
    print("VI")
elif A_n==7:
    print("VII")
elif A_n==8:
    print("VIII")
elif A_n==9:
    print("IX")
elif A_n==10:
    print("X")
else:
    print("Wrong")
#9
num=int(input("Please enter a bag num:"))
if num==0:
    print("Green.")
elif (num>=1 and num<=10) or (num>=19 and num<=28):
    if num%2 :
        print("Red.")
    else:
        print("Black.")
elif (num>=11 and num<=18) or (num>=29 and num<=36):
    if num%2:
        print("Black.")
    else:
        print("Red.")
else:
    print("Wrong.")
#10
p=int(input("Enter the number of penny:"))
n=int(input("Enter the number of nickel:"))
d=int(input("Enter the number of dime:"))
q=int(input("Enter the number of quarter:"))
a=0.01*p+0.05*n+0.1*d+0.25*q
if a==1:
    print("You are win!")
elif a>1:
    print("You are lose.The total value is above 1 dollar.")
else:
    print("You are lose.The total value is below 1 dollar.")
#13
w=float(input("Please enter the weight of baggage(by pound):"))
if w<=0:
    print("Wrong.")
else:
    if w>0 and w<=2:
      f=w*1.50
    if w>2 and w<=6:
      f=w*3.00
    if w>6 and w<=10:
      f=w*4.00
    else:
      f=w*4.75
    print("The transport fee is:$",f,sep="")
#14
w=float(input("Please enter your weight by pound:"))
h=float(input("Please enter your height by inch:"))
bmi=w*703/(h**2)
if bmi<18.5:
    print("You are too light to be fit.")
elif bmi>=18.5 and bmi<=25:
    print("You are healthy.")
else:
    print("You are too heavy.")
#15
second=int(input("Please enter a time by second:"))
if second<60:
    print("It is",second,"second.")
elif second>=60 and second<3600:
    min=second//60
    second=second%60
    print("It is",min,"minute,",second,"second.")
elif second>=3600 and second<86400:
    hour=second//3600
    min=(second%3600)//60
    second=(second%3600)%60
    print("It is",hour,"hour,",min,"minute,",second,"second.")
elif second>=86400:
    day=second//86400
    rest=second%86400
    hour=rest//3600
    min=(rest%3600)//60
    second=(rest%3600)%60
    print("It is",day,"day,", hour, "hour,", min, "minute,", second, "second.")
#16
year=int(input("Please enter a year:"))
if not(year%100):
    if not(year%400):
        print("February have 29 days.")
    else:
        print("February have 28 days.")
else:
    if not (year % 4):
        print("February have 29 days.")
    else:
        print("February have 28 days.")
#17
#该程序不涉及输入检查
NO="no"
print("Reboot the computer and try to connect.")
ans=str(input("Did that fix the problem?"))
if ans==NO:
    print("Reboot the router and try to connect.")
    ans=str(input("Did that fix the problem?"))
    if ans==NO:
        print("Make sure the cable connector that connects the router and the modem is firmly plugged into the slot.")
        ans = str(input("Did that fix the problem?"))
        if ans==NO:
            print("Move the router to a new location..")
            ans = str(input("Did that fix the problem?"))
            if ans==NO:
                print("Get a new router.")
#18
#三家餐厅的信息，info中使用1与0区别是否提供素食、严格素食、无麸质饮食，choice中使用0和1区分是否被排除出可选择范围
info=[[0,0,0],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]
choice=[1,1,1,1,1]
name=['Joe \'s Gourmet Burgers','Main Street Pizza Company','Corner Cafe','Mama \'s Fine Italian','The Chef\'s Kitchen']

ans=str(input("Is anyone in your party a vegetarian?"))
if ans=='yes':
    choice[0]=0
ans = str(input("Is anyone in your party a vegan?"))
if ans == 'yes':
    choice[0]=0
    choice[1]=0
    choice[3]=0
ans = str(input("Is anyone in your party gluten-free?"))
if ans == 'yes':
    choice[0]=0
print("Here are your restaurant choices:")
for num in range(0,5):
    if choice[num]:
        print(name[num])
#19
import turtle
import math
SCREEN_WIDTH=600
SCREEN_HEIGHT=600
TARGET_LLEFT_X=100
TARGET_LLEFT_Y=250
TARGET_WIDTH=25
FORCE_FACTOR=30
PROJECTILE_SPEED=1
NORTH=90
EAST=0
SOUTH=270
WEST=180
turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()
turtle.goto(0,0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)
angle=float(input("Enter the projectile's angle:"))
force=float(input("Enter the launch force(1-10):"))
distance=force*FORCE_FACTOR
turtle.setheading(angle)
turtle.pendown()
turtle.forward(distance)
if (turtle.xcor()>=TARGET_LLEFT_X and turtle.xcor()<=(TARGET_LLEFT_X+TARGET_WIDTH)
    and turtle.ycor()>=TARGET_LLEFT_Y and turtle.ycor()<=(TARGET_LLEFT_Y+TARGET_WIDTH)):
    print('Target hit!')
else:
    print('You miss the target.')
    d_min=math.sqrt(100**2+250**2)
    d_max=math.sqrt(130**2+280**2)
    angle_min=math.atan(250/130)
    angle_max=math.atan(280/100)
    if angle<angle_min:
        print("Try a greater angle.")
    elif angle>angle_max:
        print("Try a smaller angle.")
    if distance<d_min:
        print("Use more force.")
    elif distance>d_max:
        print("Use less force.")
