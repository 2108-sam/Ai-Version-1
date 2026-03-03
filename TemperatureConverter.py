while True:
    print("""
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
""")

    choice = input("Select option: ")

    if choice == "1":
        response = float(input("Enter temperature in Celsius: "))
        temp = (9/5 * response) + 32
        print(f"{response}°C is {temp}°F\n")

    elif choice == "2":
        response = float(input("Enter temperature in Fahrenheit: "))
        temp = (5/9 * (response - 32))
        print(f"{response}°F is {temp}°C\n")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Please select from the list.\n")