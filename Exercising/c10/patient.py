#patient.py
class Patient:
    def __init__(self,name,addr,post,tel,emname,emtel):
        self.__fullname=name
        self.__fulladdr=addr
        self.__postal=str(post)
        self.__tel=str(tel)
        self.__emergencyname=emname
        self.__emergencytel=str(emtel)
    def Set_Name(self):
        gvname=input('Please enter the patient\'s given name:')
        mdname=input('Middle name:')
        fmlname=input('Family name:')
        flname=gvname+' '+mdname+' '+fmlname
        self.__fullname=flname
    def Set_Address(self):
        print('Enter the patient\'s address,including:')
        addr=input('Number of street:')
        city=input('City:')
        state=input('State:')
        full_addr=addr+','+city+','+state
        self.__fulladdr=full_addr
    def Set_Postal(self):
        self.__postal=input('Enter the patient\'s postal number:')
    def Set_Tel(self):
        self.__tel=input('Enter the patient\'s telephone number:')
    def Set_Emer_People(self):
        self.__emergencyname=input('Enter the name of emergency contact people:')
    def Set_Emer_Tel(self):
        self.__emergencytel= input('Enter the telephone of emergency contact people:')
    def Set_Emergency(self):
        print('Enter the information of emergency contact people:')
        self.Set_Emer_People()
        self.Set_Emer_Tel()
    def Get_Name(self):
        return self.__fullname
    def Get_Addr(self):
        return self.__fulladdr
    def Get_Postal(self):
        return self.__postal
    def Get_Tel(self):
        return self.__tel
    def Get_Emer_Name(self):
        return self.__emergencyname
    def Get_Emer_Tel(self):
        return self.__emergencytel
    def Get_Emergency(self):
        return self.__emergencyname,self.__emergencytel
    def __str__(self):
        return 'Patient\'s fullname:'+self.__fullname+\
               '\nPatient\'s full address:'+self.__fulladdr+\
               '\nPatient\'s postal number:'+self.__postal+\
               '\nPatient\'s telephone number:'+self.__tel+\
                '\nPatient\'s emergency contact people\'s name:'+self.__emergencyname+\
                '\nPatient\'s emergency contact people\'s telephone number:'+self.__emergencytel

