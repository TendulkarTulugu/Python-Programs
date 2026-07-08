'''
🎯 New Method: update()

Now let's learn another very useful dictionary method.

Suppose we have:

student = {
    "name": "Tendul",
    "age": 23
}

And another dictionary:

new_data = {
    "branch": "AI & DS",
    "cgpa": 8.04
}

If we write:

student.update(new_data)

The result is:

{
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS",
    "cgpa": 8.04
}

update() merges one dictionary into another.

Another Interesting Example
student = {
    "name": "Tendul",
    "age": 23
}

new_data = {
    "age": 24,
    "city": "Hyderabad"
}

student.update(new_data)

print(student)

What happens?

"age" already exists → it is updated to 24.
"city" doesn't exist → it is added.

Final dictionary:

{
    "name": "Tendul",
    "age": 24,
    "city": "Hyderabad"
}

So update() can both update existing keys and add new ones.
'''

student = {
    "name": "Tendul",
    "age": 23
}

new_data = {
    "branch": "AI & DS",
    "cgpa": 8.04
}

student.update(new_data)
print(student)
print(new_data)


'''
🎯 Dictionary Challenge (Interview Style)

This is a very common interview question.

Given:

student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS",
    "cgpa": 8.04
}

Write a function:

def search_key(dictionary, key):

Examples:

print(search_key(student, "age"))

Output:

23

Another:

print(search_key(student, "city"))

Output:

Key Not Found
Rules
❌ Don't use get().
✅ Use what you've already learned.
✅ Return the value if the key exists.
✅ Otherwise return "Key Not Found".
'''
student = {
    "name": "Tendul",
    "age": 23,
    "branch": "AI & DS",
    "cgpa": 8.04
}

def search_key(dictionary, key):
    for keys in dictionary:
        if key in dictionary:
            return dictionary[key]
        elif key not in dictionary:
            return 'key not found'
    return


print(search_key(student, "age"))
print(search_key(student, "city"))
