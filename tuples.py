my_tuple=('Red','Blue','Green','Yellow')
print("Colors =",tuple)

print(my_tuple[0])

print(my_tuple[-1])

print(len(my_tuple))

print(my_tuple[2])
print()

for i in my_tuple:
    print(i)
print()

print('Blue'in my_tuple)

print(my_tuple[1:4])

t1=(1,2,3)
t2=(4,5,6)
concate_tuple=(t1 + t2)
print("Concatenated tuple :" ,concate_tuple)

text='python'
repeat = text*3
print("Repeated tu[ple :",repeat)

num=(1,2,3,4,5,6,7,8,9,10)
print("Maximum :" ,max(num))
print("Minimum :",min(num))
print("Sum of all element :",sum(num))

average =sum(num)/len(num)
print("Average :",average)


t=(1,5,2,5,6,5)
print(t.count(5))

t=(2,4,6,8,10)
print("Index of 8 is :" ,t.index(8))


print("Reversing :",t[ : : -1 ])

my_tuple=(1,2,3,4)
my_list= list(my_tuple)
print(my_list)

my_list=[1,2,3,4]
my_tuple= list(my_list)
print(my_tuple)

numbers=tuple(map(int,input("Enter the numbers :").split()))
print("Numbers =" ,numbers)
print()

for i in numbers:
    if i %2==0:
        print(i,end =" ")
print()


for i in numbers:
    if i %2!=0:
        print(i,end =" ")
print()        

n=tuple(map(int,input("Enter the number :").split()))
for i in n :
    print(i *i )
print()

t=(9,9,4,7,8,1,1,1,3,3,8,9,10,14,14)
print("tuple =",t)
print("Reoving Duplicates :",tuple(set(t)))


print("Ascending orer :",tuple(sorted(t)))
print("Descending order :",tuple(sorted(t,reverse=True)))

t1=(1,2,3)
t2=(4,5,6)
print("t1 =" ,t1)
print("t2 =",t2)
merge=(t1 + t2)
print("Merged tuple :" ,merge)

sort = tuple(sorted(t,reverse=True))
print("SEcond largest :",sort[2])

numbers=tuple(map(int,input("Enter the  number :").split()))
print(numbers)

i = int(input("Enter the element :"))
if i in numbers:
    print("elemets found")
else:
    print("element not found")


t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
common = tuple(set(t1) & set(t2))
print("Common elements:", common)

t = (1, 2, 2, 3, 3, 4)
unique = tuple(set(t))
print("Unique elements:", unique)


t = (10, 20, 30)
a, b, c = t
print(a)
print(b)
print(c)
print()




t = ((1, 2), (3, 4), (5, 6))
print(t[0][1])
print(t[1][0])


t = (1, 2, 2, 3, 3, 3, 4)
for i in t:
    print(i, ":", t.count(i))
print()

t = ("Hello", "World", "Python")
result = " ".join(t)
print(result)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1, t2 = t2, t1
print("t1:", t1)
print("t2:", t2)

t = (2, 3, 4, 5, 6, 7, 8, 9)
for n in t:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)

t = (2, 3, 4, 5)
product = 1
for i in t:
    product = product * i
print("Product:", product)


t = (1, 2, 3, 2, 1)
if t == t[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

input()