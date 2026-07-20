'''
Until now, we've only read data.

sample.txt
│
├── Apple
├── Banana
└── Mango

We could see what's inside.

But what if we want Python to create a file?

Or save results?

Or generate a report?

Or log errors?

That's where writing comes in.

Why do we write files?

Imagine you wrote this program:

marks = [90, 85, 78]
average = sum(marks) / len(marks)

print(average)

Output:

84.33

As soon as you close the program...

💨 It's gone.

If you want to save it permanently:

Student Report

Average = 84.33

you need file writing.

Opening a File for Writing

Last time we did:

file = open("sample.txt")

Python assumed read mode.

Now we'll specify the mode.

file = open("sample.txt", "w")

Notice the "w".

It means:

Open this file for writing.

What does "w" do?

Think of it like a blank notebook.

Notebook

Apple
Banana
Mango

You decide to erase everything and start fresh.

After opening with "w":

Notebook

(empty)

The old content is removed immediately.

That's an important point:

Opening a file in "w" mode clears its existing contents.

Your First Write
file = open("sample.txt", "w")

file.write("Hello Python")

file.close()

Now open sample.txt.

It contains:

Hello Python

The previous content is gone.

'''

file = open("File Handling\Writing\sample.txt")
print(file.read()) # -- it used to read only the file.
# and print whats inside the file
file.close()

#-- it erases the content in the file once we open using this 'w' format
file = open("File Handling\Writing\sample.txt", "w") 
#-- it starts writing in the file what we gave and it save as it is.
result=file.write("Hello Python") 
#-- it shows the length of the input
print(result) 
#-- it'll close the file.
file.close() 

'''
Two things happen:

Python writes "Hello" into the file.
write() returns the number of characters written.

Since:

Hello

has 5 characters.

it's similar to the len() function
'''


'''
 SyntaxWarning: invalid escape sequence '\W'
  file = open("File Handling\Writing\sample.txt", "w") #-- it erases the content in the file once we open using this 'w' format
'''



'''
🧠 Important Interview Question

Question: What does file.write() return?

Answer: It returns the number of characters written to the file as an integer.

This is a common Python interview question.
'''

file = open("File Handling\Writing\sample.txt", "w")

a = file.write("ABC")
b = file.write("DEF") #-- it dont overwrite the ABC. it adds next to it.

# the file contains ABCDEF not in 2 lines. if we want in new line we need to use escape sequence \n.

print(a)
print(b)

file.close()


file = open("File Handling\Writing\sample.txt", "w")

file.write("Python")
file.write("\n")
file.write("Data Science")
file.write("\n")
file.write("AI")

# -- now it writes in different lines as we used \n
file.close()




'''
Important Concept: The File Cursor

There's a hidden pointer called the file cursor.

Imagine it like a pen writing in a notebook:

Python|

After writing \n, the pen moves down:

Python
|

Then it continues writing from there.
'''


file = open("File Handling\Writing\sample.txt", "w")

file.write("Python")
file.write("\nAI")
file.write("\n")
file.write("Data")

file.close()