from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.messagebox as box
import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root",
#     database="mydatabase"
# )

root = Tk()
root.geometry("1350x700")
root.maxsize(1400, 700)
root.minsize(1100, 750)
root.config(bg="#669999")

frame5 = Frame(root, width=1400, height=750, background="#b39c7e")
frame5.place(x=0, y=0)
framelast = Frame(frame5, width=1100, bd=20, height=650, bg="black")
framelast.place(bordermode="inside", x=140, y=50)
frameout = Frame(root, width=1100, bd=20, height=650, bg="black")
frameout.place(bordermode="inside", x=140, y=50)
frame2 = Frame(root, width=1000, bd=8, height=600, bg="#367568")
frame2.place(bordermode=OUTSIDE, y=70, x=190)

frame3 = Frame(frame2, width=800, height=260)
frame3.place(bordermode=OUTSIDE, y=20, x=100)
frame4 = Frame(frame2, width=900, height=300, bg="#367568")
frame4.place(y=300, x=100)
# ----------------------------------
my_menu = Menu(root)
root.config(menu=my_menu)

def our_command():
    messagebox.showinfo("Software", "Please Call/Email On The Given For Queries, Registering Complaints :- 9309109229"
                                    "                                                       "
                                    "      Email :- anup2001ojha@gmail.com")
file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="MENU", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

goto_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="HELP", menu=goto_menu)
goto_menu.add_command(label="CONTACT US", command=our_command)

scroll_y = Scrollbar(frame4, orient=VERTICAL)
displaytable = ttk.Treeview(frame4, height=12, columns=("SRNO", "CITY", "Hall Name", "Date",
                                                        "Booked By", "Contact No", "days", "amount", "address"),
                            yscrollcommand=scroll_y.set)
scroll_y.pack(side=RIGHT, fill=Y)

displaytable.heading("SRNO", text="SRNO")
displaytable.heading("CITY", text="CITY")
displaytable.heading("Hall Name", text="HALLNAME")
displaytable.heading("Date", text="DATE")
displaytable.heading("Booked By", text="BOOKED BY")
displaytable.heading("Contact No", text="CONTACT NO.")
displaytable.heading("days", text="DAYS")
displaytable.heading("amount", text="AMOUNT")
displaytable.heading("address", text="ADDRESS")

displaytable['show'] = 'headings'

displaytable.column("SRNO", width=50)
displaytable.column("CITY", width=70)
displaytable.column("Hall Name", width=100)
displaytable.column("Date", width=70)
displaytable.column("Booked By", width=100)
displaytable.column("Contact No", width=90)
displaytable.column("days", width=50)
displaytable.column("amount", width=70)
displaytable.column("address", width=100)

displaytable.pack(fill=BOTH, expand=1)
displaytable.bind("<ButtonRelease-1>")


def displaydata():
    sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
    cur = sqlcon.cursor()
    cur.execute("select * from displaytable")
    result = cur.fetchall()
    if len(result) != 0:
        displaytable.delete(*displaytable.get_children())
        for row in result:
            displaytable.insert('', END, values=row)
            sqlcon.commit()
    sqlcon.close()


def displaydelete():
    sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
    cur = sqlcon.cursor()
    valu = [str(srno.get())]
    sql = ("DELETE FROM displaytable where srno=%s")
    cur.execute(sql, valu)
    messagebox.showinfo("SYSTEM", "Deleted Succesfully")
    sqlcon.commit()
    sqlcon.close()


serial = StringVar()
lblstid = Label(frame2, font=('arial', 12, 'bold'), text="Enter Srno. To", bd=7)
lblstid.place(x=860, y=300)
lblstid1 = Label(frame2, font=('arial', 12, 'bold'), text="Delete:-", bd=7)
lblstid1.place(x=860, y=330)
srno = Entry(frame2, font=('arial', 12, 'bold'), bd=7, width=10, justify='left', textvariable=serial)
srno.place(x=870, y=380)

btn2 = Button(frame2, text="SEE BOOKINGS", relief=tk.RAISED, command=displaydata, width=11, height=2, bd=6)
btn2.place(x=480, y=220)

btn3 = Button(frame2, text="DELETE BOOKING", relief=tk.RAISED, command=displaydelete, width=13, height=2, bd=6)
btn3.place(x=860, y=420)


# ======================Defined functions========================
def getvalues():
    if (valuefromuser.get() == 'anup' and passfromuser.get() == 'ojha'):
        messagebox.showinfo('RESULT', 'SUCCESSFULLY LOGIN')
        frame1.destroy()
        frame2.place()
    else:
        messagebox.showinfo('RESULT', 'LOGIN FAILED')


frame1 = Frame(root, width=1000, height=600)
frame1.place(bordermode=OUTSIDE, y=70, x=190)

canvas = Canvas(frame1, width=995, height=595)
canvas.place(bordermode='inside', x=1, y=1)


anup = StringVar()
ojha = StringVar()
anu = tk.Label(frame1, text="BOOK MY GARDEN ", font=('Helvatica bold', 50), bg="#B8E9FA", fg="RED")
anu.place(y=20, x=180)

user = tk.Label(frame1, text="USERNAME:-", relief=tk.RIDGE, bg="skyblue", fg="black", width=15, height=2, bd=4)
user.place(y=120, x=320)

valuefromuser = StringVar()
passfromuser = StringVar()

inpt = Entry(frame1, textvariable=valuefromuser, font=('arial', 8, 'bold'), bd=4, width=20)
inpt.place(x=450, y=130)

pwd = tk.Label(frame1, text="PASSWORD:-", relief=tk.RIDGE, bg="skyblue", fg="black", width=15, height=2, bd=4)
pwd.place(y=180, x=320)

passinput = Entry(frame1, textvariable=passfromuser, font=('arial', 8, 'bold'), show='*', bd=4, width=20)
passinput.place(x=450, y=180)

btn = Button(frame1, text="Submit and login", relief=tk.RAISED, command=getvalues, width=13, height=2, bd=6,
             activebackground='blue', activeforeground='red').place(x=460, y=230)

lbl = tk.Label(frame2, text="Please Select Your City and Date ", font=('Helvatica bold', 30), fg="black")
lbl.place(y=20, x=180)
citylabel = Label(frame2, border=5, height=0, width=5, font=("Helvatica bold", 15), relief=tk.RIDGE, fg="black",
                  bg='skyblue', text='CITY').place(y=75, x=220)
monthlabel = Label(frame2, border=5, height=0, width=7, font=("Helvatica bold", 15), fg="black", relief=tk.RIDGE,
                   bg='skyblue', text='MONTH').place(y=75, x=360)
datelabel = Label(frame2, border=5, height=0, width=5, font=("Helvatica bold", 15), fg="black", relief=tk.RIDGE,
                  bg='skyblue', text='DATE').place(y=75, x=480)
yearlabel = Label(frame2, border=5, height=0, width=5, font=("Helvatica bold", 15), fg="black", relief=tk.RIDGE,
                  bg='skyblue', text='YEAR').place(y=75, x=575)
listbox = Listbox(frame2, bd=6, border=7, bg='white', highlightcolor='#f8f9dc', height=6, exportselection=0)

listbox.insert(1, "DELHI")
listbox.insert(2, "MUMBAI")
listbox.insert(3, "PUNE")
listbox.insert(4, "NAGPUR")
listbox.bind("<<ListboxSelect>>", lambda x: go())
listbox.place(y=110, x=180)

listbox2 = Listbox(frame2, bd=6, bg='white', border=7, height=6, exportselection=0)
listbox2.insert(1, "JANUARY")
listbox2.insert(2, "FEBRUARY")
listbox2.insert(3, "MARCH")
listbox2.insert(4, "APRIL")
listbox2.insert(5, "MAY")
listbox2.insert(6, "JUNE")
listbox2.insert(7, "JULY")
listbox2.insert(8, "AUGUST")
listbox2.insert(9, "SEPTEMBER")
listbox2.insert(10, "OCTOBER")
listbox2.insert(11, "NOVEMBER")
listbox2.insert(12, "DECEMBER")
listbox2.bind("<<ListboxSelect>>", lambda x: lo())
listbox2.place(y=110, x=330)

listbox3 = Listbox(frame2, bd=2, bg='white', border=7, height=6, width=10, exportselection=0)

mylist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
          "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "30", "31"]
for items in mylist:
    listbox3.insert(END, items)
listbox3.bind("<<ListboxSelect>>", lambda x: fo())
listbox3.place(y=110, x=480)

listbox4 = Listbox(frame2, bd=6, bg='white', border=7, height=6, width=10, exportselection=0)
listbox4.insert(1, "2022")
listbox4.insert(2, "2023")
listbox4.bind("<<ListboxSelect>>", lambda x: ho())
listbox4.place(y=110, x=570)

frame6 = Frame(frame5, height=600, width=1000, background="#367568")
frame6.place(x=190, y=70)


def funk():
    box.askokcancel('System', 'YOUR SELECTED CITY IS:- ' + listbox.get(listbox.curselection()) +
                    str("_DATE_") + str(listbox3.get(listbox3.curselection())) + str(" ") + listbox2.get(
        listbox2.curselection()))
    u = listbox.curselection()

    def seelistdelhi():
        sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
        cur = sqlcon.cursor()
        cur.execute("select * from delhi")
        result = cur.fetchall()
        if len(result) != 0:
            delhi.delete(*delhi.get_children())
            for row in result:
                delhi.insert('', END, values=row)
                sqlcon.commit()
        sqlcon.close()

    def seelistpune():
        sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
        cur = sqlcon.cursor()
        cur.execute("select * from pune")
        result = cur.fetchall()
        if len(result) != 0:
            pune.delete(*pune.get_children())
            for row in result:
                pune.insert('', END, values=row)
                sqlcon.commit()
        sqlcon.close()

    def seelistnagpur():
        sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
        cur = sqlcon.cursor()
        cur.execute("select * from nagpur")
        result = cur.fetchall()
        if len(result) != 0:
            nagpur.delete(*nagpur.get_children())
            for row in result:
                nagpur.insert('', END, values=row)
                sqlcon.commit()
        sqlcon.close()

    def seelistmumbai():
        sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
        cur = sqlcon.cursor()
        cur.execute("select * from mumbai")
        result = cur.fetchall()
        if len(result) != 0:
            mumbai.delete(*mumbai.get_children())
            for row in result:
                mumbai.insert('', END, values=row)
                sqlcon.commit()
        sqlcon.close()

    if listbox.curselection() == ((1,)):
        scroll_y4 = Scrollbar(frame7, orient=VERTICAL)
        mumbai = ttk.Treeview(frame7, height=10, columns=("SRNO", "Hall Name", "Address", "Capacity", "Price"),
                              yscrollcommand=scroll_y4.set)
        scroll_y4.pack(side=RIGHT, fill=Y)

        mumbai.heading("SRNO", text="Srno")
        mumbai.heading("Hall Name", text="Hall Name")
        mumbai.heading("Address", text="Address")
        mumbai.heading("Capacity", text="Capacity")
        mumbai.heading("Price", text="Price")

        mumbai['show'] = 'headings'

        mumbai.column("SRNO", width=50)
        mumbai.column("Hall Name", width=100)
        mumbai.column("Address", width=235)
        mumbai.column("Capacity", width=100)
        mumbai.column("Price", width=100)

        mumbai.pack(fill=BOTH, expand=2)
        mumbai.bind("<<ListboxSelect>>")

        dekhlo3 = Button(frame5, text="SEE Lawns", relief=tk.RAISED, command=seelistmumbai, width=11, height=2, bd=6)
        dekhlo3.place(x=230, y=400)

    elif listbox.curselection() == (3,):
        scroll_y2 = Scrollbar(frame7, orient=VERTICAL)
        nagpur = ttk.Treeview(frame7, height=10, columns=("SRNO", "Hall Name", "Address", "Capacity", "Price"),
                              yscrollcommand=scroll_y2.set)
        scroll_y2.pack(side=RIGHT, fill=Y)

        nagpur.heading("SRNO", text="Srno")
        nagpur.heading("Hall Name", text="Hall Name")
        nagpur.heading("Address", text="Address")
        nagpur.heading("Capacity", text="Capacity")
        nagpur.heading("Price", text="Price")

        nagpur['show'] = 'headings'

        nagpur.column("SRNO", width=50)
        nagpur.column("Hall Name", width=100)
        nagpur.column("Address", width=235)
        nagpur.column("Capacity", width=100)
        nagpur.column("Price", width=100)

        nagpur.pack(fill=BOTH, expand=2)
        nagpur.bind("<<ListboxSelect>>")

        dekhlo1 = Button(frame5, text="SEE Lawns", relief=tk.RAISED, command=seelistnagpur, width=11, height=2, bd=6)
        dekhlo1.place(x=230, y=400)

    elif listbox.curselection() == (2,):

        scroll_y3 = Scrollbar(frame7, orient=VERTICAL)
        pune = ttk.Treeview(frame7, height=10, columns=("SRNO", "Hall Name", "Address", "Capacity", "Price"),
                            yscrollcommand=scroll_y3.set)
        scroll_y3.pack(side=RIGHT, fill=Y)

        pune.heading("SRNO", text="Srno")
        pune.heading("Hall Name", text="Hall Name")
        pune.heading("Address", text="Address")
        pune.heading("Capacity", text="Capacity")
        pune.heading("Price", text="Price")

        pune['show'] = 'headings'

        pune.column("SRNO", width=50)
        pune.column("Hall Name", width=100)
        pune.column("Address", width=235)
        pune.column("Capacity", width=100)
        pune.column("Price", width=100)

        pune.pack(fill=BOTH, expand=2)
        pune.bind("<<ListboxSelect>>")

        dekhlo2 = Button(frame5, text="SEE Lawns", relief=tk.RAISED, command=seelistpune, width=11, height=2, bd=6)
        dekhlo2.place(x=230, y=400)

    elif listbox.curselection() == (0,):
        scroll_y1 = Scrollbar(frame7, orient=VERTICAL)
        delhi = ttk.Treeview(frame7, height=10, columns=("SRNO", "Hall Name", "Address", "Capacity", "Price"),
                             yscrollcommand=scroll_y1.set)
        scroll_y1.pack(side=RIGHT, fill=Y)
        delhi.heading("SRNO", text="Srno")
        delhi.heading("Hall Name", text="Hall Name")
        delhi.heading("Address", text="Address")
        delhi.heading("Capacity", text="Capacity")
        delhi.heading("Price", text="Price")

        delhi['show'] = 'headings'

        delhi.column("SRNO", width=50)
        delhi.column("Hall Name", width=100)
        delhi.column("Address", width=235)
        delhi.column("Capacity", width=100)
        delhi.column("Price", width=100)

        delhi.pack(fill=BOTH, expand=2)
        delhi.bind("<<ListboxSelect>>")
        dekhlo = Button(frame5, text="SEE Lawns", relief=tk.RAISED, command=seelistdelhi, width=11, height=2, bd=6)
        dekhlo.place(x=230, y=400)
    frameout.place_forget()
    frame2.place_forget()
    frame5.place()


def go():
    cs = listbox.curselection()[0]
    ll2['text'] = listbox.get(cs)


def lo():
    cs = listbox2.curselection()[0]
    ll4['text'] = listbox2.get(cs)


def fo():
    cs = listbox3.curselection()[0]
    ll5['text'] = listbox3.get(cs)


def ho():
    cs = listbox4.curselection()[0]
    l6['text'] = listbox4.get(cs)


ll1 = tk.Label(frame6, text='Selected City is :-', width=20, height=2, relief=tk.RIDGE, font=7)
ll1.place(x=25, y=20)
ll2 = tk.Label(frame6, width=15, height=2, relief=tk.RIDGE, font=7)
ll2.place(x=245, y=20)

ll3 = tk.Label(frame6, text='Selected Date is :-', width=20, height=2, relief=tk.RIDGE, font=7)
ll3.place(x=400, y=20)
ll4 = tk.Label(frame6, width=14, height=2, relief=tk.RIDGE, font=3)
ll4.place(x=600, y=20)

l6 = tk.Label(frame6, width=15, height=2, relief=tk.RIDGE, font=3)
l6.place(x=800, y=20)

ll5 = tk.Label(frame6, width=8, height=2, relief=tk.RIDGE, font=3)
ll5.place(x=750, y=20)

but = Button(frame2, text="SELECT", command=(funk), relief=tk.RAISED, width=11, height=2, bd=6)
but.place(x=360, y=220)

frame7 = Frame(frame6, width=900, height=450)
frame7.place(y=90, x=50)
# =========================================================================================================


srno223 = Label(frame6, text="Bill No", font=12, width=10, relief=RIDGE, bd=4)
srno223.place(x=670, y=100)
srno22 = StringVar()
srno20 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=srno22)
srno20.place(x=800, y=100)

namelabel = Label(frame6, text="CITY", font=12, width=10, relief=RIDGE, bd=4)
namelabel.place(x=670, y=140)
namelabel1 = StringVar()
srno50 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=namelabel1)
srno50.place(x=800, y=140)

hallname1 = Label(frame6, text="HALLNAME", width=10, font=12, relief=RIDGE, bd=4)
hallname1.place(x=670, y=180)
hallname12 = StringVar()
srno2 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=hallname12)
srno2.place(x=800, y=180)

datee = Label(frame6, text="DATE", width=10, font=7, relief=RIDGE, bd=4)
datee.place(x=670, y=220)
datee5 = StringVar()
datee1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=datee5)
datee1.place(x=800, y=220)

BOOKEDBY = Label(frame6, text="BILLED BY", width=10, font=7, relief=RIDGE, bd=4)
BOOKEDBY.place(x=670, y=260)
BOOKEDBY5 = StringVar()
BOOKEDBY1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=BOOKEDBY5)
BOOKEDBY1.place(x=800, y=260)

contact = Label(frame6, text='PHONE NO', width=10, font=5, relief=RIDGE, bd=4)
contact.place(x=670, y=300)
contact5 = StringVar()
contact1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=contact5)
contact1.place(x=800, y=300)

days = Label(frame6, text='DAYS', width=10, font=5, relief=RIDGE, bd=4)
days.place(x=670, y=340)
days5 = StringVar()
days1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=days5)
days1.place(x=800, y=340)

ammount = Label(frame6, text='AMMOUNT', width=10, font=5, relief=RIDGE, bd=4)
ammount.place(x=670, y=380)
ammount5 = StringVar()
ammount1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=ammount5)
ammount1.place(x=800, y=380)

address = Label(frame6, text='ADDRESS', width=10, font=5, relief=RIDGE, bd=4)
address.place(x=670, y=420)
address5 = StringVar()
address1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=address5)
address1.place(x=800, y=420)


def booked():
    if srno22.get() == "" or namelabel1.get() == "" or hallname12.get() == "" or datee5.get() == "" or BOOKEDBY5.get() == "" or contact5.get() == "" \
            or days5.get() == "" or ammount5.get() == "" or address5.get() == "":
        messagebox.showerror("System", "Please enter all details")
    else:
        sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
        cur = sqlcon.cursor()
        cur.execute("INSERT INTO displaytable VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        srno22.get(),
                        namelabel1.get(),
                        hallname12.get(),
                        datee5.get(),
                        BOOKEDBY5.get(),
                        contact5.get(),
                        days5.get(),
                        ammount5.get(),
                        address5.get()
                    ))
        sqlcon.commit()
        sqlcon.close()
        messagebox.showinfo("System", "Booked Successfully")


booked = Button(frame6, text="BOOK", relief=tk.RAISED, command=booked, width=11, height=2, bd=6)
booked.place(x=800, y=460)


def Logout1():
    root.quit()
Logout = Button(frame2, text="LOGOUT", relief=tk.RAISED, command=Logout1, width=11, height=2, bd=6)
Logout.place(x=890, y=540)
Logout = Button(frame6, text="LOGOUT", relief=tk.RAISED, command=Logout1, width=11, height=2, bd=6)
Logout.place(x=890, y=540)


def backu():

    frame5 = Frame(root, width=1400, height=750, background="#b39c7e")
    frame5.place(x=0, y=0)
    framelast = Frame(frame5, width=1100, bd=20, height=650, bg="black")
    framelast.place(bordermode="inside", x=140, y=50)
    frameout = Frame(root, width=1100, bd=20, height=650, bg="black")
    frameout.place(bordermode="inside", x=140, y=50)
    frame2 = Frame(root, width=1000, bd=8, height=600, bg="#367568")
    frame2.place(bordermode=OUTSIDE, y=70, x=190)

    frame3 = Frame(frame2, width=800, height=260)
    frame3.place(bordermode=OUTSIDE, y=20, x=100)
    frame4 = Frame(frame2, width=900, height=300, bg="#367568")
    frame4.place(y=300, x=100)
    # ----------------------------------
    my_menu = Menu(root)
    root.config(menu=my_menu)

    def our_command():
        messagebox.showinfo("Software",
                            "Please Call/Email On The Given For Queries, Registering Complaints :- 9309109229"
                            "                                                       "
                            "      Email :- anup2001ojha@gmail.com")

    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="MENU", menu=file_menu)
    file_menu.add_command(label="Exit", command=root.quit)

    goto_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="HELP", menu=goto_menu)
    goto_menu.add_command(label="CONTACT US", command=our_command)

    scroll_y = Scrollbar(frame4, orient=VERTICAL)
    displaytable = ttk.Treeview(frame4, height=12, columns=("SRNO", "CITY", "Hall Name", "Date",
                                                            "Booked By", "Contact No", "days", "amount", "address"),
                                yscrollcommand=scroll_y.set)
    scroll_y.pack(side=RIGHT, fill=Y)

    displaytable.heading("SRNO", text="SRNO")
    displaytable.heading("CITY", text="CITY")
    displaytable.heading("Hall Name", text="HALLNAME")
    displaytable.heading("Date", text="DATE")
    displaytable.heading("Booked By", text="BOOKED BY")
    displaytable.heading("Contact No", text="CONTACT NO.")
    displaytable.heading("days", text="DAYS")
    displaytable.heading("amount", text="AMOUNT")
    displaytable.heading("address", text="ADDRESS")

    displaytable['show'] = 'headings'

    displaytable.column("SRNO", width=50)
    displaytable.column("CITY", width=70)
    displaytable.column("Hall Name", width=100)
    displaytable.column("Date", width=70)
    displaytable.column("Booked By", width=100)
    displaytable.column("Contact No", width=90)
    displaytable.column("days", width=50)
    displaytable.column("amount", width=70)
    displaytable.column("address", width=100)

    displaytable.pack(fill=BOTH, expand=1)
    displaytable.bind("<ButtonRelease-1>")

    def displaydata():
        sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
        cur = sqlcon.cursor()
        cur.execute("select * from displaytable")
        result = cur.fetchall()
        if len(result) != 0:
            displaytable.delete(*displaytable.get_children())
            for row in result:
                displaytable.insert('', END, values=row)
                sqlcon.commit()
        sqlcon.close()

    def displaydelete():
        sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
        cur = sqlcon.cursor()
        valu = [str(srno.get())]
        sql = ("DELETE FROM displaytable where srno=%s")
        cur.execute(sql, valu)
        messagebox.showinfo("SYSTEM", "Deleted Succesfully")
        sqlcon.commit()
        sqlcon.close()

    serial = StringVar()
    lblstid = Label(frame2, font=('arial', 12, 'bold'), text="Enter Srno. To", bd=7)
    lblstid.place(x=860, y=300)
    lblstid1 = Label(frame2, font=('arial', 12, 'bold'), text="Delete:-", bd=7)
    lblstid1.place(x=860, y=330)
    srno = Entry(frame2, font=('arial', 12, 'bold'), bd=7, width=10, justify='left', textvariable=serial)
    srno.place(x=870, y=380)

    btn2 = Button(frame2, text="SEE BOOKINGS", relief=tk.RAISED, command=displaydata, width=11, height=2, bd=6)
    btn2.place(x=480, y=220)

    btn3 = Button(frame2, text="DELETE BOOKING", relief=tk.RAISED, command=displaydelete, width=13, height=2, bd=6)
    btn3.place(x=860, y=420)

    # ======================Defined functions========================
    def getvalues():
        if (valuefromuser.get() == 'anup' and passfromuser.get() == 'ojha'):
            messagebox.showinfo('RESULT', 'SUCCESSFULLY LOGIN')
            frame1.destroy()
            frame2.place()
        else:
            messagebox.showinfo('RESULT', 'LOGIN FAILED')

    frame1 = Frame(root, width=1000, height=600)
    frame1.place(bordermode=OUTSIDE, y=70, x=190)

    canvas = Canvas(frame1, width=995, height=595)
    canvas.place(bordermode='inside', x=1, y=1)
    img = ImageTk.PhotoImage(Image.open("kk.jpg"))
    canvas.create_image(0, 0, image=img, anchor="nw")

    anup = StringVar()
    ojha = StringVar()
    anu = tk.Label(frame1, text="BOOK MY GARDEN ", font=('Helvatica bold', 50), bg="#B8E9FA", fg="RED")
    anu.place(y=20, x=180)

    user = tk.Label(frame1, text="USERNAME:-", relief=tk.RIDGE, bg="skyblue", fg="black", width=15, height=2, bd=4)
    user.place(y=120, x=320)

    valuefromuser = StringVar()
    passfromuser = StringVar()

    inpt = Entry(frame1, textvariable=valuefromuser, font=('arial', 8, 'bold'), bd=4, width=20)
    inpt.place(x=450, y=130)

    pwd = tk.Label(frame1, text="PASSWORD:-", relief=tk.RIDGE, bg="skyblue", fg="black", width=15, height=2, bd=4)
    pwd.place(y=180, x=320)

    passinput = Entry(frame1, textvariable=passfromuser, font=('arial', 8, 'bold'), show='*', bd=4, width=20)
    passinput.place(x=450, y=180)

    btn = Button(frame1, text="Submit and login", relief=tk.RAISED, command=getvalues, width=13, height=2, bd=6,
                 activebackground='blue', activeforeground='red').place(x=460, y=230)

    lbl = tk.Label(frame2, text="Please Select Your City and Date ", font=('Helvatica bold', 30), fg="black")
    lbl.place(y=20, x=180)
    citylabel = Label(frame2, border=5, height=0, width=5, font=("Helvatica bold", 15), relief=tk.RIDGE, fg="black",
                      bg='skyblue', text='CITY').place(y=75, x=220)
    monthlabel = Label(frame2, border=5, height=0, width=7, font=("Helvatica bold", 15), fg="black", relief=tk.RIDGE,
                       bg='skyblue', text='MONTH').place(y=75, x=360)
    datelabel = Label(frame2, border=5, height=0, width=5, font=("Helvatica bold", 15), fg="black", relief=tk.RIDGE,
                      bg='skyblue', text='DATE').place(y=75, x=480)
    yearlabel = Label(frame2, border=5, height=0, width=5, font=("Helvatica bold", 15), fg="black", relief=tk.RIDGE,
                      bg='skyblue', text='YEAR').place(y=75, x=575)
    listbox = Listbox(frame2, bd=6, border=7, bg='white', highlightcolor='#f8f9dc', height=6, exportselection=0)

    listbox.insert(1, "DELHI")
    listbox.insert(2, "MUMBAI")
    listbox.insert(3, "PUNE")
    listbox.insert(4, "NAGPUR")
    listbox.bind("<<ListboxSelect>>", lambda x: go())
    listbox.place(y=110, x=180)

    listbox2 = Listbox(frame2, bd=6, bg='white', border=7, height=6, exportselection=0)
    listbox2.insert(1, "JANUARY")
    listbox2.insert(2, "FEBRUARY")
    listbox2.insert(3, "MARCH")
    listbox2.insert(4, "APRIL")
    listbox2.insert(5, "MAY")
    listbox2.insert(6, "JUNE")
    listbox2.insert(7, "JULY")
    listbox2.insert(8, "AUGUST")
    listbox2.insert(9, "SEPTEMBER")
    listbox2.insert(10, "OCTOBER")
    listbox2.insert(11, "NOVEMBER")
    listbox2.insert(12, "DECEMBER")
    listbox2.bind("<<ListboxSelect>>", lambda x: lo())
    listbox2.place(y=110, x=330)

    listbox3 = Listbox(frame2, bd=2, bg='white', border=7, height=6, width=10, exportselection=0)

    mylist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
              "20",
              "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "30", "31"]
    for items in mylist:
        listbox3.insert(END, items)
    listbox3.bind("<<ListboxSelect>>", lambda x: fo())
    listbox3.place(y=110, x=480)

    listbox4 = Listbox(frame2, bd=6, bg='white', border=7, height=6, width=10, exportselection=0)
    listbox4.insert(1, "2022")
    listbox4.insert(2, "2023")
    listbox4.bind("<<ListboxSelect>>", lambda x: ho())
    listbox4.place(y=110, x=570)

    frame6 = Frame(frame5, height=600, width=1000, background="#367568")
    frame6.place(x=190, y=70)

    def funk():
        box.askokcancel('System', 'YOUR SELECTED CITY IS:- ' + listbox.get(listbox.curselection()) +
                        str("_DATE_") + str(listbox3.get(listbox3.curselection())) + str(" ") + listbox2.get(
            listbox2.curselection()))
        u = listbox.curselection()

        def seelistdelhi():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
            cur = sqlcon.cursor()
            cur.execute("select * from delhi")
            result = cur.fetchall()
            if len(result) != 0:
                delhi.delete(*delhi.get_children())
                for row in result:
                    delhi.insert('', END, values=row)
                    sqlcon.commit()
            sqlcon.close()

        def seelistpune():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
            cur = sqlcon.cursor()
            cur.execute("select * from pune")
            result = cur.fetchall()
            if len(result) != 0:
                pune.delete(*pune.get_children())
                for row in result:
                    pune.insert('', END, values=row)
                    sqlcon.commit()
            sqlcon.close()

        def seelistnagpur():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
            cur = sqlcon.cursor()
            cur.execute("select * from nagpur")
            result = cur.fetchall()
            if len(result) != 0:
                nagpur.delete(*nagpur.get_children())
                for row in result:
                    nagpur.insert('', END, values=row)
                    sqlcon.commit()
            sqlcon.close()

        def seelistmumbai():
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
            cur = sqlcon.cursor()
            cur.execute("select * from mumbai")
            result = cur.fetchall()
            if len(result) != 0:
                mumbai.delete(*mumbai.get_children())
                for row in result:
                    mumbai.insert('', END, values=row)
                    sqlcon.commit()
            sqlcon.close()

        if listbox.curselection() == ((1,)):
            scroll_y4 = Scrollbar(frame7, orient=VERTICAL)
            mumbai = ttk.Treeview(frame7, height=10, columns=("SRNO", "Hall Name", "Address", "Capacity", "Price"),
                                  yscrollcommand=scroll_y4.set)
            scroll_y4.pack(side=RIGHT, fill=Y)

            mumbai.heading("SRNO", text="Srno")
            mumbai.heading("Hall Name", text="Hall Name")
            mumbai.heading("Address", text="Address")
            mumbai.heading("Capacity", text="Capacity")
            mumbai.heading("Price", text="Price")

            mumbai['show'] = 'headings'

            mumbai.column("SRNO", width=50)
            mumbai.column("Hall Name", width=100)
            mumbai.column("Address", width=235)
            mumbai.column("Capacity", width=100)
            mumbai.column("Price", width=100)

            mumbai.pack(fill=BOTH, expand=2)
            mumbai.bind("<<ListboxSelect>>")

            dekhlo3 = Button(frame5, text="SEE Lawns", relief=tk.RAISED, command=seelistmumbai, width=11, height=2,
                             bd=6)
            dekhlo3.place(x=230, y=400)

        elif listbox.curselection() == (3,):
            scroll_y2 = Scrollbar(frame7, orient=VERTICAL)
            nagpur = ttk.Treeview(frame7, height=10, columns=("SRNO", "Hall Name", "Address", "Capacity", "Price"),
                                  yscrollcommand=scroll_y2.set)
            scroll_y2.pack(side=RIGHT, fill=Y)

            nagpur.heading("SRNO", text="Srno")
            nagpur.heading("Hall Name", text="Hall Name")
            nagpur.heading("Address", text="Address")
            nagpur.heading("Capacity", text="Capacity")
            nagpur.heading("Price", text="Price")

            nagpur['show'] = 'headings'

            nagpur.column("SRNO", width=50)
            nagpur.column("Hall Name", width=100)
            nagpur.column("Address", width=235)
            nagpur.column("Capacity", width=100)
            nagpur.column("Price", width=100)

            nagpur.pack(fill=BOTH, expand=2)
            nagpur.bind("<<ListboxSelect>>")

            dekhlo1 = Button(frame5, text="SEE Lawns", relief=tk.RAISED, command=seelistnagpur, width=11, height=2,
                             bd=6)
            dekhlo1.place(x=230, y=400)

        elif listbox.curselection() == (2,):

            scroll_y3 = Scrollbar(frame7, orient=VERTICAL)
            pune = ttk.Treeview(frame7, height=10, columns=("SRNO", "Hall Name", "Address", "Capacity", "Price"),
                                yscrollcommand=scroll_y3.set)
            scroll_y3.pack(side=RIGHT, fill=Y)

            pune.heading("SRNO", text="Srno")
            pune.heading("Hall Name", text="Hall Name")
            pune.heading("Address", text="Address")
            pune.heading("Capacity", text="Capacity")
            pune.heading("Price", text="Price")

            pune['show'] = 'headings'

            pune.column("SRNO", width=50)
            pune.column("Hall Name", width=100)
            pune.column("Address", width=235)
            pune.column("Capacity", width=100)
            pune.column("Price", width=100)

            pune.pack(fill=BOTH, expand=2)
            pune.bind("<<ListboxSelect>>")

            dekhlo2 = Button(frame5, text="SEE Lawns", relief=tk.RAISED, command=seelistpune, width=11, height=2, bd=6)
            dekhlo2.place(x=230, y=400)

        elif listbox.curselection() == (0,):
            scroll_y1 = Scrollbar(frame7, orient=VERTICAL)
            delhi = ttk.Treeview(frame7, height=10, columns=("SRNO", "Hall Name", "Address", "Capacity", "Price"),
                                 yscrollcommand=scroll_y1.set)
            scroll_y1.pack(side=RIGHT, fill=Y)
            delhi.heading("SRNO", text="Srno")
            delhi.heading("Hall Name", text="Hall Name")
            delhi.heading("Address", text="Address")
            delhi.heading("Capacity", text="Capacity")
            delhi.heading("Price", text="Price")

            delhi['show'] = 'headings'

            delhi.column("SRNO", width=50)
            delhi.column("Hall Name", width=100)
            delhi.column("Address", width=235)
            delhi.column("Capacity", width=100)
            delhi.column("Price", width=100)

            delhi.pack(fill=BOTH, expand=2)
            delhi.bind("<<ListboxSelect>>")
            dekhlo = Button(frame5, text="SEE Lawns", relief=tk.RAISED, command=seelistdelhi, width=11, height=2, bd=6)
            dekhlo.place(x=230, y=400)
        frameout.place_forget()
        frame2.place_forget()
        frame5.place()

    def go():
        cs = listbox.curselection()[0]
        ll2['text'] = listbox.get(cs)

    def lo():
        cs = listbox2.curselection()[0]
        ll4['text'] = listbox2.get(cs)

    def fo():
        cs = listbox3.curselection()[0]
        ll5['text'] = listbox3.get(cs)

    def ho():
        cs = listbox4.curselection()[0]
        l6['text'] = listbox4.get(cs)

    ll1 = tk.Label(frame6, text='Selected City is :-', width=20, height=2, relief=tk.RIDGE, font=7)
    ll1.place(x=25, y=20)
    ll2 = tk.Label(frame6, width=15, height=2, relief=tk.RIDGE, font=7)
    ll2.place(x=245, y=20)

    ll3 = tk.Label(frame6, text='Selected Date is :-', width=20, height=2, relief=tk.RIDGE, font=7)
    ll3.place(x=400, y=20)
    ll4 = tk.Label(frame6, width=14, height=2, relief=tk.RIDGE, font=3)
    ll4.place(x=600, y=20)

    l6 = tk.Label(frame6, width=15, height=2, relief=tk.RIDGE, font=3)
    l6.place(x=800, y=20)

    ll5 = tk.Label(frame6, width=8, height=2, relief=tk.RIDGE, font=3)
    ll5.place(x=750, y=20)

    but = Button(frame2, text="SELECT", command=(funk), relief=tk.RAISED, width=11, height=2, bd=6)
    but.place(x=360, y=220)

    frame7 = Frame(frame6, width=900, height=450)
    frame7.place(y=90, x=50)
    # =========================================================================================================

    srno223 = Label(frame6, text="Bill No", font=12, width=10, relief=RIDGE, bd=4)
    srno223.place(x=670, y=100)
    srno22 = StringVar()
    srno20 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=srno22)
    srno20.place(x=800, y=100)

    namelabel = Label(frame6, text="CITY", font=12, width=10, relief=RIDGE, bd=4)
    namelabel.place(x=670, y=140)
    namelabel1 = StringVar()
    srno50 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=namelabel1)
    srno50.place(x=800, y=140)

    hallname1 = Label(frame6, text="HALLNAME", width=10, font=12, relief=RIDGE, bd=4)
    hallname1.place(x=670, y=180)
    hallname12 = StringVar()
    srno2 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=hallname12)
    srno2.place(x=800, y=180)

    datee = Label(frame6, text="DATE", width=10, font=7, relief=RIDGE, bd=4)
    datee.place(x=670, y=220)
    datee5 = StringVar()
    datee1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=datee5)
    datee1.place(x=800, y=220)

    BOOKEDBY = Label(frame6, text="BILLED BY", width=10, font=7, relief=RIDGE, bd=4)
    BOOKEDBY.place(x=670, y=260)
    BOOKEDBY5 = StringVar()
    BOOKEDBY1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=BOOKEDBY5)
    BOOKEDBY1.place(x=800, y=260)

    contact = Label(frame6, text='PHONE NO', width=10, font=5, relief=RIDGE, bd=4)
    contact.place(x=670, y=300)
    contact5 = StringVar()
    contact1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=contact5)
    contact1.place(x=800, y=300)

    days = Label(frame6, text='DAYS', width=10, font=5, relief=RIDGE, bd=4)
    days.place(x=670, y=340)
    days5 = StringVar()
    days1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=days5)
    days1.place(x=800, y=340)

    ammount = Label(frame6, text='AMMOUNT', width=10, font=5, relief=RIDGE, bd=4)
    ammount.place(x=670, y=380)
    ammount5 = StringVar()
    ammount1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=ammount5)
    ammount1.place(x=800, y=380)

    address = Label(frame6, text='ADDRESS', width=10, font=5, relief=RIDGE, bd=4)
    address.place(x=670, y=420)
    address5 = StringVar()
    address1 = Entry(frame6, font=('arial', 12, 'bold'), bd=6, width=15, justify='left', textvariable=address5)
    address1.place(x=800, y=420)

    def booked():
        if srno22.get() == "" or namelabel1.get() == "" or hallname12.get() == "" or datee5.get() == "" or BOOKEDBY5.get() == "" or contact5.get() == "" \
                or days5.get() == "" or ammount5.get() == "" or address5.get() == "":
            messagebox.showerror("System", "Please enter all details")
        else:
            sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
            cur = sqlcon.cursor()
            cur.execute("INSERT INTO displaytable VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            srno22.get(),
                            namelabel1.get(),
                            hallname12.get(),
                            datee5.get(),
                            BOOKEDBY5.get(),
                            contact5.get(),
                            days5.get(),
                            ammount5.get(),
                            address5.get()
                        ))
            sqlcon.commit()
            sqlcon.close()
            messagebox.showinfo("System", "Booked Successfully")

    booked = Button(frame6, text="BOOK", relief=tk.RAISED, command=booked, width=11, height=2, bd=6)
    booked.place(x=800, y=460)

    def Logout1():
        root.quit()

    Logout = Button(frame2, text="LOGOUT", relief=tk.RAISED, command=Logout1, width=11, height=2, bd=6)
    Logout.place(x=890, y=540)
    Logout = Button(frame6, text="LOGOUT", relief=tk.RAISED, command=Logout1, width=11, height=2, bd=6)
    Logout.place(x=890, y=540)
    frame1.destroy()
    frame2.place_slaves()
    back2 = Button(frame6, text="BACK", relief=tk.RAISED, command=backu, width=11, height=2, bd=6)
    back2.place(x=780, y=540)

back2 = Button(frame6, text="BACK", relief=tk.RAISED, command=backu, width=11, height=2, bd=6)
back2.place(x=780, y=540)

root.mainloop()
