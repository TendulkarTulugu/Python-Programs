'''
Problem 1

Without looking at old code, write:

def char_frequency(text):

Example:

print(char_frequency("banana"))

Expected Output:

b -> 1
a -> 3
n -> 2
Rules
✅ Use a dictionary.
✅ Don't use count().
✅ Use the frequency logic you learned.
'''

def char_frequency(text):
    frequency={}
    for ch in text:
        if ch in frequency:
            frequency[ch]+=1
        elif ch not in frequency:
            frequency[ch]=1
    return frequency

print(char_frequency("banana"))