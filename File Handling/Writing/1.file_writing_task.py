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


'''
Task

Write a program that:

Opens student.txt
Reads the entire content into a variable called content
Prints the number of characters in the file
Closes the file
'''

file=open('File Handling\Writing\student.txt')
content=file.read()
print(len(content))
file.close()


'''
Task

Print the file line by line with line numbers.

If student.txt contains:

Name: Tendul
Age: 22
Degree: AI & DS

The output should be:

1. Name: Tendul
2. Age: 22
3. Degree: AI & DS

Rules
✅ Use a for loop.
✅ Don't use readlines(). (This is intentional.)
✅ Don't use indexing.
✅ Use a counter variable.
'''

file=open('File Handling\Writing\student.txt')

count=1
for line in file:
    print(count,line.strip())
    count+=1
file.close()

'''
Now let's make it a little more interesting.

Task

Print only the last line of student.txt.

Rules
❌ Don't use readlines()
❌ Don't use indexing ([-1])
✅ Use only a for loop.
✅ Use only one extra variable.
Example

If the file contains:

Name: Tendul
Age: 22
Degree: AI & DS

Output:

Degree: AI & DS
'''

file=open('File Handling\Writing\student.txt')

count=1
l_line=''
for line in file:
    l_line=line

print(l_line)

#-- better to use print(l_line.strip())

file.close()


