balance=0
password= "Kate100"
while True:
    check=input("Enter your password: ")
    if password==check:
        print("Password correct\n")
        break
    else:
        print("Invalid password. Try again.\n")
while True:
    print(balance)
    print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
""")

    selection = input("Enter your selection: ")

    if selection == "1":
        deposit = float(input("Enter amount to deposit: "))
        balance += deposit
        print(f"Deposit successful. New balance: {balance}\n")
    elif selection == "2":
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw > balance:
            print("Insufficient balance.\n")
        else:
            balance -= withdraw
            print(f"Withdrawal successful. New balance: {balance}\n")

    elif selection == "3":
        print(f"Your balance is: {balance}\n")

    elif selection == "4":
        print("Thank you for visiting.")
        break

    else:
        print("Invalid selection. Try again.\n")