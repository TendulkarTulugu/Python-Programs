#7

student = {
    "name": "Tendul",
    "age": 23
}

print(student.get("name")) # returns Tendul
print(student.get("branch")) # returns None

'''
Case 1
print(student.get("name"))

Python asks:

"Does the key 'name' exist?"

✅ Yes.

So it returns:

Tendul
Case 2
print(student.get("branch"))

Python asks:

"Does the key 'branch' exist?"

❌ No.

Instead of giving an error, it returns:

None
'''

'''
⭐ Now compare these two.
Using []
print(student["branch"])

Output:

KeyError: 'branch'

❌ Program stops.

Using get()
print(student.get("branch"))

Output:

None

✅ Program continues.

Why is get() useful?

Imagine you're reading data from a file or an API.

Sometimes a key might not exist.

For example:

employee = {
    "name": "Rahul",
    "salary": 50000
}

If you write:

print(employee["address"])

💥 Error!

But:

print(employee.get("address"))

gives:

None

and your program keeps running.

This is why get() is used a lot in real-world Python code.

🎯 Bonus Feature

get() lets you specify a default value.

Example:

print(student.get("branch", "Not Available"))

Output:

Not Available

Instead of None, Python returns the value you provided.

This is very useful for displaying friendly messages.
'''
