print("Even number checker" )
while True:
    number = int(input("Enter a number: "))
    x = number % 2
    if x !=0:
        print(f"{number} is an odd number.")
    elif number==0:
        print("Exiting the program")
        break
    else:
        print(f"{number} is an even number")

