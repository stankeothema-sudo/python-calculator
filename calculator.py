while True:
    print("Welcome to our basic calculator 🙌😁\n ")
    print("press q to quit")
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number:"))
    print("\n")
    print("=================================================")
    # an operatin to select ofperation of choice

    print("Select + for addition")
    print("Select - for subtaction")
    print("Select * for multiplication")
    print("Select / for division\n")
    print("")
    print("=================================================")



    choice = input("Choose the operator (+, -, *, /): ")

    # validate

    if choice=="+":
        print(num1 + num2)

    elif choice=="-":
        print(num1 - num2)

    elif choice=="*":
        print(num1 * num2)

    elif choice=="/":
        print(num1/num2)
    elif choice.lower=='q':
        break
    else:
        print("invalid operator selected")
        break