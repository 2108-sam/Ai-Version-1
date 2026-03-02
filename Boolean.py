number= int(input("Enter a number: "))
if (number>0):
    print(number)

if (number<0):
    print("A negative number")

age= int(input("Enter your age: "))
if (age>=18):
    print("Eligible to vote")

number_=number%2
if (number_==0):
    print("You just entered an even number")
password="Heal"
crid= input("Enter your password: ")
if (crid==password):
    print("Correct password")