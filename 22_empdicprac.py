d=dict()
class emp:
    def input(self):
        self.name=input("Enter the name of the employee:")
        self.age=int(input("Enter the age:"))
        self.basic=int(input("Enter the basic salary:"))
        self.da=0.25*self.basic
        self.hra=0.1*self.basic
        self.gross=self.basic+self.da+self.hra
        self.ded=0.2*self.basic
        self.net=self.gross-self.ded
        d.update({self.name:{"Name":self.name,"Age":self.age,"Basic salary":self.basic,
                            "DA":self.da,"HRA":self.hra,"Gross Salary":self.gross,
                            "Deductions":self.ded,"Net Salary":self.net}})
    
    def display(self):
        for i in d:
            print(i,d[i])
    
    def search(self,name):
        found=0
        for i in d.values():
            if(name==i["Name"]):
                print(i)
                found=1
                break
        if(found==0):
            print("Enter a valid name")

em=emp()
t=1
while(t):
    print("1.Input\n2.Display\n3.Search\n0.Exit\n")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        em.input()
    elif(ch==2):
        em.display()
    elif(ch==3):
        name=input("Enter the name of the employee:")
        em.search(name)
    elif(ch==0):
        t=0
    else:
        print("invalid choice")
print("EXECUTION COMPLETE")