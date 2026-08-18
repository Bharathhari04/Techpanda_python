a = int(input("Enter a  number: "))
print('Positive' if a>=0 else 'Negative')

a=int(input("Enter the first number : "))
b=int(input("Enter the second number :"))
print(f'{a} is largest number' if a>b else  f'{b} is largest number')

a = int(input("Enter the number :"))
print('even' if a%2==0 else 'odd')

mark = int(input("Enter the mark : "))
print('The student is pass' if mark>=40 else 'The student is fail')

age = int(input("Enter the age :"))
print('you are eligible for voting' if age>=18 else 'you are not eligible for voting')


a=int(input("Enter the first number : "))
b=int(input("Enter the second number :"))
print(f'{a} is smallest number' if a<b else  f'{b} is smallest number')


age = int(input("Enter the age :"))
print('Adult' if age>=18 else 'Minor')

a = input("Enter the character :")
print(f'{a} is uppercase' if a.isupper() else f'{a} is lowercase' )


a=int(input("Enter a year :"))
print('Its a leap year' if a%4==0 else 'Not a leap year')

mark = int(input("Enter the mark : "))
print('GRADE A'if mark>=80 and mark <=100 else 'GRADE B' if mark >=65 and mark<= 81 else 'GRADE C' if mark >=40 and mark<= 66 else'GRADE F' )
