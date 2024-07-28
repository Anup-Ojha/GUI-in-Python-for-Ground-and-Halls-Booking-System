from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
root=tk.Tk()

root.geometry("1500x800")
root.minsize(1500,800)
root.config(bg="grey")

frame=Frame(root,bg="black")
frame.place(relx=1,rely=0.2,relwidth=6,relheight=1.50,anchor='e')

def getvalues():
    username = valuefromuser.get()
    password = passfromuser.get()

    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()

    # Check if the username and password match a record in the database
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo('RESULT', 'SUCCESSFULLY LOGIN')
    else:
        messagebox.showinfo('RESULT', 'LOGIN FAILED')

    conn.close()
anup = StringVar()
ojha = StringVar()
anu=Label(text="Welcome To The Login Screen",font=('Helvatica bold',50),bg="black",fg="white")
anu.place(relx=0,rely=0,relwidth=1.0,relheight=0.112)

user=Label(root,text="USERNAME:-", relief=tk.RIDGE, bg="white",fg="black")
passes=Label(root,text="PASSWORD:-",bg="white", relief=tk.RIDGE,fg="black")

user.configure(anchor="center")
user.place(height=40,width=120,x=600,y=200)
passes.place(height=40,width=120,x=600,y=300)

valuefromuser=StringVar()
passfromuser=StringVar()

inpt=Entry(root,textvariable=valuefromuser)
pokepass=Entry(root,textvariable=passfromuser,show="*")
inpt.place(height=30,width=120,x=750,y=205)
pokepass.place(height=30,width=120,x=750,y=305)

Button(text="Login",command=getvalues).place(height=40,width=180,x=640,y=400)

root.mainloop()
