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