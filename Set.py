#SET

#CREATE SET:
fruits={"apple","banana","mango","orange"}
print(fruits)

#PRINT ALL ELEMENTS:
fruits={"apple","banana","mango","orange"}
print(fruits)

#FIND LENGTH OF THE SET:
print(len(fruits))

#ADD "PINEAPPLE" TO SET:
fruits.update({"pineapple"})
print(fruits)

#ADD MULTIPLE ELEMENTS:
fruits.update({"grapes","kiwi"})
print(fruits)

#REMOVE ORANGE:
fruits.remove("orange")
print(fruits)

#REMOVE RANDOM ELEMENT:
fruits.pop()
print(fruits)

#CHECK"BANANA" EXISTS:
fruits={"apple","banana","mango","orange"}
if "banana" in fruits:
    print("banana exists")
else:
    print("banana does not exists")

#PRINT ALL ELEMENTS USING FOR LOOP:
for fruit in fruits:
    print(fruits)

#REMOVE ALL ELEMENTS:
fruits.clear()
print(fruits)

#CREATE TWO SET:
a={1,2,3,4,5}
b={4,5,6,7,8}
print("a=",a)
print("b=",b)

#UNION ALL A AND B:
print(a.union(b))

#INTERSECTION A-B:
print(a.intersection(b))

#DIFFERENCE A-B:
print(a.difference(b))

#SYMMETRIC DIFFERENCE:
print(a.symmetric_difference(b))

#CHECK A IS A SUBSET OF B:
print(a.issubset(b))

#CHECK A IS SUPERSET OF B:
print(a.issuperset(b))

#COPY:
a_copy=a.copy()
print(a_copy)

#FIND NO OF ELEMENTS:
print(len(a))

#CONVERT LIST TO SET:
number=[1,2,3,4,5,6,6,7,4,2]
num_set=set(number)
print(num_set)

#ACCEPT 10 NUMBERS FROM USERS:
number=set()
for i in range(10):
    num=int(input("enter number: "))
    number.add(num)
print(number)

#PRINT ALL EVEN NUMBERS:
print("even numbers: ")
for num in  number:
    if num%2==0:
        print(num)

#PRINT ALL ODD NUMBERS:
print("odd numbers: ")
for num in number:
    if num %2!=0:
        print(num)

#MAX AND MIN:
print("maximum",max(number))
print("minimum",min(number))

#SUM AND AVERAGE:
total=sum(number)
average=total/len(number)
print("sum",total)
print("average",average)

#MERGE SETS:
s1={1,2,3}
s2={3,4,5}
merged=s1.union(s2)
print(merged)

#REMOVE DUPLICATES:
list=[1,2,3,4,5,6,6,7,3,4,2]
unique=set(list)
print(unique)

#COMMON ELEMENTS BETWEEN TWO SETS:
a={2,3,4,6}
b={2,4,6,1}
common=a.intersection(b)
print(common)

#ELEMENT PRESENT ONLY IN FURST SET:
a={1,2,3,4,5,6}
b={3,2,5,6,2,3}
result=a.difference(b)
print(result)

#DISJOINT:
a={1,2,3}
b={4,2,6}
if a.isdisjoint(b):
    print("sets are disjoint")
else:
    print("sets are not disjoint")