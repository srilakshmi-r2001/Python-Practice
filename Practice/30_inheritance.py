class Student:
    def __init__(self,name,USN,Age):
        self.name=name
        self.USN=USN
        self.Age=Age 

    def getData(self):
        self.name=input("Enter name:")
        self.USN=input("Enter USN:")
        self.age=int(input("Enter age:"))

    def display(self):
        print("Name:",self.name)
        print("USN:",self.USN)
        print("Age:",self.age)

class pgstudent(Student):
    def __init__(self,fees,sem,stipend):
        super().__init__(name="",USN="",Age=0)
        self.fees=fees
        self.sem=sem
        self.stipend=stipend

    def getData(self):
        super().getData()
        self.fees=int(input("Enter fees:"))
        self.sem=int(input("Enter semester:"))
        self.stipend=int(input("Enter stipend:"))

    def display(self):
        super().display()
        print("Sem:",self.sem)
        print("Fees paid:",self.fees)
        print("Stipend:",self.stipend)

class ugstudent(Student):
    def __init__(self,fees,sem,stipend):
        super().__init__(name="",USN="",Age=0)
        self.fees=fees
        self.sem=sem
        self.stipend=stipend

    def getData(self):
        super().getData()
        self.fees=int(input("Enter fees:"))
        self.sem=int(input("Enter semester:"))
        self.stipend=int(input("Enter stipend:"))

    def display(self):
        super().display()
        print("Sem:",self.sem)
        print("Fees paid:",self.fees)
        print("Stipend:",self.stipend)

pg=pgstudent(fees=0,sem=0,stipend=0)
ug=ugstudent(fees=0,sem=0,stipend=0)
t=1
while(t):
    print("1.PG Student\n2.UG Student")
    chmain=int(input("Enter choice:"))
    if(chmain==1):
        print("1.Input\n2.Display\n")
        ch=int(input("Enter choice:"))
        if(ch==1):
            pg.getData()
        elif(ch==2):
            pg.display()
        else:
            t=0
    elif(chmain==2):
        print("1.Input\n2.Display\n")
        ch=int(input("Enter choice:"))
        if(ch==1):
            ug.getData()
        elif(ch==2):
            ug.display()
        else:
            t=0
    else:
        t=0