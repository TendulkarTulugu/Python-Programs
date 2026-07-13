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



'''
⭐ Why Do Tuples Exist?

This is the question most beginners ask.

"If lists can do more, why use tuples?"

Good question.

Imagine your date of birth.

22-08-2003

Should your program accidentally change it?

❌ No.

Or GPS coordinates:

(17.3850, 78.4867)

They shouldn't change either.


# So we store data that should remain fixed in tuples.
'''


nums=(10,20,30,30,40)
print(len(nums))
print(nums[2])
print(nums)

for num in nums:
    print(num)


'''
Many people think:

"Tuple is immutable, so maybe we can't loop over it."

But looping doesn't modify the tuple.

You're only reading its values.

Reading is allowed.

Changing is not.

Think of a tuple like a book in a library:

✅ You can read every page.
❌ You cannot rewrite the pages.

'''
