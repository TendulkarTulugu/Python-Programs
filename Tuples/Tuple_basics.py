#3 
'''
A tuple is almost like a list, but with one very important difference:

A tuple cannot be changed after it is created.

We call this "immutable".

List Example

numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)

Output:

[100, 20, 30]

✅ Lists are mutable (changeable).

Tuple Example
numbers = (10, 20, 30)

numbers[0] = 100

Output:

TypeError: 'tuple' object does not support item assignment

❌ Tuples cannot be modified.

Creating a Tuple
student = ("Tendul", 23, "AI & DS")

print(student)

Output:

('Tendul', 23, 'AI & DS')

Notice the parentheses ().

Accessing Elements

Exactly like a list:

student = ("Tendul", 23, "AI & DS")

print(student[0])
print(student[1])
print(student[2])

Output:

Tendul
23
AI & DS

So indexing works exactly like lists.
'''

# lets create a tuple first

student=('Tendul',22,"AI & DS")
print(student[0])
print(student[1])
print(student[2])

# student[1]=24
# it shows the error as the tuple is immutable
print(student)