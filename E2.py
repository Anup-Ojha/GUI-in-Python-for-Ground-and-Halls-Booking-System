# Method Overriding

class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay
    def get_pay(self):
        return self.base_pay

class SalesEmployee(Employee):

    def __init__(self, name, base_pay, sales_incentive):
        self.name = name
        self.base_pay = base_pay
        self.sales_incentive = sales_incentive

    def get_pay(self):
     return self.base_pay + self.sales_incentive

kate = SalesEmployee("kate jeniffer",2000,6000)
print(kate.get_pay())
print(kate.name)
print(kate.sales_incentive)

fate= Employee("kate",5000)
print(fate.get_pay())