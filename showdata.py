
from tkinter import *
from tkinter.ttk import *
from pymysql import *
class showdata:
    def __init__(self):
        self.root=Tk()

        self.t1=Treeview(self.root,columns=("rollno","name","course","age"))
        self.t1.heading("rollno",text="Roll Number")
        self.t1.heading("name", text="Student Name")
        self.t1.heading("course", text="course")
        self.t1.heading("age", text="Student Age")
        self.t1["show"]="headings"

        conn=Connect("127.0.0.1","root","","rider")
        s="select * from students"
        cr=conn.cursor()
        cr.execute(s)
        result=cr.fetchall()

        for i in range(0,len(result)):
            row=result[i]
            self.t1.insert("",index=i,values=row)



        self.t1.pack()

        self.root.mainloop()
#--------------------------------
