from math import *
from random import *
def is_tuple(str):
    for ch in str:
        if ch==',':
            return True
    return False
def is_sin(str):
    if str=='sin':
        return True
    else:return False
def is_cos(str):
    if str=='cos':
        return True
    else:return False
def is_tan(str):
    if str=='tan':
        return True
    else:return False
def is_cot(str):
    if str=='cot':
        return True
    else:return False
def is_sec(str):
    if str=='sec':
        return True
    else:return False
def is_csc(str):
    if str=='csc':
        return True
    else:return False
def is_power(ch):
    if ch=='^':
        return True
    else:return False
def is_root(str):
    if str=='√' or str=='root':
        return True
    else:return False
def is_fact(ch):
    if ch=='!':
        return True
def isoperator(ch):
    if ch=='*' or ch=='/' or ch=='+' or ch=='-':
        return True
    else:return False
def is_mul(ch):
    if ch=='*':
        return True
    else:return False
def is_div(ch):
    if ch=='/':
        return True
    else:return False
def is_add(ch):
    if ch=='+':
        return True
    else:return False
def is_subt(ch):
    if ch=='-':
        return True
    else:return False
def is_rem(str):
    if str=='mod':
        return True
    else:return False
#以a为底数b为真数的对数应该以log(a,b)的格式输入。
def is_log(str):
    if str=='log':
        return True
    else:return False
#经过spliting()函数处理后log(a,b)变为[‘log’,a,b].
def is_ln(str):
    if str=='ln':
        return True
    else: return False
def is_lg(str):
    if str=='lg':
        return True
    else:return False
def is_asin(str):
    if str=='arcsin':
        return True
    else:return False
def is_acos(str):
    if str=='arccos':
        return True
    else:return False
def is_atan(str):
    if str=='arctan':
        return True
    else:return False
def is_acot(str):
    if str=='arccot':
        return True
    else:return False
def is_asec(str):
    if str=='arcsec':
        return True
    else:return False
def is_acsc(str):
    if str=='arccsc':
        return True
    else:return False
def is_sinh(str):
    if str=='sinh':
        return True
    else:return False
def is_cosh(str):
    if str=='cosh':
        return True
    else:return False
def is_tanh(str):
    if str=='tanh':
        return True
    else:return False
def is_asinh(str):
    if str=='arsinh':
        return True
    else:return False
def is_acosh(str):
    if str=='arcosh':
        return True
    else:return False
def is_atanh(str):
    if str=='artanh':
        return True
    else:return False
def is_abs(str):
    if str=='abs':
        return True
    else:return False
def is_gauss(str):
    if str=='gauss':
        return True
    else:return False
def is_hyp(str):
    if str=='hyp':
        return True
    else:return False
def is_ran(str):
    if str=='Ran':
        return True
    else:return False
#hyp(a,b):欧氏距离函数，计算原点到(a,b)的距离。元组处理方法与二元对数函数相同
Warning_Cannot_Be_Divided_By_Zero='Error--Can\'t be divided by 0'
Warning_Cannot_Be_Modulo_Divided_By_Zero='Error--Can\'t be modulo divided by 0'
Reporting_Infinity_Answer='Inf.'
Warning_Domain_Error='Error--Domain Error.'
def proc_tuple(t_string):
    splited=str(t_string).split(',')
    return updating_plus_and_subt(str(splited[0]))[0]+'and'+updating_plus_and_subt(str(splited[-1]))[0]
    #and指明这个元组/and左侧与右侧的数据是二元对数函数的参数
    #先算出两个操作数的具体值
def find_bracket(string):
    Pairing=False
    dict={}
    c=1
    #假设最多嵌套4层括号.超过4层需要分开计算
    for i in range(1,5,1):
        dict[i]=[]
    for j in range(len(string)):
        if string[j]=='(' and Pairing==True:
            c+=1
            dict[c].append(j)
        elif string[j]==')' and Pairing==True:
            dict[c].append(j)
            Pairing=False
        elif string[j]=='(' and Pairing==False:
            dict[c].append(j)
            Pairing=True
        elif string[j]==')' and Pairing==False:
            c-=1
            dict[c].append(j)
    n_dict={}
    for c in dict:
        if dict[c]==[]:
            continue
        else:
            n_dict[c]=dict[c]
    #下面制作括号下标列表,list[m]表示第m+1重嵌套，list[m][n]表示第m+1重嵌套的第n+1对括号的位置，
    # list[m][n][0]与list[m][n][1]分别是这对括号在最初的字符串（运算式）的下标。
    list=[]
    for i in range(len(n_dict)):
        list.append([])
        for j in range(len(n_dict[i+1])//2):
            list[i].append([])
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j].append(n_dict[i+1][2*j])
            list[i][j].append(n_dict[i+1][2*j+1])
    return list
def conv_bracket(p_string):
    #处理括号
    string=''
    #如果不在第一个字符位置的左括号之前有数字或不在最后一个字符位置的右括号之后有数字，加上乘号
    for i in range(len(p_string)):
        if p_string[i]=='(' and i!=0 and str(p_string[i-1]).isdigit():
            string+='*('
        elif p_string[i]==')' and i!=len(p_string)-1 and str(p_string[i+1]).isdigit():
            string+=')*'
        else:
            string+=p_string[i]
    list=find_bracket(string)
    include_string = ''
    while True:
        if len(list)==0:
            return string
        else:
            i=len(list)-1
                #list[m]表示第m+1重嵌套，list[m][n]表示第m+1重嵌套的第n+1对括号的位置，
                # list[m][n][0]与list[m][n][1]分别是这对括号在最初的字符串（运算式）的下标。
            j=len(list[i])-1
            for k in range(list[i][j][0],list[i][j][1]):
                include_string+=string[k]
            if is_tuple(include_string):
                bracket = proc_tuple(include_string)
            else:
                bracket = (updating_plus_and_subt(include_string))[0]
            new_string=''
            for nd in range(list[i][j][0]):
                new_string+=string[nd]
            new_string+=bracket
            if list[i][j][1]!=len(string)-1:
                for i in range(list[i][j][1]+1,len(string)):
                    new_string+=string[i]
            string=new_string
            include_string=''
            list=find_bracket(string)
def spliting(string):
    #将算术式分割成运算符-函数-运算数的分割后列表
    EmptyStringList=[]
    EmptyString=''
    i=0
    #追踪ch的index
    for ch in string:
        if string[i:i+3]=='log' and str(string[i+3]).isdigit():
            #注意对数的真数和底数都是正数。
            if EmptyString != '':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('log')
            EmptyString = ''
        if string[i:i+3]=='hyp' and str(string[i+3]).isdigit():
            #注意对数的真数和底数都是正数。
            if EmptyString != '':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('hyp')
            EmptyString = ''
        if string[i:i+3]=='and' and str(string[i+3]).isdigit() and str(string[i-1]).isdigit():
            #检测and‘信号’.此时,底数（最初元组的第一个数）已经被加入EmptyString
            if EmptyString != '':
                EmptyStringList.append(EmptyString)
            EmptyString=''
            #and不会被加入,之后第二个操作数（真数）被加入EmptyString
        if string[i:i+2]=='pi':
            if  i!=len(string)-1 and str(string[i+1]).isdigit():
                EmptyStringList.append(str(pi))
                EmptyStringList.append('*')
                EmptyString=''
            elif i!=0 and str(string[i-1]).isdigit():
                EmptyStringList.append('*')
                EmptyStringList.append(str(pi))
                EmptyString = ''
            #圆周率作为一个运算数
            else:EmptyString+=str(pi)
        if string[i]=='e' and string[i-1:i+2]!='sec' and string[i-4:i+2]!='arcsec':#排除sec和arcsec
            if  i!=len(string)-1 and str(string[i+1]).isdigit():
                EmptyStringList.append(str(e))
                EmptyStringList.append('*')
                EmptyString=''
            elif i!=0 and str(string[i-1]).isdigit():
                EmptyStringList.append('*')
                EmptyStringList.append(str(e))
                EmptyString = ''
            #e=2.718281828......作为一个运算数
            else:EmptyString+=str(e)
        #如果开头就是减号，接下来是数字，则说明第一个运算数是负数
        if string[i]=='-' and i==0 and str(string[i+1]).isdigit():
            EmptyString+='-'
        # 如果开头就是加号，接下来是数字，则说明第一个运算数是正数,可以去掉这个加号
        if string[i] == '+' and i == 0 and str(string[i + 1]).isdigit():
            EmptyString+=''
        # 检测到以下三个字符是mod，作为求余字符保留。读到‘o’和‘d’时，EmptyString没有被追加。
        if string[i:i+3]=='mod' and str(string[i+3]).isdigit():
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('mod')
            EmptyString=''
        #ln/lg后面只能接正数.
        if string[i:i+2]=='lg' and str(string[i+2]).isdigit():
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('lg')
            EmptyString=''
        if string[i:i+2]=='ln' and str(string[i+2]).isdigit():
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('ln')
            EmptyString=''
        if string[i:i+3]=='sin' and (str(string[i+3]).isdigit()\
            or str(string[i+3])=='-') and string[i-1]!='c':#兼顾sin后面接负数的情况;排除arcsin()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('sin')
            EmptyString=''
        if string[i:i+3]=='cos' and (str(string[i+3]).isdigit()\
            or str(string[i+3])=='-') and string[i-1]!='c':#兼顾cos后面接负数的情况;排除arccos()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('cos')
            EmptyString=''
        if string[i:i+3]=='tan' and (str(string[i+3]).isdigit()\
            or str(string[i+3])=='-') and string[i-1]!='c':#兼顾tan后面接负数的情况;排除arctan()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('tan')
            EmptyString=''
        if string[i:i+3]=='cot' and (str(string[i+3]).isdigit()\
            or str(string[i+3])=='-') and string[i-1]!='c':#兼顾cot后面接负数的情况;排除arccot()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('cot')
            EmptyString=''
        if string[i:i+3]=='sec' and (str(string[i+3]).isdigit()\
            or str(string[i+3])=='-') and string[i-1]!='c':#兼顾sec后面接负数的情况;排除arcsec()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('sec')
            EmptyString=''
        if string[i:i+3]=='csc' and (str(string[i+3]).isdigit()\
            or str(string[i+3])=='-') and string[i-1]!='c':#兼顾csc后面接负数的情况;排除arccsc()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('csc')
            EmptyString=''
        if string[i:i+6]=='arcsin' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('arcsin')
            EmptyString=''
        if string[i:i+6]=='arccos' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('arccos')
            EmptyString=''
        if string[i:i+6]=='arctan' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('arctan')
            EmptyString=''
        if string[i:i+6]=='arccot' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('arccot')
            EmptyString=''
        if string[i:i+6]=='arcsec' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('arcsec')
            EmptyString=''
        if string[i:i+6]=='arccsc' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('arccsc')
            EmptyString=''
        if string[i:i+4]=='sinh' and (str(string[i+4]).isdigit()\
            or str(string[i+4])=='-') and string[i-1]!='r':#兼顾sin后面接负数的情况;排除arsinh()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('sinh')
            EmptyString=''
        if string[i:i+4]=='cosh' and (str(string[i+4]).isdigit()\
            or str(string[i+4])=='-') and string[i-1]!='r':#兼顾cos后面接负数的情况;排除arcosh()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('cosh')
            EmptyString=''
        if string[i:i+4]=='tanh' and (str(string[i+4]).isdigit()\
            or str(string[i+4])=='-') and string[i-1]!='r':#兼顾tan后面接负数的情况;排除artanh()
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('tanh')
            EmptyString=''
        if string[i:i+6]=='arsinh' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('arsinh')
            EmptyString=''
        if string[i:i+6]=='arcosh' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('arcosh')
            EmptyString=''
        if string[i:i+6]=='artanh' and (str(string[i+6]).isdigit() or str(string[i+6])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('artanh')
            EmptyString=''
        if (string[i]=='√' and str(string[i+1]).isdigit()) or (string[i:i+4]=='root' and str(string[i+4]).isdigit()):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('root')
            EmptyString=''
        if string[i:i+3]=='abs' and (str(string[i+3]).isdigit() or str(string[i+3])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('abs')
            EmptyString=''
        if string[i:i+5]=='gauss' and (str(string[i+5]).isdigit() or str(string[i+5])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('gauss')
            EmptyString=''
        if string[i:i+3]=='Ran' and (str(string[i+3]).isdigit() or str(string[i+3])=='-'):
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append('Ran')
            EmptyString=''
        if ((is_add(ch) or is_subt(ch)) and i!=0 and (str(string[i-1]).isdigit() or (string[i-2]=='p' and string[i-1]=='i') or string[i-1]=='e' or string[i-1]=='%')) or is_mul(ch) or is_div(ch) or is_power(ch):
            #当四大运算符位于开头时有特殊含义
            #处理百分号可能留下空格，而空格是必须禁止的
            #当非开头的加减运算符两侧都是数据或有左侧有数据（包括pi/e)或百分号时，或对于任意乘除号,运算符表明普通的四则运算
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append(ch)
            EmptyString=''
        # 当加减号只有右侧有数字(包括pi和e)时，表明数字的正负性质
        #左侧是百分号除外
        if is_subt(ch) and i!=0 and not(str(string[i-1]).isdigit()) and string[i-1]!='%' and (str(string[i+1]).isdigit() or (string[i+1]=='p' and string[i+2]=='i') or string[i+1]=='e'):
            EmptyString+=ch
        if is_add(ch) and i!=0 and not(str(string[i-1]).isdigit()) and string[i-1]!='%' and (str(string[i+1]).isdigit() or (string[i+1]=='p' and string[i+2]=='i') or string[i+1]=='e'):
            EmptyString+=''
        if is_fact(ch) and i!=0 and str(string[i-1]).isdigit():
            #阶乘负号，前一个必须是运算数
            if EmptyString!='':
                EmptyStringList.append(EmptyString)
            EmptyStringList.append(ch)
            EmptyString=''
        if str(ch).isdigit() or ch=='.':#处理小数点
            EmptyString+=ch
        if ch=='%':#处理百分号
            EmptyStringList.append(str(float(EmptyString)/100))
            EmptyString=''
        i+=1
    #Appending the final operated number
    if EmptyString!='':
        EmptyStringList.append(EmptyString)
    return EmptyStringList
def updating_power(string):
    #幂运算具有括号以下的最高优先级。
    UpdatedList=spliting(string)
    NewList=[]
    isFirst=False
    while True:
        for i in range(len(UpdatedList)):
            if is_power(UpdatedList[i]) and isFirst==False:
                NewItem=pow(float(UpdatedList[i-1]),float(UpdatedList[i+1]))
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            else:
                NewList.append(UpdatedList[i])
        if isFirst == False:
            return NewList
        else:
            del NewList[index - 1]
            del NewList[index]
            UpdatedList = NewList
            NewList = []
            isFirst = False
def updating_factorial(string):
    #假设阶乘具有括号以下的次优先级
    UpdatedList = updating_power(string)
    NewList = []
    isFirst = False
    while True:
        for i in range(len(UpdatedList)):
            if is_fact(UpdatedList[i]) and isFirst == False:
                NewItem = factorial(float(UpdatedList[i - 1]))
                index = i
                NewList.append(str(NewItem))
                isFirst = True
            else:
                NewList.append(UpdatedList[i])
        if isFirst == False:
            return NewList
        else:
            del NewList[index - 1]
            UpdatedList = NewList
            NewList = []
            isFirst = False
def updating_binary_log_hyp(string):
    #假设log具有括号以下的次优先级
    UpdatedList = updating_factorial(string)
    NewList = []
    isFirst = False
    while True:
        for i in range(len(UpdatedList)):
            if is_log(UpdatedList[i]) and isFirst == False:
                NewItem = log(float(UpdatedList[i+2]),float(UpdatedList[i+1]))
                #Python log 函数：log(x,b)=log(b)(x).
                index = i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_hyp(UpdatedList[i]) and isFirst == False:
                NewItem = hypot(float(UpdatedList[i+2]),float(UpdatedList[i+1]))
                #Python hypot 函数
                index = i
                NewList.append(str(NewItem))
                isFirst = True
            else:
                NewList.append(UpdatedList[i])
        if isFirst == False:
            return NewList
        else:
            del NewList[index + 1]
            del NewList[index + 1]
            UpdatedList = NewList
            NewList = []
            isFirst = False
def updating_sin_cos_tan_etc(string):
    UpdatedList = updating_binary_log_hyp(string)
    NewList=[]
    isFirst=False
    while True:
        for i in range(len(UpdatedList)):
            #默认情况下，Python的三角函数是弧度制。假设输入角度
            if is_sin(UpdatedList[i]) and isFirst==False:
                NewItem=sin(radians(float(UpdatedList[i+1])))
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_cos(UpdatedList[i]) and isFirst==False:
                NewItem=cos(radians(float(UpdatedList[i+1])))
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_tan(UpdatedList[i]) and isFirst==False:
                if abs(float(UpdatedList[i+1]))%180.0==90.0:
                    return Reporting_Infinity_Answer
                else:
                    NewItem=tan(radians(float(UpdatedList[i+1])))
                    index=i
                    NewList.append(str(NewItem))
                    isFirst = True
            elif is_cot(UpdatedList[i]) and isFirst==False:
                if abs(float(UpdatedList[i+1]))%180.0==0.0:
                    return Reporting_Infinity_Answer
                else:
                    if abs(float(UpdatedList[i+1]))%180.0==90.0:
                        NewItem=0
                    else:
                        NewItem=1/tan(radians(float(UpdatedList[i+1])))
                    index=i
                    NewList.append(str(NewItem))
                    isFirst = True
            elif is_sec(UpdatedList[i]) and isFirst==False:
                if abs(float(UpdatedList[i+1]))%180.0==90.0:
                    return Reporting_Infinity_Answer
                else:
                    NewItem=1/cos(radians(float(UpdatedList[i+1])))
                    index=i
                    NewList.append(str(NewItem))
                    isFirst = True
            elif is_csc(UpdatedList[i]) and isFirst==False:
                if abs(float(UpdatedList[i+1]))%180.0==0.0:
                    return Reporting_Infinity_Answer
                else:
                    NewItem=1/sin(radians(float(UpdatedList[i+1])))
                    index=i
                    NewList.append(str(NewItem))
                    isFirst = True
            elif is_lg(UpdatedList[i]) and isFirst==False:
                NewItem=log10(float(UpdatedList[i+1]))
                index=i
                NewList.append(str(NewItem))
                isFirst=True
            elif is_ln(UpdatedList[i]) and isFirst==False:
                NewItem=log(float(UpdatedList[i+1]))
                index=i
                NewList.append(str(NewItem))
                isFirst=True
            elif is_asin(UpdatedList[i]) and isFirst==False:
                s=float(UpdatedList[i+1])
                if s>1.00 or s<-1.00:
                    return Warning_Domain_Error
                else:
                    NewItem=degrees(asin(s))
                    index=i
                    NewList.append(str(NewItem))
                    isFirst=True
            elif is_acos(UpdatedList[i]) and isFirst==False:
                s=float(UpdatedList[i+1])
                if s>1.00 or s<-1.00:
                    return Warning_Domain_Error
                else:
                    NewItem=degrees(acos(s))
                    index=i
                    NewList.append(str(NewItem))
                    isFirst=True
            elif is_atan(UpdatedList[i]) and isFirst==False:
                NewItem=degrees(atan(float(UpdatedList[i+1])))
                index=i
                NewList.append(str(NewItem))
                isFirst=True
            elif is_acot(UpdatedList[i]) and isFirst==False:
                s=float(UpdatedList[i+1])
                if s==0.0:
                    NewItem=90.0
                elif s>0.0:
                    NewItem=degrees(atan(1/s))
                else:NewItem=180+degrees(atan(1/s))
                index=i
                NewList.append(str(NewItem))
                isFirst=True
            elif is_acsc(UpdatedList[i]) and isFirst==False:
                s=float(UpdatedList[i+1])
                if s>-1 and s<1:
                    return Warning_Domain_Error
                else:
                    NewItem=degrees(asin(1/s))
                index=i
                NewList.append(str(NewItem))
                isFirst=True
            elif is_asec(UpdatedList[i]) and isFirst==False:
                s=float(UpdatedList[i+1])
                if s>-1 and s<1:
                    return Warning_Domain_Error
                else:
                    NewItem=degrees(acos(1/s))
                index=i
                NewList.append(str(NewItem))
                isFirst=True
            elif is_sinh(UpdatedList[i]) and isFirst==False:
                NewItem=sinh(float(UpdatedList[i+1]))
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_cosh(UpdatedList[i]) and isFirst==False:
                NewItem=cosh(float(UpdatedList[i+1]))
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_tanh(UpdatedList[i]) and isFirst==False:
                NewItem=tanh(float(UpdatedList[i+1]))
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_asinh(UpdatedList[i]) and isFirst==False:
                NewItem=asinh(float(UpdatedList[i+1]))
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_acosh(UpdatedList[i]) and isFirst==False:
                s=float(UpdatedList[i+1])
                if s>=1:
                    NewItem=acosh(s)
                else:return Warning_Domain_Error
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_atanh(UpdatedList[i]) and isFirst==False:
                s=float(UpdatedList[i+1])
                if s>-1 and s<1:
                    NewItem=atanh(s)
                else:return Warning_Domain_Error
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_root(UpdatedList[i]) and isFirst==False:
                s=float(UpdatedList[i+1])
                if s>=0:
                    NewItem=sqrt(s)
                else:return Warning_Domain_Error
                index=i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_abs(UpdatedList[i]) and isFirst==False:
                NewItem = fabs(float(UpdatedList[i + 1]))
                index = i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_gauss(UpdatedList[i]) and isFirst==False:
                NewItem = floor(float(UpdatedList[i + 1]))
                index = i
                NewList.append(str(NewItem))
                isFirst = True
            elif is_ran(UpdatedList[i]) and isFirst==False:
                NewItem = float(UpdatedList[i + 1])*random()
                index = i
                NewList.append(str(NewItem))
                isFirst = True
            else:
                NewList.append(UpdatedList[i])
        if isFirst == False:
            return NewList
        else:
            del NewList[index + 1]
            UpdatedList = NewList
            NewList = []
            isFirst = False
def updating_mul_and_div_rem(string):
    if updating_sin_cos_tan_etc(string)==Reporting_Infinity_Answer:
        return Reporting_Infinity_Answer
    if updating_sin_cos_tan_etc(string)==Warning_Domain_Error:
        return Warning_Domain_Error
    UpdatedList = updating_sin_cos_tan_etc(string)
    NewList = []
    isFirst = False
    #每次处理列表里的第一个乘号/除号/求余符号，且只处理一个符号
    #为此,统一首次布尔指示变量
    while True:
        for i in range(len(UpdatedList)):
            if is_mul(UpdatedList[i]) and isFirst==False :
                NewItem=float(UpdatedList[i-1])*float(UpdatedList[i+1])
                index=i
                #Noting the first index '*' appeared
                NewList.append(str(NewItem))
                isFirst=True
            elif is_div(UpdatedList[i]) and isFirst==False:
                if float(UpdatedList[i + 1]) == 0:
                    return Warning_Cannot_Be_Divided_By_Zero
                else:
                    NewItem = float(UpdatedList[i - 1]) / float(UpdatedList[i + 1])
                    index = i
                    # Noting the first index '/' appeared
                    NewList.append(str(NewItem))
                    isFirst = True
            elif is_rem(UpdatedList[i]) and isFirst==False:
                if float(UpdatedList[i + 1]) == 0:
                    return Warning_Cannot_Be_Modulo_Divided_By_Zero
                else:
                    NewItem = float(UpdatedList[i - 1]) % float(UpdatedList[i + 1])
                    index = i
                    # Noting the first index 'mod' appeared
                    NewList.append(str(NewItem))
                    isFirst = True
            else:
                NewList.append(UpdatedList[i])
        # 列表里已经没有乘除号了
        if isFirst==False:
            return NewList
        else:
            #删除旧表内首次出现的乘除号两侧的操作数
            del NewList[index-1]
            del NewList[index]
            UpdatedList=NewList
            NewList=[]
            isFirst=False
def updating_plus_and_subt(string):
    if updating_mul_and_div_rem(string)==Warning_Cannot_Be_Modulo_Divided_By_Zero:
        return Warning_Cannot_Be_Modulo_Divided_By_Zero
    if updating_mul_and_div_rem(string)==Warning_Cannot_Be_Divided_By_Zero:
        return Warning_Cannot_Be_Divided_By_Zero
    if updating_mul_and_div_rem(string)==Reporting_Infinity_Answer:
        return Reporting_Infinity_Answer
    if updating_mul_and_div_rem(string)==Warning_Domain_Error:
        return Warning_Domain_Error
    UpdatedList = updating_mul_and_div_rem(string)
    NewList = []
    isFirst = False
    # 每次处理列表里的第一个加号或减号，且只处理一个符号
    # 为此,统一首次布尔指示变量
    while True:
        for i in range(len(UpdatedList)):
            if is_add(UpdatedList[i]) and isFirst == False and i!=0:
                NewItem = float(UpdatedList[i - 1]) + float(UpdatedList[i + 1])
                index = i
                # Noting the first index '+' appeared
                NewList.append(str(NewItem))
                isFirst = True
            elif is_subt(UpdatedList[i]) and isFirst==False and i!=0:
                NewItem = float(UpdatedList[i - 1]) - float(UpdatedList[i + 1])
                index = i
                # Noting the first index '-' appeared
                NewList.append(str(NewItem))
                isFirst = True
            else:
                NewList.append(UpdatedList[i])
        # 列表里已经没有加减号了
        if isFirst == False:
            return NewList
        else:
            # 删除旧表内首次出现的加减号两侧的操作数
            del NewList[index - 1]
            del NewList[index]
            UpdatedList = NewList
            NewList = []
            isFirst = False
def convert_to_ans(string):
    UpdatedList=updating_plus_and_subt(string)
    if UpdatedList==Warning_Cannot_Be_Modulo_Divided_By_Zero:
        return Warning_Cannot_Be_Modulo_Divided_By_Zero
    if UpdatedList==Warning_Cannot_Be_Divided_By_Zero:
        return Warning_Cannot_Be_Divided_By_Zero
    if UpdatedList==Reporting_Infinity_Answer:
        return Reporting_Infinity_Answer
    if UpdatedList==Warning_Domain_Error:
        return Warning_Domain_Error
    if len(UpdatedList)==1:
        #规定：当最后一个字符是百分号时，显示为百分模式。
        if string[-1]=='%':
            return format(float(UpdatedList[0]),'%')
        else:
            return format(float(UpdatedList[0]),'.7f')
def calculate(string):
    n_s=conv_bracket(string)
    a=convert_to_ans(n_s)
    return a

