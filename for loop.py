#print numbers from 1 to 10:
for i in range(1,11):
    print(i)

#print numbers from 10 to 1 (reverse):
for i in reversed(range(1,11)):
    print(i)

#print even numbers:
for i in range(2,51,+2):
    print(i)

#print odd numbers:
for i in range(1,50,+2):
    print(i)

# multiplication table
n=int(input("enter the number to develop a multiplication table: "))
a=int(input("enter starting number: "))
b=int(input("enter ending number: "))
for i in range (a,b+1):
    print(i," =",n," *",i*n)

#sum of numbers from 1 to 100:
n=int(input("enter a number to sum: "))
i=1
sum=1
for i in range(1,n,+1):
    sum+=i
    i+=1
print(f"sum of all numbers is: ",sum)

#sum of even numbers:
n=int(input("enter a number to sum even numbers: "))
i=1
sum=2
for i in range(1,n,+2):
    sum+=i
    i+=1
print(f"sum of all even numbers is: ",sum)

#sum of odd numbers:
n=int(input("enter a number to sum odd numbers: "))
i=1
sum=1
for i in range(1,n,+1):
    sum+=i
    i+=1
print(f"sum of all odd numbers is: ",sum)

#square of numbers:
n=int(input("enter the number to square: "))
square=0
for i in range(1,n+1):
    square=n*n
print(square)

#cube of numbers:
n=int(input("enter the number to cube: "))
cube=0
for i in range(1,n+1):
    cube=n*n*n
print(cube)

#factorial number:
n=int(input("enter a number to check factorial: "))
i=1
fact=1
for i in range(1,n+1):
    fact*=i
print("the factorial of a number is: ",fact)

#count of the number of digits:
num=input("enter the number to count: ")
count=0
for i in num:
    count+=1
print(count)

#reverse a string:
n=input("enter a string: ")
reverse=" "
for i in n:
    reverse=i+reverse
print(reverse)

#count no of vowels in a string:
n=input("enter a string: ")
count=0
for i in n:
    if i in "aeiouAEIOU":
        count+=1
print(count)

#print each character in a string:
n=input("enter a string: ")
for i in n:
    print(i)

#calculate sum of all digits :
n=input("enter a number: ")
sum=0
for i in n:
    sum+=int(i)
print(sum)

#print the ASCII value:
n=input("enter a string: ")
for i in n:
    print(i, "=", ord(i))

#count of numbers of uppercase and lowercase letter:
n=input("enter a string: ")
upper=0
lower=0
for i in n:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
print("uppercase letter: ",upper)
print("lowercase letter: ",lower)

#print numbers between 1 to 100:
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)

#print the N natural numbers and calculate their average:
n=int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    print(i)
    sum+=1
average=sum/n
print("average = ",average)

#pattern:
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

#reverse pattern:
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#number pattern:
for i  in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

#same number pattern:
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

#print all prime numbers between 1 and 100:
for i in range(2,101):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:
        print(i)

        
