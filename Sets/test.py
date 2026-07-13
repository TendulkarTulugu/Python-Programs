#4

'''
Without looking at your old code, write this function:

def remove_duplicates(nums):

Example:

numbers = [10, 20, 10, 30, 20, 40]

print(remove_duplicates(numbers))

Expected Output:

{10, 20, 30, 40}
Rules
✅ Use a set.
✅ Return the set.
❌ Don't use loops if you know a simpler way.

(Hint: Think about what a set automatically does.)
'''

def remove_duplicates(nums):
    n_set=set()
    for num in nums:
        n_set.add(num)
    return n_set

numbers = [10, 20, 10, 30, 20, 40]

print(remove_duplicates(numbers))