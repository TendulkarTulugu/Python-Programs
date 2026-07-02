'''
🎯 Next Challenge (Slightly Harder)

Write a function:

def second_largest(nums):

Example:

numbers = [10, 45, 7, 92, 31]

print(second_largest(numbers))

Output:

45
Rules
❌ Don't use sort()
❌ Don't use max()
✅ Use loops
✅ Return the second largest element
Hint (Only One)

Think about maintaining two variables:

largest = ?
second = ?

When you find a new largest number:

The old largest becomes second.
The new number becomes largest.

'''


def second_largest(nums):
    if len(nums)==0:
        return None
    second=nums[0]
    largest=0
    for i in nums:
        if second<i:
            second=i
    for j in nums:
        if largest<i and largest<second:
            largest=second
            second=i
    return largest,second

numbers = [10, 4, 7, 92, 31]

print(second_largest(numbers))



'''
Already, there is a small problem.

Suppose:

nums = [-10, -5, -2]

Then:

largest = 0

is wrong because 0 isn't even in the list.

A better initialization is:

largest = nums[0]
second = nums[0]

or another suitable initial value.

First Loop
for i in nums:
    if second < i:
        second = i

This actually finds the largest element, not the second largest.

For:

10 4 7 92 31

second becomes:

10
10
10
92
92

So after this loop:

second = 92

which is actually the largest.

Second Loop
if largest < i and largest < second:

Notice something?

You're using:

i

inside this loop:

for j in nums:

There is no i in this loop.

It should have been j.

This is a variable mix-up.

The Correct Logic

Imagine the list:

10 4 7 92 31

Keep two variables:

largest
second

Initially:

largest = 10
second = -∞

Read 4

largest = 10
second = 4

Read 7

largest = 10
second = 7

Read 92

New largest!

Old largest becomes second.

largest = 92
second = 10

Read 31

31 isn't larger than 92.

But it's larger than 10.

So:

largest = 92
second = 31

Done!

Answer:

92
31
'''



def second_largest(nums):
    largest = nums[0]
    second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second


numbers = [93,10, 45, 7, 92, 31]
print(second_largest(numbers))