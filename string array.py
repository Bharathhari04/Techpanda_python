text = input("Enter a string: ")
count = 0
for ch in text:
    count += 1
print("Length:", count)

text = input("Enter a string: ")
reverse = ""
for ch in text:
    reverse = ch + reverse
print("Reverse:", reverse)

text = input("Enter a sentence: ")
words = text.split()
count = 0
for i in words:
    count += 1
print("Number of words:", count)

arr = list(map(int, input("Enter elements: ").split()))
print("Largest element :",max(arr))


arr = list(map(int, input("Enter elements: ").split()))
arr.sort(reverse=True)
print("Second largest:", arr[1])

arr = list(map(int, input("Enter elements: ").split()))
new_arr = []
for i in arr:
    if i not in new_arr:
        new_arr.append(i)
print(new_arr)

arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
print(arr1+arr2)


arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))
common = []
for i in arr1:
    if i in arr2 and i not in common:
        common.append(i)
print("Common elements:", common)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not anagram")

arr = list(map(int, input("Enter elements: ").split()))
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print("Sorted array:", arr)