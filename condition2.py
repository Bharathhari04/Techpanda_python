#IF CONDITION

#CHECK POSITIVE NUMBER:
a=int(input("enter a:"))
if a>0:
    print("positive number")

#ELIGIBLE FOR VOTING:
age=int(input("enter your age:"))
if age>=18:
    print("elegible to vote")

#DIVISIBLE BY 7:
num=int(input("enter a number:"))
if num%7==0:
    print("dvisible by 7")

#CHECKING PASS:
mark=int(input("enter your mark: "))
if mark>=40:
    print("pass")

#CHECKING UPPERCASE:
a=input("enter a character: ")
if a in["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
    print("upper case")

#IF ELSE

#CHECKING EVEN OR ODD:
num=int(input("eneter a number: "))
if num%2==0:
    print("even number")
else:
    print("odd number")

#CHECKING POSITIVE OR NEGATIVE:
num=int(input("enetr a number: "))
if num>0:
    print("positive number")
else:
    print("negative number")

#LARGEST OF TWO NUMBERS:
a=int(input("enter number a: "))
b=int(input("enter number b: "))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

#ELIGIBLE FOR LICENSE:
age=int(input("enter your age:"))
if age>=18:
    print("elegible to driving license")
else:
    print("not elegible for driving license")

#CHECKING LEAP YEAR:
a=int(input("enter year:"))
if a%4==0:
    print("leap year")
else:
    print("not a leap year")

#IF ELIF ELSE

#GRADE:
mark=int(input("enter your mark:"))
if mark>=90:
    print("grade A")
elif mark>=80:
    print("grade B")
elif mark>=70:
    print("grade C")
elif mark>=60:
    print("grade D")
elif mark<60:
    print("grade F")
else:
    print("invalid mark")

#LARGEST OF THREE NUMBERS:
a=int(input("enter number a: "))
b=int(input("enter number b: "))
c=int(input("enter number c: "))
if a>b and a>c:
    print("a is greater than b and c")
elif b>a and b>c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")

#ELECTRICITY BILL:
bill=int(input("enter your bill amount:"))
if bill==100:
    print("$2 per unit")
elif bill>100 and bill<=200:
    print("$3 per unit")
elif bill>200:
    print("$5 per unit")
else:
    print("invalid bill amount")

# #WEEKDAY:
day=int(input("enter a day:"))
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")

# #TAX:
salary=int(input("enter your salary:"))
if salary<250000:
    print("no tax")
elif salary>=250000 and salary<=500000:
    print("5% tax")
elif salary>=500000 and salary<1000000:
    print("20% tax")
elif salary>=1000000:
    print("30% tax")

#TERNARY OPERATOR:

#LARGEST OF TWO NUMBERS:
a=int(input("enter a:"))
b=int(input("enter b:"))
result="a is greater" if a>b else "b is greater"
print(result)

#EVEN OR ODD:
a=int(input("enter a number:"))
result="even number" if a%2==0 else "odd number"
print(result)

#ELIGIBLE TO VOTE:
age=int(input("enter your age:"))
result="elegible to vote" if age>=18 else "not eligible"
print(result)

#MINIMUM OF TWO NUMBERS:
a=int(input("enter a:"))
b=int(input("enter b:"))
result="a is minimum" if a<b else "b is minimum"
print(result)

#POSITIVE OR NEGATIVE:
a=int(input("enter a number:"))
result="positive number" if a>0 else "negative number"
print(result)

#ADDITIONAL QUESTIONS:

#LARGEST OF THREE NUMBERS USING NESTEST IF:
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
if a>b:
    if a>c:
        print("a is greater")

#CHARACTER IS VOWEL OR CONSONANT OR DIGIT OR SPECIAL CHARACTER:
a=input("enter a character:")
if a in ["a","e","i","o","u"]:
    print("vowel")
elif a.isalpha():
    print("consonant")
elif a.isdigit():
    print("digit")
else:
    print("special character")

#CALCULATOR:
a=int(input("enter a:"))
b=int(input("enter b:"))
operator=input("enter operator (+, -, *, /): ")
if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")

#MARKS:
mark=int(input("enter your mark:"))
if mark>=90:
    print("DISTICTION")
elif mark>=80:
    print("FIRST CLASS")
elif mark>=70:
    print("SECOND CLASS")
else:
    print("FAIL")

#CENTURY LEAP YEAR:
year=int(input("enter a year:"))
if year%100==0 and year%400==0:
    print("leap year")
elif year%4==0:
    print("leap year")
else:
    print("not leap year")
