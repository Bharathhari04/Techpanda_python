age = input("Enter your age: ")

if age.startswith("-") and age[1:].isdigit():
    print("Age must not be negative")

elif not age.isdigit():
    print("Enter right age")

else:
    age = int(age)

    if age == 0:
        print("Not yet born")

    elif age >= 1 and age <= 4:
        print("You are infant")

    elif age >= 5 and age <= 10:
        print("You are child")

    elif age >= 11 and age <= 17:
        print("You are adult")

    elif age >= 18 and age <= 53:
        print("You are eligible for voting")

    elif age >= 54 and age <= 80:
        print("You are senior citizen")

    else:
        print("Enter right age")

input()
   