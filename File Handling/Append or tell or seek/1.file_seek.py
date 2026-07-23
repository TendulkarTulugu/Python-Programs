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


file = open("File Handling\Append or tell or seek\sample.txt")

print(file.readline())

file.seek(0)

print(file.readline())

file.close()

#------------------------

file = open("File Handling\Append or tell or seek\sample.txt")

data = file.readlines()
for name in data:
    print(name.strip())
print(len(data))
print(type(data))
file.close()


'''
Now let me ask you a few rapid-fire questions like an interviewer.

Q1

Which function returns a list?

Q2

Which function reads only one line?

Q3

Which mode deletes existing data?

Q4

Which mode adds data without deleting existing content?

Q5

What does tell() return?

Q6

What does seek(0) do?

Q7

What happens if you open a file in "a" mode and the file doesn't exist?
'''

