'''
Topic 1: with open(...) as file

This is the professional and most commonly used way to work with files.

Until now we've written:

file = open("sample.txt")

content = file.read()

file.close()

It works perfectly.

But there's one problem.

🤔 Think about this

Suppose we write:

file = open("sample.txt")

print(file.read())

10 / 0

file.close()
Question

What happens here?

Notice carefully:

10 / 0

comes before

file.close()

Think about it.
'''

file = open("File Handling\Append or tell or seek\sample.txt")

print(file.read())

# 10 / 0 # -- raises zero division error and terminates the program without closing the file in the next line

file.close()


'''
10/0

Python raises:

ZeroDivisionError

The program stops here.

❌ Step 4

file.close()

This line is never executed.

So the file remains open until Python cleans it up later. 

In small programs this usually isn't noticeable, but in larger applications, 
repeatedly leaving files open can waste system resources or cause other issues.
'''

'''
Python gives us a special statement:

with open(...) as file:
'''

with open("File Handling\Append or tell or seek\sample.txt") as file:
    print(file.read())


'''
look here we don't used the file.close()

but it closes the file. 

Python automatically closes the file when the with block finishes, even if an exception occurs.
'''

'''
with

it makes a promise:

"I'll take care of opening the file, and I'll make sure it's closed when you're done—even if something goes wrong."
'''

'''
So internally, it's similar to this idea:

file = open("sample.txt", "r")

try:
    print(file.read())
finally:
    file.close()

Don't worry about try and finally yet—we'll learn them in Exception Handling. 
For now, just know that with ensures close() is always called.
'''

# with open("File Handling\Append or tell or seek\sample.txt", "r") as file:
#     print(file.read())
#     10 / 0

# print("Program End")


'''
⭐ Interview Question

Why do Python developers prefer:

with open(...)

instead of

file = open(...)
...
file.close()
Expected answer:

with open() automatically closes the file after the block finishes, 
even if an exception occurs. It prevents resource leaks and makes the code cleaner and safer.

'''
