'''
What is Append Mode?

Append mode is used when you want to add new data to the end of a file without deleting the existing contents.

Syntax:

file = open("sample.txt", "a")
Think About This

Suppose sample.txt already contains:

Rahul
Priya

Now you write:

file = open("sample.txt", "a")
file.write("Amit")
file.close()


Remember:

"w" starts writing from the beginning and erases everything.
"a" behaves differently.


When you open it in append mode:

Python doesn't erase the file.

Instead, it automatically places the file cursor at the end of the file.

append mode is designed to add data.

If there is no file to add to, Python simply creates one.

'''


# tell()

'''
What does tell() do?

tell() tells you the current position of the file cursor.

Think of the cursor as a blinking pointer inside the file.
'''

'''
For example, if the file contains:

Python

Internally, imagine it like this:

P y t h o n
0 1 2 3 4 5

When you first open it in read mode:

file = open("sample.txt", "r")

the cursor starts at the beginning:

|Python

Now:

print(file.tell())

prints:

0

because the cursor is at position 0.

Now suppose you do:

file.read(2)

Python reads:

Py

The cursor moves:

Py|thon

Now:

print(file.tell())

prints:

2

because the cursor has moved 2 characters.
'''
