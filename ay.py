def success():
    while True:
        print("______________________________")
        print("****************MAIN MENU****************")
        print("1.Add Students Record")
        print("2.Display Students Record")
        print("3.Search Students Record")
        print("4.Delete Students Record")
        print("5.Update Students Record")
        print("6.Add Class Attendance record")
        print("7.Display attendance record")
        print("_____________________________")

        a = int(input("Enter your choice:-"))
        if (a == 1):
            print("______________________")
            print("*******ENTER DETAILS OF STUDENT********")
            print("_______________________")
            R = input("Enter rollno:")
            N = input("Enter name:")
            F = input("Enter class:")
            D = input("Enter fee=")
            d = (R, N, F, D)
            mycursor = mydatabase.cursor()
            sql = "insert into students values(%s,%s,%s,%s)"
            mycursor.execute(sql, d)
            mydatabase.commit()
            print("\t\t\t\tInformation Saved")
        elif (a == 2):
            mycursor = mydatabase.cursor()
            mycursor.execute("select* from students")
            myresult = mycursor.fetchall()
            t = PrettyTable(['rollno', 'name', 'class', 'fee'])
            for rollno, name, cls, fee in myresult:
                t.add_row([rollno, name, cls, fee])
            print(t)
        elif (a == 3):
            print("___________________")
            print("*******SEARCH STUDENT*********")
            print("___________________")
            r_1 = input("Enter student rollno:")
            mycursor = mydatabase.cursor()
            mycursor.execute("select*from students where rollno=" + r_1)
            myresult = mycursor.fetchall()
            t = PrettyTable(['Rollno', 'Name', 'Class', 'Fees'])
            for Rollno, name, cls, fee in myresult:
                t.add_row([Rollno, name, cls, fee])
            print(t)
        elif (a == 4):
            print("______________________")
            print("**********Delete Record by RollNO*******")
            print("_____________________")
            r_1 = input("Enter student rollno whose information you want to delete=")
            mycursor = mydatabase.cursor()
            mycursor.execute("delete from students where rollno=" + r_1)
            mydatabase.commit()
            print("\t\t\t\tRecord Deleted Successfully!!!")
            print("______________________")
        elif (a == 5):
            r_1 = input("enter student rollno whose fees you want to update=")
            Newfees = input("Enter new fees:")
            mycursor = mydatabase.cursor()
            mycursor.execute("Update students set fee=" + Newfees + ' where rollno=' + r_1 + ';')
            mydatabase.commit()
            mycursor.execute("select* from students where rollno=" + str(r_1))
            myresult = mycursor.fetchall()
            t = PrettyTable(['rollno', 'name', 'class', 'fee'])
            for rollno, name, cls, fee in myresult:
                t.add_row([rollno, name, cls, fee])
        elif (a == 6):
            cls = input("Enter class:")
            clt = input("Enter class teacher:")
            s = input("Strength of the class:")
            ab = input("enter number of student absent:")
            dt = input("Enter Date:")
            d = (cls, clt, s, ab, dt)
            mycursor = mydatabase.cursor()
            sql = "insert into attendance values(%s,%s,%s,%s,%s)"
            mycursor.execute(sql, d)
            mydatabase.commit()
            print("Data entered succesfully")
        elif (a == 7):
            sql = 'select*from attendance'
            mycursor = mydatabase.cursor()
            mycursor.execute(sql)
            d = mycursor.fetchall()
            for i in d:
                print("class:", i[0])
                print("class teacher:", i[1])
                print("present:", i[2])
                print("absent:", i[3])
                print("Date:", i[4])

                print(" ")
            print(" ")

        else:
            exit()


from prettytable import PrettyTable
import mysql.connector

mydatabase = mysql.connector.connect(host='localhost', user='root', password='root',database="mydatabase")
mycursor = mydatabase.cursor()
# mycursor.execute("use studentrecord")
mycursor.execute("create table if not exists attendance(class varchar(20),class_teacher varchar(20),present int(25),absentees int(25),date_ varchar(20))")
success()


# from prettytable import PrettyTable
# import mysql.connector
#
# mydatabase = mysql.connector.connect(host='localhost', user='root', password='root',database="mydatabase")
# mycursor = mydatabase.cursor()
#
# mycursor.execute("create table if not exists students(rollno int, name varchar(20),class varchar(5),absents_stu int)")
#
#
# def success():
#     while True:
#         print("______________________________")
#         print("****************MAIN MENU****************")
#         print("1.Add Students Record")
#         print("2.Display Students Record")
#         print("3.Search Students Record")
#         print("4.Delete Students Record")
#         print("5.Update Students Record")
#         print("6.Add Class attendance record")
#         print("_____________________________")
#
#         a = int(input("Enter your choice;-"))
#         if (a == 1):
#             print("______________________")
#             print("*******ENTER DETAILS OF STUDENT********")
#             print("_______________________")
#             R = input("Enter rollno:")
#             N = input("Enter name:")
#             F = input("Enter class:")
#             D = input("Enter fee=")
#             mycursor = mydatabase.cursor()
#             d=(R,N,F,D)
#             sql = "insert into students values(%s,%s,%s,%s)"
#             mycursor.execute(sql,d)
#             mydatabase.commit()
#             print("\t\t\t\tInformation Saved")
#         elif (a == 2):
#             mycursor = mydatabase.cursor()
#             mycursor.execute("select* from students")
#             myresult = mycursor.fetchall()
#             t = PrettyTable(['rollno', 'name', 'class', 'fee'])
#             for rollno, name, cls, fee in myresult:
#                 t.add_row([rollno, name, cls, fee])
#             print(t)
#         elif (a == 3):
#             print("___________________")
#             print("*******SEARCH STUDENT*********")
#             print("___________________")
#             r_1 = input("Enter student rollno:")
#             mycursor = mydatabase.cursor()
#             mycursor.execute("select*from students where rollno=" + r_1)
#             myresult = mycursor.fetchall()
#             t = PrettyTable(['Rollno', 'Name', 'Class', 'Fees'])
#             for Rollno, name, cls, fee in myresult:
#                 t.add_row([Rollno, name, cls, fee])
#             print(t)
#         elif (a == 4):
#             print("______________________")
#             print("**********Delete Record by RollNO*******")
#             print("_____________________")
#             r_1 = input("Enter student rollno whose information you want to delete=")
#             mycursor = mydatabase.cursor()
#             mycursor.execute("delete from students where rollno=" + r_1)
#             mydatabase.commit()
#             print("\t\t\t\tRecord Deleted Successfully!!!")
#             print("______________________")
#         elif (a == 5):
#             r_1 = input("enter student rollno whose fees you want to update=")
#             Newfees = input("Enter new fees:")
#             mycursor = mydatabase.cursor()
#             mycursor.execute("Update students set fee=" + Newfees + ' where rollno=' + r_1 + ';')
#             mydatabase.commit()
#             mycursor.execute("select* from students where rollno=" + str(r_1))
#             myresult = mycursor.fetchall()
#             t = PrettyTable(['rollno', 'name', 'class', 'fee'])
#             for rollno, name, cls, fee in myresult:
#                 t.add_row([rollno, name, cls, fee])
#         elif (a == 6):
#             cls = input("Enter class:")
#             clt = input("Enter class teacher:")
#             s = input("Strength of the class:")
#             ab = input("enter number of absentees:")
#             d = (cls, clt, s, ab)
#             sql = "insert into students values(%s,%s,%s,%s)"
#             mycursor = mydatabase.cursor()
#             mycursor.execute(sql, d)
#             mydatabase.commit()
#             print("Data entered succesfully")
#
#         else:
#             exit()
#
# success()

































# def binary_search(a,size,key):
#     global pos
#     i=0
#     j=size-1
#     flag=0
#     while i <= j and flag == 0:
#         mid = (i + j) // 2
#         if a[mid] == key:
#             pos= mid + 1
#             flag = 1
#         if a[mid] < key:
#             i = mid - 1
#         if a[mid] > key:
#             j = mid + 1
#     if flag == 1:
#          print("Search successful:- at position ",pos)
#     else:
#          print("Unsuccessful search")
#
# a=[]
# size=int(input("nos. to be entered:-"))
# for i in range(size):
#     var=int(input("num:- "))
#     a.append(var)
# print(a)
# key=int(input("enter the num. to be search:- "))
# binary_search(a,size,key)
# #
# def insertfunk(a,size,key):
#     a.append(None)
#     i=size-1
#     while i>=0 and a[i]>key:
#         a[i+1]=a[i]
#         i=i-1
#     a[i+1]=key
#     print("list after adding element",a)
#
# a=[]
# size=int(input("No. of Inputs:-"))
# for i in range(size):
#     val=int(input("Enter no:-"))
#     a.append(val)
# key=int(input("Enter element to insert:-"))
# insertfunk(a,size,key)
#
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else :
#         print(n)
#         return n*(fact(n-1))
#
# print(fact(5))
#
# def fibo(n):
#     if n==0 or n==1:
#         return 1
#     else :
#         return fibo(n-1)+fibo(n-2)
# print(fibo(5))
#
# def doublesize(arr,num):
#     for i in arr:
#         print(arr,num)
#         if i==num:
#             num=num*2
#             print(num)
# arr=[1,2,4,11,12,8]
# num=2
# doublesize(arr,num)



# a=[]
# num=int(input("Numbers to be entered:-"))
# for i in range(num):
#     n=int(input(""))
#     a.append(n)
#
# small = a[0]
# for n in range(num):
#     if a[n]<small:
#         print(small)
#         small=a[n]
# # print(a)
# print(small)

# an=[]
# z=int(input('no'))
# for ab in range(z):
#     abn=int(input("list"))
#     an.append(abn)
# print(an)
#
# j=an[0]
# jc=an[4]
# for x in an:
#     jc-=1
#     if x>an[jc]:
#         an.remove(an[j])
#         an.remove(an[j+1])
#     else :
#         an.remove(an[jc])
#         an.remove(an[jc-2])






# for ab in range(a):
#     abn=int(input("list"))
#     cd.append(abn)
# i=cd
# if i[0]>i[1]:
#     z.append(1)
# else:
#     z.append(0)
# if i[1]>i[2]:
#     z.append(1)
# else:
#     z.append(0)
# if i[2]>i[-1]:
#     z.append(1)
# else:
#     z.append(0)
# print(z)