#1

'''
🤔 What is a Set?

A set is an unordered collection of unique elements.

The most important word is:

Unique

A set automatically removes duplicates.

Example 1
'''

numbers = {1, 2, 3, 4}

print(numbers)

# Output:

# {1, 2, 3, 4}
# Example 2

numbers = {1, 2, 2, 3, 3, 4, 4, 5}

print(numbers)

# What happens?

# Output:

# {1, 2, 3, 4, 5}

'''
Notice:

2  ❌ duplicate removed
3  ❌ duplicate removed
4  ❌ duplicate removed

Python keeps only one copy of each element.

'''

'''
⭐ Rule #1 of Sets

A set never stores duplicate values.

A set is unordered.

'''

'''
With a list:

numbers = [10, 20, 30, 40]

You know:

Index 0 → 10
Index 1 → 20
Index 2 → 30

With a set:

numbers = {10, 20, 30, 40}

There are no indexes.

So this is not allowed:

print(numbers[0])

❌ It gives an error because sets don't support indexing.

'''

'''
Now let's learn how to add an element.

Suppose we have:

numbers = {10, 20, 30}

To add a new element:

numbers.add(40)

Now the set becomes:

{10, 20, 30, 40}

Notice it's add(), not append() like lists.
'''

print(numbers)
numbers.add(6)
print(numbers)


numbers = {10, 20, 30}
numbers.add(20)
# will it be 10,20,20,30 or 10,20,30
# let's see

print(numbers)

# it prints 10,20,30 -- not allowing duplicates

# we can create a empty set and we can add numbers using add()

nums=set() # initializing empty set

nums.add(10)
nums.add(20)
nums.add(30)
nums.add(40)

print(nums)

# as set is unordered it doesn't have indexes.

