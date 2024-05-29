print("PERFORMING LIST AND SET OPERATIONS")
L1=[1,"a",2+3j,True,3.4]
L2=[]
S1={1,2,2,3,3,4,7}
S2={'a',2+3j,True,3.14}
size=int(input("Enter the size of the second list:"))
for i in range(0,size):
    ele=int(input("Enter the integer element:"))
    L2.append(ele)
print("The first list containing different type elements is",L1)
print("The list you have created is",L2,"\n \n")
print(".................................................................................")
t=1
while(t):
    ch=int(input("To perform list operations, enter 1 \n To perform set operations, enter 2 \n To exit, enter 3"))
    if(ch==1):
        print("LIST OPERATIONS")
        b=1
        while(b):
            choice=int(input("1.Length \n 2.Concatenation \n 3.Reverse \n 4.Copy \n 5.Append operator \n 6.Sort \n 7.Sum of elements \n 8.Extend operator \n 9.Clear \n 10.Delete \n 0.Exit"))
            if(choice==1):
                print(len(L1))
            elif(choice==2):
                print(L1+L2)
            elif(choice==3):
                L1.reverse()
                print(L1)
            elif(choice==4):
                L3=L1.copy()
                print("original=",L1,";","copy=",L3)
            elif(choice==5):
                L1.append(5)
                print(L1)
            elif(choice==6):
                print(L1.sort())
            elif(choice==7):
                print(sum(L1))
            elif(choice==8):
                L1.extend(1,2,4)
                print(L1)
            elif(choice==9):
                L1.clear()
                print(L1)
            elif(choice==10):
                del L1
                print(L1)
            elif(choice==0):
                b=0
            else:
                print("invalid choice")
    elif(ch==2):
        print("SET OPERATIONS")
        print("1.Union \n 2.Intersection \n 3.Symmetric Difference \n 4.Subset \n 5.Superset \n 6.Membership Operator \n 7.Remove \n 8.Pop operator \n 9.Clear \n 10.Delete \n 0.Exit")
        ch1=int(input("Enter your choice:"))
        c=1
        while(c):
            if(ch1==1):
                print(S1.union(S2))
            elif(ch1==2):
                print(S1.intersection(S2))
            elif(ch1==3):
                print(S1.symmetric_difference(S2))
            elif(ch1==4):
                print(S1.issubset(S2))
            elif(ch1==5):
                print(S1.issuperset(S2))
            elif(ch1==6):
                print('a' in S2)
            elif(ch1==7):
                S1.remove(2)
                print(S2)
            elif(ch1==8):
                S2.pop()
                print(S2)
            elif(ch1==9):
                S1.clear()
                print(S1)
            elif(ch1==10):
                for i in S2:
                    print(i)
            elif(ch1==0):
                b=0
    else:
        print("Invalid choice")