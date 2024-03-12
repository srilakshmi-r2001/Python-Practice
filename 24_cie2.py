l1=["M","na","i","Ke"]
l2=["y","me","s","lly"]
t=1
while(t):
    print("1.concat\n2.Add\n3.extend\n4.replace\n0.exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        print(l1+l2)
    elif(ch==2):
        n=int(input("Enter the index value:"))
        l1.insert(n,"NEW")
        print(l1)
    elif(ch==3):
        l3=["new","list"]
        l1.extend(l3)
        print(l1)
    elif(ch==4):
        old=input("Enter the value you want to replace")
        new=input("Enter the new value:")
        if old in l1:
            i=l1.index(old)
            l1.remove(old)
            l1[i]=new
            print(l1)
    elif(ch==0):
        t=0
    else:
        print("invalid")