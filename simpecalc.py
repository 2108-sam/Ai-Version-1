while True:
    x=input("Enter the operand 1: ")
    y=input("Enter the operand 2: ")
    print("""
    \n1.\tAddition.
    \n2.\tSubtraction.
    \n3.\tDivision.
    \n4.\tMultiplication.
    \n5.\tModulus.
    \n6.\tExit.
    """)
    selection=input("Select your Operator: ")

    if selection=="1":
        sum=x+y
        print(f"{x} + {y} = {sum}")
    elif selection=="2":
        sub= x- y
        print(f"{x} - {y} = {sub}")
    elif selection=="3":
        div= x/y
        print(f"{x} / {y} = {div}")
    elif selection=="4":
        mul=x*y
        print(f"{x} x {y} = {mul}")
    elif selection == "5":
        mod=x%y
        print(f"{x} % {y} = {mod}")
    else:
        print("Invalid Entry.")