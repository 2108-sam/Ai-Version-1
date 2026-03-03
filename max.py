while True:
    x=int(input("Enter x: "))
    y=int(input("Enter y: "))
    z= int(input("Enter z: "))

    if (x>y) and (x>z):
        print(f"{x} is greater.")
    elif (y>x) and (y>z):
        print(f"{y} is greater.")
    elif (z>x) and (z>y):
        print(f"{z} is greater.")
    else:
        print("They may be equal.")