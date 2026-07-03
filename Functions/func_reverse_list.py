'''
🎯 Problem 3 — Reverse a List

You've reversed a string before.

Now let's reverse a list.


Rules
❌ Don't use:
reverse()
❌ Don't use:
[::-1]
✅ Use a loop.
✅ Return the reversed list.


'''


def reverse_list(nums):
    reversed_list=[]
    for n in nums:
        reversed_list.insert(0,n)
    return reversed_list

numbers = [10, 20, 30, 40]

print(reverse_list(numbers))


# there is another method to perform this code

def rev_list(nums):
    rev = []

    for i in range(len(nums)-1, -1, -1):
        rev.append(nums[i])

    return rev

print(rev_list(numbers))