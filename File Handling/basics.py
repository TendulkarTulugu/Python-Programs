#1


'''
This is where Python starts interacting with the real world.

Until now, everything was inside the program.

Now we'll learn how to:

📖 Read data from files
✍️ Write data to files
➕ Append new data
📊 Read datasets (very important for Data Science)
🤔 Why File Handling?

Imagine you have marks of 10,000 students.

Will you write:

marks = [90, 85, 76, 88, ...]

❌ No.

Instead, you'll have a file:

marks.txt

or

students.csv

Your Python program reads the file.

This is exactly what Data Scientists do with datasets.

🟢 Step 1: Opening a File

Python uses:

open()

Syntax:

file = open("sample.txt")

This opens the file.

🟢 Step 2: Reading a File

file = open("sample.txt")

print(file.read())

Suppose sample.txt contains:

Hello Tendul
Welcome to Python

Output:

Hello Tendul
Welcome to Python

🟢 Step 3: Closing the File

Always close the file after using it.

file.close()

So the complete program becomes:

file = open("sample.txt")

print(file.read())

file.close()

🧠 Think of It Like a Notebook

Imagine a notebook.

Open it 📖
Read the pages 👀
Close it 📕

Exactly the same idea.
'''
import os

print("Current Working Directory:", os.getcwd())
print("Files in current folder:", os.listdir())

# # file=open("sample.txt") -- it doesn't retrive the output as the path is not correct.

# file = open(r"D:\OneDrive\Desktop\Python\Python\File Handling\sample.txt") -- it can retrive the data.
# print(file.read()) -- it reads the data
# file.close() --- it closes the file.

'''
here i have a folder named python.

in that folder i have multiple folders like basics,loops,etc.. file handling too.

as now i was working in file handling folder i created the sample.txt in file handling folder.

but the path is D:\OneDrive\Desktop\Python\Python> upto there.

so it doesn't access the file. so it throws error.

file=open(r'File Handling\sample.txt') 

i used this to retive the data from another folder from the current path.

'''



file=open(r'File Handling\sample.txt') # it is the best way to retrive
print(file.read())
file.close()


# there is another way to work the same

import os

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "sample.txt")

file = open(file_path)
print(file.read())
file.close()

'''
🎯 One More Tip

Instead of:

file = open(...)
print(file.read())
file.close()

Modern Python prefers:

with open(r"File Handling\sample.txt") as file:
    print(file.read())

Why?

Because with automatically closes the file, even if an error occurs.

We'll learn with properly after you understand open(), read(), write(), and append().
'''
