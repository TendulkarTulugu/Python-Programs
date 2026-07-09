#2

'''
New Method: remove()

Just like dictionaries had:

pop()

sets have:

remove()

Example:

numbers = {10, 20, 30, 40}

numbers.remove(20)

print(numbers)

Output:

{10, 30, 40}

20 is removed.

'''

numbers = {10, 20, 30}

# numbers.remove(50) # it throws the error

print(numbers)


'''
⭐ There is another method: discard()

Python gives us a safer alternative.'''

numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)

'''
Output:

{10, 20, 30}

No error.

Nothing happens.
'''
