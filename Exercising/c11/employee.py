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
class ProductionWorker(Employee):
    def __init__(self,n,id,cpy,vcn,sft,hrwg):
        Employee.__init__(self,n,id,cpy,vcn)
        self.__shift=str(sft)
        #self.__shift==1:daytime shift
        #self.__shift==2:night shift
        self.__hourwage=str(hrwg)
    def set_shift(self):
        sft=input('Enter his\her shift(1:daytime;2:night):')
        while sft!='1' and sft!='2':
            sft=input('It is invalid,try again:')
        self.__shift=sft
    def set_wage_per_hour(self):
        self.__hourwage=input('Enter his\her wage per hour:')
    def get_shift(self):
        return self.__shift
    def get_wage_per_hour(self):
        return self.__hourwage
    def convert(self):
        if self.__shift=='1':
            return 'Daytime'
        elif self.__shift=='2':
            return 'Nighttime'
        else:return 'UNKNOWN'
    def __str__(self):
        return Employee.__str__(self)+'\tShift:'+self.convert()+'\tWage per hour:'+str(self.__hourwage)
class ShiftSupervisor(Employee):
    def __init__(self,n,id,cpy,vcn,wgyr,bns):
        Employee.__init__(self,n,id,cpy,vcn)
        self.__wage_per_year=wgyr
        self.__bonus=bns
    def set_wage_per_year(self):
        self.__wage_per_year=input('Enter the supervisor\'s wage per year:')
    def set_bonus(self):
        self.__bonus=input('Enter the supervisor\'s producing bonus:')
    def get_wage_per_year(self):
        return self.__wage_per_year
    def get_bonus(self):
        return self.__bonus
    def __str__(self):
        return Employee.__str__(self)+'\tWage per year:'+str(self.__wage_per_year)+'\tBonus:'+str(self.__bonus)