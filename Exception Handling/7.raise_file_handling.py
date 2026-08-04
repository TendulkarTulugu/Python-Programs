# case 1
try:
    print("A")

finally:
    print("B")

print("C")



# #case 2
# try:
#     print("A")
#     10 / 0

# finally:
#     print("B")

# print("C")

#  case 2 raises error as there is an error that is zero division error to handle it there is no except block in there.

'''
There is no except block to handle it.

Normally, the program would crash...

But before Python leaves the try statement, it checks:

"Is there a finally block?"

✅ Yes.

'''



'''
After finally finishes, Python looks again.

Is the exception handled?

❌ No.

There was no except.

So the original ZeroDivisionError is raised.

The program crashes.
'''




'''
⭐ Very Important Rule

A finally block does not catch exceptions.

It only guarantees:

"Execute me before leaving the try statement."

If the exception isn't handled by an except, it continues after finally finishes.

Think of it like this:

try
 │
 ├── Exception occurs
 │
 ▼
finally   ← Always runs
 │
 ▼
Was exception handled?
 │
 ├── Yes → Continue program
 └── No  → Program crashes

'''




'''
Until now, Python has been raising exceptions for us.

For example:

10 / 0          # Python raises ZeroDivisionError
int("abc")      # Python raises ValueError

But what if you want to raise an exception?

Example:

age = -5

A negative age doesn't make sense.

Python won't complain:

print(age)

Output:

-5

But you might want your program to reject it.

That's where raise comes in.

You can tell Python:

"This value is invalid. Raise an exception."
'''


# age = -10

# if age < 0:
#     raise ValueError("Age cannot be negative") # raises the value error as the condition satisfies.

# print("Valid Age") # won't execute as the error raised
# # Because raise immediately stops normal execution (unless the exception is caught by a try-except).



'''
Python checks:

if age < 0:

Is -10 < 0?

✅ Yes.

So Python executes:

raise ValueError("Age cannot be negative")

Now you are telling Python:

"Stop the program and create a ValueError with this message."

It's exactly like Python does with:

10 / 0

Python internally does something similar to:

raise ZeroDivisionError("division by zero")

or with

int("abc")

Python internally raises:

raise ValueError("invalid literal for int()...")

The difference is:

Before → Python raised the exception.
Now → You are raising the exception.

'''


'''
⭐ Golden Rule

raise creates an exception.

except catches an exception.

Think of them as opposites.

raise  ─────────► Creates an exception 🚨

except ◄──────── Handles the exception 🛠️
'''


# now let's combine raise and try-except

try:
    age = -10

    if age < 0:
        raise ValueError("Negative Age")

    print("Valid")

except ValueError:
    print("Invalid Age")

print("Program End")


'''

raise valueerror

creates an exception with the message "Negative Age", 
but the message is not printed automatically when the exception is caught.

The except block decides what to do.

'''



'''
🤔 Now you might ask...

"Then what's the use of writing 'Negative Age' inside raise?"

Excellent question!

The message is stored inside the exception object.
'''


# If you want to print it, you have to capture the exception.

try:
    age = -10

    if age < 0:
        raise ValueError("Negative Age")

except ValueError as e:
    print(e)

print("Program End")

# this will catch the error and prints the error.

'''
Notice the difference:

except ValueError: → You ignore the message.
except ValueError as e: → You capture the exception object, and e contains the message.
'''



'''
⭐ Think of e like a box 📦
ValueError Object
┌────────────────────────────┐
│ Type    : ValueError       │
│ Message : Age cannot be... │
└────────────────────────────┘
            │
            ▼
            e

When you write:

except ValueError as e:

e is just a variable name.

You could also write:

except ValueError as error:

or

except ValueError as ex:

All of these are valid.
'''
print('--------') # seperating the blocks

try:
    raise ValueError("First Error")

except ValueError as e:
    print(type(e))
    print(e)




# try:
#     raise ValueError("Error 1")

# except ValueError as e:
#     print(e)
#     raise

# print("End")

# 💡 This is called re-raising an exception, and it's another favorite interview question.

'''
⭐ Golden Rule

There are two forms of raise.

1. Raise a new exception

raise ValueError("Invalid Input")

Creates a brand-new exception.

2. Re-raise the current exception

except ValueError:
    raise

Raises the same exception again.

This is useful when you want to:

Log the error
Perform cleanup
Let another part of the program handle it

'''
