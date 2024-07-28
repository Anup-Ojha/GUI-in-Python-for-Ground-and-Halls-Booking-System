# Write a program for gender selection using radio button. When the user clicks on submit
# button it should display the selected gender on a label.
from tkinter import *
root = Tk()
root.config()
def show():
    selection = "SELECTED GENDER is " + str (userinput.get())
    label.config(text=selection)

userinput=StringVar()
mal1e=Radiobutton(root,text="MALE",value="MALE",variable=userinput).pack()
fema1le=Radiobutton(root,text="FEMALE",value="FEMALE",variable=userinput).pack()
other1s=Radiobutton(root,text="OTHERS",value="OTHERS",variable=userinput).pack()
submit = Button(root,text="Submit",command=show).pack()

label = Label(root)
label.pack()
root.mainloop()
