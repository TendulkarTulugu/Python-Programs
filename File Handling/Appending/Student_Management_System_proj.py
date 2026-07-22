'''
🎯 Next Challenge (A Little More Realistic)

Let's build a tiny feature.

Problem 8

Create a menu-driven program:

1. Add Student
2. View Students
3. Exit

Requirements:

If the user chooses 1, ask for one student name and save it.
If the user chooses 2, display all student names with line numbers.
If the user chooses 3, end the program.
❓Challenge

Think carefully before coding.

You've already noticed that opening a file with "w" deletes the existing data.

So if the user chooses 1 multiple times, what file mode should you use so the old names are preserved and the new one is added?

'''
while True:
    choice=int(input('Choose 1 for Add Student or 2 for View Students or 3 for Exit: '))   
    if choice==1:
        print('Adding student')
        student=input('Enter student name:')
        file=open('File Handling\Appending\sample.txt','a')
        file.write(student+'\n')
        print('Added')
        file.close()
    elif choice==2:
        print('Displaying student choice')
        file2=open('File Handling\Appending\sample.txt')
        count=1
        for line in file2:
            print(count,'.',line.strip(),sep='')
            count+=1
        file2.close()
    elif choice==3:
        print('Exiting')
        break
    else:
        print('Invalid choice. Please try again.')
    