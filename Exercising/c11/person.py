#person.py
class Person:
    def __init__(self,nm,addr,tel):
        self.__name=nm
        self.__addr=addr
        self.__tel=tel
    def set_name(self):
        self.__name=input('Enter your name:')
    def insert_name(self,n):
        self.__name=n
    def set_addr(self):
        self.__addr=input('Enter your address:')
    def insert_addr(self,a):
        self.__addr=a
    def set_tel(self):
        self.__tel=input('Enter your telephone number:')
    def insert_tel(self,t):
        self.__tel=t
    def get_name(self):
        return self.__name
    def get_tel(self):
        return self.__tel
    def get_addr(self):
        return self.__addr
    def __str__(self):
        return 'Name:'+self.__name+'\tAddress:'+self.__addr+'\tTelephone number:'+self.__tel
class Customer(Person):
    def __init__(self,nm,addr,tel,id,if_emlist):
        Person.__init__(self,nm,addr,tel)
        self.__id=id
        self.__if_email_list=if_emlist
    def set_name(self):
        n= input('Enter the customer\'s name:')
        self.insert_name(n)
    def set_addr(self):
        a= input('Enter the customer\'s address:')
        self.insert_addr(a)
    def set_tel(self):
        t= input('Enter the customer\'s telephone number:')
        self.insert_tel(t)
    def set_id(self):
        self.__id=input('Enter the customer\'s id:')
    def set_if(self):
        op=input("Do the customer want to be added in email list?\nA.Yes\tB.No")
        sl=op.upper()
        while sl!='A' and sl!='B':
            sl=input('It is invalid.Try again:').upper()
        if sl=='A':
            self.__if_email_list=True
        else:self.__if_email_list=False
    def get_id(self):
        return self.__id
    def get_if(self):
        return self.__if_email_list
    def convert(self):
        if self.__if_email_list==True:
            return 'Yes'
        elif self.__if_email_list==False:
            return 'No'
        else:return 'UNKNOWN'
    def __str__(self):
        return Person.__str__(self)+'\tId:'+str(self.__id)+'\tWant to be added in email list?'+self.convert()
