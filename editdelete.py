from tkinter import *
from tkinter.messagebox import showinfo

from pymysql import *

class editdelete:

    def search(self):
        self.bt1["state"]="disabled"
        conn=Connect("127.0.0.1","root","","rider")
        s="select * from students where rollno="+self.textbox1.get()
        cr=conn.cursor()
        n=cr.execute(s)
        result=cr.fetchone()
        self.textbox2.delete(0,END)
        self.textbox3.delete(0,END)
        self.textbox4.delete(0,END)
        if n==1:
            self.bt1["state"]="normal"
            self.textbox2.insert(0,result[1])
            self.textbox3.insert(0,result[2])
            self.textbox4.insert(0,result[3])




    def remove(self):
        conn=Connect("127.0.0.1","root","","rider")
        s="delete from students where rollno="+self.textbox1.get()
        cr=conn.cursor()
        cr.execute(s)
        conn.commit()
        showinfo("","Student Record Deleted")

    def update(self):
        conn=Connect("127.0.0.1","root","","rider")
        s="update students set name='"+self.textbox2.get()+"',course='"+self.textbox3.get()+"',age="+self.textbox4.get()+" where rollno="+self.textbox1.get()
        cr=conn.cursor()
        cr.execute(s)
        conn.commit()
        showinfo("","Student Record Updated")







    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x300")

        self.lb1=Label(self.root,text="Enter Roll Number")
        self.bt2=Button(self.root,text="Search",command=self.search)
        self.bt2.grid(row=0,column=2)
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
        self.bt1=Button(self.root,text="Delete",command=self.remove,state="disabled")
        self.bt3=Button(self.root,text="Save",command=self.update)

        self.bt1.grid(row=4,column=1)
        self.bt3.grid(row=4,column=2)

        self.root.mainloop()
#--------------------------------------------
