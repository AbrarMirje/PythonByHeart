age = int(input("What's your age? "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")