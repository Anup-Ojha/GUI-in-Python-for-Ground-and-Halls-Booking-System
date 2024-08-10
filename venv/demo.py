from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector


class ConnectorDB:
   def __init__(self,root):
     self.root=root
     titlespace=""
     self.root.title(182*titlespace +"System software")
     self.root.geometry("800x680+300+0")
     self.root.resizable(width=False,height=False)

     mainframe=Frame(self.root,bd=10,width=770,height=650,relief=RIDGE,bg='cadet blue')
     mainframe.grid()

     titleframe = Frame(mainframe, bd=7, width=776, height=100, relief=RIDGE, bg='cadet blue')
     titleframe.grid(row=0,column=0)

     topframe = Frame(mainframe, bd=5, width=776, height=500, relief=RIDGE, bg='cadet blue')
     topframe.grid(row=1, column=0)

     leftframe = Frame(topframe, bd=5, width=776, height=400, relief=RIDGE)
     leftframe.pack(side=LEFT)
     leftframe1 = Frame(leftframe, bd=5, width=600, height=180, relief=RIDGE)
     leftframe1.pack(side=TOP,padx=0,pady=0)

     rightframe = Frame(topframe, bd=7, width=90, height=300,padx=2,pady=4, relief=RIDGE)
     rightframe.pack(side=RIGHT,fill=BOTH)
     rightframe2 = Frame(rightframe, bd=14, width=90, height=300, relief=RIDGE)
     rightframe2.pack(side=TOP,fill=BOTH)

     # ======================================table treeview======================
     istudid = StringVar()
     iName = StringVar()
     iSurname = StringVar()
     iaddr = StringVar()
     iGender = StringVar()
     iMobile = StringVar()
     student_records = IntVar()
     # ======================================table treeview======================

     # ======================================table treeview======================
     def iExit():
       iExit = tkinter.messagebox.askyesno("System", "Confirm if you want to Exit")
       if iExit > 0:
         root.destroy()
         return

     def Reset():
         self.studid.delete(0,END)
         self.Name.delete(0, END)
         self.Surname.delete(0, END)
         self.addr.delete(0, END)
         self.Gender.set("")
         self.Mobile.delete(0, END)

     def adddata():
         if istudid.get()=="" or iName.get()=="" or iSurname.get()=="" or iaddr.get()=="" or iGender.get()=="" or iMobile.get()=="":
             tkinter.messagebox.showerror("System","Please enter all details")
         else:
           sqlcon = mysql.connector.connect(host="localhost",user="root",password="root",database="mydatabase")
           cur = sqlcon.cursor()
           cur.execute("INSERT INTO trainee VALUES(%s,%s,%s,%s,%s,%s)",(
           istudid.get(),
           iName.get(),
           iSurname.get(),
           iaddr.get(),
           iGender.get(),
           iMobile.get()

           ))
         sqlcon.commit()
         sqlcon.close()
         tkinter.messagebox.showinfo("System", "Enterded details succesfully")

     def displaydata():

         sqlcon = mysql.connector.connect(host="localhost",user="root",password="root",database="mydatabase")
         cur = sqlcon.cursor()
         cur.execute("select * from trainee")
         result=cur.fetchall()
         if len(result)!=0:
             self.student_records.delete(*self.student_records.get_children())
             for row in result:
                self.student_records.insert('',END,values=row)
             sqlcon.commit()
         sqlcon.close()

     def infowall(ew):
         viewinfo=self.student_records.focus()
         learnerdata=self.student_records.item(viewinfo)
         row=learnerdata["values"]
         istudid.set(row[0]),
         iName.set(row[1]),
         iSurname.set(row[2]),
         iaddr.set(row[3]),
         iGender.set(row[4]),
         iMobile.set(row[5])

     def update():
         sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
         cur = sqlcon.cursor()
         cur.execute("update trainee set Name=%s,Surname=%s,address=%s,Gender=%s,Mobile=%s where studid=%s",(

         iName.get(),
         iSurname.get(),
         iaddr.get(),
         iGender.get(),
         iMobile.get(),
         istudid.get()
         ))
         sqlcon.commit()
         displaydata()
         sqlcon.close()
         tkinter.messagebox.showinfo("SYSTEM","Updated Succesfully")

     def Deletedb():
         sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
         cur = sqlcon.cursor()
         sql="delete from trainee where studid=%s"
         val=(self.studid.get(),)
         #cur.execute("delete from trainee where studid=%s",self.studid.get(),) ''''important lernaing nothing happen if we use this kind of thing syntax""""
         cur.execute(sql,val)
         tkinter.messagebox.showinfo("SYSTEM","Deleted Succesfully")
         sqlcon.commit()
         displaydata()
         sqlcon.close()


     def searchdb(studid):

         sqlcon = mysql.connector.connect(host="localhost", user="root", password="root", database="mydatabase")
         cur = sqlcon.cursor()
         cur.execute("SELECT * FROM trainee WHERE studid=studid")
         row=cur.fetchall()
         sqlcon.close()
         return row

     #=======================================================================================
     self.lbltitle=Label(titleframe,font=('arial', 50,'bold'),text="Entry System",bd=7)
     self.lbltitle.grid(row=0,column=0,padx=90)

     self.lblstid = Label(leftframe1, font=('arial', 12, 'bold'), text="STUDENT ID", bd=7)
     self.lblstid.grid(row=1 , column=0, padx=5,sticky=W)
     self.studid =Entry(leftframe1, font=('arial', 12, 'bold') , bd=7,width=44,justify='left',textvariable=istudid)
     self.studid.grid(row=1, column=1, padx=5, sticky=W)

     self.name = Label(leftframe1, font=('arial', 12, 'bold'), text="NAME", bd=7)
     self.name.grid(row=2 , column=0, padx=5,sticky=W)
     self.Name =Entry(leftframe1, font=('arial', 12, 'bold') , bd=7,width=44,justify='left',textvariable=iName)
     self.Name.grid(row=2, column=1, padx=5, sticky=W)

     self.surname = Label(leftframe1, font=('arial', 12, 'bold'), text="SURNAME", bd=7)
     self.surname.grid(row=3, column=0, padx=5, sticky=W)
     self.Surname = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=iSurname)
     self.Surname.grid(row=3, column=1, padx=5, sticky=W)

     self.addres = Label(leftframe1, font=('arial', 12, 'bold'), text="ADDRESS", bd=7)
     self.addres.grid(row=4, column=0, padx=5, sticky=W)
     self.addr = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=iaddr)
     self.addr.grid(row=4, column=1, padx=5, sticky=W)

     self.gender = Label(leftframe1, font=('arial', 12, 'bold'), text="GENDER", bd=7)
     self.gender.grid(row=5, column=0, padx=5, sticky=W)
     self.Gender=ttk.Combobox(leftframe1,font=("arial",12,'bold'),width=43,state='readonly',textvariable=iGender)
     #self.Gender = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left')
     self.Gender ['values']=('','MALE','FEMALE')
     self.Gender.current(0)
     self.Gender.grid(row=5, column=1, padx=5, sticky=W)

     self.mobile = Label(leftframe1, font=('arial', 12, 'bold'), text="Mobile", bd=7)
     self.mobile.grid(row=6, column=0, padx=5, sticky=W)
     self.Mobile = Entry(leftframe1, font=('arial', 12, 'bold'), bd=7, width=44, justify='left',textvariable=iMobile)
     self.Mobile.grid(row=6, column=1, padx=5, sticky=W)

#======================================table treeview=======================================================================================================
     scroll_y=Scrollbar(leftframe,orient=VERTICAL)
     self.student_records=ttk.Treeview(leftframe,height=14,columns=("studid","Name","Surname","Address",
                                        "Gender","Mobile"),yscrollcommand=scroll_y.set)
     scroll_y.pack(side=RIGHT,fill=Y)

     self.student_records.heading("studid",text="Student ID")
     self.student_records.heading("Name", text="Firstname")
     self.student_records.heading("Surname", text="Surname")
     self.student_records.heading("Address", text="Address")
     self.student_records.heading("Gender", text="Gender")
     self.student_records.heading("Mobile", text="Mobile")

     self.student_records ['show']='headings'

     self.student_records.column("studid", width=70)
     self.student_records.column("Name",width=100)
     self.student_records.column("Surname", width=100)
     self.student_records.column("Address", width=100)
     self.student_records.column("Gender", width=70)
     self.student_records.column("Mobile", width=70)

     self.student_records.pack(fill=BOTH,expand=1)
     self.student_records.bind("<ButtonRelease-1>",infowall)
     #displaydata()
#======================================table treeview=======================================================================================================
     self.addbtn=Button(rightframe2,font=('arial',16,'bold'),command=adddata,text="ADD NEW",bd=4,pady=1,padx=24,
                        width=8,height=2).grid(row=0,column=0,padx=1)
     self.displaybtn = Button(rightframe2, font=('arial', 16, 'bold'),command=displaydata, text="DISPLAY", bd=4, pady=1, padx=24,
                          width=8, height=2).grid(row=1, column=0, padx=1)
     self.updatebtn = Button(rightframe2, font=('arial', 16, 'bold'),command=update, text="UPDATE", bd=4, pady=1, padx=24,
                          width=8, height=2).grid(row=2, column=0, padx=1)
     self.deletebtn = Button(rightframe2, font=('arial', 16, 'bold'),command=Deletedb, text="DELETE", bd=4, pady=1, padx=24,
                          width=8, height=2).grid(row=3, column=0, padx=1)
     self.searchbtn = Button(rightframe2, font=('arial', 16, 'bold'),command=searchdb, text="SEARCH", bd=4, pady=1, padx=24,
                           width=8, height=2).grid(row=4, column=0, padx=1)
     self.resetbtn = Button(rightframe2, font=('arial', 16, 'bold'),command=Reset, text="RESET", bd=4, pady=1, padx=24,
                          width=8, height=2).grid(row=5, column=0, padx=1)
     self.exitbtn = Button(rightframe2, font=('arial', 16, 'bold'),command=iExit, text="EXIT", bd=4, pady=1, padx=24,
                          width=8, height=2).grid(row=6, column=0, padx=1)






#======================================table treeview======================

if __name__=='__main__':
  root=Tk()
  application=ConnectorDB(root)
  root.mainloop()



