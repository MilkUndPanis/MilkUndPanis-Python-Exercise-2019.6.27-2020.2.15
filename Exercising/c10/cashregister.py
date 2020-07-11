#cashregister.py
from retailitem import *
class CashRegister:
    def __init__(self):
        self.__listof_ri=[]
    def purchase_item(self,ri):
        self.__listof_ri.append(ri)
    def get_total(self):
        total=0
        for ri in self.__listof_ri:
            total+=float(ri.GetPrice())*float(ri.GetUnit())
        return total
    def show_item(self):
        for ri in self.__listof_ri:
            print(ri)
    def clear(self):
        self.__listof_ri.clear()