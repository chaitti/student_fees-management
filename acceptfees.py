from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from tkcalendar import *
from connection import *
class acceptfees:

    def insert(self):
        s="insert into fees values(NULL,"+self.cb1.get()+",'"+self.textbox2.get()+"',"+self.textbox3.get()+","+self.textbox4.get()+")"
        cr=conn.cursor()
        cr.execute(s)
        conn.commit()
        showinfo("","Fees Accepted")

    def __init__(self):

        q="select rollno from students"
        cr=conn.cursor()
        cr.execute(q)
        result=cr.fetchall()

        x=[]

        for p in result:
            x.append(p)


        self.root=Tk()
        self.lb1=Label(self.root,text="Enter Roll Number")
        self.lb2=Label(self.root,text="Enter Date of Deposit")
        self.lb3=Label(self.root,text="Enter Semester ")
        self.lb4=Label(self.root,text="Enter Amount")

        self.cb1=Combobox(self.root,values=x,state="readonly")
        self.textbox2=DateEntry(self.root)
        self.textbox3=Entry(self.root)
        self.textbox4=Entry(self.root)

        self.bt1=Button(self.root,text="Submit",command=self.insert)

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.lb3.grid(row=2,column=0)
        self.lb4.grid(row=3,column=0)

        self.cb1.grid(row=0,column=1)
        self.textbox2.grid(row=1,column=1)
        self.textbox3.grid(row=2,column=1)
        self.textbox4.grid(row=3,column=1)

        self.bt1.grid(row=4,column=1)


        self.root.mainloop()
#----------------------------------------------






