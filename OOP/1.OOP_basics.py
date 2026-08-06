'''
I'm not going to start with:

"A class is a blueprint..."

Because everyone memorizes that and still doesn't understand OOP.

Instead, let's start with a problem.

Imagine this...

Suppose you're making a Student Management System.

Without OOP, using only what you've learned so far, you might write:

student1_name = "Rahul"
student1_age = 20
student1_course = "Python"

student2_name = "Priya"
student2_age = 21
student2_course = "Java"

student3_name = "Amit"
student3_age = 22
student3_course = "Data Science"

Now imagine there are 10,000 students.

🤔 Question for you:

What problems do you see with this approach?

Don't think about OOP yet.

Just tell me:

Why is this a bad design?
What difficulties will the programmer face?

This answer is the reason OOP was invented. Once you identify the problem yourself,
the solution (classes and objects) will feel natural.



# 10000 different variables need to memorize the var to call the value.
'''




#---------------------------------------------------------------------------------------------------------------

'''
Imagine writing:

student7845_name
student7845_age
student7845_course

student7846_name
student7846_age
student7846_course

That's a nightmare.

But that's not the only problem.

Let's think a little deeper.

Suppose I ask you:

Print all student names.

You have:

student1_name = "Rahul"
student2_name = "Priya"
student3_name = "Amit"
...
student10000_name = "Kiran"
Question:

Can you use a for loop like this?

for name in ?????:
    print(name)

🤔 Where are all these names stored?

In a list?
In a dictionary?
Somewhere else?

❌ No.

They're just independent variables.

So you can't easily process them together.

Another Problem

Suppose Rahul changes his course.

You have to remember:

student1_course = "Java"

If you accidentally type:

student2_course = "Java"

😅 Oops! You updated Priya instead of Rahul.

One More Problem

Each student has related information:

Rahul
20
Python

These three values belong together.

But Python sees them as:

student1_name
student1_age
student1_course

Three completely separate variables.

There's no relationship between them.

So far we've found 4 problems

✅ 1. Too many variables.

✅ 2. Hard to remember variable names.

✅ 3. Can't easily process all students using loops.

✅ 4. Related data is scattered across multiple variables.

Now let's think like software engineers.

Suppose I ask you:

"A student has a name, age, and course."

Instead of creating three separate variables, can we create one thing called a Student, and keep all of its information together?

Something like:

Student
├── Name
├── Age
└── Course

Don't think about Python syntax yet.

Just answer this:

Does keeping all information about one student together seem like a better idea than creating separate variables? Why?

This is the exact thought process that led to the invention of objects.
'''






'''
To access the information we can just call the student variable to see all the information.

✅ Correct.

For example, instead of this:

student1_name = "Rahul"
student1_age = 20
student1_course = "Python"

We'd like to have something like:

Student
├── Name   : Rahul
├── Age    : 20
└── Course : Python

Now, whenever we talk about Rahul, all of his information stays together.

Think of your phone contacts 📱

How is a contact stored?

Not like this:

contact1_name
contact1_number
contact1_email
contact1_address

Instead, your phone stores:

Rahul
├── Phone
├── Email
├── Address

One contact contains all related information.

A Student is exactly the same idea.

Another Huge Advantage

Suppose you have:

Rahul
├── Age
├── Course
├── Marks
├── Phone
├── Address

If I say:

"Print Rahul's details."

You don't have to remember 6 different variable names.

You simply access Rahul, and everything related to Rahul is available.

So, why was OOP invented?

Let's summarize the problems we found.

Without OOP:

❌ Thousands of variables

❌ Hard to remember names

❌ Related data is scattered

❌ Difficult to manage large programs

With OOP:

✅ Related data stays together

✅ Easy to manage

✅ Easy to create many students

✅ Easy to update and access information

Now comes the most important idea in OOP.

Imagine I tell you:

"Every student has a Name, Age, and Course."

Is that describing:

One particular student (like Rahul)?
Or is it describing what every student should look like?

🤔 Think carefully.

For example:

Student
├── Name
├── Age
└── Course

Is this Rahul?

Or is it just a general description of a student?

This answer is the key to understanding the difference between a Class and an Object, which is the foundation of OOP.

'''




'''
General description of every student.

✅ Correct.

Let's build the concept.

Suppose I say:

Student
├── Name
├── Age
└── Course

Is this Rahul?

❌ No.

Is this Priya?

❌ No.

Is this Amit?

❌ No.

It's simply describing:

"What information every student should have."

This is called a Class.

Now imagine this.

We have a template.

Student
├── Name
├── Age
└── Course

Using this template, we create:

Rahul
├── Name : Rahul
├── Age  : 20
└── Course : Python

Again, using the same template:

Priya
├── Name : Priya
├── Age  : 21
└── Course : Java

Again:

Amit
├── Name : Amit
├── Age  : 22
└── Course : Data Science

Notice something?

The structure is the same.

Only the values change.

This is the first big OOP idea.
Class

A Class is a template or design.

Example:

Student
├── Name
├── Age
└── Course

It doesn't represent a real student.

Object

An Object is one real student created using that template.

Example:

Rahul
├── Name : Rahul
├── Age : 20
└── Course : Python

Rahul is an object.

Priya is another object.

Amit is another object.

Real-Life Analogy 🏠

Think of an apartment building.

Blueprint
2 Bedrooms
1 Kitchen
1 Hall
2 Bathrooms

This is just a design.

Can you live inside a blueprint?

❌ No.

Now the builder constructs:

House 101

House 102

House 103

Each house follows the same blueprint, but each one has different owners and furniture.

The blueprint is the Class.

Each house is an Object.

Another Analogy 🚗

Car Design

Car
├── Engine
├── Wheels
├── Seats

This is the Class.

Real cars:

My Car 🚗
Your Car 🚗
Taxi 🚕
Police Car 🚓

These are Objects.
'''




'''
⭐ This is the first definition I'll let you memorize.

Most definitions I don't want you to memorize.

But this one is important because you now understand it.

Class

A Class is a blueprint or template that defines the properties and behavior of objects.

Object

An Object is a real instance created from a class.

Notice I didn't give you these definitions first.

We derived them from the student example.

That's why they'll stick.
'''



# 🚀 Now let's write your FIRST class.

class Student:  # student is the name if the class.
    pass

# this contains only 1 class and no objects in this.
print(Student)  # while printing we think it prints nothing as it only contains pass statement


'''
But the correct output is:

<class '__main__.Student'>

or in some environments:

<class 'Student'>




Why?

Remember:

print(10)

prints an integer object.

print("Hello")

prints a string object.

Similarly,

print(Student)

prints the class object itself.

Python says:

"This is the class named Student."

Think of it like Functions

Suppose you write:

def hello():
    pass

print(hello)

Does Python call the function?

❌ No.

It prints something like:

<function hello at 0x...>

Because you're printing the function object, not calling it.

Similarly:

print(Student)

prints the class, not an object of that class.
'''


