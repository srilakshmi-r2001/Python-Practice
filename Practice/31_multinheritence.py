class Student:
    def __init__(self,name,age,USN):
        self.name=name
        self.age=age
        self.USN=USN

    def getData(self):
        self.name=input("Enter name:")
        self.USN=input("Enter USN:")
        self.age=int(input("Enter age:"))

class stud(Student):
    def __init__(self,sub1,sub2,sub3,sub4,sub5):
        super().__init__(name="",age=0,USN="")
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        self.sub4=sub4
        self.sub5=sub5

    def marksInput(self):
        super().getData()
        self.sub1=int(input("Enter marks of subject 1:"))
        self.sub2=int(input("Enter marks of subject 2:"))
        self.sub3=int(input("Enter marks of subject 3:"))
        self.sub4=int(input("Enter marks of subject 4:"))
        self.sub5=int(input("Enter marks of subject 5:"))

class study(stud):
    def display(self):
        print(self.name)
        print(self.age)
        print(self.USN)
        print(self.sub1)
        print(self.sub2)
        print(self.sub3)
        print(self.sub4)
        print(self.sub5)

student=study(sub1=0,sub2=0,sub3=0,sub4=0,sub5=0)
student.marksInput()
student.display()