#procedure.py
class Procedure:
    def __init__(self,prcd,prdt,dtnm,fee):
        self.__proceed=prcd
        self.__date=str(prdt)
        self.__doctor=dtnm
        self.__fee=str(fee)
    def Set_Proceed(self):
        self.__proceed=input('Please enter the name of procedure:')
    def Set_Date(self):
        self.__date=input('Please enter the date of proceeding:')
    def Set_Doctor(self):
        self.__doctor=input('Please enter the name of executing doctor:')
    def Set_Fee(self):
        self.__fee=input('Please enter the cost of procedure:')
    def Get_Proceed(self):
        return self.__proceed
    def Get_Date(self):
        return self.__date
    def Get_Doctor(self):
        return self.__doctor
    def Get_Fee(self):
        return self.__fee
    def __str__(self):
        return 'Procedure:'+self.__proceed+\
                '\nDate:'+str(self.__date)+\
                '\nDoctor:'+self.__doctor+\
                '\nFee:'+str(self.__fee)
