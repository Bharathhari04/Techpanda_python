fruits =['Apple','Banana','Mango','Orange']
print(fruits)
print(fruits[0])
print(fruits[-1])

print(len(fruits))

fruits[1]= 'Grapes' 
print(fruits)

fruits.append('pineapple')
print(fruits)

fruits.insert(1,'Kiwi')
print(fruits)

fruits.remove('Orange')
print(fruits)

del fruits[2]
print(fruits)

fruits.clear()
print(fruits)


numbers= [1,2,3,4,5,6,7,8,9,10 ]
print(numbers[:5])

print(numbers[-4:])

print(max(numbers))

print(min(numbers))

print(sum(numbers))

average = sum(numbers)/len(numbers)
print(average)

a=[1,5,2,5,6,5]
print(a.count(5))

print(numbers.index(8))

print(numbers[ : : -1 ])



numbers=list(map(int,input("Enter the list number :").split()))
print(numbers)

i = int(input("Enter the element :"))
if i in numbers:
    print("elemets found")
else:
    print("element not found")


for i in numbers:
    if i %2==0:
        print(i ,end =" ")
print()

for i in numbers:
    if i %2 !=0:
        print(i,end=" ")
print()




b =[1,2,2,3,3,3,3,4,4,5,5,6,7]
print(list(set(b)))

numbers.sort
print(numbers)

numbers.sort (reverse= True)
print(numbers)




 
list1=[1,2,3]
list2=[3,4,5,6,]
concatenated_list =list1 + list2
print(concatenated_list)



largest = max(numbers)   
numbers.remove(largest)  
print(max(numbers)) 


     
li=[10,20,30,40,50,60]
li= li[1:] + li[:1]
print(li)

li=[10,20,30,40,50,60]
li= li[-1:] + li[:-1]
print(li)

my_list = [1,4,5,6,8,2,3,10,12,11]
even_list =[]
odd_list=[]
for i in my_list:
    if i % 2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("odd",odd_list)
print("even",even_list)

list1=[1,2,3]
list2=[3,4,5,6,]
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print(common)

num=[1,-1,2,-3,5,-6,7,8,-9]
positive=[]
for i in num:
    if i>=0:
        positive.append(i)
print(positive)


n=list(map(int,input("Enter the list number :").split()))
for i in n :
    print(i *i )
print()








   
