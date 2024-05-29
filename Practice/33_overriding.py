"""class A:
    def Hello(self):
        print("Hello A")

class B(A):
    def Hello(self):
        print("Hello B")

#objA=A()
objB=B()
objB.Hello()"""

class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,emp_id,pay):
        self.first=first
        self.last=last
        self.emp_id=emp_id
        self.pay=pay

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

    def display(self):
        print("Name:",self.first,self.last)
        print("Employee ID",self.emp_id)
        print("Wage:",self.pay)

class Dev(Employee):
    raise_amt=1.05

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class Mgr(Employee):
    raise_amt=1.06

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

emp1=Mgr("John","Doe",90,120000)
emp2=Dev("David","Rose",74,100000)

print("Initial Wages:\n",emp1.pay)
print(" ",emp2.pay,"\n")

emp1.apply_raise()
emp2.apply_raise()

emp1.display()
print("\n")
emp2.display()