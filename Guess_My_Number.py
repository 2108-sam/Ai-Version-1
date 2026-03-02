secret_number=5
while True:
    for i in range(3):
        guess=int(input("Enter your guess (0-10): "))

        if guess==secret_number:
            print(f"You have entered the correct guess with {i+15} tries")
            break
        elif guess>secret_number:
            print("The number is slightly higher")
        else:
            print("You have entered a slightly lower number")
    else:
        print("Game Over")