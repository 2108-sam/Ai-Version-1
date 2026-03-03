Operand1=int(input("Enter your first operand: "))
Operand2=int(input("Enter the second operand: "))

print("""
\n1\tAddition
\n2\tSubtraction
\n3\tMultiplication
\n4\tDivision
\n5\tFloat division
\n6\tRemainder
""")
selection=int(input("Enter your selection: "))

if selection==1:
    sum=Operand1 + Operand2
    print(f"{Operand1} + {Operand2} = {sum}")
elif selection==2:
    diff= Operand1 - Operand2
    print(f"{Operand1} - {Operand2} = {sum}")
elif selection==3:
    mult= Operand1 * Operand2
    print(f"{Operand1} * {Operand2} = {mult}")
elif selection==4:
    Div=Operand1//Operand2
    print(f"{Operand1} / {Operand2}= {Div}")
elif selection==5:
    floatdiv=Operand1 / Operand2
    print(f"{Operand1} / {Operand2} = {floatdiv}")
else:
    Rem= Operand1%Operand2
    print(f"{Operand1} % {Operand2} = {Rem}")