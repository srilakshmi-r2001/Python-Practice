class palindrome:
    def checkPal(self, x):
        return x[::-1]
num=input("Enter a number:")
pal=palindrome()
check=pal.checkPal(num)
if(check==num):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")