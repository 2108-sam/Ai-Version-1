class BankAccount:
    def __init__(self, username, password, balance=0.0):
        self.username = username
        self.__password = password      # encapsulated (private)
        self.__balance = balance        # encapsulated (private)

    # ---- Authentication ----
    def check_password(self, password):
        return self.__password == password

    # ---- Banking Operations ----
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposit successful. New balance: {self.__balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient balance."
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            self.__balance -= amount
            return f"Withdrawal successful. New balance: {self.__balance}"

    def get_balance(self):
        return self.__balance


# ---------------- MAIN PROGRAM ----------------

# Create users
accounts = {
    "Jack": BankAccount("Jack", "prey", 144.0),
    "Alice": BankAccount("Alice", "123", 200.0),
    "Bob": BankAccount("Bob", "abc", 50.0)
}

print("Welcome to the OOP ATM System\n")

# -------- Login --------
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in accounts and accounts[username].check_password(password):
        print(f"Welcome, {username}!\n")
        current_account = accounts[username]
        break
    else:
        print("Incorrect credentials. Try again.\n")


# -------- ATM Menu --------
while True:
    print("""
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
""")

    choice = input("Select option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        print(current_account.deposit(amount), "\n")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        print(current_account.withdraw(amount), "\n")

    elif choice == "3":
        print(f"Your balance is: {current_account.get_balance()}\n")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid selection.\n")