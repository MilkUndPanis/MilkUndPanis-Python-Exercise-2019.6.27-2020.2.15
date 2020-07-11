#设计题
#2
class Book:
    def __init__(self,title,author,publisher):
        self.__title=title
        self.__author=author
        self.__pbsher=publisher
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_pbsher(self):
        return self.__pbsher
    def set_title(self):
        t=input('Enter the title of the book:')
        self.__title=t
    def set_author(self):
        a = input('Enter the author of the book:')
        self.__author = a
    def set_pbsher(self):
        p = input('Enter the publisher of the book:')
        self.__pbsher = p
    def __str__(self):
        return 'Title:'+self.__title+'\nAuthor:'+self.__author+'\nPublisher'+self.__pbsher
#编程题
#1
#main.py
from pet import *
def main():
    mypet=Pet()
    mypet.set_name()
    mypet.set_animal_type()
    mypet.set_age()
    print(mypet)
main()
#2
#main.py
from car import *
def main():
    mycar=Car()
    print(mycar)
    for i in range(5):
        mycar.accelerate()
        print('Now speed:',mycar.get_speed())
    for i in range(5):
        mycar.brake()
        print('Now speed:',mycar.get_speed())
main()
#3
#main.py
from info import *
def main():
    list=[Info(),Info(),Info()]
    for i in list:
        i.set_name()
        i.set_age()
        i.set_addr()
        i.set_tel()
    myinfo=list[0]
    info_one=list[1]
    info_another=list[2]
    print('My information:')
    print(myinfo)
    print('Info A:')
    print(info_one)
    print('Info_B:')
    print(info_another)
main()
#4
#main.py
from employee import *
def main():
    SM=Employee('Susan Meyers',47899,'Accounting','Vice President')
    MJ=Employee('Mark Jones',39119,'IT','Programmer')
    JR=Employee('Joy Rogers',81774,'Manufacturing','Engineer')
    print(SM)
    print(MJ)
    print(JR)
main()
#5
#main.py
from retailitem import *
def main():
    Item1=RetailItem('Jacket',12,59.95)
    Item2=RetailItem('Designer Jeans',40,34.95)
    Item3=RetailItem('Shirt',20,24.95)
    print(Item1)
    print(Item2)
    print(Item3)
main()
#6
#main.py
from patient import *
from procedure import *
def main():
    apati=Patient('Donald Trunp','New York','114514','1919810','UNKNOWN','831723')
    pro_a=Procedure('Physical Exam','Today\'s date','Dr.Irvine','250.00')
    pro_b=Procedure('X-ray','Today\'s date','Dr.Jamison','500.00')
    pro_c=Procedure('Blood test','Today\'s date','Dr.Smith','200.00')
    print(apati)
    print('A:')
    print(pro_a)
    print('B:')
    print(pro_b)
    print('C:')
    print(pro_c)
    print()
    bpati=Patient('','','','','','')
    bpati.Set_Name()
    bpati.Set_Address()
    bpati.Set_Postal()
    bpati.Set_Tel()
    bpati.Set_Emergency()
    print(bpati)
    pro_d=Procedure('','','','')
    pro_d.Set_Proceed()
    pro_d.Set_Date()
    pro_d.Set_Doctor()
    pro_d.Set_Fee()
    print(pro_d)
main()
#7
#main.py
#Use employee.py
from employee import *
from pickle import *
#First debug:The employee.dat didn't exist.Delete 12 lines under this line;use Init_dict={}.
def MakeDict():
    fo=open('employee.dat','rb')
    idct=load(fo)
    fo.close()
    return idct
Init_dict=MakeDict()
def View():
    for id in Init_dict:
        print('ID:',end='')
        print(id)
        print(Init_dict[id])
View()
def menu():
    print('Please select your option:\n'\
          'A.Searching an employee\n'\
          'B.Adding a new employee\n'\
          'C.Editing\n'\
          'D.Deleting an employee\n'\
          'Q.Quit\n')
def getchoice():
    op=input('Your choice:')
    while op.upper()!='A' and op.upper()!='B' and op.upper()!='C'\
            and op.upper()!='D' and op.upper()!='Q':
        op=input('It is invalid.Please try again:')
    return op
def Searching():
    id=input('Enter the id of employee you want to find:')
    Find=False
    for ids in Init_dict:
        if ids==id:
            Find=True
            print('Here is the employee\'s information:')
            print(Init_dict[id])
    if Find==False:
        print('ID:',id,'don\'t exist.',sep='')
def IsExist(id):
    Find=False
    for ids in Init_dict:
        if ids==id:
            Find=True
            break
    return Find
def Adding():
    id=input('Enter the id of employee you want to add:')
    info=Employee('',id,'','')
    info.set_name()
    info.set_company()
    info.set_vocation()
    Init_dict[id]=info
def Editing():
    id = input('Enter the id of employee you want to edit:')
    if IsExist(id):
        new_info = Employee('', id, '', '')
        print('Set the new information.')
        new_info.set_name()
        new_info.set_company()
        new_info.set_vocation()
        Init_dict[id] = new_info
    else:print('This id:',id,'don\'t exist.',sep='')
def Deleting():
    id = input('Enter the id of employee you want to delete:')
    if IsExist(id):
        del Init_dict[id]
    else:print('This id:',id,'don\'t exist.',sep='')
def Dump():
    fo=open('employee.dat','wb')
    dump(Init_dict,fo)
    fo.close()
def main():
    menu()
    op=getchoice()
    while True:
        if op.upper()=='A':
            Searching()
        elif op.upper()=='B':
            Adding()
        elif op.upper()=='C':
            Editing()
        elif op.upper()=='D':
            Deleting()
        elif op.upper()=='Q':
            break
        menu()
        op=getchoice()
    Dump()
    print('That\'s all')
main()
#8
#main.py
from cashregister import *
def main():
    mycash=CashRegister()
    Item1 = RetailItem('Jacket', 12, 59.95)
    Item2 = RetailItem('Designer Jeans', 40, 34.95)
    Item3 = RetailItem('Shirt', 20, 24.95)
    mycash.purchase_item(Item1)
    mycash.purchase_item(Item2)
    mycash.purchase_item(Item3)
    print('Total price:',mycash.get_total(),sep='')
    mycash.show_item()
    mycash.clear()
    mycash.show_item()
main()
#9
#main.py
from Question import *
Trivia=[]
def SetQuestion():
    for i in range(10):
        ques=Question('','','','','','')
        print(i+1,end=':')
        ques.Set_Problem()
        ques.Set_Answers()
        ques.Set_Correct()
        Trivia.append(ques)
def get_answer():
    op=input('Your Answer:')
    an=op.upper()
    while an!='A' and an!='B' and an!='C' and an!='D':
        op=input('This is invalid.Try again:')
        an=op.upper()
    return an
def PlayerA():
    print('It\'s A\'s turn.')
    score_A=0
    for i in range(5):
        print('00'+str(i+1))
        print(Trivia[i])
        an=get_answer()
        if an==Trivia[i].Get_Correct():
            score_A+=1
        else:continue
    return score_A
def PlayerB():
    print('It\'s B\'s turn.')
    score_B=0
    for i in range(5,10):
        print('00'+str(i-4))
        print(Trivia[i])
        an=get_answer()
        if an==Trivia[i].Get_Correct():
            score_B+=1
        else:continue
    return score_B
def Checkwin(a,b):
    if a>b:
        print('A is winner.')
    elif a<b:
        print('B is winner.')
    else:print('A and B tied.')
def main():
    SetQuestion()
    score_a=PlayerA()
    score_b=PlayerB()
    Checkwin(score_a,score_b)
main()




