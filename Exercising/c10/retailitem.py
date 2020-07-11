#retailitem.py
class RetailItem:
    def __init__(self,describe,unit,price):
        self.__describe=describe
        self.__unit=str(unit)
        self.__price=str(price)
    def SetDescribe(self):
        dsc=input('Enter the item\'s description:')
        self.__describe=dsc
    def SetUnit(self):
        unt=input('Enter the unit of item storage:')
        self.__unit=unt
    def SetPrice(self):
        prc=input('Enter the price:')
        self.__price=prc
    def GetDescribe(self):
        return self.__describe
    def GetUnit(self):
        return self.__unit
    def GetPrice(self):
        return self.__price
    def __str__(self):
        return 'Description:'+self.__describe+'\tUnit:'+str(self.__unit)+'\tPrice:'+str(self.__price)