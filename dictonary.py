student = {
    "Name": "John",
    "Age": 20,
    "Course": "Python"
}
print("student :" ,student)

print(student["Name"])

print(student.keys())

print(student.values())

for key, value in student.items():
    print(key, value)


student["City"] = "Chennai"
print("student :" ,student)



student["Age"] = 21
print("student :" ,student)


student.pop("Course")
print("student :" ,student)


del student["City"]
print("student :" ,student)

student.clear()
print("student :" ,student)

marks = {
    "Asha": 85,
    "Rahul": 90,
    "John": 78,
    "Priya": 88,
    "Kavin": 92
}
print("Marks =",marks)

print(marks.keys())

print(marks.values())

total = sum(marks.values())
print("Total:", total)


average = sum(marks.values()) / len(marks)
print("Average:", average)


highest = max(marks, key=marks.get)
print("Highest:", highest)


lowest = min(marks, key=marks.get)
print("Lowest:", lowest)

if "Rahul" in marks:
    print("Rahul exists in the dictionary")
else:
    print("Rahul does not exist in the dictionary")

print(len(marks))

copy_dict = marks.copy()
print(copy_dict)


students = {}

n = int(input("Enter the number of element: "))

for i in range(n):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    students[name] = marks

print(students)

for name, marks in students.items():
    if marks > 80:
        print(name)

for name, marks in students.items():
    if marks < 50:
        print(name)

passed_students = {}
for name, marks in students.items():
    if marks >= 50:
        passed_students[name] = marks
print(passed_students)


total = 0
for marks in students.values():
    if marks % 2 == 0:
        total += marks
print(total)

d1 = {"A": 10, "B": 20}
d2 = {"C": 30, "D": 40}
d1.update(d2)
print(d1)

d = {"C": 30, "A": 10, "D": 40, "B": 20}
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)


d = {"A": 40, "B": 10, "C": 30, "D": 20}
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_dict)

text = input("Enter a string: ")
frequency = {}
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
print(frequency)

student = {
    "Name": "John",
    "Age": 20,
    "City": "Chennai"
}
key = input("Enter key: ")
if key in student:
    print("Key Found")
else:
    print("Key Not Found")


input()