class Person:
    def Hello(self, name=None, age=None):
        if(name!=None and age!=None):
            print("Hello",name," aged:",age)
        elif(name!=None and age==None):
            print("Hello",name)
        else:
            print("Hello")

per=Person()
per.Hello()
per.Hello("Sri")
per.Hello("Sri",22)