#PRINT HELLO PYTHON USING FUNCTION:
def display():
    print("hello python")
display()

#CREATE FUNCTION() AND TAKE USER NAME AS INPUT:
def user_name():
    name=input("enter your name: ")
    print(f"WELCOME {name}")
user_name()

#ADD TWO NUMBERS:
def add():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    c=a+b
    print(f"sum of {a} and {b} is {c}")
add()

#FIND SQUARE OF A NUMBER:
def square():
    a=int(input("enter the number: "))
    b=a*a
    print(f"square of {a} is {b}")
square()

#EVEN OR ODD NUMBER:
def num():
    n=int(input("enter the number: "))
    if n%2==0:
        print("even number")
    else:
        print("odd number")
num()

#MAXIMUM OF TWO NUMBERS:
def num():
    a=int(input("enter first number: "))
    b=int(input("enter second number: "))
    if a>b:
        print("maximum of two number is: ",a)
    else:
        print("maximum of two number is: ",b)
num()

#CONVERT CELSIUS TO FAHRENHEIT:
def temp():
    c=int(input("enter temperature in celsius: "))
    f=(c*9/5)+32
    print(f"temperature in fahrenheit is: {f}")
temp()

#CALCULATE SIMPLE INTEREST:
def interest():
    p=int(input("enter principle amount: "))
    r=int(input("enter rate of interest: "))
    t=int(input("enter time in years: "))
    si=(p*r*t)/100
    print(f"simple interest is: {si}")
interest()

#FACTORIAL OF A NUMBER:
def factorial():
    n=int(input("enter the number: "))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"factorial of {n} is: {fact}")
factorial()

#LARGEST NUMBRE IN A LIST:
def largest():
    list=[10,25,5,40]
    max=list[0]
    for i in list:
        if i>max:
            max=i
    print(f"largest number in the list is: {max}")
largest()

#COUNT NUMBER OF VOWELS I A STRING:
def count_vowels():
    string=input("enter the string: ")
    count=0
    for i in string:
        if i in "aeiouAEIOU":
            count += 1
    print(f"number of vowels in the string is: {count}")
count_vowels()

#REVERSE A STRING:
def reverse_string():
    string=input("enter the string: ")
    reversed_string=string[::-1]
    print(f"reversed string is: {reversed_string}")
reverse_string()

#palindrome:
def palindrome():
    string=input("enter thew string: ")
    if string==string[::-1]:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")
palindrome()

#COUNT FREQUENCY OF EACH CHARACTER IN A STRING:
def frequency():
    string=input("enter the string: ")
    freq={}
    for i in string:
        freq[i] = freq.get(i, 0) + 1
    print(f"frequency of each character in the string is: {freq}")
frequency()

#SUM OF ALL ELEMENTS:
def sum_of_elements():
    list=[1,2,3,4,5]
    sum=0
    for i in list:
        sum=sum+i
    print(f"sum of all elements in the list is: {sum}")
sum_of_elements()

#FIND SECOND LARGEST NUMBER IN A LIST:
def SecondLargest():
    list=[10,20,30,40,50]
    list.sort()
    print(list[-2])
SecondLargest()

#REMOVE DUPLICATE ELEMENTS FROM A LIST:
def duplicate():
    list=[1,2,3,4,5,6,6,7,8]
    result=[]
    for i in list:
        if i not in result:
            result.append(i)
    print(result)
duplicate()

#CHECK NUMBER PRIME OR NOT:
def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print("Not a Prime Number")
                break
        else:
            print("Prime Number")
    else:
        print("Not a Prime Number")
num = int(input("Enter a number: "))
prime(num)

#FIBONACCI NUMBER:
def fibonacci():
    n = int(input("Enter the number of terms: "))
    a = 0
    b = 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
fibonacci()

#FINCTION WITH DEFAULT ARGUMENTS:

#DISPLAY NAMES:
def display(name="unknown"):
    print("name:",name)
display()

#DEFAULT BONUS PERCENTAGE:
def bonus(salary,Bonus=10):
    print(f"total bonus is: ",{salary*Bonus})
bonus(599)

#CALCULATE POWER:
def power(number,exponent=2):
    print(f"power of {number} is: {number**exponent}")
n=int(input("enter the number to power: "))
power(n)


#CALCULATE AREA OF SHAPES:
def area(length=10,width=5):
    print("area:",length*width)
area()

#EMPLOYEE INFO:
def emp(name,salary,dept="not assigned"):
    print("name:",name)
    print("salary:",salary)
    print("dept:",dept)
emp("vishnu",30000)
emp("priya",40000,"CSE")

#LAMBDA FUNCTION:

#ADD TWO NUMBERS:
add=lambda a,b:a+b
print(add(10,20))

#EVEN OR ODD:
check=lambda n:"even" if n%2==0 else "odd"
print(check(10))
print(check(7))

#MAP() TO SQUARE NUMBERS:
num=[1,2,3,4,5]
result=list(map(lambda x:x**2,num))
print(result)

#FILTER()TO EXTRACT EVEN NUMBERS:
num=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,num))
print(result)

#SORTED() ON SECOND VALUE:
student=[("vishnu",20),
         ("priya",30)]
result=sorted(student,key=lambda x:x[1])
print(result)


#*ARGS-SUM OF MULTIPLES:
def add(*args):
    total=0
    for num in args:
        total=total+num
    return total
print(add(10,20,40))

#**KWARGS-DISPLAY EMPLOYEES:
def emp(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
emp(name="vishnu",age=21,salary=30000,dept="CSE")

#MAX,MIN,AVG:
def calculate(numbers):
    minimum=min(numbers)
    maximum=max(numbers)
    average=sum(numbers)/len(numbers)
    return minimum,maximum,average
numbers=[10,20,30,40,50,60]
minimum,maximum,average=calculate(numbers)
print("minimum:",minimum)
print("maximum:",maximum)
print("average:",average)

#RECURSIVE FUNCTION TO CALCULATE FACTORIAL:
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

#FIBONACCI NUMBERS:
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
for i in range(10):
    print(fibonacci(i),end=" ")

#FUNCTION DECORATOR:
def decorator(function):
    def wrapper():
        print("funvtion started")
        function()
        print("function completed")
    return wrapper
@decorator
def hello():
    print("hello")
hello()

#CHACK PASSWORD:
def check_password(password):
    if len(password) < 8:
        return "Password must contain at least 8 characters"
    has_number = False
    has_uppercase = False
    for char in password:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True
    if has_number and has_uppercase:
        return "Strong Password"
    else:
        return "Weak Password"
password = input("Enter password: ")
print(check_password(password))

#COUNT WORDS:
def count(sentence):
    words=sentence.split()
    return len(words)
sentence=input("Enter a sentence: ")
print("Number of words:", count(sentence))

#MERGE TWO DICTIONARIES:
def merge_dict(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result
dict1 = {"name": "Vishnu", "age": 20}
dict2 = {"course": "Data Engineering", "city": "Chennai"}
result = merge_dict(dict1, dict2)
print(result)

#MENU-DRIVEN CALCULATOR:
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Calculator closed")
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == 1:
        print("Result:", addition(a, b))
    elif choice == 2:
        print("Result:", subtraction(a, b))
    elif choice == 3:
        print("Result:", multiplication(a, b))
    elif choice == 4:
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", division(a, b))
    else:
        print("Invalid choice")