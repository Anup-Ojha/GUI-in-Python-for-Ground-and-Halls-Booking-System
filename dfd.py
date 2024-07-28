from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox as box

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="mydatabase"
# )

# base = mydb.cursor()

root = Tk()
frame1 = tk.Frame(root)

frame1.grid(padx=350, pady=200)

root.geometry("1500x800")
root.minsize(1500, 800)
root.config(bg="grey")
anup = StringVar()
ojha = StringVar()
anu = tk.Label(frame1, text="WELCOME TO 'VATICA'S ", font=('Helvatica bold', 50), bg="BLUE", fg="RED")
anu.grid()

def getvalues():
    print("The value of username is", {valuefromuser.get()})
    print("The value of password is", {passfromuser.get()})

    if (valuefromuser.get()== 'anup' and passfromuser.get() == 'ojha'):
      messagebox.showinfo('RESULT', 'SUCCESSFULLY LOGIN')
      frame1.grid_forget()
      frame2.grid()

    else:
       messagebox.showinfo('RESULT', 'LOGIN FAILED')

valuefromuser = StringVar()
passfromuser = StringVar()


user = Label(frame1, text="USERNAME:-", relief=tk.RIDGE, bg="skyblue", fg="black", width=15, height=2, bd=4)
user.grid(pady=10,)

inpt = Entry(frame1, textvariable=valuefromuser, bd=4, width=20)
inpt.grid(pady=10)


passes = Label(frame1, text="PASSWORD:-", bg="skyblue", relief=tk.RIDGE, fg="black", width=15, height=2, bd=4)

passes.grid(pady=10)

pokepass = Entry(frame1, textvariable=passfromuser, bd=4, show='*', width=20)

pokepass.grid(pady=10)


Button(frame1, text="Submit and login", relief=tk.RAISED, command=getvalues, width=15, height=3, bd=8,
       activebackground='blue', activeforeground='red').grid(pady=20)




frame2=tk.Frame(root,height=1500,width=800)
frame2.grid(padx=35, pady=20)
root.geometry("1500x800")
root.minsize(1500, 800)
root.config(bg="grey")

listbox = Listbox(frame2, bd=6, bg='white', highlightcolor='#f8f9dc', height=6)
listbox.insert(1, "DELHI",)
listbox.insert(2, "MUMBAI")
listbox.insert(3, "PUNE")
listbox.insert(4, "NAGPUR")
listbox.insert(5, "SURAT")
listbox.insert(6, "UDAIPUR")
listbox.grid()

def funk():
    box.showinfo('CITY', 'YOUR SELECTED CITY IS :- ' + listbox.get(listbox.curselection()) )


but = Button(frame2, text="Select", command=funk, relief=tk.RAISED, width=10, height=2, bd=7, bg='#f8f9dc')
but.grid(row=1, column=0)

fliped=StringVar()
fliped.set("JANUARY")
listbox2 = OptionMenu(frame2, fliped, "JANUARY", "FEBRUARY","MARCH","APRIL" ,"MAY","JUNE","JULY","AUGUST","SEPTEMBER", "OCTOBER", "NOVEMBER","DECEMBER")
listbox2.grid(row=0, column=2)

clicked = StringVar()
clicked.set("2022")
listbox3 = OptionMenu(frame2, clicked, "2022", "2023")
listbox3.grid(row=0, column=3)

checked = StringVar()
checked.set("1")
listbox4 = OptionMenu(frame2,checked,"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
listbox4.grid(row=0, column=4)

root.mainloop()