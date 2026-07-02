'''
Problem 3 (Lists + Functions)

Now let's combine functions and lists.

Write a function:

Rules
Don't use max()
Use a loop
Return the largest number

'''
def find_largest(nums):
    large=nums[0]
    for i in nums:
        if i>large:
            large=i
    return large

numbers = [10, 45, 7, 92, 31]
print(find_largest(numbers))



'''
⭐ Interview Question

What if I call:

find_largest([])

What happens?

Think for a second.

The first line is:

large = nums[0]

But the list is empty.

Python will give:

IndexError: list index out of range

That's why, in real-world programs, we often write:

def find_largest(nums):
    if len(nums) == 0:
        return None

    large = nums[0]

    for i in nums:
        if i > large:
            large = i

    return large

We haven't learned len() formally yet, so don't worry about it now. 
I just wanted you to know why professionals often add extra checks.
'''
