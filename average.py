while True:
    Name=input("Enter your name: ")
    print("SUBJECT:\t\tMark")
    eng=int(input("English:\t\t"))
    kis=int(input("Kiswahili:\t\t"))
    bio=int(input("Biology:\t\t"))
    chem=int(input("CHEMISTRY:\t\t"))
    math=int(input("Mathematics:\t"))

    average=(eng+kis+bio+chem+math)/5
    print(f"Dear {Name} your average score is {average:.2f}")