#1
def main():
    fo=open('number_list.txt','r')
    for num in fo:
        print(int(num))
    fo.close()
main()
#2
def main():
    filename=input('Please enter a file name:')
    fo=open(filename.rstrip('\n'),'r')
    line=fo.readline()
    count=0
    while line!='':
        print(line.rstrip('\n'))
        count+=1
        if count>=5:
            break
        line=fo.readline()
    fo.close()
main()
#3
def main():
    filename = input('Please enter a file name:')
    fo = open(filename.rstrip('\n'), 'r')
    line = fo.readline()
    count = 0
    while line != '':
        print(count+1,':',line.rstrip('\n'),sep='')
        count += 1
        line = fo.readline()
    fo.close()
main()
#4
def main():
    filename=input('Please enter a filename:')
    fo=open(filename,'r')
    line=fo.readline()
    data=0
    while line!='':
        data+=1
        line=fo.readline()
    print("The file concludes",data,"names.")
    fo.close()
main()
#5
def main():
    filename=input('Please enter a filename:')
    fo=open(filename.rstrip('\n'),'r')
    total=0
    for line in fo:
        total+=int(line)
    fo.close()
    print("Sum of data:",total,sep='')
main()
#6
def main():
    filename=input('Please enter a filename:')
    fo=open(filename.rstrip('\n'),'r')
    total=0
    data=0
    for line in fo:
        data+=1
        total+=int(line)
    fo.close()
    aver=total/data
    print("Average of data:",aver,sep='')
main()
#7
def main():
    import random as r
    fo=open('number_list.txt','w')
    data=int(input("Please enter the amount of random numbers:"))
    for i in range(data):
        fo.write(str(r.randint(1,500))+'\n')
    fo.close()
main()
#8
def main():
    fo=open('number_list.txt','r')
    data=0
    sum=0
    for line in fo:
        print(line)
        data+=1
        sum+=int(line)
    print("Data:",data,sep='')
    print("Sum:",sum,sep='')
main()
#9
def main():
    filename=input('Please enter a filename:')
    try:
        fo=open(filename.rstrip('\n'),'r')
        total=0
        data=0
        for line in fo:
            data+=1
            total+=int(line)
        fo.close()
    except IOError:
        print("File's reading or writing error.")
    except ValueError:
        print("Error occurred while turning string to integer.")
    else:
        aver=total/data
        print("Average of data:",aver,sep='')
main()
#10
def main_a():
    fo=open('golf.txt','w')
    con='y'
    while con=='y':
        name = input('Please enter a name:')
        score = float(input("Enter his score:"))
        fo.write(name+'\n')
        fo.write(str(score)+'\n')
        con=input("Do you want to continue?")
    fo.close()
def main_b():
    fo=open('golf.txt','r')
    name=fo.readline().rstrip('\n')
    while name!='':
        score=fo.readline().rstrip('\n')
        print(name,':',format(float(score),'.2f'),sep='')
        name = fo.readline().rstrip('\n')
    fo.close()
def main():
    main_a()
    main_b()
main()
#11
def main():
    filename='Introduction.html'
    name=input('Enter your name:')
    describe=input('Describe youself:')
    fo=open(filename,'w')
    fo.write('<html>\n'+
             '<head>\n'+
             '</head>\n'+
             '<body>\n'+
             '  <center>\n'+
             '      <h1>'+name+'</h1>\n'+
             '  </center>\n'+
             '  <hr />\n'+
             '  '+describe.rstrip('\n')+'\n'+
             '  <hr />\n'+
             '</body>\n'+
             '</html>\n')
    fo.close()
main()
#12
def months(a):
    if a==1:return 'Jan'
    elif a==2:return 'Feb'
    elif a==3:return 'Mar'
    elif a==4:return 'Apr'
    elif a==5:return 'May'
    elif a==6:return 'Jun'
    elif a==7:return 'Jul'
    elif a==8:return 'Aug'
    elif a==9:return 'Sep'
    elif a==10:return 'Oct'
    elif a==11:return 'Nov'
    elif a==12:return 'Dec'
def main_a():
    import random as r
    fo=open('steps.txt','w')
    for i in range(365):
        fo.write(str(r.randint(1,20000))+'\n')
    fo.close()
def main_b():
    fo=open('steps.txt','r')
    day=0
    month=1
    steps=0
    print('Average steps per month:')
    for line in fo:
        steps+=int(line.rstrip('\n'))
        day+=1
        if ((month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and day==31)or ((month==4 or month==6 or month==9 or month==11) and day==30) or (month==2 and day==28):
            average=steps/day
            print(months(month),':',format(float(average),'.2f'),sep='')
            day=0
            steps=0
            month+=1
    fo.close()
def main():
    main_a()
    main_b()
main()





