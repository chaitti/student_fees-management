from tkinter import *
from tkinter.messagebox import showinfo

from pymysql import *

class addstudent:

    def insert(self):
        if self.textbox1.get()=="" or self.textbox2.get()=="" or self.textbox3.get()=="" or self.textbox4.get()=="":
            showinfo("","Please Fill All Values")
        elif str(self.textbox1.get()).isdigit()==False:
            showinfo("","Roll Number Must be Numeric")
        elif str(self.textbox4.get()).isdigit()==False:
            showinfo("","Age Must Be Numeric")
        else:

            s="insert into students values("+self.textbox1.get()+",'"+self.textbox2.get()+"','"+self.textbox3.get()+"',"+self.textbox4.get()+")"

            conn=Connect("127.0.0.1","root","","rider")

            cr=conn.cursor()
            cr.execute(s)
            conn.commit()
            conn.close()
            showinfo("","Data Inserted")


    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")

        self.lb1=Label(self.root,text="Enter Roll Number")
        self.lb2=Label(self.root,text="Enter Name")
        self.lb3=Label(self.root,text="Enter Course")
        self.lb4=Label(self.root,text="Enter Age")

        self.textbox1=Entry(self.root)
        self.textbox2=Entry(self.root)
        self.textbox3=Entry(self.root)
        self.textbox4=Entry(self.root)

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.lb3.grid(row=2,column=0)
        self.lb4.grid(row=3,column=0)

        self.textbox1.grid(row=0,column=1)
        self.textbox2.grid(row=1,column=1)
        self.textbox3.grid(row=2,column=1)
        self.textbox4.grid(row=3,column=1)
        self.bt1=Button(self.root,text="Submit",command=self.insert)

        self.bt1.grid(row=4,column=1)

        self.root.mainloop()
#--------------------------------------------




