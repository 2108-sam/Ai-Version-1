while True:
    number= int(input("Enter a number: "))
    if number<=1:
         print("Number Not a prime number.")
    else:
        for i in range(2, number):
            if number % i==0:
                print("Not a prime number.")
                break
        else:
            print("It is a prime.")

