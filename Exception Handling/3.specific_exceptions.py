'''
So far we've used:

except:

This catches every exception.

But in real-world Python, this is generally not recommended.

Imagine this code:

try:
    num = int(input("Enter a number: "))
    print(100 / num)

except:
    print("Something went wrong")

If the user enters:

abc

It prints:

Something went wrong

If the user enters:

0

It also prints:

Something went wrong

But these are two completely different problems:

abc → ValueError
0 → ZeroDivisionError

As a programmer, you often want to respond differently to each one.
'''

