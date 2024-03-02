L1=[]
size=int(input("Enter the size of the list:"))
for i in range(0,size):
    ele=int(input("Enter the element you want to add:"))
    L1.append(ele)
print("The list you've created is",L1)
R1=[]
for i in L1:
    if i not in R1:
       R1.append(i)
print("The list after removal of duplicate elements is:",R1)