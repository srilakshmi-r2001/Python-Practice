n=5
print("* " *((int(n/2))+1))
for i in range(n-2):
    print("*",end="")
    print(" " *(n-2),end="")
    print("*")
print("* " *((int(n/2))+1))