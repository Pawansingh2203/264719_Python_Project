def pythoncalculator():
    choice = input("Enter your choice:")  # User's choice[1,2,3,4]
    if (True):
        print("Enter two numbers: ")
        num1 = int(input())
        num2 = int(input())

        if choice == '+': # To add two numbers
            res = num1 + num2
            print("Result = num1 choice num2 =" , res)

        elif choice == '-': # To subtract two numbers
            res = num1 - num2
            print("Result = num1 choice num2 =" , res)

        elif choice == '*': # To multiply two numbers
            res = num1 * num2
            print("Result = num1 * num2 =" , res)

        elif choice == '/': # To get quotient with decimal value
            res = num1 / num2
            print("Result = num1 / num2 = " , res)

        elif choice == 'exit':\
                exit()
    else:
        print("Wrong input..!!")