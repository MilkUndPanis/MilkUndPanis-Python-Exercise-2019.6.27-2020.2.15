#info.py
class Info:
    def __init__(self):
        self.__name=''
        self.__addr=''
        self.__age=''
        self.__tel='12312345678'
    def set_name(self):
        n=input('Enter your name:')
        self.__name=n
    def set_addr(self):
        a=input('Enter your address:')
        self.__addr=a
    def set_age(self):
        y=input('Enter your age:')
        self.__age=y
    def set_tel(self):
        t=input("Enter your telephone number:")
        self.__tel=t
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_addr(self):
        return self.__addr
    def get_tel(self):
        return self.__tel
    def __str__(self):
        return 'Name:'+self.__name+'\nAddress:'+self.__addr+'\nAge:'+self.__age+'\nTel:'+self.__tel