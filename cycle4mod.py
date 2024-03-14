class operover:
    def __init__(self):
        self.list=[]
    
    def getelement(self):
        size=int(input("Enter the size of the list:"))
        for i in range(size):
            ele=int(input("Enter the element:"))
            self.list.append(ele)

    def display(self):
        print(self.list)

    def __add__(self,other):
        newlist=[]
        for i in range(len(self.list)):
            ele=self.list[i]+other.list[i]
            newlist.append(ele)
        return newlist
    
    def __sub__(self,other):
        newlist=[]
        for i in range(len(self.list)):
            ele=self.list[i]-other.list[i]
            newlist.append(ele)
        return newlist
    
    def __mul__(self,other):
        newlist=[]
        for i in range(len(self.list)):
            ele=self.list[i]*other.list[i]
            newlist.append(ele)
        return newlist
    
    def __floordiv__(self,other):
        newlist=[]
        for i in range(len(self.list)):
            ele=self.list[i]//other.list[i]
            newlist.append(ele)
        return newlist
    
    def __mod__(self,other):
        newlist=[]
        for i in range(len(self.list)):
            ele=self.list[i]%other.list[i]
            newlist.append(ele)
        return newlist
    
    def __pow__(self,other):
        newlist=[]
        for i in range(len(self.list)):
            ele=self.list[i]**other.list[i]
            newlist.append(ele)
        return newlist 