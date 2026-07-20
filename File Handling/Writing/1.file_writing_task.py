'''
Create a file named student.txt.

The file should contain:

Name: Your Name
Age: Your Age
Degree: AI & DS

Each item should be on a separate line.

Rules
Use "w" mode.
Use three write() statements.
Close the file.

Don't use with open() yet—we'll learn that later.
'''

file=open('File Handling\Writing\student.txt','w')
file.write('Name: Tendul')
file.write('\nAge: 22')
file.write('\nDegree: AI & DS')
file.close()



'''
🟢 Problem 2 (Easy)

Now we'll combine writing and reading.

Task
Open student.txt in read mode.
Read the entire file.
Store it in a variable named content.
Print the content.
Close the file.
'''

file=open('File Handling\Writing\student.txt')
content=file.read()
print(content)
file.close()


