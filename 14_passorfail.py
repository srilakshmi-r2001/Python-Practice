m1=int(input("Enter the marks scored in LSS:"))
m2=int(input("Enter the marks scored in WAP:"))
m3=int(input("Enter the marks scored in CN:"))
tot=((m1+m2+m3)/150)*(100)
if(tot>=40):
    if((m1/50)*100>=33 and (m2/50)*100>=33 and (m3/50)*100>=33):
        print("You have passed!")
else:
    print("You have failed :(")