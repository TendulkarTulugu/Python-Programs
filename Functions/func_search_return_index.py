'''
🎯 Today's Main Problem

Let's make the search function a little better.

Instead of:

print(search(numbers, 92))

Output:

Found

I want:

Found at index 3

And if it's not there:

Not Found
Example
numbers = [10, 45, 7, 92, 31]

print(search_index(numbers, 92))

Output:

Found at index 3

Because:

Index	Value
0	10
1	45
2	7
3	92
4	31
Hint

You already know:

for num in nums:

Now think...

How can we also get the position (0, 1, 2, 3...) while looping?

Try to solve it without searching online. If you get stuck, I'll guide you one step at a time.

'''


def search(nums,target):
    
    for num in nums:
        # index=nums[num]
        if target==num:
            return f'Found at {nums.index(num)}'
    return 'Not Found'
numbers = [10, 45, 7, 92, 31]

print(search(numbers, 92))