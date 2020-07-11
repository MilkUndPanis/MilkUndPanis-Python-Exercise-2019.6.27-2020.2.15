#1
def main():
    name=input('Enter your name(Given Middle Family):')
    for string in name.split():
        print(string[0],end='.')
main()
#2
def main():
    series=input('Enter a series of number:')
    total=0
    for i in range(len(series)):
        total+=int(series[i])
    print(total)
main()
#3
def month(a):
    if a==1:return 'January'
    elif a==2:return 'February'
    elif a==3:return 'March'
    elif a==4:return 'April'
    elif a==5:return 'May'
    elif a==6:return 'June'
    elif a==7:return 'July'
    elif a==8:return 'August'
    elif a==9:return 'September'
    elif a==10:return 'October'
    elif a==11:return 'November'
    elif a==12:return 'December'
    else:return 'NA'
def main():
    time=input('Please enter a time just like mm/dd/yyyy:')
    t=time.split('/')
    print(month(int(t[0])),t[1],end=',')
    print(t[2])
main()
#4
def morse(ch):
    if ch==' ':return ch
    elif ch=='.':return '--..--'
    elif ch==',':return '.-.-.-'
    elif ch=='?':return '..--..'
    else:
        for i in range(0,6,1):
            if int(ch)==i:
                return '.'*i+'-'*(5-i)
        for i in range(6,10,1):
            if int(ch)==i:
                return '-'*(i-5)+'.'*(10-i)
def main():
    str=input('Enter a series of numbers,spaces,comma,period and question mark:')
    for i in range(len(str)):
        print(morse(str[i]),end=' ')
main()
#5
def turn(ch):
    if ch=='A' or ch=='B' or ch=='C':
        return '2'
    elif ch=='D' or ch=='E' or ch=='F':
        return '3'
    elif ch=='G' or ch=='H' or ch=='I':
        return '4'
    elif ch=='J' or ch=='K' or ch=='L':
        return '5'
    elif ch=='M' or ch=='N' or ch=='O':
        return '6'
    elif ch=='P' or ch=='Q' or ch=='R' or ch=='S':
        return '7'
    elif ch=='T' or ch=='U' or ch=='V':
        return '8'
    elif ch=='W' or ch=='X' or ch=='Y' or ch=='Z':
        return '9'
    else:return ch
def main():
    tel=input('Enter a telephone number like XXX-XXX-XXXX:')
    t=tel.split('-')
    newtel=''
    for i in range(3):
        for j in range(len(t[i])):
            newtel+=turn(t[i][j])
        newtel+='-'
    newtel=newtel.rstrip('-')
    print(newtel)
main()
#6
def main():
    fo=open('text.txt','r')
    all=fo.readlines()
    for i in range(len(all)):
        all[i]=all[i].rstrip('\n')
    words=0
    for i in range(len(all)):
        words+=len(all[i].split())
    av=words/len(all)
    print('The average word of every single sentence is:',format(av,'.2f'),sep='')
main()
#7
def main():
    fo=open('text.txt','r')
    all=fo.readlines()
    for i in range(len(all)):
        all[i]=all[i].rstrip('\n')
    space=0
    digit=0
    upper=0
    lower=0
    for i in range(len(all)):
        for j in range(len(all[i])):
            if all[i][j].isspace():
                space+=1
            elif all[i][j].isdigit():
                digit+=1
            elif all[i][j].isupper():
                upper+=1
            elif all[i][j].islower():
                lower+=1
    print(space,'spaces,',digit,'digits,',upper,'capitals,',lower,'lower letters.')
main()
#8
def main():
    str=input()
    list=str.split('.')
    new_str=''
    for i in range(0,len(list)):
        new_str+=list[i][0].upper()
        for j in range(1,len(list[i])):
            new_str+=list[i][j]
        new_str+='.'
    new_str=new_str.rstrip('.')
    print(new_str)
main()
#9
def isVowel(str):
    if str.upper()=='A' or str.upper()=='E' or str.upper()=='I' or str.upper()=='O' or str.upper()=='U':
        return True
    else: return False
def isConsonant(str):
    return not(isVowel(str))
def CountVowel(str):
    vowel=0
    for ch in str:
        if isVowel(ch):
            vowel+=1
    return vowel
def CountConsonant(str):
    conso=0
    for ch in str:
        if isConsonant(ch):
            conso+=1
    return conso
def StrAssess():
    str=input('Enter your string:')
    v=CountVowel(str)
    c=CountConsonant(str)
    print('There is',c,'consonants,',v,'vowels.')
    print('VOWELS:CONSONANTS=',format(v/c,'.2f'))
def FileAssess():
    filename=input('File name:')
    fo=open(filename,'r')
    all=fo.readlines()
    v=0
    c=0
    for line in all:
        v+=CountVowel(line)
        c+=CountConsonant(line)
    print('There is', c, 'consonants,', v, 'vowels.')
    print('VOWELS:CONSONANTS=', format(v / c, '.2f'))
def main():
    ch=input('Choose the mode:\nA.File\tB.Single String\tQ.Quit\t')
    CH=ch.upper()
    while CH!='A' and CH!='B' and CH!='Q':
        ch=input('INVALID.PLEASE TRY AGAIN:')
        CH=ch.upper()
    while CH=='A' or CH=='B':
        if CH=='A':
            FileAssess()
        else: StrAssess()
        ch = input('Choose the mode:\nA.File\tB.Single String\tQ.Quit\t')
        CH = ch.upper()
        while CH != 'A' and CH != 'B' and CH != 'Q':
            ch = input('INVALID.PLEASE TRY AGAIN:')
            CH = ch.upper()
    print('THAT\'S ALL')
main()
#10
def compress(str):
    new_str=''
    for ch in str:
        Rep=False
        for c in new_str:
            if ch==c:
                Rep=True
        if Rep==False:
            new_str+=ch
    return new_str
def main():
    str=input('Please enter your string:')
    p=compress(str)
    time_collect=[]
    for ch in p:
        time_collect.append(str.count(ch))
    maxch=p[time_collect.index(max(time_collect))]
    print('The most often appeared character:',maxch)
main()
#11
def main():
    str=input()
    new_str=str[0]
    for i in range(1,len(str)):
        if str[i].isupper():
            new_str+=(' '+str[i].lower())
        else:new_str+=str[i]
    print(new_str)
main()
#12
def PL(word):
    ch=word[0]
    new_str=''
    for i in range(1,len(word)):
        new_str+=word[i]
    new_str+=(ch+'ay')
    return new_str
def PigLatin(sentence):
    new_sen=''
    word_list=sentence.split()
    for word in word_list:
        new_sen+=(PL(word)+' ')
    new_sen=new_sen.rstrip(' ')
    return new_sen
def main():
    sen=input()
    print(PigLatin(sen))
main()
#13
from random import *
def STR(i):
    if i<10:
        return '0'+str(i)
    else:
        return str(i)
def FileCreater():
    fo=open('pbnumbers.txt','w')
    for i in range(109):
        line=''
        for i in range(5):
            line+=(STR(randint(1,69))+' ')
        line+=(STR(randint(1,26))+'\n')
        fo.write(line)
    fo.close()
def Count(list,cp):
    count=0
    for va in list:
        if va==cp:
            count+=1
    return count
def main():
    FileCreater()
    fo=open('pbnumbers.txt','r')
    all=fo.readlines()
    for line in all:
        line=line.rstrip('\n')
    lst=[]
    for line in all:
        lst+=line.split()
    #lst is a list of all 654 numbers(in string mode)
    times=[]
    for i in range(69):
        #0-68->1-69
        times.append(Count(lst,STR(i+1)))
    #times is a list of appeared times(number one's appeared times saves in index 0,and so on)
    max_in=times.index(max(times))+1
    min_in=times.index(min(times))+1
    print('The most often appeared number is:',max_in)
    print('The most rarely appeared number is:',min_in)
    never=[]
    for i in range(69):
        if times[i]==0:
            never.append(i+1)
    print('Never appeared numbers:')
    print(never)
    O_S=[]
    O_T=[]
    for i in range(654):
        #1-26 numbers' index satisfy the condition:(i+1)%4==0(6,12,18,...->5,11,17,...)
        if (i+1)%6==0:
            O_T.append(int(lst[i]))
        else:O_S.append(int(lst[i]))
    O_S_frequency=[]
    for i in range(1,70,1):
        O_S_frequency.append(format((O_S.count(i))/len(O_S),'.2%'))
    O_T_frequency=[]
    for i in range(1,27,1):
        O_T_frequency.append(format((O_T.count(i))/len(O_T),'.2%'))
    print('Every number\'s frequency of 1-69:')
    print(O_S_frequency)
    print('Every number\'s frequency of 1-26:')
    print(O_T_frequency)
main()
#14
def STR(a):
    if a<10:
        return '0'+str(a)
    else:return str(a)
def INT(s):
    if s[0]=='0':
        n_s=s.lstrip('0')
        return int(n_s)
    else:return int(s)
def average_price_per_year(dic):
    total=0
    for key in dic:
        total+=float(dic[key])
    return total/len(dic)
def average_price_per_month(dic):
    temp_total=0
    averages=[]
    i = 0
    START=True
    for key in dic:
        #key is like 04-05-1993
        #4->04,5->05
        if START:
            base=INT(key.split('-')[0])
        START=False
        if key.split('-')[0]==STR(base):
            temp_total+=float(dic[key])
            i+=1
        else:
            base+=1
            averages.append(format(temp_total/i,'.2f'))
            i=0
            temp_total=0
    averages.append(format(temp_total / i, '.2f'))
    return averages
def key(dic,value):
    for keis in dic:
        if dic[keis]==value:
            return keis
    return 'N/A'
def max_price_in_a_year(dic):
    prices=dic.values()
    return {key(dic,max(prices)):max((prices))}
def min_price_in_a_year(dic):
    prices = dic.values()
    return {key(dic, min(prices)): min((prices))}
def Low_To_High(dic):
    #lambdax:y中x表示输出参数，y表示lambda 函数的返回值
    return sorted(dic.items(),key=lambda item:item[1])
def High_To_Low(dic):
    return sorted(dic.items(),key=lambda item:item[1],reverse=True)
def main():
    fo=open('GasPrices.txt','r')
    all=fo.readlines()
    for i in range(len(all)):
        all[i]=all[i].rstrip('\n')
    #all is a list which saves every week(every line)'s gas price from 1993-4-5 to 2013-8-26.
    #key is a list which saves the date and
    #value is a list saves the price.
    key=[]
    value=[]
    for i in range(len(all)):
        #temp is a list of two part of a string like '04-05-1993:1.068'
        #a part is just like '04-05-1993'(in index=0)
        #and another part is like '1.068'(in index=1)
        temp=all[i].split(':')
        key.append(temp[0])
        value.append(temp[1])
    dic={}
    for i in range(len(all)):
        dic[key[i]]=value[i]
    #Above combines key and value to a dictionary.
    #1993-2013 21 years
    l_1993_2013=[]
    base=1993
    temp = {}
    for keis in dic:
        #keis is a key('04-05-1993')
        #keis.split('-') creates a list like ['04','05','1993']
        #so keis.split('-')[2] is a string like '1993'(year).
        if keis.split('-')[2]==str(base):
            temp[keis]=dic[keis]
        else:
            #year need to refresh.
            base+=1
            l_1993_2013.append(temp)
            temp={}
            temp[keis]=dic[keis]
    l_1993_2013.append(temp)
    #l_1993_2013:
    #[0]:every week in 1993;[1]:1994;and so on
    #Each element of l_1993_2013 is a dictionary
    #it contains element like '04-05-1993':'1.068'
    average=[]
    for i in range(21):
        average.append(format(average_price_per_year(l_1993_2013[i]),'.2f'))
    #average:
    #[0]:1993 average;[1]:1994 average;and so on
    #It is a list.
    #Following shows average price per year:
    print('Gas price per year:')
    for i in range(21):
        print(1993+i,':$',average[i])
    #Following shows average price per month:
    for year in range(1993,2014,1):
        print('Gas price per month in',year,':')
        print(average_price_per_month(l_1993_2013[year-1993]))
    #Max and min
    for year in range(1993, 2014, 1):
        print('Maximum gas price per month in', year, ':')
        print(max_price_in_a_year(l_1993_2013[year - 1993]))
    for year in range(1993, 2014, 1):
        print('Minimum gas price per month in', year, ':')
        print(min_price_in_a_year(l_1993_2013[year - 1993]))
    #Sorting and writing to two files
    lth=Low_To_High(dic)
    fo_a=open('low_to_high.txt','w')
    for i in range(len(lth)):
        line=''
        line+=(lth[i][0]+':'+lth[i][1]+'\n')
        fo_a.write(line)
    fo_a.close()
    htl = High_To_Low(dic)
    fo_b = open('high_to_low.txt', 'w')
    for i in range(len(htl)):
        line = ''
        line += (htl[i][0] + ':' + htl[i][1] + '\n')
        fo_b.write(line)
    fo_b.close()
main()










