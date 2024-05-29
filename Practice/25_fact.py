def fact(a):
    sum=1
    while(a!=0):
        sum=sum*a
        a=a-1
    return sum
def oddeve(a):
    if(a%2==0):
        print("The number is even")
    else:
        print("The number is odd")

num=int(input("Enter a number:"))
t=1
while(t):
    print("1. Factorial \n 2. Odd or even \n 0.Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        sum=fact(num)
        print("Factorial of ",num,"is",sum)
    elif(ch==2):
        oddeve(num)
    elif(ch==0):
        t=0
    else:
        print("Invalid choice")
print("Execution complete")