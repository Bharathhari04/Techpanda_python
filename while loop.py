
i = 1
while i <= 10:
    print(i,end=" " )
    i += 1
print()

i = 10
while i >= 1:
    print(i,end  =" ")
    i -= 1
print()

i = 2
while i <= 50:
    print(i,end=" ")
    i += 245
print()

i = 1
while i <= 50:
    print(i,end =" ")
    i += 2
print()

i = 5
while i <= 100:
    print(i,end=" ")
    i += 5
print()

n = int(input("Enter a number for multiplication table: "))
i = 1
while i <= 10:
    print(n, "*12", i, "=", n * i)
    i += 1

n = int(input("Enter N to identify total : "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print(f"Total of first {n} number is :",total)


n = int(input("Enter N : "))
i = 1
product = 1
while i <= n:
    product *= i
    i += 1
print(f"Productof first {n} number is  :",product)

n = int(input("Enter the number :"))
fact = 1
i=1
while i <=n:
    fact*=i
    i+=1
print(f"Factorial of {n} is :",fact)

n = input("Enter the sequnce of number to count the digits :").split()
count = 0
while count <len(n):
    count +=1
print("Count :" ,count)


n =int(input("Enter the  sequence of number for reversing : "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
print("Reverse of numbers :" ,reverse)

n = int(input("Enter the sequnce of digits :"))
sum = 0
while n > 0:
   digit =n%10
   sum= sum+digit
   n=n//10
print("sum of digit is :" ,sum)

n = input("Enter the sequnce of number :").split()
largest =0
i=0
while i<len(n):
   largest =max(n)
   i+=1
print("largest digit is :" ,largest)


n = input("Enter the sequnce of number :").split()
small =0
i=0
while i<len(n):
   small =min(n)
   i+=1
print("smallest digit is :" ,small)


n = int (input("Enter the number :"))
original = n
reverse = 0
while n > 0:
    digit = n%10
    reverse = reverse *10 + digit
    n//=10 
if original == reverse:
     print("Palindrome")
else:
    print("Not a Palindrome")


n= int(input("Enter the number :"))
original =n
sum = 0
while n>0:
    digit=n%10
    sum = sum + digit**3
    n=n//10
if original == sum:
    print("Armstrong number")
else:
     print("Not a armstrong number")




a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice=input("Enter your choice (+,-,*,/) :")
while True:
    if choice == "+":
        print(a + b)
    elif choice == "-":
        print(a - b)
    elif choice == "*":
        print(a * b)
    elif choice == "/":
        print(a / b)
    choice=input("Do you want to coninue (Y/N) :")
    if choice=="N"or choice=="n":
      break


password =input("Enter your password :")
while True:
    if password == 'python123':
        print("Acess granted!")
        break 
    password =input("Enter your password:")



n = int(input("Enter number: "))
sum=0
while n != 0:
    sum = sum + n
    n = int(input("Enter number: "))
print("Sum =", sum)

n= int(input("Enter the number of terms :"))
a=0
b=1
count=0
while count< n:
    print(a, end= " ")
    c= a+b
    a=b
    b=c
    count +=1
print()


secret = 5
attempts = 0
while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong!")
print("Attempts:", attempts)

input()



