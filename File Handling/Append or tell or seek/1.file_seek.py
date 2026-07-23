'''
📚 File Handling - seek()

You've already learned:

tell() → "Where is the cursor now?"
seek() → "Move the cursor to a specific position."


Syntax
file.seek(position)

Example:

file.seek(0)

Moves the cursor to the beginning of the file.

'''



'''
Why is seek() useful?

Imagine you already read a file:

file = open("sample.txt")

print(file.read())

Output:

Python

Now you try:

print(file.read())

What do you think happens?

Nothing is printed.

Why?

Because after the first read(), the cursor is already at the end of the file.

Instead of closing and reopening the file, you can simply do:

file.seek(0)

Now the cursor goes back to the beginning, and you can read the file again.
'''


file = open("File Handling\Append or tell or seek\sample.txt")

print(file.read(6)) #-- print first 6 characters

print(file.tell()) #-- prints where the cursor was.

file.seek(7) #-- Cursor moves to the 7th position

print(file.read()) #-- Reads from the current cursor upto the end.

file.close() #-- closes the file.