# ATTRIBUTES in Python

# class apple:
#     a=10
#     def funk(self,new_x):
#         self.a=new_x
# print(apple.a)
#
# obj=apple()
# print(obj.a)
#
# obj.funk(100)
# print(obj.a)



# class empl:
#     def __init__(self,first,last,sal):
#         self.fname=first
#         self.lname=last
#         self.salary=sal
#         self.email=first + "." + last + "@apple.com"
#
#     def display(self):
#         print("First name is :-"+ self.fname)
#         print("last name is :-" + self.lname)
#         print("salary is :-", self.salary)
#         print("Email is :-" + self.email)
#
# # emp1=empl('amir','hamza',2500000)
# # print(emp1.email)
# # print(emp1.fname,emp1.salary)
#
# emp1=empl("amir","hamza",3000000)
# print(emp1.email)
#
# print("\n")
#
# g=getattr(emp1,"fname")
# print(g)
#
# print("\n")
#
# h=hasattr(emp1,"salary")
# print(h)
#
# print("\n")
# print(emp1.salary)
# setattr(emp1,"fname","guha")
# print(emp1.salary)
#
# print("\n")
#
# delattr(emp1,"lname")
#
#
# h=hasattr(emp1,"lname")
# print(h)
#
# print("\n")
#
# print(emp1.fname)
# print(emp1.lname)
# print(emp1.salary)
# print(emp1.email)
#
# print("\n")
#
# print(emp1.display())