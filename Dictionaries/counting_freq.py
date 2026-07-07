#5

'''
🎯 Problem: Frequency of Elements

Remember this?

numbers = [1, 2, 1, 3, 2, 1]

before we wrote:

count_1 = 0
count_2 = 0
count_3 = 0

It worked...

But only for 1, 2, and 3.

🤔 Think About This

Suppose I give you:

numbers = [10, 20, 10, 50, 30, 20, 10]

Can you write:

count_10
count_20
count_30
count_50

Yes.

Now suppose I give you 1000 different numbers.

😅 Impossible.

⭐ Dictionary to the Rescue

Instead of this:

count_1 = 3
count_2 = 2
count_3 = 1

We'll store everything in one dictionary.

Like this:

frequency = {
    1: 3,
    2: 2,
    3: 1
}

See how neat it is?

🧠 The Logic

Let's solve it together.

Initially:

frequency = {}

This means:

{}

An empty dictionary.

Read the first number
1

Is 1 already a key in the dictionary?

No.

So create it.

frequency[1] = 1

Dictionary becomes:

{
    1: 1
}
Read the second number
2

Already present?

No.

Create it.

frequency[2] = 1

Now:

{
    1: 1,
    2: 1
}
Read the third number
1

Already present?

✅ Yes.

So instead of creating it again:

Increase its count.

frequency[1] += 1

Now:

{
    1: 2,
    2: 1
}

Continue...

Eventually we get:

{
    1: 3,
    2: 2,
    3: 1
}
🎯 Your Challenge

Write this function:

def frequency(nums):
Rules

Use:

frequency = {}

Think about this question:

How do I check whether a key already exists in a dictionary?

💡 Hint:

Just like we checked:

if ch in vowels:

Can we check:

if num in frequency:

🤔
'''

def count_freq(nums):
    frequency={}
    for i in nums:
        if i not in frequency:
            frequency[i]=1
        elif i in frequency:
            frequency[i]+=1
    return frequency

numbers = [10, 20, 10, 50, 30, 20, 10]

print(count_freq(numbers))

'''
this runs perfectly.

Today your program works for:

[10, 20, 10, 50, 30, 20, 10]

or

[100, 500, 700, 100, 999]

or even

[9999, -5, 0, 9999]

without changing a single line.

That's the power of dictionaries.


even this logic also works

if i not in frequency:
    frequency[i] = 1
else:
    frequency[i] += 1


'''


# another challenge

'''
🎯 Challenge (No Hints)

Can you modify your function so that instead of returning:

{10: 3, 20: 2, 50: 1, 30: 1}

it prints:

10 -> 3
20 -> 2
50 -> 1
30 -> 1

Hint: You'll need to loop through the dictionary.
'''
def count_freq(nums):
    frequency={}
    for i in nums:
        if i not in frequency:
            frequency[i]=1
        elif i in frequency:
            frequency[i]+=1
    for key in frequency:
        print(key,'->',frequency[key])

numbers = [10, 20, 10, 50, 30, 20, 10]

print(count_freq(numbers))

'''
here the print statement at last calls everything in the function and printing inside the function

and at last after calling we are printing so it returns None

to overcome this simply calling the function can validate and remove the None at the ending

'''

def count_freq(nums):
    frequency={}
    for i in nums:
        if i not in frequency:
            frequency[i]=1
        elif i in frequency:
            frequency[i]+=1
    for key in frequency:
        print(key,'->',frequency[key])

numbers = [10, 20, 10, 50, 30, 20, 10]

count_freq(numbers)

# now it returns without None