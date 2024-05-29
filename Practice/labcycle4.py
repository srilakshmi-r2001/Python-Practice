import cycle4mod as mod
L1=mod.operover()
L2=mod.operover()
L1.getelement()
L2.getelement()
t=1
while(t):
    print("1.Add \n2.Sub \n3.Product \n4.Floor Division \n5.Modular division\n6.Power\n0.Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        print("Addition:")
        print(L1+L2)
    elif(ch==2):
        print("Subtraction:")
        print(L1-L2)
    elif(ch==3):
        print("Multiplication:")
        print(L1*L2)
    elif(ch==4):
        print("Division:")
        print(L1//L2)
    elif(ch==5):
        print("Remainder:")
        print(L1%L2)
    elif(ch==6):
        print("Exponent:")
        print(L1**L2)
    elif(ch==0):
        t=0
    else:
        print("Invalid choice")
    