# 1
'''
🎯 Today's Next Topic: Frequency of Elements

This is a very common interview question.

Suppose we have:

nums = [1, 2, 1, 3, 2, 1]

Expected Output:

1 -> 3
2 -> 2
3 -> 1

Meaning:

1 appears 3 times
2 appears 2 times
3 appears 1 time
❌ Don't Use
count()

or

collections.Counter
💡 Think About It

Suppose I ask:

"How many times does 1 appear?"

You already know how to do that:

count = 0

for n in nums:
    if n == 1:
        count += 1

Now the question becomes:

How do we do this for every unique number?

🤔

🎯 Challenge

Try writing a function:

def frequency(nums):
    ...

For now, don't worry if it prints duplicate results. Just try your own approach.

Example input:

numbers = [1, 2, 1, 3, 2, 1]

Try to produce something close to:

1 -> 3
2 -> 2
3 -> 1
'''

def count_frequency(nums):
    count_1=0
    count_2=0
    count_3=0
    for num in nums:
        if num==1:
            count_1+=1
        elif num==2:
            count_2+=1
        elif num==3:
            count_3+=1
    return f'\n 1-> {count_1}\n 2-> {count_2}\n 3-> {count_3}'

numbers = [1, 2, 1, 3, 2, 1]
print(count_frequency(numbers))


'''
It executes for here,

What if tomorrow I give you:

numbers = [5, 8, 10, 5, 8, 20, 5]

Now your code becomes:

count_5 = 0
count_8 = 0
count_10 = 0
count_20 = 0

😅

And what if there are 100 different numbers?

You'll need:

count_1
count_2
count_3
...
count_100

Impossible.

'''


'''
⭐ This Is Why We Need a New Data Structure

You're about to discover why dictionaries exist.

A dictionary can store:

frequency = {
    1: 3,
    2: 2,
    3: 1
}

Instead of creating:

count_1
count_2
count_3

you store everything in one variable.
'''




# tasks
'''
🎯 Before Our Next Session

Just one small practice (10–15 minutes):

Try writing these without looking at old code:

1. find_largest(nums)
2. find_smallest(nums)
3. reverse_list(nums)
4. search(nums, target)
5. count_vowels(text)

If you can write those from memory, you've truly understood the concepts.

'''

#1 

def largest(nums):
    large=nums[0]
    for num in nums:
        if num>large:
            large=num
    return large
numbers = [10, 45, 7, 92, 31]
print(largest(numbers))


#2
def smallest(nums):
    small=nums[0]
    for num in nums:
        if num<small:
            small=num
    return small
numbers = [10, 45, 7, 92, 31]
print(smallest(numbers))

#3 reverse a list
def reverse_list(nums):
    rev=[]
    for num in nums:
        rev.insert(0,num)
    return rev
numbers = [10, 45, 7, 92, 31]
print(reverse_list(numbers))

#4 search
def search(nums,target):
    for num in nums:
        if num==target:
            return 'Found'
    return 'Not Found'

numbers = [10, 45, 7, 92, 31]
print(search(numbers,92))

#5 count vowels
def count_vowels(text):
    text=text.lower()
    vowels='aeiou'
    count=0
    for ch in text:
        if ch in vowels:
            count+=1
    return count
result=count_vowels('Education')
print(result)