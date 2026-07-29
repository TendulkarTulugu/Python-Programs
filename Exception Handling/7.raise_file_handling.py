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


