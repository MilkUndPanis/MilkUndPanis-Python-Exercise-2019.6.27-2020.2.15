#employee.py
class Employee:
    def __init__(self,n,id,cpy,vcn):
        self.__name=n
        self.__id=str(id)
        self.__company=cpy
        self.__vocation=vcn
    def set_name(self):
        n=input('Set the name:')
        self.__name=n
    def set_id(self):
        id=input('Set the id number:')
        self.__id=id
    def set_company(self):
        cpn=input('Set his\her company:')
        self.__company=cpn
    def set_vocation(self):
        vcn=input('Set his\her vocation:')
        self.__vocation=vcn
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_company(self):
        return self.__company
    def get_vocation(self):
        return self.__vocation
    def __str__(self):
        return 'Name:'+self.__name+'\tID number:'+str(self.__id)+'\tCompany:'+self.__company+'\tVocation:'+self.__vocation