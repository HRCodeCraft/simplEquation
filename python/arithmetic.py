#arithmetic calculation on the user input

def switch( ):
    a=int(input("enter first value:" ))
    b=int(input("enter second value: "))
    print("press 1 for addition\n press 2 for subtraction\n press 3 for multiplication\n press 4 for divison\n press 5 for modulus\n press 6 for exponential\n press 7 for floor divison")
    
    choice=int(input("enter your option: "))
    if choice == 1:
        result=a+b
        print("Addition: ", result)

    elif choice ==2:
        result=a-b
        print("Subtraction: ",result)

    elif choice ==3:
        result=a*b
        print("Multiplication: ",result)

    elif choice==4:
        result=a/b
        print("Division: ",result)

    elif choice ==5:
        result=a%b
        print("Modulus: ",result)

    elif choice ==6:
        result=a**b
        print("Expontiall: ",result)

    elif choice ==7:
        result=a//b
        print("Floor Division: ",result)

    else:
        print("Invalid Value")


switch()