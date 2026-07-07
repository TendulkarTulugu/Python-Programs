#2

'''
What is a Dictionary?

A dictionary stores data as Key : Value pairs.

Think of an English dictionary.

Apple  → A fruit
Book   → Something you read
Python → Programming language

Each word is a key.

Each meaning is a value.

Python works the same way.

Example
student = {
    "name": "Tendul",
    "age": 22,
    "branch": "AI"
}

Here,

Key	Value
"name"	"Tendul"
"age"	22
"branch"	"AI"
How to Access Values

Suppose we have:

student = {
    "name": "Tendul",
    "age": 22,
    "branch": "AI"
}

To get the name:

print(student["name"])

Output:

Tendul

To get the age:

print(student["age"])

Output:

22

Why Dictionaries?

Imagine you use a list:

student = ["Tendul", 22, "AI"]

Now tell me...

Which one is the branch?

student[2]

You have to remember the position.

With a dictionary:

student["branch"]

It's immediately clear.

That's why dictionaries are so useful.

🎯 Your First Dictionary Program

Type this exactly:

student = {
    "name": "Tendul",
    "age": 22,
    "branch": "AI"
}

print(student["name"])
print(student["age"])
print(student["branch"])

Run it.

Then tell me the output.
'''


student = {
    "name": "Tendul",
    "age": 22,
    "branch": "AI"
}

print(student["name"])
print(student["age"])
print(student["branch"])



'''

⭐ Important Difference
List
student = ["Tendul", 22, "AI"]

Access by index:

student[0]
student[1]
student[2]
Dictionary
student = {
    "name": "Tendul",
    "age": 22,
    "branch": "AI"
}

Access by key:

student["name"]
student["age"]
student["branch"]

So:

Lists → use indexes
Dictionaries → use keys

'''

