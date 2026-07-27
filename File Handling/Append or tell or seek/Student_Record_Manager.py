'''
🏆 Mini Project

Let's build something that uses almost everything you've learned.

📚 Student Record Manager

Menu:

1. Add Student
2. View Students
3. Search Student
4. Exit
Requirements
1️⃣ Add Student

Ask:

Enter Name:
Enter Age:
Enter Course:

Store like:

Rahul,21,Data Science
Priya,22,AIML

Use:

with open()
"a"
2️⃣ View Students

Read and display all students.

Use:

with open()
"r"
3️⃣ Search Student

Ask:

Enter Name:

Read the file line by line.

If found:

Student Found:
Rahul,21,Data Science

Otherwise:

Student Not Found

Use:

readlines() or a loop
strip()
split(",")
if
4️⃣ Exit

End the program.

⭐ Challenge Rules

I want you to write it.

❌ Don't ask me for the code immediately.
✅ Try it yourself first.
✅ If you get an error, show me the error.
✅ If the logic doesn't work, we'll debug it together.

That's how you've learned everything so far.
'''


# while True:
#     choice=int(input('Choose 1. Add students 2. view students 3. search students 4. Exit'))
#     if choice==1:
#         print('Adding student')
#         name=input('Enter name:')
#         age=input('Enter age:')
#         course=input('Enter course:')
#         file=open('File Handling\Append or tell or seek\Student_Record_Manager.txt','a')
#         file.write(name+',')
#         file.write(age+',')
#         file.write(course+'\n')
#         print('Added')
#         file.close()
#     # here the code runs and adds the perfectly.
#     elif choice==2:
#         print('Displaying student details')
#         file=open('File Handling\Append or tell or seek\Student_Record_Manager.txt','r')
#         # file.seek(0) # it's unecessary bcz when we open using r the cursor automatically moves to starting point
#         print(file.read())
#         file.close()
#     elif choice==3:
#         search_key=input('Enter student name:').strip()
#         file=open('File Handling\Append or tell or seek\Student_Record_Manager.txt','r')
#         for line in file:
#             if search_key in line.split(','):
#                 file.readline()
#             else:
#                 print('Student Not Found')
#         file.close()
#     # the searching throws the error.
#     elif choice==4:
#         print('Exiting')
#         break
#     else:
#         print('Make a correct choice')



while True:
    print("\n===== Student Record Manager =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\n--- Add Student ---")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        with open("File Handling\\Append or tell or seek\\Student_Record_Manager.txt", "a") as file:
            file.write(f"{name},{age},{course}\n")

        print("Student Added Successfully!")

    elif choice == 2:
        print("\n--- Student Records ---")

        with open("File Handling\\Append or tell or seek\\Student_Record_Manager.txt", "r") as file:
            data = file.read()

            if data:
                print(data)
            else:
                print("No student records found.")

    elif choice == 3:
        print("\n--- Search Student ---")
        search_key = input("Enter Student Name: ").strip()

        found = False

        with open("File Handling\\Append or tell or seek\\Student_Record_Manager.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")

                if search_key.lower() == data[0].lower():
                    print("\nStudent Found")
                    print(f"Name   : {data[0]}")
                    print(f"Age    : {data[1]}")
                    print(f"Course : {data[2]}")
                    found = True
                    break

        if not found:
            print("Student Not Found")

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Choice. Please try again.")