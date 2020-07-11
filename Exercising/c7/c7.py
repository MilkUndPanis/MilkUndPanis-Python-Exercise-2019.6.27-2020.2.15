from matplotlib.pyplot import *
def main():
    xcor=[1,3,5,7,9,11,13,15,17,19]
    ycor=[4,22,3,4,12,43,12,12,4,132]
    plot(xcor,ycor,marker='D')
    title('Normal')
    xlabel('X')
    ylabel('Y')
    xticks([1,3,5,7,9,11,13,15,17,19],['$1','$3','$5','$7','$9','$11','$13','$15','$17','$19'])
    grid(True)
    xlim(0,20)
    ylim(0,200)
    show()
    edge=xcor.copy()
    height=ycor.copy()
    bar(edge,height,1,color=('b','g','c','b','g','c','b','g','c','b'))
    show()
    values=ycor[:-5]
    pie(values,labels=['a','b','c','d','e'],colors=('b','g','c','r','m'))
    show()
main()
#1
def main():
    sales=[]
    print('Enter the sales of everyday in a week:')
    for day in range(7):
        sales.append(int(input()))
    print("Total sales:",sum(sales),sep='')
main()
#2
from random import *
def main():
    randi=[]
    for data in range(7):
        randi.append(randint(0,9))
    for data in range(7):
        print(data+1,':',randi[data],sep='')
main()
#3
def aver(list):
    return sum(list)/len(list)
def main():
    precip=[]
    print('Please enter the precipitation of 12 months:')
    for month in range(12):
        precip.append(float(input()))
    print('Total precipitation:',format(sum(precip),'.2f'),sep='')
    print('Average month rainfall:',format(aver(precip),'.2f'),sep='')
    print('Maximum:',format(max(precip),'.2f'))
    print('Minimum:',format(min(precip),'.2f'))
main()
#4
def main():
    num=[]
    print('Enter 20 numbers:')
    for data in range(20):
        num.append(float(input()))
    print('Maximum:',format(max(num),'.2f'),sep='')
    print('Minimum:', format(min(num), '.2f'), sep='')
    print('Sum:', format(sum(num), '.2f'), sep='')
    print('Average:', format(sum(num)/len(num), '.2f'), sep='')
main()
#5
def main():
    filename='charge_accounts.txt'
    fo=open(filename,'r')
    accounts=fo.readlines()
    for i in range(len(accounts)):
        accounts[i]=accounts[i].rstrip('\n')
    test=input('Please enter an account:')
    Found=False
    for i in range(len(accounts)):
        if accounts[i]==test:
            Found=True
            print('This account is valid.')
    if Found==False:
        print('This account is invalid.')
    fo.close()
main()
#6
def Larger(list,n):
    for i in range(len(list)):
        if list[i]>n:
            print(list[i])
def main():
    list=[79,46,83,25,18,51]
    Larger(list,31)
main()
#7
def main():
    cr_aw=['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
    fo=open('myanswer.txt','r')
    my_an=fo.readlines()
    for i in range(len(my_an)):
        my_an[i]=my_an[i].rstrip('\n')
    Pass=True
    correct=0
    error=0
    error_que=[]
    for i in range(len(my_an)):
        if my_an[i]!=cr_aw[i]:
            error+=1
            error_que.append(i+1)
        else:correct+=1
    if error>5:
        Pass=False
    if Pass==True:
        print('Pass the exam.')
    else:
        print('Not pass.')
    print('Correct:',correct,sep='')
    print('Error:',error,sep='')
    print('List of erroneous question:',error_que,sep='')
    fo.close()
main()
#8
def Hottest(name,list):
    Hot=False
    for i in range(len(list)):
        if list[i]==name:
            Hot=True
            print('The name is one of the hottest name.')
            break
    if Hot==False:
        print('The name isn\'t one of the hottest name')
def main():
    fo_a=open('GirlNames.txt','r')
    fo_b=open('BoyNames.txt','r')
    name_g=fo_a.readlines()
    name_b=fo_b.readlines()
    for i in range(len(name_g)):
        name_g[i]=name_g[i].rstrip('\n')
    for j in range(len(name_b)):
        name_b[i]=name_b[i].rstrip('\n')
    get=input('Want to enter a name of___:\nA.Girl\tB.Boy\tC.Both\t')
    while get!='A' or get!='B' or get!='C':
        get = input('Invalid choice,Try again:')
    if get=='A':
        gname=input('Enter a girl\'s name:')
        Hottest(gname,name_g)
    elif get=='B':
        bname=input('Enter a boy\'s name:')
        Hottest(bname,name_b)
    elif get=='C':
        name=input('Enter a name:')
        Hottest(name,name_g+name_b)
    fo_a.close()
    fo_b.close()
main()
#9
from matplotlib.pyplot import *
#1900-2018 unit:million(10**6)
def main():
    pop=open('USPopulation.txt','r')
    pop_list=pop.readlines()
    for i in range(len(pop_list)):
        pop_list[i]=float(pop_list[i].rstrip('\n'))
    #[0]:1900,[1]:1901,...[119]:2019
    diff=[]
    for i in range(1,len(pop_list)):
        differ=pop_list[i]-pop_list[i-1]
        diff.append(differ)
    print('This is the variance of population per year:')
    for i in range(len(diff)):
        print(1900+i,'~',1901+i,':',format(diff[i],'.2f'),end='\t',sep='')
        if i%5==0:
            print('\n',end='')
    print()
    print('The minimum variance happened in:',1900+diff.index(min(diff)),'~',1901+diff.index(min(diff)),sep='')
    print('The maximum variance happened in:', 1900 + diff.index(max(diff)), '~', 1901 + diff.index(max(diff)),sep='')
    xcor=[]
    for i in range(1900,2020,1):
        xcor.append(i)
    ycor=pop_list
    plot(xcor,ycor,marker='D')
    xlabel('Year')
    ylabel('Population by million')
    title('US Population:1900-2019')
    grid(True)
    xlim(1900,2019)
    ylim(76,330)
    show()
    pop.close()
main()
#10
def main():
    filename='WorldSeriesWinner.txt'
    fo=open(filename,'r')
    winner=fo.readlines()
    for i in range(len(winner)):
        winner[i]=winner[i].rstrip('\n')
    team=input('Please enter a team:')
    win=0
    for i in range(len(winner)):
        if winner[i]==team:
            win+=1
    print("The team had won",win,"times.")
    fo.close()
main()
#11
def Russell(list):
    total=0
    for i in range(len(list)):
        for j in range(len(list[i])):
            total+=list[i][j]
        if total!=15:
            return False
        total=0
    total=0
    for j in range(len(list)):
        for i in range(len(list[j])):
            total+=list[i][j]
        if total!=15:
            return False
        total=0
    total=0
    for i in range(len(list)):
         total+=list[i][i]
    if total!=15:
        return False
    total=0
    for i in range(len(list)):
        total+=list[i][len(list)-1-i]
    if total!=15:
        return False
    return True
def main():
    list=[[4,9,2],[3,5,7],[8,1,7]]
    if Russell(list):
        print('The matrix is a Russell matrix.')
    else:
        print('The matrix is not a Russell matrix.')
main()
#12
def IsPrime(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True
def main():
    num=int(input('Please enter a num above 2:'))
    while num<2:
        num=int(input('The number is too small.Please retry:'))
    prime=[]
    for i in range(2,num+1,1):
        if IsPrime(i):
            prime.append(i)
    print('Primes range from 2 to',num)
    print(prime)
main()
#13
from random import *
def main():
    fullname='8_ball_responses.txt'
    fo=open(fullname,'r')
    answers=fo.readlines()
    for i in range(12):
        answers[i]=answers[i].rstrip('\n')
    cont='y'
    while cont=='y':
        ques=input('Your question:')
        n=randrange(1,13)
        print(answers[n])
        cont=input('Do you want to continue(Press y to continue):')
    print('That\'s all.')
main()
#14
from matplotlib.pyplot import *
def main():
    fo=open('myspend.txt','r')
    spends=fo.readlines()
    for i in range(len(spends)):
        spends[i]=spends[i].rstrip('\n')
    pie(spends,labels=['rent','gas','food','clothes','car','others'],colors=('r','g','c','y','b','m'))
    show()
main()
#15
from matplotlib.pyplot import *
def main():
    fo=open('1994_Weekly_Gas_Averages.txt','r')
    gas=fo.readlines()
    x_cor=[]
    for i in range(52):
        gas[i]=float(gas[i].rstrip('\n'))
        x_cor.append(i+1)
    plot(x_cor,gas,marker='*')
    xlim(1,52)
    ylim(1.00,5.00)
    grid(True)
    title('1994 Weekly Gas Averages')
    xlabel('Week')
    ylabel('Gas Price($)')
    show()
main()