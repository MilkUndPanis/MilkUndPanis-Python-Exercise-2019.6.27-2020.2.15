#example.py
class PhoneCall:
    def __init__(self,phone):
        self.__phone=str(phone)
    def Set_Phone(self):
        self.__phone=input('Please enter your phone number:')
    def Get_Phone(self):
        return self.__phone
    def __str__(self):
        return 'Phone number:'+self.__phone
class PhoneBook(PhoneCall):
    def __init__(self,phone,name,addr):
        PhoneCall.__init__(self,phone)
        self.__name=name
        self.__addr=addr
    def Get_Name(self):
        return self.__name
    def Get_Addr(self):
        return self.__addr
    def Set_Name(self):
        self.__name=input('Your name:')
    def Set_Addr(self):
        self.__addr=input('Your address:')
    def __str__(self):
        return PhoneCall.__str__(self)+'\tName:'+self.__name+'\tAddress:'+self.__addr