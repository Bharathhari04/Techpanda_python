n = input("Enter the string :")
count= 0
for i in n:
   if i in "AEIOUaeiou":
      count+=1
print(" Vowel count :",count)


n = "bharath"
for i in n:
   print(i)

n=input("Enter the number: ")
sum=0
for i in n:
   sum = sum + int(i)
print("Sum of all digit is :",sum)


n = input("Enter the string :")
upper_count= 0
lower_count=0
for i in n:
   if i.isupper():
      upper_count +=1
   if i.islower():
      lower_count+=1
print("Count of uppercase:" ,upper_count)
print("Count of lowercase :",lower_count)


for i in range  (1,101):
   if i%3==0 and i%5==0:
      print(i , end=" ")
print()



for i in range(1,11): 
  print(i, end =" ")
print()

for i in reversed(range(1,11)):
   print(i,end =" " )
print()

for i in range(2,51,2):
   print(i,end= " ")
print()

for i in range(1,50,2):
   print(i,end= " ")
print()

num = int(input("Enter the value to develop table :"))
i = int(input("Enter the initial value :"))
n = int(input("Enter the ending value :"))
for i in  range (1,n+1):
    print(num, "*", i ,"=",num*i )

sum=0
for i in range(1,101):
   sum = sum + i
print("sum :" , sum)


sum=0 
for i in range (2,100,2):
   sum = sum + i
print(f"sum of all even numbers is : {sum}")

sum=0 
for i in range (1,100,2):
   sum = sum + i
print(f"sum of all odd numbers is : {sum}")


print("Square of  numbers")
for i in range(1,21):
   print( i**2,end = " ")
print()


print("Cube of  numbers")
for i in range(1,21):
   print( i**3,end = " ")
print()


n=int(input("Enter the number :"))
fact =1
for i in range(1,n+1):
   fact=fact *i
print(f"factorial of given number is : {fact}")



num=list(map(int,input("Enter the list number :").split()))
count=0
for i in num:
   count+=1
print(f"Number of digits : {count}")


n=input("Enter the string :")
reverse =" "
for i in n:
   reverse =i + reverse
print("Reverse :",reverse )
    


n = int(input("Enter the number :"))
vowel_count= 0
for i in n:
   if i in ['A','E','I','O','U','a','e','i','o','u']:
      count+=1
print("count :",vowel_count)



n = int(input("Enter the number :"))
sum =0
for i in (1,n+1):
    print(i)
    sum =  sum+i
average = sum/n
print("the average of the number is:",average)


input()
