num=int(input("Enter a number:"))
num1=num
rem=0
sum=0
t=1
while(t):
    if(num<10):
        sum=sum+num
        t=0
    else:
        rem=num%10
        sum=sum+rem
        num=num-rem
        num=num/10
print("Sum of the digits of",num1,"is",sum)