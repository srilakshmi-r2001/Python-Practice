L1=[]
size=int(input("Enter the size of the list:"))
for i in range(0,size):
    ele=int(input("Enter the element you want to add:"))
    L1.append(ele)
print("The list you've created is",L1)
for i in L1:
    if(i>0):
        print(i,"is a positive value")