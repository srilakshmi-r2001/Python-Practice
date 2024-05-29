import os

with open("practice.txt","w+") as f:
    f.write("Hi everyone \n we are learning File I/O \nusing Java.\nI like programming in Java")
    data = f.read()

newdata = data.replace("Java","Python")
print(newdata)