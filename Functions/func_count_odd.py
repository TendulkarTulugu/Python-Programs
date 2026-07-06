'''
Rules
Use a loop.
Return the count.
Don't use any built-in functions.
'''


def count_odd(nums):
    count=0
    for num in nums:
        if num%2!=0:
            count+=1
    return count

numbers = [10, 15, 8, 7, 2, 5]

print(count_odd(numbers))