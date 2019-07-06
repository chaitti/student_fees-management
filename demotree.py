from tkinter import *
from tkinter.ttk import *

class demotree:
    def __init__(self):
        self.root=Tk()

        self.t1=Treeview(self.root,columns=("rollno","name","course","age"))
        self.t1.heading("rollno",text="Roll Number")
        self.t1.heading("name", text="Student Name")
        self.t1.heading("course", text="course")
        self.t1.heading("age", text="Student Age")
        self.t1["show"]="headings"
        self.t1.insert("",index=0,values=[1,"Ramesh","MCA",22])
        self.t1.insert("",index=1,values=[2,"Tarun","MCA",22])
        self.t1.insert("",index=2,values=[3,"Nikhil","MCA",22])
        self.t1.pack()

        self.root.mainloop()
#--------------------------------
obj=demotree()