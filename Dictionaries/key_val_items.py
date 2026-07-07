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

'''
student = {
    "name": "Tendul",
    "age": 23
}

First line
print("name" in student)

Python asks:

"Is "name" a key in this dictionary?"

Keys are:

name
age

So:

True

Second line

print("Tendul" in student)

Python asks:

"Is "Tendul" a key?"

Notice carefully...

"Tendul" is a value, not a key.

Keys are still:

name
age

So:

False

⭐ Very Important Rule

When you write:

if something in dictionary:

Python checks only the keys, not the values.

If you want to check the values

Use:

"Tendul" in student.values()

Example:

print("Tendul" in student.values())

Output:

True

Because now Python is checking:

Tendul
23

instead of:

name
age

🧠 Memory Trick

Think of a dictionary as a cupboard.

name  ─────► Tendul
age   ─────► 23

When you ask:

"name" in student

Python looks only at the labels on the drawers (keys).

If you want to know whether "Tendul" exists, you have to open the drawers:

"Tendul" in student.values()

'''
