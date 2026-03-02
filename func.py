def greet(name):
    print(f"Hello {name}")
greet("Sam")
greet("Mark")
greet("Rukiyah")

def add(a,b):
    return a+b
new=add(6,5)
print(new)

def calculate_area(length, width):
    area=length * width
    return area
a=calculate_area(5,4)
print(a)

#Typed of parameters
#Position parameter
def introduce(name,age):
    print(f"My name is {name} and i am {age} years old")
introduce("Jack", 23)

print("Hello ", end="***")

#Keyword parameter
def key(age=25, name="John"):
    print(f"\nHello {name} your age is {age}")
key()

#Default parameter
def namme(name="Guest"):
    print(f"Hello {name}")
namme()

#Arbitrary Positional Argument-*args
def add_all(*numbers):
    total= 0
    for num in numbers:
        total +=num
    return total

print(add_all(10,20,30,40,50,60))

#Arbitrary Keyword Argument
def profiles(**details):
    print(details)
profiles(name="Jack", age= 25, country="Kenya")

def profile(**details):
    for key,value in details.items():
        print(key,":", value)

profiles(name="Jack", age= 25, country="Kenya")

#mixed parameters
def example(a,b, *args,c=5,**kwargs):
    print(a,b)
    print(args)
    print(c)
    print(kwargs)
example(1,2,3,4,5,c=20, name="Jack")

#unpacking dict
def greet(name, age):
    print(name, age)
data={"name":"Jack","age":25}
greet(**data)

#keyword and positional only parameter
def func(a,b,/):
    print(a,b)