#pet.py
class Pet:
    def __init__(self):
        self.__name=''
        self.__type=''
        self.__age=0
    def set_name(self):
        n=input('Enter animal\'s name:')
        self.__name=n
    def set_animal_type(self):
        t=input('Enter animal type:')
        self.__type=t
    def set_age(self):
        a=input('Enter animal\' age:')
        self.__age=a
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__type
    def get_age(self):
        return self.__age
    def __str__(self):
        return 'Animal name:'+self.__name+'\nAnimal Type:'+self.__type+'\nAge:'+self.__age