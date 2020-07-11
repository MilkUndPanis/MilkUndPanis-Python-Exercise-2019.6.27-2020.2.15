#Calculate.py
from tkinter import *
import tkinter.messagebox
from math import *
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
        self.convert_button.pack(fill='x')
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
class Calculate:
    def __init__(self):
        self.r=Tk()
        #
        self.binary=Frame(self.r)
        self.a_label=Label(self.binary,text='First Calculated Number:')
        self.a_entry=Entry(self.binary,width=10)
        self.a_label.pack(side='left')
        self.a_entry.pack(side='left')
        self.b_label = Label(self.binary, text='Second Calculated Number:')
        self.b_entry = Entry(self.binary, width=10)
        self.b_label.pack(side='left')
        self.b_entry.pack(side='left')
        self.binary.pack(side='top')
        #
        self.unary_and_continue=Frame(self.r)
        self.u_label = Label(self.unary_and_continue, text='Unary Calculated Number:')
        self.u_entry = Entry(self.unary_and_continue, width=10)
        self.u_label.pack(side='left')
        self.u_entry.pack(side='left')
        self.c_label = Label(self.unary_and_continue, text='Continue Calculated Number:')
        self.c_entry = Entry(self.unary_and_continue, width=10)
        self.c_label.pack(side='left')
        self.c_entry.pack(side='left')
        self.unary_and_continue.pack(side='top')
        #
        self.mode=IntVar()
        self.mode.set(1)
        self.r_f=Frame(self.r)
        self.b_button = Radiobutton(self.r_f, text='Binary Computation', variable=self.mode, value=1)
        self.b_button.pack(side='left')
        self.u_button = Radiobutton(self.r_f, text='Unary Computation', variable=self.mode, value=2)
        self.u_button.pack(side='left')
        self.c_button = Radiobutton(self.r_f, text='Continue Computation', variable=self.mode, value=3)
        self.c_button.pack(side='left')
        self.r_f.pack()
        #
        self.notice_frame=Frame(self.r)
        self.notice=Label(self.r,text='Notice:In the Continue Computation Mode,\n'+
                                      'The continued calculated number is the second calculated number.\n'+
                                      'The first calculated number is the previous answer.')
        self.notice.pack(side='top')
        self.notice_frame.pack(side='top')
        #
        self.button_frame = Frame(self.r)
        self.button_frame.pack(side='top')
        self.unary_frame = Frame(self.r)
        self.unary_frame.pack(side='top')
        #
        self.a_button=Button(self.button_frame,text='+',command=self.add)
        self.s_button=Button(self.button_frame,text='-',command=self.sub)
        self.m_button = Button(self.button_frame, text='x', command=self.mul)
        self.d_button=Button(self.button_frame,text='÷',command=self.div)
        self.r_button=Button(self.button_frame,text='%',command=self.rem)
        self.p_button = Button(self.button_frame, text='power', command=self.pow)
        self.at_button = Button(self.button_frame, text='arctan', command=self.atan_d)
        self.log_button=Button(self.button_frame,text='log(first)(second)',command=self.log)
        self.a_button.pack(side='left')
        self.s_button.pack(side='left')
        self.m_button.pack(side='left')
        self.d_button.pack(side='left')
        self.r_button.pack(side='left')
        self.p_button.pack(side='left')
        self.at_button.pack(side='left')
        self.log_button.pack(side='left')
        #
        self.sin_b=Button(self.unary_frame,text='sin',command=self.sin)
        self.cos_b = Button(self.unary_frame, text='cos', command=self.cos)
        self.tan_b=Button(self.unary_frame,text='tan',command=self.tan)
        self.asin_b=Button(self.unary_frame,text='arcsin',command=self.asin)
        self.acos_b = Button(self.unary_frame, text='arccos', command=self.acos)
        self.atan_b = Button(self.unary_frame, text='arctan', command=self.atan)
        self.exp_b = Button(self.unary_frame, text='exp', command=self.exp)
        self.root_b=Button(self.unary_frame,text='√',command=self.root)
        self.ln_b=Button(self.unary_frame,text='ln',command=self.ln)
        self.lg_b=Button(self.unary_frame,text='lg',command=self.lg)
        self.lg2_b=Button(self.unary_frame,text='log2',command=self.log_2)
        self.u_button.pack(side='left')
        self.sin_b.pack(side='left')
        self.cos_b.pack(side='left')
        self.tan_b.pack(side='left')
        self.exp_b.pack(side='left')
        self.asin_b.pack(side='left')
        self.acos_b.pack(side='left')
        self.atan_b.pack(side='left')
        self.root_b.pack(side='left')
        self.ln_b.pack(side='left')
        self.lg_b.pack(side='left')
        self.lg2_b.pack(side='left')
        #
        self.answer=StringVar()
        self.answer.set(0)
        self.answer_frame=Frame(self.r)
        self.tip=Label(self.answer_frame,text='Answer:')
        self.answer_label=Label(self.answer_frame,textvariable=self.answer)
        self.tip.pack(side='left')
        self.answer_label.pack(side='left')
        self.answer_frame.pack()
        #
        self.clear_frame = Frame(self.r)
        self.clr_button = Button(self.r, text='Clear', command=self.clear)
        self.clr_button.pack(fill='x')
        self.clear_frame.pack()
        #
        self.dec_to_bin_frame=Frame(self.r)
        self.dec_to_bin=Button(self.r,text='Base Conversion',font=('Ink Free',25),command=self.base)
        self.dec_to_bin.pack(fill='x')
        self.dec_to_bin_frame.pack()
        #
        self.quit_frame=Frame(self.r)
        self.quit_button=Button(self.r,text='Quit',command=self.r.destroy)
        self.quit_button.pack(fill='x')
        self.quit_frame.pack()
        #
        mainloop()
    def get(self):
        if self.mode.get()==1:
            return float(self.a_entry.get()),float(self.b_entry.get())
        if self.mode.get()==3:
            return float(self.answer.get()),float(self.c_entry.get())
    def add(self):
        try:
            self.a, self.b = self.get()
            self.answer.set(self.a + self.b)
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'This is a binary computation.')
    def sub(self):
        try:
            self.a,self.b=self.get()
            self.answer.set(self.a-self.b)
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'This is a binary computation.')
    def mul(self):
        try:
            self.a,self.b=self.get()
            self.answer.set(self.a*self.b)
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'This is a binary computation.')
    def div(self):
        try:
            self.a, self.b = self.get()
            if self.b==0:
                tkinter.messagebox.showerror('Error!', 'Cannot be divided by 0.')
                self.a_entry.delete(0,END)
                self.b_entry.delete(0, END)
            else:
                self.answer.set(self.a / self.b)
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'This is a binary computation.')
    def rem(self):
        try:
            self.a, self.b = self.get()
            if self.b == 0:
                tkinter.messagebox.showerror('Error!', 'Cannot be divided by 0.')
                self.a_entry.delete(0, END)
                self.b_entry.delete(0, END)
            else:
                self.answer.set(self.a / self.b)
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'This is a binary computation.')
    def pow(self):
        try:
            self.a, self.b = self.get()
            self.answer.set(pow(self.a , self.b))
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'This is a binary computation.')
    def atan_d(self):
        try:
            self.a, self.b = self.get()
            if self.b==0:
                tkinter.messagebox.showerror('Error!', 'Cannot be divided by 0.')
                self.a_entry.delete(0,END)
                self.b_entry.delete(0, END)
            else:
                self.answer.set(format(atan2(self.a, self.b)*180/pi,'.3f'))
        except(ValueError):
            tkinter.messagebox.showerror('Error!','This is a binary computation.')
    def log(self):
        try:
            self.a, self.b = self.get()
            if self.a<=0 or self.b<=0:
                tkinter.messagebox.showerror('Error!', 'Base and natural number must be above 0.')
                self.a_entry.delete(0, END)
                self.b_entry.delete(0, END)
            else:
                self.answer.set(log(self.b , self.a))
                #log(n,base)=log(b)(N)
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'This is a binary computation.')
    #
    def sin(self):
        try:
            if self.mode.get()==2:
                self.c=float(self.u_entry.get())*pi/180
            if self.mode.get()==3:
                self.c=float(self.answer.get())*pi/180
            self.answer.set(format(sin(self.c),'.3f'))
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
    def cos(self):
        try:
            if self.mode.get() == 2:
                self.c = float(self.u_entry.get()) * pi / 180
            if self.mode.get() == 3:
                self.c = float(self.answer.get()) * pi / 180
            self.answer.set(format(cos(self.c),'.3f'))
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
    def tan(self):
        try:
            if self.mode.get() == 2:
                self.c = float(self.u_entry.get()) * pi / 180
            if self.mode.get() == 3:
                self.c = float(self.answer.get()) * pi / 180
            self.answer.set(format(tan(self.c),'.3f'))
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
    def exp(self):
        try:
            if self.mode.get() == 2:
                self.c = float(self.u_entry.get())
            if self.mode.get() == 3:
                self.c = float(self.answer.get())
            self.answer.set(format(exp(self.c), '.3f'))
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
    def asin(self):
        if self.mode.get()==1:
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
            self.a_entry.delete(0, END)
            self.b_entry.delete(0, END)
        else:
            try:
                if self.mode.get() == 2:
                    self.c = float(self.u_entry.get())
                if self.mode.get() == 3:
                    self.c = float(self.answer.get())
                self.answer.set(format(asin(self.c), '.3f'))
            except(ValueError):
                if self.c > 1.0 or self.c < -1.0:
                    tkinter.messagebox.showerror('Error!', 'Math domain error.')
                    self.u_entry.delete(0, END)
                else:
                    tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
                    self.a_entry.delete(0, END)
                    self.b_entry.delete(0, END)
    def acos(self):
        if self.mode.get()==1:
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
            self.a_entry.delete(0, END)
            self.b_entry.delete(0, END)
        else:
            try:
                if self.mode.get() == 2:
                    self.c = float(self.u_entry.get())
                if self.mode.get() == 3:
                    self.c = float(self.answer.get())
                self.answer.set(format(acos(self.c), '.3f'))
            except(ValueError):
                if self.c > 1.0 or self.c < -1.0:
                    tkinter.messagebox.showerror('Error!', 'Math domain error.')
                    self.u_entry.delete(0, END)
                else:
                    tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
                    self.a_entry.delete(0, END)
                    self.b_entry.delete(0, END)
    def atan(self):
        try:
            if self.mode.get() == 2:
                self.c = float(self.u_entry.get())
            if self.mode.get() == 3:
                self.c = float(self.answer.get())
            self.answer.set(format(atan(self.c), '.3f'))
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
            self.a_entry.delete(0,END)
            self.b_entry.delete(0,END)
    def root(self):
        try:
            if self.mode.get() == 2:
                self.c = float(self.u_entry.get())
            if self.mode.get() == 3:
                self.c = float(self.answer.get())
            if self.c<0:
                tkinter.messagebox.showerror('Error!','Rooted number cannot be smaller than 0.')
                self.u_entry.delete(0,END)
            else:
                self.answer.set(format(sqrt(self.c), '.3f'))
        except(ValueError):
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
            self.a_entry.delete(0,END)
            self.b_entry.delete(0,END)
    def ln(self):
        if self.mode.get()==1:
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
            self.a_entry.delete(0, END)
            self.b_entry.delete(0, END)
        else:
            try:
                if self.mode.get() == 2:
                    self.c = float(self.u_entry.get())
                if self.mode.get() == 3:
                    self.c = float(self.answer.get())
                self.answer.set(format(log(self.c), '.3f'))
            except(ValueError):
                if self.c <0.0:
                    tkinter.messagebox.showerror('Error!', 'Math domain error.')
                    self.u_entry.delete(0, END)
                else:
                    tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
                    self.a_entry.delete(0, END)
                    self.b_entry.delete(0, END)
    def lg(self):
        if self.mode.get()==1:
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
            self.a_entry.delete(0, END)
            self.b_entry.delete(0, END)
        else:
            try:
                if self.mode.get() == 2:
                    self.c = float(self.u_entry.get())
                if self.mode.get() == 3:
                    self.c = float(self.answer.get())
                self.answer.set(format(log10(self.c), '.3f'))
            except(ValueError):
                if self.c <0.0:
                    tkinter.messagebox.showerror('Error!', 'Math domain error.')
                    self.u_entry.delete(0, END)
                else:
                    tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
                    self.a_entry.delete(0, END)
                    self.b_entry.delete(0, END)
    def log_2(self):
        if self.mode.get()==1:
            tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
            self.a_entry.delete(0, END)
            self.b_entry.delete(0, END)
        else:
            try:
                if self.mode.get() == 2:
                    self.c = float(self.u_entry.get())
                if self.mode.get() == 3:
                    self.c = float(self.answer.get())
                self.answer.set(format(log2(self.c), '.3f'))
            except(ValueError):
                if self.c <0.0:
                    tkinter.messagebox.showerror('Error!', 'Math domain error.')
                    self.u_entry.delete(0, END)
                else:
                    tkinter.messagebox.showerror('Error!', 'It is a unary computation.')
                    self.a_entry.delete(0, END)
                    self.b_entry.delete(0, END)
    def clear(self):
        self.a_entry.delete(0,END)
        self.b_entry.delete(0, END)
        self.u_entry.delete(0, END)
        self.c_entry.delete(0, END)
        self.answer.set(0)
    def base(self):
        B=Base_Convert()
C=Calculate()

