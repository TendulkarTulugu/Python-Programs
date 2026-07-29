'''
Question

Suppose your program has 10,000 lines.

The error occurs on line 50.

Should Python stop the remaining 9,950 lines?

Usually...

❌ No.

We want to recover.

Why Python Created try

Python gives us a protected area.
'''


'''
What does try actually mean?

When Python sees

try:

It silently says:

"I'm about to execute code that might fail."

Notice something.

It doesn't assume failure.

It simply prepares for it.
'''

'''
Example

try:
    print("Hello")

Nothing dangerous here.

It still works.

Because try doesn't create errors.

It only protects code.

'''



'''
Important Rule 1

try doesn't fix errors.

Many beginners think this.

Wrong.

It only says

"Watch this code carefully."


Important Rule 2

Only the code inside the try block is protected.
'''


'''
The moment an exception occurs inside a try block, Python immediately stops executing the remaining statements in that try block.
'''


'''
🧠 Golden Rules So Far

By now, you should remember these rules:

✅ try marks code that might raise an exception.
✅ If no exception occurs, the except block is skipped.
✅ If an exception occurs, Python immediately stops the rest of the try block.
✅ Python jumps to the matching except block.
✅ After except finishes, execution continues with the code after the try-except block.
'''






'''
⭐ Very Important Interview Question

Suppose I write:

print("Start")

try:
    print("Inside Try")

except:
    print("Inside Except")

print("End")
Question

Will Python execute this program?

Or will it give an error?

Take a moment and think before answering.
'''



'''
The correct answer is:

❌ No. The program will not execute.

Python gives an error before the program starts.

Look carefully
print("Start")

try:
    print("Inside Try")

except:
    print("Inside Except")

print("End")

At first glance, it looks fine because there is an except.

But ask yourself:

What is inside the try block?
print("Inside Try")

Will this line ever raise an exception?

❌ Probably not.

But that's not the problem.

The Real Problem

Python expects that a try block might raise an exception, but it also requires that the except block contains at least one executable statement.

Your except block contains:

print("Inside Except")

So this code is actually valid.

👉 I intentionally tricked you. 😄

The code will execute.

Output:

Start
Inside Try
End

Why?

try executes normally.
No exception occurs.
except is skipped.
Program continues after the try-except block.

But now look at this code:
try:
    print("Hello")

Will this execute?

Answer:

❌ No.

Python gives:

SyntaxError: expected 'except' or 'finally' block

Because a try block cannot exist by itself.

It must be followed by one of these:

except
finally
or both
Rule to Remember

✅ Valid:

try:
    print("Hello")
except:
    print("Error")

✅ Also valid:

try:
    print("Hello")
finally:
    print("Finished")

❌ Invalid:

try:
    print("Hello")
'''

# only the try: block wouldn't run independently it requires the except or finally blocks.


'''
⭐ A New Rule

This is an interview question too.

except is not a magical safe zone.

Many beginners think:

"Once I'm inside except, no more exceptions can happen."

❌ Wrong.

Exceptions can occur anywhere:

inside try
inside except
inside else
inside finally
inside functions
inside loops

If an exception occurs outside a protected try block, the program crashes.
'''



try:
    print("Outer Try") #-- prints

    try:
        print(10 / 0) # raises error so moves to nearest except block.

    except:
        print("Inner Except") #-- prints 

    print("After Inner") #-- exception resolved so it prints the line

except:
    print("Outer Except") #-- skips the line bcz the exceptions are handled so it skips this exception block

print("Program End") #-- prints the line at last.


'''
⭐ One Very Important Rule

An exception is first offered to the nearest except block.

If that except handles it, Python continues normally.

If it doesn't handle it, the exception moves outward to the next enclosing try.
'''



try:
    print("Outer Start") #-- prints the line

    try:
        print(10 / 0) #-- raises the error

    except:
        print("Inner Except") # exception occured so the block executes and print the line
        print(10 / 0) # raises the exception

    print("Outer Continue") # as exception raised the line get skipped.

except:
    print("Outer Except") #-- as exception raised the block executes and prints the line

print("Program End") # prints the line at last as the exceptions handled






