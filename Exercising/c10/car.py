#car.py
class Car:
    def __init__(self):
        ym=input('Enter the car\'s year and model:')
        self.__year_model=ym
        producer=input('Enter the car\'s maker:')
        self.__make=producer
        self.__speed=0
    def accelerate(self):
        self.__speed+=5
    def brake(self):
        self.__speed-=5
    def get_speed(self):
        return self.__speed
    def __str__(self):
        return 'Car\'s year and model:'+self.__year_model+'\nMaker:'+self.__make+'\nSpeed:'+str(self.__speed)