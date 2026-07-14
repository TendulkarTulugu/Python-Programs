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
