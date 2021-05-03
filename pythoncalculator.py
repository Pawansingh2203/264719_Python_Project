from calculatorfunc import *


def pythoncalculator():
    while (True):
        choice = input("Enter your choice:")  # User's choice[+,-,*,/,exit]
        if choice == 'exit':
            break
        print("Enter two numbers: ")
        num1 = int(input())
        num2 = int(input())

        if choice == '+': # To add two numbers
            res=add(num1,num2)

            print("Result = num1 + num2 =" , res)

        elif choice == '-': # To subtract two numbers
            res=sub(num1,num2)
            print("Result = num1 - num2 =" , res)

        elif choice == '*': # To multiply two numbers
            res=mult(num1,num2)
            print("Result = num1 * num2 =" , res)

        elif choice == '/': # To get quotient with decimal value
            res= div(num1,num2)
            print("Result = num1 / num2 = " , res)
        else:
            print("Wrong input..!!")
        print("Enter exit to Quit")