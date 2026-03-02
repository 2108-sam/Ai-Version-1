print("This program helps you to know whether your selection is weekday or weekend")
print("""
\n1\tMonday
\n2\tTuesday
\n3\tWednesday
\n4\tThursday
\n5\tFriday
\n6\tSaturday
\n7\tSunday
""")
day=int(input("Enter your selection"))
if day<6 and day>0:
    print("This is a weekday")
else:
    print("This is a weekend4")