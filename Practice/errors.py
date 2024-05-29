while True:
    print("Error and Exception Handling\n")
    print("1.Type Error\n2.Name Error\n3.IO Error\n4.Value Error\n5.File Not Found Error\n0.Exit\n")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        try:
            f = open('file.txt', 'r', 'w')
            print("Successful")
        except TypeError:
            print("Type Error Encountered")

    elif choice == 2:
        try:
            f = open('file.txt', 'r')
            print(f1)
        except NameError:
            print("Name error, there's an undefined variable")

    elif choice == 3:
        try:
            f = open('file.txt', 'w+')
            f.write("example")
            f1 = open('file1.txt', 'r')
            print("Successful")
        except IOError:
            print("Input Output Error")

    elif choice == 4:
        try:
            f = open('file.txt', 'z')
        except ValueError:
            print("Value Error Encountered")
    
    elif choice == 5:
        try:
            f = open('file9.txt', 'r')
        except FileNotFoundError:
            print("The specified file does not exist")

    elif choice == 0:
        break
print("Execution complete")