#Question.py
class Question:
    def __init__(self,problem,an_1,an_2,an_3,an_4,cr_an):
        self.__prblm=problem
        self.__an_a=an_1
        self.__an_b=an_2
        self.__an_c=an_3
        self.__an_d=an_4
        self.__cr=cr_an
    def Set_Problem(self):
        self.__prblm=input('The Problem:')
    def Set_Answers(self):
        self.__an_a=input('Answer A:')
        self.__an_b=input('Answer B:')
        self.__an_c=input('Answer C:')
        self.__an_d=input('Answer D:')
    def Set_Correct(self):
        self.__cr=input('Correct Answer:')
    def Get_Correct(self):
        return self.__cr
    def __str__(self):
        return 'Question:'+self.__prblm+'\nA.'+self.__an_a+'\tB.'+self.__an_b+'\tC.'+self.__an_c+'\tD.'+self.__an_d