import calc
from tkinter import *
from math import *
import tkinter.messagebox
def nconvertl(n):
    if n==10:
        return 'A'
    elif n==11:
        return 'B'
    elif n==12:
        return 'C'
    elif n==13:
        return 'D'
    elif n==14:
        return 'E'
    elif n==15:
        return 'F'
    else:return str(n)
def lconvertn(l):
    if l=='A':
        return 10
    elif l=='B':
        return 11
    elif l=='C':
        return 12
    elif l=='D':
        return 13
    elif l=='E':
        return 14
    elif l=='F':
        return 15
    else:return int(l)
class Base_Convert:
    def __init__(self):
        self.r=Toplevel()
        self.r.title('Base Convert')
        self.r.protocol('WM_DELETE_WINDOW', self.trytodestroy)
        #
        self.i=IntVar()
        self.i.set(1)
        self.up_mode_set_frame=Frame(self.r)
        self.bin_to_dec_mode = Radiobutton(self.up_mode_set_frame,text='Bin to Dec',variable=self.i,value=1,command=self.func1)
        self.dec_to_bin_mode=Radiobutton(self.up_mode_set_frame,text='Dec to Bin',variable=self.i,value=2,command=self.func2)
        self.dec_to_oct_mode = Radiobutton(self.up_mode_set_frame, text='Dec to Oct', variable=self.i, value=3,
                                           command=self.func3)
        self.bin_to_dec_mode.pack(side='left')
        self.dec_to_bin_mode.pack(side='left')
        self.dec_to_oct_mode.pack(side='left')
        self.up_mode_set_frame.pack(side='top')
        #
        self.down_mode_set_frame = Frame(self.r)
        self.oct_to_dec_mode = Radiobutton(self.down_mode_set_frame, text='Oct to Dec', variable=self.i, value=4,
                                           command=self.func4)
        self.dec_to_hex_mode = Radiobutton(self.down_mode_set_frame, text='Dec to Hex', variable=self.i, value=5,
                                           command=self.func5)
        self.hex_to_dec_mode = Radiobutton(self.down_mode_set_frame, text='Hex to Dec', variable=self.i, value=6,
                                           command=self.func6)
        self.oct_to_dec_mode.pack(side='left')
        self.dec_to_hex_mode.pack(side='left')
        self.hex_to_dec_mode.pack(side='left')
        self.down_mode_set_frame.pack(side='top')
        #
        self.up_frame=Frame(self.r)
        self.up_label=Label(self.up_frame,text='Binary Number:',font=('Ink Free',20))
        self.up_entry=Entry(self.up_frame,width=30)
        self.up_label.pack(side='left')
        self.up_entry.pack(side='left')
        self.up_frame.pack(side='top')
        #
        self.ans=StringVar()
        self.ans.set(0)
        self.down_frame = Frame(self.r)
        self.down_label=Label(self.down_frame,text='Decimal Number:',font=('Ink Free',20))
        self.ans_label = Label(self.down_frame, textvariable=self.ans, font=('Ink Free', 20))
        self.down_label.pack(side='left')
        self.ans_label.pack(side='left')
        self.down_frame.pack(side='top')
        #
        self.convert_frame=Frame(self.r)
        self.convert_button=Button(self.convert_frame,text='Convert',font=('Ink Free',25),command=self.b_t_d)
        self.back_button=Button(self.convert_frame,text='Back',font=('Ink Free',25),command=self.trytodestroy)
        self.convert_button.pack(side='left',fill='x')
        self.back_button.pack(side='left',fill='x')
        self.convert_frame.pack(side='bottom')
        #
        mainloop()
    def func1(self):
        self.up_label.config(text='Binary Number:')
        self.down_label.config(text='Decimal Number:')
        self.convert_button.config(command=self.b_t_d)
    def func2(self):
        self.up_label.config(text='Decimal Number:')
        self.down_label.config(text='Binary Number:')
        self.convert_button.config(command=self.d_t_b)
    def func3(self):
        self.up_label.config(text='Decimal Integer:')
        self.down_label.config(text='Octal Integer:')
        self.convert_button.config(command=self.d_t_o)
    def func4(self):
        self.up_label.config(text='Octal Number:')
        self.down_label.config(text='Decimal Number:')
        self.convert_button.config(command=self.o_t_d)
    def func5(self):
        self.up_label.config(text='Decimal Integer:')
        self.down_label.config(text='Hex Integer:')
        self.convert_button.config(command=self.d_t_h)
    def func6(self):
        self.up_label.config(text='Hex Integer:')
        self.down_label.config(text='Decimal Integer:')
        self.convert_button.config(command=self.h_t_d)
    def b_t_d(self):
        b=str(self.up_entry.get())
        d=0
        i=0
        i_d=b.split('.')
        l=len(i_d[0])-1
        for ch in i_d[0]:
            if int(ch)!=0 and int(ch)!=1:
                tkinter.messagebox.showerror('Error!','Invalid input.')
                self.up_entry.delete(0,END)
                return
            else:
                d+=pow(2,l-i)*int(ch)
                i+=1
        if len(i_d)==2:
            j=-1
            for ch in i_d[1]:
                if int(ch)!=0 and int(ch)!=1:
                    tkinter.messagebox.showerror('Error!','Invalid input.')
                    self.up_entry.delete(0,END)
                    return
                else:
                    d+=pow(2,j)*int(ch)
                    j-=1
        self.ans.set(format(float(d),'.3f'))
    def d_t_b(self):
        u=str(self.up_entry.get())
        l=u.split('.')
        n=int(l[0])
        if n<0:
            m = -n
        else:
            m = n
        d=''
        while m>0:
            d+=str(m%2)
            m=m//2
        e = ''
        for i in range(len(d) - 1, -1, -1):
            e += d[i]
        if n<0:
            p=len(e)
            q=e
            #反码，在前面补1直到八位（最高位），剩余部分，取反
            e='1'*(8-p)
            for ch in q:
                if ch=='1':
                    e+='0'
                else:e+='1'
        if len(l)==2:
            f=''
            o=float(float(self.up_entry.get())-int(l[0]))
            while o>0.0:
                if o*2>=1:
                    f+='1'
                    o=o*2-1
                else:
                    f+='0'
                    o*=2
            e=e+'.'+f
        self.ans.set(e)
    def d_t_o(self):
        m = int(self.up_entry.get())
        if m<0:
            m=-m
            e='-'
        else:
            e=''
        d = ''
        while m > 0:
            d += str(m % 8)
            m = m // 8
        for i in range(len(d) - 1, -1, -1):
            e += d[i]
        self.ans.set(e)
    def o_t_d(self):
        b=str(self.up_entry.get())
        d=0
        i=0
        i_d=b.split('.')
        l=len(i_d[0])-1
        for ch in i_d[0]:
            if int(ch)<0 or int(ch)>7:
                tkinter.messagebox.showerror('Error!','Invalid input.')
                self.up_entry.delete(0,END)
                return
            else:
                d+=pow(8,l-i)*int(ch)
                i+=1
        if len(i_d)==2:
            j=-1
            for ch in i_d[1]:
                if int(ch)<0 or int(ch)>7:
                    tkinter.messagebox.showerror('Error!','Invalid input.')
                    self.up_entry.delete(0,END)
                    return
                else:
                    d+=pow(8,j)*int(ch)
                    j-=1
        self.ans.set(format(float(d),'.3f'))
    def d_t_h(self):
        m = int(self.up_entry.get())
        if m<0:
            m=-m
            e='-'
        else:
            e=''
        d = ''
        while m > 0:
            d += nconvertl(m % 16)
            m = m // 16
        for i in range(len(d) - 1, -1, -1):
            e += d[i]
        self.ans.set(e)
    def h_t_d(self):
        b=str(self.up_entry.get())
        d=0
        i=0
        l=len(b)-1
        for ch in b:
            if lconvertn(ch)<0 or lconvertn(ch)>15:
                tkinter.messagebox.showerror('Error!','Invalid input.')
                self.up_entry.delete(0,END)
                return
            else:
                d+=pow(16,l-i)*lconvertn(ch)
                i+=1
        self.ans.set(format(float(d),'.3f'))
    def trytodestroy(self):
        if tkinter.messagebox.askyesno('Attention:','Do you want to quit?'):
            self.r.destroy()
class Calculator:
    def __init__(self):
        self.r=Tk(className='Calculator')
        self.r.protocol('WM_DELETE_WINDOW',self.trytodestroy)
        #
        self.Entry_Frame=Frame(self.r)
        self.Entry=Entry(self.Entry_Frame,font=('Ink Free',20))
        self.Entry.pack(side='top',fill='both')
        self.Entry_Frame.pack(side='top')
        #
        self.Outtry_Frame = Frame(self.r)
        self.Outtry = Entry(self.Outtry_Frame, font=('Ink Free', 20))
        self.Outtry.insert(END,'0')
        self.Outtry.pack(side='top', fill='both')
        self.Outtry_Frame.pack(side='top')
        #
        self.height=3
        self.width=6
        self.First_Input_Frame=Frame(self.r,height=self.height,width=12*self.width)
        self.one = Button(self.First_Input_Frame,text='1',height=self.height,width=self.width,command=self.get_one)
        self.two = Button(self.First_Input_Frame, text='2', height=self.height, width=self.width, command=self.get_two)
        self.three = Button(self.First_Input_Frame, text='3', height=self.height, width=self.width, command=self.get_three)
        self.plus= Button(self.First_Input_Frame, text='+', height=self.height, width=self.width, command=self.get_pl)
        self.subt = Button(self.First_Input_Frame, text='-', height=self.height, width=self.width, command=self.get_subt)
        self.mul = Button(self.First_Input_Frame, text='×', height=self.height, width=self.width, command=self.get_mul)
        self.div = Button(self.First_Input_Frame, text='÷', height=self.height, width=self.width, command=self.get_div)
        self.log = Button(self.First_Input_Frame, text='log', height=self.height, width=self.width, command=self.get_log)
        self.ln = Button(self.First_Input_Frame, text='ln', height=self.height, width=self.width, command=self.get_ln)
        self.lg = Button(self.First_Input_Frame, text='lg', height=self.height, width=self.width, command=self.get_lg)
        self.lbr = Button(self.First_Input_Frame, text='(', height=self.height, width=self.width, command=self.get_lbr)
        self.deci = Button(self.First_Input_Frame,text='.', height=self.height, width=self.width,command=self.get_deci)
        self.one.pack(side='left')
        self.two.pack(side='left')
        self.three.pack(side='left')
        self.plus.pack(side='left')
        self.subt.pack(side='left')
        self.mul.pack(side='left')
        self.div.pack(side='left')
        self.log.pack(side='left')
        self.ln.pack(side='left')
        self.lg.pack(side='left')
        self.lbr.pack(side='left')
        self.deci.pack(side='left')
        self.First_Input_Frame.pack()
        #
        self.Second_Input_Frame = Frame(self.r, height=self.height,width=12*self.width)
        self.four = Button(self.Second_Input_Frame, text='4', height=self.height,width=self.width, command=self.get_four)
        self.five = Button(self.Second_Input_Frame, text='5', height=self.height,width=self.width, command=self.get_five)
        self.six = Button(self.Second_Input_Frame, text='6', height=self.height,width=self.width, command=self.get_six)
        self.sin = Button(self.Second_Input_Frame, text='sin', height=self.height,width=self.width, command=self.get_sin)
        self.cos = Button(self.Second_Input_Frame, text='cos', height=self.height,width=self.width, command=self.get_cos)
        self.tan = Button(self.Second_Input_Frame, text='tan', height=self.height,width=self.width, command=self.get_tan)
        self.cot = Button(self.Second_Input_Frame, text='cot', height=self.height,width=self.width, command=self.get_cot)
        self.sec = Button(self.Second_Input_Frame, text='sec', height=self.height,width=self.width, command=self.get_sec)
        self.csc = Button(self.Second_Input_Frame, text='csc', height=self.height,width=self.width, command=self.get_csc)
        self.sinh = Button(self.Second_Input_Frame, text='sinh', height=self.height,width=self.width, command=self.get_sinh)
        self.rbr = Button(self.Second_Input_Frame, text=')', height=self.height,width=self.width, command=self.get_rbr)
        self.percent = Button(self.Second_Input_Frame, text='%', height=self.height, width=self.width,command=self.get_percent)
        self.four.pack(side='left')
        self.five.pack(side='left')
        self.six.pack(side='left')
        self.sin.pack(side='left')
        self.cos.pack(side='left')
        self.tan.pack(side='left')
        self.cot.pack(side='left')
        self.sec.pack(side='left')
        self.csc.pack(side='left')
        self.sinh.pack(side='left')
        self.rbr.pack(side='left')
        self.percent.pack(side='left')
        self.Second_Input_Frame.pack()
        #
        self.Third_Input_Frame = Frame(self.r, height=self.height, width=12 * self.width)
        self.seven = Button(self.Third_Input_Frame, text='7', height=self.height, width=self.width,
                           command=self.get_seven)
        self.eight = Button(self.Third_Input_Frame, text='8', height=self.height, width=self.width,
                           command=self.get_eight)
        self.nine = Button(self.Third_Input_Frame, text='9', height=self.height, width=self.width, command=self.get_nine)
        self.cosh = Button(self.Third_Input_Frame, text='cosh', height=self.height, width=self.width,
                          command=self.get_cosh)
        self.tanh = Button(self.Third_Input_Frame, text='tanh', height=self.height, width=self.width,
                          command=self.get_tanh)
        self.asin = Button(self.Third_Input_Frame, text='asin', height=self.height, width=self.width,
                          command=self.get_asin)
        self.acos = Button(self.Third_Input_Frame, text='acos', height=self.height, width=self.width,
                          command=self.get_acos)
        self.atan = Button(self.Third_Input_Frame, text='atan', height=self.height, width=self.width,
                          command=self.get_atan)
        self.acot = Button(self.Third_Input_Frame, text='acot', height=self.height, width=self.width,
                          command=self.get_acot)
        self.acsc = Button(self.Third_Input_Frame, text='acsc', height=self.height, width=self.width,
                           command=self.get_acsc)
        self.dot = Button(self.Third_Input_Frame, text=',', height=self.height, width=self.width, command=self.get_dot)
        self.backspace=Button(self.Third_Input_Frame,text='Back',height=self.height, width=self.width,command=self.get_back)
        self.seven.pack(side='left')
        self.eight.pack(side='left')
        self.nine.pack(side='left')
        self.cosh.pack(side='left')
        self.tanh.pack(side='left')
        self.asin.pack(side='left')
        self.acos.pack(side='left')
        self.atan.pack(side='left')
        self.acot.pack(side='left')
        self.acsc.pack(side='left')
        self.dot.pack(side='left')
        self.backspace.pack(side='left')
        self.Third_Input_Frame.pack()
        #
        self.Fourth_Input_Frame = Frame(self.r, height=self.height, width=12 * self.width)
        self.mod = Button(self.Fourth_Input_Frame, text='mod', height=self.height, width=self.width,
                            command=self.get_mod)
        self.zero = Button(self.Fourth_Input_Frame, text='0', height=self.height, width=self.width,
                            command=self.get_zero)
        self.clr = Button(self.Fourth_Input_Frame, text='CLR', height=self.height, width=self.width,
                           command=self.clear)
        self.asec = Button(self.Fourth_Input_Frame, text='asec', height=self.height, width=self.width,
                           command=self.get_asec)
        self.exp = Button(self.Fourth_Input_Frame, text='exp', height=self.height, width=self.width,
                           command=self.get_exp)
        self.power = Button(self.Fourth_Input_Frame, text='^', height=self.height, width=self.width,
                           command=self.get_power)
        self.asinh = Button(self.Fourth_Input_Frame, text='asinh', height=self.height, width=self.width,
                           command=self.get_asinh)
        self.acosh = Button(self.Fourth_Input_Frame, text='acosh', height=self.height, width=self.width,
                           command=self.get_acosh)
        self.atanh = Button(self.Fourth_Input_Frame, text='atanh', height=self.height, width=self.width,
                           command=self.get_atanh)
        self.e = Button(self.Fourth_Input_Frame, text='e', height=self.height, width=self.width,
                           command=self.get_e)
        self.hyp = Button(self.Fourth_Input_Frame, text='hyp', height=self.height, width=self.width, command=self.get_hyp)
        self.quit = Button(self.Fourth_Input_Frame, text='Quit', height=self.height, width=self.width,command=self.trytodestroy)
        self.mod.pack(side='left')
        self.zero.pack(side='left')
        self.clr.pack(side='left')
        self.asec.pack(side='left')
        self.exp.pack(side='left')
        self.power.pack(side='left')
        self.asinh.pack(side='left')
        self.acosh.pack(side='left')
        self.atanh.pack(side='left')
        self.e.pack(side='left')
        self.hyp.pack(side='left')
        #备用按键
        self.quit.pack(side='left')
        self.Fourth_Input_Frame.pack()
        #
        self.Fifth_Input_Frame = Frame(self.r, height=self.height, width=12 * self.width)
        self.abs = Button(self.Fifth_Input_Frame, text='ABS', height=self.height, width=self.width,
                          command=self.get_abs)
        self.gauss = Button(self.Fifth_Input_Frame, text='[]', height=self.height, width=self.width,
                           command=self.get_gauss)
        self.root = Button(self.Fifth_Input_Frame, text='√', height=self.height, width=self.width,
                          command=self.get_root)
        self.square = Button(self.Fifth_Input_Frame, text='x²', height=self.height, width=self.width,
                           command=self.get_square)
        self.tri = Button(self.Fifth_Input_Frame, text='x³', height=self.height, width=self.width,
                          command=self.get_tri)
        self.pi = Button(self.Fifth_Input_Frame, text='π', height=self.height, width=self.width,
                            command=self.get_pi)
        self.getans = Button(self.Fifth_Input_Frame, text='ANS', height=self.height, width=self.width,
                            command=self.get_ans)
        self.centry = Button(self.Fifth_Input_Frame, text='C', height=self.height, width=self.width,
                            command=self.get_centry)
        self.ran = Button(self.Fifth_Input_Frame, text='Ran', height=self.height, width=self.width,
                             command=self.get_ran)
        self.ans = Button(self.Fifth_Input_Frame, text='=', height=self.height, width=self.width,
                            command=self.Count)
        self.bc = Button(self.Fifth_Input_Frame, text='BC', height=self.height, width=self.width,
                        command=self.get_bc)
        self.clear_answer=Button(self.Fifth_Input_Frame,text='CLRANS',height=self.height,width=self.width,command=self.clrans)
        self.abs.pack(side='left')
        self.gauss.pack(side='left')
        self.root.pack(side='left')
        self.square.pack(side='left')
        self.tri.pack(side='left')
        self.pi.pack(side='left')
        self.getans.pack(side='left')
        self.centry.pack(side='left')
        self.ran.pack(side='left')
        self.ans.pack(side='left')
        self.bc.pack(side='left')
        #备用按键
        self.clear_answer.pack(side='left')
        self.Fifth_Input_Frame.pack()
        #
        self.Answer=StringVar()
        self.Answer.set(0.000)
        #
        mainloop()
    def Count(self):
        operating=self.Entry.get()
        op=''
        if calc.isoperator(operating[0]) or operating[0]=='^':
            #继续计算功能
            op+=(str(self.Answer.get())+operating)
        for i in range(len(operating)):
            #一对中空括号表示内部装着上一次运算的结果。
            if operating[i]=='(' and operating[i+1]==')':
                    op+=('('+str(self.Answer.get()))
            else:op+=operating[i]
        try:
            s=calc.calculate(op)
            if s==None:
                self.Answer.set('Error--Syntax Error.')
            else:
                self.Answer.set(s)
            self.Outtry.delete(0,END)
            self.Outtry.insert(END,self.Answer.get())
        except:
            self.Answer.set('Error--Syntax Error.')
            self.Outtry.delete(0, END)
            self.Outtry.insert(END, self.Answer.get())
    def get_one(self):
        self.Entry.insert(INSERT,'1')
    def get_two(self):
        self.Entry.insert(INSERT,'2')
    def get_three(self):
        self.Entry.insert(INSERT,'3')
    def get_pl(self):
        self.Entry.insert(INSERT,'+')
    def get_subt(self):
        self.Entry.insert(INSERT,'-')
    def get_mul(self):
        self.Entry.insert(INSERT,'*')
    def get_div(self):
        self.Entry.insert(INSERT,'/')
    def get_log(self):
        self.Entry.insert(INSERT,'log(')
    def get_ln(self):
        self.Entry.insert(INSERT,'ln(')
    def get_lg(self):
        self.Entry.insert(INSERT,'lg(')
    def get_lbr(self):
        self.Entry.insert(INSERT,'(')
    def get_four(self):
        self.Entry.insert(INSERT,'4')
    def get_five(self):
        self.Entry.insert(INSERT,'5')
    def get_six(self):
        self.Entry.insert(INSERT,'6')
    def get_sin(self):
        self.Entry.insert(INSERT,'sin(')
    def get_cos(self):
        self.Entry.insert(INSERT,'cos(')
    def get_tan(self):
        self.Entry.insert(INSERT,'tan(')
    def get_cot(self):
        self.Entry.insert(INSERT,'cot(')
    def get_sec(self):
        self.Entry.insert(INSERT,'sec(')
    def get_csc(self):
        self.Entry.insert(INSERT,'csc(')
    def get_sinh(self):
        self.Entry.insert(INSERT,'sinh(')
    def get_rbr(self):
        self.Entry.insert(INSERT,')')
    def get_seven(self):
        self.Entry.insert(INSERT,'7')
    def get_eight(self):
        self.Entry.insert(INSERT,'8')
    def get_nine(self):
        self.Entry.insert(INSERT,'9')
    def get_cosh(self):
        self.Entry.insert(INSERT,'cosh(')
    def get_tanh(self):
        self.Entry.insert(INSERT,'tanh(')
    def get_asin(self):
        self.Entry.insert(INSERT,'arcsin(')
    def get_acos(self):
        self.Entry.insert(INSERT,'arccos(')
    def get_atan(self):
        self.Entry.insert(INSERT,'arctan(')
    def get_acot(self):
        self.Entry.insert(INSERT,'arccot(')
    def get_acsc(self):
        self.Entry.insert(INSERT,'arccsc(')
    def get_dot(self):
        self.Entry.insert(INSERT,',')
    def get_mod(self):
        self.Entry.insert(INSERT,'mod')
    def get_zero(self):
        self.Entry.insert(INSERT,'0')
    def clear(self):
        self.Entry.delete(0,END)
        self.Answer.set(0)
        self.Outtry.delete(0, END)
        self.Outtry.insert(END, self.Answer.get())
    def get_asec(self):
        self.Entry.insert(INSERT,'arcsec(')
    def get_exp(self):
        self.Entry.insert(INSERT,'e^')
    def get_power(self):
        self.Entry.insert(INSERT,'^')
    def get_asinh(self):
        self.Entry.insert(INSERT,'arsinh(')
    def get_acosh(self):
        self.Entry.insert(INSERT,'arcosh(')
    def get_atanh(self):
        self.Entry.insert(INSERT,'artanh(')
    def get_e(self):
        self.Entry.insert(INSERT,'e')
    def get_hyp(self):
        self.Entry.insert(INSERT,'hyp(')
    def get_abs(self):
        self.Entry.insert(INSERT,'abs(')
    def get_gauss(self):
        self.Entry.insert(INSERT,'gauss(')
    def get_root(self):
        self.Entry.insert(INSERT, 'root(')
    def get_square(self):
        self.Entry.insert(INSERT, '^2')
    def get_tri(self):
        self.Entry.insert(INSERT, '^3')
    def get_pi(self):
        self.Entry.insert(INSERT,'pi')
    def get_ans(self):
        self.Entry.delete(0,END)
        self.Entry.insert(END,self.Answer.get())
    def get_centry(self):
        self.Entry.delete(0,END)
    def get_ran(self):
        self.Entry.insert(INSERT,'Ran(')
    def get_bc(self):
        B=Base_Convert()
    def get_deci(self):
        self.Entry.insert(INSERT,'.')
    def get_percent(self):
        self.Entry.insert(INSERT,'%')
    def get_back(self):
        self.Entry.delete(len(self.Entry.get())-1)
    def clrans(self):
        self.Answer.set(0)
    def trytodestroy(self):
        if tkinter.messagebox.askyesno('Attention:','Do you want to quit?'):
            self.r.destroy()
c=Calculator()