username=input("Enter a username:")
t=1
while(t):
    if(len(username)>10):
        print("Username contains more than 10 characters")
        username=input("Enter a username:")
    else:
        print("Valid username")
        t=0
