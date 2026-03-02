print("Grading system.")
name = input("Enter your name: ")
Marks = int(input("Enter your grade: "))

if Marks > 100 or Marks < 0:
    print("Enter a mark ranging 0-100")
elif Marks >= 80:
    grade = 'A'
elif Marks >= 60:
    grade = 'B'
elif Marks >= 50:
    grade = 'C'
elif Marks >= 40:
    grade = "Pass"
else:
    grade = "Fail"

if 0 <= Marks <= 100:
    print(f"{name}, your grade is {grade}")