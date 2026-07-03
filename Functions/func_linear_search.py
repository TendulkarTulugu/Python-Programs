'''
🎯 Next Challenge (One Step Up)

Write a function:

def search(nums, target):

Example:

numbers = [10, 45, 7, 92, 31]

print(search(numbers, 92))

Output:

Found

Another example:

print(search(numbers, 100))

Output:

Not Found
Rules
Don't use:
in
Use a loop.
Return "Found" or "Not Found".

'''

def search(nums, target):
    
    for n in nums:
        if target==n:
            return 'Found'
    return 'Not found'
numbers = [10, 45, 7, 92, 31]

print(search(numbers, 92))
