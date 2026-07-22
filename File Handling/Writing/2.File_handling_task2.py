'''
Now we're moving away from fixed data.

Task

Write a program that:

Asks the user to enter 5 student names using input().
Saves each name into students.txt.
Each name should be on a new line.
Example

Input:

Rahul
Priya
Amit
Neha
Kiran

The file should contain:

Rahul
Priya
Amit
Neha
Kiran
Rules
✅ Use a for loop.
✅ Use input().
✅ Use write().
✅ Don't hardcode the names.
✅ Don't ask me for the solution yet.
'''

file=open('File Handling\Writing\sample.txt','w')
for _ in range(5):
    data=input().strip()
    file.write(data+'\n')
file.close()



'''
Problem 7 (Slightly More Challenging)

Now let's combine writing and reading.

Task

Write a program that:

Takes 5 student names from the user.
Stores them in students.txt.
Closes the file.
Opens the same file in read mode.
Prints all the student names with line numbers.
Expected Output

If the user enters:

Rahul
Priya
Amit
Neha
Kiran

The final output should be:

1. Rahul
2. Priya
3. Amit
4. Neha
5. Kiran
Rules
✅ Use one for loop for writing.
✅ Use another for loop for reading.
✅ Remember to close the file before opening it again in read mode.
❌ Don't use readlines().
'''


file1=open('File Handling\Writing\sample.txt','w')
for _ in range(5):
    data=input().strip()
    file1.write(data+'\n')
file1.close()

file=open('File Handling\Writing\sample.txt')
count=1
for line in file:
    print(count,'.',line.strip(),sep='')
    count+=1
file.close()



