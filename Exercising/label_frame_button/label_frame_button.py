from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import tkinter.filedialog
from tkinter import *
def func1():
    a=tkinter.filedialog.asksaveasfilename()#返回文件名
    print(a)
    a =tkinter.filedialog.asksaveasfile()#会创建文件
    print(a)
    a =tkinter.filedialog.askopenfilename()#返回文件名
    print(a)
    a =tkinter.filedialog.askopenfile()#返回文件流对象
    print(a)
    a =tkinter.filedialog.askdirectory()#返回目录名
    print(a)
    a =tkinter.filedialog.askopenfilenames()#可以返回多个文件名
    print(a)
    a =tkinter.filedialog.askopenfiles()#多个文件流对象
    print(a)
def func2():
    tkinter.messagebox.showinfo('FAQ','No')
    tkinter.messagebox.showwarning('Wrong','Quit')
    tkinter.messagebox.showinfo('A file.','Yes')
    tkinter.messagebox.askokcancel('Warning', 'Yes or no?')
    tkinter.messagebox.askquestion('Warning', 'Yes or no?')
    tkinter.messagebox.askyesno('Warning', 'Yes or no?')
    tkinter.messagebox.askretrycancel('Warning', 'Try again.')
class MyGUI:
    def __init__(self):
        self.main_window=Tk()
        self.top_frame=Frame(self.main_window,bg='white')
        self.middle_frame=Frame(self.main_window)
        self.bottom_frame=Frame(self.main_window)
        self.label_1=Label(self.top_frame,text='Hello World!',width=10,height=2,fg='green',bg='blue',font=('Segoe UI Black',20),\
                           cursor='exchange',relief='groove')
        self.label_2=Label(self.top_frame,text='Helol Wolrd!',fg='red',bg='yellow',font=('BIZ UDGothic',35),cursor='fleur'\
                           ,relief='raised')
        self.label_3=Label(self.top_frame,text='Hlelo Wdlor!',fg='blue',bg='black',font=('Ink Free',25),cursor='pirate',relief='ridge')
        self.label_1.pack(side='top')
        self.label_2.pack(side='bottom')
        self.label_3.pack(side='bottom')
        self.label_4=Label(self.middle_frame,text='Lehol Orwdl!',fg='cyan',bg='brown',font=('Ink Free',15),cursor='watch',relief='solid')
        self.label_5=Label(self.middle_frame,text='Ohwre!Ld lol',fg='black',bg='cyan',font=('Ink Free',15),cursor='trek',relief='sunken')
        self.label_4.pack(side='left')
        self.label_5.pack(side='right')
        self.label_6=Label(self.bottom_frame,text='お前はもう死んている',fg='cyan',bg='blue',font=('UD Digi Kyokasho NK-B',40)\
                           ,anchor='w',justify='right',cursor='sizing',state='disabled',underline=5)
        self.label_7=Label(self.bottom_frame,text='dushsudhwiuedhiuhawuhdiuwahdiuhdiuhaiudshauwifhdwhdeiuhw',wraplength=100\
                           ,anchor='w',justify='left',cursor='dotbox')
        self.label_6.pack(side='bottom',fill='both')
        self.label_7.pack(side='bottom')
        self.top_frame.pack(fill='both')
        self.middle_frame.pack()
        self.bottom_frame.pack()
        self.__click_button=Button(self.main_window,text='click me!',command=self.do_something,cursor='shuttle',repeatdelay=1000,repeatinterval=300)
        self.__photo = PhotoImage(file='test.png')
        self.__image_button=Button(self.main_window,text='A Look!',image=self.__photo,command=self.View,cursor='man',font=('Ink Free',35),compound='center')
        self.__quit_button=Button(self.main_window,text='QUIT',command=self.main_window.destroy,cursor='spraycan',relief='solid',\
                                  bg='red',default='normal')
        self.__click_button.pack(fill='x')
        self.__quit_button.pack(fill='x')
        self.__image_button.pack(fill='x')
        mainloop()
    def View(self):
        self.root=Toplevel()
        self.image_frame = Frame(self.root)
        self.photo = PhotoImage(file='test.png')
        self.image_label = Label(self.image_frame, image=self.photo,cursor='heart')
        self.image_label.pack(fill='both')
        self.image_frame.pack(fill='both')
        mainloop()
    def do_something(self):
        tkinter.messagebox.showinfo('Response','Thanks to click the button.')
MyGui=MyGUI()