'''
Now comes the question you've probably been thinking about:

How does Rahul actually get the values "Rahul", 20, and "Python"?

Right now we only have:

rahul = Student()

This creates an empty object.

We'll learn the constructor (__init__), which lets us create objects like this:

rahul = Student("Rahul", 20, "Python")

and later access:

rahul.name
rahul.age
rahul.course

This is where OOP starts to become really powerful.
'''



class Student:
    pass

rahul = Student()       #creating the object.

print(rahul)   


'''
Does Python know that:

Name = Rahul
Age = 20
Course = Python
'''

# No, because we've only created an empty object. We haven't given it any data yet.


'''
We only said:

"Create one Student object."

We never said:

Name = Rahul
Age = 20
Course = Python

So Python creates something like this:

rahul
├── Name   → ❓
├── Age    → ❓
└── Course → ❓

Everything is empty because we never initialized it.

Then how do we give values?

This is exactly why Python introduced constructors.

Instead of:

rahul = Student()

we'll soon write:

rahul = Student("Rahul", 20, "Python")

Now Python immediately knows:

rahul
├── Name   → Rahul
├── Age    → 20
└── Course → Python
'''

# from now lets learn about the constructor.

'''
Imagine this situation.

Suppose I give you a blank student form.

Student Form

Name : __________

Age : __________

Course : __________

It's empty.

Now Rahul comes and fills it.

Student Form

Name : Rahul

Age : 20

Course : Python

Now Priya comes.

Student Form

Name : Priya

Age : 21

Course : Java

Notice something.

The form never changes.

Only the values change.

Now think about Python.

We have:

rahul = Student()

But we never gave Rahul's information.

Wouldn't it be better if we could write:

rahul = Student("Rahul", 20, "Python")

so that at the moment the object is created, Python also receives all the required information?

🤔

'''






'''
Think about what happens.

When Python sees:

rahul = Student("Rahul", 20, "Python")

Python thinks:

"Okay, create a new Student object."

Then:

"Now I have three pieces of information."

Name   → Rahul
Age    → 20
Course → Python

Then Python stores them inside the object.

So after creation, the object looks like:

rahul
├── Name   → Rahul
├── Age    → 20
└── Course → Python

Exactly what you said.

But here's the next question...

How does Python know that:

"Rahul"

should go into Name?

How does Python know that:

20

should go into Age?

How does Python know that:

"Python"

should go into Course?

It doesn't.

We have to teach Python.

And that's exactly what a constructor does.

Meet the Constructor
'''


# class Student:

#     def __init__(self, name, age, course):
#         print(name)
#         print(age)
#         print(course)

'''
Don't panic. 😄

I'm not explaining it yet.

We're going to predict it.

'''


class Student:

    def __init__(self, name, age, course):
        print(name)
        print(age)
        print(course)

rahul = Student("Rahul", 20, "Python")



'''
Questions
1. Do you think __init__() is called automatically?

The correct answer is:

✅ Yes

This is the special behavior of __init__.

2. What do you think the output will be?

Rahul
20
Python

3. Do you see __init__() being called anywhere in the code?


We never wrote:

__init__()

or

Student.__init__()

Yet it still runs.

'''





'''
🤯 Here's the magic

When Python sees:

rahul = Student("Rahul", 20, "Python")

It secretly does something like this:

Step 1

Create an empty object.

rahul
├── ?
├── ?
└── ?
Step 2

Immediately call:

__init__(...)

and pass the values:

Rahul
20
Python

So internally, Python behaves as if it does this:

# Python does this automatically (conceptually)

rahul = Student()          # create object


rahul.__init__("Rahul", 20, "Python")

⚠️ Note: This is not the exact internal implementation, but it's the right mental model for understanding what's happening.

⭐ This is why it's called a Constructor.

It runs automatically when an object is created.

You never call it yourself.

Python calls it for you.

Think of buying a new phone 📱

When you buy a phone:

The company manufactures it.
During manufacturing, they automatically install the operating system.

You don't install Android before turning it on.

Similarly:

rahul = Student("Rahul", 20, "Python")

Python:

Creates the object.
Automatically initializes it.
🎯 First Golden Rule of OOP

__init__() is automatically called whenever an object is created.

Don't memorize it.

Remember the reasoning:

An object should receive its initial data as soon as it's created.

'''


class Student:

    def __init__(self):
        print("Constructor Called")

print("Before")

rahul = Student()

print("After")



'''
Questions
1. What is the output?      --Before    Constructor Called      After
2. Does "Before" print first?   yes
3. When exactly is __init__() called?   B
    A) Before the object is created
    B) Immediately after the object is created
    C) At the end of the program
'''




'''
Step-by-Step Execution
Step 1

Python reads the class.

class Student:
    ...

Nothing is printed.

Python simply remembers:

"Okay, there is a class called Student."

Step 2
print("Before")

Output:

Before
Step 3

Python reaches:

rahul = Student()

Now several things happen.

3.1

Python creates a new Student object.

rahul
3.2

Python immediately calls:

__init__()

Automatically.

So:

print("Constructor Called")

executes.

Output:

Constructor Called
Step 4

Python continues.

print("After")

Output:

After


Final Output
Before
Constructor Called
After
'''

