#6

student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS"
}

print(student.keys())
# it'll give all the keys of dict

print(student.values())
#it'll give all the values of dict

print(student.items())
# it 'll give all items. Each item is a (key, value) pair.

for key in student:
    print(key,':',student[key])
# it give the dict key:values

for key,value in student.items():
    print(key,':',value)

# But items() lets us get both the key and value directly.


'''
🎯 Your Turn

Create this dictionary:

student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS",
    "cgpa": 8.04
}

Now write three loops:

Loop 1

Print only the keys.

Expected:

name
age
branch
cgpa
Loop 2

Print only the values.

Expected:

Tendul
23
AI & DS
8.04
Loop 3

Print both.

Expected:

name : Tendul
age : 23
branch : AI & DS
cgpa : 8.04

'''
students = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS",
    "cgpa": 8.04
}

for key in students:
    print(key)

for values in students:
    print(students[values])

for key,value in students.items():
    print(key,':',value)