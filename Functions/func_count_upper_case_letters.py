
'''
Count Uppercase Letters

Write a function:


Rules
Use a loop.
Use return.
Don't use any built-in counting functions.

'''

def count_upper(text):
    count=0
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                count+=1
    return count

print(count_upper('PyTHon'))


# isalpha() is not needed as isupper() also checks whether its a alphabet or not

def count_upper(text):
    count=0
    for ch in text:
        if ch.isupper():
            count+=1
    return count

print(count_upper('PyTHon@752'))