d=dict()
class student:
    def Input(self):
        self.name=input("Enter the name of the employee:")
        self.age=int(input("Enter the age:"))
        self.basic=int(input("Enter the basic salary:"))
        self.da=self.basic*0.25
        self.hra=self.basic*0.10
        self.net=self.basic+self.da+self.hra
        self.ded=self.net*0.2
        d.update({self.name:{"Name":self.name,"Age":self.age,"Basic salary":self.basic,"HRA":self.hra,"DA":self.da,"Net Salary":self.net,"Deductions":self.ded}})
    
    def display(self):
        for i in d:
            print(i,d[i])

    def search(self,name):
        found=False
        for i in d.values():
            if(name==i["Name"]):
                print(i)
                found=True
        if(found==False):
            print("Enter a valid name")
        
std=student()
t=1
while(t):
    print("1.Input \n2.Display \n3.Search")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        std.Input()
    elif(ch==2):
        std.display()
    elif(ch==3):
        name=input("Enter the name:")
        std.search(name)
    else:
        t=0
print("Execution complete")