def deposit(balance,amount):
    return balance+ amount
balance=deposit(100,50)
print(balance)
#Use non local keyword
def outer():
    x = 10

    def inner():
        nonlocal x
        x=20

    inner()
    print(x)
outer()

#Show the local scope

def my_function():
    x=10
    print(x)

my_function()

#Global variable
#x=10

#def show():
#    print(x)
#show()

#Modifying Global variables
#x=10

def change():
    x=20
    print(x)
change()
#print(x)

#Modify global variable
#x=10

def change():
    global x
    x= 20
change()
#print(x)

#Local vs Global with same names
#x= 5

def test():
    x=10
    print(f"Inside {x}")
test()
#print(f"Outside {x}")

#LEGB RULE
x= "Global"

def outer():
    x= "Enclosing"

    def inner():
        x="Local"
        print(x)
    inner()
outer()