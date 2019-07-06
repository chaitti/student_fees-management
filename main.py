from tkinter import *
from addstudent import *
from showdata import *
from editdelete import *
from acceptfees import *
from PIL import ImageTk,Image
import image
class main:

    def fire1(self):
        obj=addstudent()
    def fire2(self):
        obj=showdata()
    def fire3(self):
        editdelete()
    def fire4(self):
        acceptfees()

    def __init__(self):
        self.root=Tk()
        self.root.geometry("1024x800")
        self.mymenu=Menu(self.root)
        self.root.config(menu=self.mymenu)
        self.submenu1 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Student", menu=self.submenu1)
        self.submenu1.add_command(label="Add Student", command=self.fire1)
        self.submenu1.add_command(label="View Students", command=self.fire2)
        self.submenu1.add_command(label="Edit/Delete Student",command=self.fire3)

        self.submenu2=Menu(self.mymenu,tearoff=False)
        self.mymenu.add_cascade(label="Transactions",menu=self.submenu2)
        self.submenu2.add_command(label="Accept Fees", command=self.fire4)
        self.canvas = Canvas(self.root, width=1200, height=900)
        self.canvas.pack()
        img = ImageTk.PhotoImage(Image.open("j1.jpg"))
        self.canvas.create_image(20, 20, anchor=NW, image=img)



        self.root.mainloop()

#====================------------------

main()
