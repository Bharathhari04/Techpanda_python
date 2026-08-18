month = int(input("Enter month number: "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")
match operator:
    case "+":
        print("Result =", a + b)
    case "-":
        print("Result =", a - b)
    case "*":
        print("Result =", a * b)
    case "/":
            print("Result =", a / b)
        

ch = input("Enter a character: ")
match ch:
    case "a" | "e" | "i" | "o" | "u"|"A"|"E"|"I"|"O"|"U" :
        print("Vowel")
    case _:
        print("Consonant")


print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = int(input("Enter your choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
match choice:
    case 1:
        print("Result =", a + b)
    case 2:
        print("Result =", a - b)
    case 3:
        print("Result =", a * b)
    case 4:
        print("Result =", a / b)
    case _:
        print("Invalid choice")

grade = input("Enter grade (A/B/C/D/F): ").upper()
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")


signal = input("Enter traffic signal: ").lower()
match signal:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid signal")

day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Enter your choice: "))
balance = 10000
match choice:
    case 1:
        print("Balance =", balance)
    case 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("New Balance =", balance)
    case 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("New Balance =", balance)
        else:
            print("Insufficient balance")
    case _:
        print("Invalid choice")

sides = int(input("Enter number of sides: "))
match sides:
    case 3:
        print("Triangle")
    case 4:
        print("Quadrilateral")
    case 5:
        print("Pentagon")
    case 6:
        print("Hexagon")
   

month = int(input("Enter month number: "))
match month:
    case 12 | 1 | 2:
        print("Winter")
    case 3 | 4 | 5:
        print("Spring")
    case 6 | 7 | 8:
        print("Summer")
    case 9 | 10 | 11:
        print("Autumn")
    case _:
        print("Invalid month")

input()