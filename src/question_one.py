age = input("Provide me an age: \n")
age_num = int(age)

if age_num < 13:
    print("Child")
elif age_num < 20:
    print("Teenager")
elif age_num < 60:
    print("Adult")
else:
    print("Senior")
