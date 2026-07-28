'''
What is an Exception?

Look at this program.
'''
num = int(input("Enter a number: "))
print(num * 2)
print("Program Finished")

'''
Case 1

Input:

25

Output:

Enter a number: 25
50
Program Finished

Everything works.
'''

'''
Case 2

Input:

hello

Now Python tries to execute:

int("hello")

Can Python convert "hello" into an integer?

❌ No.

So Python immediately stops the program and shows something like:

ValueError: invalid literal for int() with base 10: 'hello'

Notice something important.

The next line:

print(num * 2)

never runs.

Neither does:

print("Program Finished")

The entire program crashes.
'''



'''
What just happened?

A programmer writes a program expecting:

Input → Process → Output

But users don't always do what we expect.

Example:

Expected:

Age:
22

User enters:

twenty two

Expected:

Choice:
1

User enters:

apple

Expected:

Number:
10

User enters:

@

Programs must handle these situations.
'''

# Definition

# An exception is an error that occurs while the program is running (at runtime), 
# causing the normal flow of the program to stop unless it is handled.

# Notice the words "while the program is running."

# That's different from a syntax error.


'''
Syntax Error vs Exception
Syntax Error

print("Hello"

Python won't even start the program.

It immediately says:

SyntaxError

because the code itself is invalid.

Exception

num = int(input())

The code is perfectly correct.

The problem happens after the program starts, depending on what the user enters.
'''



'''
Think of it like driving 🚗

You're driving on a road.

Everything is normal.

Suddenly...

A dog runs across the road.

Is the road broken?

❌ No.

Did something unexpected happen while driving?

✅ Yes.

You don't throw away the car.

You react.

Exceptions are exactly that.

Your program needs a way to react instead of crashing.
'''

