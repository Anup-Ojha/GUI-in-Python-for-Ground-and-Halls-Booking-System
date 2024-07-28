
from tkinter import *
root = Tk()
root.config()
def mobi():
    selection = "SELECTED GADGET is " +str  (mobile.get(),computer.get(),laptop.get())
    label.config(text=selection)

mobile=StringVar()
laptop=StringVar()
computer=StringVar()
mal1e=Checkbutton(root,text="Laptop",variable=laptop,onvalue="Laptop").pack()
fema1le=Checkbutton(root,text="Computer",variable=computer,onvalue="Computer").pack()
other1s=Checkbutton(root,text="Mobile",variable=mobile,onvalue="Mobile").pack()
submit = Button(root,text="Submit",command=mobi).pack()

label = Label(root)
label.pack()
root.mainloop()
