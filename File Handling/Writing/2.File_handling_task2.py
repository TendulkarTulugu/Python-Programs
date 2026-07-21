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