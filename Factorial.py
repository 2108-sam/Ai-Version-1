num=int(input("Enter your number: "))
factorial= 1
i=1

while i <= num:
    factorial= factorial * i
    i += 1
print(f"The factorial of {num} is {factorial}")