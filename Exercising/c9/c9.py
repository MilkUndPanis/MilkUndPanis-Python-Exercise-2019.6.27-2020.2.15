#1
def main():
    Classroom={'CS101':3004,'CS102':4501,'CS103':6755,'NT110':1244,'CM241':1411}
    Teacher={'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
    Time={'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}
    key=input('Enter a course-number:')
    print(Classroom[key])
    print(Teacher[key])
    print(Time[key])
main()
#2
#Including seven states
def main():
    state_cap={'Alaska':'Anchorage','Arizona':'Phoenix','Alabama':'Birmingham','California':'Sacramento',
               'Connecticut':'Hartford','Georgia':'Atlanta','Florida':'Tallahassee'}
    op='Y'
    while op=='Y':
        right=0
        error=0
        for key in state_cap:
            print('What is the capital of',key,':',end='')
            cap=input()
            new_answer=cap[0].upper()+cap[1:].lower()
            if new_answer==state_cap[key]:
                right+=1
            else:
                error+=1
        print('You have',right,'right and',error,'error.')
        op=input('Do you want to continue?')
    print('That\'s all')
main()
#3
rule={'A':'!','a':'@','B':'#','b':'$','C':'%','c':'^','D':'&','d':'*','E':'(','e':')','F':'Q','f':'W',
      'G':'E','g':'r','H':'t','h':'Y','I':'u','i':'I','J':'o','j':'p','K':'P','k':'ui','L':'we','l':'wo',
      'M':'s','m':'wr','N':'wq','n':'ws','O':'a','o':'sp','P':'x','p':'z','Q':'wx','q':'zx','R':'ze','r':'er',
      'S':'df','s':'d','T':'pl','t':'rf','U':'bn','u':'ao','V':'hx','v':'sj','W':'sh','w':'ji','X':'dh','x':'wdj',
      'Y':'xr','y':'iw','Z':'hdw','z':'jp'}
rule['\'']='^'
rule['.']='$&'
rule[',']='&*'
rule[' ']=' '
def crypt(line):
    result=''
    for ch in line:
        result+=rule[ch]
    return result
def encrypt():
    fin=open('becrypt.txt','r')
    fout=open('crypted_regularly.txt','w')
    con=fin.readlines()
    for i in range(len(con)):
        con[i]=con[i].rstrip('\n')
    for line in con:
        fout.write(crypt(line)+'\n')
    fin.close()
    fout.close()
def read():
    fo=open('crypted_regularly.txt','r')
    list=fo.readlines()
    for line in list:
        print(line,end='')
def main():
    encrypt()
    read()
main()
#4
def main():
    fo=open('becrypt.txt','r')
    list=fo.readlines()
    for i in range(len(list)):
        list[i]=list[i].rstrip('\n')
    words=[]
    for line in list:
        words+=line.split(' ')
    words_only=set(words)
    print('The total word list:')
    i=0
    for val in words_only:
        print(val,end=' ')
        i+=1
        if i%5==0:
            print('\n',end='')
main()
#5
def main():
    fo=open('becrypt.txt','r')
    list=fo.readlines()
    for i in range(len(list)):
        list[i]=list[i].rstrip('\n')
    words=[]
    for line in list:
        words+=line.split(' ')
    words_only=set(words)
    freq={}
    for val in words_only:
        times=0
        for w in words:
            if w==val:
                times+=1
        freq[val]=times
    print('This is times the every word appeared:')
    for key in freq:
        print(key,":",freq[key],sep='')
main()
#6
def printset(set):
    i=0
    for val in set:
        print(val,end=' ')
        i+=1
        if i%25==0:
            print('\n',end='')
def make_file():
    fo=open('pre-file2.txt',mode='r',encoding='UTF-8')
    fi=open('file2.txt',encoding='UTF-8',mode='w')
    list_pre=fo.readlines()
    for i in range(len(list_pre)):
        list_pre[i]=list_pre[i].rstrip('\n')
    for line in list_pre:
        line_new_list=[]
        lnwrd=line.split(' ')
        for word in lnwrd:
            new_wrd=''
            for ch in word:
                if ch=='\'' or ch=='.' or ch=='\"' or ch=='(' or ch==')' or ch==',' or ch=='’' or ch=='-' or ch==':':
                    continue
                else:new_wrd+=ch
            line_new_list.append(new_wrd)#Adding element use append()
        new_line=''
        for w in line_new_list:
            new_line+=(w+' ')
        new_line.rstrip(' ')
        fi.write(new_line+'\n')
    fo.close()
    fi.close()
def analyzing():
    f1=open('file1.txt','r')
    f2=open('file2.txt','r')
    list1=f1.readlines()
    list2=f2.readlines()
    for i in range(len(list1)):
        list1[i]=list1[i].rstrip('\n')
    for i in range(len(list2)):
        list2[i]=list2[i].rstrip('\n')
    words1=[]
    words2=[]
    for line in list1:
        words1+=line.split(' ')#Merging lists use +
    for line in list2:
        words2+=line.split()
    word_set1=set(words1)
    word_set2=set(words2)
    print('The set of words in file1.txt:')
    printset(word_set1)
    print('\nThe set of words in file2.txt:')
    printset(word_set2)
    print('\nThe set of words that appeared in both two files:')
    printset(word_set1&word_set2)
    print('\nThe set of words that only appeared in file1.txt:')
    printset(word_set1-word_set2)
    print('\nThe set of words that only appeared in file2.txt:')
    printset(word_set2 - word_set1)
    print('\nThe set of words that only appeared in one of two files:')
    printset(word_set1^word_set2)
def main():
    make_file()
    analyzing()
main()
#7
def main():
    fo=open('WorldSeriesWinners.txt','r')
    list=fo.readlines()
    for i in range(len(list)):
        list[i]=list[i].rstrip('\n')
    winner_set=set(list)
    team_times={}
    for val in winner_set:
        times=0
        for line in list:
            if val==line:
                times+=1
        team_times[val]=times
    year_winner={}
    year_winner[1903]=list[0]
    j=1
    for i in range(1905,2009):
        if i==1994:
            continue
        else:
            year_winner[i]=list[j]
            j+=1
    year=int(input('Enter a year:'))
    print(year_winner[year],'won in this year.The team had won',team_times[year_winner[year]],'times.')
main()
#8
import pickle as p
def main():
    print('Please select what you want to do:')
    print('A.Searching\tB.Add a new\tC.Editing\tD.Deleting')
    print('Your choice:')
    op=input()
    if op.upper()!='A' and op.upper()!='B' and op.upper()!='C' and op.upper()!='D':
        op=input('It is invalid.Please try again:')
    if op.upper()=='A':
        fo = open('name_email.dat', 'rb')
        emails = p.load(fo)
        e_list = {}
        for line in emails:
            print(line)
            e_list[line.split()[0]] = line.split()[1]
        name=input('Please enter the name you want to search:')
        email=e_list.get(name,'CAN NOT FOUND')
        print('His\Her email:',email)
        fo.close()
    elif op.upper()=='B':
        name=input('New item\'s name:')
        email=input('His\Her email:')
        new_twin={name:email}
        fo = open('name_email.dat', 'ab')
        p.dump(new_twin,fo)
        fo.close()
    elif op.upper()=='C':
        fo = open('name_email.dat', 'rb')
        fi = open('name_email.dat', 'wb')
        emails = p.load(fo)
        e_list = {}
        for line in emails:
            e_list[line.split(':')[0]] = line.split(':')[1]
        fo.close()
        name=input('Enter the item\'s name you want to edit:')
        while True:
            Exist=False
            for key in e_list:
                if key==name:
                    Exist=True
            if Exist==False:
                name=input('This item is unexist.Please try again:')
            else:break
        e_list[name]=input('New email:')
        p.dump(e_list,fi)
        fi.close()
    elif op.upper()=='D':
        fo = open('name_email.dat', 'rb')
        fi = open('name_email.dat', 'wb')
        emails = p.load(fo)
        e_list = {}
        for line in emails:
            e_list[line.split(':')[0]] = line.split(':')[1]
        fo.close()
        name=input('Enter the name of item you want to delete:')
        while True:
            if e_list.pop(name,'NOTFOUND')=='NOTFOUND':
                name = input('This item is unexist.Please try again:')
            else:break
        p.dump(e_list, fi)
        fi.close()
main()
#10
def main():
    fo=open('Kennedy.txt','r')
    list=fo.readlines()
    for i in range(len(list)):
        list[i]=list[i].rstrip('\n')
    totalword=[]
    for line in list:
        words_of_a_line=line.split()
        totalword+=words_of_a_line
    wordset=set(totalword)
    times={}
    for val in wordset:
        ap_line=[]
        for i in range(len(list)):
            words_of_a_line = list[i].split()
            for wrd in words_of_a_line:
                if wrd==val:
                    ap_line.append(i+1)
        times[val]=set(ap_line)
    fi=open('index.txt','w')
    for key in times:
        fi.write(key+':')
        for linenum in times[key]:
            fi.write(str(linenum)+' ')
        fi.write('\n')
    fo.close()
main()









