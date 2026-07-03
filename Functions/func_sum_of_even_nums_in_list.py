'''
🎯 Problem 2 — Sum of Even Numbers

Write a function:

def sum_even(nums):


to find sum of even numbers in the list

Rules
❌ Don't use sum()
✅ Use a loop
✅ Return the answer

'''

def sum_even(nums):
    sum=0
    for n in nums:
        if n%2==0:
            sum+=n
    return sum

numbers = [10, 3, 8, 5, 2]

print(sum_even(numbers))

